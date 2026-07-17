"""Loop test sheet generator — one markdown sheet per I/O point.

Test procedures follow standard instrument loop-check practice (ISA-style
5-point analog checks, actuate/verify discrete checks). Sheets include
wiring verification, as-found/as-left, and sign-off blocks.
"""

from __future__ import annotations

from cst.panel.io_list import IOList, IOPoint

# (stimulus, expected) rows per io_type
ANALOG_5PT = (("4.0 mA", "0 %"), ("8.0 mA", "25 %"), ("12.0 mA", "50 %"),
              ("16.0 mA", "75 %"), ("20.0 mA", "100 %"))


def _test_rows(point: IOPoint) -> list[tuple[str, str]]:
    if point.io_type == "AI":
        return [(f"Inject {mA} at field device terminals", f"HMI/PLC reads {pct} of range")
                for mA, pct in ANALOG_5PT]
    if point.io_type == "AO":
        return [(f"Command {pct} from PLC/HMI", f"Measure {mA} at field terminals")
                for mA, pct in ANALOG_5PT]
    if point.io_type == "DI":
        return [("Actuate field device / apply simulation", "PLC input ON; HMI state correct"),
                ("Release field device", "PLC input OFF; HMI state correct")]
    if point.io_type == "DO":
        return [("Force output ON from PLC", "Field device energizes"),
                ("Force output OFF", "Field device de-energizes"),
                ("Remove force", "Output returns to logic control")]
    if point.io_type == "RTD":
        return [("Substitute decade box at 0 % temperature", "Reading matches range low"),
                ("Substitute decade box at 50 %", "Reading matches mid-range"),
                ("Substitute decade box at 100 %", "Reading matches range high")]
    if point.io_type == "TC":
        return [("Inject mV for range low (TC calibrator)", "Reading matches range low"),
                ("Inject mV for mid-range", "Reading matches mid-range"),
                ("Inject mV for range high", "Reading matches range high")]
    raise ValueError(f"{point.tag}: no test procedure for io_type {point.io_type!r}")


def loop_sheet(point: IOPoint, project: str = "", loop_ref: str = "") -> str:
    """Render one loop test sheet as markdown."""
    rows = _test_rows(point)
    lines = [
        f"# Loop Test Sheet — {point.tag}",
        "",
        f"| Project | {project or '_______'} | Loop / drawing | {loop_ref or '_______'} |",
        "|---|---|---|---|",
        f"| Description | {point.description} | I/O type / signal | {point.io_type} / {point.signal} |",
        f"| Device | {point.device or '—'} | Address | {point.address or 'unassigned'} |",
        f"| Location | {point.location or '—'} | Cabinet | {point.cabinet or '—'} |",
        "",
        "## Pre-checks",
        "",
        "- [ ] Wiring per schedule (wire numbers, terminals, tightness)",
        "- [ ] Shield landed at panel end only (analog)" if point.is_analog
        else "- [ ] Device supply voltage verified",
        "- [ ] Instrument datasheet range matches configuration",
        "",
        "## Function test",
        "",
        "| Step | Stimulus | Expected | As-found | As-left | Pass |",
        "|---|---|---|---|---|---|",
    ]
    lines += [
        f"| {i} | {stim} | {exp} |  |  | ☐ |"
        for i, (stim, exp) in enumerate(rows, start=1)
    ]
    lines += [
        "",
        "## Sign-off",
        "",
        "| Role | Name | Signature | Date |",
        "|---|---|---|---|",
        "| Technician |  |  |  |",
        "| Witness |  |  |  |",
        "",
        f"Notes: {point.notes or ''}",
        "",
    ]
    return "\n".join(lines)


def generate_loop_sheets(io_list: IOList, project: str = "") -> dict[str, str]:
    """{tag: markdown} for every point in the list.

    Rejects invalid or colliding I/O first: duplicate tags would otherwise
    collapse into one sheet (the dict is keyed by tag), silently losing points.
    """
    io_list.raise_for_problems()
    return {p.tag: loop_sheet(p, project=project) for p in io_list.points}
