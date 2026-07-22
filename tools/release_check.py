#!/usr/bin/env python3
"""Run the repository's governed, read-only release checks.

Profiles keep local feedback focused while ``full`` is the deployment gate:

    uv run python tools/release_check.py --profile toolkit
    uv run python tools/release_check.py --profile corpus
    uv run python tools/release_check.py --profile site
    uv run python tools/release_check.py --profile full

The metadata checks hold legacy debt at an explicit non-regression baseline.
Existing missing metadata is reported as a warning; malformed metadata and any
increase beyond the baseline fail the check.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from tools.generate_ai_method_register import (
        DATA_FILES,
        DESTINATION as AI_DATA,
        SOURCE as AI_SOURCE,
        validate as validate_ai_register,
    )
except ModuleNotFoundError:  # Direct execution: python tools/release_check.py
    from generate_ai_method_register import (  # type: ignore[no-redef]
        DATA_FILES,
        DESTINATION as AI_DATA,
        SOURCE as AI_SOURCE,
        validate as validate_ai_register,
    )

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RAG = ROOT / "control-standards" / "rag"
RAG_MIRROR = DOCS / "assets" / "rag-files"

ALLOWED_SITE_STATUSES = {
    "Reviewed",
    "Partial coverage",
    "Review pending",
    "Needs revalidation",
    "Planned",
}
REVIEW_FIELDS = {"standard", "edition", "status", "coverage", "last_reviewed"}

# Corpus header debt was driven to zero in Phase 50.2 and site review-block
# debt to zero in Phase 52.4b (three tranches, 2026-07-20), so every site page
# must now carry either a governed `review:` block or a documented
# `review_exempt: "<reason>"` — a page with neither is a hard release failure.
MAX_SITE_PAGES_WITHOUT_REVIEW = 0
MAX_RAG_WITHOUT_CONTENT_CLASS = 0
MAX_RAG_WITHOUT_STATUS = 0


def _run(command: list[str], cwd: Path = ROOT) -> list[str]:
    print(f"\n$ {' '.join(command)}")
    completed = subprocess.run(command, cwd=cwd, check=False)
    if completed.returncode:
        return [f"command exited {completed.returncode}: {' '.join(command)}"]
    return []


def _rag_files(root: Path = RAG) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.name != "README.md")


def check_rag_mirror(
    rag_root: Path = RAG,
    mirror_root: Path = RAG_MIRROR,
) -> list[str]:
    """Require an exact path-and-content mirror of publishable RAG Markdown."""
    errors: list[str] = []
    source = {path.relative_to(rag_root): path for path in _rag_files(rag_root)}
    mirrored = {
        path.relative_to(mirror_root): path
        for path in sorted(mirror_root.rglob("*.md"))
    }
    for rel in sorted(source.keys() - mirrored.keys()):
        errors.append(f"RAG mirror missing: {rel}")
    for rel in sorted(mirrored.keys() - source.keys()):
        errors.append(f"RAG mirror has stale file: {rel}")
    for rel in sorted(source.keys() & mirrored.keys()):
        if source[rel].read_bytes() != mirrored[rel].read_bytes():
            errors.append(f"RAG mirror differs: {rel}")
    return errors


def check_ai_register_generated(
    source_root: Path = AI_SOURCE,
    generated_root: Path = AI_DATA,
) -> list[str]:
    """Validate the canonical register and require exact generated Jekyll data."""
    errors = validate_ai_register(source_root)
    for name in DATA_FILES:
        source = source_root / name
        generated = generated_root / name
        if not generated.exists():
            errors.append(f"AI method data missing: {name}")
        elif source.read_bytes() != generated.read_bytes():
            errors.append(f"AI method data differs from canonical source: {name}")
    stale = sorted(path.name for path in generated_root.glob("*.yml") if path.name not in DATA_FILES)
    for name in stale:
        errors.append(f"AI method data has stale file: {name}")
    return errors


def check_rag_metadata(rag_root: Path = RAG) -> tuple[list[str], list[str]]:
    """Validate present corpus metadata and cap missing legacy metadata."""
    errors: list[str] = []
    warnings: list[str] = []
    missing_class: list[Path] = []
    missing_status: list[Path] = []
    for path in _rag_files(rag_root):
        text = path.read_text(encoding="utf-8", errors="ignore")[:1600]
        if not re.search(r"(?m)^(?:\*\*)?CONTENT_CLASS:", text):
            missing_class.append(path)
        if not re.search(r"(?m)^(?:\*\*)?STATUS:", text):
            missing_status.append(path)
        access = re.findall(
            r"(?m)^(?:\*\*)?AI_READ_ACCESS:(?:\*\*)?\s*([^\s*]+)", text
        )
        if not access or access[0] != "ALLOWED":
            errors.append(f"{path.relative_to(rag_root)}: AI_READ_ACCESS must be ALLOWED")

    if len(missing_class) > MAX_RAG_WITHOUT_CONTENT_CLASS:
        errors.append(
            "RAG CONTENT_CLASS debt increased: "
            f"{len(missing_class)} > baseline {MAX_RAG_WITHOUT_CONTENT_CLASS}"
        )
    if len(missing_status) > MAX_RAG_WITHOUT_STATUS:
        errors.append(
            f"RAG STATUS debt increased: {len(missing_status)} > baseline {MAX_RAG_WITHOUT_STATUS}"
        )
    if missing_class:
        warnings.append(f"legacy RAG files without CONTENT_CLASS: {len(missing_class)}")
    if missing_status:
        warnings.append(f"legacy RAG files without STATUS: {len(missing_status)}")
    return errors, warnings


def _site_pages(docs_root: Path = DOCS) -> list[Path]:
    excluded = {"plans", "superpowers", "_site", "vendor", "assets"}
    return sorted(
        path
        for path in docs_root.rglob("index.md")
        if not excluded.intersection(path.relative_to(docs_root).parts)
    )


def _frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) == 3 else ""


def check_site_metadata(docs_root: Path = DOCS) -> tuple[list[str], list[str]]:
    """Validate governed review blocks and cap the legacy rollout backlog."""
    errors: list[str] = []
    warnings: list[str] = []
    missing_review: list[Path] = []
    for path in _site_pages(docs_root):
        frontmatter = _frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
        rel = path.relative_to(docs_root)
        if not frontmatter:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        exempt = re.search(r"(?m)^review_exempt:\s*(.*?)\s*$", frontmatter)
        if exempt:
            # Governed opt-out for redirect stubs and pure navigation pages —
            # a reason is mandatory so the release metric stays meaningful,
            # and a page cannot be simultaneously exempt and reviewed.
            reason = exempt.group(1).strip().strip("\"'")
            if re.search(r"(?m)^review:\s*$", frontmatter):
                errors.append(f"{rel}: declares both review: and review_exempt:")
            elif not reason:
                errors.append(f"{rel}: review_exempt requires a documented reason")
            continue
        if not re.search(r"(?m)^review:\s*$", frontmatter):
            missing_review.append(path)
            continue
        block_match = re.search(
            r"(?ms)^review:\s*\n((?:^[ \t]+[^\n]*\n?)+)", frontmatter
        )
        if not block_match:
            errors.append(f"{rel}: malformed review block")
            continue
        block = block_match.group(1)
        fields = {
            match.group(1): match.group(2).strip().strip('"\'')
            for match in re.finditer(r"(?m)^\s+([a-z_]+):\s*(.*?)\s*$", block)
        }
        missing = REVIEW_FIELDS - fields.keys()
        if missing:
            errors.append(f"{rel}: review block missing {', '.join(sorted(missing))}")
        status = fields.get("status")
        if status and status not in ALLOWED_SITE_STATUSES:
            errors.append(f"{rel}: invalid review status {status!r}")

    if len(missing_review) > MAX_SITE_PAGES_WITHOUT_REVIEW:
        errors.append(
            "site review-frontmatter debt increased: "
            f"{len(missing_review)} > baseline {MAX_SITE_PAGES_WITHOUT_REVIEW}"
        )
    if missing_review:
        warnings.append(f"legacy site pages without review blocks: {len(missing_review)}")
    return errors, warnings


# Phase 52.4 badge-honesty gate. In-table "Reviewed" badges are corpus-status
# claims; every one must resolve to a standards_intelligence module marked
# "complete" in _index.yaml, and any NEC article / IEC 60079 part it cites must
# exist as a corpus file. Bare retired labels and internal phase numbers are
# banned as badge text (long-form explanatory gap flags remain allowed).
BADGE_TEXT_RE = re.compile(r'<span class="badge badge--[a-z-]+">([^<]+)</span>')
PLAIN_REVIEWED_CELL_RE = re.compile(r"\|\s*Reviewed\s*\|")
RETIRED_BADGE_LABELS = {
    "complete",
    "not in corpus",
    "not yet covered",
    "not confirmed in corpus",
    "to verify",
}
PHASE_BADGE_RE = re.compile(r"(?i)^phase\s+\d+")
# The about page hosts the badge legend — its badges define the vocabulary
# rather than claim corpus status, so it is exempt from claim resolution.
BADGE_CLAIM_EXEMPT = {Path("about/index.md")}
STANDARD_TOKEN_MODULES: tuple[tuple[str, str], ...] = (
    (r"\bNEC\b", "us/nec"),
    (r"\bNFPA\s*79\b", "us/nfpa79"),
    (r"\bUL\s*508A\b", "us/ul_508a"),
    (r"60204", "international/machinery/iec_60204_1"),
    (r"13849", "international/functional_safety/iso_13849_1"),
    (r"12100", "international/functional_safety/iso_12100"),
    (r"62061", "international/functional_safety/iec_62061"),
    (r"61508", "international/functional_safety/iec_61508"),
    (r"61511", "international/functional_safety/iec_61511"),
    (r"60079", "international/hazardous_area/iec_60079"),
    (r"\bSEMI\b", "international/semiconductor/semi"),
    (r"62443", "international/cybersecurity/iec_62443"),
    (r"\bABS\b", "international/offshore"),
    (r"\bDNV\b", "international/offshore"),
)
REVIEWED_LOOKBACK_LINES = 8


def _module_statuses(rag_root: Path = RAG) -> dict[str, str]:
    """Parse folder -> status pairs from the standards intelligence index."""
    index_path = rag_root / "standards_intelligence" / "_index.yaml"
    statuses: dict[str, str] = {}
    pending_folder: str | None = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        folder = re.search(r'folder:\s*"([^"]+)"', line)
        if folder:
            pending_folder = folder.group(1)
            continue
        status = re.search(r'status:\s*"([^"]+)"', line)
        if status and pending_folder:
            statuses[pending_folder] = status.group(1)
            pending_folder = None
    return statuses


def _nec_articles(rag_root: Path = RAG) -> set[int]:
    articles: set[int] = set()
    nec_dir = rag_root / "standards_intelligence" / "us" / "nec"
    for path in nec_dir.glob("NEC_*__Art*"):
        art_token = path.name.split("__")[1]
        for number in re.findall(r"\d+", art_token):
            if int(number) >= 90:  # NEC article numbering starts at 90
                articles.add(int(number))
    return articles


def _iec60079_parts(rag_root: Path = RAG) -> set[str]:
    parts_dir = rag_root / "standards_intelligence" / "international" / "hazardous_area" / "iec_60079"
    parts: set[str] = set()
    for path in parts_dir.glob("IEC60079_*.md"):
        token = path.stem[len("IEC60079_"):].split("__")[0]
        parts.add(token.replace("_", "-"))
    return parts


def _check_reviewed_claim(
    rel: Path,
    line_number: int,
    line: str,
    context: str,
    statuses: dict[str, str],
    nec_articles: set[int],
    iec60079_parts: set[str],
) -> list[str]:
    errors: list[str] = []
    matched_modules = {
        module
        for token, module in STANDARD_TOKEN_MODULES
        if re.search(token, context)
    }
    if not matched_modules:
        errors.append(
            f"{rel}:{line_number}: Reviewed badge with no resolvable standard"
        )
        return errors
    for module in sorted(matched_modules):
        if statuses.get(module) != "complete":
            errors.append(
                f"{rel}:{line_number}: Reviewed badge cites module {module!r} "
                f"not marked complete in _index.yaml"
            )
    if re.search(r"\bNEC\b", line):
        for span in re.findall(r"Art(?:icle)?s?\.?\s*([\d,\s]+)", line):
            for number in re.findall(r"\d+", span):
                if int(number) >= 90 and int(number) not in nec_articles:
                    errors.append(
                        f"{rel}:{line_number}: Reviewed badge cites NEC Art. "
                        f"{number} which is not in the corpus"
                    )
    for part in re.findall(r"60079-(\d+(?:-\d+)?)", line):
        if part not in iec60079_parts:
            errors.append(
                f"{rel}:{line_number}: Reviewed badge cites IEC 60079-{part} "
                f"which is not in the corpus"
            )
    return errors


def check_site_badges(
    docs_root: Path = DOCS, rag_root: Path = RAG
) -> list[str]:
    """Verify in-table status badges against the corpus index and files."""
    errors: list[str] = []
    statuses = _module_statuses(rag_root)
    nec_articles = _nec_articles(rag_root)
    iec60079_parts = _iec60079_parts(rag_root)
    for path in _site_pages(docs_root):
        rel = path.relative_to(docs_root)
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for index, line in enumerate(lines, start=1):
            for badge_text in BADGE_TEXT_RE.findall(line):
                label = badge_text.strip().lower()
                if label in RETIRED_BADGE_LABELS or PHASE_BADGE_RE.match(label):
                    errors.append(
                        f"{rel}:{index}: retired badge label {badge_text.strip()!r}"
                    )
            if rel in BADGE_CLAIM_EXEMPT:
                continue
            claims_reviewed = (
                'badge--reviewed">Reviewed<' in line
                or PLAIN_REVIEWED_CELL_RE.search(line) is not None
            )
            if not claims_reviewed:
                continue
            context = "\n".join(
                lines[max(0, index - 1 - REVIEWED_LOOKBACK_LINES) : index]
            )
            errors += _check_reviewed_claim(
                rel, index, line, context, statuses, nec_articles, iec60079_parts
            )
    # Shared includes render on every page, so a retired label there
    # propagates site-wide (only the label rule applies — includes carry
    # legends, not corpus-status claims of their own).
    includes = docs_root / "_includes"
    if includes.is_dir():
        for path in sorted(includes.glob("*.html")):
            rel = path.relative_to(docs_root)
            text = path.read_text(encoding="utf-8", errors="ignore")
            for index, line in enumerate(text.splitlines(), start=1):
                for badge_text in BADGE_TEXT_RE.findall(line):
                    label = badge_text.strip().lower()
                    if label in RETIRED_BADGE_LABELS or PHASE_BADGE_RE.match(label):
                        errors.append(
                            f"{rel}:{index}: retired badge label {badge_text.strip()!r}"
                        )
    return errors


def _bundle_command() -> str | None:
    configured = shutil.which("bundle")
    if configured:
        return configured
    local = Path.home() / ".gem" / "ruby" / "2.6.0" / "bin" / "bundle"
    return str(local) if local.exists() else None


def run_toolkit() -> list[str]:
    errors = _run(["uv", "run", "pytest", "-q"])
    errors += _run(["uv", "run", "pytest", "-q", "--doctest-modules", "src/cst"])
    return errors


def run_corpus() -> tuple[list[str], list[str]]:
    errors = _run([sys.executable, "tools/validate_ai_boundaries.py"])
    errors += _run([sys.executable, "tools/validate_corpus_quality.py"])
    errors += check_rag_mirror()
    errors += check_ai_register_generated()
    metadata_errors, warnings = check_rag_metadata()
    return errors + metadata_errors, warnings


def run_site() -> tuple[list[str], list[str]]:
    errors, warnings = check_site_metadata()
    errors += check_site_badges()
    bundle = _bundle_command()
    if bundle is None:
        return errors + ["Bundler executable not found"], warnings
    with tempfile.TemporaryDirectory(prefix="cst-site-") as destination:
        errors += _run(
            [bundle, "exec", "jekyll", "build", "--destination", destination],
            cwd=DOCS,
        )
        if not errors:
            errors += _run(
                [sys.executable, "tools/check_internal_links.py", destination]
            )
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile",
        choices=("metadata", "toolkit", "corpus", "site", "full"),
        default="full",
    )
    args = parser.parse_args(argv)

    errors: list[str] = []
    warnings: list[str] = []
    if args.profile in ("metadata", "corpus", "full"):
        corpus_errors, corpus_warnings = (
            run_corpus() if args.profile != "metadata" else check_rag_metadata()
        )
        errors += corpus_errors
        warnings += corpus_warnings
    if args.profile in ("metadata", "site", "full"):
        site_errors, site_warnings = (
            run_site() if args.profile != "metadata" else check_site_metadata()
        )
        if args.profile == "metadata":
            site_errors += check_site_badges()
        errors += site_errors
        warnings += site_warnings
    if args.profile in ("toolkit", "full"):
        errors += run_toolkit()

    print("\nRelease-check summary")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print("PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
