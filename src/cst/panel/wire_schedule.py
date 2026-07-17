"""Wire/terminal schedule generator.

Produces one row per conductor from the I/O list. Wire numbers follow the
tag-suffix convention (wire number = point tag + conductor suffix), the most
traceable scheme for machine panels. Conductor sets and default colors by
signal class follow NFPA 79 Chapter 16 wiring-identification practice
(colors are parameterized — verify against your project spec):

    24 VDC control      blue
    120 VAC control     red
    analog signal       shielded pair (e.g. black/white in shield)
    grounded conductor  white (AC) / white-blue (DC)
"""

from __future__ import annotations

import csv
import io

from cst.common.cite import Citation
from cst.panel.io_list import IOList

CITATION = Citation(
    "NFPA 79:2024", "Chapter 16",
    "conductor identification and color conventions (verify project spec)",
)

# Conductor set per point: (suffix, function, default color)
CONDUCTOR_SETS = {
    "DI": (("+", "24 VDC supply to device", "blue"),
           ("S", "signal return to input channel", "blue")),
    "DO": (("S", "switched 24 VDC from output channel", "blue"),
           ("-", "0 VDC return", "blue-white")),
    "AI": (("+", "4-20 mA loop +", "shielded pair"),
           ("-", "4-20 mA loop -", "shielded pair"),
           ("SH", "shield — ground at panel end only", "drain")),
    "AO": (("+", "4-20 mA output +", "shielded pair"),
           ("-", "4-20 mA output -", "shielded pair"),
           ("SH", "shield — ground at panel end only", "drain")),
    "RTD": (("A", "RTD sense A", "shielded triad"),
            ("B", "RTD sense B", "shielded triad"),
            ("C", "RTD excitation", "shielded triad"),
            ("SH", "shield — ground at panel end only", "drain")),
    "TC": (("+", "thermocouple + (match TC extension type)", "TC extension"),
           ("-", "thermocouple - (match TC extension type)", "TC extension"),
           ("SH", "shield — ground at panel end only", "drain")),
}


def generate_wire_schedule(
    io_list: IOList,
    terminal_start: int = 1,
    strip_prefix: str = "TB1",
) -> list[dict[str, str]]:
    """Rows: wire_no, from, to (module address), terminal, function, color.

    Terminals are assigned sequentially on ``strip_prefix`` starting at
    ``terminal_start`` in I/O-list order — reorder the list to control layout.
    """
    io_list.raise_for_problems()
    if terminal_start < 1:
        raise ValueError(f"terminal_start must be >= 1, got {terminal_start}")
    rows: list[dict[str, str]] = []
    terminal = terminal_start
    for point in io_list.points:
        conductors = CONDUCTOR_SETS.get(point.io_type)
        if conductors is None:
            raise ValueError(
                f"{point.tag}: no conductor set for io_type {point.io_type!r}"
            )
        destination = point.address or "(unassigned)"
        for suffix, function, color in conductors:
            rows.append({
                "wire_no": f"{point.tag}-{suffix}",
                "from": f"{point.device or point.tag} ({point.location})".strip(),
                "to": f"{point.io_type} {destination}",
                "terminal": f"{strip_prefix}-{terminal}",
                "function": function,
                "color": color,
            })
            terminal += 1
    return rows


def wire_schedule_to_csv(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer, fieldnames=["wire_no", "from", "to", "terminal", "function", "color"]
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()
