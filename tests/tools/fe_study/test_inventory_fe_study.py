"""Tests for inventory_fe_study.py."""

import io
import zipfile
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


def _make_minimal_docx(path):
    """Create a minimal valid DOCX at the given path."""
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body><w:p><w:r><w:t>Hello world from a .doc file.</w:t></w:r></w:p></w:body>'
        '</w:document>'
    )
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("word/document.xml", xml)
    path.write_bytes(buf.getvalue())


def test_build_record_doc_conversion_success(tmp_path, monkeypatch):
    """build_record for a .doc file marks extract_mode=docx_text when conversion succeeds."""
    import shutil
    import subprocess
    from tools.fe_study.inventory_fe_study import build_record

    source_root = tmp_path / "FE_Study"
    source_root.mkdir()
    how_to = source_root / "How to"
    how_to.mkdir()
    doc_file = how_to / "Guide.doc"
    doc_file.touch()

    # Simulate successful soffice conversion by pre-creating the .docx
    converted_dir = source_root / "_converted" / "How to"
    converted_dir.mkdir(parents=True)
    converted_docx = converted_dir / "Guide.docx"
    _make_minimal_docx(converted_docx)

    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    monkeypatch.setattr(
        subprocess, "run",
        lambda *a, **kw: type("R", (), {"returncode": 0})(),
    )

    record = build_record(source_root, doc_file)
    assert record["extension"] == ".doc"
    assert record["family"] == "howto_doc"
    assert record["priority"] == "P2"
    assert record["extract_mode"] == "docx_text"
    assert record["ocr_required"] == "no"
    assert record["text_layer_present"] == "n/a"


def test_build_record_doc_conversion_failure(tmp_path, monkeypatch):
    """build_record for a .doc file marks needs_review when conversion fails."""
    import shutil
    from tools.fe_study.inventory_fe_study import build_record

    source_root = tmp_path / "FE_Study"
    source_root.mkdir()
    doc_file = source_root / "Guide.doc"
    doc_file.touch()

    monkeypatch.setattr(shutil, "which", lambda _: None)  # no soffice

    record = build_record(source_root, doc_file)
    assert record["extract_mode"] == "needs_review"
    assert record["status"] == "needs_review"
    assert record["manual_review"] == "yes"
