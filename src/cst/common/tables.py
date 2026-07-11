"""Loader for licensed standards table data.

Table VALUES from copyrighted standards (NEC ampacity Table 310.16, motor
full-load current Tables 430.248/430.250, UL 508A SB4.1, ...) are never
committed to this repository. Each user populates ``data/standards_tables/``
from their own licensed copies, following the JSON schemas committed in
``data/standards_tables/schemas/``. This module finds, validates (minimally),
and serves those files to the calculators.

A small set of clearly-marked SAMPLE files ships in
``data/standards_tables/samples/`` so the calculators and tests run out of
the box. Sample data is for demonstration — every value must be verified
against a licensed copy before design use, and the loader tags results
loaded from samples so calculators surface a warning.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TABLES_DIR = _REPO_ROOT / "data" / "standards_tables"

SAMPLE_WARNING = (
    "Loaded SAMPLE table data — demonstration values only; verify against a "
    "licensed copy and populate data/standards_tables/ before design use"
)


class TableDataMissingError(FileNotFoundError):
    """Raised when a required licensed table file has not been supplied."""


@dataclass(frozen=True)
class LoadedTable:
    """A parsed table file plus its provenance."""

    name: str
    source: dict[str, Any]
    data: list[dict[str, Any]]
    is_sample: bool

    @property
    def source_label(self) -> str:
        src = self.source
        label = f"{src.get('standard', '?')} {src.get('edition', '')} Table {src.get('table', '?')}".strip()
        return f"{label} (SAMPLE data)" if self.is_sample else label


def _parse(path: Path, name: str, is_sample: bool) -> LoadedTable:
    with path.open(encoding="utf-8") as fh:
        content = json.load(fh)
    missing = [key for key in ("source", "data") if key not in content]
    if missing:
        raise ValueError(
            f"Table file {path} is missing required key(s): {', '.join(missing)}. "
            "Every table file must record its 'source' (standard, edition, "
            "table number) alongside its 'data'."
        )
    return LoadedTable(
        name=name, source=content["source"], data=content["data"], is_sample=is_sample
    )


def load_table(
    name: str,
    tables_dir: Path | None = None,
    allow_sample: bool = True,
) -> LoadedTable:
    """Load ``<tables_dir>/<name>.json``, falling back to ``samples/``.

    User-supplied files always win over samples. With ``allow_sample=False``
    (production/design use), a missing user file raises
    TableDataMissingError with populate-me instructions.
    """
    directory = tables_dir or DEFAULT_TABLES_DIR
    user_path = directory / f"{name}.json"
    if user_path.exists():
        return _parse(user_path, name, is_sample=False)
    sample_path = directory / "samples" / f"{name}.json"
    if allow_sample and sample_path.exists():
        return _parse(sample_path, name, is_sample=True)
    raise TableDataMissingError(
        f"Standards table {name!r} not found at {user_path}. Table values from "
        "licensed standards are not distributed with this repository — "
        "populate this file from your licensed copy using the schema in "
        f"{directory / 'schemas'} (see data/standards_tables/README.md)."
    )
