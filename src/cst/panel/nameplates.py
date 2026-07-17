"""Nameplate and legend-plate generator.

Two outputs:

1. Legend-plate list — one engraving entry per I/O device (tag + trimmed
   description) for pushbuttons, pilot lights, and field devices.
2. Machine/panel nameplate content — the marking items NFPA 79 Chapter 19
   and UL 508A require on an industrial control panel: manufacturer, supply
   voltage / phases / frequency, full-load current, largest motor, SCCR,
   diagram number. This produces the CONTENT block; verify the exact item
   list against your listing requirements.
"""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass

from cst.common.cite import Citation
from cst.panel.io_list import IOList

CITATIONS = [
    Citation("NFPA 79:2024", "Chapter 19", "machine marking and documentation items"),
    Citation("UL 508A, 3rd Ed. (2018), rev. 2025-06-26", "marking requirements incl. SCCR (SB5)",
             "verify exact required items against the listing report"),
]


@dataclass(frozen=True)
class PanelNameplate:
    """Data for the main panel nameplate."""

    manufacturer: str
    panel_id: str
    supply_voltage: str          # e.g. "480Y/277 V"
    phases: int
    frequency_hz: int
    full_load_amps: float
    sccr_ka: float
    diagram_number: str
    largest_motor_hp: float | None = None

    def render(self) -> str:
        lines = [
            f"MANUFACTURER: {self.manufacturer}",
            f"PANEL: {self.panel_id}",
            f"SUPPLY: {self.supply_voltage}, {self.phases}-PHASE, {self.frequency_hz} Hz",
            f"FULL-LOAD CURRENT: {self.full_load_amps:g} A",
        ]
        if self.largest_motor_hp is not None:
            lines.append(f"LARGEST MOTOR: {self.largest_motor_hp:g} HP")
        lines += [
            f"SHORT-CIRCUIT CURRENT RATING: {self.sccr_ka:g} kA RMS SYM.",
            f"DIAGRAM: {self.diagram_number}",
        ]
        return "\n".join(lines)


def legend_plates(io_list: IOList, max_chars_per_line: int = 24) -> list[dict[str, str]]:
    """One engraving entry per point: line1 = tag, line2 = description.

    Descriptions longer than ``max_chars_per_line`` are flagged rather than
    silently truncated — engraving vendors charge per line and operators read
    these; shorten deliberately.
    """
    if max_chars_per_line < 8:
        raise ValueError(f"max_chars_per_line unreasonably small: {max_chars_per_line}")
    io_list.raise_for_problems()
    entries = []
    for p in io_list.points:
        flag = "" if len(p.description) <= max_chars_per_line else (
            f"OVER {max_chars_per_line} CHARS — shorten"
        )
        entries.append({
            "line1": p.tag,
            "line2": p.description.upper(),
            "flag": flag,
        })
    return entries


def legend_plates_to_csv(entries: list[dict[str, str]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["line1", "line2", "flag"])
    writer.writeheader()
    writer.writerows(entries)
    return buffer.getvalue()
