# Project State

**Last Updated:** 2026-07-11 (Phase 44 COMPLETE — Communications expansion; roadmap build phases done)
**Status:** Active
**Current Phase:** Phase 44 COMPLETE — communications expansion live: EtherCAT, HART, DNP3, IEC 61850 (comms section now 22 pages, new Utility & Substation group). **All named roadmap build phases (38-44) are complete.** Remaining work is standing threads only: author review passes (Review pending -> Reviewed across the many AI-drafted pages), Phase 30.3-30.8 standards depth, cst data hand-offs (licensed NEC tables / real I/O list / Saleae captures / live PLC), original SVG diagrams, and future comms items (Foundation Fieldbus, wireless, TSN, sanitized capture library). Earlier: Phase 43 (IEC 61131-3), Phase 42 (troubleshooting), Phase 41 (wiring program), Phases 38-40 COMPLETE — repo-wide standards codified in `governance/` (PROJECT_ORGANIZATION, CONTENT_STANDARDS, ENGINEERING_STANDARDS, AI_WORKFLOW), with AGENTS.md/CLAUDE.md rewired as binding entry points: any agent or AI working here must read and follow them. Earlier same-day: Phase 35.3 COMPLETE — physical-layer tier added to communications (copper Ethernet, fiber optics, RS-485 physical layer; 18 pages + index in the section now), honoring the review's physical-layer-before-more-protocols guidance. Phase 35.4 backlog: diagrams, EtherCAT/DNP3/IEC 61850/HART/wireless/TSN, capture library. Earlier same-day: Phase 35.2 COMPLETE — communications section deepened per the second review's "add next" tier: Wireshark fundamentals page (capture-vs-display filters, Expert Info, capture hygiene), end-to-end case study (intermittent EtherNet/IP dropout, constructed example, methodology demonstrated step-by-step), illustrative config examples (EtherNet/IP table + Modbus 40001-vs-offset-0), protocol-specific Wireshark workflows on 4 pages, 6 network-documentation templates. Phase 35.3 backlog: physical-layer pages, diagrams, EtherCAT/DNP3/IEC 61850/HART/wireless/TSN, capture library. Earlier same-day: Phase 35.1 COMPLETE — second external review of the communications section validated and applied: technical corrections (protocol stack statement, MAC, PROFINET identity), honest review-metadata semantics (Last content update + Technical validation row on unreviewed pages), landing-page comparison table + task paths, grouped nav, ring-buffer captures, switch-counter table. Mermaid-broken claim was again a non-JS-scraper false positive (live-browser verified). Phase 35.2 backlog recorded in change_log (Wireshark fundamentals page, config examples, case study, physical-layer pages, comms templates, more protocols). Earlier same-day: Phase 36 COMPLETE — curated manufacturer directory at `/tools/manufacturers/` (5 categories, 127 vendors, data-driven from `_data/manufacturers/*.yml`, inclusion-is-not-endorsement framing). ALL review-derived phases (31–36) are now done. Open threads are user-driven: author review of the 12 communications pages (Review pending → Reviewed), content track Phase 30.3+ (IEC 60204-1 depth etc.), cst data hand-offs (licensed NEC tables, real I/O list, Saleae captures, live-PLC exercise). Earlier same-day: Phase 35 COMPLETE — new top-level `/communications/` section (12 pages + index): Ethernet fundamentals, managed switches, EtherNet/IP, Modbus TCP, PROFINET, OPC UA, BACnet/IP, Modbus RTU/RS-485, PROFIBUS DP, IO-Link, diagnostics methodology, packet-capture methods. All pages carry review blocks at 'Review pending' until author-reviewed against the governing specs. Remaining from review roadmap: Phase 36 (curated manufacturer directory). Earlier same-day: Phase 34 COMPLETE — engineering templates surface at `/tools/templates/` (7 cst-generated + 12 original static templates, adapt-before-use) and the Python toolkit publicly documented at `/tools/engineering-toolkit/` ("document, don't port"). `tools/generate_site_templates.py` regenerates the published examples. Review roadmap remaining: Phase 35 (Industrial Communications 12-page first release), Phase 36 (curated manufacturer directory). Earlier same-day: Phase 33 COMPLETE — per-page review-information boxes on all 12 standards pages (edition, 5-term status, coverage, last reviewed), the general controls project lifecycle separated from the functional-safety lifecycle (`/lifecycle/general/` + retitled safety-lifecycle index with overlay callout), and a numbered stage-strip navigation with you-are-here marker on every lifecycle stage page. Review roadmap remaining: Phase 34 (templates/tools surface), 35 (Industrial Communications), 36 (manufacturer directory). Earlier same-day: Phase 32 COMPLETE — from the external site review (`planning/2026-07-10-external-site-review.md`): site identity renamed to **Control Systems Engineering Field Guide** (brand "CS Field Guide"; URL unchanged); 5-term public status vocabulary replacing Complete/TO VERIFY/NOT IN CORPUS across 33 site pages (corpus mirror keeps internal flags); repo-tree removed from homepage; context panel and trust boundary de-jargonized; overconfident lifecycle language calibrated; applicability caveat under the Quick Decision table; About page rewritten with author bio, non-affiliation, honest AI-assisted-methodology statement, corrected Known Gaps (old table was 3+ months stale-pessimistic), and issue-reporting links. Review roadmap continues: Phase 33 (page metadata + dual-lifecycle separation), 34 (templates/tools surface from cst), 35 (Industrial Communications 12-page first release), 36 (curated manufacturer directory). Earlier same-day: Phase 31 COMPLETE — site information architecture unified into 7 intent-based sections (Home · Fundamentals · Standards · Design · Lifecycle · Industries · Tools), with the top nav and sidebar finally telling the same story. All 14 lifecycle stages + the journey page now live together under `/lifecycle/` in chronological order (previously split across Implementation and Verification); the NEC course moved from the stub Training section into Fundamentals; Scenarios and Troubleshooting moved under Tools; Repository/About became `/about/`. 49 pages moved with `redirect_from` on every one (Phase 26 pattern; 16 self-redirect conflicts from pages returning to their pre-Phase-26 homes were detected and stripped); 133 files link-swept; zero broken internal links and zero references to old URLs in the built site. Old section indexes are `redirect_to` stubs. Earlier same-day: Tools Suite Phase 4 COMPLETE — `cst.plc` (tag DB with IEC 61131-3 identifier validation, tags-from-I/O generator, Modbus register maps, pycomm3 read/verify helpers as `--extra plc`), `cst.diagnostics` (stdlib SBM-style anomaly detection with per-sensor fault localization; Saleae Logic 2 post-processing: pulse stats, glitch finder, x4 quadrature decode), `cst.docgen` (design-package assembler stitching I/O summary + BOM + wire schedule + nameplate + cited calc results into one markdown document). The 4-phase Tools Suite roadmap from the 2026-07-10 audit is now fully built. Earlier same-arc: Phase 3 COMPLETE — `cst.panel` (I/O list model/validation, BOM with spare-capacity math, tag-suffix wire/terminal schedule, legend + NFPA 79 Ch. 19 nameplate content) and `cst.commissioning` (per-point loop test sheets with 5-point analog checks, FAT/SAT protocol skeleton), all driven from one I/O-list CSV (`data/examples/io_list_example.csv` is the worked example). 115 tests pass; 6 new CLI subcommands (io-check / bom / wire-schedule / legend / loop-sheets / fat). Earlier same-arc: Phase 2 COMPLETE — `cst.calc` now covers ampacity with corrections (NEC 310.15), the full Art. 430 motor branch-circuit chain, transformer OCPD limits (Table 450.3(B)), panel SCCR weakest-link (UL 508A SB4), and fault current (infinite-bus + Bussmann point-to-point). Rule logic and CLI are complete; bulk table values load from `data/standards_tables/` (user-supplied) with clearly-marked SAMPLE fixtures for out-of-the-box runs. 97 tests pass. Earlier same-arc milestones: Phase 1 COMPLETE — the repository now has a second track alongside the content site: an installable Python package (`src/cst/`) of standards-cited engineering calculators. Phase 0 (hygiene) fixed the STRUCTURE_SUMMARY bloat bug, the 2 broken homepage links, the stale RAG→site mirror, and untracked the 168 MB third-party course material under `planning/Python/`. Phase 1 shipped the package spine (`cst.common`: units / citation framework / licensed-table loader) plus three zero-data-dependency tools: voltage drop + minimum-wire-size (NEC K-factor method), encoder scaling (counts↔units↔RPM), and enclosure thermal (IEC/TR 60890-style temperature rise + fan sizing). 50 new tests; 65 total pass via `uv run pytest`. CLI: `uv run cst <voltage-drop|wire-size|encoder|enclosure|fan>`. Branch: `feat/cst-suite`.
**Next Phase:** Content track resumes at Phase 30.3 (IEC 60204-1 depth pass, spec in this file below) — note its file path references predate Phase 31 (`docs/standards/...` unchanged, but any lifecycle links in new content use `/lifecycle/<stage>/`). Tools Suite user-data-dependent hardening still open: (a) licensed table values into `data/standards_tables/`, (b) a real scrubbed I/O list for column_map presets, (c) real historian/Saleae captures for SBM/decode tuning, (d) exercise `cst.plc.comms` against a live controller. Possible future: surface suite documentation on the site (document, don't port).
**Delivery Target:** GitHub Pages static site (content) + importable/installable Python package `cst` (tools), both personal-use first

## Purpose

This file is the source of truth for the current project state, active implementation scope, and near-term backlog.

## Current Direction

Phases 19–22 are complete. Phase 23 (Semiconductor Facility Build Phases 3 & 4) is now complete. The facility reference section covers gas systems, UPW and wastewater, exhaust and abatement, tool-facility interfaces, instrumentation (with 3 sub-pages: device families, vendor families, alarm strategy), commissioning reference, and system/standards crosswalks — all promoted from staging into the RAG corpus and Jekyll site.

All 13 lifecycle stage pages (Stages 1–11 plus Safety Requirements Spec and Management of Change) are now comprehensive engineering references. The lifecycle pages serve as the primary navigation hub for all phases of system development, from initial concept through maintenance.

The site is a presentation and navigation layer on top of `control-standards/rag/`. Authoritative engineering and standards guidance stays in `control-standards/rag/`. The website never modifies RAG content.

Phase 24 Task 1 is complete. The IEC earthing systems training module now includes: a visual summary flowchart showing how each system type handles fault return, compact Mermaid diagrams for each of the five earthing systems (TN-C, TT, TN-C-S, TN-S, IT), per-system blockquote callout cards, "Machine designer takeaway" lines, an expanded practical comparison table, and a selection-logic decision flowchart before the practical questions section. Jekyll build remains clean.

Phase 25 is complete. An 8-page water/wastewater section was added under `docs/industries/water-wastewater/`, covering municipal drinking water treatment and industrial wastewater treatment with Mermaid diagrams on every page. Topics include: overview and standards selection flowchart, intake and raw water pumping, filtration and clarification, chemical dosing, distribution SCADA and telemetry, equalization and neutralization, treatment and discharge compliance, and instrumentation reference. Eight corresponding RAG files were added to `control-standards/rag/design_framework/water_wastewater/`. Standards covered: IEC 61511, IEC 62443, ISA-18.2, AWWA, EPA SDWA/CWA, NFPA 820, NEC.

## Tools Suite Phases 0–1 — COMPLETE (2026-07-10)

New track: grow the repo into a comprehensive engineering tools suite (audit → architecture → phased build, user-approved 2026-07-10). Branch: `feat/cst-suite`. Key architecture decision: **calculation code is committed and open; licensed standard table values are gitignored** (`data/standards_tables/`, schemas committed) — the same copyright boundary the RAG corpus follows.

### Phase 0 — Hygiene (commit c027d72)

- Untracked `planning/Python/` (1,141 Udemy course files, 168 MB — 54 % of all tracked files; copyright exposure on a public remote). **Update 2026-07-10 (later same day):** user approved full removal — history rewritten with `git filter-repo`, course moved to `~/Dev/_archive/udemy-python-bootcamp/`, rewritten master force-pushed, 3 stale merged remote branches deleted. `.git` 171 MB → 5.9 MB. Pre-rewrite mirror backup: `~/Dev/_archive/Control-System-Tools-pre-rewrite-backup.git`.
- `tools/project_automator.py`: IGNORE_DIRS now excludes `.venv`, `docs/vendor`, `docs/_site`, caches — STRUCTURE_SUMMARY.md 600 KB → 99 KB (the pre-commit hook had been re-committing the bloat on every commit).
- Fixed the 2 long-standing broken homepage links (`/industries/food-and-beverage/`, `/industries/offshore/`).
- Excluded internal `docs/plans/` + `docs/superpowers/` from the published site (`_config.yml` exclude).
- `generate_standards_overview.py`: root derived from `__file__` instead of a hardcoded absolute path.
- Deleted 0-byte `tools/generate_rag_index.py` and the retired `_phase26_*` one-shot scripts.
- Re-ran `generate_rag_tree.py`: the 5 BLDC/PMSM corpus files added 2026-04-29 are now mirrored to the site (283 files).

### Phase 1 — Package spine + first calculators

- `src/cst/` installable package (hatchling; `uv sync` installs editable; console script `cst`).
- `cst.common`: `cite.py` (Citation + CalcResult — every result carries standard references and assumptions), `units.py` (ASTM B258 AWG geometry, exact-constant conversions), `tables.py` (loader for user-supplied licensed table JSON; refuses files without a `source` provenance block).
- `cst.calc.voltage_drop`: K-factor method (2·K·I·L/cmil, √3 for 3-phase), NEC 210.19(A)/215.2(A) 3 %/5 % recommendation warnings, inverse minimum-conductor-size search with an explicit "ampacity still governs" warning.
- `cst.motion.encoder`: EncoderScaling dataclass — quadrature, gear ratio, ballscrew lead; counts↔position↔RPM↔linear speed.
- `cst.calc.enclosure_thermal`: effective-surface-area method (IEC/TR 60890 concept, vendor-guide constants exposed as parameters), sealed temperature rise + required fan airflow, 50 °C derating warning.
- `data/standards_tables/`: README + JSON schemas for ampacity and motor-FLC tables. Values are **never committed** — user transcribes from licensed copies.
- Tests: 50 new golden-value tests (`tests/cst/`), 65 total passing including doctests; `pytest` now a declared dev dependency and runs inside the project venv (previously only worked via system Python).
- `pyproject.toml`: dropped redundant `pypdf2` (deprecated predecessor of `pypdf`), added packaging config + `[dependency-groups] dev`.

### Roadmap (remaining)

- **Phase 2** — NEC/UL data-dependent calculators (ampacity w/ corrections, motor branch circuit, transformer, SCCR, short-circuit). Needs user-populated `data/standards_tables/*.json`.
- **Phase 3** — Panel design pipeline (I/O list → BOM → wire/terminal schedule → nameplates) + commissioning generators (loop sheets, FAT/SAT). Needs a sample I/O list as reference fixture.
- **Phase 4** — PLC utilities (tag DB, address map, pycomm3 extra), diagnostics (SBM anomaly detection, Saleae post-processing — needs field data), docgen.

---

## Phase 30.2 — COMPLETE (2026-05-06)

IEC 60079 detail page upgraded from 3/8 to full ISO 13849-1 template-floor compliance. Branch: `feat/phase30-standards-depth-pass`. File: `docs/standards/hazardous-area/iec-60079/index.md` (123 → 364 lines).

### Sections added

- **Quick Start** (5 bullets) — IEC vs NEC Class/Division (Article 505 imports IEC 60079); how to read the marking string; why area classification (60079-10-1) drives every downstream decision; when to choose IS vs Ex d; certificate vs nameplate (certificates can be withdrawn).
- **Equipment Marking System** — kept and expanded: marking string format, EPL→Zone mapping table, gas-group table (IIA propane / IIB ethylene / IIC hydrogen-acetylene), T-code table with the 50 °C autoignition-margin rule.
- **Corpus Coverage** table — new. Lists all major parts of the IEC 60079 family with corpus status: 6 parts in corpus (-0, -1, -10-1, -11, -14, -17), 4 parts gap-flagged (-2 Ex p, -7 Ex e, -10-2 dust, -15 Ex nA, -18 Ex m, -31 dust enclosure). Honest about what the RAG can authoritatively support.
- **Per-Part Depth** for the 6 corpus parts: -0 (general / marking / certification schemes), -10-1 (zone definitions, release grades, ventilation, classified-area drawing), -1 (Ex d flame-path principle, cable entry methods, live-work caution), -11 (IS levels ia/ib/ic, energy limitation, zener vs galvanic isolator, entity concept with full parameter list, FISCO), -14 (equipment-selection check, cable selection, IS segregation, equipotential bonding ≤10 Ω / IS earth ≤1 Ω, commissioning certificate), -17 (visual / close / detailed inspection grades, competent person, common defects, records).
- **Worked Example** — concrete IS-loop entity check on a 4–20 mA pressure transmitter, ethylene Zone 1 (gas group IIB), area drawing requiring at least T3 equipment. Selected components: transmitter `Ex ia IIB T4 Gb` with Ui=30 V / Ii=100 mA / Ci=15 nF / Li=50 µH; zener barrier `[Ex ia] IIC` with Uo=28 V / Io=93 mA / Co=83 nF / Lo=5.7 mH; 100 m IS-rated TP cable at 200 pF/m + 0.7 µH/m. All four entity checks computed and shown to pass: Uo≤Ui, Io≤Ii, Ci+Ccable≤Co (35 nF ≤ 83 nF), Li+Lcable≤Lo (120 µH ≤ 5 700 µH). Marking compatibility verified (IIB matches, T4 colder than T3 minimum, Gb matches Zone 1). Earthing rules and documentation deliverables included.
- **Common Mistakes** (6 numbered) — IIC-by-default equipment shopping; trusting nameplate over certificate; mixing certified / uncertified components in IS loop; failing to segregate IS from non-IS cables; zener barrier with IS earth >1 Ω; field-modifying an Ex enclosure (replaced the plan's Ex e thermal-protection mistake, which would have leaned on a part not in corpus).
- **Practical Checklist** — Area Classification / Equipment Selection / Installation (60079-14) / Periodic Inspection (60079-17) groups.
- **Lifecycle Application table** — Standards Selection → Detailed Design → Build → Installation → Pre-Commissioning → Commissioning, each linking to the corresponding lifecycle-stage page.
- **Relationship to NEC** — replaced the brief table with a fuller mapping (Art. 500–503 parallel; Art. 504 ≈ 60079-11; Art. 505 imports IEC 60079) and linked the existing IEC 60079 ↔ NEC 500–505 crosswalk page.

### Plan vs RAG correction (second occurrence — lesson is sticking)

The Phase 30.2 plan called for per-part depth on **Ex e (60079-7)** and **Ex p (60079-2)**. Neither part is in the RAG corpus — only -0, -1, -10-1, -11, -14, -17 are present. Verified against `_index.yaml` and chapter front-matter before drafting.

Adjustments made:
- Per-part depth covers only the 6 RAG-corpus parts.
- Ex e and Ex p (and other gap parts: -10-2, -15, -18, -31) listed in a new "Corpus Coverage" table with explicit `<span class="badge badge--gap">` markers.
- The plan's Common Mistake #6 (Ex e motor thermal protection) was replaced with a generally-applicable mistake drawn from corpus parts (-1 / -17): field-modifying an Ex enclosure invalidates the certificate.

The IS-loop entity-check math from the plan was verified arithmetically before drafting (Ci+Ccable = 35 ≤ 83 ✓; Li+Lcable = 120 ≤ 5 700 ✓) and presented in the Worked Example as written.

### Validation

- Jekyll build: clean (1.215 s → 1.191 s after one micro-edit; site build unchanged).
- Internal links: all 12 outgoing links from the rewritten page resolve. Same 2 pre-existing site-wide broken links (`/industries/food-beverage/`, `/industries/offshore-marine/` from the homepage) — unrelated to Phase 30.2.
- `validate_ai_boundaries.py`: 2 pre-existing failures, no new regressions.
- One external URL (`https://www.iecex.com/`) was generated and **then removed** to comply with the system rule against generating external URLs not provided by the user. Replaced with a plain text reference to "the IECEx online certificate database".

### Corpus quality observations

The IEC 60079 RAG corpus is markedly cleaner than the NFPA 79 corpus encountered in Phase 30.1: no stray LLM prompts, no empty placeholder values, consistent front-matter, accurate cross-references. No corpus-hygiene findings to log from this sub-phase.

### Deferred (still to come in Phase 30)

- 30.3 — IEC 60204-1 Depth (next)
- 30.4 — SEMI S2/S8/S14 Depth
- 30.5 — IEC 62443 Depth (Worked Example + Common Mistakes)
- 30.6 — UL 508A and NEC (light polish)
- 30.7 — Functional Safety Worked Examples (ISO 12100, IEC 61508, IEC 61511)
- 30.8 — Family Overview Pages (decision-flow pass)

---

## Phase 30.1 — COMPLETE (2026-05-06)

NFPA 79 detail page upgraded from 3/8 to full ISO 13849-1 template-floor compliance. Branch: `feat/phase30-standards-depth-pass`. File: `docs/standards/us-electrical/nfpa-79/index.md` (110 → 246 lines).

### Sections added

- **Quick Start** (5 bullets) — scope cutoff (≤600 V, point-of-supply-connection), NEC handoff (Article 670 site / Article 409 panel), NFPA 79 vs IEC 60204-1 destination-market choice, where Ch 9 hands off to ISO 13849-1 / IEC 62061 for PL/SIL, UL 508A overlay (panel construction + SCCR per SB4).
- **Chapter Reference table** (corrected) — replaces the previous 11-row table that had Ch 6/7 swapped. Now lists 14 chapters with the chapters covered in depth marked in bold.
- **Per-Chapter Depth** for Ch 4 (general installation conditions), Ch 5 (disconnecting means — padlockable in OFF only, ≤2.0 m handle height, line-side guarding), Ch 6 (overcurrent protection — listed branch-circuit OCPDs, machine SCCR labelling), Ch 7 (shock protection — 30 V rms / 60 V DC threshold, IP2X/IPXXB barriers, capacitor discharge < 60 V in 5 s), Ch 8 (grounding — PE bus, Table 8.2.2.3 sizing, no daisy-chain), Ch 9 (control circuits — stop categories 0/1/2, E-stop device requirements, safety-rated controller for software safety), Ch 15 (transformers — isolated only, magnetising-inrush sizing, secondary OCP), Ch 16 (wiring colours: black/red/blue/orange/green-or-green-yellow), Ch 19 (marking & documentation — nameplate items including SCCR, ANSI Z535).
- **Worked Example** — UL-listed packaging machine for the US market: 480 V 3-phase, 50 A FLA, two E-stop zones, light curtain on infeed, NEMA 12. Walks the seven design steps (disconnect → OCP/SCCR → wire size and colour → grounding → control transformer → E-stop architecture → nameplate/docs) and ends with what NFPA 79 leaves to UL 508A and what NEC handles.
- **Common Mistakes** (6 numbered) — branch-circuit OCP vs SCCR confusion, NEC vs IEC 60204-1 PE colour mistakes, control-transformer inrush sizing, E-stop series-wiring without Cat 3/PLd architecture, treating NFPA 79 as installation code, missing the lockable-in-OFF requirement.
- **Practical Checklist** — Design / Build / Ship & Install groups.
- **Lifecycle Application table** — Standards Selection → Detailed Design → Build → Installation → Pre-Commissioning → Commissioning, each linking to the corresponding lifecycle-stage page.

### Plan vs RAG correction (lesson for 30.2 onward)

The Phase 30.1 plan as written assumed an NFPA 79 chapter layout that did not match NFPA 79:2024. Verified mapping (from `_index.yaml` and chapter content):

| Plan said | Actual NFPA 79:2024 |
|-----------|---------------------|
| Ch 4 — "general/EMC/environmental" | Ch 4 — General Conditions of Installation |
| Ch 5 — Disconnecting means ✓ | Ch 5 — Disconnecting Means ✓ |
| Ch 7 — Overcurrent vs SCCR | **Ch 6 — Overcurrent Protection** (Ch 7 is Shock Protection) |
| Ch 8 — Grounding ✓ | Ch 8 — Grounding and Bonding ✓ |
| Ch 9 — Control + transformer sizing | Ch 9 — Control Circuits; **transformer sizing is Ch 15** |
| Ch 13 — Wiring practices, colours | **Ch 16 — Wiring Methods** (Ch 13 is Appliances) |
| Ch 14 — Wireways/conduit | **Ch 16 — Wiring Methods** (Ch 14 is Lighting) |
| Ch 19 — Documentation ✓ | Ch 19 — Marking and Documentation ✓ |

The existing site page's "Key Chapters" table also had Ch 6 and Ch 7 swapped, with "Protection of equipment" mis-attributed to Ch 7 (that phrase is from IEC 60204-1, not NFPA 79). Both were corrected in this rewrite.

Specific clause numbers cited in the plan ("9.1.4" for inrush, "5.3.3" for lockable-in-OFF) are not present in the RAG corpus at the sub-clause level. The page cites chapter-level only and notes this explicitly in Common Mistake #3.

**Action for 30.2 onward:** before drafting any per-part / per-clause section, verify the chapter / part / clause mapping against the RAG `_index.yaml` and chapter front-matter. The Phase 30 plan is a target, not ground truth — the corpus is.

### Validation

- Jekyll build: clean (1.351 s, 268 HTML files generated).
- Internal links: all 13 outgoing links from the rewritten page resolve correctly. The 2 broken-link findings in the site-wide check (`/industries/food-beverage/`, `/industries/offshore-marine/`) come from `index.html` and pre-date Phase 30.1 — flagged as separate hygiene work.
- `validate_ai_boundaries.py`: 2 pre-existing failures (`IEC61511.md`, `UPW_water_skid_scenario.md`) — same baseline as start of Phase 30, no new regressions.

### Corpus hygiene findings (separate task — not Phase 30 scope)

The NFPA 79 RAG corpus at `control-standards/rag/standards_intelligence/us/nfpa79/` has several quality issues that should be addressed in a dedicated hygiene pass:

1. **Stray LLM prompts at chapter ends.** Ch 6, 7, 8, 15, 16, 17, 18 each end with a "Would you like me to assist with Chapter N?" line — clearly authoring artefacts that were never cleaned up.
2. **Empty placeholder values.** Ch 4 — temperature ranges read "between ** and ** ( to )"; Ch 17 — bend-radius multiples read "typically  to ". Numerical values are missing.
3. **Internal numbering bug.** Ch 6 file's Section 0 begins "The intent of Chapter 7 is to define..." — text refers to the chapter as 7 but the file is 6.
4. **Suspect cross-reference.** Ch 15 cites "Table 7.2.7" for primary transformer protection; that looks like a reference to an old chapter numbering and should be verified.

These do not block Phase 30.1 (the site page only used facts that were verifiable elsewhere in the chapter), but they degrade the RAG's value as authoritative source material.

### Deferred (still to come in Phase 30)

- 30.2 — IEC 60079 Depth (next)
- 30.3 — IEC 60204-1 Depth
- 30.4 — SEMI S2/S8/S14 Depth
- 30.5 — IEC 62443 Depth (Worked Example + Common Mistakes)
- 30.6 — UL 508A and NEC (light polish)
- 30.7 — Functional Safety Worked Examples (ISO 12100, IEC 61508, IEC 61511)
- 30.8 — Family Overview Pages (decision-flow pass)

---

## Phase 30 — Standards Depth Pass (Planned, 2026-04-29)

Drafted: 2026-04-29. Status: 30.1 COMPLETE (2026-05-06); 30.2–30.8 still planned. Branch: `feat/phase30-standards-depth-pass`.

### Motivation

Audit on 2026-04-29 showed standards detail pages all carry "Complete" badges on the live site, but actual depth varies by ~3×. ISO 13849-1 (224 lines) sets the bar with Quick Start, per-clause depth, a worked example, six numbered Common Mistakes, a practical checklist, and a lifecycle application table. Several other detail pages are 100–125 lines and lack worked examples, common-mistakes sections, and checklists. The site says "complete" but the user-facing utility is uneven — a US-market machine builder lands on NFPA 79 and gets a chapter table; a CE machine builder lands on IEC 60204-1 and gets a clause table; a hazardous-area engineer lands on IEC 60079 and gets marking codes without a worked IS-loop calculation. The corpus already has the underlying knowledge in `control-standards/rag/`; the gap is presentation.

### Depth Template (the floor)

Every standards detail page must carry these eight sections in this order. Pages currently missing one or more are listed below.

1. **Quick Start** — 5 bullets: the absolute essentials a designer needs before reading anything else
2. **Standard Overview** — table: Standard ID, Edition, Publisher, Jurisdiction, Scope, Repository path, Status badge
3. **Per-clause / per-part technical depth** — the standard's actual technical content, sectioned by clause or by part
4. **Worked Example** — concrete scenario → design choices → validation steps (named scenario, concrete numbers, specific clause references)
5. **Common Mistakes** — at least 5, numbered, each with root cause explanation; not generic advice but the specific mistakes that actually trigger non-compliance or rework
6. **Practical Checklist** — checkbox list a designer can use during the work, organized by lifecycle stage
7. **Lifecycle Application** — table: Stage → activity per that lifecycle stage, mapped to the site's existing lifecycle stage pages
8. **Related Standards** — links to the standards that interact with this one

### Audit Findings (2026-04-29)

Detail pages, scored against the 8-section template:

| Page | Lines | QS | Worked Ex | Mistakes | Checklist | Lifecycle | Score | Priority |
|------|-------|----|-----------|----------|-----------|-----------|-------|----------|
| ISO 13849-1 | 224 | ✓ | ✓ | 6 | ✓ | ✓ | 8/8 | reference (no work) |
| IEC 62061 | 257 | ✓ | ✓ | ✓ | ✓ | ✓ | 8/8 | reference (no work) |
| IEC 61511 | 266 | ✓ | — | ✓ | ✓ | ✓ | 7/8 | 30.7 |
| IEC 61508 | 194 | ✓ | — | ✓ | ✓ | ✓ | 7/8 | 30.7 |
| ISO 12100 | 189 | ✓ | — | ✓ | ✓ | ✓ | 7/8 | 30.7 |
| **NFPA 79** | **110** | — | — | — | — | partial | **3/8** | **30.1 (first)** |
| **IEC 60079** | **123** | — | — | — | partial | — | **3/8** | **30.2** |
| **IEC 60204-1** | **103** | — | — | — | — | partial | **3/8** | **30.3** |
| **SEMI S2/S8/S14** | **95** | — | — | — | — | — | **2/8** | **30.4** |
| IEC 62443 | 246 | ✓ | — | — | partial | partial | 5/8 | 30.5 |
| UL 508A | 307 | — | — | — | — | partial | 5/8 | 30.6 (lighter) |
| NEC | 355 | — | — | — | ✓ | partial | 6/8 | 30.6 (lighter) |

Family overview pages, scored on whether they help a user choose between members:

| Page | Lines | Has decision flow | Has comparison table | Has out-of-scope/gap call-outs | Priority |
|------|-------|-------------------|----------------------|-------------------------------|----------|
| Hazardous-area | 38 | — | partial | — | 30.8 |
| Semiconductor | 26 | — | — | — | 30.8 |
| Machinery | 63 | — | partial (60204 vs 79) | — | 30.8 |
| Cybersecurity | 74 | ✓ (routing block) | ✓ | ✓ | reference |
| Functional-safety | 124 | partial | ✓ | — | 30.8 (light) |
| US-electrical | 114 | — | partial | — | 30.8 (light) |

### Sub-Phase 30.1 — NFPA 79 Depth (FIRST)

**File:** `docs/standards/us-electrical/nfpa-79/index.md` (currently 110 lines)
**RAG source:** `control-standards/rag/standards_intelligence/us/nfpa79/` (20 chapters)
**Why first:** US-market machine-builder default. Largest gap (3/8) on a high-traffic page.

**Add — Quick Start (after page-header, before Standard Overview):**
- Five bullets covering: scope cutoff (600 V, point-of-supply-connection), relationship to NEC Article 670, when to choose NFPA 79 vs. IEC 60204-1, where Chapter 9 (E-stop) hands off to ISO 13849-1 / IEC 62061, what UL 508A adds when listing is required.

**Expand — Per-clause depth.** Current page has a 10-row chapter table. Replace or augment with sections covering:
- Chapter 4 — General requirements (EMC, environmental conditions)
- Chapter 5 — Supply circuit disconnecting means (size, type, location, lockable position)
- Chapter 7 — Overcurrent protection, branch-circuit protection vs. SCCR (this is the most-confused topic on the standard)
- Chapter 8 — Equipment grounding, equipotential bonding, grounded supply conductors
- Chapter 9 — Control circuit voltage classes, control circuit protection, control transformer sizing, E-stop categories (0/1)
- Chapter 13 — Wiring practices: wire colors, conductor identification, raceway fill (the table that catches first-time builders)
- Chapter 14 — Wireways, conduit, cable trays
- Chapter 19 — Technical documentation and markings

**Add — Worked Example: UL-listed packaging machine for US market.**
- Scenario: 480 V, 3-phase, 50 A FLA packaging machine, panel-mounted controls, two E-stop zones, one safety light curtain, NEMA 12 enclosure.
- Walk through: supply disconnect selection (Ch 5), branch-circuit OCP vs. machine SCCR (Ch 7), wire size and color (Ch 13), grounding bus and PE conductor sizing (Ch 8), control transformer sizing for 24 VDC controls (Ch 9), E-stop wiring and category selection (Ch 9 + handoff to ISO 13849-1), nameplate and documentation (Ch 19).
- End with: what NFPA 79 leaves to UL 508A (panel construction & listing) and what the NEC handles (installation post-shipment).

**Add — Common Mistakes (numbered, at least 6):**
1. Confusing branch-circuit OCP rating with machine SCCR — they are separate analyses; the panel needs both an OCPD upstream and a documented SCCR per UL 508A SB4.
2. Using NEC color rules (green-or-bare PE) when shipping to a market that requires IEC 60204-1 (yellow-green PE only).
3. Sizing control transformers from steady-state current and missing the inrush requirement (NFPA 79 9.1.4).
4. Tying E-stop pushbuttons in series without considering Category 3/PLd architectural requirements — wiring works, but the safety architecture per ISO 13849-1 doesn't.
5. Treating NFPA 79 as the installation code — it's the design code for the machine; NEC Article 670 governs installation at the site.
6. Missing the disconnecting-means lockable-in-OFF requirement (5.3.3) on machines that ship without one — added cost late if caught at site commissioning.

**Add — Practical Checklist** (Design / Build / Ship & Install groups).

**Add — Lifecycle Application table** mapping NFPA 79 activities to: Standards Selection, Detailed Design, Build, Installation, Commissioning, Maintenance.

**Estimated added length:** ~150–180 lines. Target final: ~280 lines.

**Validation:**
- Jekyll build: clean, no broken links.
- Internal links: ISO 13849-1, UL 508A, NEC Art. 670, IEC 60204-1, NFPA 79 ↔ IEC 60204-1 crosswalk all resolve.
- `validate_ai_boundaries.py`: same baseline (2 pre-existing failures — separate hygiene task).

---

### Sub-Phase 30.2 — IEC 60079 Depth

**File:** `docs/standards/hazardous-area/iec-60079/index.md` (currently 123 lines)
**RAG source:** `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/`

**Add — Quick Start** (5 bullets): when IEC 60079 applies vs. NEC Class/Division, what the marking string actually tells you, why area classification (60079-10-1) drives everything else, when intrinsic safety is the right choice, what the certificate says vs. what the nameplate says.

**Expand — Per-part depth.** Current page lists 6 parts in a marking-elements table. Add per-part sections:
- 60079-0 — General requirements; marking; T-class **temperature classes table** (T1 = 450°C through T6 = 85°C with 5 K margin rule).
- 60079-10-1 — Area classification methodology (release grade × ventilation × dispersion). This is the topic with the worst depth gap.
- 60079-11 — Intrinsic safety: ia/ib/ic; entity parameters; concept of energy limitation; **gas group autoignition examples**: hydrogen IIC (560°C), acetylene IIC (305°C), ethylene IIB (425°C), methane IIA (537°C), propane IIA (470°C).
- 60079-1 — Flameproof Ex d: flame paths, gap and length requirements, certified glands.
- 60079-7 — Increased safety Ex e: design rules, terminal blocks, motor cage rotor temperature rise.
- 60079-2 — Pressurization Ex p: types Px, Py, Pz; purge cycle; pressure monitoring loss-of-pressure response.
- 60079-14 — Installation: cable systems, gland selection by Ex method, equipotential bonding in HazAreas.
- 60079-17 — Inspection: visual / close / detailed grades; periodicity.

**Add — Worked Example: 4–20 mA pressure transmitter on an ethylene tank, Zone 1, T3.**
- IS loop math (entity check):
  - Field device: Ui = 30 V, Ii = 100 mA, Ci = 15 nF, Li = 50 µH
  - Barrier: Uo = 28 V, Io = 93 mA, Co = 83 nF, Lo = 5.7 mH
  - Cable: 100 m × 200 pF/m = 20 nF, 100 m × 0.7 µH/m = 70 µH
- Verify each: Uo ≤ Ui ✓, Io ≤ Ii ✓, Ci + Ccable ≤ Co (15 + 20 = 35 ≤ 83) ✓, Li + Lcable ≤ Lo (50 + 70 = 120 µH ≤ 5700 µH) ✓
- Earthing: zener barrier earth ≤ 1 Ω; trunk earthed at one point only.
- Marking verify: equipment Ex ia IIB T4 Gb satisfies Zone 1 ethylene (IIB) T3 area.

**Add — Common Mistakes (numbered, at least 5):**
1. Choosing equipment by gas-group letter alphabetically ("IIC must be best, pick that"). IIC equipment satisfies any gas group, but is more expensive and Ex e or Ex d in IIC has stricter installation requirements — match to actual hazard.
2. Trusting the nameplate without checking the certificate. Certificates can be withdrawn; nameplates persist. Verify against IECEx/ATEX online database.
3. Mixing certified and uncertified components in an IS loop. The entity-check math fails immediately if any uncertified component touches the loop.
4. Routing IS and non-IS cables in the same multicore cable or tray without the required separation (minimum 50 mm or rigid metal barrier, per 60079-14).
5. Using zener barriers with inadequate IS earth (>1 Ω). The fault-current path becomes the issue; barriers behave unpredictably.
6. Forgetting that Ex e motors require thermal protection (PTC or microthermistor in winding) wired to a certified relay — overload alone is not sufficient.

**Add — Practical Checklist** (Area classification / Equipment selection / Installation / Inspection groups).

**Add — Lifecycle Application table.**

**Estimated added length:** ~180–220 lines. Target final: ~310 lines.

---

### Sub-Phase 30.3 — IEC 60204-1 Depth

**File:** `docs/standards/machinery/iec-60204-1/index.md` (currently 103 lines)
**RAG source:** `control-standards/rag/standards_intelligence/international/machinery/iec_60204_1/` (15 clauses)

**Add — Quick Start** (5 bullets): scope/voltage range, harmonized status under EU Machinery Directive, where ISO 12100 hands off, where ISO 13849-1 / IEC 62061 take over for safety functions, what the Technical Construction File needs (Clause 17).

**Expand — Per-clause depth.** Current page lists 14 clauses in a crosswalk table. Add sections for at least:
- Clause 5 — Incoming supply, disconnecting means (lockable, position-indicated, 90% retention rule), main switch sizing.
- Clause 6 — Protection against electric shock; PELV vs. SELV; fault protection by automatic disconnection, double insulation, electrical separation.
- Clause 7 — Protection of equipment; overcurrent vs. overload distinction.
- Clause 8 — Equipotential bonding circuit, PE conductor sizing rules (Table 1: 16 mm² → 16 mm²; >35 mm² → S/2), continuity test 0.1 Ω at 10 A.
- Clause 9 — Control circuits; safety functions; emergency stop categories 0/1/2; control voltages 24 VAC/DC preferred; control transformer rules.
- Clause 12 — Conductors and cables; minimum sizing; voltage drop; ampacity by installation method.
- Clause 13 — Wiring practices; identification; PE wire-color requirement (yellow-green only).
- Clause 17 — Technical documentation set: schematics, layout, parts list, maintenance manual.

**Add — Worked Example: CE-marked CNC machine for EU market.**
- Scenario: 400 V 3-phase, 25 A FLA, Class I machine, two E-stop zones, safety door interlock, IP54 panel.
- Walk through: supply disconnector type and rating (Cl 5), PE conductor sizing from Table 1 (Cl 8), continuity test method (Cl 8), control voltage selection 24 VDC (Cl 9), E-stop Category 1 with safety relay (Cl 9 + handoff to ISO 13849-1), wire color audit (Cl 13), Technical Construction File contents (Cl 17 + Machinery Directive Annex VII).
- End with: what's added when shipping the same machine to the US (NFPA 79 deltas: voltage scope, wire colors, neutral handling).

**Add — Common Mistakes (numbered, at least 5):**
1. Ignoring the 90% supply-voltage retention rule on the disconnector (Cl 5). Many disconnectors meet IEC 60947-3 but not the higher retention required by 60204-1.
2. PE conductor sized by current rating instead of Table 1 — Table 1 governs and often demands a larger PE than the line conductor sizing would suggest.
3. Mixing PE wire colors (green, green-with-yellow stripe sized differently). Only yellow-green continuous is acceptable; this is a frequent CE audit finding.
4. Treating Clause 9 E-stop categories as ISO 13849-1 PL categories. They are different concepts: stop category 0/1/2 ≠ PL/Cat. They interact (a Cat-1 E-stop with PLd architecture is a typical pairing).
5. Skipping the Technical Construction File detail in Clause 17 because internal documentation already exists. CE audit specifically checks the items listed in 17 — if your internal binder doesn't map, it counts as missing.
6. Designing for global use but choosing 480 V supply and 110 V control circuits — will not pass IEC 60204-1 (above its preferred ranges) and adds rework when shipping to EU.

**Add — Practical Checklist** (Design / Build / Validation / TCF groups).

**Add — Lifecycle Application table.**

**Estimated added length:** ~180–210 lines. Target final: ~290 lines.

---

### Sub-Phase 30.4 — SEMI S2/S8/S14 Depth

**File:** `docs/standards/semiconductor/semi/index.md` (currently 95 lines)
**RAG source:** `control-standards/rag/standards_intelligence/international/semiconductor/semi/`

**Add — Quick Start** (5 bullets): why SEMI is purchase-condition not statutory, the S2 → S8 → S14 progression, overlap with IEC 60204-1 / NFPA 79, where ISO 12100 plugs in, what the third-party EHS report typically covers.

**Expand — Per-standard depth.** Current page has bullet highlights only.
- SEMI S2: deepen Sections 8 (electrical), 11 (interlocks), 14 (chemicals & gases), 19 (radiation), 23 (seismic) — what each section actually requires for control engineers.
- SEMI S8: full ergonomic envelope (reach, vertical access zones), display readability, lifting and material handling, maintenance access requirements.
- SEMI S14: fire risk assessment methodology, hazard categories, suppression options (clean agent, water mist, local pre-action), interaction with facility fire alarm.

**Add — Worked Example: PVD tool S2 review.**
- Hazards: high-voltage DC supply (cap-discharge), pyrophoric process gas (silane), heated chuck, vacuum interlocks.
- Walk through interlock chain (gas → vacuum → process), capacitor discharge proof (50 V in 5 s), S8 ergonomics for chamber access, S14 silane fire risk assessment and N₂ purge interlock.
- End with: how the third-party SEMI S2 report packet integrates with the customer's fab acceptance test.

**Add — Common Mistakes (numbered, at least 5):**
1. Treating SEMI S2 like a checklist instead of a risk-assessment-driven document. S2 references ISO 12100; the risk assessment drives interlock and protection selection.
2. Tagout-only on a primary energy isolation point. SEMI S2 requires lockable-capable; tagout-only fails most fab AHJ reviews.
3. Capacitor discharge timing measured at last-known-good but not periodically. The 50 V / 5 s rule is design-validated but field-degradable.
4. Water suppression in cleanroom areas. SEMI S14 strongly disfavors water; clean agent or pre-action is the standard.
5. Missing the integration with facility-wide gas detection and exhaust systems. The tool's own monitors are necessary but not sufficient — fab interlock and reporting protocols apply.

**Add — Practical Checklist** (S2, S8, S14 columns or sections).

**Add — Lifecycle Application table** (Tool Design → Factory Test → Site Acceptance Test → Production → Decommissioning).

**Estimated added length:** ~180 lines. Target final: ~275 lines.

---

### Sub-Phase 30.5 — IEC 62443 Depth (Worked Example + Common Mistakes)

**File:** `docs/standards/cybersecurity/iec-62443/index.md` (currently 246 lines)

Already has Quick Start, FRs, Zones/Conduits, SL table. Missing a concrete worked example and a generalised Common Mistakes section.

**Add — Worked Example: Networked safety PLC in a process plant.**
- Architecture: control-room safety PLC connected to field junction via fiber, integrated with DCS via OPC UA, SIS-rated for SIL 2.
- Walk through: Zone definition (Safety Zone vs. Process Zone vs. Office Zone), Conduit definition (OPC UA conduit between SIS-Process), SL-T target derivation per zone (SL-T 3 for Safety Zone given Internet-adjacent enterprise zone two hops away), FRs implemented per Foundational Requirement (FR1 access control, FR3 system integrity for the SIS-DCS conduit, FR5 restricted data flow), residual risk register entries.

**Add — Common Mistakes (numbered, at least 5):**
1. Conflating SIL with SL — SIL is functional-safety failure rate; SL is cybersecurity threat tier. They are independently dimensioned.
2. Treating the safety PLC as inherently isolated. Modern safety PLCs have firmware update channels, diagnostic ports, and engineering-station connections — all of which are conduits.
3. Skipping the Asset Inventory step (62443-2-1). Without an enumerated asset inventory the Zone/Conduit map is a guess.
4. Buying a "62443-4-2 certified" component and assuming the system is compliant. Component certification does not satisfy 62443-3-3 system requirements.
5. Cybersecurity risk assessment as a one-time activity. 62443 lifecycle is ongoing; threat landscape changes faster than the SIS does.

**Estimated added length:** ~80–100 lines.

---

### Sub-Phase 30.6 — UL 508A and NEC (Light Polish)

**Files:**
- `docs/standards/us-electrical/ul-508a/index.md` (307 lines, content-heavy already)
- `docs/standards/us-electrical/nec/index.md` (355 lines, content-heavy already)

Both pages have strong per-clause/per-article depth but are missing Quick Start, an explicit worked example, and a Common Mistakes section.

**UL 508A — Add:**
- Quick Start (5 bullets): when listing matters, SCCR vs. branch-circuit protection, the SB4 method, marking requirements, relationship to NFPA 79 and NEC Art. 409.
- Worked Example: SCCR calculation on an industrial control panel with VFD, fused disconnect, and TVSS — using SB4 step-by-step.
- Common Mistakes (5): SCCR = OCPD rating (wrong); using TVSS to "boost" SCCR (it doesn't); marking SCCR as letter-of-record only without component documentation; mixing UL listed and recognized components without confirming the listing chain; ignoring that field-modification can void listing.

**NEC — Add:**
- Quick Start (5 bullets): NEC scope vs. NFPA 79 scope at machinery handoff, when Art. 409/430/670 each apply, when 2026 edition matters for control engineers, where AHJ discretion applies.
- Worked Example: machine installation walk-through (Art. 670 → NFPA 79 → UL 508A panel → branch circuit & disconnect at site per Art. 240/430).
- Common Mistakes (5): treating NEC as the design code for the machine itself (it isn't — it's the installation code); confusing Art. 409 (industrial control panels) with Art. 670 (industrial machinery); missing the Art. 430 motor-circuit protection differentiation between OCP and overload; missing 2026 edition changes that affect EVSE-adjacent panels even if the panel itself isn't EV.

**Estimated added length:** ~80 lines per page.

---

### Sub-Phase 30.7 — Functional Safety Worked Examples (ISO 12100, IEC 61508, IEC 61511)

**Files:**
- `docs/standards/functional-safety/iso-12100/index.md` (189 lines)
- `docs/standards/functional-safety/iec-61508/index.md` (194 lines)
- `docs/standards/functional-safety/iec-61511/index.md` (266 lines)

These pages already have Quick Start, Common Mistakes, Checklist, and Lifecycle. They are missing concrete worked examples.

**ISO 12100 — Add Worked Example: Conveyor pinch-point risk assessment.**
- Hazard identification → S/F/P assessment → 3-step method (inherently safe by design first, then guarding, then information for use) → outputs PLr handed off to ISO 13849-1.

**IEC 61508 — Add Worked Example: Safety burner management subsystem.**
- 16-phase lifecycle traversal at high level, hardware fault-tolerance HFT calculation, SFF → SIL ceiling, software development to SIL 2.

**IEC 61511 — Add Worked Example: Process tank overpressure SIF.**
- LOPA analysis with named IPLs (relief valve credit, BPCS credit, alarm credit), PFDavg calculation by sum of subsystem PFDs, proof-test interval derivation, IPLs → SIL target → architecture.

**Estimated added length:** ~80 lines per page.

---

### Sub-Phase 30.8 — Family Overview Pages (Decision Flow Pass)

**Files:**
- `docs/standards/hazardous-area/index.md` (38 lines — extreme outlier)
- `docs/standards/semiconductor/index.md` (26 lines — extreme outlier)
- `docs/standards/machinery/index.md` (63 lines)
- `docs/standards/functional-safety/index.md` (124 lines, light polish only)
- `docs/standards/us-electrical/index.md` (114 lines, light polish only)

Family pages currently list members. They should help a user **choose between members** when more than one applies.

**Add to each family page:**
- Decision flow diagram (Mermaid, similar to cybersecurity routing block) — "I have X, which standard applies?"
- Comparison table when family has more than one member with overlapping scope.
- Out-of-scope / gap callouts (which adjacent standards we don't cover, with badges) — cybersecurity family already does this well; copy the pattern.

For semiconductor (26 lines) and hazardous-area (38 lines): also add a brief "Why this family" framing paragraph and a "Where to start by lifecycle stage" mapping.

**Estimated added length:** ~50–80 lines per family page.

---

### Cross-Cutting Principles for Phase 30

- **RAG is authoritative.** Pages draw from `control-standards/rag/`. If a worked example needs technical content not yet in RAG, add to RAG first, then to the site. Do not invent technical content on the site layer.
- **Worked examples must be concrete.** Named scenario, real numeric values, specific clause/article references. Generic advice does not count.
- **Common Mistakes are not a marketing list.** Each mistake must name what goes wrong, why it goes wrong, and how to detect it. If we cannot name the failure mode, the entry is too vague to keep.
- **No new corpus claims.** This is a depth pass on existing corpus. Do not introduce coverage of standards not already in `rag/standards_intelligence/`.
- **Build clean every sub-phase.** Each sub-phase ends with a Jekyll build, link audit, and `validate_ai_boundaries.py` baseline check.

### Recommended Order and Sequencing

1. **Pre-30 hygiene (15 min):** clear the 2 pre-existing `validate_ai_boundaries.py` failures so depth-pass commits show a clean baseline. This is mechanical, no scope.
2. **30.1 — NFPA 79** (largest gap on highest-traffic page).
3. **30.2 — IEC 60079** (largest single technical-depth gap; IS worked example is high value).
4. **30.3 — IEC 60204-1** (CE-market default; pairs naturally with 30.1 since the NFPA 79 worked example references the IEC 60204-1 contrast).
5. **30.4 — SEMI S2/S8/S14**.
6. **30.5 — IEC 62443** worked example + common mistakes.
7. **30.6 — UL 508A + NEC** (light polish — Quick Start + worked example + common mistakes).
8. **30.7 — ISO 12100, IEC 61508, IEC 61511** worked examples.
9. **30.8 — Family overview pages** (decision flows; can be done in parallel with any of the above since it touches different files).

### Sub-Phase Validation Checklist (apply to every sub-phase)

- [ ] Jekyll build clean (`cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build`).
- [ ] All internal links resolve in built HTML.
- [ ] All clause/article references in worked example match the cited standard edition.
- [ ] Common Mistakes entries each have a named failure mode + root cause + detection cue.
- [ ] Practical Checklist groups align with the site's lifecycle stage taxonomy.
- [ ] Lifecycle Application table maps to existing `/lifecycle/<slug>/` pages.
- [ ] `validate_ai_boundaries.py`: same baseline as start of Phase 30 (no new failures).
- [ ] `validate_reorg.sh all`: same baseline as start of Phase 30.
- [ ] `project_state.md` updated: sub-phase moved from Planned to COMPLETE; line counts logged.
- [ ] `change_log.md` entry added.

### Out of Scope for Phase 30

- No new standards added to corpus.
- No new pages outside `docs/standards/`.
- No re-architecture of the standards section information architecture (that would be a Phase 31).
- No changes to homepage front-door, Standards Finder, or scenario pages.
- No CSS or template changes — depth pass is content-only.

### Branch and Commit Discipline

- Single feature branch: `feat/phase30-standards-depth-pass`.
- One commit per sub-phase.
- Commit-message scheme: `site: <Page> depth pass — Quick Start + Worked Example + Common Mistakes (Phase 30.x)`.
- Each commit is independently buildable and reviewable.
- No commit lands on master directly. Merge once entire Phase 30 (or a clean sub-phase batch) is complete.

## Phase 29.4 — COMPLETE (2026-04-29)

Sketch-B faceted-filter upgrade to the Standards Finder. The Phase 29.3 page shipped with a 5-anchor jump strip and an explicit deferral note: *"If this proves insufficient, a Phase 29.4 could add real filter chips that hide non-matching scenario sections."* Phase 29.4 ships exactly that, additively — the no-JS jump strip stays.

### Filter UI (`docs/tools/standards-finder/index.md`)

- New `.finder-filters` block above the jump strip.
- Two chip rows (`<button>` + `aria-pressed`):
  - **Market**: US-market | Global / EU | Industry-bound
  - **What you're building**: Machinery / panel | Process safety (SIS) | Hazardous area | Cybersecurity | Industry overlay (SEMI / DNV)
- Result-count line (`Showing N of 9 scenarios`) and a Clear-filters link, divided by a dashed border.
- Empty-state message that surfaces when the filter combination matches nothing — links into the closing escape-hatch section.
- Each `.scenario-card` carries `data-finder-region` and `data-finder-domain` (multi-value where honest — e.g. Networked Safety PLC = `machinery cyber`; Offshore Platform = `process hazloc industry-overlay`).
- Each grouping `<section>` carries `data-finder-section` so empty sections collapse when none of their cards survive the filter.

### Filter logic (`docs/assets/js/main.js`, ~85-line IIFE)

- No-ops when `[data-finder-filters]` is absent — safe to ship in the global bundle.
- OR within a facet row, AND across rows. (Selecting two market chips broadens; selecting a market + a domain narrows.)
- Updates `aria-pressed` on chips, toggles `.is-hidden` on cards and empty sections, updates the count, surfaces the empty-state when nothing matches, hides Clear button when no chip is pressed.
- No URL persistence in this phase. (Deferred — see Next Phase.)

### CSS (`docs/assets/css/main.css`)

- New `.finder-filters` block (~95 lines): chip pill styling, active state via `aria-pressed="true"`, dashed-divider meta row, dark-mode parity via existing color tokens, `.is-hidden` helper for cards/sections.

### Progressive enhancement

The existing `.finder-jump` anchor strip is kept verbatim underneath the filter block. No-JS readers still get the original 5-section scroll-and-pick experience; JS-on readers get filter chips on top. The filter is additive and not load-bearing for the page's core function.

### Validation

- Jekyll build: clean, 1.261 s.
- Built HTML: 9 `data-finder-region` cards, 8 `.finder-chip` buttons (3 + 5), 5 `data-finder-section` sections, 1 `.finder-empty` element.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (same baseline as Phase 29.3).
- `validate_reorg.sh all`: 48/50 baseline.

### What was NOT built

- No URL persistence for filter state. Personal-use site, not yet justified.
- No "save my preset" or any storage layer.
- No new scenarios. Phase 29.4 is a UI improvement on the existing 9.
- No removal of the anchor jump strip — kept as the no-JS fallback and as a quick scroll-and-pick path.

### Known follow-ups

- **Phase 29.4.1** — URL hash persistence for filter chips (`#region=us&domain=cyber`). Cheap to add; only worth it if shareable filter links become useful.
- **Phase 29.5** — Industries-axis Finder (sibling page that pivots on industry vertical: semicon, water, pharma, oil-and-gas) reusing the same scenario cards via different grouping.

## Phase 29.3 — COMPLETE (2026-04-27)

Built the Standards Finder page that the Phase 29 Start Here grid had been promising. The "I need applicable standards" card and the hero-CTA "Find applicable standards" both used to route to `/tools/crosswalks/` — a comparison tool, not a finder. Phase 29.3 ships a real entry surface.

Implementation followed Sketch C from the IA brainstorm: a scenario-card entry page, no JS, no faceted filter (deferred). The 9 existing engineering scenarios in `docs/implementation/scenarios/` are reused verbatim — no new scenario content was authored. The Finder's job is purely to organize them so the user can scan and pick.

### New page (`docs/tools/standards-finder/index.md`)

- Page-header with the routing promise as the H1.
- A `.finder-jump` anchor-chip strip at the top with 5 in-page jumps.
- 5 grouped sections, each with the scenario cards relevant to that context:
  1. **US-market machines & control panels** (Scenarios 01, 06)
  2. **Global / EU-market machines** (Scenario 02)
  3. **Process safety — SIS / ESD** (Scenarios 03, 07)
  4. **Networked & cyber-physical safety** (Scenario 04)
  5. **Industry-specific stacks** (Scenarios 05, 08, 09)
- Closing escape-hatch section with two `.card`s: route to Crosswalks (comparison) and Standards Atlas (browse). This handles the "none of these fit" case explicitly rather than dead-ending the user.

### CSS (`docs/assets/css/main.css`)

- New `.finder-jump` block (~35 lines): horizontal flex strip with a mono `__label`, then small bordered anchor chips. Reuses existing color tokens — works in both light and dark mode without further overrides.

### Re-routes

- `docs/index.md` hero CTA: `/tools/crosswalks/` → `/tools/standards-finder/`.
- `docs/index.md` Start Here "I need applicable standards" card: same re-route, plus copy refresh to match the Finder's scenario-first framing ("Pick the scenario closest to your project — region, equipment class, and risk profile already mapped to a standards stack").
- `docs/_data/navigation.yml`: added `Standards Finder` as the first child under Tools (above RAG Browser, Glossary, Crosswalks). Now visible in the global sidebar on every Tools page.

### What was NOT built (deliberate scope cut)

- No live filter UI (Sketch B). The 5-section anchor jump covers the same find-by-context need with zero JS. If this proves insufficient, a Phase 29.4 could add real filter chips that hide non-matching scenario sections.
- No new scenario content. The 9 existing scenarios already cover the meaningful territory; what was missing was an entry surface, not more scenarios.
- The crosswalks page wasn't deprecated. It still serves the comparison use case (NFPA 79 ↔ IEC 60204-1 etc.); the Finder just stops being the wrong default destination.

### Validation

- Jekyll build: clean, 1.078 s.
- `/tools/standards-finder/` renders: 5 jump anchors, 9 scenario cards, both escape-hatch cards.
- Homepage hero CTA + Start Here card both point to `/tools/standards-finder/` in built HTML.
- Standards Finder appears in the Tools-section sidebar on `/tools/`.
- `validate_ai_boundaries.py`: 2 pre-existing failures only.
- `validate_reorg.sh all`: 48/50 baseline.

## Phase 29.2 — COMPLETE (2026-04-27)

Extended the Phase 28 local-sidebar pilot from `electrical-machines` (Motors, 18 modules, 5 buckets) to three more topic groups, taking the pilot total to 4 groups and 52 modules. Pure data change in `docs/_data/training_catalog.yml` — no template, CSS, or JS edits required, exactly as the Phase 28 architecture promised.

### Bucket taxonomies

- **Electrical Fundamentals** (`fundamentals`, 9 modules, 4 buckets): Circuit Analysis (4), Components & Devices (2), Practical Wiring (2), Quick References (1).
- **Control Systems** (`control-systems`, 14 modules, 5 buckets): Foundations (2), PID Methods (5), Machine Logic & Safety (2), Distributed Systems (2), Motion & Tuning (3).
- **NEC for Machines and Panels** (`nec-application`, 11 modules, 4 buckets): Foundations (2), Motors & Article 430 (3), Panels & Article 409 (3), Machine-Side Wiring (3).

### Module label discipline

Every module in the three new groups got a `nav_title` (32 of 34 modules — the 2 already-short ones, Passive Components and Equivalent Circuit Methods, were left to use their full `title`). Result: bucket labels and module labels both fit comfortably inside the 288 px sidebar without truncation.

### Validation

- Jekyll build: clean, 1.057 s.
- Sample local sidebars verified for `/fundamentals/electrical/electrical-quantities/` (4 buckets), `/fundamentals/control/pid-foundation/` (5 buckets), `/training/nec-application/nec-code-reading/` (4 buckets).
- `validate_ai_boundaries.py`: 2 pre-existing failures only.
- `validate_reorg.sh all`: 48/50 baseline.

### Known deferred (now in Phase 29.3)

- Standards Finder page so the "I need applicable standards" Start Here card routes to a real decision tool rather than the crosswalks page.

## Phase 29.1 — COMPLETE (2026-04-27)

Theme-compatibility and polish pass for the Phase 28 local sidebar pilot, plus an accessibility fix for the global sidebar. Single batch covering all four tiers that had been queued during Phase 29 planning.

### Tier A — dark-mode chip palette

`.sidebar__chip--b/i/a/ref/concept/code/core` were hard-coded to light-mode colors, leaving dark-mode chip backgrounds illegible on the local sidebar. Added `[data-theme="dark"]` overrides for all seven variants, mirroring the existing dark page-chip palette (lines 2016–2022 of main.css).

### Tier B — elevation, caret, letter-spacing

- `.sidebar--local .sidebar__section-meta` now carries a soft `box-shadow` (light: `0 1px 2px rgba(0,0,0,.04)`; dark: `0 1px 2px rgba(0,0,0,.35)`) to separate the section header from the bucket list.
- Global sidebar (`.sidebar__section summary::after`) was switched from a text-swap caret (▶/▼) to a rotating ▸ chevron with a 0.15s ease transition — same pattern the local sidebar already used. Both sidebars now animate consistently.
- `.sidebar__bucket-summary` letter-spacing tightened from 0.07em → 0.05em (less shouty against tightly-packed bucket labels).

### Tier C — active-weight, label abbreviations, border-radius

- New rule `.sidebar__bucket[open] > .sidebar__bucket-summary { color: var(--color-text); }` brightens the bucket label color when the bucket is open, giving a clearer "you are here" cue alongside the rotated caret.
- `.sidebar__chip` and `.sidebar__bucket-count` got `border-radius: 4px` to match the chip language used elsewhere on the site.
- Six Motors modules that were still using their full titles in the sidebar got `nav_title` overrides:
  - Induction Motor Basics → "Induction Basics"
  - DC Motor Basics → "DC Basics"
  - Motor Family Comparison → "Family Comparison"
  - Servo Drive Fundamentals → "Servo Fundamentals"
  - BLDC Motor Reference → "BLDC Reference"
  - PMSM Motor Reference → "PMSM Reference"
- VFD Fundamentals left unchanged — already concise, no shorter form without losing meaning.

### Tier D — aria-current on global sidebar

`sidebar-global.html` was setting `class="active"` on the active link but never `aria-current="page"`, leaving screen readers without a programmatic "current page" cue on every non-pilot page. Added `aria-current="page"` alongside the existing `class="active"` for section, child, and grandchild links. The local sidebar already had this since Phase 28.

### Validation

- Jekyll build: clean, 1.146 s.
- 7 dark-mode chip overrides present in built CSS.
- Rotated chevron CSS present on global sidebar.
- All 6 new `nav_title` strings rendered in the Motors sidebar.
- `aria-current="page"` present on both `/standards/` (global) and `/fundamentals/motors/induction-motor-basics/` (local).
- `validate_ai_boundaries.py`: 2 pre-existing failures only.
- `validate_reorg.sh all`: 48/50 baseline.

### Known deferred (now in Phase 29.2)

- Extend the local sidebar pilot to Control Systems, Electrical Fundamentals, or NEC topic groups (data-only change per the Phase 28 architecture).
- Dedicated Standards Finder page so the "I need applicable standards" Start Here card routes to a real decision tool rather than the crosswalks page.

## Phase 29 — COMPLETE (2026-04-21)

Homepage rework: the site's front door was inheriting the interior-page layout (default.html), so visitors arriving at `/` faced the global sidebar, right-side context panel, trust-boundary block, and a reference-first content order. Phase 29 replaces that with a dedicated home layout and a task-router content order.

### New layout (`docs/_layouts/home.html`)

- Topnav + scripts kept.
- Dropped: sidebar include, context-panel include, trust-boundary include, breadcrumb block.
- `<main class="home-main">` replaces the three-panel CSS Grid. Centered, `max-width: 1100px`, `2rem 2rem 3rem` padding.
- Theme script, Mermaid init, analytics all retained — parity with default.html except the interior chrome.

### Homepage content (`docs/index.md`)

Reordered from **Standards Families → Lifecycle → Graph → Industry Matrix → Scenarios → Repository Explorer** to **Hero → Start Here → Scenarios → Browse by family → Browse by lifecycle → Browse by industry → Power-user deep-dive (collapsed)**.

- **Hero rewritten** to a plain-language promise: title *"Find the right standards path for your machine, panel, or safety system."*, subtitle explains the routing-by-intent model, 3 CTAs (Find applicable standards / Start with a scenario / Learn fundamentals).
- **Start Here 6-card grid** (new `.start-card` component): I need applicable standards · US control panel · Machine for US + EU · Safety architecture · Troubleshooting / commissioning · Training and fundamentals. Each card routes to an existing page — all 6 URLs verified at build time.
- **Common engineering scenarios** moved up — now the second section after Start Here (was sixth).
- **Browse by standards family**: cards preserved but the raw corpus path labels (e.g., `rag/us/`, `control-standards/rag/.../overlap_matrix/`) were dropped. The `TO VERIFY` badge was also removed since IEC 62443 corpus is now complete.
- **Browse by lifecycle**: 11-stage ribbon kept intact but moved below scenarios. The `_standards_map` filename was replaced with plain *"Decision map"*.
- **Browse by industry**: the 9-row matrix table replaced with 6 clickable `.industry-tile` cards (Semiconductor, Oil & Gas, Energy, Food & Beverage, Water & Wastewater, Offshore & Marine), plus a link to the full industries page.
- **Standards graph** reduced to a one-line teaser + link inside the collapsed deep-dive block.
- **Repository explorer tree** moved into the collapsed `<details class="home-deep-dive">` block at the bottom, labelled *"For power users — standards graph and repository layout"*.

### Topnav (`docs/_includes/topnav.html`)

- Search placeholder "Search standards…" → "Search standards, workflows, training…". ARIA label updated to match. Single-line change.

### CSS (`docs/assets/css/main.css`)

New block *Home layout* introduces:
- `.home-body`, `.home-main` — centered container without grid.
- `.home-hero` + `.home-hero__label/__title/__subtitle/__ctas` — wider typography than `.hero` used elsewhere.
- `.start-grid` + `.start-card` + `.start-card__label/__title/__desc/__next` — reuses existing color tokens and border treatment so it slots into the theme.
- `.home-section` + `.home-section__intro` — consistent rhythm between the four browse sections.
- `.industry-tiles` + `.industry-tile` + `.industry-tile__name/__meta` — lightweight tile grid to replace the dense matrix.
- `.home-deep-dive` — `<details>` with mono summary that mirrors the sidebar bucket caret pattern (text-swap `▶`/`▼`, no animation).
- Mobile breakpoint tightening for hero type at ≤900px.

### Pages **not** changed

- `docs/_layouts/default.html` — interior layout is byte-for-byte unchanged. No conditional logic added; the separate-layout approach keeps the interior surface protected.
- Every non-homepage URL continues to render its existing sidebar (global or local Motors pilot) and context panel.

### Validation

- Jekyll build: clean, 1.136 s.
- `/` (home): 0 sidebar elements, 0 context-panel elements, `home-main` + `home-hero` present, 6 `start-card`, 6 `industry-tile`.
- `/standards/` (interior sample): 23 `sidebar__*` elements — global sidebar intact.
- `/fundamentals/motors/bldc-pmsm-implementation/` (Motors pilot page): local Phase 28 sidebar intact.
- `validate_ai_boundaries.py`: 2 pre-existing failures only.
- `validate_reorg.sh all`: 48/50 baseline.

### Known deferred

- Theme-compatibility plan for the Phase 28 local sidebar (Tier A dark-mode chip fix, Tier B elevation/caret/letter-spacing, Tier C active-weight/label-abbreviations/border-radius, Tier D aria-current on global sidebar) — still pending the user's pick on which tiers to run.
- Sub-categorisation or filter UI inside the Start Here grid.
- A dedicated "Standards Finder" decision page that the "I need applicable standards" card could route to instead of the crosswalks page.
- Illustrated hero (photo or diagram) — intentionally skipped for the first pass.

## Phase 28 — COMPLETE (2026-04-21)

Sidebar pilot: the global sidebar was a mirror of the top-level sitemap on every page, which meant deep-section pages (especially under `/fundamentals/motors/`) had no visible local tree, no bucket grouping, and no sense of page depth. Phase 28 introduces a **local section sidebar** for opted-in topic groups and keeps the **global sidebar** as the fallback for everything else. Pilot is scoped to `/fundamentals/motors/` (18 modules) only.

### Architecture

- **Router**: `docs/_includes/sidebar.html` now decides between a local and global sidebar at build time.
  - It walks `training_catalog.topic_groups`, finds the one whose `url` is a prefix of `page.url`, and checks whether any of that group's modules carry a `sidebar_bucket` tag.
  - If both conditions are met, it includes `sidebar-training-group.html`. Otherwise it includes `sidebar-global.html` (which contains the pre-pilot markup verbatim).
  - This means adding a new section to the pilot is a data-only change: tag its modules with `sidebar_bucket` and list the buckets under the topic group.
- **Local sidebar include**: `docs/_includes/sidebar-training-group.html` renders section title + description, then iterates `topic_groups[…].sidebar_buckets` in a defined order, rendering each bucket as a `<details>` element with its active state open. A catch-all "Other" bucket captures any tagged module whose bucket is missing from the order list.
- **Global sidebar include**: `docs/_includes/sidebar-global.html` is a byte-for-byte copy of the old sidebar.html markup. No behavior change on non-pilot pages.

### Data changes (`docs/_data/training_catalog.yml`)

- `topic_groups.electrical-machines.sidebar_buckets` — defines bucket order for both the sidebar and the landing page. Buckets:
  1. Foundations (5 modules)
  2. Drive Systems (5)
  3. Selection & Comparison (3)
  4. Deep References (3)
  5. Quick References (2)
- Each of the 18 Motors modules tagged with `sidebar_bucket`.
- 11 modules also got a `nav_title` for a shorter sidebar label (e.g. `Motor Nameplates, Slip, and Torque` → `Nameplates, Slip, Torque`; `BLDC, EV, and Drone Motor Comparison` → `BLDC / EV / Drone`; `BLDC and PMSM Implementation Guide` → `Implementation Guide`).

### Styling (`docs/assets/css/main.css`)

- `--sidebar-width: 240px → 288px`. This is a **site-wide** token — it widens every sidebar, not just the local one. Intentional per the pilot spec; visible effect on all pages.
- New CSS block for the local sidebar only: `.sidebar--local`, `.sidebar__section-meta`, `.sidebar__section-title`, `.sidebar__section-desc`, `.sidebar__bucket`, `.sidebar__bucket-summary` (+ `-label`, `-count`), `.sidebar__item` (+ active state), `.sidebar__item-meta`, `.sidebar__chip` (`-b`/`-i`/`-a`/`-ref`/`-concept`/`-code`/`-core`), `.sidebar__toc` (+ `.toc-h2`/`.toc-h3` + `.is-active`), `.sidebar__section-footer`.
- Chip palette reuses the color tokens already used in `.chip-beginner/-intermediate/-advanced/-reference/-concept/-code/-featured` blocks further down the stylesheet.

### JavaScript (`docs/assets/js/main.js`)

- New IIFE after the existing "Mark active sidebar links" block, runs only when `.sidebar.sidebar--local` is present.
- Reads `data-topic-group` from the nav to scope `localStorage` to `sidebar-buckets:<group>`, saving the open state per topic group so sections don't collide.
- On load, user-toggled bucket state is restored; the bucket containing the active page is always forced open regardless.
- Scans `.main-content h2[id], h3[id]` on the active page and injects them into `[data-local-toc]` as a nested list. An `IntersectionObserver` keeps the nearest heading highlighted as the reader scrolls. No static fallback for the TOC — it is purely a JS enhancement.

### Landing page (`docs/fundamentals/motors/index.md`)

- Description updated ("13 modules" → "18 modules"), intro copy tweaked to mention the deep BLDC/PMSM reference work added in Phase 27.
- Rebuilt the body from a single flat module table into 5 tables, one per bucket, iterating `topic_groups[…].sidebar_buckets` so the landing and sidebar always share the same ordering and mental model.

### Pages **not** changed by this pilot (kept intentionally)

- `docs/_includes/topnav.html` — topnav stays as global site navigation.
- `docs/_data/navigation.yml` — still the source for the global sidebar fallback.
- All non-motors pages — no schema change, no visual change beyond the sidebar widening.

### Validation

- Jekyll build: clean, 1.185s.
- Local sidebar verified on the motors landing, BLDC/PMSM Comparison, and BLDC/PMSM Implementation pages — correct bucket rendering, chip counts (18 bucketed modules → 18 level + 18 type chips; 6 `Core` chips matching `featured: true`), active item, and TOC mount.
- Fallback verified on 3 non-pilot pages (`/standards/`, `/standards/cybersecurity/iec-62443/`, `/fundamentals/electrical/`) — each gets exactly one sidebar and it is the global one.
- Kramdown bucket H2s render with correct slug IDs on the landing page.
- `validate_ai_boundaries.py`: 2 pre-existing failures only (no new regressions).
- `tools/validate_reorg.sh all`: 48/50 baseline unchanged.

### Known deferred

- Mobile sidebar pattern is unchanged — the drawer pattern (`is-open` on `.sidebar`) works for both local and global markup.
- The global sidebar widening may feel loose on non-pilot sections that still have short menu labels. Revisit after the pilot bakes in.
- The active-page TOC is JS-only. Users with JS disabled get the sidebar structure and module tree but no heading list.
- No search-box or filter inside the local sidebar yet; out of pilot scope.

## Phase 27.7 — COMPLETE (2026-04-21)

Same UX polish pattern as Phase 27.6, applied to the BLDC vs PMSM Comparison page (`docs/fundamentals/motors/bldc-vs-pmsm/index.md`). Site-only; no RAG edits; no new CSS.

### UX changes (reuse existing `.glance-grid`, `.card`, `.scenario-grid`, `.scenario-card`)

- **Trimmed `## Purpose`** from a 170-word paragraph to 3 short lines (Use this when / Choose BLDC if / Choose PMSM if).
- **"At a glance" 4-card decision strip** directly under Purpose: BLDC wins when / PMSM wins when / Induction still the right answer sometimes / Don't choose by motor name alone.
- **"Jump to" 5-card nav** pointing at Construction, Control, Feedback, Decision Matrix, Scenarios — all 5 kramdown anchor IDs verified in built HTML.
- **Moved the Decision matrix up** from after the scenarios to just before them (high-value content now lands before the long scenario section).
- **Rebuilt 10 scenario walkthroughs as scan cards** at the top of `## Scenario walkthroughs`, each with 4 fields (Winner / Why / When the other side wins / Stack) and each linking to the existing detail H3 below. All 10 anchor IDs verified.

### Factual and tone fixes in the same file

- "One-sentence distinction": softened `PMSM = ... always driven with sinusoidal (FOC) control` → `typically driven with sinusoidal commutation or FOC`, with an explicit scope note that this module treats PMSM as the servo-style sinusoidal/FOC case.
- Common failure modes: corrected `DC-link undervoltage during hard regen` → `overvoltage` with correct physics (regen pushes the bus up, not down, and OV trips occur when the brake chopper/resistor is undersized or missing).
- Takeaway block: softened absolute phrasing — replaced `full stop` and `the right answer in 2026` with more engineering-style qualifications while keeping the core recommendations intact.

### Validation

- Jekyll build: clean, 1.134s, page count unchanged.
- All 5 jump-menu anchor IDs verified in built HTML.
- All 10 scenario-card anchor IDs verified in built HTML (kramdown em-dash handling yields the double-hyphen slug form consistently).
- AI-boundary validator: 2 pre-existing failures only (no new regressions).
- `tools/validate_reorg.sh all`: 48/50 baseline unchanged.

### Deferred (not in first-pass scope)

- Alternating visual rhythm across `Control strategy comparison`, `Drive / inverter architecture`, and `Feedback` sections using `.compare-columns` (instead of table-after-table prose).
- Shorten per-scenario detail: move Summary line to top, trim repeat setup bullets.
- Front-matter title sharpening (`BLDC vs PMSM — Motors, Drives, and Scenarios` → decision-focused variant).
- Training vs Fundamentals identity (shared with Phase 27.6 deferred list).

## Phase 27.6 — COMPLETE (2026-04-21)

First-pass UX polish of `docs/fundamentals/motors/bldc-pmsm-implementation/index.md` (the deepest and most template-feeling page of the Phase 27 motors set) plus a small factual-correctness pass. Site-only; no RAG edits.

### UX changes (reuse existing CSS — `.glance-grid`, `.card`, `.card-grid`, `.scenario-grid`, `.scenario-card`)

- **Trimmed `## Purpose`** from a 200-word paragraph to 3 bullets: When to use, What it helps decide, What it will not do — plus an inline link back to the BLDC vs PMSM Comparison page for family-choice questions.
- **"Choose fast" 4-card strip** added directly under Purpose: Choose BLDC / Choose PMSM / Watch-outs / Build sequence.
- **"Jump to" 6-card nav** (Architecture / Control / Sizing / Drive Choice / Wiring / Checklist) rendered as `<nav class="glance-grid">` pointing at kramdown-generated H2 anchor IDs. All 6 targets verified in built HTML.
- **Scenarios cardified** — 8 scan cards (`.scenario-grid` / `.scenario-card`) showing 4 fields each (Motor, Drive, Control, Why it wins), each linking to the existing detailed H3 section below (all 8 anchors resolve via kramdown heading IDs).
- **Checklist cardified** — 5-section checklist (Motor, Drive, Wiring, Control, Testing) wrapped in `.card-grid` with `markdown="1"` per card; 44 task-list checkboxes rendered correctly inside the cards.
- **Known industry brands moved to appendix** — formerly a 5-subsection bullet-list interruption between scenarios and wiring, now a compact 3-column table (Category / Typical vendors / Fit) placed after the checklist.

### Factual fixes in the same file

- Scenario 1 drone control: corrected "PWM command ... DShot protocol" → "Digital throttle ... DShot (150/300/600/1200 kbit serial) is the common signaling protocol, not PWM".
- Common failure modes: corrected "DC-link **undervoltage** during regen" → "DC-link **overvoltage** during regen" with a correct physics description (returning kinetic energy pushes bus up, not down).
- Power wiring sizing: softened "typically 125% of motor FLA" to explicitly cite NEC 430.22 for single continuous-duty motor branch circuits and note that multi-motor / intermittent / drive-fed cases use NEC 430.24/430.33 or IEC 60204-1 §12.
- Contactor practice: rewrote "Contactor: on the line side for E-stop and lockout" to distinguish lockout/SS1-Cat-0/1 use from certified STO use, with the caveat that contactor-on-every-E-stop stresses the precharge circuit.
- Feedback shield termination: replaced the "drive end only — check drive manual" line with a more accurate note that single-end is common for classical analog/incremental encoders, and 360° both-end termination is typically required for digital one-cable interfaces (Hiperface DSL, DRIVE-CLiQ, OCT) and EMC compliance.

### Validation

- Jekyll build: clean, 1.219s, page count unchanged.
- Kramdown-generated anchor IDs verified for all 6 jump-menu targets and all 8 scenario-card targets.
- `markdown="1"` task-list rendering verified: 44 `<input type="checkbox">` elements inside the 5 checklist cards.
- AI-boundary validator: 2 pre-existing failures only (no new regressions).
- `tools/validate_reorg.sh all`: 48/50 baseline unchanged.

### What this phase did not touch

Deferred follow-ups from the full edit plan (optional second-pass work):
- Rebuild `## Executive overview` as `.compare-columns` side-by-side (first-pass keeps the existing bullet comparison).
- Rename flatter section headers to more directional ones (e.g., "Pick the drive stack", "Wire it without creating noise").
- Insert "Use this when / Avoid this when / Cost penalty / Commissioning burden" callouts through the `Drive architecture` → `Cost vs performance tradeoff` middle section.
- Resolve the Training vs Fundamentals identity mismatch (`/fundamentals/` URL under a `training-module` layout).

## Phase 27.5 — COMPLETE (2026-04-21)

Follow-up to Phase 27 adding visual wiring guides (Mermaid diagrams with cable-class coloring) across the BLDC and PMSM pages. Content-only — no new pages or routing.

### New visual convention (establishes project baseline)

All motor-system wiring diagrams use the same `classDef` stroke colors:

- Power (DC bus / battery / AC line) → `#c0392b` (red)
- Motor phase (U/V/W) → `#2c3e50` (near-black)
- Feedback (Hall / encoder / resolver / temp) → `#2980b9` (blue)
- Safety (STO / SS1 / interlocks) → `#e67e22` (orange)
- Fieldbus (EtherCAT / PROFINET / CAN) → `#27ae60` (green)
- Shield / PE → `#7f8c8d` dashed

Legend + convention table lives in the Implementation Guide §14 top (one anchor, cross-linked from other pages).

### Mermaid diagram changes (7 new across 4 pages)

- `docs/fundamentals/motors/bldc-pmsm-implementation/index.md`: +1 legend diagram (D5) + 3 archetype diagrams (D4): Battery BLDC, Integrated PMSM servo, Shared DC-bus multi-axis PMSM. Mermaid count 3 → 7.
- `docs/fundamentals/motors/bldc-reference/index.md`: +1 wiring archetype diagram (D2). Mermaid count 0 → 1.
- `docs/fundamentals/motors/pmsm-reference/index.md`: +1 industrial servo wiring diagram (D3). Mermaid count 2 → 3.
- `docs/fundamentals/motors/motor-selection-scenarios/index.md`: upgraded 3 trivial 3-node flows to labeled cable-group diagrams (D1) + added 1 new Scenario 2 wiring diagram. Mermaid count 4 → 5.

### New pinout reference tables (2)

- BLDC Reference: Hall connector pinout (5-pin, IEC 60757 conductor colors)
- PMSM Reference: Encoder connector pinout (incremental + absolute protocols + temp + shield)

### New reference content

- PMSM Reference: new `## Wiring and integration` top-level section (servo wiring diagram + encoder pinout + STO dual-channel note + cross-link to Servo Commissioning Workflow)
- Implementation Guide §14: cable-group legend subsection at top; three archetype subsections replacing prior prose bullets

### Cross-links (9 new)

- BLDC Reference → Implementation Guide Archetype A + Motor Selection Scenarios Scenario 1
- PMSM Reference → Implementation Guide Archetypes B and C + Motor Selection Scenarios Scenario 2
- BLDC vs PMSM Comparison: inline archetype references from Scenario C (servo press) and Scenario E (drone)
- Motor Selection Scenarios: cross-scenario summary → cable-group legend + three archetypes

### Validation

- Jekyll build: clean, 1.026s, 273 HTML files (unchanged)
- AI boundary validator: 2 pre-existing failures only (no new regressions)
- `tools/validate_reorg.sh all`: 48/50 baseline
- Internal link checker: exit 0, all 9 new cross-links resolve via kramdown heading IDs
- RAG files and site files stay in sync (equivalent content, per-format conventions)

## Phase 27 — COMPLETE (2026-04-20)

Five new motor reference modules promoted from `planning/motors/` into the RAG corpus and the Jekyll site. Existing `bldc-ev-drone-motors` module enriched with a drone-class vs EV-class deep comparison section.

### RAG corpus (`control-standards/rag/training_modules/electrical_machines/`)
- [x] `bldc_motor_reference.md` — deep BLDC reference (1732 lines)
- [x] `pmsm_motor_reference.md` — deep PMSM reference (437 lines)
- [x] `bldc_vs_pmsm_comparison.md` — head-to-head comparison with 10 scenarios, application-fit guidance, and choice rationale (440 lines)
- [x] `bldc_pmsm_implementation_guide.md` — 16-section production-grade implementation reference with wiring / control / drive selection patterns (918 lines)
- [x] `bldc_pmsm_scenarios.md` — three engineering-grade scenario deep-dives (fan/pump, precision axis, AGV) with per-scenario drive, wiring, tuning, measurement, and failure-mode detail (715 lines)
- [x] `_index.yaml` updated — 5 new files registered, file count 13 → 18

### Site pages (`docs/fundamentals/motors/`)
- [x] `bldc-reference/index.md` (1683 lines)
- [x] `pmsm-reference/index.md` (439 lines)
- [x] `bldc-vs-pmsm/index.md` (446 lines)
- [x] `bldc-pmsm-implementation/index.md` (922 lines)
- [x] `motor-selection-scenarios/index.md` (719 lines)

### Data / cross-links / enrichment
- [x] `docs/_data/training_catalog.yml` — electrical-machines module_count 13 → 18, 5 new module entries
- [x] `docs/fundamentals/motors/bldc-ev-drone-motors/index.md` — new drone-class vs EV-class deep comparison body section (15 subsections, 2 new Mermaid diagrams, citations to TI/Microchip/Beckhoff/Tektronix preserved as inline links) + "See also" cross-links. File grew 180 → 429 lines.
- [x] `docs/fundamentals/motors/motor-family-comparison/index.md` — "See also" cross-links to new modules

### Clean-up
- [x] `planning/motors/pmsm.md` — placeholder deleted
- [x] `planning/motors/motors_comparisons.md` — redundant, deleted (superseded by existing `motor-family-comparison` site module)
- [x] `planning/motors/scenarios.md` — retained as staging history (source for Module 5 and for `bldc-ev-drone-motors` enrichment)

### Validation
- Jekyll build: clean, 1.037s
- AI boundary validator: 2 pre-existing failures only (no new regressions)
- `tools/validate_reorg.sh all`: 48/50 baseline maintained
- Internal link checker: exit 0 (273 files scanned, no broken links)

### Header/convention adjustments made during execution
- Plan originally spec'd YAML frontmatter for RAG files; actual project convention is HTML-comment headers with richer metadata (MODULE_FAMILY, LEARNING_LEVEL, INDEX_TAGS). Adjusted after Task 1; all 5 RAG files use the correct convention.
- Source file `bldc.md` contained no Mermaid diagrams (used plain text ASCII art) — plan's "commutation state machine, control hierarchy (nested loops)" Mermaid expectation for Module 1 was not met because the source didn't have them. Content still complete.
- External citations in `scenarios.md` (TI, Microchip, Beckhoff, Tektronix) rendered as inline plain markdown links per the plan's risk-note strategy; no footnote infrastructure added.

## Phase 26 — COMPLETE (2026-04-15)

Phase 26 closed out in 12 batches covering plan Tasks 1–16. The site now has:

- A 10-group intent-based sidebar rooted at `docs/_data/navigation.yml` (Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository)
- Physical URL reorganization: ~156 pages moved into the new hierarchy
- Every moved page carries `redirect_from:` frontmatter — old URLs (3 years of history across fundamentals, control-systems, electrical-machines, engineering-workflow, workflows, commissioning-templates, scenarios, lifecycle/\*, field-engineering, reference, rag-browser, glossary, crosswalks, about) continue to resolve via `jekyll-redirect-from`
- 501 residual cross-links rewritten to point directly at new paths (no unnecessary 301 hops)
- Internal link checker `tools/check_internal_links.py` exits 0 against the built `_site/` (267 scanned files)
- AI boundary validator shows only the 2 pre-existing Phase 25 failures — no regressions
- `jekyll-redirect-from` plugin installed in `Gemfile` / `_config.yml`
- Authoritative old→new URL registry persists at `docs/_data/phase26_migration_map.yml`

Phase 26 Batch 12 (Tasks 15–16) is complete:
- Final audit: Jekyll build clean (267 HTML files), internal link check exit 0, AI-boundary validator shows same pre-existing Phase 25 failures with no new regressions, `tools/validate_reorg.sh all` returns the pre-existing baseline of 48/50 (the 2 failures are the downstream AI-boundary script exit and one archive check, both carried over from before Phase 26).
- No source changes needed — sweep in Batch 11 already resolved all residual broken links.
- `project_state/project_state.md` closed out to **Phase 26 COMPLETE — Navigation Restructure and Link Audit**; next phase set to `Phase 27 PLANNING — TBD`.
- `project_state/change_log.md` received a top-level Phase 26 COMPLETE rollup entry.

Phase 26 Batch 11 (Task 14) is complete:
- Site-wide cross-link sweep: 501 replacements across 49 files. All residual references to pre-Phase-26 URLs now point directly at the new paths instead of relying on the `jekyll-redirect-from` 301 chain.
- Paths swept (longest-first, word-boundary-safe so `/tools/X/` is not rewritten into `/tools/tools/X/`):
  - `/training/fundamentals/` → `/fundamentals/electrical/`, `/training/control-systems/` → `/fundamentals/control/`, `/training/electrical-machines/` → `/fundamentals/motors/`
  - `/engineering-workflow/` → `/design/`, `/software-stack/` → `/design/software-stack/`
  - `/workflows/electrical-review/`, `/workflows/motor-selection/` → `/design/workflows/…`; `/workflows/servo-commissioning/`, `/workflows/vfd-commissioning/` → `/implementation/…`; `/workflows/motor-troubleshooting/` → `/troubleshooting/motors/`; `/workflows/` → `/design/workflows/`
  - `/commissioning-templates/` → `/implementation/commissioning-templates/`, `/scenarios/` → `/implementation/scenarios/`
  - `/lifecycle/risk-assessment/|…/safety-*|…/maintenance/|…/management-of-change/` → `/verification/…`; `/lifecycle/concept/|…/standards-selection/|…/detailed-design/|…/draft-documentation/` → `/verification/lifecycle/…`; `/lifecycle/build/|…/pre-commissioning/|…/installation/|…/commissioning/` → `/implementation/lifecycle-*/`; `/lifecycle/` → `/verification/lifecycle/`
  - `/field-engineering/` → `/implementation/commissioning-templates/`
  - Straggler `/reference/architecture/…`, `/reference/motor-systems/…`, `/reference/`, `/rag-browser/`, `/glossary/`, `/crosswalks/`, `/about/` swept to the Phase-26 equivalents
- Skip list (safety): `redirect_from:` frontmatter blocks, `docs/_data/phase26_migration_map.yml`, `docs/_data/rag_tree.json`, `docs/assets/rag-files/**` (regenerated), and the Phase 26 plan + design spec (contain old URLs as data).
- `docs/_data/training_catalog.yml` swept (105 refs), `docs/_data/field_checklists.yml` swept (22 refs), `docs/_includes/topnav.html` + top-nav now points at the new URLs.
- `docs/field-engineering/index.md` meta-refresh shim still in place — its redirect target was updated to `/implementation/commissioning-templates/`.
- Jekyll build clean (267 HTML files); internal link check exit 0 (267 files scanned). AI-boundary validator: same pre-existing 2 Phase 25 failures, no new regressions.

Phase 26 Batch 10 (Task 13) is complete:
- Four new top-level landing pages created to support the 10-group nav structure without producing broken sidebar links:
  - `docs/fundamentals/index.md` — sub-group cards for electrical, control, motors
  - `docs/implementation/index.md` — commissioning templates, scenarios, four lifecycle stages (build/installation/pre-commissioning/commissioning), plus VFD and servo commissioning workflows
  - `docs/verification/index.md` — risk assessment, SRS, safety architecture, safety wiring, maintenance, management of change, full lifecycle journey
  - `docs/tools/index.md` — RAG browser, glossary, crosswalks, reference hub
- `docs/_data/navigation.yml` fully rewritten from the prior 5-group historical layout to the new 11-top-level structure (Home + Fundamentals + Standards + Design + Implementation + Verification + Industries + Troubleshooting + Training + Tools + Repository). Match prefixes realigned and the hardcoded legacy "Engineering Workflow" / "Reference" groups dropped.
- Sidebar now renders every top-level group clickable without 404s.
- Jekyll build clean (267 HTML files, +4 from Batch 9); internal link check exit 0.

Phase 26 Batch 9 (Task 12) is complete:
- Created `docs/repository/index.md` — Repository and Project Info landing. Lists the GitHub URL, a link to the moved About page, a "How This Site Is Built" block, a "Content Source of Truth" table keyed off `project_state/`, and a short contributing note.
- Moved `docs/about/index.md` → `docs/repository/about/index.md`, with `redirect_from: [/about/, /about/index.html]` so old URLs continue to resolve. Breadcrumb updated to `Repository › About`.
- Updated the top-nav `About` link in `docs/_includes/topnav.html` to point at `/repository/about/` (active-state logic updated too).
- Updated `docs/_data/navigation.yml` — removed the `/about/` match prefix + About child from the Reference group, and added a new Repository top-level group (children: About / Trust Boundary).
- Removed the now-empty `docs/about/` directory.
- Jekyll build clean (263 HTML files, +2 from Batch 8); internal link check exit 0.

Phase 26 Batch 8 (Task 11) is complete:
- New `/troubleshooting/` section created with two pages:
  - `docs/troubleshooting/index.md` — landing with 6 symptom categories (Motors, VFDs, PLC systems, Field I/O, Networks, Safety circuits), each row pointing at the most appropriate existing workflow, fundamentals reference, or commissioning template
  - `docs/troubleshooting/motors/index.md` — Motor Troubleshooting Decision Tree (moved from `/workflows/motor-troubleshooting/`)
- `redirect_from:` added to the motors page so `/workflows/motor-troubleshooting/` and `/workflows/motor-troubleshooting/index.html` still resolve
- Motors page breadcrumb updated from `Workflows › Motor Systems` to `Troubleshooting › Motors`
- Motors page internal cross-links updated: Related Training and Related Workflows tables now point at `/fundamentals/motors/...`, `/design/workflows/motor-selection/`, `/implementation/vfd-commissioning/`, `/implementation/servo-commissioning/`, and `/implementation/commissioning-templates/motor-rotation-verification/` (instead of the old `/training/electrical-machines/...` and `/workflows/...` paths)
- Cross-link sweep for `/workflows/motor-troubleshooting/` → `/troubleshooting/motors/` across 5 source pages and 2 data files (`docs/design/workflows/index.md`, `docs/design/workflows/motor-selection/index.md`, `docs/design/index.md`, `docs/implementation/vfd-commissioning/index.md`, `docs/implementation/servo-commissioning/index.md`, `docs/_data/training_catalog.yml`, `docs/_data/field_checklists.yml`)
- `docs/workflows/` tree removed — after the motor-troubleshooting move, only empty shells for `electrical-review/` and `motor-selection/` remained (those subdirs had already been emptied when Batch 3 moved their content to `/design/workflows/...`)
- `docs/_data/navigation.yml` — Troubleshooting group added (children: Motors). The larger nav rewrite to the new 10-group structure is reserved for plan Task 13 and is out of Batch 8 scope.
- Jekyll build clean (261 HTML files, +2 from Batch 7); internal link check exit 0.

Phase 26 Batch 7 (Task 10) is complete:
- `docs/training/index.md` rewritten as a thin structured-paths landing page. It now advertises only the NEC-for-Machines-and-Panels path (fundamentals / control / motors already moved to `/fundamentals/` in Batch 2), plus a "Related Sections" pointer block to specific existing landings (fundamentals/electrical, fundamentals/control, fundamentals/motors, design hub, lifecycle, implementation subsections, and tools entries).
- The page no longer iterates `site.data.training_catalog` — that catalog is still consumed by the three `/fundamentals/*` group landings, the NEC-application page, and the `training-module` layout, so it stays in place untouched.
- Intentionally avoided linking to `/fundamentals/`, `/verification/`, `/implementation/`, `/tools/` as bare top-level URLs — those landing pages don't exist yet and are out of Batch 7 scope. Links go to specific existing sub-pages instead.
- Jekyll build clean (259 HTML files); link check exit 0.

Phase 26 Batch 6 (Task 9) is complete:
- Tools group migrated: 10 pages moved to `/tools/`
  - `/rag-browser/` → `/tools/rag-browser/`
  - `/glossary/` → `/tools/glossary/`
  - `/crosswalks/` index + 6 subpages (compare, iec60079-nec-500-505, iec61511-iec61508, nfpa79-iec60204, standards-decision-workflow, ul508a-nec-nfpa79) → `/tools/crosswalks/...`
  - `/reference/` landing → `/tools/reference-hub/`
- Correct `redirect_from:` with bare + `/index.html` variants added to all 10 moved files
- Internal cross-links repo-wide updated: 143 replacements across 39 files; also backfilled straggler `/reference/architecture/*` and `/reference/motor-systems/*` refs (moved during design batch) in six design pages
- `docs/_data/navigation.yml` Reference group updated to point at `/tools/...` URLs
- Empty old source directories removed: `docs/rag-browser/`, `docs/glossary/`, `docs/crosswalks/`, `docs/reference/`
- One relative-link regression caught in `compare/index.md` (`../../standards/`) and rewritten to absolute `{{ '/standards/' | relative_url }}`
- Jekyll build clean (259 HTML files); link check exit 0

Phase 26 Batch 5 (Task 8) is complete:
- Verification group migrated: 5 pages under `/verification/lifecycle/` (index, concept, standards-selection, detailed-design, draft-documentation) and 6 top-level verification pages (`/verification/risk-assessment/`, `safety-requirements-spec/`, `safety-architecture/`, `maintenance/`, `management-of-change/`, `safety-wiring/`)
- Correct `redirect_from:` with bare + `/index.html` variants added to all 11 moved files
- Internal cross-links across 35 source files updated to point at new verification/implementation URLs (glossary, data files, includes, industries, water-wastewater, semiconductor facility, implementation/lifecycle-*, design hub)
- New data file `docs/_data/lifecycle_stage_urls.yml` maps lifecycle-stage slugs to their correct URLs (split across `/verification/lifecycle/`, `/verification/`, `/implementation/`); `docs/_includes/context-panel.html` and `docs/glossary/index.md` now use the lookup instead of a hardcoded prefix
- Empty `docs/lifecycle/` tree removed
- **Redirect audit and backfill for Batches 1–4:** discovered that Batches 1–4 had written `redirect_from:` entries pointing at the NEW URL (self-redirect) instead of the OLD URL. A script walked the migration map and corrected 41 files; the 5 hub pages (`/engineering-workflow/`, `/software-stack/`, `/training/fundamentals/`, `/training/electrical-machines/`, `/training/control-systems/`) and 2 stragglers (`pid-drone-control`, `motor-selection`) were fixed manually
- Link check went from 768 broken links (pre-batch-5 baseline) → 0 broken links (249 site files scanned, exit 0)
- Jekyll build: clean, 249 HTML files

Phase 26 Batch 4 (Task 7) is complete:
- Implementation group (23 pages) migrated to `/implementation/`: commissioning-templates (7), scenarios (10), servo-commissioning, vfd-commissioning, lifecycle-build, lifecycle-pre-commissioning, lifecycle-installation, lifecycle-commissioning
- `redirect_from:` with both bare and `/index.html` variants added to all 23 moved files
- Internal cross-links inside moved pages updated to new `/implementation/...` paths
- Empty source directories removed; Jekyll build clean

Phase 26 Batch 3 (Task 6) is complete:
- Design group migrated to `/design/`; all redirects in place

Phase 26 Batch 2 (Task 5) is complete:
- Fundamentals/training group migrated to `/fundamentals/`; all redirects in place

Phase 26 Batch 1 (Tasks 1–4) is complete:
- `jekyll-redirect-from` plugin installed and verified (Gemfile, Gemfile.lock, _config.yml updated; gem 0.16.0 installed)
- `tools/check_internal_links.py` created (stdlib-only internal link checker, exits 0 clean / 1 broken)
- Baseline audit: 16 broken links found across 11 source files; all 16 resolved (wrong paths in glossary.yml, semiconductor crosswalks, water-wastewater pages, lifecycle/build, training, and workflow pages); checker now exits 0 on 166 files
- `docs/_data/phase26_migration_map.yml` created — authoritative old→new URL registry for all 6 migration groups (fundamentals, design, implementation, verification, tools, training_trim)

## Current Reality

- Jekyll site deployed on GitHub Pages — `https://kyawminthu20.github.io/Control-System-Tools/`
- Last validated Jekyll build: **267 HTML files**, clean build (verified 2026-04-15; Phase 26 complete — navigation restructure, physical URL reorganization, and link audit)
- Three-panel layout (sidebar 240px + main content + context panel 220px); sidebar data-driven from `docs/_data/navigation.yml` with **11 top-level groups** — Home, Fundamentals, Standards, Design, Implementation, Verification, Industries, Troubleshooting, Training, Tools, Repository
- Mermaid.js CDN integration for all diagrams; Cytoscape.js 3.28.1 for interactive standards graph
- Google Analytics tag installed sitewide in `docs/_layouts/default.html` using measurement ID `G-RPL3G47EFZ`
- GitHub Actions deployment workflow at `.github/workflows/pages.yml`
- `jekyll-redirect-from` plugin installed — every page moved in Phase 26 has `redirect_from:` frontmatter so pre-Phase-26 URLs continue to resolve
- Internal link checker at `tools/check_internal_links.py` (stdlib only) — exits 0 against the built site
- Phase 26 URL migration registry persists at `docs/_data/phase26_migration_map.yml`
- Site covers: homepage, all standards families (US Electrical, Machinery, Functional Safety, Cybersecurity, Hazardous Area, Semiconductor), standards relationship graph, 13 lifecycle stage pages (split across `/verification/lifecycle/`, `/verification/`, and `/implementation/lifecycle-*/`), 10 scenarios under `/implementation/scenarios/`, 7 crosswalk pages under `/tools/crosswalks/`, 10 industry overlays, glossary (45 terms) at `/tools/glossary/`, NEC training track (11 modules) at `/training/nec-application/`, 7 commissioning templates at `/implementation/commissioning-templates/`, fundamentals landings for electrical/control/motors, design hub with architecture and workflows, troubleshooting landing with motors subpage, tools hub, repository landing with About/Trust Boundary
- Interactive standards graph: 12 nodes, 16 edges, including IEC 60079, IEC 61511, and SEMI
- Fundamentals groups: Electrical (9 modules), Control Systems (14 modules), Motors and Drives (13 modules) — formerly under `/training/*`, now at `/fundamentals/electrical/`, `/fundamentals/control/`, `/fundamentals/motors/`
- Reference Hub at `/tools/reference-hub/`: architecture and motor-system models; design-layer architecture pages live under `/design/architecture/`
- Root `main.py` remains a placeholder (not the site)

## Tools — FE Study Automation

**FE Study Pipeline** (`tools/fe_study/`)

The FE study tools automate content extraction and inventory from the `planning/FE_Study/` directory. The pipeline scans, extracts, and catalogs How-To and training documents.

### `.doc` File Support (P2 Priority)

- **Conversion:** LibreOffice headless (`soffice --headless --convert-to docx`) for `.doc` → `.docx` conversion
- **Caching:** Converted files cached under `planning/FE_Study/How to/_converted/` for reuse
- **Family/Priority:** `howto_doc` family, P2 (important but not urgent)
- **Scope:** All `.doc` files under `planning/FE_Study/How to/`
- **Filtering:** Temporary/lock files (`~$*.doc`) automatically excluded from scanning
- **Status:** Implemented and tested (15/15 tests PASS; scan, extract, and build_record branches functional)

## Source Of Truth By Topic

- Current phase, status, and next implementation items: `project_state/project_state.md`
- Project-level change history: `project_state/change_log.md`
- Runtime, tooling, and deployment requirements: `project_state/environment.md`
- Setup, run, validation, and deployment steps: `project_state/how_to.md`
- Phase 20 software safety routing source: `planning/safety_software_stack.md`
- Phase 18 control-systems site plan: `docs/plans/2026-03-11-phase18-control-systems-training.md`
- Cross-layer integration pre-plan and Phase 20 candidates: `docs/plans/2026-03-10-training-system-integration-preplan.md`
- Phase 19 engineering-workflow navigation plan: `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`
- Authoritative standards content: `control-standards/rag/`
- Site source: `docs/`

## Phase 1 Scope — COMPLETED

- [x] Jekyll scaffold: `docs/_config.yml`, `docs/Gemfile`, Bundler vendor install
- [x] Three-panel CSS Grid layout: `docs/assets/css/main.css`
- [x] Layouts and includes: default.html, topnav, sidebar, context-panel, trust-boundary
- [x] Mermaid.js CDN integration (theme: neutral)
- [x] Homepage with all 8 content blocks (hero, standards cards, lifecycle ribbon, relationship diagram, industry matrix, scenarios, repo explorer)
- [x] Standards explorer landing + US Electrical family + Machinery family + Functional Safety family
- [x] Individual standard pages: NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511
- [x] Lifecycle landing + 11 stage pages
- [x] Crosswalk pages: NFPA 79 ↔ IEC 60204-1, UL 508A/NEC/NFPA 79, Standards Decision Workflow
- [x] 5 scenario pages: US Control Panel, Global Machine, Process Skid, Networked Safety PLC, Semiconductor Equipment
- [x] Industry matrix landing + 9 industry pages
- [x] Software Stack and Cybersecurity routing page
- [x] About / trust boundary page
- [x] GitHub Actions pages.yml workflow

## Phase 1 — SHIPPED

Phase 1 is pushed, deployed, and live on GitHub Pages.

## Phase 2 Scope — COMPLETED

Plan: `docs/plans/2026-03-05-phase2-implementation.md`
Design: `docs/plans/2026-03-05-phase2-design.md`

- [x] Task 1: Print stylesheet (`main.css` — `@media print`)
- [x] Task 2: Diagram lightbox (`main.css` + `main.js`)
- [x] Task 3: lunr.js CDN + `search.json` data file
- [x] Task 4: Topnav search input + inline dropdown
- [x] Task 5: Crosswalk comparison selector page (`/crosswalks/compare/`)
- [x] Task 6: GitHub Pages enabled and site verified

## Phase 3 Backlog (historical carryover)

- Interactive standards graph — completed in Phase 9
- Functional-safety detail coverage — completed where corpus exists; future additions remain corpus-dependent
- SEMI S2/S8/S14 standard pages — completed in Phase 10

## Phase 4 Scope — COMPLETED

**Source:** `control-standards/work/design/simple_safety_system_design.md`

- [x] `docs/scenarios/machine-safety-implementation/index.md` — Scenario 06: Practical Machine Safety Implementation (10-step workflow, SIL/PL equivalence, Category B–4, device selection, example stack, Mermaid diagrams)
- [x] `docs/lifecycle/safety-wiring/index.md` — Safety Wiring Practices (24 VDC, NC contacts, dual-channel separation, wire gauge, color coding, termination, discrepancy time, baseline spec)
- [x] `docs/scenarios/index.md` — Scenario 06 card added
- [x] `docs/lifecycle/index.md` — safety-wiring row added to stage table
- [x] `docs/lifecycle/safety-architecture/index.md` — See Also link to safety-wiring added
- [x] `docs/lifecycle/detailed-design/index.md` — See Also link to safety-wiring added
- [x] Jekyll build clean (50 pages)

## Phase 5 Scope — IEC 62443 Cybersecurity Detail Pages — COMPLETED

**Rationale:** Cybersecurity is increasingly required alongside functional safety. Pairs with Scenario 04 (Networked Safety PLC). IEC 62443 corpus and full site pages close the visible gap.

### RAG Corpus (`control-standards/rag/standards_intelligence/international/cybersecurity/iec_62443/`)

- [x] `_index.yaml` — corpus index
- [x] `IEC62443_2_1__security_management.md` — IACS security management system, risk assessment process, security policy, asset inventory
- [x] `IEC62443_3_3__system_security_requirements.md` — Security Levels (SL 1–4), Zone/Conduit model, foundational requirements (FRs), system security requirements (SSRs)
- [x] `IEC62443_4_2__component_requirements.md` — component security requirements, embedded device requirements, software application requirements
- [x] `IEC62443_lifecycle.md` — IACS security lifecycle (assess → implement → maintain), patch management, incident response, SL-T vs SL-C distinction

### Site Pages

- [x] `docs/standards/cybersecurity/iec-62443/index.md` — full deepened page (badge: Phase 5 Complete), Zone/Conduit diagram, SL table, FR overview, lifecycle, SIL vs SL section, pairing with IEC 62061
- [x] `docs/standards/cybersecurity/index.md` — cybersecurity family page (IEC 62443 as full page entry)

### Nav / Index Updates

- [x] `docs/standards/index.md` — Cybersecurity section added with IEC 62443 entry
- [x] `docs/scenarios/networked-safety-plc/index.md` — IEC 62443 link added to related_standards; badge updated; routing note updated

### Build

- [x] Jekyll build clean — 52 pages

## Phase 6 Scope — Glossary — COMPLETED

**Rationale:** Engineers using the site encounter terms (SIL, PL, SCCR, AHJ, HFT, SFF, MTTFd)
across multiple pages with no single reference point. A cross-linked glossary closes this gap.

- [x] `docs/_data/glossary.yml` — 28 seed terms across Safety, Electrical, Standards Bodies, Regulatory domains
- [x] `docs/glossary/index.md` — rendered page with A-Z anchor strip, domain badges, standard links, lifecycle links, See Also cross-links
- [x] `docs/assets/css/main.css` — glossary entry card styles and domain badge variants
- [x] `docs/_includes/sidebar.html` — Glossary added to Reference section
- [x] Jekyll build clean

## Phase 7 Scope — Theme Switching — COMPLETED

**Rationale:** Engineers use reference sites in varied lighting environments. Dark mode
reduces eye strain during late-night or low-light reading. Following OS preference
requires zero user interaction while still allowing manual override.

- [x] `docs/assets/css/main.css` — new CSS variables for hardcoded colors; `[data-theme="dark"]` token block; `@media (prefers-color-scheme: dark)` fallback; toggle button styles
- [x] `docs/_layouts/default.html` — inline flash-prevention script in `<head>`
- [x] `docs/_includes/topnav.html` — theme toggle button (☾/☀)
- [x] `docs/assets/js/main.js` — toggle handler with `localStorage` persistence
- [x] Jekyll build clean

## Phase 8 Scope — NEC RAG Gap-Fill — COMPLETE

**Plan:** `docs/plans/2026-03-08-nec-missing-articles.md`
**Goal:** Add 9 missing NEC 2023 article files + update index/status files.

### Task 1 — Art 90 + Art 100 — COMPLETE
- [x] `NEC_2023__Art090__scope_and_purpose.md`
- [x] `NEC_2023__Art100__definitions.md`

### Task 2 — Art 500 + Art 504 — COMPLETE
- [x] `NEC_2023__Art500__hazardous_locations_general.md`
- [x] `NEC_2023__Art504__intrinsically_safe_systems.md`

### Task 3 — Art 505 (Zone Classification) — COMPLETE
- [x] `NEC_2023__Art505__zone_0_1_2_gas_vapors.md`

### Task 4 — Art 215 + Art 230 (Feeders and Services) — COMPLETE
- [x] `NEC_2023__Art215__feeders.md`
- [x] `NEC_2023__Art230__services.md`

### Task 5 — Art 700–702 (Emergency/Standby Systems) — COMPLETE
- [x] `NEC_2023__Art700_702__emergency_standby_systems.md` (combined file)

### Task 6 — Update _index.yaml + NEC_COMPLETION_STATUS + NEC_OVERVIEW — COMPLETE
- [x] All 8 new articles registered in `_index.yaml` (19 total indexed)
- [x] `NEC_COMPLETION_STATUS.md` updated to 19 articles
- [x] `NEC_OVERVIEW.md` updated with new article sections

### Additional items (from Art250.4 session)
- [x] `NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md` — committed
- [x] `_index.yaml` — NEC2023-Art250-4 entry added

## Phase 9 Scope — Interactive Standards Graph — COMPLETE

- [x] `docs/_data/standards_graph.yml` — 12 nodes, 14 edges
- [x] `docs/_includes/standards-graph.html` — Cytoscape.js include (mini + full modes)
- [x] `docs/standards/graph/index.md` — full interactive page
- [x] `docs/index.md` — mini graph replaces static Mermaid block
- [x] CSS legend and canvas styles in main.css
- [x] Cytoscape.js 3.28.1 CDN added to default layout

## Phase 10 Scope — Corpus Gap-Fill (IEC 60079 + SEMI S2/S8/S14) — COMPLETE

### IEC 60079 RAG Corpus
- [x] IEC60079_0__general_requirements.md
- [x] IEC60079_1__flameproof_Ex_d.md
- [x] IEC60079_10_1__area_classification_gas.md
- [x] IEC60079_11__intrinsically_safe_Ex_i.md
- [x] IEC60079_14__installation_design.md
- [x] IEC60079_17__inspection_maintenance.md
- [x] _index.yaml

### SEMI RAG Corpus
- [x] SEMI_S2__equipment_safety.md
- [x] SEMI_S8__ergonomics.md
- [x] SEMI_S14__fire_risk_assessment.md
- [x] _index.yaml

### Site Pages
- [x] docs/standards/hazardous-area/index.md
- [x] docs/standards/hazardous-area/iec-60079/index.md
- [x] docs/standards/semiconductor/index.md
- [x] docs/standards/semiconductor/semi/index.md
- [x] docs/standards/index.md updated (2 new families)
- [x] docs/scenarios/semiconductor-equipment/index.md updated

## Phase 11 Scope — Industry Overlay Depth — COMPLETE

### Petroleum / Oil & Gas
- [x] `docs/industries/petroleum/index.md` — deepened: standards matrix by phase, selection flow, checklist, all gap badges removed
- [x] `docs/scenarios/oil-gas-process-skid/index.md` — Scenario 07: ESD/F&G/HIPPS onshore skid

### Semiconductor
- [x] `docs/industries/semiconductor/index.md` — deepened: standards matrix by phase, SEMI S2 flow, all SEMI badges updated
- [x] `docs/scenarios/semiconductor-fab-tool/index.md` — Scenario 08: etch/CVD tool with gas control, HV interlocks

### Nav
- [x] `docs/scenarios/index.md` — Scenario 07 and 08 cards added
- [x] `docs/_includes/sidebar.html` — both new scenarios added

## Phase 12 Scope — Offshore / Marine Industry Overlay — COMPLETE

### RAG Corpus
- [x] `control-standards/rag/standards_intelligence/international/offshore/DNV_OS_D201__electrical_installations.md`
- [x] `control-standards/rag/standards_intelligence/international/offshore/ABS_offshore_electrical_control.md`
- [x] `control-standards/rag/standards_intelligence/international/offshore/_index.yaml`

### Site Pages
- [x] `docs/industries/offshore/index.md` — deepened: DNV/ABS standards matrix, IT earthing, LSOH, class approval checklist
- [x] `docs/industries/marine/index.md` — deepened: IMO framework, IEC 60092 overview, class society comparison
- [x] `docs/scenarios/offshore-platform-control/index.md` — Scenario 09: ESD/F&G/power management, IT earthing, LSOH, class FAT workflow

### Nav
- [x] `docs/scenarios/index.md` — Scenario 09 card added
- [x] `docs/_includes/sidebar.html` — Offshore Platform scenario link added

## RAG Layer — Electrical Knowledge Integration — COMPLETE

Design doc: `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

Transcript-derived electrical learning content promoted into the existing canonical RAG layers.

- [x] `training_modules/fundamentals/` — 7 circuit analysis + components files
- [x] `training_modules/electrical_machines/` — 9 motor/drive/servo files
- [x] `training_modules/nec_application/` — 3 NEC code-reading and application files
- [x] `design_framework/electrical_review/` — 4 calculation workflow files
- [x] `design_framework/motor_systems/` — 13 motor/drive design and workflow files
- [x] `commissioning_checklists/checklists/` — 6 motor, drive, and circuit checklist files
- [x] `standards_intelligence/crosswalks/overlap_notes/` — 2 motors/drives crosswalk files

EV motor files held as WIP. No new parallel layer created.

## Content Gaps (documented with badges on site)

- ISO 13849-1 — corpus complete (6 RAG files)
- IEC 62061 — corpus complete (4 RAG files + index)
- IEC 61508 — corpus complete (4 RAG files + index)
- IEC 61511 — corpus complete (4 RAG files + index)
- IEC 62443 — corpus complete (4 RAG files + index)
- IEC 60079 (hazardous area) — corpus complete (6 RAG files + index)
- SEMI S2/S8/S14 — corpus complete (3 RAG files + index)
- Medical, nuclear, marine class rules — not in corpus (no plan)

## Phase 13 Backlog (Secondary Backlog)

### RAG File Browser — COMPLETE
- [x] `tools/generate_rag_tree.py` — walks `control-standards/rag/`, outputs nested JSON
- [x] `docs/_data/rag_tree.json` — 236 file buttons, 7 top-level entries
- [x] `docs/_layouts/rag-browser.html` — two-panel layout (tree + content); marked.js + DOMPurify CDN
- [x] `docs/_includes/rag-tree-nodes.html` — recursive Jekyll include for nested `<details>` tree
- [x] `docs/rag-browser/index.md` — page at `/rag-browser/`
- [x] `docs/assets/js/rag-browser.js` — click handler, GitHub raw fetch, DOMPurify sanitization, mermaid re-init
- [x] `docs/assets/css/main.css` — RAG browser section (tree panel, file content, prose, states)
- [x] `docs/_includes/sidebar.html` — "RAG Files" link added to Reference section

### Training site pages — COMPLETE
- [x] `docs/training/index.md` — landing page, 24 modules, 3 groups
- [x] `docs/training/fundamentals/` — 8 pages
- [x] `docs/training/electrical-machines/` — 13 pages
- [x] `docs/training/nec-application/` — 3 pages
- [x] Sidebar: Training section added

### Thin industry pages — COMPLETE
- [x] `docs/industries/energy/index.md` — deepened: phase table, selection flow, key decisions, checklist
- [x] `docs/industries/food-and-beverage/index.md` — deepened: washdown, hygienic design gaps noted, checklist
- [x] `docs/industries/medical/index.md` — deepened: IEC 60601-1/ISO 14971 gaps noted, corpus status table, checklist
- [x] `docs/industries/nuclear/index.md` — deepened: IEEE 603/IEC 61513 gaps noted, corpus status table, checklist
- [x] `docs/industries/commercial/index.md` — deepened: NEC/IBC scope, Class 2 wiring, AHJ submittal, checklist

### Standards graph expansion — COMPLETE
- [x] IEC 60079 node — `docs/_data/standards_graph.yml` (12+ nodes; hazardous area family)
- [x] IEC 61511 node — functional safety family
- [x] SEMI S2/S8/S14 node — semiconductor family
- [x] Edges: IEC 60079 ↔ NEC (Zone via Art. 505), IEC 60079 ↔ IEC 61511 (hazardous-area process protection), SEMI ↔ IEC 60204-1, SEMI ↔ ISO 12100

### Glossary expansion — COMPLETE
- [x] Expanded from 28 terms to 45 terms
- [x] Added O&G/SEMI/hazardous-area terms: SIF, SRS, LOPA, PFDavg, IPL, EPL, T-code, Ex ia, SECS/GEM, PTI

### Crosswalk additions — COMPLETE
- [x] `docs/crosswalks/iec61511-iec61508/index.md` — IEC 61511 ↔ IEC 61508 (application vs. foundation); lifecycle comparison, SIL framework, architecture constraints, prior use, clause cross-reference
- [x] `docs/crosswalks/iec60079-nec-500-505/index.md` — IEC 60079 ↔ NEC Art. 500/505 (Zone vs. Division); classification tables, EPL, gas groups, equipment marking, protection types, installation rules
- [x] `docs/crosswalks/index.md` — updated with 2 new rows
- [x] `docs/_includes/sidebar.html` — 2 new crosswalk links added

## Phase 14 Scope — Training Curriculum Upgrade — COMPLETE

**Driver:** Training page review on 2026-03-10 found that `/training/` is structurally sound but still reads as a raw index instead of a learning system.
Plan: `docs/plans/2026-03-10-phase14-training-curriculum-implementation.md`
Design: `docs/plans/2026-03-10-phase14-training-curriculum-design.md`

### Landing page reframing
- [x] `docs/training/index.md` — replaced generic intro with learner-oriented copy; verification note; Start Here audience cards; learning paths; browse-by-topic cards; data-driven all-modules table with metadata chips; related standards strip; trust-boundary include retained
- [x] `docs/_data/training_catalog.yml` — shared data model for all 24 modules (level, time, type, focus, prerequisites, featured flag, learning paths, start-here, related standards)

### Learning structure
- [x] Four named learning paths: Controls Engineering Foundations, Motor and Drive Engineering, Industrial Panel Design (NEC Focus), Troubleshooting and Field Service
- [x] Three browse tracks renamed: Electrical Fundamentals, Motors, Drives, and Motion, NEC for Machines and Panels
- [x] All module summaries rewritten as outcome-focused descriptions in the catalog

### Information hierarchy
- [x] All Modules table replaces flat list — metadata columns (track, level, time, type); featured/core rows visually distinguished; mobile columns hidden via `.hide-mobile`
- [x] Training CSS section added to `docs/assets/css/main.css` — training chips, start-here cards, learning-path cards, related-standards strip, responsive rules
- [x] Group pages upgraded with group intro, recommended entry modules, and catalog-driven metadata tables
- [x] Sidebar labels updated to match display names (URLs unchanged)
- [x] Jekyll build: clean, 0.391 s

## Phase 15 Scope — Training Metadata And Module UX — COMPLETE

**Goal:** Make the training catalog scannable by difficulty, effort, prerequisite knowledge, and job context.

### Metadata model
- [x] `docs/_data/training_catalog.yml` exists with level, time, type, focus, prerequisites, featured flag for all 24 modules (completed in Phase 14)
- [x] Modules classified with Core (featured) badge; level/type/focus fields serve as status markers
- [x] Per-module metadata surfaced on individual pages via dedicated layout

### Page/application work
- [x] `docs/_layouts/training-module.html` — dedicated layout that looks up module metadata from catalog by `page.url`; renders level chip, time, type, focus, Core badge, outcome sentence, and prerequisites before page content
- [x] CSS added: `.module-meta-bar`, `.module-outcome`, `.module-prereqs`
- [x] All 24 module pages updated: `layout: training-module`, page-header div removed (layout handles it), breadcrumb labels updated to new display names
- [x] Jekyll build: clean, 0.535 s
- [x] Acceptance target met: every module page shows difficulty, time, type, outcome, and prerequisites without opening any other page

## Phase 16 Scope — NEC Training Expansion — COMPLETE

**Goal:** Rebalance the training catalog so NEC application is not limited to only three modules.

### Canonical RAG additions
- [x] Expand `control-standards/rag/training_modules/nec_application/` from 3 to 11 modules
- [x] branch_circuits_vs_feeders_motor_loads.md
- [x] disconnecting_means_for_machinery.md
- [x] grounding_bonding_control_panels.md
- [x] sccr_workflow.md
- [x] conductor_ocpd_sizing_examples.md
- [x] class1_class2_remote_control_circuits.md
- [x] article_430_practical_workflow.md
- [x] article_409_practical_workflow.md

### Site follow-through
- [x] 8 new site pages under `docs/training/nec-application/`
- [x] `docs/_data/training_catalog.yml` — 8 new entries, module_count updated to 11, panel-design-nec path expanded
- [x] NEC group index page: description updated to 11 modules, recommended entry modules updated
- [x] Footer nav chain complete across all 11 NEC modules
- [x] `docs/_data/rag_tree.json` regenerated (249 files)
- [x] Jekyll build: clean (0.529 s)
- [x] Acceptance target met: NEC track covers practical machine and panel design work end-to-end

## Phase 17 Scope — Cross-Layer Knowledge Routing — COMPLETE

**Plan:** `docs/plans/2026-03-11-phase17-cross-layer-routing.md`
**Decision:** Workflows as first-class `/workflows/` site section (Option A)

### `/workflows/` section
- [x] `docs/workflows/index.md` — landing page with workflow cards by category
- [x] `docs/workflows/motor-selection/index.md` — Motor Selection Workflow
- [x] `docs/workflows/motor-troubleshooting/index.md` — Motor Troubleshooting Decision Tree
- [x] `docs/workflows/vfd-commissioning/index.md` — VFD Commissioning Workflow
- [x] `docs/workflows/servo-commissioning/index.md` — Servo Commissioning Workflow
- [x] `docs/workflows/electrical-review/index.md` — Electrical Review Workflow

### Cross-layer data model
- [x] `docs/_data/training_catalog.yml` — `related_workflows` field added to 7 modules; Machine Lifecycle learning path added
- [x] `docs/_layouts/training-module.html` — Related Workflows block rendered on module pages

### Navigation
- [x] `docs/_includes/sidebar.html` — Workflows section added (5 workflow links)
- [x] `docs/assets/css/main.css` — Workflow card grid, badges, wf-tags, related-workflows block CSS

### Build
- [x] Jekyll build: clean, 0.583 s, 107 pages

## Phase 18 Track A — Control Systems Training Surfacing — COMPLETE

**Plan:** `docs/plans/2026-03-11-phase18-control-systems-training.md`

### Control Systems group (7 modules)
- [x] `docs/training/control-systems/index.md` — group landing page
- [x] `docs/training/control-systems/control-theory-overview/index.md`
- [x] `docs/training/control-systems/pid-foundation/index.md`
- [x] `docs/training/control-systems/pid-intuition/index.md`
- [x] `docs/training/control-systems/industrial-pid/index.md`
- [x] `docs/training/control-systems/control-loop-architectures/index.md`
- [x] `docs/training/control-systems/pid-heater-control/index.md`
- [x] `docs/training/control-systems/pid-drone-control/index.md`

### Fundamentals group addition — IEC Earthing Systems
- [x] `docs/training/fundamentals/earthing-systems-iec/index.md` — IEC Earthing System Types (TN-C, TT, TN-C-S, TN-S, IT)

### Data model and navigation
- [x] `docs/_data/training_catalog.yml` — control-systems topic group, 7 module entries, Control Systems Engineering learning path, start-here audience card, fundamentals count 8→9, earthing module entry
- [x] `docs/_includes/sidebar.html` — Control Systems link added under Training section

### Build
- [x] Jekyll build: clean, 0.629 s, 116 pages

## Phase 18 Track B — Field Engineering Section — COMPLETE

- [x] `docs/_data/field_checklists.yml` — flat YAML catalog (6 entries)
- [x] `docs/_layouts/field-checklist.html` — new layout with Liquid data lookup, cross-links, back link
- [x] CSS additions to `docs/assets/css/main.css` — `.checklist-body`, `.field-checklist__cross-links`, print rules
- [x] `docs/field-engineering/index.md` — landing page with workflow-card-grid
- [x] 6 checklist pages under `docs/field-engineering/`
- [x] Sidebar: Field Engineering section added
- [x] Reverse links: `related_checklists` in 11 training modules + "Related Checklists" sections in 5 workflow pages
- [x] Jekyll build: clean, 123 pages

## Phase 18 Track C — Reference Section + Commissioning Templates Redesign — COMPLETE

**Design spec:** `docs/superpowers/specs/2026-03-14-reference-section-commissioning-templates-design.md`

- [x] `/reference/` landing page (2 card groups: Architecture, Motor Systems)
- [x] `/reference/architecture/machine-architecture-model/` — 7-Layer model from RAG
- [x] `/reference/architecture/machine-safety-architecture/` — Universal safety architecture template
- [x] `/reference/architecture/compliance-stack/` — 15-Standard minimum compliance stack
- [x] `/reference/motor-systems/motor-selection-matrix/` — Motor selection flowchart + matrix
- [x] Sidebar "Reference Models" block with `.sidebar__group-label` sub-groups
- [x] `.sidebar__group-label` CSS added to `main.css`
- [x] `/field-engineering/` → `/commissioning-templates/` rename: 7 pages moved, redirect at old index
- [x] `field-checklist.html` layout: label updated, template header block, checkbox DOM script, back-link updated
- [x] CSS: `.template-header`, `.checklist-item`, print checkbox styles
- [x] `field_checklists.yml`: all 6 URL entries updated
- [x] `training_catalog.yml`: 13 URL references updated across 11 modules
- [x] 5 workflow pages: all `/field-engineering/` hrefs updated
- [x] Cross-links: motor-selection workflow → motor-selection-matrix; semiconductor-equipment scenario → machine-architecture-model; semiconductor industry → compliance-stack
- [x] Jekyll build: clean, 129 pages

## Phase 19 Scope — Engineering Workflow Navigation Refactor — COMPLETED

**Plan:** `docs/plans/2026-03-13-phase19-engineering-workflow-navigation.md`

- [x] Created `docs/_data/navigation.yml` — 5-group sidebar data model (Engineering Workflow, Standards, Training, Industries, Reference)
- [x] Refactored `docs/_includes/sidebar.html` from 135-line hardcoded HTML to ~60-line data-driven Liquid renderer
- [x] Added `/engineering-workflow/` hub page with 5 task-grouped sections (Design & Architecture, Select & Size, Commission & Verify, Troubleshoot, Scenarios)
- [x] Expanded `/reference/` landing page with Quick Reference section (Glossary, Crosswalks, Software Stack, RAG File Browser)
- [x] Demoted Scenarios, Crosswalks, and Workflows from top-level sidebar into Engineering Workflow and Reference hub groups
- [x] Jekyll build: clean, 132 pages

## Phase 20 Scope — Software Safety Stack Deepening — COMPLETE

**Sources:** `planning/safety_software_stack.md`, `docs/superpowers/specs/2026-03-15-software-safety-stack-phase20-design.md`

- [x] RAG corpus updated: IEC 61131-3:2025 edition note; Normal PLC vs Safety PLC vs SIS comparison table; expanded E-stop section with canonical tag names, I/O list, 7-rung pseudocode, sequence of operation, documentation checklist, logging checklist; Rockwell GuardLogix and Siemens S7-1500F vendor patterns
- [x] `/software-stack/` site page updated: edition note, comparison table section, expanded E-stop with Mermaid wiring/architecture and state machine diagrams, vendor-specific `<details>` blocks
- [x] Jekyll build: clean, 132 pages

## Phase 21 Scope — Lifecycle Stage Page Expansion — COMPLETE

**Objective:** Transform all lifecycle stage pages from thin stubs into comprehensive engineering references with detailed guidance, decision criteria, cross-links, and practical examples.

### Pages Expanded (Existing → Full)
- [x] `docs/lifecycle/index.md` — lifecycle overview with introduction section and 13-stage table
- [x] `docs/lifecycle/concept/index.md` — Stage 01 (42 lines → ~300 lines)
- [x] `docs/lifecycle/standards-selection/index.md` — Stage 02 (59 lines → ~500 lines)
- [x] `docs/lifecycle/risk-assessment/index.md` — Stage 03 (62 lines → ~600 lines)
- [x] `docs/lifecycle/safety-architecture/index.md` — Stage 04 (67 lines → ~770 lines)
- [x] `docs/lifecycle/detailed-design/index.md` — Stage 05 (58 lines → ~680 lines)
- [x] `docs/lifecycle/draft-documentation/index.md` — Stage 06 (41 lines → ~580 lines)
- [x] `docs/lifecycle/build/index.md` — Stage 07 (74 lines → ~760 lines)
- [x] `docs/lifecycle/installation/index.md` — Stage 08 (46 lines → ~580 lines)
- [x] `docs/lifecycle/pre-commissioning/index.md` — Stage 09 (46 lines → ~800 lines)
- [x] `docs/lifecycle/commissioning/index.md` — Stage 10 (60 lines → ~1000 lines)
- [x] `docs/lifecycle/maintenance/index.md` — Stage 11 (57 lines → ~1000 lines)

### Pages Created (New)
- [x] `docs/lifecycle/safety-requirements-spec/index.md` — Stage 3.5 (new)
- [x] `docs/lifecycle/management-of-change/index.md` — Stage 12 (new)

### Content Pattern (All Pages)
Each expanded lifecycle stage page includes:
- Purpose and scope summary
- Key decisions and decision criteria
- Related standards and standards guidance
- Practical guidance with checklists or step-by-step instructions
- Cross-links to related training modules, workflows, and reference material
- See Also links to adjacent lifecycle stages

### Build
- [x] Jekyll build: clean, 132 pages (no change from Phase 20)

## Phase 22 State — Semiconductor Facility Reference (In Progress)

**Last verified:** 2026-04-11

### Step 0 — Hygiene — COMPLETE
- [x] AI_READ_ACCESS headers fixed on 7 RAG files (IEC 62443 + reference models)
- [x] `validate_ai_boundaries.py` passes 305/305 (now 316/316 after RAG promotion)
- [x] `validate_reorg.sh all` passes 49/50 (archive check is pre-existing known gap)
- [x] `planning/semi_facility/` committed as draft (was untracked)

### Step 1 — Promote System and Instrumentation Notes into RAG — COMPLETE
- [x] Created `control-standards/rag/design_framework/semiconductor_facility/` with `_index.yaml`
- [x] 10 files promoted from staging with updated headers (AI_READ_ACCESS: ALLOWED, CONTENT_CLASS: DERIVED_REFERENCE):
  - `bulk_specialty_gas.md`
  - `bulk_chemical_distribution.md`
  - `upw_and_wastewater.md`
  - `exhaust_abatement_vacuum.md`
  - `hvac_and_cleanroom.md`
  - `safety_and_shutdown.md`
  - `tool_facility_interface.md`
  - `common_control_philosophy.md`
  - `instrumentation_use_matrix.md`
  - `instrumentation_selection.md`

### Step 2 — Build Jekyll Section (First Slice) — COMPLETE
- [x] `docs/industries/semiconductor/facility/index.md` — overview + standards selection flowchart + cross-cutting design threads
- [x] `docs/industries/semiconductor/facility/bulk-specialty-gas/index.md`
- [x] `docs/industries/semiconductor/facility/upw-wastewater/index.md`
- [x] `docs/industries/semiconductor/facility/exhaust-abatement/index.md`
- [x] `docs/industries/semiconductor/facility/tool-facility-interface/index.md`
- [x] `docs/industries/semiconductor/facility/instrumentation/index.md`

### Step 3 — Wire Navigation and Cross-Links — COMPLETE
- [x] `docs/_data/navigation.yml` — Semiconductor Facility sub-tree added under Industries > Semiconductor
- [x] `docs/industries/semiconductor/index.md` — Semiconductor Facility Reference table added at bottom
- [x] Jekyll build: clean, **148 pages**

### Second Slice — COMPLETE
- [x] `docs/industries/semiconductor/facility/hvac-cleanroom/index.md` — room pressure cascade, ISO 14644, particle monitoring
- [x] `docs/industries/semiconductor/facility/bulk-chemical/index.md` — storage, transfer sequencing, containment, SEMI F39/F57
- [x] `docs/industries/semiconductor/facility/safety-shutdown/index.md` — 4-layer shutdown model, cause-and-effect, SIL integration
- [x] `docs/industries/semiconductor/facility/control-philosophy/index.md` — modes, state machine, permissives/interlocks/trips, safe-state rules
- [x] Facility overview page updated to include all 9 system pages
- [x] Navigation.yml updated with 4 new entries
- [x] Semiconductor industry page cross-link table updated
- [x] Jekyll build: clean, **152 pages**

**Original planning context:**

### Baseline Reality

- Jekyll site and GitHub Pages deploy are real and working: `docs/_config.yml` + `.github/workflows/pages.yml`
- Actual build output: **142 HTML files** (earlier entries said 132 — corrected)
- Existing semiconductor coverage is **equipment-focused**, not facility-focused:
  - `docs/industries/semiconductor/index.md`
  - `docs/standards/semiconductor/index.md`
  - `docs/scenarios/semiconductor-fab-tool/index.md`
- `planning/semi_facility/` is draft-only and currently untracked in git, but is **much more complete than it looks** — see Staging Inventory below

### Staging Inventory (`planning/semi_facility/`)

The staging area already covers `build_sequence.md` Phase 1 (governance, systems map, standards gap map) and Phase 2 (normalized utility system notes). It is effectively at Phase 3 territory. The bottleneck is **promotion and presentation**, not content creation.

**systems/** — 7 normalized system notes (~80 lines each):
- `bulk_specialty_gas_systems.md`
- `bulk_chemical_distribution_and_wet_process.md`
- `upw_and_wastewater_systems.md`
- `exhaust_abatement_and_vacuum.md`
- `hvac_and_cleanroom_environment.md`
- `safety_and_shutdown_architecture.md`
- `tool_facility_interface.md`
- `common_control_philosophy.md`

**instrumentation/** — 6 files including site-ready reference material:
- `semiconductor_facility_instrumentation_use_matrix.md` (153 lines)
- `manufacturer_product_family_comparison.md` (151 lines)
- `selection_principles.md`, `measurement_and_alarm_strategy.md`, `device_family_map.md`

**standards/** — structured selection flowchart, plain-language family explanations, full candidate table (`candidate_standards_map.md`)

**sources/** — 30+ sources registered with trust labels and next-action notes (`public_source_register.md`)

Total: ~1,434 lines across 15 substantive files.

### Repo Hygiene Issues (fast fixes, do first)

- `python3 tools/validate_ai_boundaries.py` fails on **7 RAG files** missing `AI_READ_ACCESS`: all 4 IEC 62443 files + `IEC62443_lifecycle.md` + `15-Standard Minimum Compliance Stack.md`. Mechanical header fix, ~15 minutes.
- `bash tools/validate_reorg.sh all` shows 48/50 — both failures are downstream of the AI boundary script. Once the 7 files are fixed, validator passes cleanly.

### Approach

Implement the semiconductor facility reference **inside the existing Jekyll site**, not a separate repo.

- Treat it as a **facility-side utilities and interface library**, distinct from the current equipment-oriented SEMI content
- Root the Jekyll section at `/industries/semiconductor/facility/` — existing semiconductor overlay stays the entry point
- Promote system and instrumentation notes → `control-standards/rag/design_framework/semiconductor_facility/`
- Promote standards family notes → `control-standards/rag/standards_intelligence/international/semiconductor/semi_facility/`
- Add nav entry under existing Industries > Semiconductor block in `docs/_data/navigation.yml`

### Implementation Order

**Step 0 — Hygiene (15 min)**
- Add `AI_READ_ACCESS: ALLOWED` header to the 7 failing RAG files
- Commit `planning/semi_facility/` as draft (untracked, needs to be in git)
- Verify `validate_reorg.sh all` passes 50/50

**Step 1 — Promote system and instrumentation notes into RAG**

Target directory: `control-standards/rag/design_framework/semiconductor_facility/`

| Staging file | RAG target |
|---|---|
| `systems/bulk_specialty_gas_systems.md` | `bulk_specialty_gas.md` |
| `systems/bulk_chemical_distribution_and_wet_process.md` | `bulk_chemical_distribution.md` |
| `systems/upw_and_wastewater_systems.md` | `upw_and_wastewater.md` |
| `systems/exhaust_abatement_and_vacuum.md` | `exhaust_abatement_vacuum.md` |
| `systems/hvac_and_cleanroom_environment.md` | `hvac_and_cleanroom.md` |
| `systems/safety_and_shutdown_architecture.md` | `safety_and_shutdown.md` |
| `systems/tool_facility_interface.md` | `tool_facility_interface.md` |
| `systems/common_control_philosophy.md` | `common_control_philosophy.md` |
| `instrumentation/semiconductor_facility_instrumentation_use_matrix.md` | `instrumentation_use_matrix.md` |
| `instrumentation/selection_principles.md` | `instrumentation_selection.md` |

Add `AI_READ_ACCESS: ALLOWED` + `CONTENT_CLASS: DERIVED_REFERENCE` on each file at promotion. Do not restructure — content is clean.

**Step 2 — Build the Jekyll section (first slice)**

Pages to build, in order:
1. `docs/industries/semiconductor/facility/index.md` — overview + standards stack (use selection flowchart from `candidate_standards_map.md`)
2. `docs/industries/semiconductor/facility/bulk-specialty-gas/` — from promoted RAG
3. `docs/industries/semiconductor/facility/upw-wastewater/` — from promoted RAG
4. `docs/industries/semiconductor/facility/exhaust-abatement/` — from promoted RAG
5. `docs/industries/semiconductor/facility/tool-facility-interface/` — from promoted RAG
6. `docs/industries/semiconductor/facility/instrumentation/` — use matrix is essentially site-ready

Second slice (after first slice ships): HVAC, chemicals, safety/shutdown architecture.

**Step 3 — Wire navigation and crosslinks**
- Add `Semiconductor Facility` entry under Industries > Semiconductor in `navigation.yml`
- Cross-link from `docs/industries/semiconductor/index.md` into facility section
- Add See Also links on existing SEMI S2/S8/S14, IEC 61511, NFPA 79, NEC pages where relevant

### Source Files for Phase 22

- `planning/semi_facility/README.md` — corpus overview and promotion rules
- `planning/semi_facility/standards/candidate_standards_map.md` — standards targets and selection flowchart
- `planning/semi_facility/roadmap/build_sequence.md` — original 4-phase build order (Phase 1+2 already done)
- `planning/semi_facility/systems/facility_systems_map.md` — system scope boundaries
- `planning/semi_facility/sources/public_source_register.md` — source governance (30+ sources registered)

## Phase 24 — Training Visual Upgrades — COMPLETE

**Status:** Complete (2026-04-13)
**Branch:** `feat/phase24-training-visual-upgrades`

### Completed work

- [x] `docs/training/fundamentals/earthing-systems-iec/index.md` — visual upgrade package from `planning/ground_earth_visual.md`
  - Overview fault-return flowchart after IEC letter-code tables
  - Compact topology diagrams for TN-C, TT, TN-C-S, TN-S, IT
  - Per-system blockquote callout cards (fault return / protection / main risk)
  - Machine designer takeaway line under each system
  - Expanded practical comparison table (5 columns, bold System names)
  - Selection logic decision tree before practical questions section

- [x] `docs/scenarios/semiconductor-fab-tool/index.md` — visual aids from `planning/semi_facility/semiconductor_fab_tool_visual_aids.md`
  - Design Workflow Overview (4-phase LR flowchart)
  - Process Start Permissive Flow (5-permissive gate chain)
  - Fault Trip Sequence (fail-safe de-energize + latch + manual reset)
  - HV Access Interlock Flow (capacitor discharge polling loop)
  - Cybersecurity Zone Diagram (fab host → firewall → tool controller; Safety PLC hardwired-only)

### Build
- Jekyll build: clean (no errors), 157 pages
