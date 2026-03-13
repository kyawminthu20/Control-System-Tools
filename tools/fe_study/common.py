#!/usr/bin/env python3
"""Shared helpers for FE study extraction tooling."""

from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE_ROOT = PROJECT_ROOT / "planning" / "FE_Study"

WORK_DIRS = {
    "inventory": "_inventory",
    "logs": "_logs",
    "extracted_raw": "_extracted/raw",
    "extracted_clean": "_extracted/clean",
    "chunks": "_chunks",
    "summaries": "_summaries",
    "samples": "_samples",
}

MANIFEST_FIELDS = [
    "source_id",
    "source_path",
    "source_name",
    "extension",
    "family",
    "priority",
    "size_bytes",
    "page_count_est",
    "docx_text_chars",
    "docx_image_count",
    "extract_mode",
    "ocr_required",
    "text_layer_present",
    "raw_output_path",
    "clean_output_path",
    "summary_output_path",
    "chunk_output_path",
    "status",
    "quality_score",
    "manual_review",
    "notes",
    "last_processed_at",
]

DOCX_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


@dataclass
class DocxProfile:
    page_count_est: int
    text_chars: int
    image_count: int
    pages: list[str]


def utc_now_iso() -> str:
    """Return a stable UTC timestamp for logs and manifests."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def path_in_project(path: Path) -> str:
    """Return a project-relative path when possible, otherwise an absolute path."""
    resolved = path.resolve()
    try:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def ensure_workdirs(source_root: Path) -> dict[str, Path]:
    """Create the working directories used by the FE extraction pipeline."""
    paths: dict[str, Path] = {}
    for key, rel in WORK_DIRS.items():
        path = source_root / rel
        path.mkdir(parents=True, exist_ok=True)
        paths[key] = path
    (paths["logs"] / "extraction_runs").mkdir(parents=True, exist_ok=True)
    return paths


def manifest_csv_path(source_root: Path) -> Path:
    return source_root / WORK_DIRS["inventory"] / "manifest.csv"


def manifest_jsonl_path(source_root: Path) -> Path:
    return source_root / WORK_DIRS["inventory"] / "manifest.jsonl"


def slugify(name: str) -> str:
    """Convert a filename into a stable ASCII identifier."""
    return slugify_text(Path(name).stem)


def slugify_text(text: str) -> str:
    """Convert arbitrary text into a stable ASCII identifier."""
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()
    return cleaned or "source"


def relative_source_path(source_root: Path, path: Path) -> Path:
    """Return a source-relative path from the configured FE study root."""
    try:
        return path.relative_to(source_root)
    except ValueError:
        resolved = path.resolve()
        resolved_root = source_root.resolve()
        try:
            return resolved.relative_to(resolved_root)
        except ValueError:
            return Path("__external__") / f"{slugify_text(resolved.as_posix())}{path.suffix}"


def source_id_for_path(source_root: Path, path: Path) -> str:
    """Build a unique source ID from the full relative path, not just the basename."""
    rel = relative_source_path(source_root, path)
    return slugify_text(rel.with_suffix("").as_posix())


def work_output_path(source_root: Path, workdir_key: str, source_path: Path, suffix: str) -> Path:
    """Mirror the source folder structure under an extraction work directory."""
    rel = relative_source_path(source_root, source_path)
    mirrored = rel.with_suffix(suffix)
    return source_root / WORK_DIRS[workdir_key] / mirrored


def infer_family(path: Path) -> str:
    """Map FE study files to the extraction families used in the manifest."""
    name = path.name
    if name.startswith("module ") and path.suffix.lower() == ".docx":
        return "module_docx"
    if name.startswith("amatrol lesson ") and path.suffix.lower() == ".pdf":
        return "amatrol_pdf"
    if "FE Handbook" in name and path.suffix.lower() == ".pdf":
        return "handbook_pdf"
    if "Study Guide" in name and path.suffix.lower() == ".pdf":
        return "study_guide_pdf"
    if "Practice Exam" in name and path.suffix.lower() == ".pdf":
        return "practice_exam_pdf"
    if "Power_and_Cooling" in name and path.suffix.lower() == ".pdf":
        return "cheat_sheet_pdf"
    if name.startswith(("LX", "bx")) and path.suffix.lower() == ".pdf":
        return "vendor_pdf"
    return "other"


def infer_priority(family: str) -> str:
    """Assign a coarse priority to each family."""
    if family in {"handbook_pdf", "practice_exam_pdf", "study_guide_pdf", "cheat_sheet_pdf"}:
        return "P1"
    if family in {"amatrol_pdf", "other"}:
        return "P2"
    if family == "module_docx":
        return "P3"
    return "P4"


def resolve_path_ref(path_ref: str) -> Path:
    """Resolve a stored manifest path reference back to a usable filesystem path."""
    path = Path(path_ref)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def page_count_for_pdf(path: Path) -> int:
    """Use macOS Spotlight metadata to estimate PDF page count."""
    if not shutil.which("mdls"):
        return 0
    try:
        output = subprocess.check_output(
            ["mdls", "-name", "kMDItemNumberOfPages", str(path)],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return 0
    match = re.search(r"kMDItemNumberOfPages\s*=\s*(\d+)", output)
    return int(match.group(1)) if match else 0


def _docx_document_xml(path: Path) -> str:
    """Read and return the raw WordprocessingML XML from a DOCX archive."""
    try:
        with zipfile.ZipFile(path) as archive:
            return archive.read("word/document.xml").decode("utf-8", errors="ignore")
    except (KeyError, zipfile.BadZipFile) as exc:
        raise ValueError(f"Invalid or corrupted DOCX file: {path}") from exc


def _extract_pages_from_root(root: ET.Element) -> list[str]:
    """Parse a WordprocessingML document root into rendered page strings."""
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


def _extract_pages_from_xml(xml: str) -> list[str]:
    """Extract rendered pages from a WordprocessingML XML string."""
    return _extract_pages_from_root(ET.fromstring(xml))


def extract_docx_pages(path: Path) -> list[str]:
    """Extract text from a DOCX file while preserving rendered page breaks."""
    return _extract_pages_from_xml(_docx_document_xml(path))


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
    pages = _extract_pages_from_root(root)  # reuses already-parsed root
    page_count_est = len(pages) if pages else max(xml.count("lastRenderedPageBreak") + 1, 1)
    return DocxProfile(
        page_count_est=page_count_est,
        text_chars=text_chars,
        image_count=image_count,
        pages=pages,
    )


def export_docx_media(path: Path, target_dir: Path) -> int:
    """Export embedded DOCX images for later OCR work."""
    target_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    with zipfile.ZipFile(path) as archive:
        for member in archive.namelist():
            if not member.startswith("word/media/"):
                continue
            filename = Path(member).name
            if not filename:
                continue
            count += 1
            with archive.open(member) as src, open(target_dir / filename, "wb") as dst:
                dst.write(src.read())
    return count


def optional_pdf_extractors() -> list[str]:
    """List available PDF extractors in the fallback order used by the loader."""
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
            try:
                return [doc[idx].get_text("text").strip() for idx in range(doc.page_count)], "pymupdf"
            finally:
                doc.close()
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


def detect_pdf_text_layer(path: Path) -> str:
    """Return yes/no/unknown for PDF text layer availability."""
    pages, extractor = extract_pdf_pages(path)
    if not extractor:
        return "unknown"
    sample = "".join(page for page in pages[:3] if page).strip()
    if len(sample) >= 200:
        return "yes"
    return "no"


def normalize_text(text: str) -> str:
    """Apply light cleanup without destroying page-local structure."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def render_clean_markdown(record: dict, pages: Iterable[str], notes: list[str] | None = None) -> str:
    """Render normalized extracted text as a per-source Markdown file."""
    note_lines = notes or []
    header = [
        "# Source Extract",
        "",
        f"- Source: `{record['source_path']}`",
        f"- Source ID: `{record['source_id']}`",
        f"- Family: `{record['family']}`",
        f"- Extraction Mode: `{record['extract_mode']}`",
        f"- Estimated Pages: `{record['page_count_est']}`",
        f"- Quality: `{record['quality_score'] or 'unknown'}`",
    ]
    if note_lines:
        header.append(f"- Notes: `{' | '.join(note_lines)}`")
    body: list[str] = []
    for idx, page in enumerate(pages, start=1):
        cleaned = normalize_text(page)
        if not cleaned:
            continue
        body.extend(["", f"## Page {idx}", "", cleaned])
    if not body:
        body.extend(["", "## Extraction Notes", "", "No text was extracted for this source."])
    return "\n".join(header + body).strip() + "\n"


def write_manifest_csv(path: Path, rows: list[dict]) -> None:
    """Write the manifest in CSV form."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in MANIFEST_FIELDS})


def write_manifest_jsonl(path: Path, rows: list[dict]) -> None:
    """Write the manifest in JSONL form for downstream tooling."""
    with open(path, "w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps({field: row.get(field, "") for field in MANIFEST_FIELDS}, ensure_ascii=False))
            handle.write("\n")


def load_manifest(path: Path) -> list[dict]:
    """Load the CSV manifest if present."""
    if not path.exists():
        return []
    csv.field_size_limit(10**7)
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "\x00" in text:
        text = text.replace("\x00", "")
    reader = csv.DictReader(StringIO(text))
    return [dict(row) for row in reader]


def log_run(log_dir: Path, name: str, lines: Iterable[str]) -> Path:
    """Write a run log into the FE extraction log directory."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = log_dir / "extraction_runs" / f"{timestamp}_{name}.log"
    with open(path, "w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(line.rstrip())
            handle.write("\n")
    return path


def select_manifest_rows(
    rows: list[dict],
    *,
    source_ids: Iterable[str] | None = None,
    priority: str | None = None,
    family: str | None = None,
    status: str | None = None,
    limit: int | None = None,
) -> list[dict]:
    """Apply the common manifest row filters used by the FE study scripts."""
    requested_ids = set(source_ids or [])
    selected = []
    for row in rows:
        if requested_ids and row.get("source_id") not in requested_ids:
            continue
        if priority and row.get("priority") != priority:
            continue
        if family and row.get("family") != family:
            continue
        if status and row.get("status") != status:
            continue
        selected.append(row)
    if limit is not None:
        return selected[:limit]
    return selected
