"""Tests for tag database, Modbus map, and comms-helper degradation."""

from __future__ import annotations

from pathlib import Path

import pytest

from cst.panel.io_list import load_io_list
from cst.plc import comms
from cst.plc.address_map import modbus_map, modbus_map_to_csv
from cst.plc.tag_db import (
    Tag,
    TagDatabase,
    identifier_problems,
    sanitize_tag_name,
    tags_from_io_list,
)

EXAMPLE = Path(__file__).resolve().parents[2] / "data" / "examples" / "io_list_example.csv"


# --- identifiers / tag db -----------------------------------------------------

@pytest.mark.parametrize("name", ["Motor_1", "_internal", "XV_101_ZSO", "a"])
def test_legal_identifiers(name: str) -> None:
    assert identifier_problems(name) == []


@pytest.mark.parametrize("name", ["1st_motor", "bad-name", "double__under", "trail_", ""])
def test_illegal_identifiers(name: str) -> None:
    assert identifier_problems(name)


def test_sanitize_tag_name() -> None:
    assert sanitize_tag_name("XV-101-ZSO") == "XV_101_ZSO"
    assert sanitize_tag_name("101-PUMP") == "T_101_PUMP"
    assert sanitize_tag_name("a--b__c-") == "a_b_c"


def test_case_insensitive_duplicates_flagged() -> None:
    db = TagDatabase([Tag("Pump1", "BOOL"), Tag("PUMP1", "BOOL")])
    assert any("duplicate" in p for p in db.validate())


def test_unknown_datatype_flagged() -> None:
    db = TagDatabase([Tag("T1", "FLOAT64")])
    assert any("unknown datatype" in p for p in db.validate())


def test_tags_from_example_io_list() -> None:
    db = tags_from_io_list(load_io_list(EXAMPLE))
    assert db.validate() == []
    by_name = {t.name: t for t in db.tags}
    assert by_name["PT_401"].datatype == "REAL"
    assert by_name["XV_101_SOL"].datatype == "BOOL"
    assert by_name["XV_101_SOL"].io_type == "DO"
    assert by_name["PT_401"].io_type == "AI"
    assert by_name["PT_401"].address == "0/3/0"
    assert db.to_csv().splitlines()[0].startswith("name,datatype")


# --- Modbus map ---------------------------------------------------------------

def test_modbus_tables_and_widths() -> None:
    db = tags_from_io_list(load_io_list(EXAMPLE))
    rows = {r["tag"]: r for r in modbus_map(db)}
    assert rows["XV_101_ZSO"]["table"] == "discrete_input"      # DI status
    assert rows["XV_101_SOL"]["table"] == "coil"                # DO -> writable
    assert rows["YL_301"]["table"] == "coil"                    # DO without name hint
    assert rows["PT_401"]["table"] == "input_register"          # AI
    assert rows["FCV_404"]["table"] == "holding_register"       # AO -> writable analog
    assert rows["PT_401"]["registers"] == 2                     # REAL = 2 regs
    assert "word order" in rows["PT_401"]["note"]


def test_modbus_sequential_offsets_respect_width() -> None:
    db = TagDatabase([Tag("AI_1", "REAL"), Tag("AI_2", "REAL"), Tag("AI_3", "INT")])
    rows = modbus_map(db, writable_names=set())
    offsets = [r["protocol_offset"] for r in rows]
    assert offsets == [0, 2, 4]                                  # 2-wide REALs
    assert rows[0]["table_address"] == 30001
    assert modbus_map_to_csv(rows).splitlines()[0].startswith("tag,datatype")


def test_explicit_writable_set_overrides_heuristic() -> None:
    db = TagDatabase([Tag("STATUS_WORD", "INT")])
    rows = modbus_map(db, writable_names={"STATUS_WORD"})
    assert rows[0]["table"] == "holding_register"


def test_io_direction_overrides_misleading_name_heuristic() -> None:
    db = TagDatabase([
        Tag("PUMP_CMD_FEEDBACK", "BOOL", io_type="DI"),
        Tag("PLAIN_OUTPUT", "BOOL", io_type="DO"),
        Tag("SP_MONITOR", "REAL", io_type="AI"),
        Tag("PLAIN_SETPOINT", "REAL", io_type="AO"),
    ])
    rows = {r["tag"]: r for r in modbus_map(db)}
    assert rows["PUMP_CMD_FEEDBACK"]["table"] == "discrete_input"
    assert rows["PLAIN_OUTPUT"]["table"] == "coil"
    assert rows["SP_MONITOR"]["table"] == "input_register"
    assert rows["PLAIN_SETPOINT"]["table"] == "holding_register"


# --- comms (pycomm3 optional) ---------------------------------------------------

def test_comms_degrades_without_pycomm3(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(comms, "LogixDriver", None)
    with pytest.raises(RuntimeError, match="uv sync --extra plc"):
        comms.read_tags("192.168.1.10/1", ["AnyTag"])


def test_verify_tags_reports_mismatches(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        comms, "read_tags", lambda path, names: {"A": 1, "B": None}
    )
    mismatches = comms.verify_tags("x", {"A": 1, "B": 2})
    assert mismatches == [("B", 2, None)]
