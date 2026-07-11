"""Tests for the design-package assembler."""

from __future__ import annotations

from pathlib import Path

from cst.calc.voltage_drop import voltage_drop
from cst.docgen.design_package import DesignPackage
from cst.panel.io_list import load_io_list
from cst.panel.nameplates import PanelNameplate

EXAMPLE = Path(__file__).resolve().parents[2] / "data" / "examples" / "io_list_example.csv"


def test_full_package_assembly() -> None:
    io_list = load_io_list(EXAMPLE)
    package = DesignPackage(project="Demo Skid", panel_id="CP-01", prepared_by="KMT")
    package.add_io_summary(io_list)
    package.add_bom(io_list)
    package.add_wire_schedule(io_list, limit=5)
    package.add_calc(voltage_drop(20, 100, "12", 120))
    package.add_nameplate(PanelNameplate(
        manufacturer="Acme", panel_id="CP-01", supply_voltage="480 V",
        phases=3, frequency_hz=60, full_load_amps=42, sccr_ka=65,
        diagram_number="E-1001",
    ))
    package.add_section("Notes", "Free-form section body.")

    doc = package.render()
    assert doc.startswith("# Design Package — Demo Skid")
    assert "## Contents" in doc and "6. [Notes](#notes)" in doc
    assert "| TOTAL | 13 |" in doc
    assert "field terminal blocks" in doc
    assert "(27 more rows" in doc              # 32 wires, 5 shown
    assert "NEC 2023" in doc                   # calc citations carried through
    assert "SHORT-CIRCUIT CURRENT RATING: 65 kA" in doc
    assert "Validation: clean." in doc


def test_wire_schedule_no_limit() -> None:
    io_list = load_io_list(EXAMPLE)
    package = DesignPackage(project="X")
    package.add_wire_schedule(io_list, limit=None)
    assert "more rows" not in package.render()
