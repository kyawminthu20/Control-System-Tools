# Phase 11: Industry Overlay Depth — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Phase:** Phase 11

## Overview

Deepen two industry overlay pages (Petroleum/O&G and Semiconductor) from thin stubs into full reference pages, and add two new scenario pages (onshore process skid and etch/CVD fab tool). No new RAG corpus files required — all backing content already exists.

## Workstream 1: Petroleum / Oil & Gas (Onshore)

### Industry page update — `docs/industries/petroleum/index.md`

- Remove stale `badge--gap` and `badge--verify` for IEC 60079, IEC 61511, IEC 61508 (all now complete)
- Add `related_standards` front matter: IEC 61511, IEC 61508, IEC 60079, NEC
- Standards applicability matrix by project phase: Concept → SIS Design → Detailed Design → Installation → Commissioning → Maintenance
- Standards selection flow: hazardous area? → Zone or Division? → SIS required? → SIL target?
- O&G-specific compliance checklist (pre-commissioning gate items)
- Link to new scenario page

### New scenario page — `docs/scenarios/oil-gas-process-skid/index.md`

**Profile:** Onshore process skid with ESD, F&G, and HIPPS

**Content:**
- Step-by-step design workflow: HAZOP → LOPA → SIL determination → SIF design → Ex equipment selection → installation per IEC 60079-14 → proof test
- Mermaid diagram: SIS architecture (logic solver + final elements) + hazardous zone layout
- Example standard stack table: IEC 61511 + IEC 61508 + IEC 60079 + NEC 500/504/505 + IEC 60204-1
- Common engineering decisions: zener barrier vs. galvanic isolator, Zone 1 vs. Division 1 equipment, SIL 2 vs. SIL 3 architecture

## Workstream 2: Semiconductor (Etch/CVD Tool)

### Industry page update — `docs/industries/semiconductor/index.md`

- Update all SEMI badges from `badge--gap` / `badge--verify` to `badge--complete`
- Add `related_standards` front matter: SEMI S2/S8/S14, IEC 60204-1, ISO 12100
- Standards applicability matrix: tool design → electrical build → tool qualification → fab installation → periodic inspection
- SEMI S2 compliance flow: risk assessment → interlock design → LOTO provisions → documentation package
- Link to new scenario page

### New scenario page — `docs/scenarios/semiconductor-fab-tool/index.md`

**Profile:** Etch/CVD process tool with flammable/toxic process gases, gas cabinet, RF power supply

**Content:**
- Step-by-step: ISO 12100 risk assessment → SEMI S2 electrical safety → S14 fire risk → S8 ergonomics → IEC 60204-1 electrical build → fab qualification
- Mermaid diagram: gas delivery control system (NC shutoff valves, flow/pressure interlocks, exhaust monitoring) + interlock hierarchy
- Example standard stack: SEMI S2 + S8 + S14 + IEC 60204-1 + NFPA 79 + ISO 12100 + IEC 62443
- Common engineering decisions: capacitor discharge interlock design, gas detector integration with ESD, single-point ground vs. equipotential bonding

## Site Nav Updates

- `docs/_includes/sidebar.html`: add both new scenario links under Scenarios section
- `docs/scenarios/index.md`: add cards for both new scenarios

## Out of Scope

- No new RAG corpus files
- No offshore, marine, or midstream coverage
- No API standards (API 14C, API 670)
