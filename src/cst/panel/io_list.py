"""I/O list data model — the single source every panel/commissioning tool consumes.

Canonical CSV columns (header row required, case/space tolerant):

    tag, description, io_type, signal, device, location, cabinet,
    rack, slot, channel, notes

``io_type`` is one of DI, DO, AI, AO, RTD, TC. ``signal`` defaults by type
(DI/DO -> 24VDC, AI/AO -> 4-20mA) when blank. rack/slot/channel are optional
but must be unique as a triple when given.

This format is the suite's default; map your own export's columns with the
``column_map`` argument of :func:`load_io_list`.
"""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

IO_TYPES = ("DI", "DO", "AI", "AO", "RTD", "TC")


class IOListError(ValueError):
    """Raised when a generator is asked to work from an invalid I/O list.

    Carries the full :meth:`IOList.validate` problem list so callers (and the
    CLI) can report every defect, not just the first. Subclasses ``ValueError``
    so existing error handling keeps working.
    """

    def __init__(self, problems: list[str]) -> None:
        self.problems = list(problems)
        summary = "; ".join(self.problems)
        super().__init__(
            f"I/O list has {len(self.problems)} problem(s) — fix before generating: "
            f"{summary}"
        )

DEFAULT_SIGNALS = {
    "DI": "24VDC", "DO": "24VDC",
    "AI": "4-20mA", "AO": "4-20mA",
    "RTD": "RTD-3W", "TC": "TC-K",
}

CANONICAL_COLUMNS = (
    "tag", "description", "io_type", "signal", "device", "location",
    "cabinet", "rack", "slot", "channel", "notes",
)


@dataclass
class IOPoint:
    """One I/O point. Only tag/description/io_type are mandatory."""

    tag: str
    description: str
    io_type: str
    signal: str = ""
    device: str = ""
    location: str = ""
    cabinet: str = ""
    rack: str = ""
    slot: str = ""
    channel: str = ""
    notes: str = ""

    def __post_init__(self) -> None:
        self.io_type = self.io_type.strip().upper()
        if not self.signal:
            self.signal = DEFAULT_SIGNALS.get(self.io_type, "")

    @property
    def address(self) -> str:
        """Rack/slot/channel as a display string, empty if unassigned."""
        if self.rack == "" and self.slot == "" and self.channel == "":
            return ""
        return f"{self.rack}/{self.slot}/{self.channel}"

    @property
    def is_analog(self) -> bool:
        return self.io_type in ("AI", "AO", "RTD", "TC")


@dataclass
class IOList:
    """A validated collection of I/O points."""

    points: list[IOPoint] = field(default_factory=list)

    def counts_by_type(self) -> dict[str, int]:
        counts = Counter(p.io_type for p in self.points)
        return {t: counts.get(t, 0) for t in IO_TYPES if counts.get(t, 0)}

    def validate(self) -> list[str]:
        """Return a list of problems (empty = clean)."""
        problems: list[str] = []
        tags = Counter(p.tag for p in self.points)
        problems.extend(
            f"duplicate tag: {tag} ({n} occurrences)"
            for tag, n in tags.items() if n > 1
        )
        addresses = Counter(p.address for p in self.points if p.address)
        problems.extend(
            f"address conflict: rack/slot/channel {addr} assigned {n} times"
            for addr, n in addresses.items() if n > 1
        )
        for i, p in enumerate(self.points, start=2):  # row 1 is the header
            where = f"row {i} ({p.tag or 'no tag'})"
            if not p.tag:
                problems.append(f"{where}: missing tag")
            if not p.description:
                problems.append(f"{where}: missing description")
            if p.io_type not in IO_TYPES:
                problems.append(
                    f"{where}: unknown io_type {p.io_type!r} (expected {'/'.join(IO_TYPES)})"
                )
        return problems

    def raise_for_problems(self) -> None:
        """The generator seam: raise :class:`IOListError` if the list is invalid.

        Every artifact generator calls this before producing output so malformed
        or colliding source data cannot silently yield a wrong deliverable.
        """
        problems = self.validate()
        if problems:
            raise IOListError(problems)


def _normalize_header(name: str) -> str:
    return name.strip().lower().replace(" ", "_").replace("-", "_")


def load_io_list(
    csv_path: str | Path,
    column_map: dict[str, str] | None = None,
) -> IOList:
    """Load an I/O list CSV.

    ``column_map`` maps YOUR file's (normalized) header names to canonical
    ones, e.g. ``{"point_name": "tag", "type": "io_type"}``.
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"I/O list not found: {path}")
    remap = {_normalize_header(k): v for k, v in (column_map or {}).items()}

    points: list[IOPoint] = []
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError(f"{path} is empty — expected a header row")
        for raw in reader:
            row: dict[str, str] = {}
            for key, value in raw.items():
                if key is None:
                    continue
                canonical = remap.get(_normalize_header(key), _normalize_header(key))
                if canonical in CANONICAL_COLUMNS:
                    row[canonical] = (value or "").strip()
            if not any(row.values()):
                continue  # skip blank lines
            points.append(IOPoint(
                tag=row.get("tag", ""),
                description=row.get("description", ""),
                io_type=row.get("io_type", ""),
                signal=row.get("signal", ""),
                device=row.get("device", ""),
                location=row.get("location", ""),
                cabinet=row.get("cabinet", ""),
                rack=row.get("rack", ""),
                slot=row.get("slot", ""),
                channel=row.get("channel", ""),
                notes=row.get("notes", ""),
            ))
    return IOList(points)
