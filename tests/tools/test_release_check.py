"""Tests for the governed release-check module."""

from __future__ import annotations

from pathlib import Path

from tools.release_check import (
    check_ai_register_generated,
    check_rag_metadata,
    check_rag_mirror,
    check_site_metadata,
)


def test_ai_register_generated_detects_changed_data(tmp_path: Path) -> None:
    source = tmp_path / "source"
    generated = tmp_path / "generated"
    source.mkdir()
    generated.mkdir()
    canonical = Path("control-standards/rag/design_framework/ai_integration")
    for name in ("methods.yml", "sources.yml"):
        content = (canonical / name).read_bytes()
        (source / name).write_bytes(content)
        (generated / name).write_bytes(content)
    (generated / "methods.yml").write_text("{}", encoding="utf-8")

    errors = check_ai_register_generated(source, generated)

    assert "AI method data differs from canonical source: methods.yml" in errors


def test_rag_mirror_detects_missing_stale_and_changed_files(tmp_path: Path) -> None:
    rag = tmp_path / "rag"
    mirror = tmp_path / "mirror"
    rag.mkdir()
    mirror.mkdir()
    (rag / "same.md").write_text("same", encoding="utf-8")
    (mirror / "same.md").write_text("same", encoding="utf-8")
    (rag / "changed.md").write_text("canonical", encoding="utf-8")
    (mirror / "changed.md").write_text("stale", encoding="utf-8")
    (rag / "missing.md").write_text("missing", encoding="utf-8")
    (mirror / "stale.md").write_text("stale", encoding="utf-8")
    (rag / "README.md").write_text("intentionally skipped", encoding="utf-8")

    errors = check_rag_mirror(rag, mirror)

    assert "RAG mirror differs: changed.md" in errors
    assert "RAG mirror missing: missing.md" in errors
    assert "RAG mirror has stale file: stale.md" in errors
    assert all("README" not in error for error in errors)


def test_rag_metadata_rejects_bad_access_tag(tmp_path: Path) -> None:
    path = tmp_path / "bad.md"
    path.write_text(
        "AI_READ_ACCESS: DENIED\nCONTENT_CLASS: RAG_APPROVED\nSTATUS: DRAFT\n",
        encoding="utf-8",
    )
    errors, _ = check_rag_metadata(tmp_path)
    assert any("AI_READ_ACCESS must be ALLOWED" in error for error in errors)


def test_site_metadata_accepts_complete_review_block(tmp_path: Path) -> None:
    page = tmp_path / "topic" / "index.md"
    page.parent.mkdir()
    page.write_text(
        """---
layout: default
title: Test
description: Test page
breadcrumb: []
review:
  standard: Test standard
  edition: Test edition
  status: Review pending
  coverage: Test coverage
  last_reviewed: July 2026
---
""",
        encoding="utf-8",
    )
    errors, warnings = check_site_metadata(tmp_path)
    assert errors == []
    assert warnings == []


def test_site_metadata_rejects_retired_status(tmp_path: Path) -> None:
    page = tmp_path / "topic" / "index.md"
    page.parent.mkdir()
    page.write_text(
        """---
layout: default
review:
  standard: Test standard
  edition: Test edition
  status: Complete
  coverage: Test coverage
  last_reviewed: July 2026
---
""",
        encoding="utf-8",
    )
    errors, _ = check_site_metadata(tmp_path)
    assert any("invalid review status" in error for error in errors)
