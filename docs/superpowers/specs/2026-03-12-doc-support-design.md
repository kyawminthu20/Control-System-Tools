# `.doc` File Support — Design Spec

**Date:** 2026-03-12
**Status:** Approved

---

## Goal

Add `.doc` (Word 97-2003 binary format) support to the FE study extraction pipeline. All `.doc` files live under `planning/FE_Study/How to/` and are operational/procedural documents (PLC guides, commissioning procedures, software how-tos).

---

## Scope

- Extend `scan_sources` to discover `.doc` files
- Filter out Word lock/temp files (`~$` prefix) from scanning
- Add `howto_doc` family and `P2` priority
- Convert `.doc` → `.docx` via LibreOffice headless, cache result in `_converted/`
- Reuse the existing DOCX profiling and extraction pipeline on the converted file
- No changes to quality check, summarize, or manifest schema

---

## Prerequisite

LibreOffice must be installed on the machine running the pipeline:

```bash
brew install --cask libreoffice
```

Verify: `soffice --version`

---

## Architecture

### Conversion strategy: cached

A new `_converted/` work directory is added to `WORK_DIRS`. During **inventory**, each `.doc` file is converted to `.docx` once and stored there, mirroring the source folder structure. During **extraction**, the cached `.docx` is resolved and passed to the existing `extract_docx` function. If the cached file is missing at extraction time, it is re-converted on demand.

LibreOffice runs once per source file (not once per pipeline stage).

### Data flow

```
.doc source file
    ↓ inventory: soffice --headless --convert-to docx
_converted/<rel_path>.docx  (cached)
    ↓ profile_docx()         (existing)
manifest row (extension=.doc, family=howto_doc, extract_mode=docx_text|docx_image_ocr)
    ↓ extract_docx()         (existing, operates on cached .docx)
_extracted/raw/  _extracted/clean/
    ↓ quality_check / summarize  (unchanged)
```

---

## File Changes

### `common.py`

**1. Add `"converted": "_converted"` to `WORK_DIRS`**

```python
WORK_DIRS = {
    ...
    "converted": "_converted",
}
```

**2. Add `infer_family` rule for `.doc`**

```python
if path.suffix.lower() == ".doc":
    return "howto_doc"
```

Place before the final `return "other"`.

**3. Add `infer_priority` rule for `howto_doc`**

```python
if family == "howto_doc":
    return "P2"
```

**4. Add `convert_doc_to_docx(path, target_dir) -> Path | None`**

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

**5. Add `converted_docx_path(source_root, source_path) -> Path`**

```python
def converted_docx_path(source_root: Path, source_path: Path) -> Path:
    """Return the expected cached .docx path for a .doc source file."""
    return work_output_path(source_root, "converted", source_path, ".docx")
```

---

### `inventory_fe_study.py`

**`scan_sources`** — add `.doc` to extensions, filter `~$` temp files:

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

**`build_record`** — restructure the existing `if/else` into `if/elif/else` inside the `try` block. The `.doc` branch must be inserted as a true `elif` between the PDF branch and the existing DOCX `else` — **not** as a standalone `if`:

```python
if path.suffix.lower() == ".pdf":
    # ... existing PDF branch (unchanged) ...
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
    # ... existing DOCX branch (unchanged) ...
```

Add `convert_doc_to_docx` and `converted_docx_path` to the imports from `common` alongside the existing imports.

---

### `extract_fe_study.py`

**`main()` loop** — add `.doc` branch:

```python
if record["extension"] == ".docx":
    notes = extract_docx(record, source_path, export_media=not args.no_export_media)
elif record["extension"] == ".doc":
    converted: Path | None = converted_docx_path(source_root, source_path)
    if not converted.exists():
        # Re-convert on demand if cache is missing
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

Add `convert_doc_to_docx` and `converted_docx_path` to the imports from `common`.

---

## Family & Priority

| Family | Trigger | Priority |
|---|---|---|
| `howto_doc` | `path.suffix.lower() == ".doc"` | `P2` |

---

## Edge Cases

| Case | Handling |
|---|---|
| `~$*.doc` temp/lock files | Filtered in `scan_sources` via `path.name.startswith("~$")` |
| LibreOffice not installed | `convert_doc_to_docx` returns `None`; row marked `needs_review` |
| Conversion produces no output | Same as above — `None` check on `converted.exists()` |
| `.doc` file name collides with sibling `.docx` | `converted_docx_path` mirrors the full relative path, so `foo/bar.doc` → `_converted/foo/bar.docx` — distinct from any `foo/bar.docx` source because source and converted live in different trees |

---

## No-Change Surfaces

- `MANIFEST_FIELDS` — unchanged; `.doc` records use the same fields as `.docx`
- `quality_check_fe_study.py` — operates on clean markdown output, format-agnostic
- `summarize_fe_study.py` — same
- Jekyll site layer — unchanged
