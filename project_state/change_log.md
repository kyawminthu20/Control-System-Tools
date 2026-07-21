# Project Change Log

**Last Updated:** 2026-07-20 (Phase 52.4b COMPLETE — review-metadata debt at zero)
**Status:** Active

## 2026-07-20 — Phase 52.4b tranche 3 (fundamentals + design + tools) — ROLLOUT COMPLETE

**Type:** Site metadata only. **No technical claim changed; no page marked Reviewed.**

- **77 `Review pending` blocks added:** the 6 training section hubs; 9 electrical-theory,
  13 control, and 16 motors modules ("established theory/practice — no single governing
  standard", with NEC-adjacent conductor-ampacity and IEC-earthing modules called out
  individually, and the interlocks module explicitly routing safety-rated design to
  ISO 13849-1 / IEC 62061); the 11 NEC-application modules ("taught against the NEC 2023
  corpus basis; the locally enforceable edition governs — verify with the AHJ"; "worked as
  education, not a code determination"); the 12 design pages (original reference models
  labelled as editorial, not normative); and the remaining tools/landing pages (toolkit page
  notes SAMPLE-data and user-supplied licensed tables; glossary defers to each standard's own
  definitions). The RAG browser is `review_exempt` (interactive corpus browser — status lives
  in each file's corpus header).
- **Baseline ratcheted 78 → 0.** Every site page now carries either a governed `review:` block
  or a documented `review_exempt` reason; a page with neither is a hard release failure. The
  release gate now runs with **zero warnings** for the first time.
- Verified: full release gate PASSED clean (303 tests, 10 doctests, clean build, zero broken
  links, zero warnings); rendered boxes spot-checked on NEC-application, control, and design
  pages.

## 2026-07-20 — Phase 52.4b tranche 2 (review metadata: lifecycle stages + industries)

**Type:** Site metadata only. **No technical claim changed; no page marked Reviewed.**

- **50 `Review pending` blocks added:** the 16 lifecycle pages (hub, general, and the 14 stage pages —
  each `standard:` names the stage's governing standards, practice-level stages say so explicitly,
  and coverage lines state "stage guidance, not a performed assessment/verification") and all 34
  industries pages (the overlay matrix + 9 industry overviews — medical/nuclear/food-and-beverage
  blocks preserve the pages' own corpus-gap flags; the 8 water/wastewater pages framed as control
  patterns with "site design / permits govern"; the 16 semiconductor facility pages framed as
  practice-level with "site codes and the AHJ govern", SEMI F-series and S6/NFPA 318 cited only where
  the page cites them).
- **Baseline ratcheted 128 → 78.** Remaining backlog: fundamentals 56, design 12, plus about,
  communications landing, fundamentals/plc-software landing, glossary, rag-browser, reference-hub,
  engineering-toolkit, troubleshooting pages.
- Verified: full release gate PASSED (303 tests, clean build, zero broken links, zero metadata
  errors).

## 2026-07-20 — Phase 52.4b tranche 1 (review-metadata rollout, risk order)

**Type:** Site metadata + release tooling. **No technical claim changed; no page marked Reviewed**
(every new block is `Review pending` — only the owner may mark Reviewed).

- **Governed exemption mechanism:** pages that are pure navigation or redirect stubs may declare
  `review_exempt: "<reason>"` instead of a `review:` block. `tools/release_check.py` enforces it
  (reason mandatory; declaring both keys is an error) with 3 new tests (suite 300 → 303); rule
  documented in `governance/CONTENT_STANDARDS.md` §4. Exempted with documented reasons: the six
  redirect stubs (`repository/`, `training/`, `troubleshooting/`, `verification/`,
  `implementation/`, `field-engineering/`) and the homepage (home-layout navigation hub — its
  decision claims link to pages that hold the governed metadata).
- **31 review blocks added in the recommendation's risk order:** the Standards Finder + all 9
  scenario pages (routing scenarios — coverage lines state "selection guidance, not a compliance
  determination"); the 5 remaining crosswalk pages; the standards landing + 6 family index pages
  ("routing page — editions recorded on the child standard pages"); and all 9 commissioning-guide
  pages (checklists honestly framed as "reminder layer — OEM instructions and the site electrical
  safety program govern"). Editions are stated only where the page itself pins them (e.g.
  NFPA 79:2024 ↔ IEC 60204-1:2016+AMD1:2021 crosswalk); otherwise recorded as "exact governing
  revisions not yet recorded" per CONTENT_STANDARDS §4. `last_reviewed` = the page's last
  content-commit month.
- **Baseline ratcheted 166 → 128** (`MAX_SITE_PAGES_WITHOUT_REVIEW`); any regression now fails the
  release gate. Remaining backlog by section: fundamentals 56, industries 34, lifecycle stages 20,
  tools 8, design 12, plus section landings — next tranches.
- **Follow-on identified (not done here):** ~60 corpus-status "Reviewed" badges sit inside page
  tables (industries, standards indexes, crosswalks, scenarios). They are corpus-module claims per
  the /about/ vocabulary, distinct from page review status, but the 52.4 recommendation's
  badge-honesty audit (verify each against `_index.yaml`, prefer computed summaries) is still open
  and should be its own slice.
- Verified: full release gate PASSED (303 tests, 10 doctests, clean Jekyll build, zero broken
  links); review boxes confirmed rendering on scenario and commissioning pages (field-checklist
  layout inherits default).

## 2026-07-20 — Phase 52.3 (Task-first information architecture)

**Type:** Site navigation/IA only. **No technical content, corpus note, register value, or authority
ceiling changed.** The owner-directed next Phase 52 slice (decision recorded 2026-07-17).

- **Section-local sidebars extended beyond the training pilot** to Standards, Design, Lifecycle,
  Communications, and Tools. New generic include `docs/_includes/sidebar-section-local.html` is driven
  by `_data/navigation.yml` sections flagged `local_sidebar: true`; the router
  (`_includes/sidebar.html`) keeps the training pilot at priority 1, the new section sidebars at
  priority 2, and the global sidebar as fallback for everything else (Fundamentals non-pilot pages,
  Industries, Home). Each local sidebar shows the parent landing page + section description, the page
  sequence (flat children as one ordered list; grouped children as collapsible buckets with counts and
  an Overview link), the active page with `aria-current` and the injected on-page outline
  (`[data-local-toc]`, reusing the existing main.js hooks and bucket-state persistence), and a new
  **Related workflows** block (`related_workflows` per section in navigation.yml).
- **Homepage restructured task-first:** first journey is now hero → Start here → scenarios →
  lifecycle ribbon; the standards-family cards, industry tiles, and the power-user graph/source-browser
  details moved into a secondary **Explore the field guide** region (headings demoted to h3).
- **Section landing pages** (Standards, Design, Lifecycle, Communications, Tools) each gained a
  `section-guide` block with **Use this when / Start here / Next step** rows; links verified by the
  site link checker.
- **Search now available at every viewport** (52.3 acceptance): below 768px the topnav search box was
  `display: none`; it now flexes into the row freed by the hidden nav links. CSS-only; the full 52.2
  mobile drawer/responsive-context work stays deferred pending device verification.
- No top-level navigation section added or removed; taxonomy order unchanged; no page orphaned.
- Verified: full release gate PASSED (300 tests, 10 doctests, clean Jekyll build, 378 files
  link-checked, boundary/quality checks green, legacy review-block warning at the pre-existing 166
  baseline); desktop + 375px mobile rendering spot-checked in a real browser (local sidebar buckets,
  active-page outline, related workflows, mobile search box all render).

## 2026-07-20 — Digital-twin arc deployed (delivery tail)

**Type:** Delivery only — no code or content change. The five arc commits (49d evidence closure,
53.1 maturity ladder, 53.2 `src/cst/twin/`, 53.3 published contract schema, plus the fixed-point
timestamp fix `a4d9c1c`) were pushed to `master` after a green full release gate (300 tests,
10 doctests, clean Jekyll build, 378 files link-checked, boundary/quality checks green; legacy
review-block warning at the pre-existing 166 baseline). GitHub Pages run `29746024901` completed
**success**; live-verified 200 on `/design/ai-integration/digital-twin/`,
`/assets/templates/twin_data_contract.schema.json`, and
`/assets/templates/twin_payload_example.json` (schema content spot-checked). Outstanding items are
unchanged: owner review of the Review-pending AI-integration pages, the 49c chem/bio register
decision, and the Phase 52.3 task-first IA slice.

## 2026-07-19 — Phase 53.3 (Twin data-contract schema + worked payload on the site)

**Type:** Site + tooling. **No authority ceiling, register value, or contract field changed.** Slice 4 of
4 — **the digital-twin deepening arc is complete.** Suite **297 → 300 tests**.

Published the data contract as a machine-readable artifact, generated from the same `FIELD_SPECS` the
validator enforces so the two cannot drift.

- **`tools/generate_site_templates.py`** gains `_write_twin_contract()`: writes
  `docs/assets/templates/twin_data_contract.schema.json` (JSON Schema draft 2020-12, banner carried in
  `$comment`) and `twin_payload_example.json`. The generator **asserts the worked payload still validates**
  before writing it, so a contract change that orphans the example fails generation rather than shipping.
- **Defect caught during the slice:** the first version prepended a `$comment` banner to the payload —
  which, with `additionalProperties: false`, made the published example violate the very schema it
  demonstrates. The payload is now published verbatim; the banner lives in the schema, where `$comment`
  is a legal keyword rather than instance data. Three regression tests lock this down (published schema
  equals generated schema; published payload validates; published payload carries no banner key).
- **Corpus** `digital_twin.md` §5 gains one sentence recording that the contract is implemented as an
  executable check with a generated schema, so the site change stays a distillation. Mirror regenerated.
- **Site:** the digital-twin page's data-contract section gains a download block for both files plus the
  `cst twin-sync` cross-link; `/tools/templates/` gains two rows under AI & Model Lifecycle. Both pages
  state plainly that schema-validity is never a safety verdict and that the ceiling comes from the method
  register, not the payload's own claim. Digital-twin page stays **Review pending**.

**Arc summary (49d → 53.1 → 53.2 → 53.3):** evidence closure found a published NIST ladder that had been
sitting unextracted in our own source list; the maturity ladder shipped with its citation split by axis;
the prose contract became a runnable check; the check's field definitions became the published schema.
**No ceiling moved at any point.** Full release gate green.

## 2026-07-19 — Phase 53.2 (`src/cst/twin/` — the data contract as an executable check)

**Type:** Toolkit. Stdlib-only, no new dependency. **No authority ceiling or register value changed.**
Slice 3 of the digital-twin deepening arc. Suite **226 → 297 tests** (+71), 10 doctests.

Turned the corpus note's prose data contract (§5) and data-integrity steps (§3 steps 2 and 4) into code
that can be run against a real payload and a real telemetry file.

- **`src/cst/twin/contract.py`** — `FIELD_SPECS` (19 required + 7 optional fields) is the single
  definition of the contract; `validate_payload()` returns every violation named by field, in the
  `io_list.validate()` convention. Checks: missing/mistyped/unknown fields, closed `value_kind`
  vocabulary, inference-cannot-precede-observation, authority within 0–5, **authority vs the register
  ceiling naming both numbers**, and staleness against an injected `now`. **Level 5 is flagged
  unconditionally** — no configured ceiling can authorize it, because the ladder assigns it to no
  learned twin output. `bool` is explicitly excluded from integer fields so `True` cannot read as
  authority level 1.
- **`authority_ceilings()`** parses `methods.yml` (JSON-as-YAML — `json.loads` reads it, no PyYAML).
  **`Planned` rows are excluded rather than treated as 0** — no ceiling established is a different claim
  from a ceiling of zero, and the CLI says which case it hit rather than letting it read as a typo.
- **`schema()`** generates JSON Schema draft 2020-12 from the same `FIELD_SPECS`, so the schema Slice 4
  publishes cannot drift from the validator (tested both directions).
- **`src/cst/twin/sync_health.py`** — measures gaps, out-of-order arrivals, staleness, mean/max clock
  skew, and **skew drift** (stdlib least-squares) over `(source_ts, acquisition_ts)` pairs. Samples are
  analysed in arrival order deliberately: sorting first would erase the out-of-order condition §3 step 4
  requires be detected. `report()` follows `CalcResult.report()` and carries its corpus citation.
- **CLI:** `cst twin-validate` and `cst twin-sync`, flat-hyphenated per existing convention; exit 1 on
  problems/warnings, 2 on bad input. Worked examples committed at
  `data/examples/twin_payload_example.json` and `twin_sync_example.csv` (60 samples with a seeded 12 s
  dropout and slow clock drift).
- **Design stance, stated in the module docstrings and on the toolkit page:** these **report and never
  act.** A clean result means a proposal is well-formed enough for a gate to judge — never that it is
  safe or authorized. The gate itself is plant-side engineering, not a Python library.
- One real defect caught during integration: `cst.twin` re-exports a `sync_health` *function* that
  shadows the submodule of the same name, so the CLI imports from the submodule directly (commented).

Full release gate green.

## 2026-07-19 — Phase 53.1 (Twin maturity ladder — corpus + site)

**Type:** Content. Corpus-first; **no authority ceiling, register row, or method value changed**
(`generate_ai_method_register.py` re-run, zero diff). Slice 2 of the digital-twin deepening arc.

Closed the Phase 49a research backlog item "define digital-twin maturity levels" (`research-map.md`
line 144, now ticked) by adding **§4 Twin maturity — a synchronization ladder, not an authority ladder**
to `digital_twin.md` (sections 4–6 renumbered to 5–7; no repo file linked the old anchors), with a
distilled section and two new elements on the site page.

- **M0 offline model → M1 connected shadow → M2 synchronized twin → M3 predictive twin → M4 bounded
  closed-loop twin**, each graded by synchronization character, question answered, and the §3
  data-integrity steps it presupposes.
- **Citation split by axis, per the 49d verdict.** The functional progression is cited to NIST's
  published five-category ladder (descriptive → diagnostic → predictive → prescriptive → intelligent);
  the **synchronization grading is labelled this project's engineering judgement**, because no standard
  read defines a graded sync scale. M0 is stated to sit *below* NIST's scale, which presumes a live twin.
- **M4 is described, not authorized** — two independent reasons now on the page: no register row grants a
  twin-composed learned output above advisory, and NIST's own top rung is *"envisaged to"* control, in the
  future tense.
- **Two design rules added:** declare target maturity per use case at concept design (ISO 23247's
  fit-for-purpose principle in practice); a maturity claim never appears in an authority argument.
- Site page gains the maturity table plus a second Mermaid diagram (`flowchart LR`, M0→M4 with M4 dashed
  as described-not-authorized and a register-authority annotation). Frontmatter `edition`/`coverage`
  refreshed; page stays **Review pending**.
- `_index.yaml` description + changelog updated; RAG mirror regenerated (320 files, body byte-identical).

Full release gate green.

## 2026-07-19 — Phase 49d (Digital-twin maturity vocabulary + ISO 23247 currency)

**Type:** Work-tier research only — **no site, corpus, or register change.** First slice of the
four-slice digital-twin deepening arc.
**Outputs (under `control-standards/work/research/ai-ml-control-systems/`):** new `49d-findings.md`;
`source-register.md` Phase 49d additions section; two verdicts appended to `adversarial-verdicts.md`.

Ran the evidence closure the maturity-ladder content slice depends on. **The headline result inverted
the expectation:** the ladder is *better* grounded than assumed.

- **A published five-rung twin ladder exists and was already in our own source list, unextracted.** The
  NIST publication (Shao, Kibira & Frechette, *Digital Twins for Advanced Manufacturing: The Standardized
  Approach*) defines **Descriptive → Diagnostic → Predictive → Prescriptive → Intelligent** in Figure 1,
  captioned "Increasing complexity, more decision support, and greater value". VERIFIED_AT_PUBLISHER.
- **NIST's own top rung is aspirational** — "Intelligent Digital Twins are **envisaged to** control their
  physical counterparts" (future tense in the source). This independently corroborates the planned
  *described-not-authorized* framing of the top maturity level: two reasons now, one external, one internal.
- **ISO 23247-5:2026 confirmed current** — Ed. 1, June 2026, 26 pp, ISO/TC 184/SC 4, Part 5 *Digital thread
  for digital twin*. **Existence/title/edition/date only** — the catalogue page 403'd (bot-gated, the Phase
  48 Siemens pattern) and the body is paywalled and unread. The corpus note's "ISO body not read" caveat
  stands and must not be softened. Also sighted, not read: ISO/FDIS 23247-6 (twin composition) and
  **ISO/TR 23247-100:2025** (semiconductor ingot-growth use case — adjacent to `semiconductor_facility/`,
  flagged as a future cross-link).
- **Maturity-model sweep:** the Gemini/CDBB line (Chen et al., *Sustainability* 13(15):8224, DOI
  10.3390/su13158224, VERIFIED_VIA_DOI_REGISTRY) is an assessment **rubric** (3 dimensions / 9
  sub-dimensions / 27 rubrics) scoped to built-environment asset management — adjacent prior art, does
  **not** ground a control-system ladder. A standards-defined *synchronization* ladder: **NOT_FOUND**.
- **Verdict for the content slice (§5 of the findings): split the citation by axis.** Cite NIST for the
  functional progression; label the synchronization grading (no link / one-way / reconciled / validated
  horizon / gated action path) explicitly as project working vocabulary; state that M0 sits *below*
  NIST's scale, which presumes a live twin.
- **Adversarial pass:** `twin-maturity-ladder-vocabulary` partially refuted (grounding better than
  claimed — publish with the axis split). `twin-maturity-implies-authority` **flatly refuted** — maturity
  never supports authority; `digital_twin_state_sync` stays at max_authority 2, PINN rows stay at 1,
  level 5 remains unavailable to any learned method at any maturity.

**No ceiling moved.** Full release gate green.

## 2026-07-19 — Phase 50.14: `cst modbus-decode` (offline Modbus TCP capture analysis)

**Type:** Toolkit feature. New `cst` subcommand + module; no corpus, register, or AI-authority
position changed.

Added offline Modbus TCP capture decoding to the diagnostics module, closing the gap between the
design-time register map (`cst modbus-map`) and what a link actually carries in the field.

- **`src/cst/diagnostics/modbus_decode.py`** (new) — classic pcap and pcapng readers (stdlib only:
  Ethernet, VLAN, Linux SLL, raw-IP, and loopback link types), TCP stream reassembly, Modbus TCP
  ADU framing and PDU decode, request/response pairing, and a field-diagnostic summary
  (exception responses, unanswered requests, response latency, polled register spans).
- **`src/cst/cli.py`** — new `modbus-decode` subcommand with `--port`, `--addresses`,
  `--exceptions`, `--unanswered`. Also widened `main`'s handler to catch `FileNotFoundError`
  alongside `ValueError`: a missing input file (or an unsupplied licensed table, since
  `TableDataMissingError` subclasses it) now exits 2 with a clean message instead of a traceback.
  This fixed a pre-existing gap that also affected `io-check`, `saleae`, and the table-backed
  calculators.
- **`docs/tools/engineering-toolkit/index.md`** — command-table row, worked example, and a limits
  note that capture itself must be passive (TAP or mirror port) on a live OT segment.
- **`tests/cst/test_modbus_decode.py`** (new, 19 tests) + 5 CLI tests in `tests/cst/test_cli.py`.
  Captures are synthesised in-test rather than committed as binary fixtures, so every byte under
  test is visible and reviewable. Suite 202 → 226.

**Provenance.** The TCP reassembly approach (32-bit sequence-space arithmetic, retransmission and
gap handling, framing-violation resync, LRU stream eviction) is adapted from the owner's own
`~/Dev/network_monitoring` project, which is intentionally private and has no remote. Only
original code was carried across — the knowledge-base content there is derived from private
source files and was deliberately **not** ported. The live-capture daemon was also left behind:
`cst` stays a read-only offline analysis toolkit with no privileged network access.

**Design notes.** Protocol constants (MBAP framing, function codes, exception codes) follow the
openly published Modbus Application Protocol Specification V1.1b3 — no licensed table values are
embedded. A wrong `--port` labels every frame a response, which would otherwise produce a
silently meaningless summary; the CLI warns rather than fails, because a direction-filtered
capture legitimately has no requests.

Full release gate green at delivery (226 tests + 10 doctests, clean Jekyll build, zero broken
internal links, AI-boundary and corpus-quality checks green).

## 2026-07-19 — Repository scope-and-intent statement (documentation only)

**Type:** Documentation / governance. **No technical, corpus, register, or site content changed.**

Added an explicit, prominent statement of what this repository is and is not, because the
process-engineering vocabulary here ("chemical", "biological", "hazardous", "adversarial pass")
reads as sensitive when encountered without context — by human reviewers and automated review
alike. The statement is descriptive of what the repository already does; it introduces no new
position.

- **`README.md`** — new **Scope and Intent** section directly after the intro: defensive
  industrial-automation engineering; a term-by-term table mapping each ambiguous word to its
  actual process-engineering meaning; the governing hard/soft-layer constraint (established
  scientific law is the ceiling and holds the veto, ML capped at advisory with zero safety-function
  authority); and the sourcing/verification posture.
- **`governance/AI_WORKFLOW.md`** — new **§0 Scope of This Repository**, placed ahead of the read
  order so any agent meets it first. Same vocabulary clarification, plus an explicit instruction
  that work here is safety-compliance documentation, and that anything which would *increase*
  rather than constrain hazard capability is out of scope for this repository.
- **`control-standards/work/research/ai-ml-control-systems/README.md`** — blockquoted scope note
  at the top, since this is where the chem/bio shorthand actually lives. Records that Phase 49c
  attempted to justify greater ML authority in chemical and bioprocess plants and **refuted every
  attempt** — the deliverable was a tighter limit, not a broader capability.

Full release gate green at delivery (202 tests + 10 doctests, clean Jekyll build, zero broken
internal links across 378 files, AI-boundary and corpus-quality checks clean). The 166-page
legacy `review:`-block warning is the pre-existing baseline, unchanged.

## 2026-07-17 — Phase 49c (Chemical & biological evidence closure + adversarial pass)

**Type:** Work-tier research only — **no site, corpus, or register change.** Owner-authorised
2026-07-17 (authorisation covered the work, not the ceiling).
**Outputs (under `control-standards/work/research/ai-ml-control-systems/`):** new `49c-findings.md`;
`source-register.md` extended with a Phase 49c additions section; pointer notes added to
`authority-ceilings.md` and `adversarial-verdicts.md` so the "unattacked / no coverage" caveats no
longer read as current.

Closed the two gaps 49a left open for the chemical/biological families, via three parallel
publisher-verification research workstreams plus a single-lens adversarial synthesis.

- **Gap 1 closed — equilibrium/thermodynamics had no verified source.** Now anchored on the **NIST
  Chemistry WebBook (VERIFIED_AT_PUBLISHER)** for the hard leg (equilibrium by Gibbs-energy minimisation),
  with IUPAC + the Wiley activity-model chapter DOI-registry-verified for the soft leg (NRTL/UNIQUAC/
  UNIFAC/EoS are fitted closures). **Transport phenomena (Bird, Stewart & Lightfoot) upgraded
  UNVERIFIABLE → VERIFIED_AT_PUBLISHER.** ML in thermo (UNIFAC 2.0, GH-GNN) confirmed as property-
  prediction closures with no control authority.
- **Gap 2 closed — no adversarial coverage.** First chem/bio adversarial pass performed (refute-by-
  default). Every attempt to raise the ceiling was refuted; safety-function participation pushed to 0.
  **Adjudicated ceilings:** learned/hybrid chem/bio methods ≤ Level 2 (advisory/soft-sensor), default 1
  where transferability/fault-tolerance unproven, **0** for any safety function; deterministic governing
  models are the hard-constraint layer, but a fitted closure inside them is not; supervisory RL (the
  Yokogawa pattern) bounded behind an independent non-learned veto.
- **Regulatory frame verified:** IEC 61511 (VERIFIED_AT_PUBLISHER) has no AI/ML provisions; EMA reflection
  paper and FDA PAT verified at publisher/government record; the Yokogawa+JSR 840 h RL run re-verified
  (protection untouched — confirms the ceiling). Adversarial sweep for a certified ML controller or a
  permitting standard: **NOT_FOUND**.
- **Recommendation (OWNER DECISION, not applied):** the chem/bio rows may now move **off `Planned`** to
  the conservative evidenced ceilings above, and the 50.13 chem/bio `safety_relevance` values may drop
  their *provisional* tag — every one staying `safety-adjacent`/`non-safety`, never `safety-related`.
  This is a safety-significant register change held for owner approval; if approved it is a bounded slice.
- **Do-not-publish (carried):** IEC 61508-3 "AI not recommended ≥ SIL 2" table ratings (SECONDARY_ONLY);
  IWA STR series numbers; the Raman/CHO paper must be pinned before use. Full detail: `49c-findings.md` §7.

## 2026-07-17 — Phase 50.6 (CLI + citation test coverage)

**Type:** Test coverage for the toolkit's two previously-untested modules. No behaviour change.
**Branch:** `feat/phase50-6-cli-tests`.

Closes the Phase 50 "thin CLI + tests" gap. On inspection the CLI is **already a thin dispatch
layer** — `main(argv)` parses, calls `args.func(args)`, and catches `ValueError` → prints `error: …`
to stderr and returns exit code 2; each `_cmd_*` handler is a few lines calling a calc function and
printing. No adapter refactor was warranted, so this slice adds the missing tests rather than
restructuring working code.

- **New `tests/cst/test_cli.py` (14 tests).** Exercises the dispatch/exit-code contract, not the
  numerics (calculators are covered by their own tests + doctests):
  - `cst.common.cite`: `Citation.__str__` with and without a note; `CalcResult.report()` renders
    value/detail/warnings/assumptions/citations; the minimal single-line case.
  - `cst.cli` happy paths via `main([...])` for five **table-free** commands (encoder, enclosure, fan,
    fault-current, sccr) — chosen so the suite never depends on the gitignored licensed standards tables.
  - Error handling: a `ValueError` (non-positive heat load; malformed `--component`) returns **2** and
    writes `error:` to stderr; an unknown subcommand, a missing required subcommand, and a missing
    required argument each raise `SystemExit` (argparse).
- **Suite 188 → 202.** `environment.md` and `how_to.md` test counts updated to 202. Full release gate
  green (202 tests, 10 doctests, clean build, 0 broken links, corpus checks clean).

Remaining Phase 50: project-state history split (50.8). Every `cst` module now has test coverage.

## 2026-07-17 — Phase 50.13a (Selector-classification vocabulary + invariants)

**Type:** Canonical-schema extension + generator validation + tests (no site behaviour change yet).
**Branch:** `feat/phase50-13a-classification-vocabulary`.

Owner signed off the 50.13 vocabulary draft (`planning/2026-07-17-phase50-13-classification-vocabulary.md`);
this slice implements the schema half. The interactive selector UI (50.13b) is deferred alongside the
Phase 52.2 mobile/accessibility work (needs keyboard/screen-reader device verification).

- **Four validated classification fields added to all 42 `methods.yml` rows** (proposed assignments
  adopted as-is, including the five judgement-call rows): `method_class` (deterministic/learned/hybrid),
  `decision_type` (7 values), `data_availability` (5-level measured-data burden), `safety_relevance`
  (safety-related/safety-adjacent/non-safety). Backfill applied line-by-line so the compact
  one-row-per-method format is preserved (42 insertions / 42 deletions, no reformat).
- **Generator now enforces membership + three cross-field invariants** (`generate_ai_method_register.py`):
  (1) `safety-related` ⟹ `method_class == deterministic` — the load-bearing guardrail encoding the Phase
  49a finding; (2) `safety-related` ⟹ `max_authority != Planned`; (3) `pretrained-plus-context` ⟹
  `learned` and not `safety-related`. Exactly two rows are `safety-related` — `rule_engine` and
  `robust_mpc_safety_filter`, both deterministic with a real authority value.
- **Tests: 5 → 13** in `test_generate_ai_method_register.py` (fixture extended with the four fields;
  membership rejections; one test per invariant incl. a learned-marked-safety-related failing fixture;
  and a regression test asserting the real 42-row register satisfies every rule). Suite **180 → 188**.
- **Docs:** the vocabulary + invariants documented in the corpus register README; the plan marked
  APPROVED / 50.13a implemented. Register data regenerated to `docs/_data/ai_methods/`.
- **Verification:** full release gate green (188 tests, 10 doctests, clean build, 0 broken links,
  corpus checks clean). Fields are present in the data but not yet rendered — the selector UI is 50.13b.

## 2026-07-17 — Owner decisions + analytics scoping

**Type:** Governance decisions recorded; one small site change (analytics scope). No technical/standards
content changed.

Owner answered the open-decision list. Rulings and the actions taken:

- **Next Phase 52 slice → 52.3 (task-first IA).** 52.2 (mobile) deferred: its acceptance needs
  real-device/browser verification the agent cannot perform. **52.4a IEC 62061 parked** — the Ed. 2.2
  (2021+AMD1:2024+AMD2:2026) rebuild needs the licensed consolidated source, which is unavailable.
- **50.13 classification vocabulary SIGNED OFF.** Implement the four canonical fields (`method_class`,
  `decision_type`, `data_availability`, `safety_relevance`) + the four generator-enforced invariants
  (chief: safety-related ⟹ deterministic), then the interactive method selector. Queued as a bounded
  slice (fully build-verifiable, no device dependency).
- **Phase 49c AUTHORISED.** The chem/bio evidence-closure + adversarial sprint may proceed. Authorisation
  is for the *work only* — no authority ceiling is granted until the evidence supports it; rows stay
  Planned and Level 5 / safety-function status stays unavailable to learned methods. Sprint queued.
- **Analytics scoped to access logging only** (visitor / system / location; no behavioural or ad
  tracking). Implemented in `docs/_layouts/default.html`: `gtag('config', …)` now passes
  `allow_google_signals:false` and `allow_ad_personalization_signals:false`. **Two caveats surfaced to
  the owner:** (a) an anonymous static site cannot identify *which user* — GA reports pseudonymous
  visitors, approximate geo (IP), and device/browser/OS, not named individuals; (b) data-retention and
  any Signals/demographics property settings must be minimised in the GA4 console (not controllable from
  page code). A short public privacy note remains recommended but was not part of this ruling.
- **Three UNVERIFIABLE purchased-text items → discarded as tracking items** (E-stop restricted to Stop
  Category 0/1; IEC 62061 "conventionally SIL 1–3"; ISO 13849-1 PL band numbers incl. PL e ≥ 10⁻⁸).
  **Interpreted conservatively for safety content:** the claims and their on-page **verify badges stay**
  (removing a hedge on a paywalled safety number would over-assert and violate the governance honesty
  posture); only the open author-action to chase publisher verification is closed. No page content was
  edited. *If the owner instead meant delete the claims themselves, flag it — that was not done.*
- **Withheld legacy-panel photographs stay out** — resolved; the repo publishes original diagrams only.
- **Eight Review-pending AI-integration pages → remain pending** (owner will review later).

### Recommendation for the Phase 45 / Phase 48 page re-reviews (owner requested)

Rather than a full manual re-read, review in risk order and spot-check only the load-bearing claims:

1. **Phase 45 standards pages (highest risk first):** IEC 60204-1, IEC 62061, ISO 13849-1, NEC, NFPA 79,
   UL 508A. For each, verify only (a) the edition/date line, (b) any number that carries a verify badge,
   and (c) the specific corrections logged in `planning/2026-07-11-standards-accuracy-review.md`. Those
   corrections were publisher-verified where free text allowed; the residual risk is confined to the
   badged paywalled numbers, which are now closed as "conservative + badged."
2. **IEC 62061 is the exception** — it is at *Needs revalidation* and should be **rebuilt from the
   consolidated Ed. 2.2**, not spot-checked. It stays parked until the licensed source is available; do
   not mark it Reviewed on a spot-check.
3. **Two Phase 48 pages** (Vendor Documentation Index, PLC/IPC Hardware Families): these are
   data-driven and every lifecycle/market claim already carries an `as_of: July 2026` + verify-current
   stamp. Re-review reduces to confirming the `as_of` stamps read correctly and re-running vendor-link
   liveness (28/129 failures were all bot-gated Siemens portals, not dead links) — a mechanical check,
   not a claim audit.
4. **Do not bulk-mark Reviewed.** Approve page-by-page; an agent cannot set Reviewed, so these stay
   owner-only regardless.

## 2026-07-17 — Phase 52.1 (State accuracy and navigation hygiene)

**Type:** Project-state correction + site navigation hygiene (no technical content change).
**Branch:** `feat/phase52-1-state-nav-hygiene`.

First implementation slice of Phase 52. Validated all four `project_state/` files against reality and
reconciled the six duplicate navigation URLs flagged in the recommendation.

- **State-file drift fixed.** `how_to.md` claimed "155 tests" — corrected to **180** (+ noted the 10
  doctests); `how_to.md` and `environment.md` "Last Updated" refreshed to 2026-07-17. Verified accurate
  and left as-is: `environment.md` runtime baseline (`.python-version` = 3.13, `requires-python >=3.12`,
  stdlib-only core install, 180 tests) and the `project_state.md` header the owner refreshed in `10177a2`
  (current delivery / phase / next action / authorization gate all in the first 40 lines). No tracking
  statement now contradicts `git log` (the earlier stale "Phase 50.5 awaiting owner merge" was already
  corrected in `10177a2`; 50.5 is on `master` at `ed85dac`).
- **Six duplicate navigation URLs reconciled.** Each was a group-header parent
  (`Fundamentals`, `Ethernet Protocols`, `Serial & Device Networks`, `Utility & Substation`,
  `Diagnostics`, `Guides`) reusing its first child's URL. Removed the `url:` from those six headers so
  they are now **non-link category labels**; every underlying page stays reachable via its own child
  entry (e.g. "Ethernet Fundamentals", "DNP3", "Commissioning Templates"). Canonical data now drives the
  presentation rather than a header standing in for a page.
- **Template + style.** `docs/_includes/sidebar-global.html` renders a child with no `url` as
  `<span class="sub sub--group">` instead of an `<a href="">`, and guards the active-state computation
  against a nil url (Liquid's `contains nil` would otherwise match every page). A minimal
  `.sub--group` rule in `main.css` styles the header as a non-interactive group label.
- **Verification.** Duplicate-URL scan of `navigation.yml`: **0**. Built site: the six headers render as
  `<span>` labels with **0** empty `href` attributes; all pages still build. Full release gate green
  (180 tests, 10 doctests, clean build, 0 broken links, corpus checks clean). The 166-legacy-page
  `review:` warning is unchanged (that is Phase 52.4b work).

## 2026-07-17 — Phase 52 UI/UX and content-upgrade recommendation

**Type:** Planning + project-state correction.

**Branch:** `docs/phase52-ui-ux-content-recommendations`.

Recorded `planning/2026-07-17-phase52-ui-ux-content-upgrade-recommendations.md`, converting the
current-project audit into five bounded follow-up slices:

1. state accuracy and reconciliation of six repeated navigation URLs;
2. mobile search, responsive page context, accessible drawers, and wide-table handling;
3. task-first homepage routes and local-section navigation over the governed taxonomy;
4. IEC 62061 Ed. 2.2 rebuild, risk-ordered `review:` rollout, honest aggregate status, content
   layering, and field-guide-to-`cst` integration; and
5. reusable UI components plus an accessibility release gate.

The plan records the measured baseline: 180 tests and 10 doctests green, clean Jekyll build, zero
broken links across 378 rendered files, 248 reader-facing index pages, 166 legacy pages without a
`review:` block, six repeated navigation URLs, and a growing 2,722-line CSS / 579-line JavaScript
surface. It recommends trust and discovery work before another broad content expansion.

Corrected the first-page project status to reflect reality: Phase 51 is the current completed
delivery; Phase 52 is proposed and not implemented; Phase 50.5 is already merged in `ed85dac`; and
the remaining Phase 50 follow-ups are carried forward explicitly. Phase 49c remains unauthorised,
and this planning change raises no AI/ML authority ceiling.

Validation for this documentation-only change: full release check passed (180 tests, 10 doctests,
clean Jekyll build, zero broken links, AI-boundary and corpus-quality checks green).

## 2026-07-17 — AI-integration 7-page build, Slice G (Worked Architectures) — build COMPLETE

**Type:** Site content (Design section) + corpus note. **Final page of the seven.**
**Branch:** `feat/phase51-ai-integration-worked-architectures`.

Added the closing page — four end-to-end worked architectures, each walked through the authority
ladder. **Introduces no new technical claims**; it composes the positions verified across Slices B–F.

- **Corpus note:** `control-standards/rag/design_framework/ai_integration/worked_architectures.md`
  (RAG_APPROVED/DRAFT) — vision inspection cell (2-D CNN, advisory, PLC owns the reject action);
  predictive-maintenance pipeline (1-D CNN, advisory, edge inference, the leakage + fleet caveats);
  PINN soft sensor (level 1–2, never closes the loop, FP64 + silent-failure caveats, cross-checked
  against measurements); read-only LLM copilot (advisory; offline for drafted code; GenAI Profile;
  no write). Each answered in four beats — the job, the rung (and why not higher), what stays
  independent, the seam and the gated contract.
- **Site page:** `/design/ai-integration/worked-architectures/` distils the note (a summary table, the
  four walkthroughs, an original shared-envelope diagram). Gate page gained a "worked architectures"
  pointer; nav child added; cross-linked to every other page in the section. Mirror regenerated
  (320 files, byte-identical); no register-data change this slice. Full release gate green (180 tests,
  10 doctests, clean build, 0 broken links, 380 AI-boundary files, corpus-quality clean).

**The seven-page AI-integration expansion is COMPLETE and deployed** (all pages Review pending):
gate `/design/ai-integration/` · method-register · safety-boundaries · interfaces · model-families ·
digital-twin · validation-lifecycle · worked-architectures, plus the downloadable model-evidence
ledger. All corpus-first, all gates green, all deploy-verified. **Author review of the eight
Review-pending pages is the outstanding follow-up.** Remaining Phase 50 backlog (Workstream D site
editorial: `review:` rollout for 166 legacy pages; IEC 62061 Ed 2.2 rebuild) and Phase 49c
(chem/bio authority, unauthorised) are unaffected by this build.

## 2026-07-17 — AI-integration 7-page build, Slice F (Validation, Drift & Model Lifecycle)

**Type:** Site content (Design section) + corpus note + downloadable template + register annotation.
**Branch:** `feat/phase51-ai-integration-validation-lifecycle`.

Added the validation-and-lifecycle explainer, corpus-first — the "authority is perishable" page — and
closed the NIST AI RMF GenAI-Profile item deferred from Phase 50.12.

- **Source verified & added:** **NIST AI RMF Generative AI Profile (NIST AI 600-1)** confirmed at the
  publisher — designation, publication date **2024-07-26**, and companion-not-replacement status
  (*"cross-sectoral profile of and companion resource for the AI RMF 1.0"*). Added as
  `nist_genai_profile` and framed as the LLM-relevant companion; the base AI RMF 1.0 relabelled with its
  `NIST AI 100-1` designation. NIST AI RMF is framed throughout as **process vocabulary, not safety
  permission** (consistent with the Phase 49a WS1 finding that governance frameworks confer no
  functional-safety authority).
- **Corpus note:** `control-standards/rag/design_framework/ai_integration/validation_lifecycle.md`
  (RAG_APPROVED/DRAFT) — why the lifecycle (not commissioning) is the point; the Govern/Map/Measure/
  Manage mapping of the lifecycle demands (owner + MoC + audit; data lineage + envelope; leakage-free
  component-wise test sets + uncertainty + deployment-condition validation; drift/OOD + hazard-derived
  failure response + rollback + human review); the model-evidence ledger.
- **Downloadable template:** `docs/assets/templates/ai_model_evidence_ledger.md` — an original,
  per-component fill-in ledger (NIST AI RMF Govern/Map/Measure/Manage-aligned; grants no authority),
  promoted from the `scientific-domain-integration.md` research note. Linked from a new "AI & Model
  Lifecycle" section on `/tools/templates/`.
- **Register annotation:** `llm_engineering_copilot` sources gained `nist_genai_profile`. Data
  regenerated to `docs/_data/ai_methods/`.
- **Site page:** `/design/ai-integration/validation-lifecycle/` distils the note (the four-function
  table, an original failure-response/`on_fail` diagram, the ledger with a download link). Gate page
  gained a "validation, drift, and the model lifecycle" pointer; nav child added; cross-linked. Mirror
  regenerated (319 files, byte-identical). Full release gate green (180 tests, 10 doctests, clean build,
  0 broken links, 379 AI-boundary files, corpus-quality clean).

**Only Slice G (Worked architectures) remains** in the 7-page build; it depends on B–F, now all shipped.

## 2026-07-17 — AI-integration 7-page build, Slice E (Digital Twin)

**Type:** Site content (Design section) + corpus note + register annotation.
**Branch:** `feat/phase51-ai-integration-digital-twin`.

Added the digital-twin explainer, corpus-first — the "integration spine" page — after re-verifying the
Phase 49a research note `digital-twin-integration.md` before promotion.

- **Definition grounded in a published framework.** The note's unsourced working definition was replaced
  with **ISO 23247 (Digital Twin Framework for Manufacturing)**: a *"fit for purpose digital
  representation of an observable manufacturing element with synchronization between the element and its
  digital representation."* Four-part series (2021: overview, reference architecture, digital
  representation, information exchange) + Part 5:2026 (digital thread); four-domain reference model
  (observable manufacturing / device communication / digital twin / user, plus a cross-system entity).
  **Verified via a NIST government publication that cites the standard** ("Digital Twins for Advanced
  Manufacturing: The Standardized Approach"); the ISO body itself was **not read** (ISO catalogue blocks
  automated retrieval), and the note/page say so.
- **The load-bearing distinction is now anchored, not asserted:** a live data **mirror** (one-way
  synchronization — "receives data but gives no control feedback," per the jet-engine example) is not a
  **behavioural** twin, and physical-to-digital (data integrity) and digital-to-physical (gated action)
  are separate problems. The digital-to-physical authority ladder is the register's; the twin grants no
  authority and no safety function routes through it.
- **Corpus note:** `control-standards/rag/design_framework/ai_integration/digital_twin.md`
  (RAG_APPROVED/DRAFT) — twin vs mirror; ISO 23247 reference model with the device-communication seam as
  the authority-critical junction; the two synchronization directions; the twin↔control data contract;
  the CNN/PINN/LLM families inside the twin at their register ceilings.
- **Register annotation:** `digital_twin_state_sync` authority_basis notes "ISO 23247 frames the twin
  but confers no safety authority"; `iso_23247` and `nist_dt_manufacturing` added to `sources.yml` and
  the row's sources. Data regenerated to `docs/_data/ai_methods/`.
- **Site page:** `/design/ai-integration/digital-twin/` distils the note (twin-vs-mirror, an original
  four-domain reference-model diagram, both direction workflows, the digital-to-physical ladder, the
  data contract). Gate page gained a "digital twin as integration spine" pointer; nav child added;
  cross-linked. Mirror regenerated (318 files, byte-identical). Full release gate green (180 tests,
  10 doctests, clean build, 0 broken links, 378 AI-boundary files, corpus-quality clean).

Slice F next: Validation, drift & model lifecycle (+ NIST AI RMF GenAI Profile, deferred from 50.12; +
model-evidence-ledger template under /tools/templates/).

## 2026-07-17 — AI-integration 7-page build, Slice D (Model Families & Fit)

**Type:** Site content (Design section) + corpus note + register correction.
**Branch:** `feat/phase51-ai-integration-model-families`.

Added the model-families explainer, corpus-first, covering the three learned families the register
leans on — CNN/temporal perception, PINN, and LLM — each shown as **capability *and* poor fit**.

- **Source gaps closed at the publisher** (the build plan named these as blockers for Slice D):
  - **FP64/PINN:** verified as Xu et al., "FP64 is All You Need," **NeurIPS 2025** (arXiv:2505.10949) —
    several canonical PINN failures are FP32-precision-induced stalls rescued by FP64. Control-systems
    implication carried onto the page: embedded FP32/fixed-point hardware can break a
    workstation-validated PINN, so validate at the deployment precision.
  - **LLM4PLC** (arXiv:2401.05443) — confirmed **peer-reviewed, ICSE 2024 SEIP track** (not just a
    preprint). **Xia et al.** (arXiv:2409.18009) — confirmed **peer-reviewed, IEEE ETFA 2025**
    (DOI 10.1109/ETFA65518.2025.11205539). Both remain proof-of-concept demonstrations, not production
    evidence, and are labelled as such.
- **Corpus note:** `control-standards/rag/design_framework/ai_integration/model_families.md`
  (RAG_APPROVED/DRAFT) — the "name the deterministic alternative first" rule; CNN advisory ceiling with
  the train/test-leakage collapse (CWRU 100.0→66.4, Paderborn 99.9→53.2) and the vibration-beats-motor-
  current sensor result; PINN loses-to-FEM / silent-failure / steady-state-reversion / no-error-bound
  case plus the FP64 caveat; LLM draft-then-verify (47%→72%) and why raw output/agentic control stay out
  of the loop; dataset-licence note (Paderborn CC BY-NC; CWRU undefined — cite, never redistribute).
- **Register correction:** `methods.yml` `llm_plc_code_draft` `evidence_strength` `preprint → peer-reviewed`
  and its `authority_basis` reworded (LLM4PLC now peer-reviewed ICSE 2024 SEIP). `sources.yml` gained
  Grossmann (PINN-vs-FEM), Xu et al. (FP64), the bearing-leakage and Paderborn sources, and the
  Xia et al. ETFA entry; LLM4PLC relabelled peer-reviewed. Register data regenerated to `docs/_data/ai_methods/`.
- **Site page:** `/design/ai-integration/model-families/` distils the note (fit/poor-fit summary table,
  per-family sections, an original ladder diagram, FP64 and licence callouts). Gate page gained a
  "Model families and fit" pointer section; nav child added; cross-linked. Mirror regenerated
  (317 files, byte-identical). Full release gate green (180 tests, 10 doctests, clean build, 0 broken
  links, 377 AI-boundary files, corpus-quality clean).

Slice E next: Digital twin (re-verify the research note `digital-twin-integration.md` first).

## 2026-07-17 — AI-integration 7-page build, Slice C (Interfaces & Handshakes)

**Type:** Site content (Design section) + corpus note.
**Branch:** `feat/phase51-ai-integration-interfaces`.

Moved the interface material off the crowded gate page into its own page and expanded it, corpus-first.

- **Corpus note:** `control-standards/rag/design_framework/ai_integration/interfaces_edge.md`
  (RAG_APPROVED/DRAFT) — the rule (infer at the edge, publish the verdict); the **four constraints**
  that put inference at the edge (server sampling floor; decoupled-source aliasing; historian
  compression; segmentation) with the "kHz is not a protocol limit" correction; what OPC UA and
  Sparkplug do/don't give (no AI companion spec, coarse StatusCode → Structured DataTypes, `Uncertain_*`,
  Part 9 Alarms; Sparkplug per-metric properties + birth/death liveness); write-authority separation
  via the OPC UA Observer role; the result contract; NIST SP 800-82r3 OT placement.
- **Verification correction:** the Phase 49a note claimed Sparkplug B has a "first-class STALE quality."
  That could **not** be confirmed against the Sparkplug specification during Slice C, so it was replaced
  with the verified birth/death-certificate liveness mechanism — the page does not ship the unverified claim.
- **Site page:** `/design/ai-integration/interfaces/` distils the note (two acquisition-path diagrams
  moved from the gate, an OPC-UA-vs-Sparkplug capability table, the result-contract JSON). The gate
  page's long "Interface rule" section is replaced by a two-sentence pointer. `_index.yaml` updated;
  mirror regenerated (316 files); nav child added; cross-linked. Full release gate green.

Slice D next: Model families & fit (close FP64/PINN + arXiv-preprint gaps first).

## 2026-07-17 — AI-integration 7-page build, Slice B (Safety & Security Boundaries)

**Type:** Site content (Design section) + corpus note + source-gap closure.
**Branch:** `feat/phase51-ai-integration-safety-boundaries`.

The load-bearing page of the section: **why a learned component cannot hold a machine's safety
function today.** Corpus-first per the plan.

- **Source gap closed (verified at the publisher):** IEC 62061 — flagged "never checked for
  ML/self-evolving content" since Phase 49a — confirmed at the IEC webstore (publication 59927) as
  **Ed. 2.0, 2021-03-22**, scope within the IEC 61508 framework with **no mention of AI/ML/self-evolving
  components**. ISO/IEC TS 22440 status sharpened: **Committee Draft (Feb 2026), three parts** (ISO
  catalogue 89535/89536/89537). Both recorded in the work-tier `source-register.md`. The page can now
  *source* the "no certification route" position rather than assert it.
- **Corpus note:** `control-standards/rag/design_framework/ai_integration/safety_boundary.md`
  (headered RAG_APPROVED/DRAFT) — the deterministic FS standards (ISO 13849-1, IEC 62061, IEC 61508)
  with no learned-component route; TR 5469 as guidance-not-certifiable; TS 22440 unpublished; EU
  Machinery Reg 2023/1230 Annex I items 5–6 + Annex III EHSR 1.2.1 (statutory ≤4 ceiling) and AI Act
  Art 6(1); the verified-non-learned-layer architecture; NIST SP 800-82r3 OT placement. `_index.yaml`
  updated; mirror regenerated (315 files).
- **Site page:** `/design/ai-integration/safety-boundaries/` distils the note — document-status table,
  the EU-law ceiling, an original standards-track-vs-law-track Mermaid diagram, the independence rule,
  and the cybersecurity boundary. Review pending; cross-linked from the gate's safety-boundary callout
  and back to the gate/register; nav child added. Full release gate green (build, 0 broken links, 180
  tests, corpus-quality + `_index.yaml` validators clean).

Slice C next: Interfaces & handshakes (corpus-first; content largely already on the gate page).

## 2026-07-17 — AI-integration 7-page build, Slice A (skeleton split)

**Type:** Site information architecture (Design section).
**Branch:** `feat/phase51-ai-integration-expansion`.

Owner authorised expanding the single `/design/ai-integration/` page into the authority-first
7-page structure the Phase 49 presentation plan designed (the one page crammed the gate, authority
ladder, envelope architecture, the full 42-method register, the interface rule, and domain limits).
Build plan recorded at `planning/2026-07-17-ai-integration-7page-build-plan.md` — sequences the seven
pages into corpus-first slices with per-page evidence status and the source gaps to close first
(IEC 62061 ML check, FP64/PINN, arXiv preprint status).

Slice A is presentation-only (no new technical claims): the 42-method register moved to its own page
`/design/ai-integration/method-register/` (dir + `index.md`, matching the site's child-page
convention so the pretty URL resolves — a first `.md` build produced `method-register.html`, which
GitHub Pages would not serve at the trailing-slash URL). The index is now the **authority gate** —
plain-terms intro, the pre-flight question, authority ladder, envelope architecture, interface rule,
domain limits — and links out to the register. Both pages restate the safety-independence boundary;
both stay Review pending. Nav gains a Method Register child. Full release gate green (build, 0 broken
links across 372 files, 180 tests). Slice B next: the corpus-first Safety & Security Boundaries page.

## 2026-07-17 — Phase 50.5 — licensed-table module + packaging cleanup

**Type:** Toolkit correctness + packaging (Workstream B).
**Branch:** `feat/phase50-licensed-tables` (off `master`).

Closed all three open defects the plan flagged for the licensed-table loader and packaging:

- **Load-time validation (TDD):** `cst.common.tables._parse` now rejects, with an actionable
  message naming the file, a `source` that is not an object or is missing any of
  `standard`/`edition`/`table` (previously passed silently — `source_label` printed `?`), a `data`
  value that is not a list of objects, and — for tables with a mapped committed schema
  (`_SCHEMA_FOR`) — any row missing a schema-`required` field. Row validation reads the required
  keys straight from `schemas/<name>.schema.json`, so it stays in lockstep with the schemas and adds
  no dependency. 5 new loader tests (12 total in `test_tables.py`).
- **Install without a checkout:** the wheel now force-includes `data/standards_tables/{samples,schemas}`
  as `cst/_bundled_tables/`. `load_table` resolves its default directory as **`CST_TABLES_DIR` env
  var → repo `data/` checkout → bundled package data**, and falls back to bundled samples when the
  user dir has none. Verified by building the wheel, installing it in a clean venv, and loading a
  sample + resolving its bundled schema from `/tmp` with no source tree present.
- **Stdlib-only core install:** `pymupdf`/`pypdf` moved out of core `dependencies` into an optional
  `fe-study` extra (they serve only `tools/fe_study/`, whose imports are already lazy +
  ImportError-guarded). `pip show control-system-tools` → `Requires:` empty. `pycomm3` documented as
  the `plc` extra. `uv sync` now yields a dependency-free core + pytest.

README (`data/standards_tables/`) documents the resolution order and validation; `environment.md`
updated for the dependency move, the new `CST_TABLES_DIR` variable, and the corrected test count
(155 → 180). Full suite **180 passed**; full release gate green.

## 2026-07-17 — Phase 50.4 merged to master + 50.13 classification vocabulary drafted

**50.4 shipped:** `feat/phase50-validated-io-seam` fast-forward merged to `master` (full release
gate green: 175 tests, 10 doctests, clean build, 0 broken links, both validators clean) and the
branch deleted. Toolkit-only change — no site content moves — but master pushed so the deploy stays
in lockstep.

**50.13 vocabulary drafted (owner review pending):**
`planning/2026-07-17-phase50-13-classification-vocabulary.md` proposes the four new canonical
classification fields the interactive method selector needs — `method_class` (deterministic/learned/
hybrid), `decision_type` (7 values), `data_availability` (5-level measured-data ladder), and
`safety_relevance` (safety-related / safety-adjacent / non-safety). Includes crisp inclusion tests,
four generator-enforced cross-field invariants (chief among them **safety-related ⟹ deterministic**,
so no learned/hybrid method can ever be classed into the protective layer), a full 42-row proposed
assignment table, and five flagged judgement calls for sign-off. Chemical/biological
`safety_relevance` is marked provisional, mirroring their Planned authority. **No canonical row,
generator, or site data changed** — implementation of 50.13 is gated on approval of this draft.

## 2026-07-17 — Phase 50 corpus/AI stack shipped to master

The stacked branch `feat/phase50-corpus-quality-validator` (50.2 corpus-quality validator → Workstream-E
plan → 50.12 AI correctness/safety → 50.3 `_index.yaml` reconciliation) was fast-forward merged to
`master` and deployed. Full release gate green before merge (165 tests, 10 doctests, clean Jekyll build,
0 broken links across 371 files, AI-boundary + corpus-quality validators clean). GitHub Pages deploy run
`29595960732` green (build + deploy); live `/design/ai-integration/` verified carrying the
`ISO/IEC TR 5469` source-identity fix. Merged branch deleted.

## 2026-07-17 — Phase 50.4 — validated-I/O application seam

**Type:** Toolkit correctness / data-integrity gate (Workstream B).
**Branch:** `feat/phase50-validated-io-seam` (off `master`).

Closed the confirmed defect where every panel/commissioning generator consumed `IOList.points`
directly without ever calling `validate()` — so malformed or colliding source data produced
plausible-looking, wrong deliverables. The worst symptom: `generate_loop_sheets` keyed its result
dict by tag, so **duplicate tags silently overwrote each other and points vanished** from the sheet set.

- **The seam (deep module, small interface):** new `IOListError(ValueError)` carrying the full
  `validate()` problem list, and `IOList.raise_for_problems()` which raises it when the list is
  invalid. Subclassing `ValueError` means the CLI gate comes for free — `cli.main()` already maps
  `ValueError` to exit code 2 with the message on stderr.
- **Every generator now rejects before emitting:** `generate_bom`, `generate_wire_schedule`,
  `generate_loop_sheets`, `legend_plates`, `fat_template`, and `tags_from_io_list` (which protects the
  Modbus map — duplicate tags would otherwise double-map registers) all call `raise_for_problems()`
  at entry. `DesignPackage.add_io_summary` now aborts instead of rendering a "Validation problems:"
  note and proceeding to emit BOM/wire tables from the same bad data (the flagged
  `design_package.py:56-58` behaviour); its dead reporting branch was removed.
- **Division of responsibility preserved:** `cst io-check` stays the advisory reporter (exit 1 with a
  friendly problem list); the generators are the hard gate (exit 2). Valid input is unaffected.
- **Tests (TDD, red→green per slice):** new `tests/cst/test_io_validation_seam.py` — 10 tests over the
  collision fixture (shared tag + shared rack/slot/channel): each generator raises, the error carries
  every problem, clean input still generates, the CLI writes no files and exits 2 on an invalid CSV,
  and the design package aborts. Suite: **175 passed** (was 165). Full release gate green.

## 2026-07-17 — Phase 50.3 — `_index.yaml` reconciliation + index-vs-disk validator

**Type:** Corpus manifest correctness (Workstream A) + validator extension.
**Branch:** `feat/phase50-corpus-quality-validator` (stacked after 50.2 → E-plan → 50.12).

The master index `standards_intelligence/_index.yaml` could not be trusted as a manifest; it now can,
and a validator keeps it that way:

- **Validator (TDD, stdlib-only):** `check_index()` added to `tools/validate_corpus_quality.py`
  (5 new tests; 9 total in the module). Verifies: every indexed `folder:` exists on disk; every
  corpus standards folder under `us/`/`international/` appears in the `standards:` inventory; and
  every `folder:`/`file:`/`guidance_file:` reference resolves **case-sensitively** by comparing
  directory listings — a plain `Path.exists()` passes wrong-case references on macOS and then breaks
  on case-sensitive CI. Wired into the existing script `main()`, so the corpus and full release-check
  profiles enforce it with no profile changes. Run against the real corpus before the data fix, it
  reported exactly the 7 planned defects (5 case-mismatched references + 2 unindexed folders).
- **Inventory completeness:** `international/cybersecurity/iec_62443` (4 files) and
  `international/offshore` (ABS + DNV, 2 files) added to `standards:`.
- **Case fix:** all 6 `reference_models/software_safety_and_intrinsic_safety_standards.md` references
  (5 structured + 1 in the notes block) corrected to the on-disk
  `Software_Safety_and_Intrinsic_Safety_Standards.md`.
- **Guidance documents:** `15-Standard Minimum Compliance Stack.md` and
  `standards_atlas_diagrams_reference.md` added to `guidance_documents`.
- **Edition provenance:** UL 508A `edition: "2022"` → `"3rd Ed. (2018), rev. 2025-06-26"` and
  IEC 60204-1 `edition: "2018"` → `"2016+AMD1:2021"`, matching Phase 45's publisher-verified findings
  (a P0.2 residue — the sub-index header was fixed then, the master index field was not).
- **Tracker honesty:** `crosswalks/overlap_notes/GENERATION_STATUS.md` re-stamped 2026-07-17 as
  **paused/backlog — 3 of 28 overlap notes exist**; its checkboxes were already accurate, but the
  "🔄 In Progress / 19%" framing had been frozen since 2026-01-15. Writing the 25 missing notes
  remains backlog, not Phase 50 scope.

Index changelog entry added inside `_index.yaml` itself (header date bumped to 2026-07-17). RAG site
mirror regenerated (314 files). Gates: full release check green — corpus-quality validator (incl. the
new index check), AI boundaries, Jekyll build, zero broken internal links, full pytest + doctests;
the only warning is the pre-existing 166 legacy-page review-block count (Workstream D scope).

## 2026-07-16 — Phase 50 plan expanded — AI/ML decision-support upgrade

**Type:** Planning and next-phase handoff only. No code, site, corpus, authority, or deployment
change in this entry.
**Plan:** `planning/2026-07-16-phase50-hardening-hygiene-plan.md` Workstream E (50.12–50.15).

Reviewed the deployed `/design/ai-integration/` page and its 42-row canonical register, then added a
bounded Phase 50 workstream that evolves the method catalogue into a gated engineering selection
workspace. The planned slices are: (1) correctness/safety language — correct `IEC TR 5469` to
`ISO/IEC TR 5469`, replace the universal deterministic-fallback example with an
application/hazard-analysis-derived failure policy, clarify deterministic-vs-verified language and
the level-4 architectural ceiling, and evaluate the NIST Generative AI Profile for agentic rows;
(2) a canonical-data-driven, accessible method selector with shareable URL state; (3) an explicit
offline→shadow→advisory→operator-approved→bounded-supervisory promotion worksheet plus a versioned,
semantically defined AI-result contract; and (4) row-level evidence provenance and a primary-source,
applicability-scoped machinery/AI checklist.

The plan explicitly preserves all authority gates: no authority ceiling is raised, all ten
chemical/biological rows remain `Planned`, and evidence closure, adversarial authority review, or
layer-design pages remain Phase 49c work requiring separate owner authorisation. Existing dirty
worktree changes for the active Phase 50.1/50.2 corpus-quality slice were not touched. Validation for
this planning-only edit: Markdown/diff inspection and whitespace check; implementation gates are
defined per slice in the plan.

## 2026-07-16 — Phase 50.12 — AI/ML page correctness & safety-language pass

**Type:** Corpus source metadata + site presentation. Fixes live errors on the deployed page.
**Branch:** `feat/phase50-corpus-quality-validator` (stacked after 50.2 + Workstream-E plan).

Three verified-live defects corrected; no new authority claims, chemical/biological rows stay Planned:

- **Factual: source identity.** `sources.yml` titled the standard `IEC TR 5469:2024`; corrected to
  **`ISO/IEC TR 5469:2024`** (joint identity; publisher `ISO/IEC`) with "Technical Report: guidance,
  not certifiable requirements" inline — matching the Phase 49a governing finding, which had already
  flagged this exact error. Register data regenerated (site title synced).
- **Safety language: veto-gate code.** The example returned `baseline.compute(state)` on every failed
  check ("deterministic fallback"), implying a deterministic fallback is automatically safe. Replaced
  with `on_fail(state, reason=…)` and prose stating the response is the application's
  hazard-analysis-derived policy (bumpless transfer, bounded-lifetime hold, manual takeover, defined
  safe state, or shutdown) — deterministic ≠ automatically safe. Envelope diagram's VETO node
  relabelled "defined failure response".
- **Ceiling clarity.** Added a paragraph by the ladder: level 4 is an architectural *ceiling* for a
  learned method behind a verified envelope, not an authority any learned row currently holds — the
  three level-4 rows (Kalman, MPC, first-principles) are deterministic/model-based; no learned row
  exceeds level 3. Envelope subgraph relabelled "operational authority ≤ 4 (architectural ceiling)".

**Deferred within 50.12:** adding the NIST AI RMF Generative AI Profile as an evidence source and
re-evaluating the language/agentic rows — that is an evidence/claim change needing judgment, not a
rush job. Full release gate PASSED. **Workstream E remaining:** 50.13 selector, 50.14 deployment-gate
worksheet + versioned result contract, 50.15 evidence provenance + machinery/AI checklist.

## 2026-07-16 — Phase 50.2 — corpus-quality validator + metadata completeness

**Type:** Tooling + governance + corpus metadata. Structural prevention for the 50.1 defect classes.
**Branch:** `feat/phase50-corpus-quality-validator`.

Root-cause fix so the 50.1 defects cannot recur silently:

- **New `tools/validate_corpus_quality.py`** — hard-fails on conversational AI artifacts
  ("Would you like…", "If you want, I can…", "Shall I…") and empty numeric placeholders
  ("between ** and **", "typically  to ", "of  to  times"). Wired into `release_check.py`'s corpus
  and full profiles; four self-tests in `tests/tools/test_validate_corpus_quality.py` prove it
  catches both classes, ignores READMEs, and passes clean content (including legitimate ranges like
  "`PL c` to `PL d`", which an earlier draft pattern false-flagged and was corrected).
- **Corpus metadata debt driven to zero.** Backfilled `CONTENT_CLASS` and/or `STATUS` on 37 files
  that lacked them (22 missing CONTENT_CLASS, 37 missing STATUS): iec_62443 clause files →
  `RAG_APPROVED`; overviews, reference models, admin/tracking, and generation notes →
  `DERIVED_REFERENCE`; all missing `STATUS` → `DRAFT` (the corpus's conservative default). The
  `release_check.py` ratchet baselines dropped from 25/37 to **0/0**, so any future RAG file missing
  a header is now a hard release failure (verified with a probe file).
- **Header schema documented** in `governance/AI_WORKFLOW.md` §1 — the `AI_READ_ACCESS` /
  `CONTENT_CLASS` / `STATUS` fields, their allowed values, and the two content defect classes were
  previously an undocumented convention (the reason authors omitted them); now a governed table with
  an enforcing validator.

Verification: full release gate PASSED — 160 tests (4 new), 10 doctests, clean build, zero broken
links, exact mirror and register equality; the two RAG metadata warnings are **gone** (only the
site review-block backlog warning remains, tracked as 50.9). Mirror regenerated (37 files).
**Workstream A remaining:** 50.3 `_index.yaml` reconciliation (iec_62443 + offshore absent from the
standards inventory; case-mismatched software-safety reference).

## 2026-07-16 — Phase 50.1 — corpus correctness (authoritative-tier defect fixes)

**Type:** Corpus (source-of-truth) correction; site mirror regenerated to match. No toolkit change.
**Branch:** `fix/phase50-corpus-correctness`.

Fixed the long-standing authoritative-tier defects catalogued in the 2026-07-16 audit, including two
conversational artifacts the whole-tree grep found that earlier lists had missed:

- **Conversational AI artifacts removed/neutralized (5).** Two lead-ins that precede real
  cross-reference content were rewritten as neutral references (`reference_models/Universal Machine
  Safety Architecture.md`, `7-Layer Industrial Machine Architecture Model.md`); three trailing
  conversational offers were deleted (`crosswalks/overlap_matrix/standards_decision_workflow.md`,
  `crosswalks/overlap_matrix/standards_overlap.md`, `iec_60204_1/…Clause18__verification.md`).
- **NFPA 79 Ch06 numbering bug fixed.** The overcurrent-protection file called itself "Chapter 7"
  twice in body text (metadata was already correct); both now read "Chapter 6".
- **NFPA 79 Ch15 suspect citation flagged.** The unverifiable "Table 7.2.7" transformer-protection
  citation is replaced with an inline "table reference unverified — confirm the exact number"
  flag rather than a guessed number.
- **Three empty placeholders gap-flagged, not fabricated.** NFPA 79 Ch04 ambient-temperature range,
  Ch17 bend-radius multiplier, and IEC 60204-1 Clause 05 voltage-tolerance band carried blank
  values (`between ** and **`, `typically  to `, `of  to  times`). Per the plan and the repo's
  copyright posture (numeric table values are not stored) and because the licensed text is not
  available to verify here, each is replaced with an explicit "NOT IN LOCAL CORPUS — transcribe from
  the licensed text before use" flag pointing at the governing clause.
- **`iec_60204_1/README.md` stub replaced** with a real module README (clause map, edition note,
  copyright/placeholder policy).

Verification: whole-tree grep shows zero residual conversational artifacts and zero empty
placeholders; RAG mirror regenerated (314 files, byte-identical); full release gate PASSED (156
tests, 10 doctests, clean build, zero broken links, exact mirror and register equality). Pre-existing
metadata-completeness warnings (CONTENT_CLASS/STATUS) are unchanged — that is the separate 50.2 slice.
Still open in Workstream A: the corpus-quality validator (50.2) and `_index.yaml` reconciliation
(50.3).

## 2026-07-16 — Phase 50 slice — per-method examples + context panel on AI integration page

**Type:** Corpus register schema addition + site presentation. Page remains **Review pending**.
**Branch:** `feat/phase50-register-examples`.

Added a concrete example to every method in the canonical register. Corpus:
`control-standards/rag/design_framework/ai_integration/methods.yml` gains an `example` field on all
42 rows, inserted after `does`, each an illustrative typical use kept strictly inside that row's
own `does`/`justified_when` scope (no new capability or authority claims, no product endorsement).
Generator: `example` added to `REQUIRED_METHOD_FIELDS` in `tools/generate_ai_method_register.py`
(enforced, not merely tolerated) with a new `test_register_requires_example` and the fixture
updated; site data regenerated to `docs/_data/ai_methods/` (exact-equality gate green). Page:
entry template renders `<dt>Example</dt>`; the how-to-read key documents the field and labels the
examples illustrative.

Context panel: the page previously showed only the generic status note. Added topic-appropriate
frontmatter — `related_standards` (ISO 13849-1, IEC 62061, IEC 61511, IEC 61508, IEC 62443, and the
Software Stack routing page — the functional-safety and OT-cyber standards the register references),
`lifecycle_stage` (Risk Assessment, Safety Architecture, Detailed Design), and `repo_path` to the
canonical register — so the right rail now routes to the standards and lifecycle stages the topic
depends on.

Gates: full release profile PASSED (155→156 tests incl. the new example test, 10 doctests, 374
boundary files, exact mirror and register data, clean Jekyll build, zero broken internal links);
rendered page verified — 42 example rows, populated Related Standards and Lifecycle Stage panels.

## 2026-07-16 — Phase 50 site slice — plain-language pass on the AI integration page

**Type:** Site presentation change only; register data untouched; page remains **Review pending**.
**Branch:** `feat/phase50-ai-integration-plain-language`. Owner feedback: the deployed page was hard
to understand for readers coming from industrial automation / OT without a functional-safety
background.

Added comprehension scaffolding with no new authority claims: (1) "The idea in plain terms" —
what AI/ML integration means in an OT path, the deterministic-vs-learned distinction, and why the
page's three demands (beat a deterministic alternative, survive validation, independent protection)
follow from it; (2) a nine-term glossary (authority, envelope, veto, independent protection, safety
function, Planned, …) so load-bearing vocabulary is defined before first use; (3) "One task up the
ladder" — one pump condition-monitoring scenario shown at every authority level, each level naming
a method that can actually hold it in the register (1D CNN at 2, MPC at 4, PID at 5); (4) a
"how to read an entry" key for the eleven register fields; (5) one-sentence plain-terms leads on
the envelope-architecture and high-rate-data sections. Gates: site profile PASSED (clean build,
zero broken links); rendered page verified.

## 2026-07-16 — Phase 50 site slice — AI integration page visualization pass

**Type:** Site presentation change only. The corpus register and `docs/_data/ai_methods/` are untouched.
**Branch:** `feat/phase50-ai-integration-page-design`. Page remains **Review pending**.

Redesigned `/design/ai-integration/` from a text-and-collapsed-entries register into a visual
decision path, per the owner-approved proposal (layout approved; content fact-checked against
`methods.yml` and the Phase 49a findings before build). Added, using the site's existing
`mermaid-wrap` pattern: (1) the gate question as a decision flowchart — with the corrected logic
that a deterministic alternative meeting the requirement is *preferred unless* a specific validated
advantage is demonstrated, and "keep the method offline" as an explicit terminal; (2) the authority
ladder as a Liquid-generated diagram whose node labels are emitted from `register.authority_levels`
(cannot drift from data), with the level 4→5 boundary scoped exactly as the register states it
("no learned method is assigned level 5 in this register"); (3) a new envelope-architecture section
drawing the Phase 49a convergent pattern (learned policy inside the envelope; verified non-learned
layer holds the safety function and veto; the safety-function path never routes through the learned
layer) plus a veto-gate code block whose failure fallback is the register-guaranteed deterministic
baseline; (4) a two-lane acquisition-path diagram for the kHz rule carrying the four 49a constraints
(sampling floor, no source-update knowledge, historian compression, segmentation) and blaming the
path, not OPC UA; and a result-contract JSON showing exactly the page's six required fields, with
training-set id and authority tag noted as optional strengtheners. Register usability: per-family
comparison tables (method, max authority, must-beat, maturity) generated from the same data, anchor
ids on every entry, a maturity/evidence-strength legend, and a leakage-aware validation-split
callout for the perception family that restates only the rows' own failure-mode/validation fields.

**Content corrections made during fact-check, before build:** removed an invented "ISO 10816"
baseline and an invented "10–100 ms" scan figure from the draft; replaced paraphrased ladder labels
with register text; corrected maturity vocabulary to *industrially routine · piloted · research*;
narrowed the perception callout after verifying all four rows' actual leakage variants.

Gates: full release profile PASSED (155 tests, 10 doctests, 374 boundary files, exact mirror and
register data, clean Jekyll build, zero broken internal links across 371 files; pre-existing
non-regression warnings unchanged). Rendered page verified: 4 mermaid blocks, 9 family tables,
anchors resolve, ladder labels verbatim from data.

## 2026-07-16 — Phase 50 recorded — whole-project audit and next-phase plan

**Type:** Planning and next-phase handoff. No code, site, or corpus changes in this entry.
**Plan:** `planning/2026-07-16-phase50-hardening-hygiene-plan.md`

Ran a four-track whole-project audit (toolkit, site, corpus/governance, repo hygiene) and reconciled
it against the accepted `planning/2026-07-13-whole-project-architecture-recommendations.md`.

**Verified complete (execution-sequence rows 1–4):** P0.1 I/O direction (`Tag.io_type` structural,
heuristic fallback only, `YL-301` → coil with regression tests), P0.2 UL 508A provenance (zero
`508A:2022` in committed code/site/corpus; only a stale git-ignored local `docs/_site` remains),
P0.3 mirror (byte-identical, 314 files), release-check module (`tools/release_check.py`, 5 profiles)
running `--profile full` in CI on push and PR. Audit-day gates all green: 155 tests, 10 doctests,
clean Jekyll build (3.22 s), zero broken internal links (371 files), 374/374 AI-boundary files,
`.git` 21 MB, no secrets/PII, no licensed values committed.

**Verified NOT started (rows 5–7):** licensed-table validation + packaging (presence-only key check;
pymupdf/pypdf still unconditional core deps; wheel ships no schemas/samples), validated-I/O seam
(duplicate tags silently overwrite loop sheets; generators and most CLI commands skip validation),
thin CLI + tests (`cli.py` 486 lines and `cite.py` are the only untested modules), site metadata
rollout and project_state split.

**New findings folded into Phase 50:** unfixed factual defects in the authoritative corpus (NFPA 79
Ch06 "Chapter 7" numbering, Ch15 "Table 7.2.7" suspect citation, 3 empty placeholders incl.
IEC 60204-1 Cl05, 3 conversational AI artifacts in reference_models + Cl18) with no validator
covering these defect classes; undocumented `CONTENT_CLASS`/`STATUS` header schema; `_index.yaml`
omits iec_62443 and offshore and carries a case-mismatched reference; tracked `temp/` intake (24
files) violating PROJECT_ORGANIZATION; dead `main.py`; stray tracked root binaries; 34 stale local
branches; environment.md drift (Python 3.13 pin vs 3.12.7 interpreter; stale test counts);
283/360 site pages without `review:` blocks (vendor/ and industries/ at zero); 6 duplicate nav
URLs; 28/129 vendor links dead (all bot-gated Siemens portals).

Phase 49c authorisation state and all AI/ML gates are unchanged. Outstanding owner actions carried
forward in the plan's "Explicitly Out of Scope" section.

## 2026-07-13 — Phase 49b — AI/ML method register complete

Completed the hardening gate and the authority-first AI/ML register. The canonical Draft register is
under `control-standards/rag/design_framework/ai_integration/`; a dependency-free validator/generator
publishes exact data to `docs/_data/ai_methods/`, and the rendered page is
`/design/ai-integration/` at Review pending. Forty method rows span deterministic baselines, learned
methods, interfaces, chemical models, and biological models. Every row carries the complete decision
and safety schema. Learned methods receive no level-5 or safety authority; chemical and biological
rows remain Planned because Phase 49a did not complete adversarial authority coverage for them.

Added register tests and an exact generated-data check to the governed release gate. The page rewrites
the kHz statement around the conventional acquisition path rather than falsely constraining OPC UA as
a protocol, and distinguishes transport semantics from application-defined AI-result meaning.

Validation: the full governed release gate passed — 155 tests, 10 doctests, 374 boundary checks,
exact corpus mirror, exact generated register data, clean Jekyll build, and zero broken internal links
across 371 rendered files. The gate reports only the recorded non-regression debt: 22 corpus files
without `CONTENT_CLASS`, 37 without `STATUS`, and 166 site pages without review blocks.

## 2026-07-13 — Phase 49b — whole-project architecture recommendation accepted

**Type:** Planning and next-phase handoff.
**Status:** Recommendation recorded; no implementation changes in this entry.
**Plan:** `planning/2026-07-13-whole-project-architecture-recommendations.md`

Recorded the whole-project assessment as the Phase 49b hardening gate without replacing the existing
AI/ML method-register scope. Three P0 prerequisites now precede AI/ML implementation: preserve I/O
direction through the PLC module and fix the confirmed `YL-301` Modbus mapping defect; normalize stale
`UL 508A:2022` provenance across code/site/corpus; and regenerate plus compare the two drifted RAG
mirror files. A governed release-check module and CI adoption are required before the Phase 49b merge.
The remaining table-validation, validated-I/O, CLI/package, site-metadata, and project-state work is
sequenced as bounded hardening slices in the plan.

**Evidence recorded in the plan:** 145 tests passed; 10 doctests passed; Jekyll build clean; zero broken
internal links across 370 rendered HTML files; 372 AI-boundary files passed. This change added planning
and tracking documentation only, so code/site/corpus validation gates were not rerun for the edit.

## 2026-07-13 — Phase 49a — AI/ML source-closure research sprint

**Type:** Research (work tier). **No site or corpus content was written.**
**Status:** Complete on `feat/phase49a-ai-ml-source-closure`.
**Spec:** `docs/superpowers/specs/2026-07-12-ai-ml-methods-register-design.md`
**Plan:** `docs/superpowers/plans/2026-07-12-phase49a-ai-ml-source-closure.md`

Executed as a multi-agent workflow (owner-authorised): six parallel research workstreams under
publisher-verification rules, then an adversarial stage that attacked every proposed authority ceiling.
**98 claims — 72 VERIFIED_AT_PUBLISHER, 21 SECONDARY_ONLY (paywall), 3 UNVERIFIABLE, 2 NOT_FOUND.**
**80 authority ceilings attacked; 76 refuted** — and essentially every refutation pushed the ceiling
**down**, which is the intended asymmetry.

**New (work tier):** `evidence-table.md` (98 claims, each with a *"what this source does NOT support"*
column) · `authority-ceilings.md` (written to read as a list of what could **not** be justified) ·
`adversarial-verdicts.md` (raw) · `49a-findings.md` (go/no-go) · `source-register.md` extended.

**The governing finding.** ISO/IEC TR 5469:2024 is real (Ed. 1.0, 2024-01-08, verified at the IEC
webstore) — but it is a **Technical Report: guidance, not a certifiable requirement set**, and its
requirement-bearing successor ISO/IEC TS 22440 is still a committee draft. **There is therefore no
published normative standard against which a learned closed-loop safety function could be certified.**
Meanwhile the law has moved ahead of the standards: **Regulation (EU) 2023/1230** Annex I Part A items
5–6 list ML-based self-evolving safety components (mandatory notified body; no self-declaration), and
Annex III EHSR 1.2.1 codifies an authority ceiling — no action beyond the defined task/movement space,
correctable at all times, no hazardous self-modification of safety rules *including during learning*.
The AI Act binds to the same route ~6 months later. **The convergent architecture, found independently
in the standards, the law, and every documented deployment: the learned policy holds operational
authority inside an envelope; a verified non-learned layer holds the safety function and the veto.**
Write *"learned control is used in the loop; it is never given the safety function"* — **not** "learned
control is never used in the loop", which is false.

**Also confirmed:** Phase 45's **20 Jan 2027** Machinery Regulation date is correct — but only via the
Corrigendum of 4.7.2023; the uncorrected OJ text says 14 January.

**Three orchestrator errors the sprint caught** (the design was built to survive exactly this):
1. **"kHz signals cannot pass through OPC UA" is FALSE as a protocol claim** — PubSub/UADP over TSN has
   been measured at a 250 µs cycle. The edge-inference conclusion survives, but on four *different*
   constraints (server-imposed sampling floor; the server has no knowledge of a decoupled source's update
   logic, so a waveform cannot be recovered by oversampling a scan-rate tag; historians compress by
   design; segmentation). **The argument must be rewritten before it goes on the site.**
2. **The standard is ISO/IEC TR 5469, not "IEC TR 5469"** — and it is guidance, not requirements.
3. **The accelerometer-vs-drive-current question is answerable, and the answer went against drive
   current** — Paderborn carries both signals synchronously at 64 kHz on the same 32 bearings, and
   vibration beat motor-current in every case (98.3% vs 93.3%; 75.0% vs 45.9% train-artificial/test-real).

**Other load-bearing negatives:** PINNs lose to FEM at equal accuracy (5–6 orders of magnitude on
Allen-Cahn) and revert to a plausible-but-wrong steady state when the data flow stops — while the PDE
residual can stay small, so a residual-based health monitor can be fooled. The CNN fault-diagnosis
literature is contaminated by train/test leakage: under a strict bearing-wise split, performance
collapses to near chance (Paderborn AUROC 99.9 → 53.2). **No source measures learned fault diagnosis on
a real industrial fleet.** **No standard says how good an ML model must be to hold any safety
authority** — that void is itself a finding. **Licences:** Paderborn is CC BY-NC (NonCommercial); CWRU
has *no licence of any kind* — cite and link it, never redistribute.

**Go/no-go:** **GO** for core AI/ML, interfaces (with the mandatory kHz rewrite), and classical
baselines. **PARTIAL** for chemical and biological — their *structure* and *reality check* may be
written, but **their authority ceilings received no adversarial coverage** (the run hit a session limit)
and no authority claims may be made until re-run.

**Run limits, recorded honestly:** the workflow hit a session limit during the refute stage — 82 of 178
agents errored, and the synthesis agent died. The research (the expensive part) survived and was
salvaged from the run journal; the four documents were written by the orchestrator from that data. Only
2 of 80 ceilings received all three adversarial lenses; most received one. **The workflow's own printed
tally ("29 refuted") was wrong** — it applied a ≥2-refutation majority rule to claims that had only one
surviving verdict. Recomputed against returned verdicts: **76 of 80 refuted.**

**Blocked / next:** buy **ISO/IEC TR 5469:2024** (its Usage-Level × Technology-Class matrix is the single
highest-value missing artefact); check **IEC 62061** for ML content; re-run adversarial coverage for
chemical/biological. **Phase 49b remains gated** on that and on the owner confirming the
`/design/ai-integration/` placement.

## 2026-07-12 — Phase 48 — PLC/IPC hardware reference + vendor documentation index

**Type:** Content expansion (data-driven reference pages)
**Status:** Complete on `feat/phase48-plc-hardware-vendor-docs`. Both pages at **Review pending**.

Two new pages under `/tools/manufacturers/`, both rendered from committed YAML data files rather
than hand-maintained tables, so the reference set can be re-verified and updated without touching
page prose.

**New data files**

- `docs/_data/manufacturers/vendor_doc_links.yml` (1,078 ln) — 129 curated official-documentation
  links plus 8 master portals across Siemens, Allen-Bradley/Rockwell, and Beckhoff. `utm_source`
  params stripped. Liveness-checked 2026-07-12: **101/129 return 200/206**; all 28 failures are
  `sieportal.siemens.com` / `support.industry.siemens.com`, which are bot-gated to `curl` and
  expected to resolve in a browser — not dead links. The **publication ID is carried as the stable
  reference** precisely because URLs move.
- `docs/_data/manufacturers/plc_hardware_families.yml` (390 ln) — 38 controller and IPC families.
  **Every `status` value carries an `as_of: July 2026` field** and a file-level lifecycle warning:
  these are vendor market/lifecycle claims with a shelf life, not durable facts.

**New pages**

- **Official Vendor Documentation Index** (`/tools/manufacturers/vendor-documentation/`) — master
  portals, per-vendor manual tables, and the exact-model lookup method (nameplate order number →
  vendor portal → current manual → firmware compatibility → archive the revision you designed
  against). Carries a safety-documentation caveat: a safety function is never designed from a
  general product manual.
- **PLC & IPC Hardware Families** (`/tools/manufacturers/plc-hardware-families/`) — the three
  architectural models (Siemens separates PLC and PC platforms; Rockwell centres on a dedicated
  Logix controller; Beckhoff treats the IPC-plus-TwinCAT-runtime *as* the controller), a Mermaid
  selection flowchart driven by application requirement rather than brand, cross-vendor mapping by
  system size, Siemens suffix decoding (F/T/TF/R/H/S/V/D-TF), an "industrial PCs are not
  controllers" section, 7 numbered common mistakes with root causes, and a practical checklist.

**Editorial discipline applied to the source**

- The source document's market-positioning language was softened per CONTENT_STANDARDS §6 — no
  "clearest", "best", or ranking claims survive; families are named as examples.
- Every lifecycle claim is dated and marked verify-current. The **CompactLogix 5390 is recorded as
  announced, not shipping** (vendor-published availability Q4 2026), and is called out as a common
  mistake rather than presented as an available option.
- Cross-vendor size rows are explicitly labelled equivalences of *role*, not of performance.
- Safety framing hardened beyond the source: reaching "integrated safety" in the selection flow
  tells you which families *offer* a safety variant, not which integrity level the application
  needs — that comes from the risk assessment, and the certification documents for the exact
  hardware revision govern the claim.

**Source relocation** (per PROJECT_ORGANIZATION — `temp/` is intake only)

- `temp/plcs.md` → `control-standards/work/general/plc_ipc_hardware_intake_2026-07.md` (work tier =
  non-authoritative capture), with all `utm_source=chatgpt.com` params stripped and the dead
  `sandbox:/mnt/data/` download link replaced with the workbook's real location.
- `temp/PLC_IPC_Official_Reference_Links.xlsx` → `planning/`.

**Wiring:** both pages added to `docs/_data/navigation.yml` under Manufacturers and to the
`/tools/manufacturers/` section index under a new "Deep Dives" group — no orphan pages.

**Gates:** Jekyll build clean (2.074 s); `check_internal_links.py` — zero broken links across 370
files (up from 368); `validate_ai_boundaries.py` at the pre-existing 2-failure baseline, no new
regressions.

**Known limits:** family-level only — no per-CPU specifications, performance figures, or prices;
the vendor ordering documentation stays authoritative. Lifecycle statuses will go stale and are
labelled as such on the page itself.

## 2026-07-12 — Phase 47 — PLC software expansion (4 pages + 4 corpus notes)

**Type:** Content expansion (corpus-first)
**Status:** Complete on `feat/phase47-plc-software-expansion`.

The `/fundamentals/plc-software/` section doubled from 4 to 8 pages, executed corpus-first per
CONTENT_STANDARDS §1: each topic landed as a deep corpus note in
`control-standards/rag/training_modules/plc_software/`, then as a site distillation. Written by
four parallel writer agents under one shared spec (AI_WORKFLOW §4); every page starts at
**Review pending**.

**New pages / corpus notes** (site lines / corpus lines):

- **Ladder Logic Fundamentals** (257/509) — element set, seal-in walkthrough, fail-safe
  NC-wired stops, I/O mapping at the edges, command vs status vs feedback, constructed
  motor-control example with failed-to-start detection, scan-order effects, last-write-wins,
  one-shots, retentive data, alarm delay + hysteresis, analog scaling, 9 numbered design
  mistakes with root causes.
- **PLC Algorithms & Equipment Staging** (232/482) — FIFO/circular buffers, conveyor shift
  registers, queue records, sorting at PLC scale (index-array pattern), and the staging family:
  lead-lag, demand staging with dead-band/anti-hunting, runtime accumulation/equalization,
  start-count balancing, round-robin, first-available, priority- and capacity-based selection,
  start-delay sequencing, failed-to-start replacement, load-shedding and alarm queues.
  Cross-links water/wastewater intake-pumping (the lead-lag field application).
- **PackML, ISA-88 & ISA-95** (242/459) — the deep treatment the machine-state-model page's
  one-row summary was pointing at: PackML state/mode models (acting/wait, state-complete),
  PackTags at concept level, the wrapper-vs-sequence distinction, ISA-88 physical + procedural
  models and EM/CM decomposition, ISA-TR88.95.01 bridge, ISA-95/IEC 62264 levels 0–4, brief
  pharma (GAMP 5, Part 11) and semiconductor (SECS/GEM) mappings. No state-transition tables or
  tag lists reproduced (copyright boundary).
- **Vendor Programming Architectures** (234/515) — how Siemens TIA Portal (OB/FC/FB/DB,
  instance DBs, process image), Rockwell Logix (task→program→routine, tag-centric memory, UDTs,
  AOIs, RPI-asynchronous I/O), and Beckhoff TwinCAT 3 (PC-based runtime, OO extensions, linked
  I/O layer, EtherCAT) each implement the shared IEC 61131-3 model; 13-row concept-translation
  table; the same FIFO and staging skeleton three ways. All market-position language from the
  source reframed to neutral fit language per CONTENT_STANDARDS §6.

**Source discipline (roadmap Phase 47 requirements, all met):**

- `temp/plc_software.md` (4,976 lines, 4 concatenated source docs) relocated to
  `control-standards/work/general/plc_software_intake_2026-07.md` with every `utm_source`
  param stripped (28 occurrences → 0).
- All 31 cited URLs liveness-checked after stripping: 24 return 200/206; the 7 failures are
  bot-gated portals (Siemens Industry Support ×5, ISA blog, SEMI), not dead links. Site pages
  cite by document name/publication ID only; cleaned URLs live in the corpus notes' Sources
  sections.
- One citation defect found and fixed: the source attributed the Logix tasks/programs/routines
  manual to the URL of 1756-PM006 (Sequential Function Charts); the correct reference
  1756-PM005 is cited in prose and the PM006 URL is now labelled accurately.
- Paraphrase-only throughout; illustrative code labelled, invented tags, constructed examples
  marked; platform-specific raw-count endpoints dropped rather than asserted.

**Wiring:** navigation.yml + section index carry all 8 pages in learning order (Languages →
Ladder Logic → Program Structure → State Machines → Algorithms & Staging → PackML/ISA-88/ISA-95
→ Vendor Architectures → Safety Application Patterns). RAG mirror regenerated
(`generate_rag_tree.py`, 314 files, 4 new).

**Validation:** Jekyll build clean (1.656 s); `check_internal_links.py` zero broken links
(368 files); `validate_ai_boundaries.py` 2 failures = pre-existing baseline
(`process_safety_details/`), no new regressions.

## 2026-07-12 — Phase 46.1 — Design-page review triage + AI/ML presentation plan

**Type:** Correctness fixes (site consistency) + planning record
**Status:** Complete on `fix/phase-46.1-design-page-defects`.

**A fourth external review was found untriaged.** `prompt.md` — 1,068 lines, untracked at the
repo root — was never part of the `temp/` intake batch. It is a review of the `/design/` page,
and it is also the **upstream source of the wire-colour and design-package assets published in
Phase 46**: that phase shipped from its downstream artifacts without the source document ever
being read. Now relocated to `planning/2026-07-12-design-page-review.md` with a triage record.

**Three defects verified against the repo and fixed:**

- **Lifecycle stage count — wrong in three places, and worse than the review said.** `/design/`
  and the homepage claimed **11 stages**; `/lifecycle/` claimed **13**; the lifecycle index
  actually publishes **14**. Neither number was correct. Adopted the review's own better
  recommendation and **dropped the count** rather than restating a number that keeps rotting as
  stages are added.
- **The "through decommissioning" endpoint was also false** (found while fixing the above):
  **there is no decommissioning stage page.** The claim is corrected, and an explicit
  coverage-gap note added to `/lifecycle/` — the functional-safety standards (IEC 61508, 61511,
  62061) all define a lifecycle through decommissioning, so the gap is now stated rather than
  papered over.
- **Duplicate sidebar entry** — "Motor Selection" appeared twice (navigation.yml:133 and :145).
  Disambiguated to *Motor Selection Fundamentals* (section) and *Motor Selection Workflow*.
- **"Standards Atlas" branding survived on live pages** — the standards-finder rendered a card
  titled "Standards Atlas" and the nav read "About this Atlas". (Phase 45's review flagged the
  same leak on the NEC page; that pass fixed the status labels but missed the branding.) Card →
  *Standards Library*; nav → *About this Field Guide*. Site identity is now **Control Systems
  Engineering Field Guide** throughout.

**AI/ML for Control Systems — presentation plan recorded (Phase 49, still gated).**
Research relocated `temp/ai-ml-control-systems-research/` →
`control-standards/work/research/ai-ml-control-systems/` (work tier, non-authoritative — the
intake loop's capture tier, which `temp/` is not). Plan at
`planning/2026-07-12-ai-ml-control-systems-presentation-plan.md`. **No site or corpus content
authored** — the workspace carries the owner's explicit do-not-build-yet posture, which stands.

Two substantive decisions in the plan:
- **Placement:** one subsection under Design (`/design/ai-integration/`), **not** split across
  Fundamentals and Design. Co-location is a *safety property*: a reader landing on "CNNs" or
  "LLMs" from a search engine must not meet the capability with the authority gate seven entries
  away.
- **Authority-first, not topic-first.** The research's own provisional tree put safety **8th of
  9**. Reordered so the least-authority ladder (offline → read-only → advisory →
  operator-approved → bounded supervisory → closed-loop) and the safety boundary are pages 1 and
  2, with model families, the digital-twin spine, interfaces/handshakes, validation & drift, and
  worked architectures hanging off them. The scientific-domain track is deferred — real, large,
  and currently unsourced.

Promotion remains gated on the source-register's own "still needed" list — most importantly
*current standards or guidance for AI in machinery and functional safety*, without which the
safety page would be inventing a position — and on re-checking the two 2024 arXiv preprints
against the publisher, per the Phase 45 precedent.

**Validation:** clean build (364 files), zero broken internal links.

## 2026-07-12 — Phase 46 — Visual assets (wire colour coding gallery + design-package poster)

**Type:** New content (reference gallery) + first image assets on the site
**Status:** Complete on `feat/phase-46-visual-assets`.

- **New page** `/design/wiring/wire-color-coding/` — 15 reference diagrams in 8 groups (reference
  standards · machinery & facility power · PLC and control circuits · instrumentation & IS ·
  VFD/servo/motion · HVAC & semiconductor · industrial networks · field notes). Written around two
  things colour actually does: **orange = may still be live with the disconnect OFF**, and
  **green/green-yellow = protective earth, never anything else**. Everything else is convention in
  service of traceability — colour narrows the *kind* of circuit; the wire number and drawing identify
  *which*. AHJ/customer-drawings precedence caveat at the top, per the asset README's own instruction.
- **Two collisions called out explicitly** (not in the source assets — added from the diagrams read
  side by side): **orange** is the L2 phase in a US 277/480 V facility *and* the
  external-live-with-disconnect-off marker in NFPA 79 machinery — and a machine panel fed from a 480 V
  facility can contain both. **Light blue** is simultaneously the IEC neutral, an IEC DC common, and
  the intrinsic-safety marking colour.
- **Design-package poster** embedded on `/tools/templates/` — a pump & VFD skid carried through all ten
  deliverables (P&ID → network → SLD → I/O list → cause & effect → panel layout → sequence → ladder →
  HMI → hookup), showing how they reference each other. Carries the required
  *products-shown-are-examples* caption (the poster depicts named vendor hardware as generic icons).
- **Cross-links:** wiring index (new "Reference Gallery" group), sidebar nav, US industrial control
  panel scenario, global machine scenario.
- **CSS:** `.diagram-grid` / `.diagram-card` added to `main.css`, remapped from the source README's
  MkDocs variables onto this site's design tokens. Images keep a white ground in dark mode so the
  PNGs' own white background does not fight the panel.

**One asset withheld.** `14-legacy-panel-before-after.png` is **not published**. It is the only asset
containing **photographs of real control panels**, and their provenance is unknown — the repo's
copyright posture is original diagrams only, never third-party photos or vendor screenshots, and
Phase 45 is a fresh reminder of what unverified source material costs. It stays in `temp/` pending the
author confirming he shot those photos himself. (It is also clipped on its right edge.)

**Asset defects recorded, not hidden:** `15-important-wiring-notes.png` carries a sliver of an
adjacent panel on its left edge, and `06-120vac-control-circuit.png` is slightly clipped at the right.
Both are cropping artifacts in the source deck; the 15 note is disclosed in its caption rather than
silently shipped.

**Also fixed:** the global-machine scenario still carried the stale **NFPA 79 "600 V max"** scope — a
Phase 45 correction this page was missed by. Now 1000 V, with the conductor-identification row
expanded and pointed at the new gallery.

**Alt text was written from the diagrams, not from `assets.json`** — the shipped alt strings were
auto-generated filename echoes ("05 Plc 24Vdc Io Wiring") and are useless to a screen reader. Every
diagram was opened and described.

**Validation:** clean build (364 files), zero broken internal links, both pages rendered and checked in
a browser (gallery grid, poster, dark mode, nav entry, review-meta). The 2 AI-boundary violations in
`control-standards/rag/process_safety_details/` remain **pre-existing on `master`**.

## 2026-07-12 — Phase 45 — Standards accuracy pass (safety-significant)

**Type:** Correctness fixes to published standards content + corpus structure
**Status:** Complete on `fix/phase-45-standards-accuracy`.

Claim-by-claim triage of the third external review (`planning/2026-07-11-standards-accuracy-review.md`,
with the full triage record appended to it). **Every edition claim was verified against the official
publisher before adoption** — IEC webstore, ISO catalogue/OBP, NFPA, UL Standards, EUR-Lex. Claims the
publisher's free text could not settle are marked UNVERIFIABLE and carry a verify badge on the page
rather than a confident assertion.

**Safety-significant corrections (site + corpus):**
- **ISO 12100 → PLr misattribution.** The S/F/P risk graph that yields PLr is in **ISO 13849-1 Annex A**,
  not ISO 12100 (which supplies the risk-assessment methodology); IEC 62061 has its own SIL method.
  Corrected in the corpus (ISO 12100 Cl.5/Cl.7, ISO 13849-1 Cl.4/Annex A, IEC 62061 Cl.6) and on the
  ISO 12100, ISO 13849-1, IEC 62061 and functional-safety family pages.
- **ISO 13849-1 / IEC 62061 are alternative routes**, not a ladder. Removed the false rule that IEC 62061
  is "required when SIL > 2 is not achievable with ISO 13849-1".
- **IEC 60204-1 edition, scope, clause structure, emergency stop.** Edition corrected to
  **2016+AMD1:2021** (no "2018" edition exists). The **"applies above 25 V AC / 60 V DC" lower threshold
  was fabricated** — the official scope sets only an upper limit (1 000 V AC / 1 500 V DC, ≤200 Hz).
  Clause table rebuilt to the real **18 clauses** (Clause 18 Verification was missing entirely).
  Emergency stop restricted to **Stop Category 0 or 1** (Category 2 is not an e-stop category).
- **CE marking.** Replaced "CE marking requires an ISO 12100 risk assessment" with the legally correct
  statement: EU machinery law requires a documented risk assessment and conformity with the applicable
  EHSRs; harmonised standards are **voluntary** and confer presumption of conformity. Added the
  **Machinery Regulation transition** — 2006/42/EC through **19 Jan 2027**, (EU) 2023/1230 from
  **20 Jan 2027** (note: the original OJ text says 14 January; only the corrigendum OJ L 169 makes it the 20th).
- **IEC 62443.** Part editions updated (**2-1:2024**, **2-4:2023**); **zones/conduits and SL-T moved to
  62443-3-2** (3-3 defines system security requirements and SLs); **removed the default SL prescriptions**
  ("most zones SL 2, safety zones SL 3") — SL-T must be derived from the documented risk assessment.
- **IEC 61511 SIL range — the review itself was wrong, and so were we.** IEC 61511-1:2016 Clause 1
  explicitly defines a maximum of **SIL 4** and a minimum of SIL 1. The page claimed "SIL 1–3 only; SIL 4
  is excluded" (an Edition-1 belief). Corrected to SIL 1–4.
- **UL 508A.** There is **no "UL 508A:2022"** — UL designates by edition + revision date. Corrected to
  **3rd Edition (2018-04-24), revisions through 2025-06-26**. Removed the implication that every
  industrial control panel must be UL listed (NEC Art. 409 mandates *marking* incl. SCCR, not Listing;
  the requirement comes from AHJ / customer spec / insurance / contract).
- **NFPA 79 ↔ UL 508A** scopes are **complementary and overlap** at the machine control panel — they do
  not merely "interlock". UL's own guidance says reference to NFPA 79 may be needed for additional requirements.
- **NEC** now carries three separate fields (edition covered / latest published / legally applicable),
  supported by a new optional `edition_latest` + `edition_enforceable` in `_includes/review-meta.html`.

**Found independently, not in the review:**
- **NFPA 79 scope voltage was stale site-wide** — pages said 600 V; the current scope is **1000 V or less**.
- **The IEC 60204-1 corpus module had been drafted against the superseded 2005 edition** — its Clause 15
  carried the Ed. 5.0 title ("Accessories and lighting"), and it cited 9.2.5.4.2, which does not exist in
  Ed. 6. It had 15 clause files, **skipped Clauses 12 (Conductors and cables) and 13 (Wiring practices)
  entirely**, merged 16 and 17, and mis-numbered everything from 12 onward. Module renumbered against the
  official contents (files re-prefixed `IEC60204_1_2016A1__`, ~600 cross-references rewritten); Clauses
  12, 13 and 17 created (principles only — depth pass pending); `_index.yaml` rebuilt to 18 documents.
- **22 corpus files ended with an AI drafting artifact** ("Would you like me to move on to Clause 15?"),
  published through the RAG browser. All stripped.

**Status vocabulary sweep (CONTENT_STANDARDS §3):** removed every internal label from the presentation
layer ("Phase N Complete", "Corpus Complete", "Status in Corpus", shouty "REVIEWED"). Added real CSS for
the five governed badges (`badge--reviewed/partial/pending/revalidate/planned`) — `badge--complete` was
never even defined in CSS. **The review's proposed 6-term replacement vocabulary is REJECTED** (conflicts
with the binding 5-term vocabulary); the substance of the complaint was fixed using the existing terms.

**Page statuses:** every page whose technical content or edition metadata an agent touched dropped to
**Review pending** — per governance, an agent never marks its own work Reviewed. **IEC 62061 → Needs
revalidation**: its current reference is **2021+AMD1:2024+AMD2:2026 (CSV Ed. 2.2, published 2026-03-20)**;
the page was written against the base 2021 edition and must be rebuilt from the consolidated text, not
patched (SILCL → subsystem *maximum SIL*; scope extended beyond E/E/PE). 18 SILCL references remain by
design, flagged at the top of the page.

**Validation:** clean Jekyll build (363 files); **zero broken internal links**; RAG mirror re-synced
(310 files). The AI-boundary validator reports 2 violations in
`control-standards/rag/process_safety_details/` — **pre-existing on `master`, not introduced here**.

## 2026-07-11 — Phase 38 — Wiring & Installation Guides program + Wave 1

**Type:** New content genre (owner roadmap: consolidate practical control-system knowledge)
**Status:** Complete on `feat/phase38-wiring-guides`.

- **Program formalized:** `governance/ROADMAP.md` — full device matrix across 4 waves (VFD/sizing/grounding/EMC → PLCs/IPCs/remote-I/O/4-20mA/0-10V → servo/encoders → comm cables/safety/starters/control-power/RTD-TC), then troubleshooting engine, IEC 61131-3, comms expansion. Includes the knowledge-intake loop (rough field notes in work/ → agent-normalized into corpus via promotion checklist → guides). Wiring-guide page template added to CONTENT_STANDARDS §5 with genre rules (safety notice, consult-the-manual refrain, generally-accepted-practice labeling).
- **New corpus module** `rag/design_framework/wiring_practices/` — 4 source notes (vfd_wiring, wire_sizing_workflow, panel_grounding_bonding, emc_noise_mitigation; ~470 lines) with RAG headers, chapter/article-level citations only, field practice flagged. Mirror re-synced (287 files).
- **4 site guides** at `docs/design/wiring/` (+ section index showing planned waves; Design nav group):
  - How to Wire a VFD (260 lines, flagship) — line/load/control/brake terminal groups, table-FLC-vs-nameplate sizing via cst, inverter-duty cable + 360° shields, reflected wave, megger-before-connecting warning
  - Wire Sizing Walkthrough (247) — nameplate→conductor→OCPD→overload worked with REAL cst outputs (SAMPLE-data warning shown)
  - Panel Grounding & Bonding (180) — the three conflated jobs; shield one-end-vs-both-ends physics; table numbers cited, never values; writer corrected a corpus clause number against the published IEC 60204-1 edition
  - Noise & EMC Mitigation (192) — coupling mechanisms, separate/shield/filter hierarchy, 4-class separation table, flyback-diode drop-out caveat for safety circuits
- All guides at "Review pending"; validation: clean build (338 files), zero broken links, boundary-validator baseline unchanged, 145 tests pass.


## 2026-07-11 — Phase 37 — Governance documentation (binding standards for humans and AI)

**Type:** Project governance / documentation architecture
**Status:** Complete on `feat/governance-docs`.

- New `governance/` directory — four authoritative documents codifying everything established through Phases 0–36:
  - `PROJECT_ORGANIZATION.md` — the two-track model (site + cst toolkit fed by the reference library), directory roles with AI trust levels, the 9-section site taxonomy, a where-new-content-belongs decision table, naming/URL/redirect conventions
  - `CONTENT_STANDARDS.md` — corpus-is-ground-truth source discipline, the copyright boundary, the 5-term status vocabulary and review-block semantics, the Phase 30 standards-page template and the communications six-question template, calibrated-voice rules, privacy rules, validation gates
  - `ENGINEERING_STANDARDS.md` — the cst package's three design principles (citations on results, licensed-values-never-distributed, one-I/O-list), code rules (stdlib core, tests, no invented values), data-file conventions, template origins, the verification matrix
  - `AI_WORKFLOW.md` — read order, path trust tiers, branch/commit/ff-merge discipline, the phase loop (incl. mandatory project_state updates), sub-agent orchestration rules, external-review intake procedure (validate claims first; the JS-scraper lesson), safety rails (backups before destructive ops, sanitization policy), session hand-off contract
- Entry points rewired so agents actually hit the standards: `AGENTS.md` rewritten (binding governance rule + trust-tier summary + non-negotiables), `CLAUDE.md` refreshed (binding rule, two-track description, current quick-commands incl. pytest/cst/templates, stale main.py-era content removed), `PROJECT_STARTUP_CONTEXT.md` reduced to a pointer.
- Precedence rule stated everywhere: governance docs win over conflicting instructions unless the user explicitly overrides.

## 2026-07-11 — Phase 35.3 — Physical-layer pages (copper, fiber, RS-485)

**Type:** Content expansion of the communications section (second review's "physical layer before more protocols" guidance)
**Status:** Complete on `feat/phase35-3-physical-layer`.

- **`/communications/copper-ethernet/`** (150 lines) — category ratings, 100BASE-TX vs 1000BASE-T pair usage, channel-length budget, M12 vs RJ45, shield bonding decisions, patch-cord weak link, VFD-cable separation, cable certification vs wiremap testers, PoE overview. Cross-links the intermittent-I/O case study (whose root cause was exactly this failure class).
- **`/communications/fiber-optics/`** (154 lines) — when fiber beats copper, single-mode vs multimode, connector types and TX/RX polarity, optical power budget, cleanliness discipline, SFP compatibility, DOM readings via managed switches, light-source/power-meter vs OTDR, eye-safety note.
- **`/communications/rs485-physical-layer/`** (161 lines) — differential signaling and common-mode rejection, termination placement and value, bias/failsafe resistors, the signal-reference/isolation question, vendor polarity-labeling chaos, stub length and topology, unit loads, oscilloscope practice (healthy vs reflections/rounding/noise/contention waveform signatures). Protocol content deferred to the Modbus RTU page (cross-linked both ways).
- All three at "Review pending" with TIA/ISO-IEC/IEEE reference bodies named; nav (Fundamentals group) + landing page updated.
- Validation: clean build (333 files), zero broken internal links.

**Phase 35.4 backlog (remaining from second review):** interface-neutral diagrams, protocol expansion (EtherCAT, DNP3, IEC 61850, HART, FF, wireless, TSN), sanitized capture library, optional build-time Mermaid pre-render.

## 2026-07-11 — Phase 35.2 — Communications diagnostics depth (second review's "add next" tier)

**Type:** Content expansion of the communications section
**Status:** Complete on `feat/phase35-2-diagnostics-depth`.

- **New page `/communications/wireshark-fundamentals/`** — interface selection (tshark -D, sparklines), promiscuous mode, the switched-network visibility rule, capture-vs-display filter syntax distinction (BPF vs Wireshark, with the capture-broadly-display-narrowly rule), time display + clock-offset practice, name-resolution caution, Conversations/Endpoints, coloring, I/O Graph for dropout hunting, Expert Information, Export Specified Packets, pcapng comments, sanitize-before-sharing.
- **New page `/communications/case-study-intermittent-io/`** — one complete end-to-end investigation (clearly labeled constructed teaching example): vague ticket → precise symptom statement → boundary → physical checks → config checks → switch CRC counters localize to one leg → ring-buffer capture with I/O-graph gap analysis → baseline comparison → evidence chain (motor replacement + missing tray divider + failed cable cert) → verified fix. Demonstrates the 8-step methodology in action.
- **Configuration examples** (illustrative, vendor-defined-values flagged): EtherNet/IP PLC↔VFD parameter table + control-word/scaling example; Modbus TCP "register 40001 vs protocol address 0" worked example with the off-by-one failure modes.
- **Protocol-specific Wireshark workflows** (numbered what-to-look-for sequences) added to EtherNet/IP, Modbus TCP, PROFINET, and OPC UA diagnostics sections.
- **6 network-documentation templates** added to /tools/templates/ (Communications & Networks group): IP address register, switch port schedule, VLAN register, firewall communication matrix, device & firmware inventory, baseline capture log.
- Nav (Diagnostics group) + landing page updated with the two new pages.
- Validation: clean build (330 files), zero broken internal links.

**Still on Phase 35.3 backlog:** physical-layer pages (copper/fiber/RS-485), interface-neutral diagrams, protocol expansion (EtherCAT, DNP3, IEC 61850, HART, FF, wireless, TSN), sanitized capture library, optional build-time Mermaid pre-render.

## 2026-07-11 — Phase 35.1 — Communications fixes from the second external review

**Type:** Corrections + enhancements to the Phase 35 section (review validated claim-by-claim)
**Status:** Complete on `feat/phase35-review-fixes`.

**Validated as FALSE POSITIVE:** "Mermaid diagrams not rendering" — live-browser check confirmed 1 mermaid div → 1 rendered SVG, zero raw code blocks. Same cause as the first review: reviewer scrapes HTML without JS and assumes MkDocs. (Kernel of truth kept on backlog: build-time SVG pre-render would serve no-JS readers/SEO.)

**Real findings fixed:**
- Ethernet-fundamentals opener wrongly claimed all industrial Ethernet protocols ride IP/TCP/UDP — contradicted our own PROFINET page (RT is Layer-2). Corrected per the review's wording, incl. EtherCAT divergence note.
- MAC-address bullet ("burned in… never changes") → locally-administered/override reality; broadcast-domain phrasing.
- Three over-absolute phrasings calibrated: PROFINET name-of-station identity (commissioning identity; IP still matters for IP services), Modbus TCP "simplest" (subjective), EtherNet/IP "dominant" (market claim).
- review-meta include semantics: non-Reviewed pages now show "Last content update" + "Technical validation: Not yet completed" (a page can no longer say both "Review pending" and "Last reviewed"); comms pages' edition field → "exact governing revision not yet recorded" (12 pages); note wording is now context-aware ("jurisdiction" kept on standards pages; spec-revision/firmware/vendor-implementation wording on comms pages).
- Landing page: protocol comparison table ("Which protocol am I looking at?"), Start-by-Task learning paths (4 tasks), IO-Link recategorized under "Smart device interfaces" (point-to-point, not a fieldbus).
- Sidebar nav grouped: Fundamentals / Ethernet Protocols / Serial & Device Networks / Diagnostics (scales for future protocols).
- Packet-capture page: ring-buffer TShark instructions (time- and size-based rotation). Managed-switches page: 10-row port-counter interpretation table with vendor-naming caveat.

**Deferred to Phase 35.2 backlog (review's "add next / expand later"):** Wireshark fundamentals page (capture vs display filter syntax, interface selection, Expert Info...), vendor-neutral configuration examples per protocol (EtherNet/IP assembly/scaling, Modbus 40001-vs-offset-0 worked example), protocol-specific Wireshark workflows, one end-to-end packet-analysis case study, physical-layer pages (copper/fiber/RS-485), comms templates (IP register, switch-port schedule, firewall matrix, capture log), interface-neutral diagrams, then EtherCAT/DNP3/IEC 61850/HART/FF/wireless/TSN, sanitized capture library.

## 2026-07-11 — Phase 36 — Curated manufacturer directory (review roadmap complete)

**Type:** New site feature (review Part C proposal, curated per its own R23 guardrail)
**Status:** Complete on `feat/phase36-manufacturers`.

- `/tools/manufacturers/` + 5 category pages: PLC/PAC & safety controllers (25), VFDs (21), servo/motion incl. CNC (26), SCADA/HMI incl. open source (29), process instrumentation (26) — 127 vendor entries total.
- Data-driven: vendors live in `docs/_data/manufacturers/*.yml` (name/region/families/protocols/notes), extracted from the review's major tables only — additional/regional long lists deliberately skipped for the curated first release; entries the review doesn't support were excluded rather than invented. Pages render tables via Liquid, so future faceted filtering is a data-attribute pass, not a rewrite.
- Framing per the review's own guardrails: "major and notable, not all"; absence-means-nothing scope note; inclusion-is-not-endorsement notice; per-category selection notes (ecosystem lock-in, licensing models, open-source caveats, hazardous-area certificates) cross-linked to standards and lifecycle pages; review blocks at "Partial coverage".
- Tools nav + index updated.
- Validation: clean build (328 files), zero broken links, table row counts match data entries, 145 tests pass.

**With this, all six phases derived from the external site review (32–36 + the Phase 31 IA restructure that preceded it) are complete.** Remaining work is user-driven: review the comms pages (Review pending → Reviewed), content Phase 30.3+, cst data hand-offs.

## 2026-07-11 — Phase 35 — Industrial Communications & Network Diagnostics (first release)

**Type:** New site section (review Part D proposal, first-release scope per its R44)
**Status:** Complete on `feat/phase35-communications`.

- New top-level section `/communications/` (8th nav section, top nav + sidebar): 12 pages + index, each answering the review's six questions (what / where used / network design / configuration / commissioning / diagnostics) plus a common-faults table and related pages.
- Pages: Ethernet fundamentals, managed switches, EtherNet/IP, Modbus TCP, PROFINET, OPC UA, BACnet/IP, Modbus RTU/RS-485, PROFIBUS DP, IO-Link, diagnostics methodology (8-step workflow, Wireshark can/cannot lists), packet-capture methods (workstation vs SPAN vs TAP vs hub, confidentiality warning: never share employer/customer captures).
- Technical guardrails carried through: Modbus-protocol vs RS-485-physical-layer distinction explicit; serial buses documented as NOT Wireshark-capturable with the real toolset instead; filter names carry verify-against-your-version caveats; RFC1918 example addressing only; every page has a review: block at status "Review pending" (honest — awaiting author review against the governing specs).
- Authored by 4 parallel writer agents against a shared page spec; coordinator fixed 2 wrong-slug cross-links at assembly.
- Planned next per the review: EtherCAT, DNP3, IEC 61850, HART, Foundation Fieldbus, wireless.
- Validation: clean build (322 files), zero broken internal links, 12/12 Mermaid diagrams render, review-meta boxes render.

## 2026-07-11 — Phase 34 — Engineering templates + Python toolkit surfaced on the site

**Type:** Site feature (review item R12/R20 templates; "document, don't port" for the cst suite)
**Status:** Complete on `feat/phase34-templates-tools`.

- **19 downloadable templates** at `/tools/templates/` (`docs/assets/templates/`), grouped Design / Safety & Compliance / Commissioning / Documentation:
  - 7 GENERATED by the cst suite from the worked-example I/O list (BOM, wire schedule, legend plates, loop sheet, FAT protocol, design package, I/O list format) via new `tools/generate_site_templates.py` — repeatable, documented in how_to
  - 12 ORIGINAL static templates: controls design basis, standards applicability register, instrument index, control narrative, cause & effect matrix, SRS skeleton, electrical drawing review checklist, alarm rationalization, MOC form, commissioning punch list, test instrument record, cybersecurity asset inventory
  - All marked adapt-before-use; none reproduce standards text or table values
- **`/tools/engineering-toolkit/`** — public documentation of the cst package: install, design principles (citations on every result; licensed values never distributed; one I/O list drives everything), full command table, worked Art. 430 example, limits
- Tools nav + tools index cards updated; templates page cross-links CLI commands for regenerating from a real I/O list
- Validation: clean build (309 files), zero broken links, 145 tests pass

## 2026-07-11 — Phase 33 — Page metadata, dual-lifecycle separation, stage navigation

**Type:** Site trust/navigation features (review items R9/R22, R7, R15)
**Status:** Complete on `feat/phase33-metadata-lifecycle`.

- **Page review information** (R9/R22): new `review:` frontmatter block + `_includes/review-meta.html` box rendered under the breadcrumb on all 12 standards detail pages — edition covered, content status (5-term vocabulary), coverage limits, last-reviewed date, primary-reference reminder. Statuses assigned honestly: IEC 60204-1, IEC 62443, SEMI = Partial coverage (pending depth passes); others Reviewed with coverage caveats (e.g. IEC 60079 "6 of 12+ parts").
- **General vs functional-safety lifecycle** (R7): new `/lifecycle/general/` page (requirements → architecture → design → build → FAT → installation → SAT → handover → maintenance → MOC, with Mermaid flow and a phase-by-phase overlay table mapping the safety stages onto it). Lifecycle index retitled "Functional-Safety Engineering Lifecycle" with a "Two lifecycles, one project" callout — fixes the general-title/safety-content mislabel the review flagged. Added to Lifecycle nav as first child.
- **Stage-strip navigation** (R15): `_data/lifecycle_stages.yml` (14 ordered stages) + `_includes/stage-nav.html` — every lifecycle stage page shows the full numbered journey with a "you are here" marker plus prev/next/all links. URL-matched, zero per-page frontmatter.
- Validation: clean build (307 files), zero broken internal links, stage strip and review boxes verified in built HTML.

## 2026-07-11 — Phase 32 — Trust & language pass (from external site review)

**Type:** Site identity, status vocabulary, and public-language overhaul
**Status:** Complete on `feat/phase32-trust-language`.
**Source:** External review saved at `planning/2026-07-10-external-site-review.md` (4 concatenated proposals: site review, homepage rewrite, manufacturer directory, industrial communications section). Review was written against the stale May build and assumes MkDocs — recommendations validated claim-by-claim; several were already fixed (Phase 29 badges, Phase 31 nav) or false positives (Mermaid "broken" = reviewer scraped without JS).

**User decisions:** identity renamed to **"Control Systems Engineering Field Guide"** (brand: "CS Field Guide"; repo/URL unchanged); 5-term status vocabulary (Reviewed / Partial coverage / Review pending / Needs revalidation / Planned); sequencing Phase 33→34→35→36.

**Changes:**
- Identity: `_config.yml` title/description, topnav brand, homepage hero label + subtitle
- Status vocabulary swept across 33 site pages: Complete→Reviewed, TO VERIFY→Review pending, NOT IN CORPUS→Not yet covered, CORPUS COMPLETE→REVIEWED; "RAG corpus"/"local corpus"→"reference library". Corpus mirror (rag-files) deliberately untouched — corpus keeps internal authoring flags; site is presentation layer only
- Context panel: "Repository Path"→"Source Notes"; content-status blurb de-jargonized. Trust-boundary include rewritten (independent educational reference; new badge legend)
- Homepage: repository tree removed from the power-user block (replaced with source-browser + About links)
- Overconfident-language pass on lifecycle index: "mandatory"→calibrated should-normally-follow wording; independence "required at SIL 2+"→varies-by-standard wording; "non-negotiable principles" softened; `_standards_map.md` internal reference→Standards Finder link
- Applicability caveat added under the Quick Decision table (AHJ, listing, local adoption, hazloc, customer specs, equipment/installation boundary)
- About page fully rewritten: calibrated author bio + non-affiliation statement, honest methodology section (AI-assisted drafting + author curation + promotion checklist), 5-term status table, corrected Known Gaps (old table still claimed functional-safety/SEMI/IEC 60079 were missing — stale by 3+ months), 8-item not-a-substitute-for notice, repo/issues links

**Planned next (from the same review):** Phase 33 page-metadata blocks + general-vs-safety lifecycle separation; Phase 34 templates/tools surface (cst-generated downloads); Phase 35 Industrial Communications section (12-page first release); Phase 36 curated manufacturer directory. Rejected: MkDocs migration, all-protocols-at-once, "all manufacturers" claim.

## 2026-07-11 — Phase 31 — Information-architecture restructure (user-approved)

**Type:** Site IA / navigation re-architecture
**Status:** Complete on `feat/phase31-ia-restructure`.
**Reason:** User feedback: "layout and contents are not really organized." Diagnosis confirmed: top nav and sidebar disagreed (7 grab-bag deep links vs 11 sections), the 14 lifecycle stages were split across Implementation and Verification (the data file even documented the split apologetically), Training vs Fundamentals was one content class with two homes, and stub sections (Troubleshooting 2 pages, Repository 2) held top-level rank.

**New taxonomy (7 intent-based sections, top nav = sidebar):** Home · Fundamentals · Standards · Design · Lifecycle · Industries · Tools.

**Moves (49 pages, all with redirect_from; old section indexes are redirect_to stubs):**
- All lifecycle stages → `/lifecycle/` in chronological order (concept → standards-selection → risk-assessment → SRS → safety-architecture → detailed-design → draft-documentation → safety-wiring → build → installation → pre-commissioning → commissioning → maintenance → MoC); journey page is the section index; commissioning guides (templates/VFD/servo) under `/lifecycle/guides/`
- `/training/nec-application/` → `/fundamentals/nec-application/` (Training section dissolved)
- `/implementation/scenarios/` → `/tools/scenarios/`; `/troubleshooting/` → `/tools/troubleshooting/`
- `/repository/about/` → `/about/` (linked under Tools)

**Mechanics:** migration script (Phase 26 pattern) — git mv, docs-wide ordered link sweep (133 files), then redirect_from insertion; 16 self-redirect conflicts stripped (pages returning to pre-Phase-26 URLs); `lifecycle_stage_urls.yml` now all `/lifecycle/*`; navigation.yml and topnav.html rewritten to the same 7 sections.

**Validation:** clean Jekyll build (306 output files), zero broken internal links, zero built pages referencing old URLs, all 8 old-section redirects verified in `_site`, NEC-course local sidebar renders at its new home.

## Purpose

This file tracks meaningful project-level changes for the current implementation effort.

Use it for:

- project direction changes
- documentation workflow changes
- tooling changes
- architecture and delivery changes

Keep entries concise and oriented to what future work needs to know.

## Change History

## 2026-07-11 — Intake batch digested and planned (Phases 45–48 + AI/ML research track)

**Type:** Planning/recording only — no content built
**Status:** Recorded on `docs/intake-batch-plan`; plan approved by owner in plan mode.

Digested everything in `temp/` and `drawings examples/` (3 explore passes) and recorded the integration plan in `governance/ROADMAP.md`:

- **Phase 45 (do first, safety-significant):** standards accuracy pass from a third external review (`temp/standards_check.md`). Confirmed-real catches include the IEC 60204-1 edition/scope/Clause-18/E-stop-category errors, the ISO 12100↔13849-1 risk-graph misattribution, CE-marking wording, 62061/62443 edition issues, and a residual raw "Complete" status leak in plain-text table cells that the Phase 32 sweep missed. Every edition claim gets publisher verification before adoption. **Triage decision recorded: the review's proposed replacement status vocabulary is REJECTED — it conflicts with the governance 5-term vocabulary (CONTENT_STANDARDS §3); the leak it found is real, the fix uses OUR terms.** Expansion wishlist + 3-level page model → backlog, not scheduled.
- **Phase 46:** wire-color-coding gallery guide (17 ready diagrams) + the worked design-package poster.
- **Phase 47:** PLC software expansion — 4 new pages (ladder fundamentals, algorithms/staging, PackML/ISA-88/95, vendor programming architectures) from `temp/plc_software.md` via the knowledge-intake loop; utm-stripping + citation re-verification required.
- **Phase 48:** PLC/IPC hardware families page + a data-driven vendor-documentation index (~130 official links from the xlsx) under `/tools/manufacturers/`.
- **AI/ML for Control Systems** recorded as a deferred research track honoring its own do-not-build-yet status; promotion criteria written into ROADMAP.

Sources stay in place until each phase executes (relocations are written into each phase's steps). No site content, corpus content, or temp/ moves in this change.



## 2026-07-11 — Phase 44 — Communications Expansion (EtherCAT, HART, DNP3, IEC 61850)

**Type:** Content — communications section expansion (35.4 backlog, first batch)
**Status:** Complete on `feat/phase44-comms-expansion`.

- 4 new protocol pages using the established six-question comms template:
  - EtherCAT (Ethernet Protocols group) — processing-on-the-fly, distributed clocks, ESI files, INIT→...→OP state machine, working-counter health indicator; explicitly not switched Ethernet
  - HART (smart-device group) — FSK digital on the 4–20 mA loop, point-to-point vs multidrop, loop-resistance requirement, DD/EDD; "use a HART modem, not Wireshark" — links the 4–20 mA wiring + analog-fault troubleshooting pages
  - DNP3 (new Utility & Substation group) — master/outstation, time-stamped events, report-by-exception, point-map-as-contract; serial-capture caveat
  - IEC 61850 (Utility & Substation) — data model + GOOSE (Layer-2, non-routable, PROFINET-RT parallel) + Sampled Values, SCL files, PTP time sync; mms/goose/sv filters
- Coordinator normalized 27 links from `{{ site.baseurl }}` to the governance-standard `relative_url` form before merge.
- Landing page + nav updated (EtherCAT into Ethernet, HART into serial/device, new Utility & Substation group). Communications section now 22 protocol/diagnostics pages.
- All Review pending; validation: clean build (363 files), zero broken links, boundary baseline unchanged, 145 tests.

**This completes the Phase 42-44 arc and the roadmap's named build phases.** Remaining are standing threads (author reviews, Phase 30.3+ standards depth, cst data hand-offs, SVG diagrams) and future comms items (Foundation Fieldbus, wireless, TSN, capture library).



## 2026-07-11 — Phase 43 — IEC 61131-3 / PLC Software

**Type:** Content — new PLC-software section, closes the longest-standing corpus gap
**Status:** Complete on `feat/phase43-iec61131`.

- New `/fundamentals/plc-software/` section (4 pages + index) + corpus `training_modules/plc_software/` module (4 notes):
  - Languages Overview (184) — the five IEC 61131-3 languages (LD/FBD/ST/SFC/IL, IL deprecation noted), when each fits, comparison table, SFC step-transition diagram
  - Program Structure (159) — POUs (Program/FB/Function), tasks/scan model (standard vs vendor reality), variable scope + globals-as-trap, links cst tag tooling
  - State Machines (195) — explicit-state-machine argument, three implementations (SFC / ST CASE / Ladder), fault-recovery, links the existing machine-state-model page
  - Safety Application Patterns (174) — framed patterns-not-PL/SIL: safety-rated controller + certified function blocks, safety program kept separate/traceable, anti-patterns; links ISO 13849-1/IEC 62061/IEC 61508, SRS, safety-circuit wiring
- IEC 61131-3 paraphrased at concept level, illustrative ST snippets only, no reproduced grammar tables. Vendor tools as examples with consult-your-platform refrain.
- Added to Fundamentals landing + nav. Mirror synced.
- All Review pending; validation: clean build (359 files), zero broken links, boundary baseline unchanged, 145 tests.



## 2026-07-11 — Phase 42 — Troubleshooting Engine

**Type:** Content — new troubleshooting decision-tree genre + corpus module populated
**Status:** Complete on `feat/phase42-troubleshooting`.

- 4 symptom decision-tree pages under `/tools/troubleshooting/`, each with a Mermaid decision flowchart, routing INTO the wiring guides and comms diagnostics rather than duplicating them:
  - VFD Faults (230) — by fault category (overvoltage/overcurrent/overtemp/ground-fault/no-fault-but-won't-run); "consult your drive's fault-code list" refrain, no vendor code tables reproduced
  - Motor Won't Start (206) — branches from "does the contactor pull in?" into control-circuit vs power-side vs mechanical
  - Analog Signal Faults (230) — 4–20 mA / 0–10 V by reading symptom (zero/full-scale/noisy/offset), bisect-the-loop method
  - Communication Dropouts (202) — triage front-end that routes into the Communications 8-step methodology (doesn't restate it)
- Corpus `troubleshooting_engine/` module (previously empty per the known-gaps list) now populated: 4 notes across new `motion_drives/`, `analog_io/`, `networks/` dirs. Mirror synced (rag tree 6→7 top-level entries).
- Troubleshooting landing page upgraded to a symptom card grid; nav extended.
- All Review pending; validation: clean build (354 files), zero broken links, boundary baseline unchanged, 145 tests.



## 2026-07-11 — Phase 41 — Wiring Guides Wave 4 (Infrastructure & Safety) — wiring program complete

**Type:** Content (wiring-guides program, wave 4 — final wave)
**Status:** Complete on `feat/phase41-wave4-infra`.

- 5 site guides + 5 corpus notes, completing the 16-guide wiring program:
  - Communication Cable Installation (257) — install-practice companion to the Communications physical-layer pages: routing/segregation from motor cables, connectors/termination, shield-at-gland; references the intermittent-I/O case study
  - Control Power Distribution (242) — CPT vs 24 V PSU, sizing for inrush not holding VA (the classic brownout), primary+secondary and per-branch fusing, grounded-control-circuit bonding; cites cst transformer
  - Safety Circuit Wiring (327) — framed as wiring-not-design (architecture comes from the SRS/risk assessment): dual-channel e-stop/interlock, EDM feedback, monitored reset, redundant contactors/STO; per-channel functional test
  - Motor Starters (261) — DOL/reversing/star-delta: the Art. 430 chain (OCPD protects wiring, overload protects motor), seal-in rung, reversing interlock (electrical+mechanical), SCCR via UL 508A; cites cst motor-branch
  - RTD & Thermocouple (249) — 2/3/4-wire RTD lead compensation, matched TC extension wire + polarity + cold-junction, single-end shielding, grounded vs ungrounded junction; IEC 60751/60584 at category level
- Coordinator fixes at assembly: reworded a "mandatory" voice flag in the RTD/TC guide; fixed one broken link (/lifecycle/guides/ index doesn't exist -> /lifecycle/commissioning/).
- Section index gains an Infrastructure & Safety card grid (Planned-Guides table removed); nav lists all 16 guides; mirror synced.
- All Review pending; validation: clean build (350 files), zero broken links, boundary baseline unchanged, 145 tests pass.

**The Wiring & Installation Guides program (Phases 38-41) is complete: 16 guides across Foundations, Controllers & I/O, Motion & Feedback, and Infrastructure & Safety.**



## 2026-07-11 — Phase 40 — Wiring Guides Wave 3 (Motion & Feedback)

**Type:** Content (wiring-guides program, wave 3)
**Status:** Complete on `feat/phase40-wave3-motion`.

- Servo Drive Wiring (321) — builds on the VFD guide for power/shielding/reflected-wave, focuses on the closed-loop differences: feedback cable segregation, dual-channel STO (not a disconnect, still LOTO the mains), holding brake (holds != stops, release/enable sequencing, coil suppression). Longer than the nominal ceiling by design — a servo axis carries feedback+STO+brake subsystems a VFD lacks, all safety-relevant.
- Encoder Wiring (267) — differential vs single-ended output matching, twisted-pair channel-complement grouping, 5 V supply drop over distance, counts-jump-under-motor-load fault, one-end vs both-ends shield contrast; differential theory deferred to the RS-485 page, scaling math to the cst encoder tool.
- 2 corpus notes; section index gains a Motion & Feedback card grid; nav extended; mirror synced.
- All Review pending; validation: clean build (345 files), zero broken links, boundary baseline unchanged, 145 tests pass.



## 2026-07-11 — Phase 39 — Wiring Guides Wave 2 (Controllers & I/O)

**Type:** Content (wiring-guides program, wave 2)
**Status:** Complete on `feat/phase39-wave2-io`.

- 5 site guides at `docs/design/wiring/` + 5 corpus notes in `wiring_practices/`:
  - PLC Wiring (263) — sinking vs sourcing DI, relay/transistor DO, shared-vs-isolated common sneak paths, freewheeling diodes; NFPA 79 Ch. 6/7/9/16 basis incl. wire-color convention
  - Remote I/O Stations (226) — separate logic/actuator 24 V rails, feeder voltage-drop browning out the coupler (cst voltage-drop), inter-panel ground loops
  - Industrial PCs (261) — UPS/holdup vs storage corruption, PE mandatory on a DC device, port segregation, clean-side placement
  - 4–20 mA Current Loops (260) — 2/3/4-wire transmitters, compliance/burden budget, active-vs-passive double-powering trap, one-point grounding, isolators; contrasts the analog one-end shield rule against the VFD both-ends rule
  - 0–10 V Signals (225) — companion to 4–20 mA; shared-reference weakness, return-conductor voltage-divider distance limit, no broken-wire detection
- Section index promotes Wave 2 to a Controllers & I/O card grid; nav group extended. Mirror synced.
- All Review pending; validation: clean build (343 files), zero broken links, boundary baseline unchanged, 145 tests pass.



## 2026-07-11 — Tools Suite Phase 4 — PLC utilities, diagnostics, docgen (roadmap complete)

**Type:** Feature (cst package expansion — final planned phase)
**Status:** Complete on `feat/cst-phase4`.

- `cst.plc.tag_db` — tag model + IEC 61131-3 (Cl. 6.1) identifier validation, case-insensitive duplicate detection, `tags_from_io_list` bridge (sanitizes field tags like `XV-101-ZSO` → `XV_101_ZSO`).
- `cst.plc.address_map` — Modbus register maps per the Modbus Application Protocol data model: coils/discrete-inputs/input-registers/holding-registers, 2-register REAL/DINT with word-order flag, writable-set override.
- `cst.plc.comms` — pycomm3 LogixDriver wrappers (batch read, FAT read-back verify) as optional extra `plc`; writes deliberately not wrapped. Degrades with a clear install message.
- `cst.diagnostics.sbm` — SBM-style (Wegerich) kernel autoassociative anomaly detection, stdlib-only: z-scored memory matrix (envelope + spaced selection), Gaussian-kernel reconstruction, per-sensor residual localization; score = max |z-residual|, thresholds set from a normal baseline (documented).
- `cst.diagnostics.saleae` — Logic 2 digital-export parser (initial state ≠ edge), pulse stats (freq/duty/width extremes), glitch finder, x4 quadrature decode with direction reversals.
- `cst.docgen.design_package` — DesignPackage assembler: I/O summary + BOM + wire schedule + nameplate + cited CalcResults → single markdown with TOC.
- 5 new CLI subcommands: `tags-from-io`, `modbus-map`, `saleae`, `sbm`, `design-package`.
- Tests: 145 passing (30 new). Two real bugs caught and fixed during test-first work: quadrature initial-level derivation, and SBM scoring diluted by RMS (now max-residual with baseline-relative thresholds).

**All four Tools Suite phases now complete.** Remaining user-dependent items: licensed table values for design use (Phase 2), real project I/O list for column presets (Phase 3), real historian/Saleae data for SBM/decode tuning (Phase 4), content Phase 30.3+.

## 2026-07-11 — Tools Suite Phase 3 — panel design pipeline + commissioning generators

**Type:** Feature (cst package expansion)
**Status:** Complete on `feat/cst-phase3`.

- `cst.panel.io_list` — canonical I/O-list CSV model (tag/description/io_type/signal/address...), tolerant header mapping via `column_map`, validation (duplicate tags, address conflicts, unknown types).
- `cst.panel.bom` — structural BOM: module counts from channel totals + spare fraction (default 20 %), terminal blocks per point by signal class, shield terminals, optional interposing relays. Generic descriptions; part numbers deliberately left to the user.
- `cst.panel.wire_schedule` — tag-suffix wire numbers, sequential terminal assignment, conductor sets + default colors per NFPA 79 Ch. 16 practice (parameterized).
- `cst.panel.nameplates` — legend-plate engraving list (flags over-length descriptions) + panel nameplate content per NFPA 79 Ch. 19 / UL 508A marking items.
- `cst.commissioning.loop_sheets` — markdown loop test sheet per point: ISA-style 5-point analog checks, actuate/verify discrete checks, RTD/TC substitution checks, as-found/as-left, sign-off.
- `cst.commissioning.fat_sat` — FAT/SAT protocol skeleton generated from the I/O list summary.
- `data/examples/io_list_example.csv` — 13-point worked example driving docs, demos, and tests.
- 6 new CLI subcommands: `io-check`, `bom`, `wire-schedule`, `legend`, `loop-sheets`, `fat`.
- Tests: 115 passing (18 new).

**Note:** default CSV format is the suite's own; a real (scrubbed) project I/O list from the user would let `column_map` presets be added for their exports.

## 2026-07-11 — Tools Suite Phase 2 — NEC/UL calculators

**Type:** Feature (cst package expansion)
**Status:** Complete on `feat/cst-phase2`.

- `cst.calc.ampacity` — NEC 310.15: base ampacity from user table, ambient correction via the 310.15(B) equation, bundle adjustment per Table 310.15(C)(1).
- `cst.calc.motor_branch` — full Art. 430 chain: table FLC → conductors at 125 % (430.22) → OCPD max per Table 430.52(C)(1) with next-size-up (240.6(A)) → overload per 430.32(A)(1) from nameplate FLA.
- `cst.calc.transformer` — FLA math + OCPD limits per Table 450.3(B) (primary-only and primary+secondary schemes, Note 1 next-size-up only where permitted).
- `cst.calc.sccr` — UL 508A SB4 weakest-link panel SCCR with NEC 409.22 available-fault check; never infers series ratings.
- `cst.calc.short_circuit` — infinite-bus transformer fault current + Bussmann point-to-point attenuation (C-value user-supplied; not embedded).
- Table loader now supports `data/standards_tables/samples/` fallback: clearly-marked SAMPLE files (common NEC 310.16 Cu-75°C and 430.250 460 V values) let everything run/test out of the box; results carry a SAMPLE warning; user files always win; `allow_sample=False` for design use.
- 5 new CLI subcommands: `ampacity`, `motor-branch`, `transformer`, `sccr`, `fault-current`.
- Tests: 97 passing (32 new), all doctests green.

**Boundary note:** rule multipliers/percentages implemented in code with clause citations (same class of content as the corpus's worked examples); bulk table values (310.16, 430.250, Bussmann C) remain user-supplied per the licensing boundary. SAMPLE values are flagged for verification against a licensed copy.

## 2026-07-10 — Pre-public sanitization pass (user-approved)

**Type:** Repository sanitization + second history rewrite
**Reason:** Repo is going public. Full audit (secrets/PII/copyright, tree + history) found no credentials, no client/employer references, and a clean RAG corpus — but flagged verbatim third-party video transcripts, a backup tarball leaking the restricted tree, and personal learning material.

**Removed from tree AND purged from history** (copies archived in `~/Dev/_archive/repo-sanitize-removed-20260710/`; pre-sanitize mirror at `~/Dev/_archive/CST-pre-sanitize-backup-20260710.git`):
- 8 verbatim YouTube/webinar transcripts + 1 affiliate-links copy under `control-standards/work/design/` (Ryan Jackson 2026 NEC, Electrical Code Coach paid exam prep, NEC livestream, Engineering Mindset motors, Solid State Workshop circuit analysis, Praxis NFPA 79/70E webinar, temp links, mini_machine v2 status chat dump)
- History-only ghosts: `check_this.md`, the Mike Holt-derived grounding note
- `planning/backups/*.tgz` (pre-reorg snapshot containing drafts_DO_NOT_READ + business-IP module skeletons), `planning/manifests/` (leaked restricted filenames)
- Personal learning/AI-chat material: `planning/RUST/`, `planning/SCADA/`, `planning/motors/`, `safety_software_stack.md`, `ground_earth_visual.md`, `semi_facility/phase_20260413.md`
- `STRUCTURE_SUMMARY.md` history (old versions listed restricted filenames; regenerated clean)

**Tree-only fixes:**
- 37 derived-note files: links to removed raw transcripts converted to plain-text notes (derived paraphrased summaries were audited as fine and KEPT)
- `ul508_spacing.md`: 13 ephemeral images.openai.com URLs stripped
- All `/Users/kyawminthu/...` absolute paths scrubbed from 34 tracked files (repo-relative or `~` forms)
- `.claude/settings.json`: legacy `~/Dev/tools` permission removed
- `project_automator.py`: `restricted/`, `drafts_DO_NOT_READ/`, `archive/` excluded from the generated structure summary
- Commit author/committer email rewritten to the GitHub noreply address across all history

**Audited and cleared (no action):** RAG corpus paraphrasing (no reproduced NEC/UL tables), semi_facility (follows its public-content rules), GA4 ID, docs/ content, secrets/keys (zero hits tree + history), PII (only fictional examples), internal hostnames/IPs (none), employer/client names (none).

## 2026-07-10 — Git history rewrite: Udemy course purged from repo and remote

**Type:** Repository history rewrite (user-approved)
**Status:** Complete; rewritten `master` force-pushed to `origin`.
**Reason:** `planning/Python/` (168 MB third-party "Complete Python 3 Bootcamp" course, 1,141 files) was tracked since early history and present on the public GitHub remote — copyright exposure and 165 MB of pointless `.git` weight.

**What was done:**
- Full mirror backup first: `~/Dev/_archive/Control-System-Tools-pre-rewrite-backup.git` (169 MB, contains pre-rewrite history).
- Course files moved out of the repo to `~/Dev/_archive/udemy-python-bootcamp/`.
- The stale `phase-19-nav-refactor` worktree blocked filter-repo; its uncommitted changes were committed onto the `phase-19-nav-refactor` branch (and copied to `~/Dev/_archive/phase19-worktree-uncommitted/`), then the worktree was removed.
- `git filter-repo --invert-paths --path planning/Python` rewrote all 328 commits. `.git`: 171 MB → 5.9 MB. Zero refs touch `planning/Python` afterwards; 65/65 tests pass.
- Rewritten `master` force-pushed; 3 stale fully-merged remote branches deleted (`feat/control-systems-training-expansion`, `feat/phase22-semiconductor-facility-reference`, `feat/ul508a-content-depth`). Remote now carries only `master`.

**Consequences to know:**
- **All commit SHAs changed.** Any existing clone of this repo must be re-cloned (or hard-reset to the new history). Old SHAs in notes/links no longer resolve.
- GitHub may retain pre-rewrite objects in caches/unreachable storage for a while; a GitHub Support request can force-purge if needed.
- `planning/Python/` remains in `.gitignore` as a guard.

## 2026-07-10 — Tools Suite Phases 0–1 — repo hygiene + `cst` Python package

**Type:** New project track (Python tools suite) + repository hygiene
**Status:** Complete on `feat/cst-suite` (Phase 0: commit c027d72; Phase 1: follow-up commit).
**Reason:** Full repo audit (2026-07-10) found zero engineering-calculation code despite the "Control System Tools" name, plus active hygiene defects. User approved a 4-phase plan to grow the repo into a comprehensive, portfolio-grade engineering tools suite alongside the content site.

**Phase 0 changes (hygiene):**
- Untracked `planning/Python/` (168 MB Udemy course, 1,141 files — 54 % of tracked files; copyright exposure). History rewrite deferred pending user decision.
- `tools/project_automator.py` IGNORE_DIRS fixed (was indexing `.venv`/`docs/vendor`/`docs/_site`) — STRUCTURE_SUMMARY.md 600 KB → 99 KB.
- Fixed the 2 pre-existing broken homepage links; excluded `docs/plans/` + `docs/superpowers/` from the published site.
- Deleted 0-byte `generate_rag_index.py` and retired `_phase26_*` scripts; un-hardcoded `generate_standards_overview.py` root path.
- Re-synced the RAG→site mirror (5 stale BLDC/PMSM files).

**Phase 1 changes (package):**
- New installable package `src/cst/` with console script `cst` (hatchling, `uv sync`).
- `cst.common`: units (ASTM B258 AWG), Citation/CalcResult framework (every result carries standard references + assumptions), loader for user-supplied licensed table JSON.
- Calculators: `cst.calc.voltage_drop` (NEC K-factor method + minimum-wire-size search), `cst.motion.encoder` (counts↔units↔RPM scaling), `cst.calc.enclosure_thermal` (IEC/TR 60890-style temp rise + fan sizing).
- `data/standards_tables/`: committed schemas, gitignored values — licensed table data (NEC 310.16, 430.250, …) is supplied by the user, never committed.
- 50 new tests in `tests/cst/` (65 total pass); pytest declared as dev dependency; redundant `pypdf2` dropped.

**Architecture decision:** calculation logic open/committed, licensed numeric table values local-only — same copyright boundary as the RAG corpus. Roadmap: Phase 2 NEC/UL data-dependent calculators (blocked on user table data), Phase 3 panel/commissioning pipeline, Phase 4 PLC/diagnostics/docgen.

## 2026-05-06 — Phase 30.2 COMPLETE — IEC 60079 depth pass

**Type:** Site content / standards detail page upgrade
**Status:** Complete on `feat/phase30-standards-depth-pass`.
**Reason:** IEC 60079 detail page audited at 3/8 on the ISO 13849-1 template floor — missing Quick Start, Worked Example, Common Mistakes, Practical Checklist, Lifecycle Application; protection-method table did not distinguish corpus-backed parts from gap-flagged ones. Brought page up to floor compliance.

**Changes:**
- `docs/standards/hazardous-area/iec-60079/index.md` — 123 → 364 lines.
  - **Added** Quick Start (5 bullets), Corpus Coverage table (6 corpus parts + 6 gap-flagged parts), Per-Part Depth (60079-0 / -1 / -10-1 / -11 / -14 / -17), Worked Example (4–20 mA IS loop on ethylene Zone 1 with full entity-parameter math), Common Mistakes (6 numbered), Practical Checklist (Area classification / Equipment / Installation / Inspection groups), Lifecycle Application table.
  - **Expanded** the existing Equipment Marking System tables (EPL→Zone, gas groups, T-codes) and added the 50 °C autoignition margin rule.
  - **Replaced** the brief NEC Article 500–505 note with a fuller mapping table linked to the IEC 60079 ↔ NEC 500–505 crosswalk page.
  - **Kept** the existing page header, hazardous-area family link, and Related Standards block.

**Plan vs RAG correction (recurrence).** The Phase 30.2 plan called for per-part depth on Ex e (60079-7) and Ex p (60079-2), but neither part is in the RAG corpus. Verified against `_index.yaml` before drafting (lesson learned in 30.1 successfully applied). Per-part depth covers the 6 corpus-backed parts only; Ex e, Ex p, and other family members appear in the Corpus Coverage gap-flag table. Plan's Common Mistake #6 (Ex e motor thermal protection) replaced with a corpus-backed mistake — field-modifying an Ex enclosure.

**Validation:**
- Jekyll build: clean (1.19 s).
- All 12 outgoing internal links from the rewritten page resolve.
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.
- One external URL (`https://www.iecex.com/`) generated by mistake and removed before commit per the rule against generating external URLs.

**Corpus quality:** unlike the NFPA 79 corpus in Phase 30.1, the IEC 60079 corpus is clean — no stray LLM prompts, no empty placeholders, consistent front-matter. Nothing to flag.

## 2026-05-06 — Phase 30.1 COMPLETE — NFPA 79 depth pass

**Type:** Site content / standards detail page upgrade
**Status:** Complete on `feat/phase30-standards-depth-pass`.
**Reason:** NFPA 79 detail page audited at 3/8 on the ISO 13849-1 template floor — missing Quick Start, Worked Example, Common Mistakes, Practical Checklist; chapter table had wrong titles. Brought page up to floor compliance.

**Changes:**
- `docs/standards/us-electrical/nfpa-79/index.md` — 110 → 246 lines.
  - **Added** Quick Start (5 bullets), Per-Chapter Depth (9 chapters: 4, 5, 6, 7, 8, 9, 15, 16, 19), Worked Example (UL-listed packaging machine), Common Mistakes (6 numbered), Practical Checklist (Design / Build / Ship & Install), Lifecycle Application table.
  - **Replaced** the previous "Key Chapters" table (which had Ch 6/7 swapped and used "Protection of equipment" — an IEC 60204-1 phrase, not an NFPA 79 chapter title) with a corrected 14-row Chapter Reference table.
  - **Replaced** the thin "Lifecycle Stages" section with a Lifecycle Application table linking to all six site lifecycle-stage pages.
  - **Kept** the page header, Standard Overview table, "Relationship to NEC and UL 508A" diagram, "PL / SIL Relevance" cross-reference, and Related Standards block.

**Plan vs RAG correction.** The Phase 30.1 plan as drafted on 2026-04-29 assumed a different NFPA 79 chapter layout than NFPA 79:2024 actually uses. Mapping verified against `control-standards/rag/standards_intelligence/us/nfpa79/_index.yaml` and chapter front-matter. Page drafted against the verified corpus mapping, not the stale plan. See `project_state/project_state.md` for the per-chapter delta table. Same verification step is queued ahead of 30.2.

**Validation:**
- Jekyll build: clean (1.351 s, 268 HTML files).
- All 13 outgoing links from the rewritten page resolve. Two pre-existing broken links elsewhere on the site (homepage → `/industries/food-beverage/` and `/industries/offshore-marine/`) are not Phase 30.1 regressions; flagged for a separate hygiene task.
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.

**Corpus hygiene findings (out of scope for Phase 30, queued separately).** The NFPA 79 RAG files contain stray LLM prompts at chapter ends (Ch 6, 7, 8, 15, 16, 17, 18), empty placeholder values for numerical ranges (Ch 4 temperatures, Ch 17 bend-radius), an internal-numbering bug (Ch 6 says "intent of Chapter 7"), and a suspect "Table 7.2.7" cite in Ch 15. These do not affect site content because the rewrite only used independently verifiable facts.

## 2026-04-29 — Phase 30 plan recorded — Standards Depth Pass (planning only, no code)

**Type:** Planning / project_state authored
**Status:** Plan recorded; implementation not started.
**Reason:** Live-site audit revealed standards detail pages all carry "Complete" badges but actual depth varies ~3×. ISO 13849-1 and IEC 62061 set an 8-section template (Quick Start, per-clause depth, Worked Example, Common Mistakes, Practical Checklist, Lifecycle Application, plus Standard Overview and Related Standards). NFPA 79, IEC 60079, IEC 60204-1, and SEMI S2/S8/S14 are at 3/8 or below. Family overview pages are list-only when they should help a user choose between members.

**What was added:**
- New "## Phase 30 — Standards Depth Pass (Planned)" section in `project_state/project_state.md` between Current Direction and the Phase 29.4 entry.
- Header `Next Phase` line in `project_state.md` updated to point to Phase 30 with the audit summary.
- Phase 30 plan contents:
  - Audit findings table (per-page template-completeness scores).
  - Family-page audit table.
  - Eight sub-phases (30.1 through 30.8) with file paths, RAG sources, exact section additions per page, worked-example specifications with concrete numbers (e.g. NFPA 79 packaging machine, IEC 60079 ethylene-tank IS loop with entity-parameter math, IEC 60204-1 CNC machine, SEMI PVD tool, IEC 62443 networked safety PLC), and Common Mistakes specifications.
  - Cross-cutting principles (RAG is authoritative; worked examples must be concrete; no new corpus claims; build clean every sub-phase).
  - Recommended sequencing.
  - Sub-phase validation checklist.
  - Out-of-scope statement.
  - Branch and commit discipline.

**No code changes in this entry.** Implementation begins when Phase 30.1 (NFPA 79) starts on `feat/phase30-standards-depth-pass`.

## 2026-04-29 — Terminology pass: "confidential" → "proprietary" / "sensitive"

**Type:** Editorial / public-content tone
**Status:** Complete
**Reason:** "Confidential" framing in the BLDC pages made the public site sound like it was hiding restricted material. Replaced with engineering-accurate words. IEC 62443 standard terminology kept (with a clarifying note added).

**Renamed:**

- `docs/fundamentals/motors/bldc-reference/index.md` — three section headings + body references: "confidential BLDC system" → "proprietary BLDC system", "confidential system" → "proprietary system", "confidential-system worksheet" → "proprietary-system worksheet".
- `control-standards/rag/training_modules/electrical_machines/bldc_motor_reference.md` — same three replacements (RAG source kept in sync with site).
- `planning/motors/bldc.md` — same three replacements + the opening line ("right way to approach a confidential system" → "right way to approach a proprietary system").
- `planning/semi_facility/governance/public_content_rules.md` — "confidential alarm lists" → "sensitive alarm lists" in the Not-allowed list.

**Kept (with terminology footnote added):**

IEC 62443 cybersecurity docs use "Data Confidentiality" / "Confidentiality" as the literal CIA-triad security-property name from the standard (FR 4). Renaming would misquote the standard. Per user direction (Option B), the term is kept and a one-line note has been added to each file:

> *Terminology: "Confidentiality" here is the IEC 62443 security property (the C in C-I-A) — protection from unauthorized disclosure, not a content-classification label.*

Files with the note (7 total — public summary plus 3 RAG-file mirror pairs):

- `docs/standards/cybersecurity/iec-62443/index.md` — after the FR table.
- `docs/assets/rag-files/.../IEC62443_3_3__system_security_requirements.md` + `control-standards/rag/.../IEC62443_3_3...md` — after the FR table.
- `docs/assets/rag-files/.../IEC62443_2_1__security_management.md` + `control-standards/rag/.../IEC62443_2_1...md` — after the IT-vs-IACS comparison table.
- `docs/assets/rag-files/.../IEC62443_4_2__component_requirements.md` + `control-standards/rag/.../IEC62443_4_2...md` — directly under the "Common Findings" heading.

**Kept (validator):**

- `tools/validate_ai_boundaries.py:22` — `"CONFIDENTIAL"` is a forbidden-keyword string the validator scans for. Removing it would weaken the rule that prevents this very issue.

**Validation:** `jekyll build` clean, 1.078 s. No structural changes.

## 2026-04-29 — Phase 29.4 complete: Standards Finder faceted filter (Sketch B)

**Type:** UX enhancement / progressive enhancement
**Status:** Complete
**Scope:** Faceted-filter chip UI added to the Standards Finder page; vanilla-JS filter logic; no new content.

**Files touched:**

- `docs/tools/standards-finder/index.md` — added `.finder-filters` block with 2 chip rows (Market: US/Global/Industry; What you're building: Machinery, Process, Hazloc, Cyber, Industry overlay), result-count display, Clear button, empty-state message. Tagged each `.scenario-card` with `data-finder-region` and `data-finder-domain` (multi-value where honest, e.g. Networked Safety PLC = `machinery cyber`). Tagged each grouping `<section>` with `data-finder-section` so empty sections collapse on filter. Added `id="escape-hatch"` to the closing "None of these fit?" section so the empty-state message can deep-link to it.
- `docs/assets/css/main.css` — new `.finder-filters` block (~95 lines): chip pill styling, active state via `aria-pressed="true"`, dashed-divider meta row with count + clear, dark-mode parity via existing color tokens, `.is-hidden` helper for cards/sections.
- `docs/assets/js/main.js` — appended ~85-line IIFE. No-ops if `[data-finder-filters]` not present. Filter logic: OR within a facet row, AND across rows. Updates `aria-pressed` on chips, hides non-matching cards via `.is-hidden`, hides any section whose cards are all hidden, updates result-count text, toggles Clear button visibility, surfaces an empty-state message when zero match.

**Facet tagging (region / domain):**

- 01 US ICP — `us` / `machinery`
- 02 Global Machine — `us global` / `machinery`
- 03 Process Skid — `us global` / `process`
- 04 Networked Safety PLC — `us global` / `machinery cyber`
- 05 Semi Equipment — `industry` / `industry-overlay`
- 06 Practical Machine Safety — `us global` / `machinery`
- 07 O&G Onshore Skid — `us` / `process hazloc`
- 08 Semi Fab Tool — `industry` / `industry-overlay machinery`
- 09 Offshore Platform — `industry` / `process hazloc industry-overlay`

**Progressive enhancement:** the existing `.finder-jump` anchor strip is kept underneath the filter block. No-JS readers still get the original scenario-card listing with section anchors — the filter is additive, not load-bearing.

**No URL persistence in this phase.** Deferred to a possible Phase 29.4.1 if the personal-use case actually demands shareable filter URLs.

**Validation:**

- `jekyll build`: clean, 1.261 s.
- `_site/tools/standards-finder/index.html`: 9 cards carry `data-finder-region`, 8 `.finder-chip` buttons (3 region + 5 domain), 5 `data-finder-section` markers, 1 `.finder-empty` element.
- `validate_ai_boundaries.py`: 2 pre-existing failures (UPW_water_skid_scenario.md, plus one other) — same baseline as Phase 29.3, unrelated.
- `validate_reorg.sh all`: 48/50 baseline.

**What this phase did not change:**

- No scenario content rewritten or added.
- No deprecation of the comparison crosswalks page.
- No edits to other Tools pages, sidebar, or the homepage.

## 2026-04-27 — Phase 29.3 complete: Standards Finder page (scenario-card entry)

**Type:** Information architecture / new page
**Status:** Complete
**Scope:** New page at `/tools/standards-finder/` + homepage re-routes + nav entry

The Phase 29 homepage promised a "Find applicable standards" entry point but routed both the hero CTA and the Start Here card to `/tools/crosswalks/` — a comparison tool, not a finder. Phase 29.3 ships the actual finder.

New page (`docs/tools/standards-finder/index.md`):
- Sketch C from the IA brainstorm — scenario-card entry, no JS, no faceted filter.
- `.finder-jump` anchor-chip strip + 5 grouped sections covering the 9 existing engineering scenarios reused from `docs/implementation/scenarios/`.
- Sections: US-market machines & panels (Scen. 01, 06) · Global / EU machines (02) · Process safety SIS/ESD (03, 07) · Networked & cyber-physical safety (04) · Industry-specific stacks (05, 08, 09).
- Closing escape-hatch routes to crosswalks (comparison) and the standards atlas (browse) so users who don't match a scenario don't dead-end.

CSS (`docs/assets/css/main.css`):
- `.finder-jump` block — bordered horizontal anchor strip, theme-token only, no overrides needed.

Re-routes (`docs/index.md`):
- Hero CTA "Find applicable standards" → `/tools/standards-finder/`.
- Start Here card "I need applicable standards" → `/tools/standards-finder/` + copy refreshed to match the Finder's scenario-first framing.

Navigation (`docs/_data/navigation.yml`):
- Added `Standards Finder` as the first child under Tools (above RAG Browser).

Validated: clean Jekyll build (1.078 s), 9 scenario cards + 5 jump anchors render on the Finder, both homepage entry points re-route correctly, validators show only baseline failures.

## 2026-04-27 — Phase 29.2 complete: Extend local sidebar pilot to 3 more topic groups

**Type:** Information architecture
**Status:** Complete
**Scope:** Pure data change in `docs/_data/training_catalog.yml`

The Phase 28 local-sidebar pilot covered only `electrical-machines` (Motors). Phase 29.2 extends it to three more groups, going from 1/4 → 4/4 of the topic groups in the catalog.

Data (`docs/_data/training_catalog.yml`):
- Added `sidebar_buckets:` ordering arrays to `fundamentals`, `control-systems`, and `nec-application` topic_groups.
- Tagged all 34 modules in those groups with `sidebar_bucket:` and gave 32 of them a `nav_title:` for sidebar-friendly labels.

Bucket taxonomies:
- **Electrical Fundamentals** (9 modules): Circuit Analysis · Components & Devices · Practical Wiring · Quick References.
- **Control Systems** (14 modules): Foundations · PID Methods · Machine Logic & Safety · Distributed Systems · Motion & Tuning.
- **NEC for Machines and Panels** (11 modules): Foundations · Motors & Article 430 · Panels & Article 409 · Machine-Side Wiring.

No template, CSS, or JS changes — the Phase 28 router (`docs/_includes/sidebar.html`) automatically opts a topic group in once any of its modules carry a `sidebar_bucket`. Validated: clean Jekyll build (1.057 s), local sidebar rendering on a sample page from each new group, baseline validators unchanged.

## 2026-04-27 — Phase 29.1 complete: Sidebar theme-compatibility tiers A–D

**Type:** UI polish / accessibility
**Status:** Complete
**Scope:** Phase 28 local sidebar (Motors pilot) + global sidebar aria-current

Single batch covering the four sidebar tiers that had been queued during Phase 29 planning.

CSS (`docs/assets/css/main.css`):
- Tier A — `[data-theme="dark"] .sidebar__chip--{b,i,a,ref,concept,code,core}` overrides mirroring the existing dark page-chip palette so local-sidebar level/type chips read in dark mode.
- Tier B — `.sidebar--local .sidebar__section-meta` gains a subtle `box-shadow` (separate light/dark values); global sidebar caret switched from text-swap (▶/▼) to a rotating ▸ chevron with a 0.15s ease, harmonizing with the local sidebar; `.sidebar__bucket-summary` letter-spacing tightened 0.07em → 0.05em.
- Tier C — `.sidebar__bucket[open] > .sidebar__bucket-summary` brightens to `var(--color-text)`; `.sidebar__chip` and `.sidebar__bucket-count` get `border-radius: 4px`.

Data (`docs/_data/training_catalog.yml`):
- Tier C — added `nav_title` for 6 Motors modules previously using their full titles in the sidebar (Induction/DC/Servo modules + Motor Family Comparison + BLDC/PMSM References).

Includes (`docs/_includes/sidebar-global.html`):
- Tier D — added `aria-current="page"` alongside `class="active"` on section, child, and grandchild links (local sidebar already had this since Phase 28).

Validated: clean Jekyll build (1.146 s), `validate_ai_boundaries.py` and `validate_reorg.sh all` show only pre-existing baseline failures.

## 2026-04-21 — Phase 29 complete: Homepage front-door rework (task-router, dedicated home layout)

**Type:** Information architecture / landing page
**Status:** Complete
**Scope:** `/` only; interior pages unchanged

Reworked the homepage from a reference-first atlas index into a task-first front door. The interior `default.html` layout was forcing the global sidebar, right-side context panel, and trust-boundary block onto `/`, competing with the topnav as a third navigation system. Phase 29 addresses that.

Includes / layouts:
- `docs/_layouts/home.html` — new. Topnav + scripts, no sidebar, no context panel, no trust-boundary, no breadcrumb. Uses a centered `.home-main` instead of the three-panel CSS Grid.
- `docs/_layouts/default.html` — untouched; interior surface stays byte-for-byte identical.

Content (`docs/index.md`):
- Hero rewritten with a plain-language promise: "Find the right standards path for your machine, panel, or safety system." 3 CTAs route to the decision workflow, scenarios, and training.
- New "Start here" 6-card task grid (decision / US panel / US+EU machine / safety / troubleshooting / training).
- Scenarios moved up from sixth section to second.
- Standards Families card grid kept but raw corpus paths (`rag/...`) removed from card bodies.
- Industry Matrix table replaced with 6 industry tile links.
- Standards Graph reduced to a one-line teaser + link.
- Repository tree moved into a collapsed `<details>` block at the bottom labelled for power users.

Topnav (`docs/_includes/topnav.html`):
- Search placeholder + ARIA "Search standards…" → "Search standards, workflows, training…".

Styling (`docs/assets/css/main.css`):
- New block at the existing home-styles area: `.home-body`, `.home-main`, `.home-hero` family, `.start-grid` / `.start-card` family, `.home-section` + intro, `.industry-tiles` / `.industry-tile` family, `.home-deep-dive` with text-swap caret matching the sidebar pattern. Reuses `--color-*` tokens so dark mode works automatically.

Validation:
- Jekyll clean build, 1.14 s.
- Home has 0 sidebars + 0 context panels; 6 Start Here cards + 6 industry tiles verified in built HTML.
- Interior pages (/standards/, Motors pilot page) unchanged.
- AI-boundary validator: 2 pre-existing failures.
- `validate_reorg.sh all`: 48/50 baseline.

## 2026-04-21 — Phase 28 complete: Sidebar pilot for Motors/Fundamentals (local section tree)

**Type:** Navigation architecture
**Status:** Complete
**Scope:** Sidebar architecture change, pilot scoped to `/fundamentals/motors/`

Replaced the single global sidebar include with a router that picks between a local section tree and the existing global sidebar. Pilot runs on one topic group; global fallback is byte-for-byte identical to the pre-pilot sidebar on every other page.

Includes:
- `docs/_includes/sidebar.html` — now a router. Matches `page.url` against `training_catalog.topic_groups[].url`; if the active group's modules carry `sidebar_bucket` tags, it includes the local sidebar, else the global.
- `docs/_includes/sidebar-global.html` — new, contains the pre-pilot markup verbatim.
- `docs/_includes/sidebar-training-group.html` — new, renders section meta + buckets (with counts) + module rows with compact chips (B/I/A, Ref/Concept/Code, Core) + nav_title-driven short labels + a TOC mount point under the active module.

Data (`docs/_data/training_catalog.yml`):
- Added `sidebar_buckets` order under `topic_groups[electrical-machines]` (Foundations / Drive Systems / Selection & Comparison / Deep References / Quick References).
- Tagged all 18 Motors modules with `sidebar_bucket`; 11 of them also received a `nav_title` for tighter sidebar text.

Styling (`docs/assets/css/main.css`):
- `--sidebar-width` bumped 240 → 288 (global token; affects all sidebars).
- New CSS block scoped to `.sidebar--local` and its children, including a chip palette and a `.sidebar__toc` active-heading indicator.

JS (`docs/assets/js/main.js`):
- New IIFE that only runs when `.sidebar.sidebar--local` exists.
- Persists open bucket state per topic group in `localStorage` (`sidebar-buckets:<group>`).
- On active module pages, scans `.main-content h2[id], h3[id]` and injects them into the TOC; an IntersectionObserver keeps the nearest heading highlighted while scrolling. No static fallback — JS-only enhancement.

Landing page (`docs/fundamentals/motors/index.md`):
- Rebuilt from one flat table into 5 bucket-grouped tables, iterating the same `sidebar_buckets` array so the landing and sidebar cannot drift out of sync.
- Module-count copy corrected 13 → 18; intro copy tweaked to mention the Phase 27 BLDC/PMSM deep references.

Validation:
- Jekyll build: clean, 1.185s.
- 3 motors pages inspected for local sidebar + correct bucket rendering + active state + TOC mount.
- 3 non-pilot pages inspected — all get the global sidebar (fallback verified).
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.
- `validate_reorg.sh all`: 48/50 baseline unchanged.

Deferred:
- Extending the local sidebar to other topic groups (Control Systems, Electrical Fundamentals, NEC) — data-only changes when ready.
- Search / filter inside the local sidebar.
- Sidebar TOC fallback for no-JS users.

## 2026-04-21 — Phase 27.7 complete: BLDC vs PMSM Comparison UX polish + factual pass

**Type:** Page-level UX polish + factual correctness
**Status:** Complete
**Scope:** `docs/fundamentals/motors/bldc-vs-pmsm/index.md` only

Applied the same pattern that landed in Phase 27.6, adapted for a decision-framed comparison page. No new pages, no new CSS; reused `.glance-grid`, `.card`, `.scenario-grid`, `.scenario-card`.

UX:
- Trimmed `## Purpose` from a 170-word paragraph to 3 bullets (Use this when / Choose BLDC if / Choose PMSM if).
- Added a 4-card "At a glance" decision strip under Purpose (BLDC wins / PMSM wins / Induction still valid / Don't choose by motor name).
- Added a 5-card "Jump to" nav: Construction, Control, Feedback, Decision Matrix, Scenarios. All anchor IDs verified.
- Moved `## Decision matrix` from after the scenarios to before them — high-value content now lands early.
- Rebuilt all 10 scenario walkthroughs (A–J) as scan cards at the top of `## Scenario walkthroughs`, each with Winner / Why / When other side wins / Stack, each linking to its existing detail H3. All 10 anchor IDs verified.

Factual / tone fixes:
- Softened `PMSM = ... always driven with sinusoidal (FOC)` → `typically driven with sinusoidal commutation or FOC`, with an explicit module-scope note.
- Corrected `DC-link undervoltage during hard regen` → `overvoltage` with correct physics.
- Softened `full stop` and `the right answer in 2026` phrasing in the takeaway section while keeping the core engineering advice.

Validation:
- Jekyll build: clean, 1.134s.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (no new regressions).
- `validate_reorg.sh all`: 48/50 baseline unchanged.

## 2026-04-21 — Phase 27.6 complete: BLDC/PMSM Implementation Guide UX polish + factual pass

**Type:** Page-level UX polish + factual correctness
**Status:** Complete
**Scope:** `docs/fundamentals/motors/bldc-pmsm-implementation/index.md` only

First-pass rework of the deepest motors page to make it feel less like a generic template. No new pages, no new layouts, no new CSS — reused `.glance-grid`, `.card`, `.card-grid`, `.scenario-grid`, `.scenario-card`.

UX:
- Trimmed `## Purpose` from a 200-word paragraph to 3 bullets (When/What/Will-not).
- Added a "Choose fast" 4-card decision strip (Choose BLDC / Choose PMSM / Watch-outs / Build sequence).
- Added a 6-card "Jump to" nav (Architecture / Control / Sizing / Drive Choice / Wiring / Checklist); all kramdown anchor IDs verified.
- Rebuilt the 8 `Practical implementation scenarios` as scan cards (Motor / Drive / Control / Why it wins), each linking to the existing detail H3 below.
- Moved `## Known industry brands` to a compact 3-column appendix table (Category / Typical vendors / Fit) at the end of the page.
- Cardified `## Implementation checklist` into 5 `.card-grid` cards (Motor / Drive / Wiring / Control / Testing). 44 task-list checkboxes render correctly inside the cards via kramdown `markdown="1"`.

Factual fixes:
- Scenario 1 drone: "PWM command ... DShot protocol" → "Digital throttle, DShot (150/300/600/1200 kbit serial) signaling — not PWM".
- Common failure modes: "DC-link **undervoltage** during regen" → "DC-link **overvoltage** during regen" with corrected physics.
- Power wiring: softened "125% of motor FLA" into an explicit NEC 430.22 citation for single continuous-duty motor branch circuits, with pointers to NEC 430.24/430.33 and IEC 60204-1 §12 for other cases.
- Contactor: rewrote to distinguish lockout / SS1-Cat-0/1 use from certified STO use.
- Feedback shield: replaced absolute "at drive end only" with a drive-manual-driven note covering single-end vs 360° both-end practice.

Validation:
- Jekyll build: clean, 1.219s.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (no new regressions).
- `validate_reorg.sh all`: 48/50 baseline unchanged.

## 2026-04-21 — Phase 27.5 complete: Visual wiring guides for BLDC and PMSM

**Type:** Phase completion (follow-up to Phase 27)
**Status:** Complete

Phase 27 shipped five BLDC/PMSM modules with wiring **tables** but minimal visuals — scenario architecture flows were 3-node `Source → Drive → Motor` blocks and the Reference modules had no wiring diagrams. Phase 27.5 closes that gap with engineer-grade Mermaid wiring visuals across all four in-scope motor pages.

**Seven new Mermaid diagrams added** using a new cable-class `classDef` convention (power=red, phase=near-black, feedback=blue, safety=orange, bus=green, shield=dashed gray):

- Implementation Guide §14: cable-group legend + table (D5), plus three archetype diagrams (D4) — Battery BLDC, Integrated PMSM servo, Shared DC-bus multi-axis PMSM
- BLDC Reference: wiring archetype (at-a-glance view of all 5 wiring groups) (D2)
- PMSM Reference: industrial servo wiring (3φ AC, EMI filter, drive with STO/fieldbus/brake, motor cable, encoder) (D3)
- Motor Selection Scenarios: upgraded 3 trivial flows + added new Scenario 2 wiring diagram (D1)

**Two pinout reference tables added** (baseline for this content class — didn't exist before):

- BLDC Reference: Hall connector pinout (IEC 60757 colors)
- PMSM Reference: Encoder connector pinout (incremental + absolute protocols + temp + shield)

**New PMSM Reference section:** `## Wiring and integration` (servo wiring + encoder pinout + STO dual-channel note + cross-link to Servo Commissioning Workflow).

**Nine cross-links added** between the diagrams across BLDC Reference, PMSM Reference, BLDC vs PMSM Comparison, Motor Selection Scenarios, and Implementation Guide — all resolve via kramdown-generated heading IDs.

Jekyll build clean, AI boundary validator shows only the 2 pre-existing failures, `validate_reorg.sh all` at 48/50 baseline, internal link checker exit 0 (273 files). RAG files and site files stay in sync.

No new pages, no routing changes — purely content enrichment layered on top of the Phase 27 footprint.

## 2026-04-20 — Phase 27 complete: BLDC/PMSM motor implementation

**Type:** Phase completion
**Status:** Complete

Five new motor reference modules shipped from planning → RAG → site:

- BLDC Motor Reference (`/fundamentals/motors/bldc-reference/`)
- PMSM Motor Reference (`/fundamentals/motors/pmsm-reference/`)
- BLDC vs PMSM Comparison (`/fundamentals/motors/bldc-vs-pmsm/`) — Core/featured, with application-fit and choice-rationale scenarios
- BLDC and PMSM Implementation Guide (`/fundamentals/motors/bldc-pmsm-implementation/`) — Core/featured, with basic wiring / control / drive patterns
- Motor Selection Scenarios (`/fundamentals/motors/motor-selection-scenarios/`) — Core/featured, three engineering-grade archetypes (fan/pump, precision axis, AGV) with per-scenario drive, wiring, tuning, measurement, and failure-mode detail

Existing `bldc-ev-drone-motors` module enriched with a drone-class BLDC vs EV-class PMSM/IPMSM deep comparison section (15 subsections sourced from `planning/motors/scenarios.md` block 3, including 2 new Mermaid architecture diagrams and inline citations to TI/Microchip/Beckhoff/Tektronix). File grew from 180 → 429 lines.

RAG corpus at `control-standards/rag/training_modules/electrical_machines/` grew from 13 → 18 files. Training catalog `electrical-machines` group `module_count` 13 → 18. Cross-links added from `bldc-ev-drone-motors` and `motor-family-comparison` modules to the five new modules.

Site HTML file count: baseline + 5. Jekyll build clean, AI boundary validator shows only the 2 pre-existing failures, `validate_reorg.sh all` at 48/50 baseline, internal link checker exit 0 (273 files scanned).

Superseded planning files removed: `planning/motors/pmsm.md` (placeholder), `planning/motors/motors_comparisons.md` (redundant with existing `motor-family-comparison` site module). `planning/motors/scenarios.md` retained as staging history (source for Module 5 and for `bldc-ev-drone-motors` enrichment).

Convention adjustments during execution:
- RAG file headers use HTML-comment format (not YAML frontmatter as plan originally spec'd) — matches the existing 13 files in the same directory.
- External citations rendered as inline plain-text markdown links, not kramdown footnotes.
- `bldc.md` source had no Mermaid diagrams (used plain text ASCII) so Module 1's Mermaid diagram expectations were not met — content complete otherwise.

## 2026-04-20 — Motors planning: BLDC vs PMSM deep dive + full implementation reference

**Type:** Planning / Content staging
**Status:** Drafts in `planning/motors/`

Two new files added to the motors planning set:

1. `planning/motors/bldc_vs_pmsm.md` — focused head-to-head engineering comparison
2. `planning/motors/bldc_pmsm_implementation.md` — full 16-section production-grade implementation reference (replaces a master-prompt template that was in the file)

`bldc_pmsm_implementation.md` covers: executive overview, end-to-end system architecture with Mermaid diagrams, BLDC vs PMSM comparison table, control methods (6-step, sinusoidal, FOC with Clarke/Park flow diagram), practical math (V = Ri + Ldi/dt + K_e·ω, T = K_t·I, ω_e = p·ω_m, mechanical equation), drive architecture (inverter / gate driver / MCU / current sensing / feedback interface), motor selection (hobby vs industrial), drive selection (ESC/VESC/ODrive vs Siemens/Beckhoff/Kollmorgen/Yaskawa/Rockwell/Mitsubishi/etc.), hobby vs industrial comparison, cost-performance tradeoff, measurement and testing (why RMS meters fail on PWM, correct instrument set, power analyzer role), 8 practical scenarios (drone, conveyor, cobot, low-cost automation, semiconductor stage, CNC spindle, e-bike, servo press), industry brand classification, wiring and integration (shielding, grounding, cable practice), common failure modes, full implementation checklist.

Scope of the new document:

- Physical construction differences (SPM vs IPM, concentrated vs distributed windings, saliency, reluctance torque)
- Back-EMF shape as the root cause of all control-strategy differences
- Control strategies: 6-step trapezoidal, sinusoidal commutation, FOC/vector
- Drive / inverter architecture comparison (shared power stage; differences in MCU, feedback, PWM, control loop rates, functional safety)
- Feedback options and match to control strategy
- Torque ripple quantified per scheme
- Speed range and field weakening (SPM vs IPM)
- Efficiency and cost structure
- 10 real-world scenarios (HVAC EC fan, e-bike, servo press, conveyor, drone, CNC spindle, cobot joint, semiconductor wafer handler, power tool, retrofit)
- Decision matrix for architecture selection
- Common field failure modes specific to each family
- Suggested follow-up planning docs (FOC math, field weakening, commissioning, servo tuning, drive hardware review)

This stays in `planning/` — it is not yet promoted to `control-standards/rag/` or built into the Jekyll site. Next step when ready: promote relevant portions into `rag/training_modules/electrical_machines/` and expand the `fundamentals/motors/` site section.

## 2026-04-16 — Control Theory Overview page rebuild

**Type:** Content / Training Enhancement
**Status:** Complete

Rebuilt `docs/fundamentals/control/control-theory-overview/index.md` from a text-dense 151-line concept dump into a visual map page. Same topics, new presentation:

- Hero Mermaid diagram showing the full feedback loop (reference → controller → plant → sensors → estimator → feedback)
- 4-card "at a glance" summary row (Plant, Controller, Sensors/Estimator, Verification) using new `.glance-grid` CSS
- Side-by-side open-loop vs closed-loop comparison with separate Mermaid diagrams using new `.compare-columns` CSS
- "Where PID fits" layered architecture diagram showing PID as one block in a larger system
- Controller families decision matrix (7 rows, 4 columns including industrial use level)
- Estimator/observer flow diagram with method table (added Luenberger observer)
- Verification process strip (model → simulation → frequency response → margins → hardware test)
- "Where to go next" 6-row routing table replacing the old 2-link footer

Added `.glance-grid` and `.compare-columns` CSS utility classes to `main.css`. Fixed kramdown markdown-inside-HTML rendering with `markdown="1"` attributes. No new pages, no layout changes, no JS.

Jekyll build clean (268 files). Internal link checker exit 0.

## 2026-04-16 — Sidebar Enumeration for Control Theory & Crosswalks

**Type:** Navigation / Discoverability
**Status:** Complete

Hybrid response to the 2026-04-16 site audit finding that `docs/_data/navigation.yml` listed `/fundamentals/control/` and `/tools/crosswalks/` as hubs without enumerating children, leaving 20+ reachable pages invisible in the sidebar.

- **Control Theory**: added 3 curated entry modules (Control Theory Overview, PID — Intuitive Foundation, PID Intuition in Practice). Full 14-page catalog continues to render on the landing page's data-driven table — sidebar stays scannable.
- **Crosswalks**: full enumeration of all 6 crosswalk pages (NFPA 79 ↔ IEC 60204-1, UL 508A / NEC / NFPA 79, IEC 61511 ↔ IEC 61508, IEC 60079 ↔ NEC 500/505, Standards Decision Workflow, Standards Comparison Tool).
- Semiconductor Facility subtree (11+3 pages) **not** added to sidebar — its landing already presents all systems in a descriptive table that would be hard to replicate cleanly as flat nav entries.

Jekyll build clean (268 files); internal link checker exit 0; visual verification of both built pages confirms new entries render at correct depth.

## 2026-04-16 — Trust-Boundary Deduplication

**Type:** Site / Content Hygiene
**Status:** Complete

Removed duplicate trust-boundary notices on 18 site pages. Root cause: `docs/_layouts/default.html:52` already auto-includes `trust-boundary.html` on every page, so per-page inline `{% include trust-boundary.html %}` calls produced two notices back-to-back. Five pages in `/industries/semiconductor/facility/` additionally wrapped the include in a redundant `<div class="trust-boundary">` parent, rendering an empty styled wrapper around the include's own div.

Pages fixed:
- `docs/training/index.md`, `docs/repository/index.md`, `docs/troubleshooting/index.md`, `docs/fundamentals/index.md`, `docs/implementation/index.md`, `docs/tools/index.md`, `docs/verification/index.md`, `docs/design/workflows/index.md`
- `docs/design/workflows/motor-selection/index.md`, `docs/design/workflows/electrical-review/index.md`
- `docs/implementation/vfd-commissioning/index.md`, `docs/implementation/servo-commissioning/index.md`, `docs/troubleshooting/motors/index.md`
- `docs/industries/semiconductor/facility/commissioning/index.md`, `.../crosswalks/index.md`, `.../instrumentation/vendor-families/index.md`, `.../instrumentation/device-families/index.md`, `.../instrumentation/alarm-strategy/index.md`

Verification: Jekyll build clean (1.327 s), internal link checker exit 0 (268 files scanned), zero built HTML pages now contain the trust-boundary heading more than once. The planning doc at `docs/superpowers/plans/2026-04-11-phase23-facility-build-phases-3-4.md` contains the include in example snippets but has no frontmatter, so Jekyll does not process its Liquid — left untouched.

## 2026-04-15 — Phase 26 COMPLETE: Navigation Restructure and Link Audit

**Type:** Site Architecture / UX
**Status:** Complete

Twelve-batch restructure that replaces the legacy 5-group sidebar with a 10-group intent-based navigation, physically relocates ~156 Jekyll pages into the new hierarchy, installs redirect infrastructure, and drives the internal link checker to zero broken links.

- Installed `jekyll-redirect-from` plugin (Gemfile + _config.yml) and created `tools/check_internal_links.py` (stdlib-only internal link checker) — Batch 1.
- Authoritative old→new URL registry persisted at `docs/_data/phase26_migration_map.yml`.
- Group migrations (Batches 2–5): fundamentals/control/motors moved from `/training/*` to `/fundamentals/electrical|control|motors/`; engineering-workflow/software-stack/workflows/reference-architecture/reference-motor-systems moved to `/design/...`; commissioning-templates, scenarios, and four build-side lifecycle stages moved to `/implementation/...`; seven verification-oriented lifecycle stages moved to `/verification/...`.
- Tools migration (Batch 6): rag-browser, glossary, crosswalks (+6 sub-pages), and reference landing moved to `/tools/...`. Word-boundary-safe link rewriter introduced after the first attempt hit a double-prefix bug.
- Training landing (Batch 7) trimmed to structured-paths only; only `/training/nec-application/` remains under `/training/`.
- Troubleshooting section (Batch 8) created; motor-troubleshooting moved from `/workflows/` into `/troubleshooting/motors/`; `/workflows/` tree deleted.
- Repository section (Batch 9) created; `/about/` moved to `/repository/about/`.
- Navigation rewrite (Batch 10): `docs/_data/navigation.yml` fully rewritten to 11 top-level groups (Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository). Four top-level landings (`/fundamentals/`, `/implementation/`, `/verification/`, `/tools/`) created so sidebar group labels do not 404.
- Cross-link sweep (Batch 11): 501 residual references to pre-Phase-26 URLs rewritten across 49 files — `training_catalog.yml` (105), `field_checklists.yml` (22), `topnav.html`, plus dozens of industry/scenario/training/standards pages. Skipped `redirect_from:` frontmatter, the migration map, `rag_tree.json`, generated RAG assets under `docs/assets/rag-files/`, and the Phase 26 plan + design spec (contain old URLs as data).
- Final audit (Batch 12): Jekyll build clean (267 HTML files), internal link check exit 0 (267 scanned), AI-boundary validator shows same 2 pre-existing Phase 25 failures with no new regressions, reorg validator 48/50 (same pre-existing baseline).

Every moved page carries `redirect_from:` frontmatter covering bare + `/index.html` variants, so three years of accumulated deep links (fundamentals/control-systems/electrical-machines, engineering-workflow, workflows/*, commissioning-templates, scenarios, lifecycle/*, field-engineering, reference, rag-browser, glossary, crosswalks, about) continue to resolve.

## 2026-04-15 — Phase 26 Batch 11 COMPLETE: Site-wide cross-link sweep

**Type:** Site structure / Cross-link sweep
**Status:** Complete

- Swept 501 residual references to pre-Phase-26 URLs across 49 files (training/fundamentals, training/control-systems, training/electrical-machines, engineering-workflow, software-stack, workflows/* split between design/implementation/troubleshooting, commissioning-templates, scenarios, all lifecycle/* stages split across verification/implementation, field-engineering, legacy reference/architecture + motor-systems, legacy /rag-browser/ /glossary/ /crosswalks/ /about/).
- Used a word-boundary-safe rewriter with ordered longest-first replacements (so `/tools/rag-browser/` is not rewritten into `/tools/tools/rag-browser/`).
- Preserved `redirect_from:` frontmatter entries (they must keep the old URLs for the plugin). Skipped `docs/_data/phase26_migration_map.yml`, `docs/_data/rag_tree.json`, `docs/assets/rag-files/**`, and the Phase 26 plan/design spec (those contain old URLs as data).
- `docs/_data/training_catalog.yml` (105 refs) and `docs/_data/field_checklists.yml` (22 refs) are the biggest single-file updates — the catalog no longer round-trips every module URL through a 301 redirect.
- `docs/field-engineering/index.md` meta-refresh shim retained and retargeted to `/implementation/commissioning-templates/`.
- Jekyll build clean (267 HTML files). Internal link check exit 0 (267 scanned). AI-boundary validator: only the 2 pre-existing Phase 25 failures, no new regressions.

## 2026-04-15 — Phase 26 Batch 10 COMPLETE: navigation.yml rewrite + 4 top-level landings

**Type:** Site structure / Navigation rewrite
**Status:** Complete

- Added 4 top-level landing pages required by the new nav structure — `docs/fundamentals/index.md`, `docs/implementation/index.md`, `docs/verification/index.md`, `docs/tools/index.md`. Each page presents sub-group cards, a scope blockquote, and cross-links into adjacent sections. Without these landings, sidebar group labels (which are clickable) would have 404'd.
- Fully rewrote `docs/_data/navigation.yml` from the prior 5-group historical layout to the 11-group intent-based structure: Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository. Match prefixes realigned; legacy "Engineering Workflow" and "Reference" meta-groups dropped.
- Standards group retains the full per-family hierarchy (US Electrical → NEC/NFPA 79/UL 508A, Machinery → IEC 60204-1, Functional Safety → IEC 61508/61511/62061/ISO 12100/ISO 13849-1, Cybersecurity → IEC 62443, Hazardous Area → IEC 60079, Semiconductor → SEMI, plus the Relationship Graph).
- Jekyll build clean (267 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 9 COMPLETE: Repository landing + About relocation

**Type:** Site structure / New section + page move
**Status:** Complete

- Added `docs/repository/index.md` — Repository and Project Info landing with the GitHub link, a build-stack summary (Jekyll, Mermaid, Cytoscape, jekyll-redirect-from, internal link checker), a content-source-of-truth table pointing at `project_state/`, and a contributing note.
- Moved `docs/about/index.md` to `docs/repository/about/index.md` with `redirect_from:` for `/about/` + `/about/index.html`. Breadcrumb retargeted to `Repository › About`.
- `docs/_includes/topnav.html` — top-nav "About" link updated to `/repository/about/`.
- `docs/_data/navigation.yml` — dropped the `/about/` prefix + About child from the Reference group, added a new Repository top-level group (children: About / Trust Boundary).
- Empty `docs/about/` directory removed.
- Jekyll build clean (263 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 8 COMPLETE: Troubleshooting section

**Type:** Site structure / New section
**Status:** Complete

- Created `/troubleshooting/` section with landing + Motors subpage. Landing organizes field diagnosis entry points into 6 symptom categories (Motors, VFDs, PLC systems, Field I/O, Networks, Safety circuits), each pointing at the right existing workflow, fundamentals reference, or commissioning template.
- Moved `docs/workflows/motor-troubleshooting/index.md` to `docs/troubleshooting/motors/index.md` with `redirect_from:` stanza, updated breadcrumb, and refreshed cross-links (fundamentals/motors, design/workflows/motor-selection, implementation/vfd-commissioning, implementation/servo-commissioning, implementation/commissioning-templates/motor-rotation-verification).
- Sweep of `/workflows/motor-troubleshooting/` → `/troubleshooting/motors/` across 5 source pages and 2 data files (`design/workflows/index.md`, `design/workflows/motor-selection/index.md`, `design/index.md`, `implementation/vfd-commissioning/index.md`, `implementation/servo-commissioning/index.md`, `_data/training_catalog.yml`, `_data/field_checklists.yml`).
- Removed `docs/workflows/` entirely — the empty `electrical-review/` and `motor-selection/` shells from Batch 3 were deleted along with the motor-troubleshooting subdir.
- Added Troubleshooting group to `docs/_data/navigation.yml` (children: Motors). Full nav restructure to the 10-group target is still reserved for plan Task 13.
- Jekyll build clean (261 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 7 COMPLETE: Training landing trim

**Type:** Site structure / Navigation refactor
**Status:** Complete

- Rewrote `docs/training/index.md` as a thin structured-paths landing. Only NEC-for-Machines-and-Panels remains under `/training/`; foundational electrical, control, and motors content has lived under `/fundamentals/` since Batch 2 and is no longer enumerated on the training page.
- Replaced the old catalog-driven Start-Here grid, Learning-Paths grid, topic-group cards, all-modules table, and related-standards list with a short path table plus a "Related Sections" pointer block.
- Link targets retargeted to existing sub-landings (`/fundamentals/electrical/`, `/design/architecture/`, `/verification/lifecycle/`, `/implementation/scenarios/`, `/tools/reference-hub/`, etc.) rather than bare `/fundamentals/`, `/verification/`, `/implementation/`, `/tools/` — those top-level landings don't exist yet and are out of scope for Batch 7.
- `docs/_data/training_catalog.yml` untouched — it is still consumed by the three `/fundamentals/*` group landings, the NEC-application index, and the `training-module` layout.
- Jekyll build clean (259 HTML files); internal link check exit 0.

## 2026-04-15 — Phase 26 Batch 6 COMPLETE: Tools group migration

**Type:** Site structure / Navigation refactor
**Status:** Complete

- Moved 10 pages from `/rag-browser/`, `/glossary/`, `/crosswalks/`, and `/reference/` into the new `/tools/` hierarchy (`/tools/rag-browser/`, `/tools/glossary/`, `/tools/crosswalks/...`, `/tools/reference-hub/`).
- Added `redirect_from:` (bare + `/index.html` variants) to every moved file so old URLs continue to resolve via `jekyll-redirect-from`.
- Repo-wide cross-link sweep: 143 replacements across 39 files using a word-boundary-safe rewriter (`tools/_phase26_batch6_update_links.py`) that avoids double-prefix pollution like `/tools/tools/...`.
- Also backfilled straggler references to `/reference/architecture/*` and `/reference/motor-systems/*` (originally moved to `/design/` in Batch 3) within the six design pages.
- `docs/_data/navigation.yml` Reference group updated to point at `/tools/...` URLs.
- Removed empty source directories: `docs/rag-browser/`, `docs/glossary/`, `docs/crosswalks/`, `docs/reference/`.
- Fixed relative-link regression in `tools/crosswalks/compare/index.md` where `../../standards/` no longer resolves from the deeper path; rewrote to absolute `{{ '/standards/' | relative_url }}`.
- Jekyll build clean (259 HTML files); internal link check exit 0.

## 2026-04-13 — Phase 24 COMPLETE: Training visual upgrades

**Type:** Content / Training Enhancement
**Status:** Complete

### Task 2 — Semiconductor Fab Tool scenario page visual aids

- Added `## Design Workflow Overview` flowchart (LR, 4-phase) after the Standard Stack table
- Added `## Process Start Permissive Flow` flowchart (5-permissive gate chain: exhaust, gas detector, doors, HV/RF, manual reset → gas/RF enable)
- Added `## Fault Trip Sequence` flowchart (4 fault types → Safety PLC → close NC valves + disable RF/HV + stop motion + alarm → latch → manual reset → standby)
- Added `### HV Access Interlock Flow` inside Key Engineering Decisions (discharge loop with polling)
- Added `### Cybersecurity Zone Diagram` inside Key Engineering Decisions (fab host → firewall → tool controller; Safety PLC shown as hardwired-only, not network-reachable)
- Jekyll build: clean

---

## 2026-04-13 — Phase 24 Task 1 complete: IEC earthing systems visual upgrades

**Type:** Content / Training Enhancement
**Status:** Complete

- Added visual summary flowchart (fault return path decision tree) after the IEC letter-code tables
- Added compact Mermaid topology diagrams for each of the five earthing systems (TN-C, TT, TN-C-S, TN-S, IT)
- Added per-system blockquote callout cards (fault return / protection / main risk)
- Added "Machine designer takeaway" bold paragraph after each system's callout
- Replaced the existing 5-column comparison table with an expanded version including "Typical clearing method" column and bold System names
- Added "Selection logic — what are you optimizing for?" flowchart section before "The practical questions to ask"
- Jekyll build remains clean (no errors or warnings)

## 2026-04-12 — Phase 24 planning seeded with earthing-systems visual upgrade

**Type:** Project Direction
**Status:** Planned

- Updated `project_state/project_state.md` so the next tracked phase is `Phase 24 PLANNING — Training Visual Upgrades`
- Queued a visual enhancement pass for `docs/training/fundamentals/earthing-systems-iec/index.md`
- Recorded `planning/ground_earth_visual.md` as the implementation note for the earthing-systems page upgrade
- Captured the expected scope: overview fault-path visual, five compact system diagrams, decision tree, comparison table cleanup, and short per-system callout cards

## 2026-04-12 — Phase 23 Complete: Semiconductor Facility Build Phases 3 & 4

**Type:** Content / Standards Reference
**Status:** Complete

- Promoted 3 instrumentation staging files to RAG corpus (`device_family_library.md`, `vendor_families.md`, `alarm_and_measurement_strategy.md`)
- Authored new `commissioning_reference.md` RAG file; updated `_index.yaml` with 4 new entries
- Built 5 new Jekyll pages:
  - `/instrumentation/device-families/` — device family library grouped by function
  - `/instrumentation/vendor-families/` — manufacturer comparison by measurement class (pressure, flow, UPW, MFCs, gas detection, level, vacuum, cleanroom)
  - `/instrumentation/alarm-strategy/` — alarm philosophy, measurement windows, alarm classes, safe-state design
  - `/commissioning/` — phase-based commissioning framework with readiness criteria and system-specific notes
  - `/crosswalks/` — system-to-system dependency map and standards-to-systems crosswalk
- Added "In This Section" navigation block to instrumentation landing page
- Updated `navigation.yml` (instrumentation sub-pages + Commissioning + System Crosswalks under facility)
- Updated facility `index.md` scope table
- Jekyll build: clean, 157 pages

## 2026-04-11 — Phase 22 Complete: Semiconductor Facility Reference (10 pages)

Second slice — four additional pages:

- HVAC and Cleanroom (room pressure cascade, ISO 14644, particle monitoring)
- Bulk Chemical Distribution (storage, transfer sequencing, containment, SEMI F39/F57)
- Safety and Shutdown Architecture (4-layer shutdown model, cause-and-effect, SIL integration)
- Common Control Philosophy (modes, state machine, permissives/interlocks/trips, safe-state rules)
- Facility overview and semiconductor industry page updated; navigation extended
- Jekyll build: clean, 152 pages

## 2026-04-11 — Phase 22 First Slice: Semiconductor Facility Reference

- Fixed AI boundary headers on 7 RAG files; validate_ai_boundaries.py now passes 316/316
- Committed `planning/semi_facility/` staging area to git
- Promoted 10 staging files to `control-standards/rag/design_framework/semiconductor_facility/` with proper headers and `_index.yaml`
- Built 6 new Jekyll pages under `docs/industries/semiconductor/facility/`:
  - Facility overview + standards selection flowchart
  - Bulk Specialty Gas Systems
  - UPW and Wastewater Systems
  - Exhaust and Abatement Systems
  - Tool-Facility Interface
  - Instrumentation Reference (full use matrix by system)
- Added Semiconductor Facility sub-tree to `docs/_data/navigation.yml`
- Cross-linked from existing semiconductor industry page
- Jekyll build: clean, 148 pages (up from 142)

## 2026-03-27 — Control Systems Training Expansion (7 new modules)

- Added 7 training modules to `docs/training/control-systems/` from `planning/phase_27march26/` content:
  - Machine State Model (FSM types, state design, fault handling)
  - Interlocks, Permissives & Safety Trips (definitions, logic separation, bypass design)
  - Async Faults in Distributed Systems (detection, classification, response, recovery)
  - Deterministic vs Non-Deterministic Control (real-time requirements, architecture separation)
  - Servo Tuning Strategy (loop-by-loop workflow, resonance detection, notch filters, feedforward)
  - Vibration and Resonance (causes, detection, mechanical and control mitigation)
  - Multi-Axis Coordination (master-slave, electronic gearing, interpolation, gantry)
- Updated `_data/training_catalog.yml`: 7 module entries added, module_count 7 → 14, description updated
- Jekyll build: clean
- `planning/phase_27march26/things_to_fix.md` (lifecycle improvements) deferred — separate task

## 2026-03-22 — Phase 21: Lifecycle Stage Page Expansion

- Expanded all 12 lifecycle stage pages (Stages 01–11 plus Safety Wiring) from thin stubs (41–74 lines) to comprehensive engineering references (580–1000+ lines)
- Created 2 new pages: Stage 3.5 (Safety Requirements Specification) and Stage 12 (Management of Change)
- Updated `docs/lifecycle/index.md` with expanded introduction section and 13-stage table (all stages now comprehensive)
- All lifecycle pages now follow consistent content pattern: purpose/scope, key decisions, related standards, practical guidance, checklists, cross-links to training/workflows/reference material
- No new pages added beyond the 2 planned new stages; lifecycle section maintains stable URL structure
- Jekyll build: clean, 132 pages (no change in page count from Phase 20)

## 2026-03-15 — Phase 20: Software Safety Stack Deepening

- Updated RAG source `Software_Safety_and_Intrinsic_Safety_Standards.md`: IEC 61131-3 edition note updated to 2025; Normal PLC / Safety PLC / SIS comparison table added; E-stop section fully replaced with canonical tag names (SI_ESTOP_CH1, ESTOP_HEALTHY, SAFETY_ENABLE), 7-rung pseudocode, I/O list, sequence of operation, documentation and logging checklists; Rockwell GuardLogix and Siemens S7-1500F vendor patterns added
- Updated `/software-stack/` site page: edition note updated; comparison table section added; E-stop section replaced with expanded content including Mermaid wiring/architecture flowchart and state machine diagram; vendor patterns in `<details>` expandable blocks
- No new pages; no navigation changes; build remains clean at 132 pages

### 2026-03-15 — Phase 20 changed to software safety routing work

- Updated `project_state/project_state.md` so the next tracked phase is now `Phase 20 QUEUED — Software Safety, Traceability, and Cybersecurity Routing`
- Added a Phase 20 queue section sourced from `planning/safety_software_stack.md`
- Replaced the previous Phase 20 scenario-driven learning candidate as the active next-phase entry in project state

### 2026-03-15 — Software stack reference flow rebuilt from planning + RAG

- Rewrote `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` into a tighter reference flow: scope boundary, quick answers, routing, traceability/logging, redundancy, worked E-stop example, cybersecurity, wiring, intrinsic safety, and implementation deliverables
- Merged high-value practical content from `planning/safety_software_stack.md` into the canonical RAG source without pulling the planning file itself into the site or RAG browser
- Updated `docs/software-stack/index.md` to match the new flow and remove the older IEC 61131-3 presentation that was less aligned with the practical question the page is answering
- Jekyll build: clean after rewrite; AI boundary validator still reports pre-existing unrelated violations elsewhere in the RAG corpus

### 2026-03-14 — Project state reconciled after Phase 19 completion

- Updated `project_state/project_state.md` to reflect that Phases 18 and 19 are fully complete with no active implementation backlog remaining from those tracks
- Changed `Next Phase` from `Phase 20 TBD` to `Phase 20 CANDIDATE — Scenario-Driven Learning Layer`
- Rewrote the `Current Direction` section to reflect planning-mode status rather than queued Phase 18/19 implementation work
- Removed the stale `Phase 18 Backlog` and `Phase 19 Queue` sections and replaced them with a Phase 20 candidate summary sourced from the cross-layer integration pre-plan

### 2026-03-14 — Phase 19: Engineering Workflow Navigation Refactor

- Created `docs/_data/navigation.yml` — 5-group sidebar data model (Engineering Workflow, Standards, Training, Industries, Reference)
- Refactored `docs/_includes/sidebar.html` from 135-line hardcoded HTML to ~60-line data-driven Liquid renderer
- Added `/engineering-workflow/` hub page with 5 task-grouped sections (Design & Architecture, Select & Size, Commission & Verify, Troubleshoot, Scenarios)
- Expanded `/reference/` landing page with Quick Reference section (Glossary, Crosswalks, Software Stack, RAG File Browser)
- Demoted Scenarios, Crosswalks, and Workflows from top-level sidebar into Engineering Workflow and Reference hub groups
- Jekyll build: clean, 132 pages

### 2026-03-14 — Phase 18 Track C: Reference Section + Commissioning Templates Redesign

- Added `/reference/` section: landing page + 4 content pages (machine architecture model, machine safety architecture, compliance stack, motor selection matrix)
- Added new "Reference Models" sidebar block with Architecture and Motor Systems sub-groups + `.sidebar__group-label` CSS
- Renamed `/field-engineering/` → `/commissioning-templates/`: 7 pages moved, old sub-pages removed, redirect at `/field-engineering/`
- Updated `field-checklist.html` layout: label renamed to "Commissioning Templates", template header block (6-field fill-in grid), checkbox DOM transformation script, back-link updated
- CSS additions: `.template-header`, `.checklist-item`, `.sidebar__group-label`, print checkbox styles
- URL updates: `field_checklists.yml` (6 entries), `training_catalog.yml` (13 URLs across 11 modules), 5 workflow pages
- Cross-links added: motor-selection workflow → motor-selection-matrix; semiconductor-equipment scenario → machine-architecture-model; semiconductor industry → compliance-stack
- Jekyll build: clean, 0.446 s, **129 pages** (matches spec target)

### 2026-03-13 — FE Study Tools: `.doc` File Support

- feat(fe_study): `.doc` file support — LibreOffice headless conversion, `howto_doc` family (P2 priority), cached under `_converted/`
- Conversion: LibreOffice headless (`soffice --headless --convert-to docx`), cached in `_converted/`
- Covers all `.doc` files under `planning/FE_Study/How to/`
- Filtered: `~$*.doc` temp/lock files excluded from scanning
- Full test suite: 15/15 PASS

### 2026-03-13 — Phase 18 Track B: Field Engineering Section

- Added `/field-engineering/` site section with 7 pages (landing + 6 commissioning checklists)
- New `field-checklist` layout with Liquid data lookup from `field_checklists.yml`, "When to use" box, cross-links block, and print-optimized view
- Created `docs/_data/field_checklists.yml` flat YAML catalog driving all checklist metadata
- CSS additions: `.checklist-body` (☐ pseudo-element), `.field-checklist__cross-links`, `.cross-links-group`, print hiding rules
- Reverse links: `related_checklists` key added to 11 training module entries in `training_catalog.yml`; `training-module.html` updated to render them
- Reverse links: "Related Checklists" sections appended to 5 workflow pages
- Sidebar: Field Engineering section with 7 links and active state logic
- Jekyll build: clean, 123 pages

### 2026-03-13 — Phase 19 engineering-workflow navigation refactor queued

- Added plan doc: `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`
- Queued Phase 19 in `project_state/project_state.md` as the next navigation refactor after Phase 18 Track C
- Recorded that the first refactor pass will keep current URLs stable, add workflow/reference hub pages, and move the sidebar toward a data-driven model

### 2026-03-13 — Phase 18 Track A: Control Systems training surfaced (9 new pages)

- Added `/training/control-systems/` group landing page and 7 module pages: Control Theory Overview, PID Foundation, PID Intuition, Industrial PID Implementation, Control Loop Architectures, PID Heater Control, PID Drone Control
- Added `/training/fundamentals/earthing-systems-iec/` page covering IEC TN-C/TT/TN-C-S/TN-S/IT earthing systems with comparison table
- Updated `docs/_data/training_catalog.yml`: control-systems topic group (7 modules), Control Systems Engineering learning path, start-here audience entry, fundamentals count 8→9, earthing module entry
- Updated sidebar: Control Systems link added under Training section
- Fundamentals group index updated: description and module count 8→9
- Jekyll build: clean, 116 pages (up from 107)

### 2026-03-13 — Project-state backlog reconciled after Phase 17

- Updated `project_state/project_state.md` to reflect the actual post-Phase-17 site state: 107-page clean build, 45-term glossary, 9 scenarios, 6 crosswalk pages, 32 surfaced training modules, 5 workflow pages, and standards graph coverage that already includes IEC 60079, IEC 61511, and SEMI
- Clarified `Next Phase` as `Phase 18 QUEUED — Field Engineering, Reference Library, and Control Systems Training`
- Replaced the stale note that Control Systems training needs new RAG corpus; canonical `training_modules/control_systems/` content already exists, so the remaining work is site surfacing and navigation
- Marked the old GitHub Pages deployment notes as completed and converted the old Phase 3 backlog note into historical carryover status
- Added direct references in `project_state/project_state.md` to the Phase 18 control-systems plan and the field/reference pre-plan

### 2026-03-10 — Phase 16 complete: NEC training expansion — 11-module NEC track

- Expanded NEC application training track from 3 to 11 modules (8 new RAG files + 8 new site pages)
- New RAG files in `control-standards/rag/training_modules/nec_application/`: branch_circuits_vs_feeders_motor_loads.md, disconnecting_means_for_machinery.md, grounding_bonding_control_panels.md, sccr_workflow.md, conductor_ocpd_sizing_examples.md, class1_class2_remote_control_circuits.md, article_430_practical_workflow.md, article_409_practical_workflow.md
- All 8 RAG files mirrored to `docs/assets/rag-files/training_modules/nec_application/`
- `control-standards/rag/training_modules/nec_application/_index.yaml` updated to 11 files
- `docs/_data/training_catalog.yml`: 8 new module entries added; nec-application topic_group module_count updated to 11; panel-design-nec learning path expanded with 4 new URLs
- `docs/training/nec-application/index.md`: description updated to 11 modules; recommended entry modules expanded to 4; page header updated
- `docs/training/nec-application/motor-panel-code-application/index.md`: footer next-link updated to point to branch-circuits-vs-feeders
- `docs/_data/rag_tree.json` regenerated (249 .md files, 5 top-level entries)
- Jekyll build: clean (0.529 s)

### 2026-03-10 — Phase 16 partial: four additional NEC site pages (pages 5–8)

- Added `docs/training/nec-application/conductor-ocpd-sizing/index.md` — step-by-step Art 430 sizing: table FLC, 125% conductor, 115%/125% overload, Table 430.52 OCPD, Table 250.122 EGC; full worked examples for 10 HP and 25 HP motors; Art 430.24 feeder formula with three-motor example; quick-reference HP sizing table (1–50 HP at 460/480 V); common mistakes table; won't-start exception explained
- Added `docs/training/nec-application/class1-class2-circuits/index.md` — Art 725 circuit classification (Class 1/2/3), supply-listing rule, 24 VDC PLC I/O as Class 2, Mermaid classification flowchart, Art 725.136 separation rules (separate duct / barrier), NFPA 79 color coding (blue=24 VDC, red=120 VAC), common mistakes table
- Added `docs/training/nec-application/article-430-workflow/index.md` — Art 430 Parts routing table (Parts I–X), Art 430.6(A) table-not-nameplate rule, Mermaid motor-circuit question router, standard 5-step sizing sequence (table FLC → conductor → overload → OCPD → disconnect), full worked example for 25 HP 460 V through all 5 steps, won't-start exception procedure, NFPA 79 alignment notes
- Added `docs/training/nec-application/article-409-workflow/index.md` — Art 409 ICP scope (factory-built assembly), Art 409.20 supply conductor sizing formula (125% largest motor + 100% others + 125% resistance heating), worked example with 25 HP + 10 HP motors, Art 409.110 required markings table (SCCR, FLC, enclosure type), Art 409.22 OCPD sizing, Art 409 vs. UL 508A comparison table (code vs. product standard), ICP (Art 409) vs. MCC (Art 430 Part F) comparison table, pre-shipment inspection checklist
- All four pages use `layout: training-module`, correct breadcrumbs, prev/next navigation, and Mermaid diagrams where specified
- Prev/next chain now complete: sccr-workflow → conductor-ocpd-sizing → class1-class2-circuits → article-430-workflow → article-409-workflow (terminus)

### 2026-03-10 — Phase 16 partial: four new NEC site pages

- Added `docs/training/nec-application/branch-circuits-vs-feeders/index.md` — branch circuit vs. feeder boundary, Art 430.22 125% conductor rule, Art 430.24 multi-motor feeder formula, Mermaid circuit flow, nameplate vs. table FLC common mistake
- Added `docs/training/nec-application/disconnecting-means/index.md` — Art 430.102 in-sight rule (visible + ≤50 ft), permitted disconnect types (HP-rated switch, MCCB, molded-case switch), NFPA 79 §6.2 lockable main disconnect, group disconnect exception Art 430.112, VFD placement rule (input side only), Mermaid VFD flow
- Added `docs/training/nec-application/grounding-bonding-panels/index.md` — grounding vs. bonding distinction, EGC sizing from Table 250.122 (earth rod is not the fault-current path), EGC sizing reference table (15A–200A), neutral/ground separation at downstream panels, enclosure bonding, VFD grounding notes, Mermaid 4-wire feeder flow
- Added `docs/training/nec-application/sccr-workflow/index.md` — SCCR definition, NEC 409.110 marking requirement, available fault current concept, UL 508A Supplement SB 4-step component method, current-limiting device raise strategy, Mermaid SB workflow diagram, 5 kA contactor default trap
- All pages use `layout: training-module`, correct breadcrumb, prev/next navigation, and Mermaid diagrams
- `training_catalog.yml` entries for these 4 modules still pending

### 2026-03-10 — Phase 15 complete: Training Module UX

- Created `docs/_layouts/training-module.html` — dedicated layout that looks up module metadata from `training_catalog.yml` by `page.url` and renders level chip, time, type, focus, Core badge, outcome sentence, and prerequisites before page content
- Added CSS: `.module-meta-bar`, `.module-outcome`, `.module-prereqs` to `main.css`
- Batch-updated all 24 module pages: layout changed to `training-module`, hardcoded page-header div removed, breadcrumb labels updated to new display names (Electrical Fundamentals, Motors Drives and Motion, NEC for Machines and Panels)
- Jekyll build: clean, 0.535 s

### 2026-03-10 — Phase 14 complete: Training Curriculum Upgrade

- Created `docs/_data/training_catalog.yml` — shared data model for all 24 modules with level, time, type, focus, prerequisites, featured flag, learning paths, start-here entries, and related standards
- Added training-specific CSS section to `docs/assets/css/main.css` — verification note, start-here cards, learning-path cards, training chips/badges (beginner/intermediate/advanced/concept/reference/code/featured), module table wrapper, related-standards strip, mobile responsive rules
- Rewrote `docs/training/index.md` — now a curriculum hub with verification note, start-here audience cards, four learning paths, browse-by-topic cards, data-driven all-modules table with metadata, and a related-standards strip; trust-boundary include retained at bottom
- Upgraded `docs/training/fundamentals/index.md` — new display label "Electrical Fundamentals", group intro, recommended entry modules, metadata-rich table driven from catalog
- Upgraded `docs/training/electrical-machines/index.md` — renamed to "Motors, Drives, and Motion", group intro, recommended entry modules, metadata-rich table
- Upgraded `docs/training/nec-application/index.md` — renamed to "NEC for Machines and Panels", group intro, recommended entry modules, metadata-rich table, note about Phase 16 expansion
- Updated sidebar labels to match new display names (URLs unchanged)
- Jekyll build: clean, 0.391 s

### 2026-03-11 — Post-Phase 16 site planning expanded for control-systems and eVTOL content

- Updated `docs/plans/2026-03-10-training-system-integration-preplan.md` to reserve a future `docs/training/control-systems/` route for the new PID/control-loop material
- Added a candidate scenario/page for a paraphrased public-source Archer vs. Joby eVTOL motor architecture comparison
- Recorded page rules that future public-source application notes should be paraphrased engineering analysis rather than raw transcript dumps or authoritative standards guidance
- Updated `project_state/project_state.md` post-Phase 16 target themes without changing the queued Phase 14-16 sequence

### 2026-03-10 — Training system integration pre-plan added

- Added planning-prep note: `docs/plans/2026-03-10-training-system-integration-preplan.md`
- Captured the current architecture gap between training, standards, lifecycle, scenarios, workflows, field checklists, and reference material
- Documented a post-Phase 16 candidate breakdown for:
  - cross-layer knowledge routing
  - field engineering and reference-library surfacing
  - safety and machine-architecture training expansion
  - scenario-driven learning
- Updated `project_state/project_state.md` with a post-Phase 16 planning candidate reference without changing the current queued Phase 14-16 sequence

### 2026-03-10 — Phase 14 training curriculum planning docs added

- Added design doc: `docs/plans/2026-03-10-phase14-training-curriculum-design.md`
- Added implementation plan: `docs/plans/2026-03-10-phase14-training-curriculum-implementation.md`
- Updated `project_state/project_state.md` Phase 14 section to reference the new planning docs
- Planning direction keeps current URLs stable while redesigning `/training/` around Start Here, Learning Paths, metadata-backed tables, filters, standards links, and a top-of-page verification note

### 2026-03-10 — Training page review converted into queued Phase 14-16 work

- `project_state/project_state.md` — next planned work changed from generic maintenance to `Phase 14 QUEUED — Training Curriculum Upgrade`
- Recorded that the current `/training/` section is complete but still behaves more like a browsable module index than a guided learning system
- Added `Phase 14 Scope — Training Curriculum Upgrade` for Start Here entry points, learning paths, audience framing, stronger hierarchy, outcome-focused copy, and a top-of-page verification note
- Added `Phase 15 Scope — Training Metadata And Module UX` for module chips and metadata fields covering level, time, prerequisites, type, role focus, and optional filtering/sorting
- Added `Phase 16 Scope — NEC Training Expansion` to grow NEC training from 3 modules to at least 8-10 modules with practical Article 409/430, SCCR, bonding, OCPD, and control-circuit topics

### 2026-03-10 — Phase 13 COMPLETE — all secondary backlog items done

- `docs/crosswalks/iec61511-iec61508/index.md` — new crosswalk: process SIS (IEC 61511) vs. functional safety foundation (IEC 61508); lifecycle comparison, SIL framework, architecture constraints, prior use, clause cross-reference (~250 lines)
- `docs/crosswalks/iec60079-nec-500-505/index.md` — new crosswalk: Zone vs. Division hazardous area; classification tables, EPL, gas groups, equipment marking, protection types, Zone/Division selection flow (~260 lines)
- `docs/crosswalks/index.md` — 2 new rows added
- `docs/_includes/sidebar.html` — 2 new crosswalk sidebar links
- All remaining Phase 13 backlog items confirmed complete: industry pages (5), standards graph (IEC 60079/61511/SEMI nodes), glossary (45 terms)
- Build: clean

### 2026-03-09 — Training site pages complete (24 modules)

- `docs/training/index.md` — landing page, 24 modules in 3 groups
- `docs/training/fundamentals/` — 8 pages: circuit theory, components, equations, conductor sizing
- `docs/training/electrical-machines/` — 13 pages: motors, drives, servo systems
- `docs/training/nec-application/` — 3 pages: code reading, table navigation, motor/panel application
- Sidebar updated with Training section (Training → Fundamentals / Electrical Machines / NEC Application)
- Build: 85 pages, clean

---

### 2026-03-09 — Motor interview source note promoted into additional training and design files

- `control-standards/work/design/check_this.md` — used as a read-only source for motor interview-style fundamentals, VFD electrical design points, and troubleshooting patterns; source file left unchanged.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_and_vfd_equations_reference.md`, `motor_efficiency_power_factor_and_losses.md`, `motor_control_methods_and_operating_regions.md`, and `servo_feedback_and_inertia_matching.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_cable_and_protection_review.md` and `motor_symptom_troubleshooting_patterns.md`; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Phase 12 Complete: Offshore / Marine Industry Overlay

- `DNV_OS_D201__electrical_installations.md` — RAG module: marine grade, IT earthing, LSOH cable, DP class, ESD/F&G class requirements, class approval workflow
- `ABS_offshore_electrical_control.md` — RAG module: ABS class notations, type approval, IT earthing implications, emergency power requirements
- `docs/industries/offshore/index.md` — full reference page: standards matrix by phase, DNV/ABS selection flow, IT earthing, LSOH, 11-item compliance checklist
- `docs/industries/marine/index.md` — deepened with IMO regulatory framework, IEC 60092 series structure, marine vs. offshore comparison; IEC 60092 corpus gap documented
- `docs/scenarios/offshore-platform-control/index.md` — Scenario 09: 4-phase workflow, ESD level hierarchy, Mermaid power/ESD architecture diagram, IT earthing and FAT decisions
- Scenarios index and sidebar updated

---

### 2026-03-09 — Electrical Knowledge Integration complete

Promoted three transcript-derived electrical learning sources into the existing canonical RAG layers.
No new parallel layer created. All content routes into existing `training_modules/`, `design_framework/`,
`commissioning_checklists/checklists/`, and `standards_intelligence/crosswalks/overlap_notes/`.

Design doc: `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

#### training_modules/fundamentals/ (new)

- 7 files: `electrical_quantities_and_circuit_language`, `series_parallel_and_divider_methods`,
  `kirchhoff_laws_and_systematic_analysis`, `equivalent_circuit_methods`,
  `electrical_equations_reference`, `passive_components_resistors_capacitors`,
  `diodes_transistors_and_switching_basics`

#### training_modules/electrical_machines/ (expanded)

- 3 core motor files + 6 additional: `vfd_fundamentals`, `servo_drive_fundamentals`,
  `ac_vs_dc_motor_comparison`, `motor_family_comparison`,
  `brushless_dc_ev_and_drone_motor_comparison`, `vfd_and_servo_architecture_diagrams`

#### training_modules/nec_application/ (new)

- 3 files: `nec_code_reading_fundamentals`, `working_space_and_table_navigation`,
  `motor_and_panel_code_application`

#### design_framework/electrical_review/ (new)

- 4 files: `ohms_law_and_power_check_workflow`, `basic_resistive_network_review`,
  `component_selection_basics`, `simple_signal_and_interface_circuit_notes`

#### design_framework/motor_systems/ (expanded)

- 13 total files including: selection workflow, nameplate checklist, star-delta notes,
  VFD integration review, commissioning workflows, troubleshooting decision tree,
  comparison matrices, integrated-drive architecture notes

#### commissioning_checklists/checklists/ (expanded)

- 6 files: motor rotation/overload, nameplate/overload setting, circuit polarity,
  capacitor discharge, drive commissioning, pre-power panel check

#### standards_intelligence/crosswalks/overlap_notes/ (gap fill)

- `overlap__motors_drives.md`
- `overlap_nfpa79_iec60204__motors_drives.md`

---

### 2026-03-09 — Integrated motor-drive architecture notes extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for integrated drive-on-motor content; source file left unchanged during extraction.
- `control-standards/rag/design_framework/motor_systems/` — added `integrated_motor_drive_architecture_comparison.md`, `industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md`, `motor_mounted_drive_thermal_and_emc_design_notes.md`, `integrated_drive_failure_modes_and_tradeoffs.md`, and `integrated_drive_serviceability_and_field_replacement_review.md`.
- `control-standards/rag/design_framework/motor_systems/README.md` and `_index.yaml` — updated to include the new integrated-drive architecture note set.

---

### 2026-03-09 — Motor comparison pages extracted from work-note source

- `control-standards/work/design/check_this.md` — used as a read-only source for new motor comparison and architecture content; source file left unchanged during the extraction pass.
- `control-standards/rag/training_modules/electrical_machines/` — added `motor_family_comparison.md`, `ac_vs_dc_motor_comparison.md`, `vfd_and_servo_architecture_diagrams.md`, and `brushless_dc_ev_and_drone_motor_comparison.md`; updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/motor_selection_comparison_matrix.md` — added a concept-stage motor-family selection matrix; updated the module README and `_index.yaml`.

---

### 2026-03-09 — Motor comparison/diagram source note normalized for RAG promotion prep

- `control-standards/work/design/check_this.md` — converted a raw generated draft on motor, VFD, servo, BLDC, EV, and drone comparison pages into a scoped promotion-prep note.
- The note now identifies which content should enrich existing motor fundamentals files, which new RAG files are high-value next additions, and which EV/drone topics should remain lower-priority unless the repository scope expands.

---

### 2026-03-09 — Motor/VFD/servo RAG modules expanded from updated work note

- `control-standards/work/design/check_this.md` — used as a source note for additional motor-drive training, workflow, and checklist content; source left in place as work material.
- `control-standards/rag/training_modules/electrical_machines/` — added `vfd_fundamentals.md` and `servo_drive_fundamentals.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/design_framework/motor_systems/` — added `motor_troubleshooting_decision_tree.md`, `vfd_commissioning_workflow.md`, and `servo_commissioning_workflow.md`, and updated the module README and `_index.yaml`.
- `control-standards/rag/commissioning_checklists/checklists/drive_commissioning.md` — added a field checklist for first drive power-up and early verification; checklist README and `_index.yaml` updated accordingly.

---

### 2026-03-09 — Templates folder refreshed to current project conventions

- `control-standards/templates/README.md` — rewritten to match the current repo structure and actual available templates.
- `control-standards/templates/md_headers/` — refreshed `rag_approved_header.md` and `draft_only_header.md`, and added `archived_header.md` in the current metadata style.
- `control-standards/templates/checklists/checklist_template.md` — added a real checklist starter.
- `control-standards/templates/design_guides/design_guide_template.md` — added a design-guide starter.
- `control-standards/templates/reports/report_template.md` — added a report starter.
- `control-standards/templates/work_notes/work_note_template.md` — added a work-note starter for transcript-derived and normalized source notes.

---

### 2026-03-09 — Pre-power commissioning checklist promoted from work note

- `control-standards/work/design/check_this.md` — normalized as a commissioning source note for pre-power panel and incoming-supply verification.
- `control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md` — added a new pre-power checklist covering incoming supply, upstream protection, panel inspection, grounding/bonding, staged energization, and stored-energy awareness.
- `control-standards/rag/commissioning_checklists/README.md` and `checklists/README.md` — updated to reflect the expanded checklist set.
- `control-standards/rag/commissioning_checklists/checklists/_index.yaml` — updated with the new pre-power checklist.

---

### 2026-03-09 — Fundamentals training modules expanded from circuit-analysis source set

- `control-standards/rag/training_modules/fundamentals/` — added seven missing fundamentals modules covering circuit language, series/parallel methods, Kirchhoff laws, equivalent-circuit methods, electrical equations, passive components, and diode/transistor switching basics.
- `control-standards/rag/training_modules/fundamentals/README.md` — updated to reflect the expanded fundamentals module set.
- `control-standards/rag/training_modules/fundamentals/_index.yaml` — updated with the new module list.

---

### 2026-03-09 — Electrical integration design and implementation docs rewritten

- `docs/plans/2026-03-08-electrical-intelligence-integration-design.md` — replaced the obsolete `electrical_intelligence/` parallel-layer design with the current canonical architecture using `training_modules`, `design_framework`, `commissioning_checklists/checklists`, and `standards_intelligence`.
- `docs/plans/2026-03-08-electrical-intelligence-integration-plan.md` — replaced the stale implementation plan with a current executable backlog focused on the remaining circuit-analysis promotions and current validation constraints.

---

### 2026-03-09 — Electrical integration requirements doc added

- `docs/plans/2026-03-08-electrical-intelligence-integration-requirements.md` — added a concrete requirement list covering architecture, source readiness, metadata, target files, engineering-rule constraints, validation, and acceptance criteria for rewriting the Phase 11 electrical integration docs.

---

### 2026-03-09 — Missing electrical-intelligence components promoted into current RAG architecture

- `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/` — added a normalized source package from `electrical exam prep.md`, including README and integration guidance based on the source's real content.
- `control-standards/rag/training_modules/` — added root README/index plus new `electrical_machines/` and `nec_application/` submodules with induction-motor, DC-motor, nameplate/slip/torque, NEC code-reading, table-navigation, and article-routing modules.
- `control-standards/rag/design_framework/electrical_review/` — added quick electrical review workflows for Ohm's law, resistive networks, component selection, and simple interface circuits.
- `control-standards/rag/design_framework/motor_systems/` — added motor selection, nameplate review, star/delta supply matching, and VFD integration review notes.
- `control-standards/rag/commissioning_checklists/` — added root README/index plus starter field checklists for circuit polarity/power, capacitor discharge awareness, and motor startup verification.
- `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/` — added the previously missing `motors_drives` overlap notes for UL 508A/NEC/NFPA 79 and NFPA 79/IEC 60204-1 routing.

---

### 2026-03-09 — Design framework minimum viable set created

- `control-standards/rag/design_framework/README.md` — added module purpose and scope note.
- `control-standards/rag/design_framework/_index.yaml` — added seeded-content index for the design framework.
- `control-standards/rag/design_framework/design_guides/02_power_distribution_guide.md` — added applied power-distribution workflow guide.
- `control-standards/rag/design_framework/constraints/grounding_bonding_rules.yaml` — added reusable grounding and bonding ruleset.
- `control-standards/rag/design_framework/us_eu_compliance_wizard/` — added wizard README, spec, rules, and delta-report template to satisfy existing internal references.

---

### 2026-03-09 — Google tag added sitewide

- `docs/_layouts/default.html` — added the Google tag (`gtag.js`) snippet in `<head>` with measurement ID `G-RPL3G47EFZ`, which applies to every page using the default Jekyll layout.
- `project_state/project_state.md` — updated current-state tracking to record sitewide analytics installation.
- `project_state/environment.md` — recorded the active measurement ID and layout location for site analytics.
- Corrected the documented live GitHub Pages URL to `https://kyawminthu20.github.io/Control-System-Tools/`.

---

### 2026-03-09 — Conductor ampacity topic promoted into standards and training

- `control-standards/rag/training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md` — new fundamentals training module covering ampacity, bundling, ambient correction, terminal temperature limits, and protection logic.
- `control-standards/rag/training_modules/fundamentals/README.md` — new fundamentals training-module index note.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md` — corrected the Article 240.4 conductor-protection reference and expanded the conductor/OCPD coordination workflow.
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md` — replaced placeholder artifacts with cleaner ampacity, current-carrying-conductor, and termination-temperature guidance.

---

### 2026-03-08 — UL 508A website update: scenario and lifecycle pages

- `docs/scenarios/us-industrial-control-panel/index.md` — major rework: 4 thin engineering decisions expanded to 12 topic-aligned decisions covering listing basis, enclosures, layout, spacing/creepage, wiring, SCCR (weakest-link), grounding, control circuits, motor controllers, transformers, marking, and E-stop; added inspection readiness checklist table.
- `docs/lifecycle/detailed-design/index.md` — key activities updated: old UL section number references replaced with descriptive topic references; SCCR bullet expanded with weakest-link logic; spacing/creepage bullet improved; deliverables table updated to match current RAG module names.

---

### 2026-03-08 — UL 508A spacing/creepage/clearance module populated

- `UL508A_2022__spacing_creepage_clearance.md` — populated from project working note: clearance vs creepage definitions, voltage-based heuristics (0–150 V, 151–300 V, 301–600 V), live parts review logic, mitigation methods (barriers, finger-safe, routing, layout), field inspection failure patterns.
- `docs/standards/us-electrical/ul-508a/index.md` — topic table updated (removed "in progress" marker); spacing/creepage section added between Enclosures and Wiring Methods.
- All 11 UL 508A RAG modules now populated.

---

### 2026-03-08 — UL 508A RAG populated; website updated

- All 11 UL 508A RAG modules filled from `_TODO_` to substantive practical guidance (10 populated; `spacing_creepage_clearance` still TODO).
- `docs/standards/us-electrical/ul-508a/index.md` — major rework: RAG-aligned topic table, practical topic sections for all 10 populated modules, expanded SCCR weakest-link section, marking/documentation section.
- `docs/crosswalks/ul508a-nec-nfpa79/index.md` — minor: expanded grounding row with safety vs noise grounding distinction.
- `docs/lifecycle/build/index.md` — expanded panel build activity into detailed UL 508A build checklist (layout, wiring, grounding, enclosure integrity, SCCR, nameplate).

---

### 2026-03-08 — Phase 11 Complete: Industry Overlay Depth

- `docs/industries/petroleum/index.md` — full reference page: standards matrix by phase, selection flow, checklist; all gap badges removed
- `docs/industries/semiconductor/index.md` — full reference page: SEMI badges updated to complete, applicability matrix, SEMI S2 compliance flow
- `docs/scenarios/oil-gas-process-skid/index.md` — Scenario 07: onshore O&G ESD/F&G/HIPPS with IEC 61511 + IEC 60079 + NEC workflow, Mermaid SIS diagram, engineering decisions
- `docs/scenarios/semiconductor-fab-tool/index.md` — Scenario 08: etch/CVD fab tool with SEMI S2/S14 gas control system, Mermaid interlock diagram, engineering decisions
- Scenarios index and sidebar updated with new entries

---

### 2026-03-08 — Phase 10 Complete: IEC 60079 + SEMI Corpus Gap-Fill

#### IEC 60079 (Hazardous Area)

- 6 new RAG files: Parts 0, 1, 10-1, 11, 14, 17
- \_index.yaml indexing all 6 parts
- 2 site pages: hazardous-area family landing + IEC 60079 standard page

#### SEMI S2/S8/S14 (Semiconductor Equipment Safety)

- 3 new RAG files: S2 (equipment safety), S8 (ergonomics), S14 (fire risk)
- \_index.yaml indexing all 3 standards
- 2 site pages: semiconductor family landing + SEMI S2/S8/S14 detail page

#### Site updates

- docs/standards/index.md: added Hazardous Area + Semiconductor sections
- docs/scenarios/semiconductor-equipment/index.md: added SEMI/IEC 60079 links, upgraded badges

---

### 2026-03-08 — Phase 9 Complete: Interactive Standards Graph

- Added `docs/_data/standards_graph.yml` — 12 nodes (6 families), 14 edges (4 types)
- Added `docs/_includes/standards-graph.html` — Cytoscape.js 3.28.1, parameterized mini/full
- Added `/standards/graph/` full page with zoom, pan, hover highlights, edge tooltips
- Homepage Mermaid block replaced with mini Cytoscape graph (preset layout, click-navigable)
- Edge types: requires (amber), pairs-with (blue), enforces (green), aligns-with (gray)
- Planned nodes (IEC 60079, SEMI) shown as dashed/dimmed — auto-activate when corpus added
- NEC page: readability overhaul (TOC, quick-reference callout, scope/limitations merge, 2026 section as change-log cards with impact levels + engineer takeaways, phased workflow)
- NEC page: technical improvements (Art. 240 added, SCCR critical rule + 4 determination methods, Art. 670 scoped to facility connection only, standards table updated)

---

### 2026-03-08 — Phase 10 Queued: IEC 60079 + SEMI Corpus Gap-Fill

**Type:** Planning
**Status:** NOT STARTED — begin next session

- Plan doc: `docs/plans/2026-03-08-phase10-corpus-gap-fill.md`
- **IEC 60079 (6 RAG files):** Parts 0, 1, 10-1, 11, 14, 17 → `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/`
- **SEMI S2/S8/S14 (3 RAG files):** → `control-standards/rag/standards_intelligence/us/semi/`
- **Site pages:** `/standards/hazardous-area/` family + `/standards/hazardous-area/iec-60079/`; `/standards/semiconductor/` family + `/standards/semiconductor/semi/`
- **Standards index:** add Hazardous Area and Semiconductor sections
- **NEC polish:** rename table column, verify 409.70/670.6, clean up nec_update.md
- Full task list with file paths in `project_state/project_state.md` Phase 10 section

---

### 2026-03-08 — Phase 8 Complete: NEC RAG Corpus Expanded to 19 Articles

**Type:** RAG Corpus / Content
**Status:** Complete

- Added Art 90 (scope and purpose) — NEC jurisdiction limits, AHJ authority, adoption process
- Added Art 100 (definitions) — authoritative NEC terminology (listed, labeled, SCCR, grounded conductor, EGC)
- Added Art 215 (feeders) — feeder conductor sizing, 125% continuous load rule, OCPD coordination
- Added Art 230 (services) — available fault current, service disconnect, neutral-to-ground bond rule
- Added Art 250.4 (grounding purposes) — synthesized from NEC 250.4 + Mike Holt 2020; system vs equipment grounding, GEC routing
- Added Art 500 (hazardous locations general) — Class I/II/III, Division 1/2, T-codes, explosion-proof equipment
- Added Art 504 (intrinsically safe systems) — IS design rules, zener barriers, galvanic isolators, FISCO model
- Added Art 505 (Zone 0/1/2) — IEC-aligned zone system, ATEX/IECEx equipment acceptance, EPL markings
- Added Art 700–702 (emergency/standby) — three-tier power architecture, transfer times, ATS requirements, safety system coordination
- Updated \_index.yaml: 19 articles now indexed (was 12); coverage_notes.complete updated
- Updated NEC_COMPLETION_STATUS.md: 19/19 articles complete (~9,500 words)
- Updated NEC_OVERVIEW.md: new sections for General, Power Distribution, Hazardous Locations, Emergency Power

**NEC corpus now covers:** general/definitions, power distribution, grounding, hazardous locations (Class/Division + Zone), IS systems, emergency power, industrial control panels, motors, conductors, wiring methods, overcurrent protection

---

### 2026-03-08 — NEC RAG Gap-Fill: Art250.4 Added

**Type:** RAG Corpus / Content
**Status:** Partial (250.4 complete; 409.70, 670.6 outstanding)

- Created `NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md` — synthesized from NEC 250.4 code text and Mike Holt 2020 instructional content. No verbatim NEC text. Covers: system grounding vs equipment grounding, bonding vs grounding distinction, effective ground-fault current path, GEC routing rationale (inductive reactance / skin effect), grounded and ungrounded system differences, common engineering errors.
- Updated `_index.yaml`: registered NEC2023-Art250-4 entry using `note` field (valid); corrected `coverage_notes.complete` to list all 13 article files actually present in the corpus.
- Source file: `control-standards/archive/superseded_designs/work_design/promoted_to_rag/Grounding, System and Equipment [250.4, 2020 NEC].md` (raw transcript — not committed to RAG).
- Remaining gaps: Art409.70 (surge protection) and Art670.6 (overvoltage protection) referenced on NEC site page but no dedicated RAG sub-files.

---

### 2026-03-08: Dark Mode / Theme Switching Added

**Type:** UX / CSS
**Status:** Complete

- Added CSS custom property variables for all previously hardcoded colors (topnav, cards, table stripes, lifecycle stages)
- Added `[data-theme="dark"]` token block and `@media (prefers-color-scheme: dark)` fallback
- Added inline flash-prevention script in `<head>` — resolves theme before first paint
- Added theme toggle button (☾/☀) to topnav
- Added toggle handler in `main.js` with `localStorage` persistence
- Default: follows OS `prefers-color-scheme`; user override saved across sessions
- Build clean

---

### 2026-03-08 — Standards Decision Workflow Enhancements

- Added `last_reviewed` and `standards_editions` to front matter
- Added Purpose section with audience list and standards scope table
- Added sequential Lifecycle Workflow Mermaid diagram
- Added decision questions (key question + outputs) to Steps 1–3
- Added Standard Scope Boundaries table (NFPA 79 / UL 508A / NEC)
- Added Common Engineering Mistakes section (6 items)
- Added Typical Machine Compliance Stack table with editions
- Added Worked Example — Automated Conveyor System
- File: `docs/crosswalks/standards-decision-workflow/index.md`

---

### 2026-03-08: Glossary Page Added

**Type:** Content / Reference
**Status:** Complete

- Added `docs/_data/glossary.yml` with 28 seed terms (SIL, PL, SL, SCCR, AHJ, HFT, SFF, MTTFd, DC, Category, PFH, PLC, SIS, SIF, LOPA, E-stop, AFC, AIC, VFD, SPD, NEC, NFPA, UL, IEC, ISO, SEMI, CE, OSHA)
- Added `docs/glossary/index.md` — A-Z anchor navigation, domain badges, cross-links to standard pages, lifecycle stages, and related terms
- Added glossary card CSS and domain badge color variants to `main.css`
- Added Glossary to Reference section in sidebar
- Build clean

---

### 2026-03-08: NEC Page — Compliance-Focused Update

**Type:** Content / Standards
**Status:** Complete

- Added "Use This Page For" section clarifying NEC scope vs NFPA 79, UL 508A, ISO 13849-1
- Added "What the NEC Does Not Cover" section (PL, SIL, safety arch, stop categories)
- Expanded Key Articles table: added Article 300, 409.70 (surge protection), 670.6 (overvoltage protection)
- Tightened Article 409 SCCR language — UL 508A SB is one approved method, not the only path
- Softened Article 670 / NFPA 79 relationship language to be more accurate
- Added adoption warning callout (AHJ edition verification)
- Added "Typical Machine Builder Workflow" step sequence
- Added "Machine Builder Compliance Checklist" (8-point pre-installation checklist)
- Replaced ASCII relationship diagram with a proper standards table and summary blockquote
- Build: 52 pages, clean

---

### 2026-03-08 — Phase 5 Complete: IEC 62443 Cybersecurity Corpus and Site Pages

**Summary:** IEC 62443 cybersecurity corpus created from scratch (no prior RAG files). Full site page with Zone/Conduit diagram, SL table, FR overview, SIL vs SL distinction, and safety checklist. Cybersecurity family index created. Standards index updated. Networked Safety PLC scenario updated.

**What changed:**

- Created `control-standards/rag/standards_intelligence/international/cybersecurity/iec_62443/` — new directory
- Created `_index.yaml` — corpus index
- Created `IEC62443_2_1__security_management.md` — CSMS, risk assessment process, asset inventory, policy elements, IT vs OT distinctions
- Created `IEC62443_3_3__system_security_requirements.md` — Zone/Conduit model, SL 1–4 definitions, SL-T/SL-C/SL-A, FR 1–7, selected SR table, safety Zone guidance
- Created `IEC62443_4_2__component_requirements.md` — four component types (ED/SA/HD/ND), SL-C concept, selected requirements by component, secure development (4-1), component selection guidance
- Created `IEC62443_lifecycle.md` — Assess/Implement/Maintain lifecycle, SL designation lifecycle perspective, IACS patch management procedure, incident response for OT, functional safety coordination points
- Created `docs/standards/cybersecurity/iec-62443/index.md` — full site page: SL table, SIL vs SL section, Zone/Conduit Mermaid diagram, FR overview, lifecycle flowchart, safety/security coordination table, practical checklist
- Created `docs/standards/cybersecurity/index.md` — cybersecurity family page with routing table and out-of-scope gaps documented
- Updated `docs/standards/index.md` — added Cybersecurity Standards section
- Updated `docs/scenarios/networked-safety-plc/index.md` — added IEC 62443 to related_standards; updated badge to Phase 5 Complete; updated routing note to link to IEC 62443 detail page
- Jekyll build clean — 52 pages

**Phase 5 status: COMPLETE**

---

### 2026-03-07 — Phase 4 Complete: Practical Safety Guides

**Summary:** Two new site pages added sourcing content from `control-standards/work/design/simple_safety_system_design.md`. No RAG changes.

**What changed:**

- Created `docs/scenarios/machine-safety-implementation/index.md` — Scenario 06: Practical Machine Safety Implementation. 10-step workflow (risk assessment → safety functions → architecture → device selection → wiring → safety logic → validation), SIL/PL equivalence table, Category B/1/2/3/4 selection table, example hydraulic+chemical machine safety stack, Mermaid input→PLC→output and Category 3 architecture diagrams.
- Created `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices lifecycle page. 24 VDC SELV rationale, NC contact fail-safe logic, dual-channel separation requirements, diagnostic test pulse explanation, discrepancy time (20–100 ms), wire gauge (18 AWG default), insulation rating, NFPA 79/UL 508A color coding, ferrule and spring-clamp termination guidance, baseline dual-channel input specification table.
- `docs/scenarios/index.md` — added Scenario 06 card
- `docs/lifecycle/index.md` — added safety-wiring row to stage table
- `docs/lifecycle/safety-architecture/index.md` — added See Also link
- `docs/lifecycle/detailed-design/index.md` — added See Also link
- Jekyll build clean.

**Phase 4 status: COMPLETE**

---

### 2026-03-07 — Phase 3 Complete: IEC 61511 RAG Corpus and Site Page

**Summary:** IEC 61511 RAG corpus created and site page rewritten with Phase 3 Complete badge. Phase 3 is now fully complete across all four functional safety standards.

**What changed:**

- Created `control-standards/rag/standards_intelligence/international/functional_safety/iec_61511/_index.yaml`
- Created `IEC61511_2016__Part1__framework.md` — SIS/SIF concepts, three-part structure, lifecycle overview, IEC 61508 relationship, prior use clause, ISA 84 equivalence
- Created `IEC61511_2016__Clause08__sil_determination.md` — HAZOP inputs, LOPA equation, IPL credits, tolerable risk targets, worked LOPA example, risk graph overview, FTA, common mistakes
- Created `IEC61511_2016__Clause10__sis_design.md` — PFDavg equation, redundancy architectures (1oo1/1oo2/2oo3), sensor and final element design, logic solver selection, prior use clause, SRS contents
- Created `IEC61511_2016__Clause16__operation_maintenance.md` — proof testing theory, proof test coverage, bypass management, functional safety audit, modification (MOC) process, decommissioning
- Rewrote `docs/standards/functional-safety/iec-61511/index.md` — badge updated to Phase 3 Complete; added Quick Start, SIL/PFDavg table, LOPA overview with IPL credits, PFDavg calculation table, architecture comparison table, prior use clause, IEC 61511 vs machinery comparison table, common mistakes, practical checklist, lifecycle application table

**Phase 3 status: COMPLETE** — ISO 13849-1, IEC 62061, IEC 61508, IEC 61511 all done.

---

### 2026-03-06 — Phase 4 Queue Defined: Practical Safety Guides

**Summary:** Identified two new site pages to implement after Phase 3 completes, sourced from `control-standards/work/design/simple_safety_system_design.md`.

**What changed:**

- Added Phase 4 queue to `project_state/project_state.md`
- New untracked design file: `control-standards/work/design/simple_safety_system_design.md`

**Planned pages:**

- `docs/scenarios/machine-safety-implementation/index.md` — Practical Machine Safety Implementation (Scenario 05)
- `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices lifecycle stage

**No RAG changes required** — source doc already in `control-standards/work/design/`.

---

### 2026-03-06 — Phase 3 Group 2: IEC 62061 RAG Corpus and Site Page Complete

**Summary:** Full IEC 62061 RAG corpus created; site page rewritten with Phase 3 Complete badge and detailed content. DC vs SFF distinction clarified post-review.

**What changed:**

- Created `control-standards/rag/standards_intelligence/international/functional_safety/iec_62061/` corpus (Clause 06, 07, 08, Annex B, plus index)
- IEC 62061 Clause 07 fix: corrected DC labels and clarified DC vs SFF distinction
- Deepened `docs/standards/functional-safety/iec-62061/index.md` — badge updated to Phase 3 Complete
- ISO 13849-1 site page: removed Annex B stub reference, corrected RAG status, clarified PLr table

**Phase 3 status after this group:** ISO 13849-1 complete, IEC 62061 complete. IEC 61508 and IEC 61511 remain.

---

### 2026-03-06 — Phase 3: ISO 13849-1 RAG Corpus and Site Page Complete

**Summary:** Full ISO 13849-1 RAG corpus created; site page rewritten with Phase 3 Complete badge and detailed content.

**What changed:**

- Created `control-standards/rag/standards_intelligence/international/functional_safety/iso_13849_1/_index.yaml` — corpus index listing all 6 files
- Created `ISO13849_2023__Clause04__design_strategy.md` — design strategy, safety function specification, PL level table, ISO 12100 relationship
- Created `ISO13849_2023__Clause05__srp_cs.md` — MTTFd, DC, CCF parameters; PL lookup table; PFHd and SIL equivalence
- Created `ISO13849_2023__Clause06__categories.md` — Categories B/1/2/3/4 requirements, summary table, common architecture examples
- Created `ISO13849_2023__Clause07__validation.md` — validation plan, FMEA, functional testing, fault exclusion, documentation requirements
- Created `ISO13849_2023__AnnexA__risk_assessment.md` — S/F/P parameters, full PLr table, worked example, PLe conditions
- Created `ISO13849_2023__AnnexF__ccf.md` — CCF definition, Annex F scoring table, path to 65 points, common pitfalls
- Deleted `file_structure.md` placeholder
- Rewrote `docs/standards/functional-safety/iso-13849-1/index.md` — 224 lines; badge updated to Phase 3 Complete; added Quick Start, full PLr table, PL/PFHd table, design parameters table, Category architecture table, worked E-stop example, PL vs SIL comparison, 6 common mistakes, practical checklist, lifecycle application table

### 2026-03-06 — Phase 2 Implementation Complete

**Summary:** All Phase 2 features implemented and committed to master.

**What changed:**

- `docs/assets/css/main.css` — full `@media print` block (hide nav/sidebar/context, full-width content, URL-after-links, page-break rules); diagram lightbox styles; lunr.js search dropdown styles; crosswalk comparison selector styles
- `docs/assets/js/main.js` — diagram lightbox IIFE (click `.mermaid` → full-screen SVG clone, close via ×/Escape/click-outside); lunr.js search IIFE (fetch search.json, index on load, arrow-key nav, XSS-safe DOM building)
- `docs/_layouts/default.html` — lunr.js CDN script tag added before `</body>`
- `docs/_includes/topnav.html` — search input with ARIA attributes and `data-search-url`
- `docs/assets/data/search.json` — new Jekyll Liquid template; renders valid JSON search index at build time
- `docs/crosswalks/compare/index.md` — new comparison selector page; two `<select>` dropdowns; hidden pair divs for NFPA79/IEC60204 and US electrical trio; vanilla JS selector logic
- `docs/crosswalks/index.md` — compare link added to crosswalk table

**Architecture:** All additive. Vanilla JS + CSS only. No new Jekyll plugins. CDN-only dependency (lunr.js).

**Next step:** `git push` then enable GitHub Pages (Settings → Pages → Source: GitHub Actions).

### 2026-03-06 — Phase 1 Jekyll Site Implementation

**Summary:** Built the complete Phase 1 GitHub Pages static site under `docs/`.

**What changed:**

- Created `docs/` Jekyll scaffold with `_config.yml`, `Gemfile`, and vendor bundle (Ruby 2.6 / Bundler 2.4.22 local)
- Built three-panel layout: CSS Grid (240px sidebar + 1fr main + 220px context), responsive to tablet/mobile
- Mermaid.js CDN integration (theme: neutral) in default layout
- 48 HTML pages across all planned sections
- GitHub Actions workflow at `.github/workflows/pages.yml` (deploys from master branch)
- Updated `.gitignore` to exclude `docs/_site/`, `docs/vendor/`, `docs/.jekyll-cache/`

**Site sections implemented:**

- Homepage: 8 content blocks (hero, standards cards, lifecycle ribbon, relationship diagram, industry matrix, scenarios, repo explorer, trust boundary)
- Standards: explorer landing, US Electrical (NEC, NFPA 79, UL 508A), International Machinery (IEC 60204-1), Functional Safety (ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511)
- Lifecycle: landing + 11 stage pages
- Crosswalks: NFPA 79 ↔ IEC 60204-1, UL 508A/NEC/NFPA 79, Decision Workflow
- Scenarios: 5 pages (US Control Panel, Global Machine, Process Skid, Networked Safety PLC, Semiconductor Equipment)
- Industries: matrix landing + 9 industry overlay pages
- Software Stack, About

**Architecture decision:** Jekyll static site with custom CSS (no framework). Content sourced from RAG corpus paraphrase. `docs/` is presentation only — never modifies `rag/`.

**Next step:** Commit, push, enable GitHub Pages in repo settings (Source: GitHub Actions).

### 2026-03-06: Commit Automation Retargeted To Project-State Log

**Type:** Automation / Workflow
**Status:** Active

- Updated the Git hook installer and the installed pre-commit hook to stage `project_state/change_log.md` instead of the removed root `general_change_log.md`.
- Kept `project_state/change_log.md` as a manual project log instead of using it as an auto-generated generation-summary feed.
- Aligned project runbook and tooling docs with the new project-state tracking path.

### 2026-03-06: Project-State Workflow Established

**Type:** Documentation / Process
**Status:** Active

- Established `project_state/` as the operational tracking area for this project.
- Defined file ownership:
  - `project_state.md` for current phase, scope, and next implementation work
  - `environment.md` for runtime and deployment requirements
  - `how_to.md` for setup and run instructions
  - `change_log.md` for project-level change tracking
- Updated root documentation so the project state is discoverable from the repository root.
- Set the current delivery target to Phase 1 GitHub Pages deployment for personal use.

### 2026-03-05 — Phase 2 Planning Docs Added

**Type:** Planning / Documentation
**Status:** Active

- Added Phase 2 design doc: `docs/plans/2026-03-05-phase2-design.md`
- Added Phase 2 implementation plan: `docs/plans/2026-03-05-phase2-implementation.md`
- Features planned: print stylesheet, diagram lightbox, lunr.js inline search, crosswalk comparison selector
- Architecture: all additive changes to existing files; vanilla JS + CSS only; no build step; CDN-only deps
- Implementation structured as 2 releases (Release 1: print + lightbox; Release 2: search + comparison)

### 2026-03-05: Repository Reorganization Executed

**Type:** Structure
**Status:** Completed

- Consolidated the repository under `control-standards/` as the clear product root.
- Kept `control-standards/rag/` as the authoritative AI-readable knowledge path.
- Grouped standards content under `us/`, `international/`, and `crosswalks/`.

### 2026-01-15: Legacy Migration Tooling Created

**Type:** Historical Infrastructure
**Status:** Historical

- Migration helper scripts and migration documentation were created for an earlier repository layout.
- These records remain useful as project history but are not the primary workflow for the current structure.

## Notes

- Older migration and generation details remain available elsewhere in the repository as historical context.
- This file should stay focused on the active project and current implementation effort.

## 2026-03-11 — Phase 17: Cross-Layer Knowledge Routing

- Added `/workflows/` as first-class site section (Option A decision)
- 5 workflow pages: Motor Selection, Motor Troubleshooting, VFD Commissioning, Servo Commissioning, Electrical Review
- Extended training_catalog.yml: `related_workflows` field on 7 modules; Machine Lifecycle learning path added
- training-module.html layout updated to render Related Workflows block
- Sidebar Workflows section added (5 direct links)
- Workflow CSS: card grid, badges, wf-tags, related-workflows block
- Jekyll build: clean, 0.583 s, 107 pages
