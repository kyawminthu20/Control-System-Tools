# Lifecycle Page Expansion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand all 11 thin lifecycle stage pages (40–74 lines each) into comprehensive, standards-accurate engineering references using the detailed content in `planning/things_to_fix.md` in the kyawminthu20.github.io repo, and add 2 new stage pages (SRS and MOC) plus update the lifecycle index.

**Architecture:** Each lifecycle stage gets a single `index.md` rewrite — same Jekyll frontmatter pattern as existing pages, content expanded from the planning document. The lifecycle index (`/verification/lifecycle/index.md`) gets new stages added to the table, new mermaid diagram, and an introduction section. Two new stage directories are created for the SRS and MOC stages.

**Tech Stack:** Jekyll 4 static site, kramdown markdown, Mermaid.js diagrams, `default` layout. All pages live in `docs/lifecycle/`.

**Source of truth for content:** `~/Dev/kyawminthu20.github.io/planning/things_to_fix.md` (8635 lines, organized by page URL — each section after a `https://...` URL is the content for that page).

**Content extraction guide:**
- Lines 1–411: `/verification/lifecycle/` index page improvements (new stages, columns, introduction text)
- Lines 412–699: `/verification/lifecycle/concept/` — Stage 01
- Lines 700–1158: `/verification/lifecycle/standards-selection/` — Stage 02
- Lines 1159–1750: `/verification/risk-assessment/` — Stage 03
- Lines 1751–2501: `/verification/safety-architecture/` — Stage 04
- Lines 2502–3196: `/verification/lifecycle/detailed-design/` — Stage 05
- Lines 3197–3779: `/verification/lifecycle/draft-documentation/` — Stage 06
- Lines 3780–4540: `/implementation/lifecycle-build/` — Stage 07
- Lines 4541–5128: `/implementation/lifecycle-installation/` — Stage 08
- Lines 5129–5926: `/implementation/lifecycle-pre-commissioning/` — Stage 09
- Lines 5927–6992: `/implementation/lifecycle-commissioning/` — Stage 10
- Lines 6993–8635: `/verification/maintenance/` — Stage 11

**New pages to create:**
- `/verification/safety-requirements-spec/index.md` — Stage 3.5 (SRS), content from lines 11–19 of planning file plus general SRS knowledge
- `/verification/management-of-change/index.md` — Stage 12 (MOC), content from lines 31–38 of planning file

---

## File Map

| Action | File | Purpose |
|--------|------|---------|
| Modify | `docs/lifecycle/index.md` | Add new stages to table, expand mermaid, add introduction section |
| Rewrite | `docs/lifecycle/concept/index.md` | Full expansion from planning lines 414–699 |
| Rewrite | `docs/lifecycle/standards-selection/index.md` | Full expansion from planning lines 702–1158 |
| Rewrite | `docs/lifecycle/risk-assessment/index.md` | Full expansion from planning lines 1161–1750 |
| Rewrite | `docs/lifecycle/safety-architecture/index.md` | Full expansion from planning lines 1753–2501 |
| Rewrite | `docs/lifecycle/detailed-design/index.md` | Full expansion from planning lines 2504–3196 |
| Rewrite | `docs/lifecycle/draft-documentation/index.md` | Full expansion from planning lines 3199–3779 |
| Rewrite | `docs/lifecycle/build/index.md` | Full expansion from planning lines 3782–4540 |
| Rewrite | `docs/lifecycle/installation/index.md` | Full expansion from planning lines 4543–5128 |
| Rewrite | `docs/lifecycle/pre-commissioning/index.md` | Full expansion from planning lines 5131–5926 |
| Rewrite | `docs/lifecycle/commissioning/index.md` | Full expansion from planning lines 5930–6992 |
| Rewrite | `docs/lifecycle/maintenance/index.md` | Full expansion from planning lines 6995–8635 |
| Create | `docs/lifecycle/safety-requirements-spec/index.md` | New Stage 3.5 — Safety Requirements Specification |
| Create | `docs/lifecycle/management-of-change/index.md` | New Stage 12 — Management of Change |

---

## Approach Notes

- **Do not deviate from the planning file content.** The content in `things_to_fix.md` is authoritative. Transcribe it faithfully into markdown with the Jekyll frontmatter pattern.
- **Preserve Jekyll frontmatter pattern** from existing pages: `layout`, `title`, `description`, `breadcrumb`, `related_standards` fields.
- **Keep Mermaid diagrams** where the planning file includes ASCII art diagrams — convert them to Mermaid flowchart syntax wrapped in `<div class="mermaid-wrap"><pre class="mermaid">...</pre></div>`.
- **ASCII art hierarchy diagrams** (like the standards hierarchy) can be kept as fenced code blocks.
- **Tables** transcribe directly — kramdown GFM handles them.
- **No tests needed** — these are documentation-only markdown files with no executable code.
- **Commit after each page rewrite** — 14 commits total.

---

## Task 1: Update the lifecycle index page

**Files:**
- Modify: `docs/lifecycle/index.md`

Read planning lines 1–411 for the index page content. The key changes:
1. Update the stage table to include Stage 3.5 (SRS) and Stage 12 (MOC) rows
2. Add an introduction section (Purpose, Scope, Integration map, When to enter, Roles, Principles)
3. Update the mermaid flowchart to include the new stages
4. Add the V-model integration diagram as an ASCII/code block

- [ ] **Step 1: Read current index file**

Read: `docs/lifecycle/index.md`

- [ ] **Step 2: Read planning content for the index**

Read planning file lines 1–411 (from kyawminthu20.github.io repo):
```
~/Dev/kyawminthu20.github.io/planning/things_to_fix.md
offset=0, limit=411
```

- [ ] **Step 3: Rewrite the lifecycle index**

New frontmatter:
```yaml
---
layout: default
title: "Engineering Lifecycle"
description: "Safety engineering lifecycle — 13 stages from concept through decommissioning, with standards overlay, roles, and entry/exit criteria at each stage."
breadcrumb:
  - name: "Lifecycle"
repo_path: "control-standards/rag/standards_intelligence/reference_models/"
related_standards:
  - name: "ISO 12100 (Risk Assessment)"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

The page body should include:
- The "Introduction Section" content from the planning file (Purpose, Scope, Integration map, When to enter, Roles, Standards framework, Key principles, How to use) — this is lines 176–409 of the planning file
- Updated stage table with 13 rows (including Stage 3.5 SRS and Stage 12 MOC)
- Updated mermaid flowchart showing all stages

- [ ] **Step 4: Commit**

```bash
cd "."
git add docs/lifecycle/index.md
git commit -m "docs: expand lifecycle index with introduction, roles, and stages 3.5/12"
```

---

## Task 2: Rewrite Stage 01 — Concept

**Files:**
- Rewrite: `docs/lifecycle/concept/index.md`

Read planning lines 414–699 for this page's content. This stage covers: purpose, entry criteria, required inputs, standards influence (ISO 12100 §5, type-C standards), engineering activities (machine limits, intended use, foreseeable misuse, markets, stakeholders, hazard scan), key deliverables table, exit criteria gate, roles, common mistakes, adjacent stage relationships, templates.

- [ ] **Step 1: Read planning content**

```
offset=413, limit=287
```

- [ ] **Step 2: Rewrite concept/index.md**

Frontmatter to preserve:
```yaml
---
layout: default
title: "Lifecycle Stage 1 — Concept"
description: "Define machine limits, intended use, foreseeable misuse, and applicable markets before risk assessment begins."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "1. Concept"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/concept/index.md
git commit -m "docs: expand lifecycle stage 01 concept page"
```

---

## Task 3: Rewrite Stage 02 — Standards Selection

**Files:**
- Rewrite: `docs/lifecycle/standards-selection/index.md`

Read planning lines 702–1158. Key content: purpose, entry criteria, standards hierarchy (type A/B/C), override rule, PL vs SIL routing logic table, key deliverables with expanded standards register template, exit criteria, common mistakes (16 listed), adjacent stage relationships, PL↔SIL equivalence table.

- [ ] **Step 1: Read planning content**

```
offset=701, limit=458
```

- [ ] **Step 2: Rewrite standards-selection/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 2 — Standards Selection"
description: "Identify all applicable standards, resolve type-A/B/C hierarchy, and determine the PL or SIL pathway before detailed design begins."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "2. Standards Selection"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/standards-selection/index.md
git commit -m "docs: expand lifecycle stage 02 standards selection page"
```

---

## Task 4: Rewrite Stage 03 — Risk Assessment

**Files:**
- Rewrite: `docs/lifecycle/risk-assessment/index.md`

Read planning lines 1161–1750. Key content: purpose (critical gate), 3-step risk reduction strategy (ISO 12100 §6), hazard identification methodology, risk estimation matrices (S×F×P), PL/SIL decision detailed with routing logic, safety function register template, risk assessment report structure, exit criteria (9 criteria), common mistakes, iterative nature of risk assessment.

- [ ] **Step 1: Read planning content**

```
offset=1160, limit=591
```

- [ ] **Step 2: Rewrite risk-assessment/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 3 — Risk Assessment"
description: "Systematic hazard identification and risk estimation — the critical gate where PLr or SIL targets are assigned to each safety function."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "3. Risk Assessment"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/risk-assessment/index.md
git commit -m "docs: expand lifecycle stage 03 risk assessment page"
```

---

## Task 5: Create Stage 3.5 — Safety Requirements Specification

**Files:**
- Create: `docs/lifecycle/safety-requirements-spec/index.md`

This is a new page. The planning file (lines 11–18) defines what SRS is. Expand it with the standard content: purpose (contract between risk assessment and design), required content per IEC 62061 §5.3, IEC 61511-1 §10, ISO 13849-1 §5 — safety function definitions, required PL/SIL, inputs/outputs, response times, demand mode, process parameters. Include entry/exit criteria, deliverables table, and relationship to Stages 3 and 4.

- [ ] **Step 1: Read planning lines for SRS context**

```
offset=10, limit=20
```

- [ ] **Step 2: Create safety-requirements-spec/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 3.5 — Safety Requirements Specification"
description: "The SRS is the contract between risk assessment and architecture — every safety function defined with required PL/SIL, inputs, outputs, and response time."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "3.5. Safety Requirements Spec"
related_standards:
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
---
```

Page sections: Purpose, Why the SRS Matters, Standards Requirements (IEC 62061 §5.3, IEC 61511-1 §10, ISO 13849-1 §5), Entry Criteria, Engineering Activities (writing SRS line items per safety function), SRS Template Table (SF ID | Safety Function | Required PL/SIL | Inputs | Outputs | Demand Mode | Response Time | Process Parameters), Exit Criteria, Common Mistakes, Relationships to Stages 3 and 4.

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/safety-requirements-spec/index.md
git commit -m "docs: add lifecycle stage 3.5 safety requirements specification page"
```

---

## Task 6: Rewrite Stage 04 — Safety Architecture

**Files:**
- Rewrite: `docs/lifecycle/safety-architecture/index.md`

Read planning lines 1753–2501. Key content: safety chain subsystem decomposition, ISO 13849-1 categories (B, 1, 2, 3, 4) with architecture tables, IEC 62061 subsystem architectures (1oo1, 1oo2, 2oo2), MTTFd calculation from B10d, diagnostic coverage estimation table, CCF scoring (ISO 13849-1 Annex F), PL calculation procedure (SISTEMA pathway), SIL verification (PFHD methodology), response time budget, fault exclusion rules, architecture decision documentation template, exit criteria (12 criteria), common mistakes.

- [ ] **Step 1: Read planning content**

```
offset=1752, limit=750
```

- [ ] **Step 2: Rewrite safety-architecture/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 4 — Safety Architecture Definition"
description: "Decompose safety functions into subsystems, select category/architecture, calculate PL or SIL, and verify response time budgets."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "4. Safety Architecture"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/safety-architecture/index.md
git commit -m "docs: expand lifecycle stage 04 safety architecture page"
```

---

## Task 7: Rewrite Stage 05 — Detailed Design

**Files:**
- Rewrite: `docs/lifecycle/detailed-design/index.md`

Read planning lines 2504–3196. Key content: circuit design (power distribution, overcurrent, control transformers, SCCR), wire sizing (NEC 310 / UL 508A Section 28), grounding (safety ground vs equipment ground), protective bonding, conduit fill, device spacing, label requirements, BOM structure, verification plan template, exit criteria, common mistakes. Long section covering all of NEC / NFPA 79 / UL 508A design requirements.

- [ ] **Step 1: Read planning content in two passes (long section)**

```
offset=2503, limit=350   # first half
offset=2853, limit=344   # second half
```

- [ ] **Step 2: Rewrite detailed-design/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 5 — Detailed Design and Part Sizing"
description: "Circuit design, wire sizing, SCCR, grounding, label requirements, BOM, and verification plan — governed by NFPA 79, UL 508A, and NEC."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "5. Detailed Design"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/detailed-design/index.md
git commit -m "docs: expand lifecycle stage 05 detailed design page"
```

---

## Task 8: Rewrite Stage 06 — Draft Documentation

**Files:**
- Rewrite: `docs/lifecycle/draft-documentation/index.md`

Read planning lines 3199–3779. Key content: three audiences (build team, commissioning team, regulatory/customer), documentation package structure (schematics, BOM, panel layout, wire schedule, shop traveler, safety manual, verification plan, safety function register), document control requirements, traceability matrix, safety manual required content per IEC 62061/61511, exit criteria, common mistakes.

- [ ] **Step 1: Read planning content**

```
offset=3198, limit=582
```

- [ ] **Step 2: Rewrite draft-documentation/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 6 — Draft Design Documentation"
description: "Compile engineering outputs into formal document packages for the build team, commissioning team, and regulatory record."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "6. Draft Documentation"
related_standards:
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/draft-documentation/index.md
git commit -m "docs: expand lifecycle stage 06 draft documentation page"
```

---

## Task 9: Rewrite Stage 07 — Build

**Files:**
- Rewrite: `docs/lifecycle/build/index.md`

Read planning lines 3782–4540. Key content: shop traveler system, panel fabrication sequence, safety PLC application programming (IVL/LVL per IEC 62061 §6.7, ISO 13849-1 Annex J), functional test at panel level (pre-shipment test), CRC/signature backup of safety program, build record requirements, acceptance inspection, common mistakes.

- [ ] **Step 1: Read planning content**

```
offset=3781, limit=760
```

- [ ] **Step 2: Rewrite build/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 7 — Control System Build and Software Implementation"
description: "Panel fabrication, safety PLC programming, pre-shipment functional test, and program backup — with build records for every safety-rated component."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "7. Build"
related_standards:
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61131-3"
    url: "/standards/plc-programming/iec-61131-3/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/build/index.md
git commit -m "docs: expand lifecycle stage 07 build page"
```

---

## Task 10: Rewrite Stage 08 — Installation

**Files:**
- Rewrite: `docs/lifecycle/installation/index.md`

Read planning lines 4543–5128. Key content: field installation requirements per NEC/NFPA 79, conduit and cable routing separation (safety vs non-safety), field wiring verification, grounding continuity, installation record requirements, EMC considerations, commissioning handoff package, exit criteria, common mistakes.

- [ ] **Step 1: Read planning content**

```
offset=4542, limit=587
```

- [ ] **Step 2: Rewrite installation/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 8 — Installation"
description: "Field installation of control panels and safety devices — NEC/NFPA 79 wiring, cable segregation, grounding continuity, and installation record."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "8. Installation"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/installation/index.md
git commit -m "docs: expand lifecycle stage 08 installation page"
```

---

## Task 11: Rewrite Stage 09 — Pre-Commissioning

**Files:**
- Rewrite: `docs/lifecycle/pre-commissioning/index.md`

Read planning lines 5131–5926. Key content: pre-commissioning checklist structure (power-off checks, power-on checks, functional checks, safety function checks), proof test baseline values (initial trip calibrations, valve stroke times), independence of verification requirement, pre-commissioning vs commissioning distinction, exit criteria, common mistakes.

- [ ] **Step 1: Read planning content**

```
offset=5130, limit=797
```

- [ ] **Step 2: Rewrite pre-commissioning/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 9 — Pre-Commissioning and Calibration"
description: "Systematic verification of wiring, I/O, calibration, and safety function response before process startup — establishes proof test baselines."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "9. Pre-Commissioning"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/pre-commissioning/index.md
git commit -m "docs: expand lifecycle stage 09 pre-commissioning page"
```

---

## Task 12: Rewrite Stage 10 — Commissioning

**Files:**
- Rewrite: `docs/lifecycle/commissioning/index.md`

Read planning lines 5930–6992. Key content: FAT vs SAT distinction (location, responsibilities, scope), independence of verification requirement, V&V report structure, safety function validation procedure per safety function, SIL/PL final verification record, commissioning report, handover package to operations, exit criteria (9 criteria), common mistakes.

- [ ] **Step 1: Read planning content in two passes**

```
offset=5929, limit=530   # first half
offset=6459, limit=534   # second half
```

- [ ] **Step 2: Rewrite commissioning/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 10 — Commissioning and Validation"
description: "FAT, SAT, safety function validation, and final PL/SIL verification — the stage where design intent is formally demonstrated on the physical system."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "10. Commissioning"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/commissioning/index.md
git commit -m "docs: expand lifecycle stage 10 commissioning page"
```

---

## Task 13: Rewrite Stage 11 — Maintenance

**Files:**
- Rewrite: `docs/lifecycle/maintenance/index.md`

Read planning lines 6995–8635. Key content: three parallel tracks (proof testing, preventive maintenance, MOC), proof test interval justification linked to SIL/PL calculations (T_proof), proof test procedures per safety function, bypass/override management, safety-related maintenance procedures, competency requirements for maintenance personnel, functional safety assessment (FSA) for ongoing operations, exit criteria (ongoing), common mistakes.

- [ ] **Step 1: Read planning content in three passes (very long)**

```
offset=6994, limit=550   # sections 1-4
offset=7544, limit=550   # sections 5-8
offset=8094, limit=541   # sections 9-end
```

- [ ] **Step 2: Rewrite maintenance/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 11 — Maintenance and Lifecycle Support"
description: "Proof testing at defined intervals, preventive maintenance, bypass management, and MOC — sustaining safety integrity across the full operational life."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "11. Maintenance"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/maintenance/index.md
git commit -m "docs: expand lifecycle stage 11 maintenance page"
```

---

## Task 14: Create Stage 12 — Management of Change

**Files:**
- Create: `docs/lifecycle/management-of-change/index.md`

Content from planning file lines 31–38 plus MOC references from the introduction section (lines 275–295). Expand with full page structure: purpose (most commonly failed audit point), MOC procedure structure, change impact assessment, which stages to re-enter depending on change type (table), re-verification requirements, documentation requirements, relationship to all other stages.

- [ ] **Step 1: Read planning content for MOC**

```
offset=30, limit=12    # core definition
offset=270, limit=30   # integration map references
```

- [ ] **Step 2: Create management-of-change/index.md**

```yaml
---
layout: default
title: "Lifecycle Stage 12 — Management of Change"
description: "Structured re-entry into the safety lifecycle for any modification to a safety function, component, or program — the most commonly failed audit point."
breadcrumb:
  - name: "Lifecycle"
    url: "/verification/lifecycle/"
  - name: "12. Management of Change"
related_standards:
  - name: "IEC 61511-1"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
---
```

- [ ] **Step 3: Commit**

```bash
git add docs/lifecycle/management-of-change/index.md
git commit -m "docs: add lifecycle stage 12 management of change page"
```

---

## Task 15: Update project state files

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

- [ ] **Step 1: Update project_state.md**

Reflect that all 11 lifecycle stage pages have been expanded, 2 new pages created (SRS, MOC), and lifecycle index updated.

- [ ] **Step 2: Update change_log.md**

Add dated entry for this expansion work.

- [ ] **Step 3: Commit**

```bash
git add project_state/
git commit -m "chore: update project state after lifecycle page expansion"
```

---

## Summary

15 tasks, 14 file rewrites/creates, ~14 commits. No tests needed (documentation only). Estimated total content: 12 pages going from ~40–74 lines to ~200–500+ lines each based on the planning file depth.

**Priority order if doing partial execution:**
1. Tasks 4 (risk assessment) and 6 (safety architecture) — these are the most technically deep and most visited
2. Tasks 2 (concept) and 3 (standards selection) — foundation stages
3. Tasks 5 (SRS) and 14 (MOC) — new pages, closes the lifecycle loop
4. Remaining stages in order (5→6→7→8→9→10→11)
5. Task 1 (index) last — update after all stage pages are done so table is accurate
