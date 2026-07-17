"""FAT / SAT protocol template generator.

Builds a factory- or site-acceptance-test skeleton from the I/O list:
document control, visual/construction inspection (NFPA 79 / UL 508A
verification items), point-to-point summary keyed to the generated loop
sheets, functional test placeholders, punch list, and sign-off. The
functional-test section is a frame — project-specific sequences are yours
to fill in.
"""

from __future__ import annotations

from cst.panel.io_list import IOList

VISUAL_CHECKS = (
    "Panel construction matches approved drawings (layout, devices, ratings)",
    "Nameplate present and complete: supply V/ph/Hz, FLA, SCCR, diagram no.",
    "Disconnect operation, door interlock, lockable in OFF",
    "Wire numbers and terminal labels match the wire schedule",
    "PE bonding: sized per standard, no daisy-chains, continuity verified",
    "Segregation: power / control / analog routing per design",
    "Torque marks on power terminations",
    "Enclosure rating unbroken (unused openings sealed, gland plates fitted)",
)


def fat_template(
    io_list: IOList,
    project: str = "",
    panel_id: str = "",
    test_type: str = "FAT",
) -> str:
    """Render a FAT/SAT protocol skeleton as markdown."""
    if test_type not in ("FAT", "SAT"):
        raise ValueError(f"test_type must be 'FAT' or 'SAT', got {test_type!r}")
    io_list.raise_for_problems()
    counts = io_list.counts_by_type()
    total = sum(counts.values())

    lines = [
        f"# {test_type} Protocol — {panel_id or 'Panel'}",
        "",
        f"| Project | {project or '_______'} | Document rev | ___ |",
        "|---|---|---|---|",
        f"| Test type | {test_type} | Date | ___ |",
        f"| I/O count | {total} ({', '.join(f'{t}: {n}' for t, n in counts.items())}) | Location | ___ |",
        "",
        "## 1. References",
        "",
        "- [ ] Approved electrical drawings (rev ___)",
        "- [ ] I/O list (rev ___)",
        "- [ ] Wire/terminal schedule (rev ___)",
        "- [ ] Functional/sequence description (rev ___)",
        "",
        "## 2. Visual and construction inspection",
        "",
    ]
    lines += [f"- [ ] {item}" for item in VISUAL_CHECKS]
    lines += [
        "",
        "## 3. Point-to-point verification",
        "",
        "Execute the individual loop test sheets; record completion here.",
        "",
        "| I/O type | Points | Sheets complete | Punch items |",
        "|---|---|---|---|",
    ]
    lines += [f"| {t} | {n} |  /{n} |  |" for t, n in counts.items()]
    lines += [
        "",
        "## 4. Functional tests (project-specific)",
        "",
        "| # | Test | Reference | Result | Pass |",
        "|---|---|---|---|---|",
        "| 1 | E-stop / safety circuit function |  |  | ☐ |",
        "| 2 | Power-loss / recovery behavior |  |  | ☐ |",
        "| 3 | Sequence per functional description |  |  | ☐ |",
        "| 4 | Alarms and interlocks |  |  | ☐ |",
        "",
        "## 5. Punch list",
        "",
        "| # | Item | Category (A/B/C) | Owner | Closed |",
        "|---|---|---|---|---|",
        "|  |  |  |  |  |",
        "",
        "## 6. Sign-off",
        "",
        "| Role | Name | Signature | Date |",
        "|---|---|---|---|",
        "| Vendor |  |  |  |",
        "| Customer |  |  |  |",
        "",
    ]
    return "\n".join(lines)
