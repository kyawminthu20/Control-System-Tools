# `.doc` File Support Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `.doc` (Word 97-2003) support to the FE study extraction pipeline by converting files to `.docx` via LibreOffice headless, then reusing the existing DOCX profiling and extraction path.

**Architecture:** A new `_converted/` work directory caches `.docx` conversions produced by `soffice --headless`. Inventory converts each `.doc` once and stores the result. Extraction resolves the cached `.docx` (or re-converts on demand) and delegates to the existing `extract_docx` function. No changes to quality check, summarize, or manifest schema.

**Tech Stack:** Python 3.12, LibreOffice (`soffice`), `subprocess`, `pathlib`, existing `zipfile`/`xml.etree.ElementTree` DOCX pipeline.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `tools/fe_study/common.py` | Modify | Add `converted` workdir, `.doc` family/priority rules, `convert_doc_to_docx`, `converted_docx_path` |
| `tools/fe_study/inventory_fe_study.py` | Modify | Extend `scan_sources` for `.doc`; restructure `build_record` to `if/elif/else` |
| `tools/fe_study/extract_fe_study.py` | Modify | Add `.doc` branch to main extraction loop |
| `tests/tools/fe_study/test_common.py` | Modify | Tests for new helpers |
| `tests/tools/fe_study/test_inventory_fe_study.py` | Modify | Tests for `.doc` scan and build_record |
| `tests/tools/fe_study/test_extract_fe_study.py` | Modify | Tests for `.doc` extraction branch |

---

## Chunk 1: `common.py` helpers

### Task 1: `_converted` workdir entry

**Files:**
- Modify: `tools/fe_study/common.py:22-30`
- Test: `tests/tools/fe_study/test_common.py`

- [ ] **Step 1: Write failing test**

```python
def test_work_dirs_has_converted():
    from tools.fe_study.common import WORK_DIRS
    assert "converted" in WORK_DIRS
    assert WORK_DIRS["converted"] == "_converted"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_work_dirs_has_converted -v
```

Expected: FAIL — `AssertionError` (key not in dict)

- [ ] **Step 3: Add to `WORK_DIRS` in `common.py`**

In `common.py`, add `"converted": "_converted"` to the `WORK_DIRS` dict (after `"samples"`):

```python
WORK_DIRS = {
    "inventory": "_inventory",
    "logs": "_logs",
    "extracted_raw": "_extracted/raw",
    "extracted_clean": "_extracted/clean",
    "chunks": "_chunks",
    "summaries": "_summaries",
    "samples": "_samples",
    "converted": "_converted",
}
```

- [ ] **Step 4: Run test to verify it passes**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_work_dirs_has_converted -v
```

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/fe_study/common.py tests/tools/fe_study/test_common.py
git commit -m "feat(fe_study): add _converted workdir to WORK_DIRS"
```

---

### Task 2: `infer_family` and `infer_priority` for `.doc`

**Files:**
- Modify: `tools/fe_study/common.py:138-166`
- Test: `tests/tools/fe_study/test_common.py`

- [ ] **Step 1: Write failing tests**

```python
def test_infer_family_doc():
    from tools.fe_study.common import infer_family
    from pathlib import Path
    assert infer_family(Path("planning/FE_Study/How to/SomePLC.doc")) == "howto_doc"

def test_infer_priority_howto_doc():
    from tools.fe_study.common import infer_priority
    assert infer_priority("howto_doc") == "P2"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_infer_family_doc tests/tools/fe_study/test_common.py::test_infer_priority_howto_doc -v
```

Expected: FAIL — both return wrong values

- [ ] **Step 3: Add rules to `common.py`**

In `infer_family`, add before the final `return "other"`:

```python
    if path.suffix.lower() == ".doc":
        return "howto_doc"
```

In `infer_priority`, add before the final `return "P4"`:

```python
    if family == "howto_doc":
        return "P2"
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_infer_family_doc tests/tools/fe_study/test_common.py::test_infer_priority_howto_doc -v
```

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/fe_study/common.py tests/tools/fe_study/test_common.py
git commit -m "feat(fe_study): add howto_doc family and P2 priority for .doc files"
```

---

### Task 3: `convert_doc_to_docx` helper

**Files:**
- Modify: `tools/fe_study/common.py`
- Test: `tests/tools/fe_study/test_common.py`

- [ ] **Step 1: Write failing tests**

```python
def test_convert_doc_to_docx_no_soffice(tmp_path, monkeypatch):
    """Returns None when soffice is not on PATH."""
    import shutil
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: None)
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None

def test_convert_doc_to_docx_nonzero_exit(tmp_path, monkeypatch):
    """Returns None when soffice exits non-zero."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    monkeypatch.setattr(
        subprocess, "run",
        lambda *a, **kw: type("R", (), {"returncode": 1})(),
    )
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None

def test_convert_doc_to_docx_timeout(tmp_path, monkeypatch):
    """Returns None on TimeoutExpired."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    def raise_timeout(*a, **kw):
        raise subprocess.TimeoutExpired(cmd="soffice", timeout=60)
    monkeypatch.setattr(subprocess, "run", raise_timeout)
    result = convert_doc_to_docx(tmp_path / "fake.doc", tmp_path / "out")
    assert result is None

def test_convert_doc_to_docx_success(tmp_path, monkeypatch):
    """Returns .docx path when conversion succeeds and file exists."""
    import shutil, subprocess
    from tools.fe_study.common import convert_doc_to_docx
    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    docx_path = out_dir / "fake.docx"
    docx_path.touch()
    monkeypatch.setattr(
        subprocess, "run",
        lambda *a, **kw: type("R", (), {"returncode": 0})(),
    )
    result = convert_doc_to_docx(tmp_path / "fake.doc", out_dir)
    assert result == docx_path
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py -k "convert_doc" -v
```

Expected: FAIL — `ImportError: cannot import name 'convert_doc_to_docx'`

- [ ] **Step 3: Add `convert_doc_to_docx` to `common.py`**

Add after `page_count_for_pdf`:

```python
def convert_doc_to_docx(path: Path, target_dir: Path) -> Path | None:
    """Convert a legacy .doc file to .docx using LibreOffice headless.

    Returns the path to the converted .docx, or None if conversion fails or
    LibreOffice is not installed.
    """
    if not shutil.which("soffice"):
        return None
    target_dir.mkdir(parents=True, exist_ok=True)
    try:
        proc = subprocess.run(
            [
                "soffice",
                "--headless",
                "--convert-to", "docx",
                "--outdir", str(target_dir),
                str(path),
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        return None
    if proc.returncode != 0:
        return None
    converted = target_dir / (path.stem + ".docx")
    return converted if converted.exists() else None
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py -k "convert_doc" -v
```

Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add tools/fe_study/common.py tests/tools/fe_study/test_common.py
git commit -m "feat(fe_study): add convert_doc_to_docx helper"
```

---

### Task 4: `converted_docx_path` helper

**Files:**
- Modify: `tools/fe_study/common.py`
- Test: `tests/tools/fe_study/test_common.py`

- [ ] **Step 1: Write failing test**

```python
def test_converted_docx_path(tmp_path):
    from tools.fe_study.common import converted_docx_path
    source_root = tmp_path / "FE_Study"
    source_path = source_root / "How to" / "PLC Guide.doc"
    result = converted_docx_path(source_root, source_path)
    assert result == source_root / "_converted" / "How to" / "PLC Guide.docx"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_converted_docx_path -v
```

Expected: FAIL — `ImportError`

- [ ] **Step 3: Add `converted_docx_path` to `common.py`**

Add immediately after `convert_doc_to_docx`:

```python
def converted_docx_path(source_root: Path, source_path: Path) -> Path:
    """Return the expected cached .docx path for a .doc source file."""
    return work_output_path(source_root, "converted", source_path, ".docx")
```

- [ ] **Step 4: Run test to verify it passes**

```bash
cd . && python -m pytest tests/tools/fe_study/test_common.py::test_converted_docx_path -v
```

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tools/fe_study/common.py tests/tools/fe_study/test_common.py
git commit -m "feat(fe_study): add converted_docx_path helper"
```

---

## Chunk 2: `inventory_fe_study.py`

### Task 5: `scan_sources` — add `.doc`, filter `~$` temp files

**Files:**
- Modify: `tools/fe_study/inventory_fe_study.py`
- Test: `tests/tools/fe_study/test_inventory_fe_study.py`

- [ ] **Step 1: Write failing tests**

```python
def test_scan_sources_includes_doc(tmp_path):
    from tools.fe_study.inventory_fe_study import scan_sources
    doc = tmp_path / "How to" / "Guide.doc"
    doc.parent.mkdir(parents=True)
    doc.touch()
    results = scan_sources(tmp_path)
    assert doc in results

def test_scan_sources_excludes_temp_doc(tmp_path):
    from tools.fe_study.inventory_fe_study import scan_sources
    temp = tmp_path / "How to" / "~$Guide.doc"
    temp.parent.mkdir(parents=True)
    temp.touch()
    results = scan_sources(tmp_path)
    assert temp not in results

def test_scan_sources_excludes_converted_dir(tmp_path):
    from tools.fe_study.inventory_fe_study import scan_sources
    converted = tmp_path / "_converted" / "foo.doc"
    converted.parent.mkdir(parents=True)
    converted.touch()
    results = scan_sources(tmp_path)
    assert converted not in results
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd . && python -m pytest tests/tools/fe_study/test_inventory_fe_study.py -k "scan_sources" -v
```

Expected: FAIL

- [ ] **Step 3: Update `scan_sources` in `inventory_fe_study.py`**

```python
def scan_sources(source_root: Path) -> list[Path]:
    ignore_dirs = {"_inventory", "_logs", "_extracted", "_chunks", "_summaries", "_samples", "_converted"}
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".pdf", ".docx", ".doc"}
        and not path.name.startswith("~$")
        and not any(part in ignore_dirs for part in path.relative_to(source_root).parts)
    )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd . && python -m pytest tests/tools/fe_study/test_inventory_fe_study.py -k "scan_sources" -v
```

Expected: PASS

- [ ] **Step 5: Add `convert_doc_to_docx`, `converted_docx_path` to imports in `inventory_fe_study.py`**

Find the existing `from tools.fe_study.common import (` block and add both names:

```python
from tools.fe_study.common import (
    ...
    convert_doc_to_docx,
    converted_docx_path,
    ...
)
```

- [ ] **Step 6: Commit**

```bash
git add tools/fe_study/inventory_fe_study.py tests/tools/fe_study/test_inventory_fe_study.py
git commit -m "feat(fe_study): extend scan_sources to include .doc, filter ~$ temp files"
```

---

### Task 6: `build_record` — `.doc` branch

**Files:**
- Modify: `tools/fe_study/inventory_fe_study.py`
- Test: `tests/tools/fe_study/test_inventory_fe_study.py`

- [ ] **Step 1: Write failing tests**

```python
import zipfile, io

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
    import shutil, subprocess
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd . && python -m pytest tests/tools/fe_study/test_inventory_fe_study.py -k "build_record_doc" -v
```

Expected: FAIL

- [ ] **Step 3: Restructure `build_record` in `inventory_fe_study.py`**

Find the existing `try` block inside `build_record` that contains `if path.suffix.lower() == ".pdf":` / `else:` (DOCX branch). Restructure it to `if/elif/else` by inserting the `.doc` branch between them:

```python
if path.suffix.lower() == ".pdf":
    # ... existing PDF branch — leave completely unchanged ...

elif path.suffix.lower() == ".doc":
    target_dir = work_output_path(source_root, "converted", path, ".docx").parent
    converted = convert_doc_to_docx(path, target_dir)
    if converted and converted.exists():
        profile = profile_docx(converted)
        record["page_count_est"] = str(profile.page_count_est)
        record["docx_text_chars"] = str(profile.text_chars)
        record["docx_image_count"] = str(profile.image_count)
        record["text_layer_present"] = "n/a"
        if profile.image_count and profile.text_chars < 500:
            record["extract_mode"] = "docx_image_ocr"
            record["ocr_required"] = "yes"
        else:
            record["extract_mode"] = "docx_text"
            record["ocr_required"] = "no"
    else:
        record["page_count_est"] = "0"
        record["docx_text_chars"] = "0"
        record["docx_image_count"] = "0"
        record["text_layer_present"] = "n/a"
        record["extract_mode"] = "needs_review"
        record["ocr_required"] = "unknown"
        record["status"] = "needs_review"
        record["quality_score"] = "low"
        record["manual_review"] = "yes"
        record["notes"] = "LibreOffice not available or .doc conversion failed."

else:
    # ... existing DOCX branch — leave completely unchanged ...
```

Also add `work_output_path` to the imports from `common` if not already present.

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd . && python -m pytest tests/tools/fe_study/test_inventory_fe_study.py -k "build_record_doc" -v
```

Expected: PASS

- [ ] **Step 5: Run all inventory tests to catch regressions**

```bash
cd . && python -m pytest tests/tools/fe_study/test_inventory_fe_study.py -v
```

Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add tools/fe_study/inventory_fe_study.py tests/tools/fe_study/test_inventory_fe_study.py
git commit -m "feat(fe_study): add .doc branch to build_record with LibreOffice conversion"
```

---

## Chunk 3: `extract_fe_study.py`

### Task 7: `.doc` extraction branch in `main()`

**Files:**
- Modify: `tools/fe_study/extract_fe_study.py`
- Test: `tests/tools/fe_study/test_extract_fe_study.py`

- [ ] **Step 1: Write failing tests**

```python
import zipfile, io

def _make_minimal_docx(path):
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


def _make_minimal_record(source_root, source_path, extension=".doc"):
    from tools.fe_study.common import (
        source_id_for_path, infer_family, infer_priority, work_output_path
    )
    from pathlib import Path
    rel = source_path.relative_to(source_root)
    return {
        "source_id": source_id_for_path(source_root, source_path),
        "source_path": str(source_path),
        "source_name": source_path.name,
        "extension": extension,
        "family": infer_family(source_path),
        "priority": infer_priority(infer_family(source_path)),
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


def test_extract_doc_uses_cached_docx(tmp_path, monkeypatch):
    """When cached .docx exists, extract_fe_study uses it directly."""
    from tools.fe_study.extract_fe_study import extract_docx
    from tools.fe_study.common import converted_docx_path, ensure_workdirs

    source_root = tmp_path / "FE_Study"
    source_root.mkdir()
    ensure_workdirs(source_root)

    doc_file = source_root / "How to" / "Guide.doc"
    doc_file.parent.mkdir(parents=True)
    doc_file.touch()

    # pre-create the cached .docx
    cached = converted_docx_path(source_root, doc_file)
    cached.parent.mkdir(parents=True, exist_ok=True)
    _make_minimal_docx(cached)

    record = _make_minimal_record(source_root, doc_file)

    # extract_docx should succeed using the cached .docx path
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

    # The cache is absent initially; simulate soffice creating it
    cached = converted_docx_path(source_root, doc_file)

    monkeypatch.setattr(shutil, "which", lambda _: "/usr/bin/soffice")

    def fake_run(*a, **kw):
        # soffice side-effect: create the converted file
        cached.parent.mkdir(parents=True, exist_ok=True)
        _make_minimal_docx(cached)
        return type("R", (), {"returncode": 0})()

    monkeypatch.setattr(subprocess, "run", fake_run)

    record = _make_minimal_record(source_root, doc_file)

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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd . && python -m pytest tests/tools/fe_study/test_extract_fe_study.py -k "doc" -v
```

Expected: FAIL

- [ ] **Step 3: Add `.doc` branch to `main()` in `extract_fe_study.py`**

Find the existing dispatch block in `main()`:

```python
        if record["extension"] == ".docx":
            notes = extract_docx(record, source_path, export_media=not args.no_export_media)
        else:
            notes = extract_pdf(record, source_path)
```

Replace with:

```python
        if record["extension"] == ".docx":
            notes = extract_docx(record, source_path, export_media=not args.no_export_media)
        elif record["extension"] == ".doc":
            converted: Path | None = converted_docx_path(source_root, source_path)
            if not converted.exists():
                converted = convert_doc_to_docx(source_path, converted.parent)
            if converted is not None and converted.exists():
                notes = extract_docx(record, converted, export_media=not args.no_export_media)
            else:
                record["status"] = "needs_review"
                record["quality_score"] = "low"
                record["manual_review"] = "yes"
                record["notes"] = "LibreOffice conversion failed at extraction time."
                notes = ["LibreOffice not available or conversion failed."]
        else:
            notes = extract_pdf(record, source_path)
```

Add `convert_doc_to_docx` and `converted_docx_path` to the `from tools.fe_study.common import (` block.

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd . && python -m pytest tests/tools/fe_study/test_extract_fe_study.py -k "doc" -v
```

Expected: PASS

- [ ] **Step 5: Run full test suite to catch regressions**

```bash
cd . && python -m pytest tests/tools/fe_study/ -v
```

Expected: all PASS

- [ ] **Step 6: Commit**

```bash
git add tools/fe_study/extract_fe_study.py tests/tools/fe_study/test_extract_fe_study.py
git commit -m "feat(fe_study): add .doc extraction branch — re-convert on cache miss"
```

---

## Chunk 4: Wrap-up

### Task 8: Update project state and validate

- [ ] **Step 1: Update `project_state/project_state.md`**

Add a note that `.doc` support (family `howto_doc`, priority `P2`) is implemented via LibreOffice headless conversion, with cached output in `_converted/`.

- [ ] **Step 2: Update `project_state/change_log.md`**

Add a dated entry:

```
## 2026-03-13
- feat(fe_study): .doc file support — LibreOffice headless conversion, howto_doc family, P2 priority
```

- [ ] **Step 3: Run full test suite one final time**

```bash
cd . && python -m pytest tests/tools/fe_study/ -v
```

Expected: all PASS

- [ ] **Step 4: Verify soffice is accessible**

```bash
soffice --version
```

Expected: `LibreOffice 26.x.x.x ...` (or similar)

- [ ] **Step 5: Commit project state updates**

```bash
git add project_state/project_state.md project_state/change_log.md
git commit -m "chore: update project state for .doc support milestone"
```
