# Corpus Gap-Fill: IEC 60079 + SEMI S2/S8/S14 — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Phase:** Phase 10

## Overview

Add two missing standards families to the RAG corpus and site: IEC 60079 (hazardous area electrical equipment, 6 parts) and SEMI S2/S8/S14 (semiconductor equipment safety, 3 standards). All content synthesized from engineering knowledge — no verbatim standard text. Follows the same pattern as all prior phases.

## Goals

- Close the IEC 60079 gap referenced by existing NEC Art. 504/505 RAG files
- Add SEMI S2/S8/S14 to support the existing Semiconductor Equipment scenario page
- Add corresponding site pages for both families
- Update `docs/standards/index.md` with both new families

## IEC 60079 — Hazardous Area Electrical Equipment

### RAG Corpus

**Directory:** `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/`

| File | Content |
|------|---------|
| `_index.yaml` | Corpus index for all 6 parts |
| `IEC60079_0__general_requirements.md` | Equipment marking system (Ex, protection method, gas group, T-code, EPL), certification bodies (ATEX, IECEx, UL), inspection requirements overview |
| `IEC60079_1__flameproof_Ex_d.md` | Ex d enclosure design principles, joint gaps, cable entry methods (glands, conduit seals), surface temperature limits, installation rules |
| `IEC60079_10_1__area_classification_gas.md` | Zone 0/1/2 determination methodology, release source grades (continuous/primary/secondary), ventilation effectiveness, documentation requirements, relationship to NEC Art. 505 |
| `IEC60079_11__intrinsically_safe_Ex_i.md` | IS protection levels (ia/ib/ic), energy limitation principles, associated apparatus (zener barriers, galvanic isolators), entity parameters (Ui/Ii/Pi/Ci/Li), FISCO model, relationship to NEC Art. 504 |
| `IEC60079_14__installation_design.md` | Cable selection for Ex areas, segregation from non-Ex wiring, equipotential bonding requirements, initial verification, inspection documentation |
| `IEC60079_17__inspection_maintenance.md` | Inspection types (initial/periodic/sample), inspection grades (close/detailed/visual), documentation requirements, competency requirements, defect classification |

### Site Pages

**Directory:** `docs/standards/hazardous-area/`

| File | Content |
|------|---------|
| `index.md` | Hazardous area family landing: scope, Zone vs. Division comparison table, links to IEC 60079 page, link to NEC Art. 500/504/505 |
| `iec-60079/index.md` | Full standard page: marking system, Zone overview, protection methods table (Ex d/e/i/m/n/p), area classification process, installation checklist, relationship to ATEX/IECEx/NEC |

**Update:** `docs/standards/index.md` — add Hazardous Area Standards section.

## SEMI S2/S8/S14 — Semiconductor Equipment Safety

### RAG Corpus

**Directory:** `control-standards/rag/standards_intelligence/international/semiconductor/semi/`

| File | Content |
|------|---------|
| `_index.yaml` | Corpus index for S2, S8, S14 |
| `SEMI_S2__equipment_safety.md` | Electrical safety requirements (isolation, grounding, interlocks), chemical handling guidelines, gas system safety, emissions limits, labeling and documentation requirements, relationship to IEC 60204-1 and NFPA 79 |
| `SEMI_S8__ergonomics.md` | Human factors principles for equipment design, maintenance access requirements, force/torque limits, reach envelopes, control placement, visual display requirements |
| `SEMI_S14__fire_risk_assessment.md` | Fire risk assessment process, material flammability classification, ignition source identification, fire detection and suppression in fab environments, cleanroom-specific considerations |

### Site Pages

**Directory:** `docs/standards/semiconductor/`

| File | Content |
|------|---------|
| `index.md` | Semiconductor family landing: scope, SEMI standards overview table, fab environment context |
| `semi/index.md` | SEMI S2/S8/S14 combined page: equipment safety overview, S2 electrical safety highlights, S8 ergonomics summary, S14 fire risk process, relationship to IEC 60204-1 and ISO 12100 |

**Update:** `docs/standards/index.md` — add Semiconductor Standards section.
**Update:** `docs/scenarios/semiconductor-equipment/index.md` — add SEMI standard links.

## Corpus File Template

Each RAG file follows the established pattern:

```
<!-- metadata header: CONTENT_CLASS, AI_READ_ACCESS, STATUS, STANDARD_FAMILY, etc. -->

# [Standard] — [Part/Section Title]

## 0. Why this matters for control engineers
## 1. [Core concept]
## 2. [Core concept]
...
## N. Change log
```

All content paraphrased — zero verbatim standard text. No copyrighted material.

## Out of Scope

- IEC 60079 parts beyond the 6 selected (dust: 60079-10-2, 31; encapsulation: 60079-18)
- SEMI S6, S22, or other SEMI standards
- Detailed FAB process equipment coverage
