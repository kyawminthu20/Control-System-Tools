# Roadmap — Consolidating Control System Knowledge

**Owner intent:** consolidate practical control-system knowledge — not just
what standards require, but how work is actually done in the field: wiring,
sizing, protection, noise mitigation, device by device, with real-life
knowledge and the appropriate standards cited.

**Status field:** update this file as phases complete (it is part of the
phase loop, like `project_state/`).

## The Wiring & Installation Guides Program

**All four waves complete (2026-07-11) — 16 guides live, all Review pending.**

New content genre at `docs/design/wiring/` (Design section). Every guide
follows the wiring-guide template in
[CONTENT_STANDARDS.md](CONTENT_STANDARDS.md) §5 and integrates the three
existing assets: corpus standards knowledge, `cst` calculations, and field
practice captured through the knowledge-intake loop (§ below).

### Device coverage matrix

| Wave | Phase | Guides | Status |
|---|---|---|---|
| 1 — Foundations | 38 | **How to wire a VFD** (flagship, sets the template) · Wire-sizing walkthrough (cst-driven: ampacity + voltage drop + Art. 430) · Panel grounding & bonding practice · Noise & EMC mitigation | **Done 2026-07-11** (Review pending) |
| 2 — Controllers & I/O | 39 | PLC wiring (power, DI/DO, sourcing/sinking, commons, fusing) · Remote I/O stations (network + power + commons across drops) · IPC / industrial PC (power/UPS, grounding, environment, ports) · 4–20 mA current loops (2/3/4-wire, loop power, shields, isolators) · 0–10 V signals (when voltage is acceptable, commons, distance limits) | **Done 2026-07-11** (Review pending) |
| 3 — Motion & feedback | 40 | Servo drive wiring (power, motor, feedback, STO, brake) · Encoder wiring (differential vs single-ended, TTL/HTL, cable spec, shields) | **Done 2026-07-11** (Review pending) |
| 4 — Infrastructure & safety | 41 | Communication cable installation (Ethernet/RS-485/PROFIBUS field practice in machines — routing, termination, segregation; cross-links the communications physical-layer pages) · Safety circuit wiring (e-stop chains, safety relays, monitored reset) · Motor starters (DOL/reversing/star-delta) · Control power distribution (CPT vs PSU, fusing scheme) · RTD & thermocouple wiring | **Done 2026-07-11** (Review pending) |

### After the wiring program

| Phase | Program | Why |
|---|---|---|
| 42 | **Troubleshooting engine** — DONE 2026-07-11 (Review pending): 4 decision-tree pages (VFD faults, motor-won't-start, analog signal faults, comms dropouts) + corpus troubleshooting_engine module populated | Field pattern-recognition is the least Google-able knowledge here |
| 43 | **IEC 61131-3 / PLC software** — DONE 2026-07-11 (Review pending): 4 pages under /fundamentals/plc-software/ + corpus training_modules/plc_software module | Longest-standing known corpus gap; pairs with cst tag tooling |
| 44 | **Communications expansion** — DONE 2026-07-11 (Review pending): EtherCAT, HART, DNP3, IEC 61850 pages added (Foundation Fieldbus, wireless, TSN, capture library, SVG diagrams remain future) | Deferred by design until fundamentals/diagnostics matured |

### Standing threads (parallel to all phases)

- **Author review passes** — flip AI-drafted pages from *Review pending* to
  *Reviewed* (only the author does this)
- **Standards depth passes** — Phase 30.3–30.8 (IEC 60204-1 next; spec in
  `project_state/project_state.md` history)
- **cst data hand-offs** — licensed NEC tables into `data/standards_tables/`,
  a real scrubbed I/O list, Saleae captures, live-controller exercise
- **Diagrams** — original SVG wiring/terminal diagrams added incrementally
  (guides ship text+table-first; never vendor screenshots)

## Intake Batch 2026-07-11 (`temp/` + `drawings examples/`)

Digested and planned 2026-07-11 (plan file: session record; triage per
AI_WORKFLOW §5). Items stay in place until their phase executes — each phase
below records the relocation so nothing is lost.

| Phase | Program | Source material | Status |
|---|---|---|---|
| 45 | **Standards accuracy pass** — see `planning/2026-07-11-standards-accuracy-review.md` (review + full triage record appended). | `planning/2026-07-11-standards-accuracy-review.md` | **DONE 2026-07-12** |
| 46 | **Visual assets** — wire-color-coding gallery guide at `/design/wiring/wire-color-coding/` (17 diagrams grouped per the asset README, alt text from assets.json, AHJ/customer-drawings precedence caveat, corpus note, diagram-grid CSS adapted from MkDocs vars to site tokens) + the design-package poster embedded on `/tools/templates/` (products-shown-are-examples caption) and cross-linked from scenarios. Assets move to `docs/assets/images/`. | `temp/wire-color-coding-web-assets/`, `drawings examples/` | Planned — quick win |
| 47 | **PLC software expansion** — 4 new pages + corpus notes in `/fundamentals/plc-software/`: Ladder Logic Fundamentals (primitives, seal-in, one-shots, scan order, alarm hysteresis, analog scaling) · PLC Algorithms & Equipment Staging (FIFO/queues, lead-lag, runtime/capacity staging, load shedding; cross-links water-wastewater) · PackML/ISA-88/ISA-95 (deepens machine-state/architecture models, no duplication) · Vendor Programming Architectures (Siemens OB/FB/DB vs Logix tags/AOI vs TwinCAT OO — consolidates both source docs' philosophy comparison, written once). Source discipline: strip `utm_source` params, re-verify all citations, paraphrase only. Source doc relocates to `control-standards/work/` (intake-loop capture tier). | `temp/plc_software.md` | Planned |
| 48 | **PLC/IPC hardware reference + vendor documentation index** — xlsx → `docs/_data/manufacturers/vendor_doc_links.yml` → `/tools/manufacturers/vendor-documentation/` (~130 official-manual links: portal/manual/pub-ID/URL/notes); `/tools/manufacturers/plc-hardware-families/` from plcs.md (data-driven family tables, Mermaid selection flowchart, suffix decoding; ALL lifecycle/market claims dated "as of July 2026" and marked verify-current; positioning language softened). NOTE: `docs/vendor/` is the Jekyll Ruby bundle, not a content home. Sources relocate to `control-standards/work/` (md) and `planning/` (xlsx). | `temp/plcs.md`, `temp/PLC_IPC_Official_Reference_Links.xlsx` | Planned |

### Research Tracks (recorded, deliberately not scheduled)

**AI/ML for Control Systems** — the owner's staging workspace
(`temp/ai-ml-control-systems-research/`, 5 files: digital-twin integration
spine, 6-level authority model, model-family capability map, source register,
scientific-domain mapping). Self-labeled non-authoritative with an explicit
do-not-build-yet posture, which this roadmap honors.

- **Relocation (when touched next):** → `control-standards/work/research/ai-ml-control-systems/` (work tier)
- **Promotion criteria before ANY site/corpus content:** the source-register
  "still needed" gaps filled; the two arXiv preprints re-checked for
  supersession; peer-reviewed vs vendor claims separated; the owner decides
  taxonomy placement (candidates: Fundamentals or Design); corpus-first
  authoring via the promotion checklist; least-authority framing (offline →
  read-only → advisory → … → closed-loop) preserved; safety functions stay
  independent of any AI path.

### Backlog (recorded from the third review, not scheduled)

- **Standards-family expansion wishlist** (robotics ISO 10218-1/-2 + ISO/TS
  15066, B11, NFPA 70E, IEEE 1584, ISA-18.2/IEC 62682, ISA-5.1/88/95,
  IEC 61499/61800-5-2, additional UL/CSA panel standards, SEMI S10/S22/F47/
  E-series, NIST SP 800-82/CSF, IEC 61784/61850 parts, …). Each addition is a
  corpus-first effort with real copyright exposure — clause-level coverage
  must stay paraphrase (CONTENT_STANDARDS §2). Adopt selectively by project
  need, not as a bulk import.
- **Three-level page architecture** (Simple / Engineering / Design-guide
  variants + 19-section master template) — evaluate after Phase 45 lands;
  conflicts partially with the established Phase-30 eight-section template.

## The Knowledge-Intake Loop (how real-life knowledge gets in)

1. **Capture** — the author brain-dumps field lessons into
   `control-standards/work/` in any rough form (bullet notes, transcripts,
   war stories). No polish required; this tier is non-authoritative by
   definition.
2. **Normalize** — an agent session paraphrases the notes into corpus form
   (metadata headers, original language, no third-party material) and runs
   the promotion checklist in `control-standards/governance/`.
3. **Publish** — guides and pages draw on the promoted corpus notes; new
   pages start at *Review pending*.
4. **Review** — the author validates and flips status.

Field knowledge enters ONLY through this loop — agents do not invent field
practice. Where a guide states practice not yet in the corpus, it must be
marked as generally-accepted practice with a verify note, and the gap
queued for capture.
