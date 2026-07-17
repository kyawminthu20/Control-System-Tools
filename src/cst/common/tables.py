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

import importlib.resources
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[3]
# Repo/editable-checkout location. In an installed wheel this path does not exist;
# resolution then falls back to data bundled inside the package (see _bundled_dir).
DEFAULT_TABLES_DIR = _REPO_ROOT / "data" / "standards_tables"

#: Environment variable pointing at a user's licensed-table directory (highest
#: priority for the default location, so installed users need no source checkout).
TABLES_DIR_ENV = "CST_TABLES_DIR"


def _bundled_dir() -> Path | None:
    """Samples + schemas shipped inside the wheel (``cst/_bundled_tables``)."""
    try:
        path = Path(str(importlib.resources.files("cst") / "_bundled_tables"))
    except (ModuleNotFoundError, TypeError):
        return None
    return path if path.exists() else None


def _default_tables_dir() -> Path:
    """Resolve the default table directory: env override, then checkout, then wheel."""
    env = os.environ.get(TABLES_DIR_ENV)
    if env:
        return Path(env)
    if DEFAULT_TABLES_DIR.exists():
        return DEFAULT_TABLES_DIR
    return _bundled_dir() or DEFAULT_TABLES_DIR


def _schema_dir() -> Path:
    """Directory holding the committed row schemas (checkout or bundled)."""
    if (DEFAULT_TABLES_DIR / "schemas").exists():
        return DEFAULT_TABLES_DIR / "schemas"
    bundled = _bundled_dir()
    if bundled and (bundled / "schemas").exists():
        return bundled / "schemas"
    return DEFAULT_TABLES_DIR / "schemas"

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


REQUIRED_SOURCE_KEYS = ("standard", "edition", "table")

# Table file name -> committed row schema (schemas/<value>.schema.json). Tables not
# listed here are still shape-checked (list of objects) but skip per-field key checks.
_SCHEMA_FOR = {
    "ampacity_nec_310_16": "ampacity",
    "motor_flc_nec_430_250": "motor_flc",
}


def _required_row_keys(name: str) -> tuple[str, ...]:
    """Required per-row keys for ``name``, read from its committed JSON schema.

    Returns an empty tuple when no schema is mapped or readable — validation then
    falls back to the structural (list-of-objects) check only.
    """
    schema_name = _SCHEMA_FOR.get(name)
    if schema_name is None:
        return ()
    schema_path = _schema_dir() / f"{schema_name}.schema.json"
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        required = schema["properties"]["data"]["items"]["required"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        return ()
    return tuple(required) if isinstance(required, list) else ()


def _validate_rows(path: Path, name: str, data: Any) -> None:
    if not isinstance(data, list):
        raise ValueError(
            f"Table file {path}: 'data' must be a list of row objects, "
            f"got {type(data).__name__}."
        )
    required = _required_row_keys(name)
    for index, row in enumerate(data):
        if not isinstance(row, dict):
            raise ValueError(
                f"Table file {path}: data row {index} must be an object, "
                f"got {type(row).__name__}."
            )
        missing = [key for key in required if key not in row]
        if missing:
            raise ValueError(
                f"Table file {path}: data row {index} is missing required "
                f"field(s): {', '.join(missing)} (per schema for {name!r})."
            )


def _parse(path: Path, name: str, is_sample: bool) -> LoadedTable:
    with path.open(encoding="utf-8") as fh:
        content = json.load(fh)
    if not isinstance(content, dict):
        raise ValueError(f"Table file {path} must be a JSON object, got {type(content).__name__}.")
    missing = [key for key in ("source", "data") if key not in content]
    if missing:
        raise ValueError(
            f"Table file {path} is missing required key(s): {', '.join(missing)}. "
            "Every table file must record its 'source' (standard, edition, "
            "table number) alongside its 'data'."
        )
    source, data = content["source"], content["data"]
    if not isinstance(source, dict):
        raise ValueError(
            f"Table file {path}: 'source' must be an object recording provenance "
            f"(standard, edition, table), got {type(source).__name__}."
        )
    missing_prov = [
        key for key in REQUIRED_SOURCE_KEYS
        if not str(source.get(key, "")).strip()
    ]
    if missing_prov:
        raise ValueError(
            f"Table file {path}: 'source' is missing provenance field(s): "
            f"{', '.join(missing_prov)}. Every table file must record which "
            "standard, edition, and table its values came from."
        )
    _validate_rows(path, name, data)
    return LoadedTable(name=name, source=source, data=data, is_sample=is_sample)


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
    directory = tables_dir if tables_dir is not None else _default_tables_dir()
    user_path = directory / f"{name}.json"
    if user_path.exists():
        return _parse(user_path, name, is_sample=False)
    sample_path = directory / "samples" / f"{name}.json"
    if allow_sample and sample_path.exists():
        return _parse(sample_path, name, is_sample=True)
    # When resolving the default location (e.g. CST_TABLES_DIR points at a user
    # dir with no samples), fall back to the samples bundled in the package.
    if allow_sample and tables_dir is None:
        bundled = _bundled_dir()
        if bundled and bundled != directory:
            bundled_sample = bundled / "samples" / f"{name}.json"
            if bundled_sample.exists():
                return _parse(bundled_sample, name, is_sample=True)
    raise TableDataMissingError(
        f"Standards table {name!r} not found at {user_path}. Table values from "
        "licensed standards are not distributed with this repository — "
        "populate this file from your licensed copy using the schema in "
        f"{directory / 'schemas'} (see data/standards_tables/README.md)."
    )
