#!/usr/bin/env python3
"""Detect authoring-quality defects in the RAG corpus.

Complements ``validate_ai_boundaries.py`` (which enforces AI-access headers and
forbidden keywords). This checker targets the defect classes that reached the
authoritative tier in earlier phases and had no automated guard:

- Conversational AI artifacts (e.g. "Would you like me to...", "If you want, I
  can...") — raw un-edited assistant output shipped as canonical content.
- Empty numeric placeholders (e.g. "between ** and **", "typically  to ") —
  a value the author meant to fill and never did.

Findings are hard errors: neither class should ever exist in ``control-standards/rag/``.
Run standalone or via ``tools/release_check.py`` (corpus and full profiles).
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


def main() -> int:
    errors = check()
    if errors:
        print(f"❌ FAILED: {len(errors)} corpus-quality defect(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print("✅ PASSED: no conversational artifacts or empty placeholders in the RAG corpus.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
