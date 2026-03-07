# Phase 3 Design — Functional Safety Standards Deep Coverage

**Date:** 2026-03-06
**Status:** Approved
**Scope:** Five functional safety standards — ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511

---

## Goal

Upgrade all five functional safety standard pages from shallow stubs (with "PLANNED — TO VERIFY" badges) to full-depth reference pages, backed by a clause-level RAG corpus.

---

## Approach: Hybrid (RAG corpus + site pages, dependency-ordered)

For each standard:
1. Create structured RAG corpus files (`control-standards/rag/`) at clause level
2. Deepen the site page (`docs/standards/functional-safety/`) using those files as the authoritative source
3. Update badge from `PLANNED` to `Phase 3 Complete`
4. Commit group as a unit and update `project_state/`

---

## Architecture

### RAG Corpus Structure

```
control-standards/rag/standards_intelligence/international/functional_safety/
  iso_12100/
    _index.yaml
    ISO12100_2010__Clause04__risk_assessment_principles.md
    ISO12100_2010__Clause05__risk_estimation.md
    ISO12100_2010__Clause06__risk_evaluation.md
    ISO12100_2010__Clause07__risk_reduction.md
    ISO12100_2010__AnnexA__hazard_list.md
  iso_13849_1/
    _index.yaml
    ISO13849_2023__Clause04__design_strategy.md
    ISO13849_2023__Clause05__srp_cs.md
    ISO13849_2023__Clause06__categories.md
    ISO13849_2023__Clause07__validation.md
    ISO13849_2023__AnnexA__risk_assessment.md
    ISO13849_2023__AnnexF__ccf.md
  iec_62061/
    _index.yaml
    IEC62061_2021__Clause04__scope_context.md
    IEC62061_2021__Clause06__srecs_design.md
    IEC62061_2021__Clause07__subsystem_design.md
    IEC62061_2021__AnnexA__silcl_tables.md
  iec_61508/
    _index.yaml
    IEC61508_2010__Part1__framework.md
    IEC61508_2010__Part2__hardware.md
    IEC61508_2010__Part3__software.md
    IEC61508_2010__Clause07__safety_lifecycle.md
  iec_61511/
    _index.yaml
    IEC61511_2016__Part1__framework.md
    IEC61511_2016__Clause09__sis_design.md
    IEC61511_2016__Clause11__lopa.md
    IEC61511_2016__AnnexA__risk_assessment.md
```

### Site Page Structure (per standard)

Each deepened page targets ~300–350 lines and follows this template:

1. **Page header** — badge updated to "Phase 3 Complete"
2. **Standard Overview table** (existing, retained)
3. **Quick-Start** — 3–5 bullets for practitioners new to the standard
4. **Key Clauses** — expanded table with one-line clause summaries
5. **Technical Reference**
   - Decision/lookup tables (e.g. Category → achievable PL, SIL → PFHd range)
   - Key parameters defined (MTTFd, DC, CCF, PFHd, SILCL, etc.)
   - Key formulas where applicable
6. **When To Use This Standard** — comparison vs. closest alternative, crosswalk links
7. **Common Mistakes** — 4–6 practical pitfalls
8. **Practical Checklist** — yes/no items for a typical project
9. **Lifecycle Application** (existing section, expanded)

---

## Delivery Groups

### Group 1 — ISO 12100 (foundation)

**Why first:** ISO 12100 underpins all other standards in this list. Every other page references it.

RAG files (6):
- `_index.yaml`
- `ISO12100_2010__Clause04__risk_assessment_principles.md`
- `ISO12100_2010__Clause05__risk_estimation.md`
- `ISO12100_2010__Clause06__risk_evaluation.md`
- `ISO12100_2010__Clause07__risk_reduction.md`
- `ISO12100_2010__AnnexA__hazard_list.md`

Site page: `docs/standards/functional-safety/iso-12100/index.md` — ~300 lines
Commit: `feat: phase3 group1 — ISO 12100 RAG corpus and deepened site page`

---

### Group 2 — ISO 13849-1 + IEC 62061 (PL/SIL decision pair)

**Why together:** These two are the primary daily-use standards for machinery safety functions. Practitioners must choose between PL and SIL — the pages are more useful when each explains the other.

ISO 13849-1 RAG files (7):
- `_index.yaml`
- `ISO13849_2023__Clause04__design_strategy.md`
- `ISO13849_2023__Clause05__srp_cs.md`
- `ISO13849_2023__Clause06__categories.md`
- `ISO13849_2023__Clause07__validation.md`
- `ISO13849_2023__AnnexA__risk_assessment.md`
- `ISO13849_2023__AnnexF__ccf.md`

IEC 62061 RAG files (5):
- `_index.yaml`
- `IEC62061_2021__Clause04__scope_context.md`
- `IEC62061_2021__Clause06__srecs_design.md`
- `IEC62061_2021__Clause07__subsystem_design.md`
- `IEC62061_2021__AnnexA__silcl_tables.md`

Site pages:
- `docs/standards/functional-safety/iso-13849-1/index.md` — ~350 lines
- `docs/standards/functional-safety/iec-62061/index.md` — ~350 lines
- Both include a shared "PL vs SIL" comparison section with cross-links

Commit: `feat: phase3 group2 — ISO 13849-1 + IEC 62061 RAG corpus and deepened site pages`

---

### Group 3 — IEC 61508 + IEC 61511 (parent/process pair)

**Why together:** IEC 61508 is the parent standard referenced by 62061 and 61511. IEC 61511 is the process industry application of 61508. They share safety lifecycle concepts and are typically reference-only for machinery users.

IEC 61508 RAG files (5):
- `_index.yaml`
- `IEC61508_2010__Part1__framework.md`
- `IEC61508_2010__Part2__hardware.md`
- `IEC61508_2010__Part3__software.md`
- `IEC61508_2010__Clause07__safety_lifecycle.md`

IEC 61511 RAG files (5):
- `_index.yaml`
- `IEC61511_2016__Part1__framework.md`
- `IEC61511_2016__Clause09__sis_design.md`
- `IEC61511_2016__Clause11__lopa.md`
- `IEC61511_2016__AnnexA__risk_assessment.md`

Site pages:
- `docs/standards/functional-safety/iec-61508/index.md` — ~300 lines, framed as parent reference
- `docs/standards/functional-safety/iec-61511/index.md` — ~300 lines, framed as process industry application
- IEC 61508 page links to 62061 and 61511 as "where to apply this"
- IEC 61511 page links to the process skid scenario page

Commit: `feat: phase3 group3 — IEC 61508 + IEC 61511 RAG corpus and deepened site pages`

---

## Constraints

- RAG corpus files are AI-readable structured Markdown — clause summaries, key concepts, decision tables
- Site pages are presentation only — paraphrase and surface the corpus; never modify RAG content
- No new Jekyll plugins, no new JS dependencies
- All changes are additive — no existing pages removed or restructured
- `project_state/` updated after each group commit

---

## Success Criteria

- All five functional safety pages have no "PLANNED — TO VERIFY" badges
- Each page has a Quick-Start, Technical Reference, Common Mistakes, and Practical Checklist section
- Each RAG standard directory has an `_index.yaml` and clause-level `.md` files
- Jekyll build remains clean (0 errors, 0 warnings)
- `project_state/project_state.md` reflects Phase 3 in progress / complete after each group
