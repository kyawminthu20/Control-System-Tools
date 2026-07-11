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
| 44 | **Communications expansion** (35.4 backlog) — EtherCAT, DNP3, IEC 61850, HART, FF, wireless, TSN; capture library; interface-neutral diagrams | Deferred by design until fundamentals/diagnostics matured |

### Standing threads (parallel to all phases)

- **Author review passes** — flip AI-drafted pages from *Review pending* to
  *Reviewed* (only the author does this)
- **Standards depth passes** — Phase 30.3–30.8 (IEC 60204-1 next; spec in
  `project_state/project_state.md` history)
- **cst data hand-offs** — licensed NEC tables into `data/standards_tables/`,
  a real scrubbed I/O list, Saleae captures, live-controller exercise
- **Diagrams** — original SVG wiring/terminal diagrams added incrementally
  (guides ship text+table-first; never vendor screenshots)

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
