"""Tests for loop sheets and FAT/SAT template generation."""

from __future__ import annotations

from pathlib import Path

import pytest

from cst.commissioning.fat_sat import fat_template
from cst.commissioning.loop_sheets import generate_loop_sheets, loop_sheet
from cst.panel.io_list import IOPoint, load_io_list

EXAMPLE = Path(__file__).resolve().parents[2] / "data" / "examples" / "io_list_example.csv"


def test_ai_sheet_has_5_point_check() -> None:
    point = IOPoint("PT-401", "Discharge pressure", "AI", device="pressure transmitter")
    sheet = loop_sheet(point, project="Demo")
    for stim in ("4.0 mA", "12.0 mA", "20.0 mA"):
        assert stim in sheet
    assert "Shield landed at panel end only" in sheet
    assert "Sign-off" in sheet


def test_do_sheet_includes_force_removal() -> None:
    sheet = loop_sheet(IOPoint("Y1", "Valve solenoid", "DO"))
    assert "Remove force" in sheet
    assert "Shield" not in sheet  # discrete point — no shield pre-check


def test_sheets_generated_for_every_point() -> None:
    io_list = load_io_list(EXAMPLE)
    sheets = generate_loop_sheets(io_list, project="Demo")
    assert len(sheets) == 13
    assert "TE-405" in sheets and "decade box" in sheets["TE-405"]


def test_fat_template_summarizes_io() -> None:
    io_list = load_io_list(EXAMPLE)
    doc = fat_template(io_list, project="Demo", panel_id="CP-01", test_type="FAT")
    assert "# FAT Protocol — CP-01" in doc
    assert "DI: 5" in doc and "| DI | 5 |" in doc
    assert "SCCR" in doc  # nameplate verification item
    assert "E-stop" in doc


def test_fat_rejects_unknown_test_type() -> None:
    with pytest.raises(ValueError, match="FAT.*SAT"):
        fat_template(load_io_list(EXAMPLE), test_type="XAT")
