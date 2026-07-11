"""Tests for the licensed-table loader (uses tmp_path, never real data)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cst.common.tables import TableDataMissingError, load_table


def test_missing_table_raises_with_populate_instructions(tmp_path: Path) -> None:
    with pytest.raises(TableDataMissingError, match="licensed copy"):
        load_table("ampacity_nec_310_16", tables_dir=tmp_path)


def test_table_without_source_rejected(tmp_path: Path) -> None:
    (tmp_path / "bad.json").write_text(json.dumps({"data": []}), encoding="utf-8")
    with pytest.raises(ValueError, match="source"):
        load_table("bad", tables_dir=tmp_path)


def test_valid_table_round_trips(tmp_path: Path) -> None:
    content = {
        "source": {"standard": "NEC (NFPA 70)", "edition": "2023", "table": "310.16"},
        "data": [{"size_awg_kcmil": "12", "material": "cu",
                  "insulation_rating_c": 75, "ampacity_a": 25}],
    }
    (tmp_path / "ampacity.json").write_text(json.dumps(content), encoding="utf-8")
    loaded = load_table("ampacity", tables_dir=tmp_path)
    assert loaded["data"][0]["ampacity_a"] == 25
