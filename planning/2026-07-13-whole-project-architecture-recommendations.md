# Whole-Project Architecture Recommendations — Phase 49b Hardening Gate

**Date:** 2026-07-13  
**Status:** Accepted into the next-phase handoff  
**Scope:** `src/cst/`, `tests/`, `docs/`, `control-standards/rag/`, `tools/`, CI, and `project_state/`  
**Relationship to Phase 49b:** Complete the P0 gate below before implementing the AI/ML method register. The remaining work packages may proceed as bounded hardening slices alongside Phase 49b when they do not disturb its authority-first content work.

## Executive Recommendation

Keep the repository's existing three-part architecture:

1. `control-standards/rag/` is the canonical reference library.
2. `docs/` is the presentation layer.
3. `src/cst/` is the standards-cited engineering toolkit.

The project does not need a structural rewrite. It needs stronger enforcement at the seams where canonical knowledge becomes published content or calculated output. The recommended sequence is:

1. Correct the confirmed I/O-direction defect and standards-edition drift.
2. Centralize standards provenance so the same drift cannot recur independently in code, corpus, and site pages.
3. Put every governed verification gate behind one release-check Module and run it in CI.
4. Deepen licensed-table loading into a validated, installable Module.
5. Make validated I/O the required application Seam for every generator.
6. Separate current operational state from historical phase narrative.

This order puts incorrect engineering output first, factual provenance second, and systemic prevention third.

## Baseline Evidence

The analysis found a healthy baseline:

- `uv run pytest -q`: **145 passed**.
- `uv run pytest -q --doctest-modules src/cst`: **10 passed**.
- Jekyll build: **clean**.
- Internal link check: **zero broken links across 370 rendered HTML files**.
- AI-boundary validation: **372 scanned files passed**.
- Canonical and mirrored RAG trees: **314 publishable Markdown files each**, but two mirrored files differ from their canonical copies.

The green baseline does not cover several governed properties. In particular, deployment CI builds Jekyll but does not run the Python suite, doctests, link checker, AI-boundary validator, site-frontmatter checks, or generated-mirror comparison.

## P0 — Correctness and Provenance Gate

Complete all three items before Phase 49b begins implementation work.

### P0.1 Preserve I/O direction through the PLC Module

**Files:**

- `src/cst/panel/io_list.py`
- `src/cst/plc/tag_db.py`
- `src/cst/plc/address_map.py`
- `tests/cst/test_plc.py`
- `data/examples/io_list_example.csv`

**Problem:** The `IOPoint` Interface distinguishes DI, DO, AI, and AO, but that direction is discarded when an `IOPoint` becomes a PLC tag. The Modbus mapping Implementation then guesses writability from substrings such as `CMD`, `SOL`, and `FCV`. The shipped digital output `YL-301` is consequently emitted as a Modbus discrete input.

**Recommendation:** Preserve explicit I/O direction or access semantics through the PLC Module and make name-based classification an explicit fallback only when no authoritative direction exists.

**Benefits:**

- Locality: protocol access decisions live in one place.
- Leverage: every tag export and address map receives correct semantics.
- Tests: assert mapping for every example DI, DO, AI, and AO, including names with no favorable heuristic substring.

### P0.2 Normalize UL 508A provenance

**Files:**

- `src/cst/calc/sccr.py`
- `src/cst/panel/nameplates.py`
- affected `docs/` pages
- affected `control-standards/rag/standards_intelligence/` records

**Problem:** The verified project record says there is no `UL 508A:2022` edition, while that label remains in calculator citations, nameplate output, site pages, and canonical corpus administration material.

**Recommendation:** Perform one governed provenance sweep using the verified edition/revision form already established by Phase 45. Do not rename corpus files merely to improve appearance; separate historical filenames from displayed provenance where necessary.

**Benefits:**

- Locality: one verified fact is applied consistently across all consumers.
- Leverage: generated engineering output and published guidance agree.
- Tests: add assertions over emitted citations, not only numeric results.

### P0.3 Refresh and verify the RAG mirror

**Problem:** The two trees have the same file count, but the mirrored copies of `process_safety_details/IEC61511.md` and `process_safety_details/UPW_water_skid_scenario.md` differ from canonical files.

**Recommendation:** Regenerate with `tools/generate_rag_tree.py`, then compare canonical and mirrored publishable Markdown by relative path and content.

**Benefits:** Readers see the current canonical metadata and content; future verification detects content drift rather than merely comparing counts.

## Deepening Opportunities

### 1. Governed standards-provenance Module

**Files:** `src/cst/common/cite.py`, calculator and generator modules, standards metadata, and provenance tests.

**Problem:** Standards identifiers and editions are repeated as free-form strings. `CalcResult` also permits standards-derived results with empty citation lists.

**Recommendation:** Concentrate verified identifiers, edition/revision metadata, and citation rendering in one Module. Standards-derived artifacts should cross this Seam instead of recreating display text independently.

**Benefits:** Greater Depth hides edition-formatting and provenance rules behind a small Interface. Callers gain Leverage, while maintainers gain Locality for standards updates.

### 2. Release-check Module

**Files:** `.github/workflows/pages.yml`, `tools/`, test configuration, and governance documentation.

**Problem:** Required checks are separate commands, several governed properties have no validator, and CI runs only the Jekyll build.

**Recommendation:** Provide one read-only release-check Module with scoped profiles for toolkit, site, corpus, templates, and full-repository verification. Run the full profile before deployment and on pull requests.

The full profile should cover:

- Python tests and doctests.
- Jekyll build and rendered-link checking.
- AI access metadata and forbidden-path rules.
- `CONTENT_CLASS` and `STATUS` metadata.
- Site `review:` frontmatter and five-term status vocabulary.
- Internal-link style.
- Canonical-to-generated mirror equality.
- Generated-artifact cleanliness.

**Benefits:** One Interface provides high Leverage across local work and CI. Failures become reproducible, and verification knowledge gains Locality.

### 3. Licensed-table Module: locate, validate, normalize

**Files:** `src/cst/common/tables.py`, JSON schemas, samples, packaging configuration, calculator callers, and table tests.

**Problem:** Loading checks only the presence of top-level `source` and `data` keys. It does not enforce required provenance fields or row shapes. The default data path assumes a source checkout, while wheel packaging omits schemas and samples. PDF extraction dependencies are also installed unconditionally despite the stdlib-only toolkit rule.

**Recommendation:** Make one Module own table-location policy, schema validation, typed provenance, row normalization, SAMPLE/design-use behavior, and installed-package resources. Move FE-study dependencies out of the core install.

**Benefits:** Copyright and provenance rules gain Locality; every current and future data-dependent calculator gains Leverage; malformed transcriptions fail at the table Seam with actionable `ValueError`s.

### 4. Validated-I/O application Seam

**Files:** `src/cst/panel/io_list.py`, CLI consumers, panel/commissioning/PLC/document generators, and their tests.

**Problem:** I/O validation is optional caller knowledge. Most CLI generators load and consume data without validating it. Duplicate tags can silently overwrite generated loop sheets because tag names are dictionary keys.

**Recommendation:** Require validated I/O before downstream generation and reject duplicate/collision conditions before any artifacts are produced.

**Benefits:** Validation ordering gains Locality. All generators and future Adapters receive the same invariants, increasing Leverage and shrinking their test setup.

### 5. Thin CLI Adapter with shipped-distribution tests

**Files:** `src/cst/cli.py`, command modules, packaging configuration, and new CLI/wheel tests.

**Problem:** The 486-line CLI mixes parser declarations, application behavior, formatting, exit-code policy, and filesystem effects. Tests call library functions but never cross the public CLI or installed-wheel Seam.

**Recommendation:** Keep argparse as the CLI Adapter while moving application behavior and artifact generation behind domain Modules. Add tests for public commands, exit codes, sample-data warnings, filesystem outputs, and wheel installation.

**Benefits:** Errors and output policy gain Locality; the same application behavior can serve Python and future Adapters without duplicating engineering logic.

### 6. Current-state Module and historical phase records

**Files:** `project_state/project_state.md`, `project_state/change_log.md`, `governance/ROADMAP.md`, and `tools/validate_reorg.sh`.

**Problem:** Current state is mixed with extensive completed-phase narrative. Test counts and lifecycle counts have drifted, and the legacy reorganization validator checks obsolete artifacts while invoking a writer during validation.

**Recommendation:** Keep a small current-state Interface for active phase, gates, owner actions, and next phase. Move durable completed-phase narrative into dated history records. Retire or replace the stale reorganization validator with read-only checks owned by the release-check Module.

**Benefits:** The handoff contract becomes dependable; current facts gain Locality; automated checks can validate counts and commands without parsing a large historical document.

## Phase 49b Execution Sequence

| Order | Work package | Phase 49b relationship | Required verification |
|---:|---|---|---|
| 1 | P0.1 I/O-direction correction | Blocking prerequisite | Targeted regression tests + full pytest + doctests |
| 2 | P0.2 UL 508A provenance normalization | Blocking prerequisite | Citation sweep + affected tests + site/corpus gates |
| 3 | P0.3 RAG mirror refresh | Blocking prerequisite | Exact mirror comparison + boundary validator |
| 4 | Release-check Module and CI adoption | Before Phase 49b merge | Full profile green locally and in CI |
| 5 | Licensed-table Module and package cleanup | Bounded hardening slice | Malformed-data tests + wheel smoke test |
| 6 | Validated-I/O Seam and CLI tests | Bounded hardening slice | Invalid/collision fixtures + CLI acceptance tests |
| 7 | Site metadata rollout and state cleanup | Phased; do not bulk-mark pages Reviewed | Jekyll + links + governed metadata validator |
| 8 | AI/ML method register implementation | Existing Phase 49b scope | Existing authority and source gates remain binding |

## Definition of Done

- The example DO `YL-301` maps as writable without relying on its name.
- No live code or site prose presents `UL 508A:2022` as an edition.
- Canonical and mirrored RAG Markdown match exactly for publishable files.
- CI runs the governed release profile before deployment.
- Normal `uv run pytest` includes the required doctest policy or CI runs it explicitly.
- Invalid licensed-table provenance and rows fail at load time with actionable errors.
- A built wheel can locate its schemas/samples or clearly locate user data without assuming a repository checkout.
- Every generator rejects invalid or colliding I/O before producing output.
- Project-state test counts and active lifecycle claims are current.
- AI/ML Phase 49b authority, placement, source, and safety-independence gates remain unchanged unless the owner explicitly changes them.

## Deferred Decisions

This recommendation deliberately does not choose detailed Interfaces for the deepened Modules. Those choices should be made while implementing each vertical slice, after confirming caller requirements and test surfaces. It also does not resolve the owner decision on `/design/ai-integration/`, purchase ISO/IEC TR 5469:2024, or relax any AI/ML authority ceiling.
