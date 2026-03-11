# Phase 16: NEC Training Expansion Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the NEC training track from 3 modules to 11 modules covering branch circuits, disconnects, grounding/bonding, SCCR, Article 430, Article 409, Class 1/2/3 circuits, and conductor/OCPD sizing.

**Architecture:** For each module: write a RAG source file in `control-standards/rag/training_modules/nec_application/`, copy it to `docs/assets/rag-files/training_modules/nec_application/`, create a site page under `docs/training/nec-application/`, add the module to `docs/_data/training_catalog.yml`, then update the index files and group page. All 8 new modules follow the exact same pattern as the 3 existing NEC modules.

**Tech Stack:** Jekyll 4.x, Markdown, Liquid, existing `training-module` layout from Phase 15.

---

## Before You Start

Read these files for patterns:

- `control-standards/rag/training_modules/nec_application/motor_and_panel_code_application.md` — RAG file header and section structure
- `docs/training/nec-application/motor-panel-code-application/index.md` — site page pattern
- `docs/_data/training_catalog.yml` — catalog entry structure (add new modules under `# ── NEC Application` section)
- `control-standards/rag/training_modules/nec_application/_index.yaml` — RAG index to update
- `docs/training/nec-application/index.md` — group page to update (module count + table)

Build command:
```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: clean build, no Liquid errors.

---

## File Map

### New RAG source files (8)
| File | Module |
|------|--------|
| `control-standards/rag/training_modules/nec_application/branch_circuits_vs_feeders_motor_loads.md` | Branch Circuits vs. Feeders for Motor Loads |
| `control-standards/rag/training_modules/nec_application/disconnecting_means_for_machinery.md` | Disconnecting Means for Machinery |
| `control-standards/rag/training_modules/nec_application/grounding_bonding_control_panels.md` | Grounding and Bonding for Control Panels |
| `control-standards/rag/training_modules/nec_application/sccr_workflow.md` | SCCR Workflow for Industrial Control Panels |
| `control-standards/rag/training_modules/nec_application/conductor_ocpd_sizing_examples.md` | Conductor and OCPD Sizing Worked Examples |
| `control-standards/rag/training_modules/nec_application/class1_class2_remote_control_circuits.md` | Class 1, Class 2, and Remote-Control Circuits |
| `control-standards/rag/training_modules/nec_application/article_430_practical_workflow.md` | Practical Article 430 Workflow |
| `control-standards/rag/training_modules/nec_application/article_409_practical_workflow.md` | Practical Article 409 Workflow |

### New published RAG copies (8)
Same filenames under `docs/assets/rag-files/training_modules/nec_application/`.

### New site pages (8)
| Directory | Module |
|-----------|--------|
| `docs/training/nec-application/branch-circuits-vs-feeders/` | Branch Circuits vs. Feeders |
| `docs/training/nec-application/disconnecting-means/` | Disconnecting Means |
| `docs/training/nec-application/grounding-bonding-panels/` | Grounding and Bonding |
| `docs/training/nec-application/sccr-workflow/` | SCCR Workflow |
| `docs/training/nec-application/conductor-ocpd-sizing/` | Conductor and OCPD Sizing |
| `docs/training/nec-application/class1-class2-circuits/` | Class 1, Class 2, and Remote-Control Circuits |
| `docs/training/nec-application/article-430-workflow/` | Practical Article 430 Workflow |
| `docs/training/nec-application/article-409-workflow/` | Practical Article 409 Workflow |

### Modified files
| File | Change |
|------|--------|
| `control-standards/rag/training_modules/nec_application/_index.yaml` | Add 8 new filenames |
| `docs/assets/rag-files/training_modules/nec_application/` | Same (mirrored) |
| `docs/_data/training_catalog.yml` | Add 8 new module entries + update topic_groups count |
| `docs/training/nec-application/index.md` | Update module count, add 8 rows to table |
| `docs/_data/rag_tree.json` | Regenerate via `python3 tools/generate_rag_tree.py` |
| `project_state/project_state.md` | Mark Phase 16 complete |
| `project_state/change_log.md` | Add Phase 16 entry |

---

## RAG File Content Guide

Each RAG file must follow this header pattern exactly:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: NEC_APPLICATION
MODULE_ID: <snake_case_id>
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["<tag1>", "<tag2>"]
  systems: ["industrial_control_panel", "machine"]
-->

# <Title>

## 0. Purpose
...

## 1. <First concept>
...

## Related files
- [NEC Code Reading Fundamentals](./nec_code_reading_fundamentals.md)
- [Motor and Panel Code Application](./motor_and_panel_code_application.md)
```

Each site page must use `layout: training-module` and follow the pattern in `motor-panel-code-application/index.md`.

---

## Module Content Specifications

### Module 1: Branch Circuits vs. Feeders for Motor Loads
**RAG file:** `branch_circuits_vs_feeders_motor_loads.md`
**Site slug:** `branch-circuits-vs-feeders`
**Level:** Beginner | **Time:** 20 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Definition: branch circuit ends at the last OCPD before the load; feeder runs between OCPDs
- Why motor loads create special branch-circuit sizing rules (FLA × 125% for conductors, Art 430.22)
- When multiple motors share a feeder (Art 430.24 — sum of FLA × 125% for largest + 100% of rest)
- Typical single-motor branch circuit layout: feeder tap → OCPD → disconnect → overload → motor
- Common mistake: using motor nameplate FLA directly without the 125% multiplier
- Mermaid diagram: feeder → branch circuit → disconnect → overload → motor

Related standards: NEC Art 430 Part II, Art 240, NFPA 79 Ch 7

---

### Module 2: Disconnecting Means for Machinery
**RAG file:** `disconnecting_means_for_machinery.md`
**Site slug:** `disconnecting-means`
**Level:** Beginner | **Time:** 20 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- NEC 430.102: each motor must have a disconnecting means in sight from the motor
- "In sight" definition: visible and not more than 50 ft away (Art 430.102(A))
- When a single disconnect can serve a group of motors (Art 430.112 exceptions)
- NFPA 79 6.2: main disconnect at the panel must be lockable in the off position
- Acceptable disconnect types: motor-circuit switch rated in HP, inverse-time CB, molded-case switch
- VFD installations: disconnect must be upstream of the drive, not between drive and motor
- Mermaid diagram: service → main disconnect → individual motor disconnects

Related standards: NEC Art 430 Part IX, NFPA 79 Ch 6, IEC 60204-1 Clause 5

---

### Module 3: Grounding and Bonding for Control Panels
**RAG file:** `grounding_bonding_control_panels.md`
**Site slug:** `grounding-bonding-panels`
**Level:** Beginner | **Time:** 25 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Difference between grounding (connecting to earth) and bonding (connecting metal parts together)
- Equipment grounding conductor (EGC): sized from Table 250.122 based on upstream OCPD rating
- Main bonding jumper vs. system bonding jumper
- Panel enclosure bonding: all metal parts must be bonded to the EGC bus
- Ground bus vs. neutral bus: why they must be separated in downstream panels
- Grounding electrode system: not the same as the EGC fault path
- Common mistake: undersizing the EGC or relying on conduit as the only bonding path
- VFD grounding: drive chassis must be bonded; long cable runs and dedicated EGC recommendations

Related standards: NEC Art 250, UL 508A, NFPA 79 Ch 8, IEC 60204-1 Clause 8

---

### Module 4: SCCR Workflow for Industrial Control Panels
**RAG file:** `sccr_workflow.md`
**Site slug:** `sccr-workflow`
**Level:** Intermediate | **Time:** 30 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- What SCCR means: the maximum fault current the panel can safely interrupt
- Why it matters: NEC 409.110 requires SCCR marking; AHJ uses it to confirm safe installation
- Two methods to establish SCCR: component method (UL 508A Supplement SB) and series-rating method
- Component method workflow: identify the lowest-rated component in the fault-current path; that rating is the panel SCCR unless a higher-rated protective device shields it
- Common components that limit SCCR: contactors, overload relays, terminal blocks rated below the upstream fault current
- How a current-limiting fuse upstream can raise the effective SCCR of downstream components
- Practical step-by-step: get AIC at the installation point → compare to each component's listed fault rating → identify the weak link → add current-limiting protection if needed
- Mermaid diagram: fault-current path from utility → main OCPD → components → SCCR marking

Related standards: NEC Art 409, UL 508A Supplement SB, NFPA 79 Ch 7

---

### Module 5: Conductor and OCPD Sizing Worked Examples
**RAG file:** `conductor_ocpd_sizing_examples.md`
**Site slug:** `conductor-ocpd-sizing`
**Level:** Intermediate | **Time:** 30 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Step-by-step sizing for a single-motor branch circuit (worked example: 10 HP, 480V, 3-phase, Design B)
  1. Find FLA from Table 430.250
  2. Branch conductor: FLA × 125% → select from Table 310.15(B)(16) at 75°C
  3. Overload protection: FLA × 115% (SF ≥ 1.15) or × 125%
  4. Branch-circuit OCPD: FLA × 250% (inverse-time CB) or 175% (dual-element fuse) per Table 430.52
  5. Disconnect rating: must be ≥ 115% of FLA and ≥ HP rating
- Second worked example: feeder serving three motors (Art 430.24)
- Common mistake table: what happens when you size by nameplate amps instead of Table 430.250
- Quick-reference sizing table for common 480V motor sizes

Related standards: NEC Art 430, Art 240, Art 310, Table 430.250

---

### Module 6: Class 1, Class 2, and Remote-Control Circuits
**RAG file:** `class1_class2_remote_control_circuits.md`
**Site slug:** `class1-class2-circuits`
**Level:** Intermediate | **Time:** 25 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Art 725 defines three classes of remote-control, signaling, and power-limited circuits
- Class 1: follows power wiring rules (Art 300); conductors can be 14 AWG minimum
- Class 2: power-limited (≤ 100 VA); relaxed wiring methods; 24 VDC PLC I/O wiring typically falls here
- Class 3: power-limited at higher voltage (≤ 100 VA, ≤ 150V); fire-alarm and intercom typical
- How to classify a circuit: check the power source output — listed Class 2 power supply determines Class 2 status
- Separation rules: Class 2 cables must be separated from Class 1 or power conductors (unless cable is listed for the combination or a barrier is used)
- Common mistake: routing 24 VDC control wiring in the same conduit as 480 VAC without checking Art 725.136
- Why this matters at panel build: separate wireway, different connector colors, different cable labeling

Related standards: NEC Art 725, NFPA 79 Ch 13, IEC 60204-1 Clause 14

---

### Module 7: Practical Article 430 Workflow
**RAG file:** `article_430_practical_workflow.md`
**Site slug:** `article-430-workflow`
**Level:** Intermediate | **Time:** 30 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Art 430 internal structure: Parts I–XIV — know which Part answers which question
  - Part I: general
  - Part II: conductors
  - Part III: overload protection
  - Part IV: branch-circuit SCPD
  - Part IX: disconnecting means
  - Part X: controllers
- Decision flowchart for a motor installation question: what are you sizing? → route to the Part
- How Art 430.6 tells you to use Table values, not nameplate FLA, for conductor and OCPD sizing
- The 430.52 exception chain: starting with 250% CB → when you can go higher (up to 400%) if the motor won't start
- Overload relay sizing: Art 430.32 with the SF and temperature-rise test
- Worked routing example: "Size the branch-circuit CB for a 25 HP, 460V motor" — step by step through the Parts
- Mermaid flowchart: motor installation question → Part selection

Related standards: NEC 2023 Art 430, Table 430.250, Table 430.52

---

### Module 8: Practical Article 409 Workflow
**RAG file:** `article_409_practical_workflow.md`
**Site slug:** `article-409-workflow`
**Level:** Intermediate | **Time:** 25 min | **Type:** Code Application | **Focus:** Panel Design / NEC

Cover:
- Art 409 scope: industrial control panels (ICPs) — factory-built assemblies with control equipment
- 409.20: supply conductors sized at 125% of full-load current of all resistance heating loads + 125% of largest motor + 100% of remaining loads
- 409.110: required marking on every ICP enclosure: manufacturer, supply voltage/phase/frequency, full-load current, SCCR, and enclosure type
- 409.22: overcurrent protection — the panel's main OCPD must be sized for the calculated load
- How 409 and 508A relate: Art 409 is the NEC requirement; UL 508A is the construction standard that satisfies it
- Difference between an ICP (Art 409) and motor control center (Art 430 Part F)
- Common AHJ check: is the SCCR marking present and does it equal or exceed available fault current?
- Practical workflow: receive fault-current study → verify panel SCCR marking → confirm supply OCPD type → sign off

Related standards: NEC Art 409, UL 508A, NFPA 79 Ch 4

---

## Task 1: Write RAG files — Article 430 group (Modules 1, 2, 7)

**Files:**
- Create: `control-standards/rag/training_modules/nec_application/branch_circuits_vs_feeders_motor_loads.md`
- Create: `control-standards/rag/training_modules/nec_application/disconnecting_means_for_machinery.md`
- Create: `control-standards/rag/training_modules/nec_application/article_430_practical_workflow.md`

- [ ] Write `branch_circuits_vs_feeders_motor_loads.md` following the RAG header pattern and Module 1 spec above. Include a Mermaid diagram for the feeder → branch circuit layout.

- [ ] Write `disconnecting_means_for_machinery.md` following Module 2 spec. Include a Mermaid diagram showing disconnect placement.

- [ ] Write `article_430_practical_workflow.md` following Module 7 spec. Include an Art 430 Parts routing table and Mermaid decision flowchart.

- [ ] Copy all three files to `docs/assets/rag-files/training_modules/nec_application/`.

---

## Task 2: Write RAG files — Panel design group (Modules 3, 4, 8)

**Files:**
- Create: `control-standards/rag/training_modules/nec_application/grounding_bonding_control_panels.md`
- Create: `control-standards/rag/training_modules/nec_application/sccr_workflow.md`
- Create: `control-standards/rag/training_modules/nec_application/article_409_practical_workflow.md`

- [ ] Write `grounding_bonding_control_panels.md` following Module 3 spec. Include the EGC sizing rule (Table 250.122) and common mistakes.

- [ ] Write `sccr_workflow.md` following Module 4 spec. Include the component method step-by-step and a Mermaid fault-path diagram.

- [ ] Write `article_409_practical_workflow.md` following Module 8 spec. Include the 409.110 marking checklist.

- [ ] Copy all three files to `docs/assets/rag-files/training_modules/nec_application/`.

---

## Task 3: Write RAG files — Sizing and control circuits group (Modules 5, 6)

**Files:**
- Create: `control-standards/rag/training_modules/nec_application/conductor_ocpd_sizing_examples.md`
- Create: `control-standards/rag/training_modules/nec_application/class1_class2_remote_control_circuits.md`

- [ ] Write `conductor_ocpd_sizing_examples.md` following Module 5 spec. Include both worked examples and the quick-reference sizing table.

- [ ] Write `class1_class2_remote_control_circuits.md` following Module 6 spec. Include the classification decision logic and separation rules.

- [ ] Copy both files to `docs/assets/rag-files/training_modules/nec_application/`.

---

## Task 4: Create site pages for all 8 modules

**Files:** 8 × `docs/training/nec-application/<slug>/index.md`

For each module, follow this front matter pattern exactly:

```yaml
---
layout: training-module
title: "<Module Title>"
description: "<One-sentence description>"
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/<filename>.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
---
```

Page body: write concise, practical prose matching the RAG file content. Include Mermaid diagrams where the RAG file has them. End each page with the standard three-link footer nav (prev ← | ↑ group | → next).

Module sequence for nav links (full 11-module order):
1. NEC Code Reading Fundamentals
2. Working Space and Table Navigation
3. Motor and Panel Code Application
4. Branch Circuits vs. Feeders ← **new**
5. Disconnecting Means ← **new**
6. Grounding and Bonding for Control Panels ← **new**
7. SCCR Workflow ← **new**
8. Conductor and OCPD Sizing ← **new**
9. Class 1, Class 2, and Remote-Control Circuits ← **new**
10. Practical Article 430 Workflow ← **new**
11. Practical Article 409 Workflow ← **new**

- [ ] Create `docs/training/nec-application/branch-circuits-vs-feeders/index.md`
- [ ] Create `docs/training/nec-application/disconnecting-means/index.md`
- [ ] Create `docs/training/nec-application/grounding-bonding-panels/index.md`
- [ ] Create `docs/training/nec-application/sccr-workflow/index.md`
- [ ] Create `docs/training/nec-application/conductor-ocpd-sizing/index.md`
- [ ] Create `docs/training/nec-application/class1-class2-circuits/index.md`
- [ ] Create `docs/training/nec-application/article-430-workflow/index.md`
- [ ] Create `docs/training/nec-application/article-409-workflow/index.md`

**Also update the existing module 3 nav link** — `motor-panel-code-application/index.md` currently ends with `<span></span>` as the next link. Update it to point to `branch-circuits-vs-feeders`.

---

## Task 5: Update training_catalog.yml

**File:** `docs/_data/training_catalog.yml`

- [ ] Update `topic_groups` entry for `nec-application`: change `module_count: 3` to `module_count: 11`

- [ ] Add 8 new module entries under the `# ── NEC Application` section. Use this pattern for each:

```yaml
  - title: "Branch Circuits vs. Feeders for Motor Loads"
    url: "/training/nec-application/branch-circuits-vs-feeders/"
    group: "nec-application"
    group_label: "NEC for Machines and Panels"
    summary: "Understand where a branch circuit ends and a feeder begins, and why motor loads require the 125% conductor multiplier from Article 430."
    level: "Beginner"
    time: "20 min"
    focus: "Panel Design / NEC"
    type: "Code Application"
    prerequisites:
      - "NEC Code Reading Fundamentals"
    featured: true
```

Full entries for all 8 new modules (levels, times, and featured flags):

| Module | Level | Time | Featured |
|--------|-------|------|----------|
| Branch Circuits vs. Feeders | Beginner | 20 min | true |
| Disconnecting Means | Beginner | 20 min | false |
| Grounding and Bonding | Beginner | 25 min | true |
| SCCR Workflow | Intermediate | 30 min | true |
| Conductor and OCPD Sizing | Intermediate | 30 min | true |
| Class 1, Class 2, Circuits | Intermediate | 25 min | false |
| Practical Art 430 Workflow | Intermediate | 30 min | true |
| Practical Art 409 Workflow | Intermediate | 25 min | false |

- [ ] Update `learning_paths` entry for `panel-design-nec` to include the 4 most relevant new modules:
  - Add `url: "/training/nec-application/branch-circuits-vs-feeders/"`
  - Add `url: "/training/nec-application/grounding-bonding-panels/"`
  - Add `url: "/training/nec-application/sccr-workflow/"`
  - Add `url: "/training/nec-application/conductor-ocpd-sizing/"`

---

## Task 6: Update index files and group page

**Files:**
- `control-standards/rag/training_modules/nec_application/_index.yaml`
- `docs/training/nec-application/index.md`

- [ ] Add 8 new filenames to `_index.yaml` under `files:`:

```yaml
  - "branch_circuits_vs_feeders_motor_loads.md"
  - "disconnecting_means_for_machinery.md"
  - "grounding_bonding_control_panels.md"
  - "sccr_workflow.md"
  - "conductor_ocpd_sizing_examples.md"
  - "class1_class2_remote_control_circuits.md"
  - "article_430_practical_workflow.md"
  - "article_409_practical_workflow.md"
```

- [ ] Update `docs/training/nec-application/index.md`:
  - Change the page header count: "3 modules" → "11 modules"
  - The module table is data-driven from `training_catalog.yml` so no table edits needed — the new entries will appear automatically once the catalog is updated.
  - Update the page `description:` front matter to reflect 11 modules.

---

## Task 7: Regenerate RAG tree and build

- [ ] Regenerate `docs/_data/rag_tree.json`:

```bash
cd "/Users/kyawminthu/Dev/Control System Tools" && python3 tools/generate_rag_tree.py
```

- [ ] Run Jekyll build:

```bash
cd "/Users/kyawminthu/Dev/Control System Tools/docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: clean build. Count should now be ~68+ pages.

- [ ] Spot-check `_site/training/nec-application/sccr-workflow/index.html`:
  - Contains `module-meta-bar` (level chip)
  - Contains `module-outcome` (summary sentence)
  - Contains `chip-intermediate` chip
  - Does not contain a duplicate `page-header`

---

## Task 8: Update project state

**Files:**
- `project_state/project_state.md`
- `project_state/change_log.md`

- [ ] In `project_state.md`:
  - Change current phase to `Phase 16 COMPLETE — NEC Training Expansion`
  - Change next phase to `Post-Phase 16 Planning — Training System Integration`
  - Mark all Phase 16 checkboxes complete

- [ ] In `change_log.md`, add:

```
### 2026-03-10 — Phase 16 complete: NEC Training Expansion

- Added 8 new NEC RAG training files to control-standards/rag/training_modules/nec_application/
- Published 8 new site pages under docs/training/nec-application/
- NEC track grows from 3 to 11 modules
- Updated training_catalog.yml: 8 new module entries, module_count 3→11,
  panel-design learning path expanded with 4 new NEC modules
- Updated _index.yaml, group page, and rag_tree.json
- Jekyll build: clean
```

---

## Explicit Deferrals

- Cross-linking new NEC modules into standards/crosswalk pages — low priority, can be added incrementally
- Filtering/sorting on landing page — deferred to post-Phase 16
- Training system integration (workflows, field checklists, reference library) — post-Phase 16 planning note already exists at `docs/plans/2026-03-10-training-system-integration-preplan.md`

## Out of Scope

- Changing any existing module page content
- Adding new RAG files outside `nec_application/`
- Changing URL slugs of existing pages
