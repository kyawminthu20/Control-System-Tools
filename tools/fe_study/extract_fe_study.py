#!/usr/bin/env python3
"""Local-first extraction for FE study PDFs and DOCX files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.fe_study.common import (
    DEFAULT_SOURCE_ROOT,
    ensure_workdirs,
    export_docx_media,
    extract_pdf_pages,
    load_manifest,
    log_run,
    manifest_csv_path,
    manifest_jsonl_path,
    normalize_text,
    path_in_project,
    profile_docx,
    render_clean_markdown,
    resolve_path_ref,
    select_manifest_rows,
    utc_now_iso,
    write_manifest_csv,
    write_manifest_jsonl,
)


def write_text_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def build_raw_text_from_pages(pages: list[str]) -> str:
    blocks = []
    for idx, page in enumerate(pages, start=1):
        blocks.append(f"--- PAGE {idx} ---")
        blocks.append(normalize_text(page))
        blocks.append("")
    return "\n".join(blocks).strip() + "\n"


def extract_docx(record: dict, source_path: Path, export_media: bool) -> list[str]:
    """Extract text from or stage OCR assets for a DOCX source."""
    notes: list[str] = []
    profile = profile_docx(source_path)
    record["last_processed_at"] = utc_now_iso()

    if record["extract_mode"] == "docx_text":
        pages = profile.pages
        record["status"] = "cleaned"
        record["quality_score"] = "high" if profile.text_chars >= 1500 else "medium"
        record["manual_review"] = "no"
        record["notes"] = "DOCX text extracted locally from WordprocessingML."
        raw_text = build_raw_text_from_pages(pages)
        write_text_file(resolve_path_ref(record["raw_output_path"]), raw_text)
        write_text_file(
            resolve_path_ref(record["clean_output_path"]),
            render_clean_markdown(record, pages, notes=["Text-native DOCX extraction"]),
        )
        return notes

    media_dir = resolve_path_ref(record["raw_output_path"]).with_suffix("")
    media_dir = media_dir.parent / f"{media_dir.name}_media"
    exported = export_docx_media(source_path, media_dir) if export_media else 0
    notes.append(f"Image-heavy DOCX exported {exported} media files to {path_in_project(media_dir)}")
    record["status"] = "needs_review"
    record["quality_score"] = "low"
    record["manual_review"] = "yes"
    record["notes"] = "DOCX is image-heavy and requires OCR; media assets were exported."
    placeholder = [
        "Image-heavy DOCX detected.",
        f"Embedded images exported: {exported}",
        f"Estimated pages: {profile.page_count_est}",
        "Run OCR against the exported media files, then replace this placeholder.",
    ]
    write_text_file(resolve_path_ref(record["raw_output_path"]), "\n".join(placeholder) + "\n")
    write_text_file(
        resolve_path_ref(record["clean_output_path"]),
        render_clean_markdown(record, [], notes=notes),
    )
    return notes


def extract_pdf(record: dict, source_path: Path) -> list[str]:
    """Extract PDF text if a local extractor is available, else stage a review placeholder."""
    notes: list[str] = []
    record["last_processed_at"] = utc_now_iso()
    pages, extractor, errors = extract_pdf_pages(source_path)

    if extractor and any(page.strip() for page in pages):
        if errors:
            notes.extend(errors)
        notes.append(f"Extracted with {extractor}")
        total_chars = sum(len(page) for page in pages)
        record["text_layer_present"] = "yes"
        record["status"] = "cleaned"
        record["quality_score"] = "high" if total_chars >= 4000 else "medium"
        record["manual_review"] = "no"
        if errors:
            record["notes"] = f"PDF text extracted locally using {extractor}; earlier extractors failed and were logged."
        else:
            record["notes"] = f"PDF text extracted locally using {extractor}."
        raw_text = build_raw_text_from_pages(pages)
        write_text_file(resolve_path_ref(record["raw_output_path"]), raw_text)
        write_text_file(
            resolve_path_ref(record["clean_output_path"]),
            render_clean_markdown(record, pages, notes=notes),
        )
        return notes

    notes.extend(errors)
    notes.append("No local PDF text extractor produced usable text.")
    notes.append("Install pypdf, PyPDF2, PyMuPDF, or pdftotext, or run an OCR workflow.")
    record["status"] = "needs_review"
    record["quality_score"] = "low"
    record["manual_review"] = "yes"
    record["text_layer_present"] = "unknown" if not extractor else "no"
    record["notes"] = "PDF needs OCR or an optional text extraction dependency."
    write_text_file(resolve_path_ref(record["raw_output_path"]), "\n".join(notes) + "\n")
    write_text_file(
        resolve_path_ref(record["clean_output_path"]),
        render_clean_markdown(record, [], notes=notes),
    )
    return notes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        default=str(DEFAULT_SOURCE_ROOT),
        help="Folder containing the FE study automation files.",
    )
    parser.add_argument("--priority", help="Only process rows with the given priority (P1-P4).")
    parser.add_argument("--family", help="Only process rows in the given family.")
    parser.add_argument("--source-id", action="append", help="Process a specific source_id.")
    parser.add_argument("--status", help="Only process rows with the given manifest status.")
    parser.add_argument("--limit", type=int, help="Maximum number of rows to process.")
    parser.add_argument(
        "--no-export-media",
        action="store_true",
        help="Do not export embedded media for image-heavy DOCX files.",
    )
    args = parser.parse_args()

    source_root = Path(args.source_root).resolve()
    ensure_workdirs(source_root)
    manifest_path = manifest_csv_path(source_root)
    rows = load_manifest(manifest_path)
    if not rows:
        raise SystemExit(f"Manifest not found or empty: {manifest_path}")

    selected = select_manifest_rows(
        rows,
        source_ids=args.source_id,
        priority=args.priority,
        family=args.family,
        status=args.status,
        limit=args.limit,
    )
    if not selected:
        raise SystemExit("No manifest rows matched the requested extraction scope.")

    log_lines = []
    for record in selected:
        source_path = resolve_path_ref(record["source_path"])
        if not source_path.exists():
            record["status"] = "needs_review"
            record["quality_score"] = "low"
            record["manual_review"] = "yes"
            record["notes"] = "Source path missing at extraction time."
            log_lines.append(f"{record['source_id']}: missing source {record['source_path']}")
            continue

        if record["extension"] == ".docx":
            notes = extract_docx(record, source_path, export_media=not args.no_export_media)
        else:
            notes = extract_pdf(record, source_path)
        log_lines.append(f"{record['source_id']}: {record['status']} ({'; '.join(notes)})")

    write_manifest_csv(manifest_path, rows)
    write_manifest_jsonl(manifest_jsonl_path(source_root), rows)
    log_path = log_run(source_root / "_logs", "extract", log_lines)
    print(f"Processed {len(selected)} sources. Updated manifest: {path_in_project(manifest_path)}")
    print(f"Run log: {path_in_project(log_path)}")


if __name__ == "__main__":
    main()
