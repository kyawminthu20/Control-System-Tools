# Phase 50 — Whole-Project Hardening & Hygiene

**Date:** 2026-07-16
**Status:** Recorded as the next phase (owner may reorder or drop workstreams)
**Source:** Whole-project audit, 2026-07-16 (four parallel review passes: toolkit, site, corpus/governance, repo hygiene), reconciled against the accepted `planning/2026-07-13-whole-project-architecture-recommendations.md`
**Relationship to Phase 49c:** Independent. Phase 49c (AI/ML layer-design pages) remains **not authorised** and its gates are unchanged by this plan.

## Audit Baseline (verified 2026-07-16)

All governed gates are green: `uv run pytest -q` **155 passed**, doctests **10 passed**, Jekyll build clean (3.22 s), **zero** broken internal links (371 rendered files), `validate_ai_boundaries.py` **374/374 pass**, RAG mirror **byte-identical** (314 files each side), `.git` healthy at 21 MB, no secrets/PII in tracked files, no licensed table values committed.

Status of the accepted 2026-07-13 recommendation:

| Row | Work package | Verdict |
|---:|---|---|
| 1 | P0.1 I/O direction through the PLC module (`YL-301` fix) | **DONE** — `Tag.io_type` carries direction; heuristic is fallback only; regression tests in `tests/cst/test_plc.py:68-101` |
| 2 | P0.2 UL 508A provenance normalization | **DONE** — zero `508A:2022` hits in `src/`, `tests/`, `docs/` source, corpus (stale local `docs/_site` only, git-ignored) |
| 3 | P0.3 RAG mirror refresh | **DONE** — mirror byte-identical |
| 4 | Release-check module + CI | **DONE** — `tools/release_check.py` (5 profiles) runs `--profile full` in `pages.yml` on push and PR |
| 5 | Licensed-table module + packaging cleanup | **NOT STARTED** → Phase 50.3 |
| 6 | Validated-I/O seam + CLI tests | **NOT STARTED** → Phase 50.2, 50.4 |
| 7 | Site metadata rollout + state cleanup | **NOT STARTED** → Phase 50.8, 50.9 |

## Priority Order

Correctness in the authoritative tier first, then prevention (validators/seams), then packaging/CLI, then hygiene, then editorial rollout. Each workstream is a bounded slice: branch → implement → full release gate → project_state update → merge.

---

## Workstream A — Corpus correctness (highest priority: source-of-truth defects)

### 50.1 Fix factual defects in authoritative corpus files

The corpus is the source of truth and these defects propagate into the site mirror and any RAG answer:

- `control-standards/rag/standards_intelligence/us/nfpa79/Ch06__overcurrent_protection.md:20,45` — body text says "Chapter 7" twice; the file is Chapter 6 (metadata is correct). Long-known, never fixed.
- `.../nfpa79/Ch15__transformers_and_power_supplies.md:37` — suspect "Table 7.2.7" citation for transformer OCPD ratios (overcurrent is Ch 6 in this corpus). Verify against the standard or flag inline as unverified; do not guess a number.
- Empty placeholder values (missing numerics): `.../nfpa79/Ch04__general_conditions_of_installation.md:23` ("between ** and ** ( to )"), `.../nfpa79/Ch17__cables_and_flexible_cords.md:28` ("typically ` to `"), `.../machinery/iec_60204_1/IEC60204_1_2016A1__Clause05__incoming_supply.md:34` ("` to ` times the nominal voltage"). Fill only from verifiable sources; otherwise replace with an explicit gap flag.
- Conversational AI artifacts in canonical files: `reference_models/Universal Machine Safety Architecture.md:395`, `reference_models/7-Layer Industrial Machine Architecture Model.md:332`, `iec_60204_1/IEC60204_1_2016A1__Clause18__verification.md:56` — strip all three.
- `iec_60204_1/README.md` is a 27-byte stub (header line only) — write a real README or delete it.

After edits: rerun `tools/generate_rag_tree.py` and the full release gate (mirror equality check will otherwise fail).

**Done when:** zero conversational artifacts and zero empty placeholders in `control-standards/rag/`; Ch06 numbering consistent; Ch15 citation verified or explicitly flagged.

### 50.2 Corpus-quality validator (prevention — root cause of 50.1 surviving three phases)

The only corpus validators today are `validate_ai_boundaries.py` (AI_READ_ACCESS + forbidden keywords) and mirror equality. Nothing catches the defect classes above. Extend `tools/release_check.py`'s corpus profile (or a new `tools/validate_corpus_quality.py` it calls) to detect:

- Conversational artifacts ("Would you like", "If you want, I can", "Shall I", "Let me know if").
- Empty-placeholder patterns ("` to `", "** and **", "( to )").
- Header completeness: `CONTENT_CLASS` and `STATUS` presence (currently reported by the gate as non-regression debt; make the target zero and then hard-fail).

Also **document the corpus header schema in governance** — `CONTENT_CLASS`/`STATUS` are used throughout the corpus but defined in none of the governance docs (`AI_WORKFLOW.md` documents only `AI_READ_ACCESS` and path tiers). Add the schema to `governance/AI_WORKFLOW.md` (or CONTENT_STANDARDS) so the rule has an owner.

**Done when:** the new checks run in the corpus/full profiles and CI; header schema documented; metadata debt (gate reports 22 missing `CONTENT_CLASS`, 37 missing `STATUS`; direct count found 13/35 — re-measure with the gate as authoritative) is driven to zero and the check flips from warn to fail.

### 50.3 `_index.yaml` reconciliation

`standards_intelligence/_index.yaml` cannot currently be trusted as a manifest:

- `cybersecurity/iec_62443/` (4 files) missing from the `standards:` inventory (only in topic routing).
- `international/offshore/` (ABS + DNV, 2 files) entirely absent.
- Case-mismatched reference: index says `reference_models/software_safety_and_intrinsic_safety_standards.md`; disk has `Software_Safety_and_Intrinsic_Safety_Standards.md` (4 references — works on macOS, breaks on case-sensitive filesystems/CI).
- `reference_models/15-Standard Minimum Compliance Stack.md` and `standards_atlas_diagrams_reference.md` not in `guidance_documents`.
- `crosswalks/overlap_notes/GENERATION_STATUS.md` frozen at "19% / IN PROGRESS" since 2026-01-15 (reality: 3 of 28 overlap notes exist). Update the tracker to reflect reality; writing the 25 missing notes stays backlog, not Phase 50 scope.

Optionally add an index-vs-disk consistency check to the corpus profile.

**Done when:** every corpus standards folder appears in the index, references resolve case-sensitively, and the tracker states the true count.

## Workstream B — Toolkit hardening (accepted slices 5–6, unchanged scope)

### 50.4 Validated-I/O application seam

Verified still open: `load_io_list` (`src/cst/panel/io_list.py:110-152`) never calls `validate()`; `generate_bom`, `generate_wire_schedule`, `generate_loop_sheets`, `modbus_map` consume points unvalidated; duplicate tags silently overwrite loop sheets (`loop_sheets.py:85` keys a dict by tag); most CLI generator commands have no validation gate; `design_package.py:56-58` reports problems but does not abort. Implement per the accepted plan: validation enforced at the seam, duplicate/collision conditions rejected before any artifact is produced.

**Done when:** every generator rejects invalid or colliding I/O before producing output, with tests for the collision fixtures.

### 50.5 Licensed-table module + packaging cleanup

Verified still open: `tables.py:56` checks only top-level `source`/`data` key presence (missing provenance passes silently via `.get(..., '?')`); no row-shape or JSON-schema validation; `DEFAULT_TABLES_DIR` assumes a source checkout; the wheel ships neither schemas nor samples; `pymupdf`/`pypdf` remain **unconditional** core dependencies despite the "stdlib-only toolkit" rule (they serve only `tools/fe_study/`). Implement per the accepted plan; move the PDF deps to an optional group.

**Done when:** malformed provenance/rows fail at load with actionable errors; a built wheel locates its schemas/samples or user data without a checkout; `uv sync` core install is stdlib-only.

### 50.6 Thin CLI adapter + missing tests

Verified still open: `src/cst/cli.py` is 486 lines (next-largest module: 169) with **zero** tests crossing the CLI seam; `src/cst/common/cite.py` (the provenance-rendering module on the citation critical path) also has no direct test — these are the only two untested modules in `src/cst`. Split application behavior out of the CLI per the accepted plan; add CLI tests (public commands, exit codes, sample-data warnings, filesystem outputs), a wheel smoke test, and direct `cite.py` tests.

**Done when:** CLI and `cite.py` are covered; `cli.py` is a thin argparse adapter.

## Workstream C — Repo hygiene

### 50.7 Root and intake cleanup

- Relocate `temp/` (24 tracked files, unsanctioned by PROJECT_ORGANIZATION): `temp/ai-ml-control-systems-research/` → `control-standards/work/research/`; `temp/wire-color-coding-web-assets/` → `docs/assets/` (or work tier if not published). Then remove `temp/`.
- Delete `main.py` (dead `uv init` scaffold; environment.md already calls it superseded).
- Untrack `lifecycle-build-page.png` (232 KB tracked binary that escapes the `control-theory-*.png` ignore) and move/rename `drawings examples/` (1.6 MB single PNG, tracked, dir name contains a space) under `docs/assets/` or `planning/`.
- Add `temp/` and screenshot patterns to `.gitignore`; extend `project_automator.py` IGNORE_DIRS if any staging dirs remain.
- Prune the 34 stale local `feat/phaseNN-*` branches (delete merged ones; list survivors).
- Fill or delete the three 0-byte `.claude/skills/{new-rag-module,promote-draft,validate-rag}/SKILL.md` stubs (advertised capabilities with no body).

**Done when:** repo root contains only governance-sanctioned entries; no tracked stray binaries; branch list legible.

### 50.8 project_state restructure (accepted slice: current state vs history)

`project_state.md` is 1,760 lines and `change_log.md` 2,241 — current facts are buried in phase narrative. Implement the accepted recommendation: keep a small current-state file (active phase, gates, owner actions, next phase); move completed-phase narrative to dated files under `project_state/history/`. Fix verified drift while at it: `environment.md` claims local Python 3.13 (actual interpreter 3.12.7; `.python-version` says 3.13 — reconcile), both docs stamp 2026-07-10 and claim stale test counts; document that fresh clones must run `tools/setup_hooks.sh` or the pre-commit STRUCTURE_SUMMARY regeneration silently never happens. Retire or narrow `tools/validate_reorg.sh` (self-described legacy migration audit) per the accepted plan.

**Done when:** current-state file ≤ ~150 lines, history preserved under `project_state/history/`, environment/how_to claims match reality.

## Workstream D — Site editorial (phased; several items are owner review work)

### 50.9 `review:` frontmatter rollout

283 of 360 content pages (79%) lack a `review:` block — entirely absent in `docs/vendor/` (58 pages) and `docs/industries/` (34 pages), which are reader-facing. Roll out in slices, per the accepted plan's rule: **do not bulk-mark pages Reviewed** — new blocks start at honest statuses. Decide whether `docs/plans/` and `docs/superpowers/` (planning artifacts, already excluded from the published site) are exempt, and record the exemption in CONTENT_STANDARDS so the release-gate debt number becomes meaningful.

### 50.10 IEC 62061 rebuild

`docs/standards/functional-safety/iec-62061/index.md` is the only page at **Needs revalidation** (since Phase 45): rebuild from the consolidated 2021+AMD1:2024+AMD2:2026 (CSV Ed. 2.2) text, not by patching. Also check it for ML content (Phase 49a follow-up).

### 50.11 Small site fixes

- Confirm the 6 double-listed URLs in `docs/_data/navigation.yml` are intentional cross-listings (commissioning-templates, wireshark-methodology, modbus-rtu-rs485, ethernet-ip, ethernet-fundamentals, dnp3); deduplicate any that aren't.
- Vendor doc links: 28/129 dead as of the 2026-07-12 liveness stamp (all bot-gated Siemens portals, publication IDs already carried as stable references) — re-run the liveness check and annotate rather than delete.
- Consider splitting the 90 KB+ lifecycle pages (`commissioning` 95 KB, `maintenance` 91 KB) — low priority, only if editing friction is felt.

## Explicitly Out of Scope / Unchanged Gates

- **Phase 49c stays not authorised.** Chemical/biological authority ceilings still have zero adversarial coverage; owner authorisation required before layer-design pages.
- **Owner actions outstanding (carried forward, not agent-executable):** review the two Phase 48 pages and the Phase 45 Review-pending set; settle the three UNVERIFIABLE purchased-text items; confirm legacy-panel photo provenance; purchase ISO/IEC TR 5469:2024; confirm/overrule `/design/ai-integration/` placement (page shipped there at Review pending).
- Writing the 25 missing crosswalk overlap notes and an indexed IEC 61131-3 standards module (currently covered only pedagogically in `training_modules/plc_software/`) are content backlog, not Phase 50.

## Definition of Done (phase level)

1. Zero conversational artifacts, empty placeholders, or known numbering/citation defects in `control-standards/rag/`; new corpus-quality checks enforce this in CI.
2. `_index.yaml` is a trustworthy, case-correct manifest.
3. Accepted slices 5–7 from the 2026-07-13 plan are implemented (validated-I/O seam, licensed-table module + stdlib-only core install, thin tested CLI, project_state split).
4. Repo root matches PROJECT_ORGANIZATION; `temp/` gone; stale branches pruned.
5. Corpus metadata debt at zero and the gate check hard-fails on regressions; `review:` rollout underway with an agreed exemption list.
6. Full release gate green locally and in CI at every merge.
