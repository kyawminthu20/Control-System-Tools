"""Loader for licensed standards table data.

Table VALUES from copyrighted standards (NEC ampacity Table 310.16, motor
full-load current Tables 430.248/430.250, UL 508A SB4.1, ...) are never
committed to this repository. Each user populates ``data/standards_tables/``
from their own licensed copies, following the JSON schemas committed in
``data/standards_tables/schemas/``. This module finds, validates (minimally),
and serves those files to the calculators.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TABLES_DIR = _REPO_ROOT / "data" / "standards_tables"


class TableDataMissingError(FileNotFoundError):
    """Raised when a required licensed table file has not been supplied."""


def load_table(name: str, tables_dir: Path | None = None) -> dict[str, Any]:
    """Load ``<tables_dir>/<name>.json`` and return its parsed content.

    Raises TableDataMissingError with populate-me instructions when the file
    is absent, and ValueError when the file exists but lacks the required
    provenance keys (``source`` and ``data``).
    """
    directory = tables_dir or DEFAULT_TABLES_DIR
    path = directory / f"{name}.json"
    if not path.exists():
        raise TableDataMissingError(
            f"Standards table {name!r} not found at {path}. Table values from "
            "licensed standards are not distributed with this repository — "
            "populate this file from your licensed copy using the schema in "
            f"{directory / 'schemas'} (see data/standards_tables/README.md)."
        )
    with path.open(encoding="utf-8") as fh:
        content = json.load(fh)
    missing = [key for key in ("source", "data") if key not in content]
    if missing:
        raise ValueError(
            f"Table file {path} is missing required key(s): {', '.join(missing)}. "
            "Every table file must record its 'source' (standard, edition, "
            "table number) alongside its 'data'."
        )
    return content
