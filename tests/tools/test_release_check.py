"""Tests for the governed release-check module."""

from __future__ import annotations

from pathlib import Path

from tools.release_check import (
    check_site_badges,
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


def test_site_metadata_accepts_documented_exemption(tmp_path: Path) -> None:
    page = tmp_path / "stub" / "index.md"
    page.parent.mkdir()
    page.write_text(
        '---\ntitle: Moved\nreview_exempt: "redirect stub — no content"\n---\n',
        encoding="utf-8",
    )
    errors, warnings = check_site_metadata(tmp_path)
    assert errors == []
    assert warnings == []


def test_site_metadata_rejects_exemption_without_reason(tmp_path: Path) -> None:
    page = tmp_path / "stub" / "index.md"
    page.parent.mkdir()
    page.write_text("---\ntitle: Moved\nreview_exempt:\n---\n", encoding="utf-8")
    errors, _ = check_site_metadata(tmp_path)
    assert any("requires a documented reason" in error for error in errors)


def test_site_metadata_rejects_exemption_alongside_review_block(tmp_path: Path) -> None:
    page = tmp_path / "stub" / "index.md"
    page.parent.mkdir()
    page.write_text(
        """---
title: Both
review_exempt: "nav page"
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
    errors, _ = check_site_metadata(tmp_path)
    assert any("both review: and review_exempt:" in error for error in errors)


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


def _badge_corpus(tmp_path: Path) -> Path:
    """Minimal standards_intelligence tree for badge-honesty tests."""
    rag = tmp_path / "rag"
    intel = rag / "standards_intelligence"
    nec = intel / "us" / "nec"
    hazloc = intel / "international" / "hazardous_area" / "iec_60079"
    nec.mkdir(parents=True)
    hazloc.mkdir(parents=True)
    (intel / "_index.yaml").write_text(
        """standards:
  us:
    - standard_id: "NEC_2023"
      folder: "us/nec"
      status: "complete"
  international:
    hazardous_area:
      - standard_id: "IEC_60079"
        folder: "international/hazardous_area/iec_60079"
        status: "complete"
    functional_safety:
      - standard_id: "IEC_61511_2016"
        folder: "international/functional_safety/iec_61511"
        status: "draft"
""",
        encoding="utf-8",
    )
    (nec / "NEC_2023__Art500__hazardous_locations_general.md").write_text(
        "AI_READ_ACCESS: ALLOWED\n", encoding="utf-8"
    )
    (nec / "NEC_2023__Art700_702__emergency_standby_systems.md").write_text(
        "AI_READ_ACCESS: ALLOWED\n", encoding="utf-8"
    )
    (hazloc / "IEC60079_10_1__area_classification_gas.md").write_text(
        "AI_READ_ACCESS: ALLOWED\n", encoding="utf-8"
    )
    return rag


def _badge_page(tmp_path: Path, body: str) -> Path:
    docs = tmp_path / "docs"
    page = docs / "topic" / "index.md"
    page.parent.mkdir(parents=True)
    page.write_text(body, encoding="utf-8")
    return docs


def test_site_badges_rejects_retired_labels_and_phase_badges(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '<span class="badge badge--complete">Complete</span>\n'
        '<span class="badge badge--gap">Not in corpus</span>\n'
        '<span class="badge badge--new">Phase 22</span>\n',
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert sum("retired badge label" in error for error in errors) == 3


def test_site_badges_allows_longform_gap_flags(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '<span class="badge badge--verify">IEC 60092 not in corpus — class rules summary only</span>\n',
    )
    assert check_site_badges(docs, _badge_corpus(tmp_path)) == []


def test_site_badges_accepts_verified_module_and_article(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '| US route | NEC Art. 500, 700 | <span class="badge badge--reviewed">Reviewed</span> |\n'
        '| Zone classification | IEC 60079-10-1 | <span class="badge badge--reviewed">Reviewed</span> |\n',
    )
    assert check_site_badges(docs, _badge_corpus(tmp_path)) == []


def test_site_badges_rejects_article_missing_from_corpus(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '| US route | NEC Art. 500, 501 | <span class="badge badge--reviewed">Reviewed</span> |\n',
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert any("NEC Art. 501" in error for error in errors)


def test_site_badges_rejects_part_missing_from_corpus(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '| Dust | IEC 60079-10-2 | <span class="badge badge--reviewed">Reviewed</span> |\n',
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert any("IEC 60079-10-2" in error for error in errors)


def test_site_badges_rejects_incomplete_module(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '| SIS lifecycle | IEC 61511 | <span class="badge badge--reviewed">Reviewed</span> |\n',
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert any("iec_61511" in error and "not marked complete" in error for error in errors)


def test_site_badges_rejects_unresolvable_reviewed_claim(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        '| Mystery topic | <span class="badge badge--reviewed">Reviewed</span> |\n',
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert any("no resolvable standard" in error for error in errors)


def test_site_badges_resolves_standard_from_preceding_lines(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        "### IEC 60079 — Explosive Atmospheres\n\n"
        '**Status:** <span class="badge badge--reviewed">Reviewed</span>\n',
    )
    assert check_site_badges(docs, _badge_corpus(tmp_path)) == []


def test_site_badges_checks_plain_reviewed_table_cells(tmp_path: Path) -> None:
    docs = _badge_page(
        tmp_path,
        "| Mystery standard | somewhere | Reviewed |\n"
        "| Reviewed by | supervisor |\n",
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert sum("no resolvable standard" in error for error in errors) == 1


def test_site_badges_rejects_retired_labels_in_shared_includes(tmp_path: Path) -> None:
    docs = _badge_page(tmp_path, "no badges here\n")
    includes = docs / "_includes"
    includes.mkdir()
    (includes / "legend.html").write_text(
        '<span class="badge badge--gap">Not yet covered</span>\n', encoding="utf-8"
    )
    errors = check_site_badges(docs, _badge_corpus(tmp_path))
    assert any("legend.html" in error and "retired badge label" in error for error in errors)
