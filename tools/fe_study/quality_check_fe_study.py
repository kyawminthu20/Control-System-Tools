#!/usr/bin/env python3
"""Score FE study extraction outputs and flag likely bad results."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.fe_study.common import (
    DEFAULT_SOURCE_ROOT,
    load_manifest,
    log_run,
    manifest_csv_path,
    manifest_jsonl_path,
    path_in_project,
    resolve_path_ref,
    select_manifest_rows,
    utc_now_iso,
    write_manifest_csv,
    write_manifest_jsonl,
)


def _clean_lines(text: str) -> list[str]:
    return [line.rstrip() for line in text.splitlines()]


def _body_lines(lines: list[str]) -> list[str]:
    filtered = []
    metadata_prefixes = (
        "# Source Extract",
        "- Source:",
        "- Source ID:",
        "- Family:",
        "- Extraction Mode:",
        "- Estimated Pages:",
        "- Quality:",
        "- Notes:",
    )
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(metadata_prefixes):
            continue
        filtered.append(stripped)
    return filtered


def _append_quality_note(existing: str, quality_note: str) -> str:
    if "Quality check:" in existing:
        existing = existing.split("Quality check:", 1)[0].rstrip(" |")
    if existing:
        return f"{existing} | Quality check: {quality_note}"
    return f"Quality check: {quality_note}"


def quality_metrics(clean_path: Path, estimated_pages: int) -> dict:
    text = clean_path.read_text(encoding="utf-8")
    lines = _clean_lines(text)
    body_lines = _body_lines(lines)
    body_text = "\n".join(body_lines)
    page_sections = sum(1 for line in lines if line.startswith("## Page "))
    headings = sum(1 for line in lines if line.startswith("#"))
    formula_lines = sum(
        1
        for line in body_lines
        if "=" in line or any(token in line for token in ("Σ", "∫", "√", "ω", "τ", "ζ"))
    )
    printable_chars = sum(1 for ch in body_text if ch.isalnum() or ch.isspace() or ch in ".,;:!?()[]{}<>+-=*/_%$#@'\"`~|\\")
    total_chars = len(body_text)
    printable_ratio = printable_chars / total_chars if total_chars else 0.0
    effective_pages = page_sections or estimated_pages or 1
    avg_chars_per_page = total_chars / effective_pages if effective_pages else 0.0
    no_text_placeholder = "No text was extracted for this source." in text

    issues: list[str] = []
    warnings: list[str] = []

    if no_text_placeholder:
        issues.append("no_text_placeholder")
    if total_chars < 120:
        issues.append("body_too_small")
    elif total_chars < 400:
        warnings.append("body_small")

    if estimated_pages >= 3 and page_sections == 0:
        issues.append("no_page_markers")
    elif estimated_pages >= 3 and page_sections < max(1, estimated_pages // 5):
        warnings.append("few_page_markers")

    if estimated_pages >= 3 and avg_chars_per_page < 80:
        issues.append("sparse_text_per_page")
    elif estimated_pages >= 3 and avg_chars_per_page < 180:
        warnings.append("low_text_density")

    if total_chars and printable_ratio < 0.72:
        issues.append("high_noise")
    elif total_chars and printable_ratio < 0.88:
        warnings.append("some_noise")

    if total_chars >= 800 and headings <= 1:
        warnings.append("weak_structure")
    if total_chars >= 800 and formula_lines == 0 and "formula" in clean_path.name.lower():
        warnings.append("missing_formula_lines")

    if issues:
        quality_score = "low"
    elif warnings:
        quality_score = "medium"
    else:
        quality_score = "high"

    return {
        "page_sections": page_sections,
        "estimated_pages": estimated_pages,
        "body_chars": total_chars,
        "avg_chars_per_page": avg_chars_per_page,
        "printable_ratio": printable_ratio,
        "headings": headings,
        "formula_lines": formula_lines,
        "issues": issues,
        "warnings": warnings,
        "quality_score": quality_score,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        default=str(DEFAULT_SOURCE_ROOT),
        help="Folder containing the FE study files and manifest.",
    )
    parser.add_argument("--priority", help="Only check rows with the given priority.")
    parser.add_argument("--family", help="Only check rows in the given family.")
    parser.add_argument("--status", help="Only check rows with the given status.")
    parser.add_argument("--source-id", action="append", help="Check a specific source_id.")
    parser.add_argument("--limit", type=int, help="Maximum number of rows to check.")
    args = parser.parse_args()

    source_root = Path(args.source_root).resolve()
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
        raise SystemExit("No manifest rows matched the requested quality-check scope.")

    log_lines = []
    counts = {"high": 0, "medium": 0, "low": 0}

    for record in selected:
        clean_path = resolve_path_ref(record["clean_output_path"])
        try:
            estimated_pages = int(record["page_count_est"] or 0)
        except (ValueError, TypeError):
            estimated_pages = 0

        if not clean_path.exists():
            record["quality_score"] = "low"
            record["manual_review"] = "yes"
            record["status"] = "needs_review"
            record["notes"] = _append_quality_note(record.get("notes", ""), "missing clean markdown")
            record["last_processed_at"] = utc_now_iso()
            counts["low"] += 1
            log_lines.append(f"{record['source_id']}: low missing_clean_markdown")
            continue

        metrics = quality_metrics(clean_path, estimated_pages)
        quality = metrics["quality_score"]
        counts[quality] += 1
        record["quality_score"] = quality
        if quality == "low":
            record["manual_review"] = "yes"
            record["status"] = "needs_review"
        elif record.get("manual_review") != "yes":
            record["manual_review"] = "no"

        detail_parts = []
        if metrics["issues"]:
            detail_parts.append("issues=" + ",".join(metrics["issues"]))
        if metrics["warnings"]:
            detail_parts.append("warnings=" + ",".join(metrics["warnings"]))
        detail_parts.append(f"body_chars={metrics['body_chars']}")
        detail_parts.append(f"page_sections={metrics['page_sections']}")
        detail_parts.append(f"avg_chars_per_page={metrics['avg_chars_per_page']:.1f}")
        detail_parts.append(f"printable_ratio={metrics['printable_ratio']:.2f}")
        record["notes"] = _append_quality_note(record.get("notes", ""), "; ".join(detail_parts))
        record["last_processed_at"] = utc_now_iso()

        log_lines.append(
            f"{record['source_id']}: {quality} "
            f"issues={','.join(metrics['issues']) or 'none'} "
            f"warnings={','.join(metrics['warnings']) or 'none'} "
            f"body_chars={metrics['body_chars']} "
            f"page_sections={metrics['page_sections']} "
            f"avg_chars_per_page={metrics['avg_chars_per_page']:.1f} "
            f"printable_ratio={metrics['printable_ratio']:.2f}"
        )

    write_manifest_csv(manifest_path, rows)
    write_manifest_jsonl(manifest_jsonl_path(source_root), rows)
    log_path = log_run(source_root / "_logs", "quality_check", log_lines)
    print(
        f"Quality-checked {len(selected)} sources. "
        f"high={counts['high']} medium={counts['medium']} low={counts['low']}"
    )
    print(f"Run log: {path_in_project(log_path)}")


if __name__ == "__main__":
    main()
