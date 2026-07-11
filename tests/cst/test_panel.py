"""Tests for the panel pipeline: I/O list, BOM, wire schedule, nameplates."""

from __future__ import annotations

from pathlib import Path

import pytest

from cst.panel.bom import bom_to_csv, generate_bom
from cst.panel.io_list import IOList, IOPoint, load_io_list
from cst.panel.nameplates import PanelNameplate, legend_plates
from cst.panel.wire_schedule import generate_wire_schedule

EXAMPLE = Path(__file__).resolve().parents[2] / "data" / "examples" / "io_list_example.csv"


@pytest.fixture
def example_list() -> IOList:
    return load_io_list(EXAMPLE)


# --- I/O list ---------------------------------------------------------------

def test_example_loads_and_validates_clean(example_list: IOList) -> None:
    assert len(example_list.points) == 13
    assert example_list.validate() == []
    assert example_list.counts_by_type() == {"DI": 5, "DO": 3, "AI": 3, "AO": 1, "RTD": 1}


def test_signal_defaults_by_type() -> None:
    p = IOPoint(tag="T1", description="d", io_type="ai")
    assert p.io_type == "AI" and p.signal == "4-20mA"


def test_validation_catches_duplicates_and_bad_types(tmp_path: Path) -> None:
    csv_file = tmp_path / "io.csv"
    csv_file.write_text(
        "tag,description,io_type,rack,slot,channel\n"
        "A1,thing,DI,0,1,0\n"
        "A1,thing again,DI,0,1,0\n"
        ",no tag,DX,,,\n",
        encoding="utf-8",
    )
    problems = load_io_list(csv_file).validate()
    text = "\n".join(problems)
    assert "duplicate tag: A1" in text
    assert "address conflict" in text
    assert "missing tag" in text and "unknown io_type 'DX'" in text


def test_column_map_remaps_headers(tmp_path: Path) -> None:
    csv_file = tmp_path / "io.csv"
    csv_file.write_text("Point Name,Desc,Type\nX1,valve,DI\n", encoding="utf-8")
    io_list = load_io_list(
        csv_file,
        column_map={"Point Name": "tag", "Desc": "description", "Type": "io_type"},
    )
    assert io_list.points[0].tag == "X1"
    assert io_list.validate() == []


def test_missing_file_raises() -> None:
    with pytest.raises(FileNotFoundError):
        load_io_list("/nonexistent/io.csv")


# --- BOM ---------------------------------------------------------------------

def test_bom_module_math(example_list: IOList) -> None:
    lines = {l["item"]: l for l in generate_bom(example_list)}
    # 5 DI * 1.2 = 6 ch -> one 16-ch module
    assert lines["DI modules"]["qty"] == 1
    # 3 AI * 1.2 = 3.6 -> 4 ch -> one 8-ch module
    assert lines["AI modules"]["qty"] == 1
    # terminals: DI 5*2 + DO 3*2 + AI 3*3 + AO 1*3 + RTD 1*4 = 32
    assert lines["field terminal blocks"]["qty"] == 32
    # shields: 3 AI + 1 AO + 1 RTD = 5
    assert lines["shield/ground terminals"]["qty"] == 5
    # no invented part numbers
    assert all(l["part_number"] == "" for l in lines.values())


def test_bom_spares_push_module_count() -> None:
    io_list = IOList([IOPoint(f"D{i}", "x", "DI") for i in range(14)])
    lines = {l["item"]: l for l in generate_bom(io_list, spare_fraction=0.20)}
    # 14 * 1.2 = 16.8 -> 17 ch -> two 16-ch modules
    assert lines["DI modules"]["qty"] == 2


def test_bom_interposing_relays_option(example_list: IOList) -> None:
    lines = {l["item"]: l for l in generate_bom(example_list, interposing_relays_for_do=True)}
    assert lines["interposing relays"]["qty"] == 3


def test_bom_csv_render(example_list: IOList) -> None:
    text = bom_to_csv(generate_bom(example_list))
    assert text.splitlines()[0] == "item,description,qty,part_number,basis"


# --- wire schedule -------------------------------------------------------------

def test_wire_schedule_conductor_counts(example_list: IOList) -> None:
    rows = generate_wire_schedule(example_list)
    # DI 5*2 + DO 3*2 + AI 3*3 + AO 1*3 + RTD 1*4 = 32 conductors
    assert len(rows) == 32
    assert rows[0]["wire_no"] == "XV-101-ZSO-+"
    assert rows[0]["terminal"] == "TB1-1"
    assert rows[-1]["terminal"] == "TB1-32"


def test_wire_schedule_analog_has_shield(example_list: IOList) -> None:
    shields = [r for r in rows_for(example_list, "PT-401")]
    assert any(r["wire_no"].endswith("-SH") for r in shields)


def rows_for(io_list: IOList, tag: str) -> list[dict[str, str]]:
    return [r for r in generate_wire_schedule(io_list) if r["wire_no"].startswith(tag)]


# --- nameplates ----------------------------------------------------------------

def test_legend_plates_flag_long_descriptions() -> None:
    io_list = IOList([
        IOPoint("OK1", "Short name", "DI"),
        IOPoint("LONG1", "This description is far too long for a legend plate", "DI"),
    ])
    entries = legend_plates(io_list)
    assert entries[0]["flag"] == ""
    assert "shorten" in entries[1]["flag"]


def test_panel_nameplate_renders_required_items() -> None:
    plate = PanelNameplate(
        manufacturer="Acme Controls", panel_id="CP-01",
        supply_voltage="480Y/277 V", phases=3, frequency_hz=60,
        full_load_amps=42, sccr_ka=65, diagram_number="E-1001",
        largest_motor_hp=25,
    )
    text = plate.render()
    for token in ("480Y/277", "3-PHASE", "42 A", "65 kA", "E-1001", "25 HP"):
        assert token in text
