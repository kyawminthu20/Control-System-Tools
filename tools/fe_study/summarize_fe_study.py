#!/usr/bin/env python3
"""Generate simple per-source summaries from cleaned FE study Markdown files."""

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


def read_clean_markdown(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read().splitlines()


def body_paragraphs(lines: list[str]) -> list[str]:
    text = "\n".join(lines)
    paragraphs = [item.strip() for item in re.split(r"\n\s*\n", text) if item.strip()]
    return [
        item
        for item in paragraphs
        if not item.startswith(("#", "- Source:", "- Source ID:", "- Family:", "- Priority:", "- Clean File:"))
    ]


def formula_candidates(lines: list[str]) -> list[str]:
    candidates = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if "=" in stripped or any(token in stripped for token in ("Σ", "∫", "√", "ω", "τ", "ζ")):
            candidates.append(stripped)
    # preserve order and deduplicate
    seen = set()
    unique = []
    for item in candidates:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique[:12]


def heading_candidates(lines: list[str]) -> list[str]:
    return [line.lstrip("#").strip() for line in lines if line.startswith("#")]


def write_summary(record: dict, lines: list[str]) -> None:
    headings = heading_candidates(lines)
    paragraphs = body_paragraphs(lines)
    formulas = formula_candidates(lines)
    overview = paragraphs[:3]
    page_sections = sum(1 for line in lines if line.startswith("## Page "))

    summary_lines = [
        f"# Summary: {record['source_name']}",
        "",
        f"- Source: `{record['source_path']}`",
        f"- Source ID: `{record['source_id']}`",
        f"- Family: `{record['family']}`",
        f"- Priority: `{record['priority']}`",
        f"- Clean File: `{record['clean_output_path']}`",
        f"- Estimated Pages: `{record['page_count_est']}`",
        f"- Page Sections In Markdown: `{page_sections}`",
        f"- Extraction Quality: `{record['quality_score'] or 'unknown'}`",
        "",
        "## Overview",
        "",
    ]

    if overview:
        summary_lines.extend(f"- {para[:280]}" for para in overview)
    else:
        summary_lines.append("- No meaningful body text was available to summarize.")

    summary_lines.extend(["", "## Key Headings", ""])
    if headings:
        summary_lines.extend(f"- {heading}" for heading in headings[:12])
    else:
        summary_lines.append("- No headings detected.")

    summary_lines.extend(["", "## Formula-Like Lines", ""])
    if formulas:
        summary_lines.extend(f"- `{formula[:220]}`" for formula in formulas)
    else:
        summary_lines.append("- No formula-like lines detected.")

    summary_lines.extend(
        [
            "",
            "## Extraction Notes",
            "",
            f"- Manifest status: `{record['status']}`",
            f"- Manual review: `{record['manual_review']}`",
            f"- Notes: `{record['notes'] or 'none'}`",
        ]
    )

    target = resolve_path_ref(record["summary_output_path"])
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write("\n".join(summary_lines).strip() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root",
        default=str(DEFAULT_SOURCE_ROOT),
        help="Folder containing the FE study automation files.",
    )
    parser.add_argument("--priority", help="Only summarize rows with the given priority.")
    parser.add_argument("--family", help="Only summarize rows in the given family.")
    parser.add_argument("--status", help="Only summarize rows with the given status.")
    parser.add_argument("--source-id", action="append", help="Summarize a specific source_id.")
    parser.add_argument("--limit", type=int, help="Maximum number of rows to summarize.")
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
        raise SystemExit("No manifest rows matched the requested summary scope.")

    log_lines = []
    summarized_count = 0
    for record in selected:
        clean_path = resolve_path_ref(record["clean_output_path"])
        if not clean_path.exists():
            log_lines.append(f"{record['source_id']}: missing clean markdown")
            continue
        lines = read_clean_markdown(clean_path)
        write_summary(record, lines)
        record["last_processed_at"] = utc_now_iso()
        if record["status"] == "cleaned":
            record["status"] = "summarized"
        log_lines.append(f"{record['source_id']}: summarized")
        summarized_count += 1

    write_manifest_csv(manifest_path, rows)
    write_manifest_jsonl(manifest_jsonl_path(source_root), rows)
    log_path = log_run(source_root / "_logs", "summarize", log_lines)
    print(f"Updated summaries for {summarized_count} sources.")
    print(f"Run log: {path_in_project(log_path)}")


if __name__ == "__main__":
    main()
