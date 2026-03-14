"""Tests for inventory_fe_study.py."""

from pathlib import Path

from tools.fe_study.inventory_fe_study import scan_sources


def test_scan_sources_includes_doc(tmp_path):
    """Test that .doc files are included in scan results."""
    doc = tmp_path / "How to" / "Guide.doc"
    doc.parent.mkdir(parents=True)
    doc.touch()
    results = scan_sources(tmp_path)
    assert doc in results


def test_scan_sources_excludes_temp_doc(tmp_path):
    """Test that ~$ temp files are excluded from scan results."""
    temp = tmp_path / "How to" / "~$Guide.doc"
    temp.parent.mkdir(parents=True)
    temp.touch()
    results = scan_sources(tmp_path)
    assert temp not in results


def test_scan_sources_excludes_converted_dir(tmp_path):
    """Test that _converted directory is excluded from scan results."""
    converted = tmp_path / "_converted" / "foo.doc"
    converted.parent.mkdir(parents=True)
    converted.touch()
    results = scan_sources(tmp_path)
    assert converted not in results
