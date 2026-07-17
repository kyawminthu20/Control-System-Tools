"""Tests for the licensed-table loader (tmp_path + shipped samples)."""

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


def test_source_missing_provenance_key_rejected(tmp_path: Path) -> None:
    # 'source' present but incomplete used to pass silently (source_label showed '?').
    content = {"source": {"standard": "NEC (NFPA 70)", "table": "310.16"}, "data": []}
    (tmp_path / "bad.json").write_text(json.dumps(content), encoding="utf-8")
    with pytest.raises(ValueError, match="edition"):
        load_table("bad", tables_dir=tmp_path)


def test_nondict_source_rejected(tmp_path: Path) -> None:
    (tmp_path / "bad.json").write_text(
        json.dumps({"source": "NEC 2023", "data": []}), encoding="utf-8"
    )
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
    assert loaded.data[0]["ampacity_a"] == 25
    assert not loaded.is_sample


def test_nondict_row_rejected(tmp_path: Path) -> None:
    content = {"source": {"standard": "S", "edition": "1", "table": "T"}, "data": [42]}
    (tmp_path / "bad.json").write_text(json.dumps(content), encoding="utf-8")
    with pytest.raises(ValueError, match="row 0 must be an object"):
        load_table("bad", tables_dir=tmp_path)


def test_row_missing_schema_required_field_rejected(tmp_path: Path) -> None:
    # Known table -> rows validated against the committed schema's required keys.
    content = {
        "source": {"standard": "NEC (NFPA 70)", "edition": "2023", "table": "430.250"},
        "data": [{"hp": 5, "voltage": 460}],  # missing flc_a
    }
    (tmp_path / "motor_flc_nec_430_250.json").write_text(json.dumps(content), encoding="utf-8")
    with pytest.raises(ValueError, match="flc_a"):
        load_table("motor_flc_nec_430_250", tables_dir=tmp_path)


def test_sample_fallback_is_tagged(tmp_path: Path) -> None:
    sample_dir = tmp_path / "samples"
    sample_dir.mkdir()
    content = {"source": {"standard": "X", "edition": "1", "table": "T"}, "data": []}
    (sample_dir / "demo.json").write_text(json.dumps(content), encoding="utf-8")
    loaded = load_table("demo", tables_dir=tmp_path)
    assert loaded.is_sample
    assert "SAMPLE" in loaded.source_label


def test_user_file_wins_over_sample(tmp_path: Path) -> None:
    (tmp_path / "samples").mkdir()
    sample = {"source": {"standard": "S", "edition": "1", "table": "T"}, "data": [{"v": 1}]}
    user = {"source": {"standard": "U", "edition": "1", "table": "T"}, "data": [{"v": 2}]}
    (tmp_path / "samples" / "demo.json").write_text(json.dumps(sample), encoding="utf-8")
    (tmp_path / "demo.json").write_text(json.dumps(user), encoding="utf-8")
    loaded = load_table("demo", tables_dir=tmp_path)
    assert loaded.data[0]["v"] == 2 and not loaded.is_sample


def test_allow_sample_false_requires_user_data(tmp_path: Path) -> None:
    (tmp_path / "samples").mkdir()
    content = {"source": {"standard": "S", "edition": "1", "table": "T"}, "data": []}
    (tmp_path / "samples" / "demo.json").write_text(json.dumps(content), encoding="utf-8")
    with pytest.raises(TableDataMissingError):
        load_table("demo", tables_dir=tmp_path, allow_sample=False)


def test_shipped_samples_load() -> None:
    for name in ("ampacity_nec_310_16", "motor_flc_nec_430_250"):
        loaded = load_table(name)
        assert loaded.is_sample and loaded.data, name


def test_env_var_sets_default_user_dir(tmp_path: Path, monkeypatch) -> None:
    # Installed users point CST_TABLES_DIR at their licensed data — no checkout.
    content = {"source": {"standard": "NEC (NFPA 70)", "edition": "2023", "table": "310.16"},
               "data": [{"size_awg_kcmil": "12", "material": "cu", "ampacity_a": 25}]}
    (tmp_path / "ampacity_nec_310_16.json").write_text(json.dumps(content), encoding="utf-8")
    monkeypatch.setenv("CST_TABLES_DIR", str(tmp_path))
    loaded = load_table("ampacity_nec_310_16")  # no explicit tables_dir
    assert not loaded.is_sample
    assert loaded.data[0]["ampacity_a"] == 25
