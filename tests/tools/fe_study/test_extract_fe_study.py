import zipfile, io
from pathlib import Path


def _make_minimal_docx(path: Path) -> None:
    """Create a minimal valid DOCX at the given path."""
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body><w:p><w:r><w:t>Test doc content.</w:t></w:r></w:p></w:body>'
        '</w:document>'
    )
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("word/document.xml", xml)
    path.write_bytes(buf.getvalue())


def _make_record(source_root: Path, source_path: Path) -> dict:
    """Build a minimal manifest record for a .doc source file."""
    from tools.fe_study.common import (
        source_id_for_path, infer_family, infer_priority, work_output_path
    )
    family = infer_family(source_path)
    return {
        "source_id": source_id_for_path(source_root, source_path),
        "source_path": str(source_path),
        "source_name": source_path.name,
        "extension": ".doc",
        "family": family,
        "priority": infer_priority(family),
        "extract_mode": "docx_text",
        "ocr_required": "no",
        "text_layer_present": "n/a",
        "page_count_est": "1",
        "docx_text_chars": "20",
        "docx_image_count": "0",
        "raw_output_path": str(work_output_path(source_root, "extracted_raw", source_path, ".txt")),
        "clean_output_path": str(work_output_path(source_root, "extracted_clean", source_path, ".md")),
        "summary_output_path": str(work_output_path(source_root, "summaries", source_path, ".md")),
        "chunk_output_path": str(work_output_path(source_root, "chunks", source_path, ".jsonl")),
        "status": "pending",
        "quality_score": "",
        "manual_review": "no",
        "notes": "",
        "last_processed_at": "",
    }


def test_extract_doc_uses_cached_docx(tmp_path):
    """When cached .docx exists, extraction succeeds using it directly."""
    from tools.fe_study.common import converted_docx_path, ensure_workdirs
    from tools.fe_study.extract_fe_study import extract_docx

    source_root = tmp_path / "FE_Study"
    source_root.mkdir()
    ensure_workdirs(source_root)

    doc_file = source_root / "How to" / "Guide.doc"
    doc_file.parent.mkdir(parents=True)
    doc_file.touch()

    # Pre-create the cached .docx
    cached = converted_docx_path(source_root, doc_file)
    cached.parent.mkdir(parents=True, exist_ok=True)
    _make_minimal_docx(cached)

    record = _make_record(source_root, doc_file)
    notes = extract_docx(record, cached, export_media=False)
    assert record["status"] == "cleaned"


def test_extract_doc_reconverts_when_cache_missing(tmp_path, monkeypatch):
    """When cached .docx is absent, the pipeline re-converts on demand."""
    import shutil, subprocess
    from tools.fe_study.common import converted_docx_path, ensure_workdirs

    source_root = tmp_path / "FE_Study"
    source_root.mkdir()
    ensure_workdirs(source_root)

    doc_file = source_root / "How to" / "Guide.doc"
    doc_file.parent.mkdir(parents=True)
    doc_file.touch()

    cached = converted_docx_path(source_root, doc_file)

    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")

    def fake_run(*a, **kw):
        # Simulate soffice creating the .docx as a side effect
        cached.parent.mkdir(parents=True, exist_ok=True)
        _make_minimal_docx(cached)
        return type("R", (), {"returncode": 0})()

    monkeypatch.setattr(subprocess, "run", fake_run)

    record = _make_record(source_root, doc_file)

    # Simulate what main() does for a .doc record
    from tools.fe_study.common import convert_doc_to_docx
    from tools.fe_study.extract_fe_study import extract_docx

    converted = cached
    if not converted.exists():
        converted = convert_doc_to_docx(doc_file, cached.parent)
    if converted is not None and converted.exists():
        notes = extract_docx(record, converted, export_media=False)
    else:
        record["status"] = "needs_review"

    assert record["status"] == "cleaned"
