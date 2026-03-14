#!/usr/bin/env python3
"""Build an extraction manifest for FE study PDFs and DOCX files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.fe_study.common import (
    DEFAULT_SOURCE_ROOT,
    MANIFEST_FIELDS,
    convert_doc_to_docx,
    detect_pdf_text_layer,
    ensure_workdirs,
    infer_family,
    infer_priority,
    load_manifest,
    manifest_csv_path,
    manifest_jsonl_path,
    page_count_for_pdf,
    path_in_project,
    profile_docx,
    source_id_for_path,
    utc_now_iso,
    work_output_path,
    write_manifest_csv,
    write_manifest_jsonl,
)


def scan_sources(source_root: Path) -> list[Path]:
    """Find all PDF and DOCX sources below the FE automation folder."""
    ignore_dirs = {"_inventory", "_logs", "_extracted", "_chunks", "_summaries", "_samples", "_converted"}
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".pdf", ".docx", ".doc"}
        and not path.name.startswith("~$")
        and not any(part in ignore_dirs for part in path.relative_to(source_root).parts)
    )


def build_record(source_root: Path, path: Path, existing: dict | None = None) -> dict:
    """Build or refresh a manifest row for a single source file."""
    family = infer_family(path)
    priority = infer_priority(family)
    source_id = source_id_for_path(source_root, path)
    record = {field: "" for field in MANIFEST_FIELDS}
    if existing:
        record.update(existing)

    record.update(
        {
            "source_id": source_id,
            "source_path": path_in_project(path),
            "source_name": path.name,
            "extension": path.suffix.lower(),
            "family": family,
            "priority": priority,
            "size_bytes": str(path.stat().st_size) if path.exists() else "0",
            "raw_output_path": path_in_project(work_output_path(source_root, "extracted_raw", path, ".txt")),
            "clean_output_path": path_in_project(work_output_path(source_root, "extracted_clean", path, ".md")),
            "summary_output_path": path_in_project(work_output_path(source_root, "summaries", path, ".md")),
            "chunk_output_path": path_in_project(work_output_path(source_root, "chunks", path, ".jsonl")),
        }
    )

    try:
        if path.suffix.lower() == ".pdf":
            page_count_est = page_count_for_pdf(path)
            text_layer = detect_pdf_text_layer(path)
            record["page_count_est"] = str(page_count_est)
            record["docx_text_chars"] = "0"
            record["docx_image_count"] = "0"
            record["text_layer_present"] = text_layer
            if text_layer == "yes":
                record["extract_mode"] = "pdf_text"
                record["ocr_required"] = "no"
            elif text_layer == "no":
                record["extract_mode"] = "pdf_ocr"
                record["ocr_required"] = "yes"
            else:
                record["extract_mode"] = "pdf_text_then_ocr"
                record["ocr_required"] = "unknown"
        elif path.suffix.lower() == ".doc":
            target_dir = work_output_path(source_root, "converted", path, ".docx").parent
            converted = convert_doc_to_docx(path, target_dir)
            if converted and converted.exists():
                profile = profile_docx(converted)
                record["page_count_est"] = str(profile.page_count_est)
                record["docx_text_chars"] = str(profile.text_chars)
                record["docx_image_count"] = str(profile.image_count)
                record["text_layer_present"] = "n/a"
                record["notes"] = ""
                record["status"] = ""
                record["quality_score"] = ""
                record["manual_review"] = ""
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
            profile = profile_docx(path)
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
    except Exception as exc:
        fallback_defaults = {
            "page_count_est": "0",
            "docx_text_chars": "0",
            "docx_image_count": "0",
            "extract_mode": "needs_review",
            "ocr_required": "unknown",
            "text_layer_present": "unknown",
        }
        for field, default in fallback_defaults.items():
            if not record.get(field):
                record[field] = default
        record["status"] = "needs_review"
        record["quality_score"] = "low"
        record["manual_review"] = "yes"
        record["notes"] = f"Inventory profiling failed: {type(exc).__name__}: {exc}"

    if not record["status"]:
        record["status"] = "queued"
    if not record["quality_score"]:
        record["quality_score"] = "unknown"
    if not record["manual_review"]:
        record["manual_review"] = "no"
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        default=str(DEFAULT_SOURCE_ROOT),
        help="Folder containing the FE study automation files.",
    )
    args = parser.parse_args()

    source_root = Path(args.source_root).resolve()
    if not source_root.exists():
        raise SystemExit(f"Source root does not exist: {source_root}")

    ensure_workdirs(source_root)
    existing_rows = {
        row["source_id"]: row
        for row in load_manifest(manifest_csv_path(source_root))
        if row.get("source_id")
    }

    rows = []
    for path in scan_sources(source_root):
        source_id = source_id_for_path(source_root, path)
        row = build_record(source_root, path, existing_rows.get(source_id))
        rows.append(row)

    rows.sort(key=lambda item: (item["priority"], item["family"], item["source_name"].lower()))
    write_manifest_csv(manifest_csv_path(source_root), rows)
    write_manifest_jsonl(manifest_jsonl_path(source_root), rows)

    family_counts: dict[str, int] = {}
    for row in rows:
        family_counts[row["family"]] = family_counts.get(row["family"], 0) + 1

    print(f"Wrote manifest for {len(rows)} sources at {path_in_project(manifest_csv_path(source_root))}")
    for family in sorted(family_counts):
        print(f"  {family}: {family_counts[family]}")
    print(f"Inventory timestamp: {utc_now_iso()}")


if __name__ == "__main__":
    main()
