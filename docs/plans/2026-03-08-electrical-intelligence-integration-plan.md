# Electrical Intelligence Integration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build `control-standards/rag/electrical_intelligence/` — a new knowledge layer parallel to `standards_intelligence/` — by promoting three transcript-derived sources into clean teaching modules, design workflows, commissioning checklists, and standards crosswalks.

**Architecture:** Three sources (circuit analysis, motors, NEC exam prep) are rewritten (not copied) into a coordinated `electrical_intelligence/` folder tree. Nothing enters `standards_intelligence/` unless compliance-verified. EV motor files are held as WIP and skipped.

**Design doc:** `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

**Tech Stack:** Markdown, YAML front matter, Jekyll static site (presentation layer reads from `rag/` but is not modified in this plan)

---

## Content Rules (read before every task)

1. Promoted files are **rewrites**, not copies of transcript summaries. Write in clean, direct engineering prose.
2. Every promoted file must open with a YAML-style comment block declaring:
   - `SOURCE:` — which source file(s) it was derived from
   - `PROMOTION_TARGET:` — which layer it belongs to
   - `CONTENT_CLASS: PROMOTED`
   - `AI_READ_ACCESS: ALLOWED`
3. Add a short `## Related standards` section at the bottom of any file where NEC/NFPA79/IEC60204-1 applies.
4. Do not invent compliance claims. If unsure, write "verify against [standard]" rather than asserting.
5. Crosswalk files in `standards_intelligence/` must be anchored to real article/clause numbers from existing RAG files.

---

## Phase 11.0 — Segment NEC Exam Prep Transcript

**Source:** `control-standards/work/design/electrical exam prep.md`
**Output folder:** `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/`

### Task 0.1: Read and map the transcript

**Files:**
- Read: `control-standards/work/design/electrical exam prep.md`

**Step 1:** Read the full transcript. Identify all lesson boundaries — look for topic shifts, new section headers, or timestamp jumps.

**Step 2:** List every distinct topic in order with approximate source range (timestamp or line range).

**Step 3:** Group topics into these expected segments:
- NEC code-reading method and structure
- Motor circuits and branch protection (Art 430 territory)
- Panel and control circuit application (Art 409, Art 725 territory)
- Grounding and bonding application (Art 250 territory)
- Overcurrent and feeder application (Art 240, Art 215 territory)
- Practical job-site application notes (anything that doesn't map to a specific article)

Note any segments that don't fit the above groups — they may need a new destination.

### Task 0.2: Write topic files

**Files:**
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_code_reading_and_structure.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_motor_circuits_art430.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_panel_and_control_circuits_art409_art725.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_grounding_and_bonding_art250.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_overcurrent_and_feeders_art240_art215.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/nec_practical_jobsite_notes.md`

**Step 1:** For each segment identified in Task 0.1, write a topic file. Follow the header pattern from the existing `motors_topics/` files:

```markdown
<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: NEC_EXAM_PREP
-->

# [Topic Title]

## What this file is
[One paragraph describing source and scope]

## Topic focus
[One paragraph on what this segment covers]

## Main concepts captured
[Structured bullet points — not raw transcript prose]

## Important caution
This is a transcript-derived work note. Verify all code citations against NEC 2023 before design use.
```

**Step 2:** Write each file. Keep concepts structured, not paragraph-dense.

### Task 0.3: Write README and INTEGRATION_PLAN

**Files:**
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/README.md`
- Create: `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/INTEGRATION_PLAN.md`

**Step 1:** Write `README.md` — mirror the structure of `motors_topics/README.md`. List all topic files with one-line descriptions and a category map.

**Step 2:** Write `INTEGRATION_PLAN.md` — mirror the structure of `motors_topics/INTEGRATION_PLAN.md`. For each file, state:
- promotion target
- destination file path
- whether it goes into `electrical_intelligence/training_modules/nec_application/` or as an addendum to an existing NEC standards file
- promotion confidence (TRAINING_ONLY / STANDARDS_ADDENDUM / HOLD_WIP)

### Task 0.4: Commit Phase 11.0

```bash
git add control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/
git commit -m "feat(rag): segment NEC exam prep transcript into nec_exam_prep_topics"
```

---

## Phase 11.1 — Scaffold `electrical_intelligence/`

### Task 1.1: Create directory tree

**Files to create:**
- `control-standards/rag/electrical_intelligence/README.md`
- `control-standards/rag/electrical_intelligence/_index.yaml`
- `control-standards/rag/electrical_intelligence/training_modules/README.md`
- `control-standards/rag/electrical_intelligence/training_modules/_index.yaml`
- `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/README.md`
- `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/_index.yaml`
- `control-standards/rag/electrical_intelligence/training_modules/electronics_basics/README.md`
- `control-standards/rag/electrical_intelligence/training_modules/electronics_basics/_index.yaml`
- `control-standards/rag/electrical_intelligence/training_modules/electrical_machines/README.md`
- `control-standards/rag/electrical_intelligence/training_modules/electrical_machines/_index.yaml`
- `control-standards/rag/electrical_intelligence/training_modules/nec_application/README.md`
- `control-standards/rag/electrical_intelligence/training_modules/nec_application/_index.yaml`
- `control-standards/rag/electrical_intelligence/design_framework/README.md`
- `control-standards/rag/electrical_intelligence/design_framework/_index.yaml`
- `control-standards/rag/electrical_intelligence/design_framework/electrical_review/README.md`
- `control-standards/rag/electrical_intelligence/design_framework/electrical_review/_index.yaml`
- `control-standards/rag/electrical_intelligence/design_framework/motor_systems/README.md`
- `control-standards/rag/electrical_intelligence/design_framework/motor_systems/_index.yaml`
- `control-standards/rag/electrical_intelligence/commissioning_checklists/README.md`
- `control-standards/rag/electrical_intelligence/commissioning_checklists/_index.yaml`

**Step 1:** Write `control-standards/rag/electrical_intelligence/README.md`:

```markdown
<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: LAYER_INDEX
-->

# Electrical Intelligence

Educational and applied engineering content derived from transcript-based learning sources.

This layer is parallel to `standards_intelligence/` but serves a different purpose:
it provides teaching modules, design workflows, and commissioning checklists.

It is NOT the authoritative standards layer. For compliance decisions, use `standards_intelligence/`.

## Structure

- `training_modules/` — teaching modules by topic area
- `design_framework/` — applied engineering workflows and checklists
- `commissioning_checklists/` — field verification checklists

## Source material

All content in this layer was derived from:
- `work/design/project_implementation_gaps/electrical_and_practical_circuit_analysis_topics/`
- `work/design/project_implementation_gaps/motors_topics/`
- `work/design/project_implementation_gaps/nec_exam_prep_topics/`
```

**Step 2:** Write `_index.yaml` for each folder. Use this pattern:

```yaml
# electrical_intelligence/_index.yaml
layer: electrical_intelligence
content_class: PROMOTED
sublayers:
  - training_modules
  - design_framework
  - commissioning_checklists
```

For sub-folder `_index.yaml` files, list the files that will be created in that folder (they can be placeholders at this stage).

**Step 3:** Write one-line `README.md` for each subfolder explaining what belongs there.

### Task 1.2: Validate scaffold

**Step 1:** Run:
```bash
find control-standards/rag/electrical_intelligence -type f | sort
```

Expected: all 20 scaffold files listed.

**Step 2:** Confirm no content files yet — only `README.md` and `_index.yaml` at each level.

### Task 1.3: Commit Phase 11.1

```bash
git add control-standards/rag/electrical_intelligence/
git commit -m "feat(rag): scaffold electrical_intelligence layer structure"
```

---

## Phase 11.2 — Promote Circuit Analysis Files

**Source folder:** `control-standards/work/design/project_implementation_gaps/electrical_and_practical_circuit_analysis_topics/`

Read the source folder's `INTEGRATION_PLAN.md` before starting each task.

### Task 2.1: `electrical_quantities_and_circuit_language.md`

**Source:** `circuit_analysis_overview_and_linear_elements.md`
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/electrical_quantities_and_circuit_language.md`

**Step 1:** Read the source file fully.

**Step 2:** Write the promoted file. Structure:
- Opening comment block (SOURCE, PROMOTION_TARGET, CONTENT_CLASS, AI_READ_ACCESS)
- `# Electrical Quantities and Circuit Language`
- `## Voltage, current, and resistance` — define each clearly
- `## Power` — P = VI relationship
- `## Circuit topology` — nodes, branches, loops, sources, passive elements
- `## Linear elements` — resistors, capacitors, inductors (brief)
- `## Related standards` — narrow link to NEC Art 110 (general installation requirements) where conductor sizing and voltage concepts apply

**Step 3:** Verify file is a clean teaching module, not a transcript summary. No phrases like "the video explains" or "the instructor says".

### Task 2.2: `series_parallel_and_divider_methods.md` (training)

**Source:** `series_parallel_and_divider_methods.md`
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/series_parallel_and_divider_methods.md`

**Step 1:** Read source file.

**Step 2:** Write the training module. Structure:
- `## Series resistance` — R_eq = R1 + R2 + ... formula, when it applies
- `## Parallel resistance` — 1/R_eq formula, two-resistor shortcut
- `## Voltage divider` — V_out = V_s × (R2 / (R1+R2)), loading effect warning
- `## Current divider` — I_x = I_s × (R_other / (R_x + R_other))
- `## Topology recognition` — how to identify series vs parallel at a glance
- No standards link needed here

### Task 2.3: `basic_resistive_network_review.md` (design framework)

**Source:** `series_parallel_and_divider_methods.md` (applied portion)
**Target:** `control-standards/rag/electrical_intelligence/design_framework/electrical_review/basic_resistive_network_review.md`

**Step 1:** Write as a workflow/checklist, not a teaching module. Structure:
- `## When to use this review` — scope: quick field or design-check for resistive networks
- `## Step 1: Identify topology` — series, parallel, or mixed
- `## Step 2: Simplify` — reduction steps
- `## Step 3: Check divider loading` — is the load impedance ≥10× divider resistance?
- `## Step 4: Verify power ratings` — P = V²/R check for each resistor
- `## Common mistakes` — wrong topology assumption, ignoring load on divider

### Task 2.4: `kirchhoff_laws_and_systematic_analysis.md`

**Sources:** `kcl_and_nodal_analysis.md` + `kvl_and_loop_analysis.md` (merge)
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/kirchhoff_laws_and_systematic_analysis.md`

**Step 1:** Read both source files.

**Step 2:** Write merged module. Structure:
- `## Kirchhoff's Current Law (KCL)` — sum of currents at a node = 0, sign convention
- `## Kirchhoff's Voltage Law (KVL)` — sum of voltages around a loop = 0, sign convention
- `## Nodal analysis` — steps: choose reference node, write KCL at each unknown node, solve
- `## Loop (mesh) analysis` — steps: assign mesh currents, write KVL for each mesh, solve
- `## Choosing a method` — when nodal is faster, when loop is faster
- `## Sign convention discipline` — wrong assumed direction gives negative answer, not an error

### Task 2.5: `equivalent_circuit_methods.md`

**Source:** `source_transformation_and_equivalent_methods.md`
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/equivalent_circuit_methods.md`

**Step 1:** Read source file.

**Step 2:** Write module. Structure:
- `## Source transformation` — V_s = I_s × R, when to use
- `## Thevenin equivalent` — V_th (open-circuit voltage), R_th (dead-network resistance), steps
- `## Norton equivalent` — I_n = V_th / R_th, parallel form
- `## Superposition` — one independent source at a time, sum results
- `## Practical use` — simplifying drive/load interface models

### Task 2.6: `canonical_equations.md`

**Source:** All circuit analysis source files + `electrical_and_practical_circuit_analysis_topics/INTEGRATION_PLAN.md` (equations section)
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/canonical_equations.md`

**Step 1:** Write a single consolidated reference file. Structure:
- `## Ohm's law` — V = IR, I = V/R, R = V/I
- `## Power` — P = VI, P = I²R, P = V²/R
- `## Series resistance` — R_eq = R1 + R2 + ...
- `## Parallel resistance` — 1/R_eq = 1/R1 + 1/R2 + ...
- `## Voltage divider` — V_out = V_s × (R_x / R_total)
- `## Current divider` — I_x = I_s × (R_other / (R_x + R_other))
- `## KCL` — Σ I_in = Σ I_out at a node
- `## KVL` — Σ V around a closed loop = 0
- `## Nodal current` — I = (V_a - V_b) / R
- `## Source transformation` — V_s = I_s × R
- `## Thevenin/Norton` — V_th = I_n × R_th
- `## Capacitor energy` — E = ½CV²

**Step 2:** Keep it dense — this is a reference card, not a teaching module. No explanatory prose beyond one-line descriptions per equation.

### Task 2.7: Electronics basics files

**Source:** `practical_components_resistors_and_capacitors.md`, `practical_components_diodes_and_transistors.md`
**Targets:**
- `control-standards/rag/electrical_intelligence/training_modules/electronics_basics/resistors_capacitors_and_ratings.md`
- `control-standards/rag/electrical_intelligence/training_modules/electronics_basics/diodes_transistors_and_switching.md`

**Step 1:** Read both source files.

**Step 2:** Write `resistors_capacitors_and_ratings.md`. Structure:
- `## Resistors` — types, tolerance, power rating, temperature coefficient
- `## Capacitors` — types, voltage rating, stored energy (E = ½CV²), polarity for electrolytics
- `## Practical sizing` — resistor wattage margin (use 50% derating), capacitor voltage margin (use 80% of rating)
- `## Related standards` — narrow link: capacitor stored energy → NFPA 79 Ch 7 (protection against electric shock), IEC 60204-1 Cl 6 (residual voltage discharge)

**Step 3:** Write `diodes_transistors_and_switching.md`. Structure:
- `## Diodes` — forward voltage drop, polarity, rectifier vs signal vs zener vs LED
- `## Transistors (BJT)` — NPN/PNP, saturation/cutoff, base drive
- `## MOSFETs and IGBTs` — gate-drive basics, enhancement mode, drive vs power applications
- `## Flyback diodes` — why inductive loads need them, placement
- No standards link needed

### Task 2.8: `ohms_law_and_power_check_workflow.md`

**Source:** `practical_ohms_law_power_and_resistor_color_code.md`
**Target:** `control-standards/rag/electrical_intelligence/design_framework/electrical_review/ohms_law_and_power_check_workflow.md`

**Step 1:** Read source file.

**Step 2:** Write as a practical workflow. Structure:
- `## Quick current estimate` — measured voltage drop across known resistance → I = V/R
- `## Resistor wattage check` — P = V²/R or P = I²R, apply 50% derating
- `## LED current check` — (V_supply - V_f) / R_series
- `## Resistor color code` — 4-band and 5-band table (include the table)
- `## Common field checks` — list of five quick checks an engineer can do at the bench

### Task 2.9: `component_selection_basics.md`

**Source:** Both practical component files
**Target:** `control-standards/rag/electrical_intelligence/design_framework/electrical_review/component_selection_basics.md`

**Step 1:** Write as a selection guide. Structure:
- `## Resistor selection` — resistance value, power rating, tolerance, temperature
- `## Capacitor selection` — capacitance, voltage, type (ceramic/electrolytic/film), polarity
- `## Diode selection` — V_f, V_r, I_f, recovery time, application type
- `## Transistor/FET selection` — V_ce or V_ds, I_c or I_d, R_ds(on), gate drive requirements
- `## General rule` — always derate: 50% power, 80% voltage, 80% current

### Task 2.10: Commit Phase 11.2

**Step 1:** Update `_index.yaml` for `electrical_fundamentals/` and `electronics_basics/` and `design_framework/electrical_review/` to list all newly created files.

**Step 2:**
```bash
git add control-standards/rag/electrical_intelligence/training_modules/electrical_fundamentals/
git add control-standards/rag/electrical_intelligence/training_modules/electronics_basics/
git add control-standards/rag/electrical_intelligence/design_framework/electrical_review/
git commit -m "feat(rag): promote circuit analysis files into electrical_intelligence"
```

---

## Phase 11.3 — Promote Motor Files + Commissioning Checklists

**Source folder:** `control-standards/work/design/project_implementation_gaps/motors_topics/`

Read the source folder's `INTEGRATION_PLAN.md` before starting each task.

### Task 3.1: `induction_motor_basics.md`

**Sources:** `induction_motor_construction_and_rotating_field.md` + `induction_motor_components_induction_and_slip.md` (merge)
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_machines/induction_motor_basics.md`

**Step 1:** Read both source files.

**Step 2:** Write merged module. Structure:
- `## Stator and rotating magnetic field` — three-phase winding, pole pairs, synchronous speed formula (n_s = 120f/p)
- `## Rotor and induction` — squirrel cage construction, how current is induced, why the rotor follows the field
- `## Slip` — definition (s = (n_s - n_r) / n_s), typical values at full load (1–5%), why slip must be non-zero
- `## Torque production` — relationship between slip, rotor current, and torque
- `## Starting behavior` — high inrush at start, torque curve shape
- `## Related standards` — NEC Art 430 (branch circuit sizing, overload protection), NFPA 79 Ch 12 (machine motor integration)

### Task 3.2: `dc_motor_basics.md`

**Sources:** `dc_motor_magnetism_stator_and_mechanical_structure.md` + `dc_motor_armature_winding_and_torque_production.md` + `dc_motor_commutator_brushes_and_power_path.md` (merge all three)
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_machines/dc_motor_basics.md`

**Step 1:** Read all three source files.

**Step 2:** Write merged module. Structure:
- `## Stator and field excitation` — permanent magnet vs wound field, flux path
- `## Armature construction` — windings, slots, coils
- `## Torque production` — F = BIL, how current in a magnetic field produces rotation
- `## Commutator and brushes` — mechanical rectification, carbon brush contact, current path
- `## Back-EMF` — why it limits speed and current at steady state
- `## Speed control` — armature voltage control vs field weakening
- `## Maintenance considerations` — brush wear, commutator condition, sparking causes
- `## Related standards` — NEC Art 430 applies; note DC-specific considerations for drives

### Task 3.3: `motor_nameplates_slip_and_torque.md`

**Source:** `induction_motor_poles_torque_curves_and_nema_designs.md`
**Target:** `control-standards/rag/electrical_intelligence/training_modules/electrical_machines/motor_nameplates_slip_and_torque.md`

**Step 1:** Read source file.

**Step 2:** Write module. Structure:
- `## NEMA design letters` — A, B, C, D: torque and slip characteristics for each, typical applications
- `## Torque curve` — breakdown torque, pull-up torque, full-load torque, locked-rotor torque; what each region means
- `## Nameplate rated speed` — why it shows rated (not synchronous) speed, how to infer synchronous speed
- `## Poles and synchronous speed` — 2-pole = 3600 RPM, 4-pole = 1800 RPM, 6-pole = 1200 RPM (60 Hz), formula
- `## Selecting by NEMA design` — when to use B (general), when to use D (high-inertia loads)
- `## Related standards` — NEC Art 430 overload sizing, NFPA 79 Ch 12 motor selection context

### Task 3.4: `star_delta_and_supply_matching_notes.md`

**Source:** `induction_motor_terminal_connections_and_star_delta.md`
**Target:** `control-standards/rag/electrical_intelligence/design_framework/motor_systems/star_delta_and_supply_matching_notes.md`

**Step 1:** Read source file.

**Step 2:** Write as a design note. Structure:
- `## Terminal markings` — T1–T9 (NEMA) vs U1/V1/W1 (IEC), what they mean
- `## Wye (star) connection` — when to use, voltage relationship
- `## Delta connection` — when to use, voltage relationship
- `## Dual-voltage motors` — 230/460 V example: wye for high voltage, delta for low voltage
- `## Supply voltage matching` — how to read nameplate to confirm correct connection
- `## Star-delta starting` — reduced-voltage starting sequence, torque reduction tradeoff
- `## Verification step` — always confirm nameplate voltage matches supply before energizing
- `## Related standards` — NEC Art 430, IEC 60204-1 Cl 12

### Task 3.5: `motor_selection_workflow.md`

**Source:** `induction_motor_poles_torque_curves_and_nema_designs.md` (selection logic portion)
**Target:** `control-standards/rag/electrical_intelligence/design_framework/motor_systems/motor_selection_workflow.md`

**Step 1:** Write as a step-by-step workflow. Structure:
- `## Step 1: Define load requirements` — torque, speed, duty cycle, starting conditions
- `## Step 2: Select horsepower` — from load torque and speed, add service factor margin
- `## Step 3: Select NEMA design letter` — B for most applications, D for high-inertia, C for high starting torque
- `## Step 4: Confirm voltage and phase` — match to available supply, verify nameplate
- `## Step 5: Select enclosure` — ODP, TEFC, TENV — based on environment
- `## Step 6: Verify frame size` — mounting compatibility
- `## Step 7: Size overload protection` — per NEC Art 430.32 (125% of FLA for SF ≥ 1.15, 115% for others)
- `## Common mistakes` — oversizing motor (poor power factor), wrong NEMA design for load type

### Task 3.6: `motor_nameplate_review_checklist.md`

**Source:** `induction_motor_nameplate_and_enclosures.md`
**Target:** `control-standards/rag/electrical_intelligence/design_framework/motor_systems/motor_nameplate_review_checklist.md`

**Step 1:** Read source file.

**Step 2:** Write as a design review checklist. Structure:
- `## Checklist: nameplate data verification`
  - [ ] HP / kW confirmed for application
  - [ ] Rated voltage matches available supply
  - [ ] Rated frequency matches supply (50 or 60 Hz)
  - [ ] Phase confirmed (single-phase or three-phase)
  - [ ] FLA noted for overload sizing
  - [ ] Service factor noted
  - [ ] Insulation class confirmed for ambient temperature
  - [ ] Frame size confirmed for mounting
  - [ ] Enclosure type confirmed for environment
  - [ ] NEMA design letter confirmed for load type
- `## Related standards` — NEC Art 430.7 (nameplate requirements), NFPA 79 Ch 12

### Task 3.7: `vfd_motor_integration_review.md`

**Source:** Derived from induction motor files + existing NEC Art 430 and NFPA79 Ch 12 RAG files
**Target:** `control-standards/rag/electrical_intelligence/design_framework/motor_systems/vfd_motor_integration_review.md`

**Step 1:** Read `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md` and `control-standards/rag/standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md` to anchor any compliance claims.

**Step 2:** Write as a design review note. Structure:
- `## Motor suitability for VFD` — inverter-duty rating, insulation class (F or H preferred), shaft grounding
- `## Cable selection` — shielded cable between VFD and motor, shield termination at VFD only
- `## Overload protection` — electronic overload in VFD vs separate overload relay, NEC 430.52 context
- `## Motor disconnect` — NEC 430.102 requirement, placement relative to VFD
- `## Braking considerations` — dynamic braking resistor, regenerative braking, NFPA 79 stop categories
- `## EMC notes` — cable length limits, common-mode choke use cases
- `## Related standards` — NEC Art 430, NFPA 79 Ch 12, IEC 60204-1 Cl 12; verify specific requirements before design use

### Task 3.8: Commissioning checklists

**Targets:**
- `control-standards/rag/electrical_intelligence/commissioning_checklists/motor_rotation_and_overload_verification.md`
- `control-standards/rag/electrical_intelligence/commissioning_checklists/motor_nameplate_and_overload_setting.md`
- `control-standards/rag/electrical_intelligence/commissioning_checklists/basic_circuit_polarity_and_power_checks.md`
- `control-standards/rag/electrical_intelligence/commissioning_checklists/capacitor_discharge_awareness_check.md`

**Step 1:** Write `motor_rotation_and_overload_verification.md`:
- Pre-power checks: nameplate confirmed, overload relay set, direction of rotation marked
- First energization: jog only, confirm rotation direction
- Full-speed run: confirm current within FLA, check for vibration or noise
- Overload verification: confirm overload trip current setting (NEC 430.32)

**Step 2:** Write `motor_nameplate_and_overload_setting.md`:
- Record nameplate FLA
- Determine overload relay setting (125% of FLA for SF ≥ 1.15; 115% otherwise)
- Set and lock overload relay
- Document settings on motor schedule or panel label

**Step 3:** Write `basic_circuit_polarity_and_power_checks.md`:
- DC circuit: confirm polarity before energizing (measure supply, check component orientation)
- AC circuit: confirm phase and neutral assignment
- Signal circuits: confirm signal level and range before connecting to input card
- Power check: measure loaded voltage, confirm within tolerance

**Step 4:** Write `capacitor_discharge_awareness_check.md`:
- Identify all capacitors in circuit (filter caps, drive DC bus, power supply hold-up)
- After de-energizing: wait per manufacturer's discharge specification (commonly 5 minutes for drives)
- Measure DC bus voltage before touching drive terminals — must be below 50 VDC (or per nameplate)
- Related: NFPA 79 Ch 7, IEC 60204-1 Cl 6 residual voltage requirements; verify against actual standard before specifying wait time

### Task 3.9: Commit Phase 11.3

**Step 1:** Update `_index.yaml` files for `electrical_machines/`, `motor_systems/`, and `commissioning_checklists/`.

**Step 2:**
```bash
git add control-standards/rag/electrical_intelligence/training_modules/electrical_machines/
git add control-standards/rag/electrical_intelligence/design_framework/motor_systems/
git add control-standards/rag/electrical_intelligence/commissioning_checklists/
git commit -m "feat(rag): promote motor files and commissioning checklists into electrical_intelligence"
```

---

## Phase 11.4 — Create Missing Motors/Drives Crosswalk Files

**Target folder:** `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/`

Before writing, read both anchor files:
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md`
- `control-standards/rag/standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md`

Also read IEC 60204-1 if present:
```bash
find control-standards/rag/standards_intelligence -name "*60204*" | head -5
```

### Task 4.1: `overlap__motors_drives.md`

**Target:** `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/overlap__motors_drives.md`

**Step 1:** Write the crosswalk. Structure:
- `## Standards in scope` — NEC Art 430, NFPA 79 Ch 12, IEC 60204-1 Cl 12, UL 508A motor/drive content
- `## Who owns branch-circuit motor protection math` — NEC Art 430 (US); table answer with article references
- `## Who owns machine motor integration and stop behavior` — NFPA 79 Ch 12 for US machines; IEC 60204-1 Cl 9/12 for international
- `## VFD cable and shield guidance` — IEC 60204-1 Cl 12 primary; NEC Art 430 for feeder/disconnect
- `## STO and safe-stop context` — functional safety standards (ISO 13849-1, IEC 62061) own STO; NFPA 79 Ch 9 owns stop categories for the machine
- `## Overload protection jurisdiction` — NEC 430.32 for branch circuit; NFPA 79 12.6 for machine application
- `## Local isolation and disconnect` — NEC 430.102 for branch circuit; NFPA 79 Ch 5 for machine disconnect
- `## Key conflicts or gaps` — note any areas where the standards give different requirements for the same situation

**Step 2:** Every claim must trace to a specific article or clause number from the RAG files you read. Do not make up clause numbers.

### Task 4.2: `overlap_nfpa79_iec60204__motors_drives.md`

**Target:** `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/overlap_nfpa79_iec60204__motors_drives.md`

**Step 1:** Write as a paired comparison. Structure:
- `## Motor suitability` — NFPA 79 12.2 vs IEC 60204-1 Cl 12.2
- `## Drive integration` — NFPA 79 12.7 vs IEC 60204-1 Cl 12.6
- `## Motor protection` — NFPA 79 12.6 vs IEC 60204-1 Cl 12.5
- `## Starting and braking` — NFPA 79 vs IEC 60204-1 stop/braking requirements
- `## Isolation and switching` — NFPA 79 Ch 5 vs IEC 60204-1 Cl 5
- `## Where they align` — common requirements shared by both
- `## Where they diverge` — US-specific vs international-specific requirements

**Step 2:** Same rule — every claim traces to a specific clause from the RAG files.

### Task 4.3: Commit Phase 11.4

```bash
git add control-standards/rag/standards_intelligence/crosswalks/overlap_notes/overlap__motors_drives.md
git add control-standards/rag/standards_intelligence/crosswalks/overlap_notes/overlap_nfpa79_iec60204__motors_drives.md
git commit -m "feat(rag): add motors_drives crosswalk overlap notes"
```

---

## Phase 11.5 — Promote NEC Exam Prep Content

**Depends on:** Phase 11.0 (segmentation complete) + Phase 11.1 (scaffold complete)

**Source folder:** `control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/`

Read the folder's `INTEGRATION_PLAN.md` before each task.

### Task 5.1: `nec_code_reading_fundamentals.md`

**Source:** `nec_exam_prep_topics/nec_code_reading_and_structure.md`
**Target:** `control-standards/rag/electrical_intelligence/training_modules/nec_application/nec_code_reading_fundamentals.md`

**Step 1:** Read source file.

**Step 2:** Write as a teaching module. Structure:
- `## How the NEC is organized` — chapters, articles, sections, exceptions
- `## How to read an article` — scope first, then definitions, then rules, then exceptions
- `## Mandatory vs permissive language` — "shall" vs "shall be permitted"
- `## How exceptions work` — exception narrows the rule; always read the parent rule first
- `## Tables and their limits` — conditions of use, Notes, footnotes
- `## Common misreads` — list of 5–7 frequent misinterpretations from the exam prep source

### Task 5.2: `motors_and_panel_code_application.md`

**Sources:** Motor circuits, panel/control circuit, and job-site notes segments
**Target:** `control-standards/rag/electrical_intelligence/training_modules/nec_application/motors_and_panel_code_application.md`

**Step 1:** Read the relevant source files from `nec_exam_prep_topics/`.

**Step 2:** Write as an applied reference module. Structure:
- `## Motor branch circuit sizing (Art 430)` — 125% FLA rule for conductors, overcurrent device sizing table
- `## Motor overload sizing (Art 430.32)` — 125% for SF ≥ 1.15, 115% for others
- `## Disconnect requirements (Art 430.102)` — in sight, within 50 ft, or lockable
- `## Industrial control panels (Art 409)` — SCCR marking, field wiring space
- `## Control circuits (Art 725)` — Class 1/2/3, power-limited vs non-power-limited
- `## Common field application notes` — from job-site segment of exam prep source

### Task 5.3: Add addenda to existing NEC standards files

For each of the following, check whether the NEC exam prep content adds meaningful field-application clarity not already in the file. Only add content that genuinely extends the existing file.

**Files to check and potentially extend:**
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md`
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art409__industrial_control_panels.md`
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art725__class_1_2_3_control_circuits.md`
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art250__grounding_and_bonding.md`
- `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md`

**Step 1:** Read each file.

**Step 2:** For each file, determine: does the exam prep source add anything not already covered?
- If yes: add a `## Field application notes` section at the bottom with 3–5 bullets. Keep it short.
- If no: leave the file unchanged.

**Step 3:** Never rewrite existing content in `standards_intelligence/` files — only append.

### Task 5.4: Commit Phase 11.5

**Step 1:** Update `_index.yaml` for `nec_application/`.

**Step 2:**
```bash
git add control-standards/rag/electrical_intelligence/training_modules/nec_application/
git add control-standards/rag/standards_intelligence/us/nec/
git commit -m "feat(rag): promote NEC exam prep content into nec_application training modules"
```

---

## Final: Update Project State

**Files:**
- Modify: `project_state/project_state.md` — mark Phase 11 COMPLETE, update phase checkboxes
- Modify: `project_state/change_log.md` — add Phase 11 entry

```bash
git add project_state/
git commit -m "chore(state): mark Phase 11 complete — electrical_intelligence layer"
```

---

## Validation

After all phases complete, run:

```bash
find control-standards/rag/electrical_intelligence -type f | sort
```

Expected: 20 scaffold files + 19 content files = 39 files total.

```bash
find control-standards/rag/standards_intelligence/crosswalks/overlap_notes -name "*motors*"
```

Expected: 2 files (`overlap__motors_drives.md`, `overlap_nfpa79_iec60204__motors_drives.md`).

```bash
bash tools/validate_reorg.sh all
```

Expected: clean validation with no errors.
