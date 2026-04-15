# Phase 25 Design: Water/Wastewater Multi-Page Section

**Date:** 2026-04-14
**Status:** Approved
**Phase:** 25

---

## Overview

Add a multi-page Water/Wastewater reference section to the Jekyll site, covering both municipal drinking water treatment and industrial wastewater treatment. Mirrors the structure and depth of the existing semiconductor facility section (Phases 22–23).

---

## File & URL Structure

### Jekyll Pages

```
docs/industries/water-wastewater/
├── index.md                              # Overview + standards stack
├── intake-pumping/index.md               # Intake & raw water pumping
├── filtration-clarification/index.md     # Filtration & clarification
├── chemical-dosing/index.md              # Chemical dosing (Cl, coagulation, pH)
├── distribution-scada/index.md           # Distribution SCADA & telemetry
├── equalization-neutralization/index.md  # Industrial WW: equalization & neutralization
├── treatment-discharge/index.md          # Industrial WW: treatment & discharge
└── instrumentation/index.md             # Instrumentation reference
```

### RAG Corpus

```
control-standards/rag/design_framework/water_wastewater/
├── _index.yaml
├── overview_and_standards.md
├── intake_and_pumping.md
├── filtration_and_clarification.md
├── chemical_dosing.md
├── distribution_scada_telemetry.md
├── equalization_and_neutralization.md
├── treatment_and_discharge.md
└── instrumentation_reference.md
```

### Navigation

- Add "Water/Wastewater" entry to `docs/_data/navigation.yml` under the Industries group
- Sub-links for all 7 sub-pages
- "In This Section" navigation block on the overview page

---

## Standards Coverage

| Standard | Scope |
|---|---|
| IEC 61511 | SIL-rated safety functions (high-level shutdown, chemical OT/UV fail-safe) |
| IEC 62443 | SCADA/telemetry cybersecurity zones, remote access segmentation |
| ISA-18.2 | Alarm philosophy, alarm rationalization |
| AWWA M31/M36 | Distribution system design, water loss control |
| EPA SDWA / CWA | Safe Drinking Water Act compliance; Clean Water Act discharge limits |
| NFPA 820 | Hazardous area classification in wastewater facilities |
| NFPA 70 / NEC | Wet/corrosive environment wiring, submerged pump circuits |

---

## Per-Page Content Pattern

Every page follows this structure (consistent with the semiconductor facility pages):

1. Purpose & scope callout box
2. Standards selection table (which standards apply and why)
3. Control narrative (sequence of operation)
4. Mermaid diagrams (minimum 2 per page)
5. Key engineering decisions
6. Instrumentation list
7. Cross-links to lifecycle stages and related training modules

---

## Mermaid Visual Plan

| Page | Diagram 1 | Diagram 2 | Diagram 3 |
|---|---|---|---|
| Overview | Standards selection flowchart | Section navigation map | — |
| Intake & Pumping | Pump station control architecture | Start permissive chain (level, pressure, VFD ready) | — |
| Filtration & Clarification | Filter run / backwash cycle state machine | Turbidity-driven filter bypass logic | — |
| Chemical Dosing | Dosing loop control flow (flow-paced + feedback trim) | Chlorine OT / UV fail-safe shutdown sequence | Chemical feed interlock chain |
| Distribution SCADA | SCADA zone diagram (RTU → SCADA → historian) | IEC 62443 security zone map | Telemetry failure fallback logic |
| Equalization & Neutralization | Equalization basin level control state machine | pH neutralization control loop | — |
| Treatment & Discharge | Treatment train flow (biological → settling → effluent) | Permit limit trip logic (TOC, TSS, pH) | — |
| Instrumentation | Analyzer loop architecture (4-20mA + HART) | Instrument selection decision tree | — |

All diagrams use Mermaid (`flowchart LR`, `flowchart TD`, or `stateDiagram-v2`), consistent with the Phase 24 visual style.

---

## Build Order

1. **RAG corpus** — author all 8 RAG files with proper AI boundary headers and `_index.yaml`
2. **Jekyll pages** — promote each RAG file into a site page, add Mermaid diagrams and cross-links
3. **Navigation** — wire into `navigation.yml`, add "In This Section" block to overview
4. **Validation** — run `python3 tools/validate_ai_boundaries.py` and `bundle exec jekyll build` (must be clean)

RAG files are independent of each other and can be authored in any order. Each RAG file must be complete before its corresponding Jekyll page is built.

---

## Scope Summary

- 8 new RAG files
- 8 new Jekyll pages
- 1 navigation update (`navigation.yml`)
- ~20 Mermaid diagrams total
- Page count: 157 → ~165 pages

---

## Out of Scope

- Interactive filtration or dosing calculators
- Real SCADA data integration
- Medical, nuclear, or marine content
- Search or site-wide UX changes

---

## Constraints

- RAG files must have `AI_READ_ACCESS: ALLOWED` and `CONTENT_CLASS: DERIVED_REFERENCE` headers
- Jekyll site is the presentation layer only — authoritative content stays in `control-standards/rag/`
- No new CSS frameworks; vanilla CSS only
- Jekyll build must remain clean (0 errors, 0 warnings)
