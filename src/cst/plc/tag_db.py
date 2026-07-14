"""PLC tag database — model, validation, and generation from an I/O list.

Tag names are validated against IEC 61131-3 identifier rules (Cl. 6.1):
letters/digits/underscores, must not start with a digit, no consecutive
underscores, no trailing underscore; uniqueness is case-insensitive. Vendor
tools are often looser — passing these rules keeps tags portable across
platforms.
"""

from __future__ import annotations

import csv
import io
import re
from collections import Counter
from dataclasses import dataclass, field

from cst.panel.io_list import IOList

DATATYPES = ("BOOL", "INT", "DINT", "REAL", "STRING")

# Datatype conventionally used for each I/O type when generating tags.
IO_TYPE_DATATYPE = {
    "DI": "BOOL", "DO": "BOOL",
    "AI": "REAL", "AO": "REAL", "RTD": "REAL", "TC": "REAL",
}

_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def identifier_problems(name: str) -> list[str]:
    """IEC 61131-3 identifier rule violations for one tag name."""
    problems = []
    if not name:
        return ["empty tag name"]
    if not _IDENTIFIER_RE.match(name):
        problems.append(
            f"{name!r}: only letters/digits/underscores, must not start with a digit"
        )
    if "__" in name:
        problems.append(f"{name!r}: consecutive underscores not permitted")
    if name.endswith("_"):
        problems.append(f"{name!r}: trailing underscore not permitted")
    return problems


@dataclass
class Tag:
    """One PLC tag."""

    name: str
    datatype: str
    description: str = ""
    scope: str = "controller"
    address: str = ""
    initial_value: str = ""
    io_type: str = ""

    def __post_init__(self) -> None:
        self.datatype = self.datatype.strip().upper()
        self.io_type = self.io_type.strip().upper()


@dataclass
class TagDatabase:
    tags: list[Tag] = field(default_factory=list)

    def validate(self) -> list[str]:
        """IEC 61131-3 identifier violations, duplicates, unknown datatypes."""
        problems: list[str] = []
        lower_names = Counter(t.name.lower() for t in self.tags)
        problems.extend(
            f"duplicate tag (case-insensitive): {name} ({n} occurrences)"
            for name, n in lower_names.items() if n > 1
        )
        for tag in self.tags:
            problems.extend(identifier_problems(tag.name))
            if tag.datatype not in DATATYPES:
                problems.append(
                    f"{tag.name}: unknown datatype {tag.datatype!r} "
                    f"(expected {'/'.join(DATATYPES)})"
                )
        return problems

    def to_csv(self) -> str:
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer,
            fieldnames=[
                "name", "datatype", "description", "scope", "address",
                "initial_value", "io_type",
            ],
        )
        writer.writeheader()
        for t in self.tags:
            writer.writerow(vars(t))
        return buffer.getvalue()


def sanitize_tag_name(raw: str) -> str:
    """Convert a field tag like ``XV-101-ZSO`` to a legal identifier ``XV_101_ZSO``."""
    name = re.sub(r"[^A-Za-z0-9_]", "_", raw.strip())
    name = re.sub(r"_+", "_", name).strip("_")
    if name and name[0].isdigit():
        name = f"T_{name}"
    return name


def tags_from_io_list(io_list: IOList, prefix: str = "") -> TagDatabase:
    """Generate a tag per I/O point using the sanitized field tag as the name."""
    tags = []
    for p in io_list.points:
        name = sanitize_tag_name(f"{prefix}{p.tag}")
        tags.append(Tag(
            name=name,
            datatype=IO_TYPE_DATATYPE.get(p.io_type, "BOOL"),
            description=p.description,
            address=p.address,
            io_type=p.io_type,
        ))
    return TagDatabase(tags)
