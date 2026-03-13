# FE Study Tooling Bug Fixes — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix seven confirmed issues found in the second-pass code review of `tools/fe_study/`.

**Architecture:** All fixes are confined to `tools/fe_study/`. Three changes touch `common.py` internals (DOCX XML refactor, silent extractor diagnostics, JSONL encoding). Two are one-liner cleanups (ensure_ascii, docstring). Two are style fixes (blank lines). No public function signatures change except `extract_pdf_pages`, which gains an optional keyword argument with a default so callers are unaffected.

**Tech Stack:** Python 3.12, stdlib only (`zipfile`, `xml.etree`, `subprocess`, `csv`, `json`). No test framework — verification uses `python3 -m py_compile` and a CLI smoke test with `--source-root` pointing at a temp directory with dummy files.

---

## Issue Reference

| # | Severity | Issue | File |
|---|---|---|---|
| 1 | Bug | Double ZIP open — `profile_docx` opens ZIP then calls `extract_docx_pages` which opens it again | `common.py` |
| 2 | Bug | Double page extraction — `extract_docx` calls `profile_docx` (pages inside) then `extract_docx_pages` again | `extract_fe_study.py` |
| 3 | Bug | XPath `//w:p` now includes table-cell paragraphs — silent behavioral change, needs a deliberate decision | `common.py:225` |
| 4 | Bug | Silent `except Exception: pass` blocks in `extract_pdf_pages` — extractor failures are invisible | `common.py:306-318` |
| 5 | Data | `ensure_ascii=True` in `write_manifest_jsonl` escapes Σ, ∫, √ to `\uXXXX` | `common.py:395` |
| 6 | Mislead | `optional_pdf_extractors` docstring says "preference order" but `extract_pdf_pages` ignores list order | `common.py:271` |
| 7 | Style | Missing blank line after imports in two files | `quality_check_fe_study.py:28`, `summarize_fe_study.py:29` |

---

## File Map

| File | What changes |
|---|---|
| `tools/fe_study/common.py` | Issues 1, 3, 4, 5, 6 — DOCX refactor, XPath fix, diagnostics param, encoding, docstring |
| `tools/fe_study/extract_fe_study.py` | Issue 2 — use `profile.pages` instead of second `extract_docx_pages` call |
| `tools/fe_study/quality_check_fe_study.py` | Issue 7 — blank line |
| `tools/fe_study/summarize_fe_study.py` | Issue 7 — blank line |

---

## Chunk 1: DOCX XML Double-Read Fix (Issues 1, 2, 3)

**Root cause:** `profile_docx` opens the ZIP to read `word/document.xml`, then calls
`extract_docx_pages(path)` which opens the ZIP again via `_docx_document_xml`. The
extraction script then calls `extract_docx_pages` a second time even though `profile.pages`
already holds the result.

**Approach:**
1. Introduce `_extract_pages_from_xml(xml: str) -> list[str]` — the parsing logic extracted
   from `extract_docx_pages`, taking the already-read XML string.
2. `extract_docx_pages(path)` becomes a thin wrapper: read XML once, call the helper.
3. `profile_docx` reads the ZIP once, calls the helper directly — no second ZIP open.
4. `extract_docx` in `extract_fe_study.py` uses `profile.pages` instead of calling
   `extract_docx_pages` again.

**XPath decision (Issue 3):**
The change from `.//w:body/w:p` to `.//w:body//w:p` includes table-cell paragraphs.
For FE study content (handbooks, textbook modules with data tables), including table text
improves content coverage. **Recommendation: keep `//w:p`** but add a comment documenting
the intent. If you see duplicate text in practice, revert to `/w:p`.

---

### Task 1: Refactor `common.py` DOCX XML reading

**Files:**
- Modify: `tools/fe_study/common.py` — `_docx_document_xml`, `extract_docx_pages`, `profile_docx`

- [ ] **Step 1: Add internal XML-to-pages helper**

  In `common.py`, add a new private function immediately before `extract_docx_pages`:

  ```python
  def _extract_pages_from_xml(xml: str) -> list[str]:
      """Parse already-read WordprocessingML XML into rendered page strings."""
      root = ET.fromstring(xml)
      pages: list[list[str]] = [[]]
      page_index = 0

      # //w:p includes table-cell paragraphs intentionally — captures formula tables
      for para in root.findall(".//w:body//w:p", DOCX_NS):
          parts: list[str] = []
          for child in para.iter():
              tag = child.tag.rsplit("}", 1)[-1]
              if tag == "t" and child.text:
                  parts.append(child.text)
              elif tag == "tab":
                  parts.append("\t")
              elif tag in {"br", "cr"}:
                  parts.append("\n")
              elif tag == "lastRenderedPageBreak":
                  parts.append("\f")

          text = "".join(parts).strip()
          if not text:
              continue

          subparts = [item.strip() for item in text.split("\f")]
          for idx, item in enumerate(subparts):
              if item:
                  pages[page_index].append(item)
              if idx < len(subparts) - 1:
                  pages.append([])
                  page_index += 1

      return [
          "\n\n".join(page).strip()
          for page in pages
          if any(line.strip() for line in page)
      ]
  ```

- [ ] **Step 2: Simplify `extract_docx_pages` to delegate to the helper**

  Replace the body of `extract_docx_pages`:

  ```python
  def extract_docx_pages(path: Path) -> list[str]:
      """Extract text from a DOCX file while preserving rendered page breaks."""
      return _extract_pages_from_xml(_docx_document_xml(path))
  ```

- [ ] **Step 3: Refactor `profile_docx` to open the ZIP exactly once**

  Replace `profile_docx`:

  ```python
  def profile_docx(path: Path) -> DocxProfile:
      """Estimate page count and content profile for a DOCX source."""
      with zipfile.ZipFile(path) as archive:
          xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
          image_count = sum(
              1
              for member in archive.namelist()
              if member.startswith("word/media/") and not member.endswith("/")
          )
      root = ET.fromstring(xml)
      text_chars = sum(len(node.text or "") for node in root.findall(".//w:t", DOCX_NS))
      pages = _extract_pages_from_xml(xml)
      page_count_est = len(pages) if pages else max(xml.count("lastRenderedPageBreak") + 1, 1)
      return DocxProfile(
          page_count_est=page_count_est,
          text_chars=text_chars,
          image_count=image_count,
          pages=pages,
      )
  ```

  Key change: passes `xml` (already in memory) to `_extract_pages_from_xml` — no second
  ZIP open, no second `ET.fromstring`.

- [ ] **Step 4: Compile-check**

  ```bash
  cd "/Users/kyawminthu/Dev/Control System Tools"
  python3 -m py_compile tools/fe_study/common.py && echo "OK"
  ```

  Expected: `OK`

- [ ] **Step 5: Commit**

  ```bash
  git add tools/fe_study/common.py
  git commit -m "refactor(fe-study): consolidate DOCX XML read — single ZIP open per profile"
  ```

---

### Task 2: Remove double page extraction in `extract_docx`

**Files:**
- Modify: `tools/fe_study/extract_fe_study.py` — `extract_docx` function

- [ ] **Step 1: Replace `extract_docx_pages` call with `profile.pages`**

  In `extract_docx`, change:

  ```python
  # Before
  if record["extract_mode"] == "docx_text":
      pages = extract_docx_pages(source_path)
  ```

  To:

  ```python
  # After — pages already computed inside profile_docx
  if record["extract_mode"] == "docx_text":
      pages = profile.pages
  ```

  Also remove `extract_docx_pages` from the import list at the top of the file since it is
  no longer called directly:

  ```python
  # Remove this line from the imports:
  extract_docx_pages,
  ```

- [ ] **Step 2: Compile-check**

  ```bash
  python3 -m py_compile tools/fe_study/extract_fe_study.py && echo "OK"
  ```

  Expected: `OK`

- [ ] **Step 3: Commit**

  ```bash
  git add tools/fe_study/extract_fe_study.py
  git commit -m "fix(fe-study): use profile.pages in extract_docx — eliminates redundant page extraction"
  ```

---

## Chunk 2: Extractor Diagnostics + JSONL Encoding (Issues 4, 5)

---

### Task 3: Surface PDF extractor failures

**Problem:** Three `except Exception: pass` blocks in `extract_pdf_pages` swallow errors
silently. A corrupt file or library bug causes silent fallthrough with no diagnostic.

**Approach:** Add an optional `diagnostics: list[str] | None = None` parameter. When
provided, failed extractor attempts append a message. Callers that don't pass the argument
are unaffected (backwards compatible).

**Files:**
- Modify: `tools/fe_study/common.py` — `extract_pdf_pages`
- Modify: `tools/fe_study/extract_fe_study.py` — `extract_pdf` (pass diagnostics through to notes)

- [ ] **Step 1: Update `extract_pdf_pages` signature and exception handling**

  Replace the function signature and each `except` block:

  ```python
  def extract_pdf_pages(
      path: Path,
      diagnostics: list[str] | None = None,
  ) -> tuple[list[str], str | None]:
      """Try the available PDF text extractors and return page text if successful.

      If *diagnostics* is provided, failed extractor attempts append a message to it.
      """
      extractors = optional_pdf_extractors()
      if "pypdf" in extractors:
          try:
              from pypdf import PdfReader  # type: ignore
              reader = PdfReader(str(path))
              return [(page.extract_text() or "").strip() for page in reader.pages], "pypdf"
          except Exception as exc:
              if diagnostics is not None:
                  diagnostics.append(f"pypdf failed: {exc}")
      if "PyPDF2" in extractors:
          try:
              from PyPDF2 import PdfReader  # type: ignore
              reader = PdfReader(str(path))
              return [(page.extract_text() or "").strip() for page in reader.pages], "PyPDF2"
          except Exception as exc:
              if diagnostics is not None:
                  diagnostics.append(f"PyPDF2 failed: {exc}")
      if "pymupdf" in extractors:
          try:
              import fitz  # type: ignore
              doc = fitz.open(str(path))
              return [doc[idx].get_text("text").strip() for idx in range(doc.page_count)], "pymupdf"
          except Exception as exc:
              if diagnostics is not None:
                  diagnostics.append(f"pymupdf failed: {exc}")
      if "pdftotext" in extractors:
          proc = subprocess.run(
              ["pdftotext", str(path), "-"],
              text=True,
              capture_output=True,
              check=False,
          )
          if proc.returncode == 0 and proc.stdout.strip():
              pages = [page.strip() for page in proc.stdout.split("\f") if page.strip()]
              return pages, "pdftotext"
          if diagnostics is not None and proc.returncode != 0:
              diagnostics.append(f"pdftotext failed (exit {proc.returncode}): {proc.stderr.strip()}")
      return [], None
  ```

- [ ] **Step 2: Thread diagnostics through `extract_pdf` in `extract_fe_study.py`**

  ```python
  def extract_pdf(record: dict, source_path: Path) -> list[str]:
      notes: list[str] = []
      record["last_processed_at"] = utc_now_iso()
      diag: list[str] = []
      pages, extractor = extract_pdf_pages(source_path, diagnostics=diag)
      if diag:
          notes.extend(diag)
      ...
  ```

  The rest of `extract_pdf` is unchanged. Diagnostic messages end up in `notes` and
  therefore in the manifest and run log.

- [ ] **Step 3: Compile-check both files**

  ```bash
  python3 -m py_compile tools/fe_study/common.py tools/fe_study/extract_fe_study.py && echo "OK"
  ```

  Expected: `OK`

- [ ] **Step 4: Commit**

  ```bash
  git add tools/fe_study/common.py tools/fe_study/extract_fe_study.py
  git commit -m "fix(fe-study): surface PDF extractor failures via optional diagnostics list"
  ```

---

### Task 4: Fix JSONL Unicode encoding

**Files:**
- Modify: `tools/fe_study/common.py` — `write_manifest_jsonl`

- [ ] **Step 1: Change `ensure_ascii=True` to `ensure_ascii=False`**

  ```python
  # Before
  handle.write(json.dumps({...}, ensure_ascii=True))

  # After
  handle.write(json.dumps({...}, ensure_ascii=False))
  ```

  Math symbols (Σ, ∫, √, ω, τ, ζ) now appear as-is in the JSONL file instead of
  `\u03a3`, `\u222b`, etc.

- [ ] **Step 2: Compile-check**

  ```bash
  python3 -m py_compile tools/fe_study/common.py && echo "OK"
  ```

- [ ] **Step 3: Commit**

  ```bash
  git add tools/fe_study/common.py
  git commit -m "fix(fe-study): use ensure_ascii=False in manifest JSONL — preserves math symbols"
  ```

---

## Chunk 3: Cleanup (Issues 6, 7)

---

### Task 5: Fix `optional_pdf_extractors` docstring and ordering

**Problem:** Docstring says "preference order" but the function lists `pdftotext` first
while `extract_pdf_pages` always tries `pypdf → PyPDF2 → pymupdf → pdftotext` regardless
of list order. The ordering in `optional_pdf_extractors` is vestigial.

**Fix:** Update docstring to accurately describe what the function does (availability
check, not ordering). Reorder the list to match the actual try order in `extract_pdf_pages`
for consistency, even though the order isn't consumed.

**Files:**
- Modify: `tools/fe_study/common.py` — `optional_pdf_extractors`

- [ ] **Step 1: Update docstring and reorder**

  ```python
  def optional_pdf_extractors() -> list[str]:
      """Return the set of available PDF text extractors.

      Order matches the try sequence in extract_pdf_pages:
      pypdf → PyPDF2 → pymupdf → pdftotext.
      """
      available: list[str] = []
      try:
          import pypdf  # noqa: F401
          available.append("pypdf")
      except ImportError:
          pass
      try:
          import PyPDF2  # noqa: F401
          available.append("PyPDF2")
      except ImportError:
          pass
      try:
          import fitz  # noqa: F401
          available.append("pymupdf")
      except ImportError:
          pass
      if shutil.which("pdftotext"):
          available.append("pdftotext")
      return available
  ```

- [ ] **Step 2: Compile-check**

  ```bash
  python3 -m py_compile tools/fe_study/common.py && echo "OK"
  ```

- [ ] **Step 3: Commit**

  ```bash
  git add tools/fe_study/common.py
  git commit -m "fix(fe-study): align optional_pdf_extractors order and docstring with actual try sequence"
  ```

---

### Task 6: Style — blank lines after imports

**Files:**
- Modify: `tools/fe_study/quality_check_fe_study.py` — line 28
- Modify: `tools/fe_study/summarize_fe_study.py` — line 29

- [ ] **Step 1: Add blank line in `quality_check_fe_study.py`**

  Between the last import and `def _clean_lines`, add one blank line so there are two
  blank lines separating imports from the first function definition (PEP 8).

- [ ] **Step 2: Add blank line in `summarize_fe_study.py`**

  Same fix between the last import and `def read_clean_markdown`.

- [ ] **Step 3: Compile-check both**

  ```bash
  python3 -m py_compile tools/fe_study/quality_check_fe_study.py tools/fe_study/summarize_fe_study.py && echo "OK"
  ```

- [ ] **Step 4: Commit**

  ```bash
  git add tools/fe_study/quality_check_fe_study.py tools/fe_study/summarize_fe_study.py
  git commit -m "style(fe-study): add missing blank lines after imports (PEP 8)"
  ```

---

## Final Verification

- [ ] **Full compile-check of all five files**

  ```bash
  cd "/Users/kyawminthu/Dev/Control System Tools"
  python3 -m py_compile \
    tools/fe_study/common.py \
    tools/fe_study/inventory_fe_study.py \
    tools/fe_study/extract_fe_study.py \
    tools/fe_study/quality_check_fe_study.py \
    tools/fe_study/summarize_fe_study.py \
    && echo "all OK"
  ```

- [ ] **Import smoke test** (verifies no missing names in imports)

  ```bash
  python3 -c "from tools.fe_study import common; print('imports OK')"
  ```

- [ ] **DOCX double-read regression check** (manual inspection)

  Add a temporary `print` inside `_docx_document_xml` and `_extract_pages_from_xml`,
  run `inventory_fe_study.py` against a single DOCX, verify each prints exactly once
  per file, then remove the prints.
