"""BOM generator — structural bill of materials derived from an I/O list.

Derives quantities by engineering rules (module channel counts with spare
capacity, terminal blocks per point by signal type, optional interposing
relays for outputs). Descriptions are GENERIC — part numbers are a blank
column for you to fill from your preferred vendor; this tool does not invent
catalog numbers.

Defaults are common practice and fully parameterized:
- Module densities: DI/DO 16-ch, AI/AO 8-ch, RTD/TC 8-ch
- Spare I/O capacity: 20 % (typical spec requirement — check your project spec)
- Terminals per point: DI/DO 2, AI/AO 3 (incl. shield land), RTD 4, TC 3
"""

from __future__ import annotations

import csv
import io
import math

from cst.panel.io_list import IOList

DEFAULT_MODULE_DENSITY = {"DI": 16, "DO": 16, "AI": 8, "AO": 8, "RTD": 8, "TC": 8}
DEFAULT_TERMINALS_PER_POINT = {"DI": 2, "DO": 2, "AI": 3, "AO": 3, "RTD": 4, "TC": 3}

MODULE_DESCRIPTION = {
    "DI": "digital input module, 24 VDC",
    "DO": "digital output module, 24 VDC",
    "AI": "analog input module, 4-20 mA",
    "AO": "analog output module, 4-20 mA",
    "RTD": "RTD input module",
    "TC": "thermocouple input module",
}


def generate_bom(
    io_list: IOList,
    spare_fraction: float = 0.20,
    module_density: dict[str, int] | None = None,
    terminals_per_point: dict[str, int] | None = None,
    interposing_relays_for_do: bool = False,
) -> list[dict[str, str | int]]:
    """Return BOM lines: {item, description, qty, part_number(blank), basis}."""
    io_list.raise_for_problems()
    if not 0 <= spare_fraction < 1:
        raise ValueError(f"spare_fraction must be in [0, 1), got {spare_fraction}")
    density = {**DEFAULT_MODULE_DENSITY, **(module_density or {})}
    terminals = {**DEFAULT_TERMINALS_PER_POINT, **(terminals_per_point or {})}

    counts = io_list.counts_by_type()
    lines: list[dict[str, str | int]] = []

    for io_type, count in counts.items():
        required = math.ceil(count * (1 + spare_fraction))
        modules = math.ceil(required / density[io_type])
        lines.append({
            "item": f"{io_type} modules",
            "description": f"{density[io_type]}-channel {MODULE_DESCRIPTION[io_type]}",
            "qty": modules,
            "part_number": "",
            "basis": f"{count} points + {spare_fraction:.0%} spares = {required} ch "
                     f"@ {density[io_type]}/module",
        })

    tb_total = sum(counts[t] * terminals[t] for t in counts)
    if tb_total:
        lines.append({
            "item": "field terminal blocks",
            "description": "feed-through terminal block (screw or spring per spec)",
            "qty": tb_total,
            "part_number": "",
            "basis": "per-point terminal counts: "
                     + ", ".join(f"{t}x{terminals[t]}" for t in counts),
        })
        shielded = sum(counts.get(t, 0) for t in ("AI", "AO", "RTD", "TC"))
        if shielded:
            lines.append({
                "item": "shield/ground terminals",
                "description": "shield landing terminal, grounded",
                "qty": shielded,
                "part_number": "",
                "basis": f"{shielded} shielded analog points",
            })

    if interposing_relays_for_do and counts.get("DO"):
        lines.append({
            "item": "interposing relays",
            "description": "slim interface relay, 24 VDC coil, with socket",
            "qty": counts["DO"],
            "part_number": "",
            "basis": "one per DO point (interposing option enabled)",
        })

    return lines


def bom_to_csv(lines: list[dict[str, str | int]]) -> str:
    """Render BOM lines as CSV text (part_number column left for the user)."""
    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer, fieldnames=["item", "description", "qty", "part_number", "basis"]
    )
    writer.writeheader()
    writer.writerows(lines)
    return buffer.getvalue()
