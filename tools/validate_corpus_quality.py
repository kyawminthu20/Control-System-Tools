#!/usr/bin/env python3
"""Detect authoring-quality defects in the RAG corpus.

Complements ``validate_ai_boundaries.py`` (which enforces AI-access headers and
forbidden keywords). This checker targets the defect classes that reached the
authoritative tier in earlier phases and had no automated guard:

- Conversational AI artifacts (e.g. "Would you like me to...", "If you want, I
  can...") — raw un-edited assistant output shipped as canonical content.
- Empty numeric placeholders (e.g. "between ** and **", "typically  to ") —
  a value the author meant to fill and never did.
- Master-index drift (``standards_intelligence/_index.yaml``): folders listed
  in the index but absent on disk, corpus folders absent from the index, and
  file references that only resolve on case-insensitive filesystems.

Findings are hard errors: none of these classes should ever exist in
``control-standards/rag/``. Run standalone or via ``tools/release_check.py``
(corpus and full profiles).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG = ROOT / "control-standards" / "rag"

# Second-person offers and hand-offs that only make sense in a chat transcript.
CONVERSATIONAL = re.compile(
    r"(?i)\b("
    r"would you like (?:me|to)|"
    r"if you want,? i can|"
    r"shall i\b|"
    r"let me know if|"
    r"do you want me to|"
    r"i can also show you|"
    r"would you like to move on"
    r")",
)

# Blank fill-in spots: adjacent bold/backtick markers or "to"/"and" with the
# value missing between them. Kept specific to avoid flagging legitimate prose.
PLACEHOLDERS = (
    re.compile(r"between \*\* and \*\*"),
    re.compile(r"\( to \)"),
    re.compile(r"typically\s{2,}to\s"),
    re.compile(r"of\s+to\s+times"),
    re.compile(r"``\s*to\s*``"),
    re.compile(r"between\s+and\s+\("),
)


def _rag_files(rag_root: Path = RAG):
    for path in sorted(rag_root.rglob("*.md")):
        if path.name == "README.md":
            continue
        yield path


def check(rag_root: Path = RAG) -> list[str]:
    """Return one human-readable error per defect found (empty list = clean)."""
    errors: list[str] = []
    for path in _rag_files(rag_root):
        rel = path.relative_to(rag_root)
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1
        ):
            if CONVERSATIONAL.search(line):
                errors.append(f"{rel}:{lineno}: conversational AI artifact: {line.strip()[:80]}")
            for pattern in PLACEHOLDERS:
                if pattern.search(line):
                    errors.append(f"{rel}:{lineno}: empty placeholder: {line.strip()[:80]}")
                    break
    return errors


# Path-bearing keys in the master index. Values are always double-quoted there;
# the free-text notes block is deliberately out of scope for this parser.
_INDEX_REFERENCE = re.compile(r'\s*(?:-\s*)?(folder|file|guidance_file):\s*"([^"]+)"')


def _case_sensitive_exists(base: Path, relative: str) -> bool:
    """True only if every path segment matches a directory entry byte-for-byte.

    Path.exists() would accept wrong-case references on macOS (case-insensitive
    filesystem) that then break on case-sensitive CI runners.
    """
    current = base
    for part in Path(relative).parts:
        if not current.is_dir() or part not in {entry.name for entry in current.iterdir()}:
            return False
        current = current / part
    return True


def _disk_standards_folders(intelligence_root: Path) -> set[str]:
    """Directories under us/ and international/ that directly hold corpus files."""
    folders: set[str] = set()
    for region in ("us", "international"):
        region_root = intelligence_root / region
        if not region_root.is_dir():
            continue
        for md_file in region_root.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            folders.add(md_file.parent.relative_to(intelligence_root).as_posix())
    return folders


def check_index(rag_root: Path = RAG) -> list[str]:
    """Validate standards_intelligence/_index.yaml against the on-disk corpus."""
    intelligence_root = rag_root / "standards_intelligence"
    index_path = intelligence_root / "_index.yaml"
    if not index_path.exists():
        return ["standards_intelligence/_index.yaml: master index is missing"]

    errors: list[str] = []
    indexed_folders: set[str] = set()
    lines = index_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for lineno, line in enumerate(lines, start=1):
        match = _INDEX_REFERENCE.match(line)
        if not match:
            continue
        key, value = match.groups()
        if not _case_sensitive_exists(intelligence_root, value):
            errors.append(
                f"standards_intelligence/_index.yaml:{lineno}: "
                f"{key} does not resolve case-sensitively on disk: {value}"
            )
        elif key == "folder":
            indexed_folders.add(value)

    for folder in sorted(_disk_standards_folders(intelligence_root) - indexed_folders):
        errors.append(
            f"standards_intelligence/_index.yaml: corpus folder missing from "
            f"standards inventory: {folder}"
        )
    return errors


def main() -> int:
    errors = check() + check_index()
    if errors:
        print(f"❌ FAILED: {len(errors)} corpus-quality defect(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print("✅ PASSED: no conversational artifacts or empty placeholders in the RAG corpus.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
