"""Live PLC communication helpers (pycomm3 — optional dependency).

Install with:  uv sync --extra plc   (or: pip install 'control-system-tools[plc]')

Thin, safe wrappers around pycomm3's LogixDriver for the common field tasks:
batch tag reads for commissioning verification and a read-back comparison
against expected values. WRITES are deliberately not wrapped — write to a
running controller through the vendor tool or your own reviewed script.
"""

from __future__ import annotations

from typing import Any

try:  # optional dependency — everything degrades to a clear error message
    from pycomm3 import LogixDriver  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised only without the extra
    LogixDriver = None


def _require_pycomm3() -> None:
    if LogixDriver is None:
        raise RuntimeError(
            "pycomm3 is not installed — install the optional extra: "
            "uv sync --extra plc"
        )


def read_tags(plc_path: str, tag_names: list[str]) -> dict[str, Any]:
    """Batch-read tags from a Logix controller. Returns {tag: value|None}.

    ``plc_path`` example: '192.168.1.10/1' (IP/slot).
    Unreadable tags map to None instead of raising, so a commissioning sweep
    completes and reports gaps.
    """
    _require_pycomm3()
    if not tag_names:
        return {}
    results: dict[str, Any] = {}
    with LogixDriver(plc_path) as plc:
        for response in plc.read(*tag_names):
            results[response.tag] = response.value if response else None
    return results


def verify_tags(
    plc_path: str, expected: dict[str, Any]
) -> list[tuple[str, Any, Any]]:
    """Read tags and return mismatches as (tag, expected, actual).

    Empty list means every tag read back as expected — useful as a scripted
    point-check during FAT/SAT.
    """
    actual = read_tags(plc_path, list(expected))
    return [
        (tag, want, actual.get(tag))
        for tag, want in expected.items()
        if actual.get(tag) != want
    ]
