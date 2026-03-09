# Electrical Knowledge Integration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Promote transcript-derived electrical knowledge into the existing RAG layers using clean rewrites with correct metadata. No new parallel layers.

**Architecture:** All content routes into `training_modules/`, `design_framework/`, `commissioning_checklists/checklists/`, or `standards_intelligence/crosswalks/overlap_notes/`. EV motor files are held as WIP.

**Design doc:** `docs/plans/2026-03-08-electrical-intelligence-integration-design.md`

**Tech Stack:** Markdown with YAML comment metadata, existing RAG folder structure

---

## Status

| Phase | Work | Status |
|---|---|---|
| Phase 0 | Segment NEC exam prep transcript | Complete |
| Phase 1 | Promote circuit-analysis theory into `fundamentals/` | Complete |
| Phase 2 | Update `fundamentals/` indexing | Complete |
| Phase 3 | Promote motor files into `electrical_machines/` | Complete |
| Phase 4 | Promote motor design workflows into `motor_systems/` | Complete |
| Phase 5 | Promote commissioning checklists | Complete |
| Phase 6 | Create motors/drives crosswalk files | Complete |
| Phase 7 | Promote NEC exam prep into `nec_application/` | Complete |
| Phase 8 | Update project tracking | Remaining |

---

## Content rules

1. Promoted files are rewrites, not transcript copies.
2. Every authoritative RAG file uses:
   - `CONTENT_CLASS: RAG_APPROVED`
   - `AI_READ_ACCESS: ALLOWED`
   - `STATUS: DRAFT`
3. Add `## Related standards` only where there is a real standards anchor.
4. Engineering heuristics are labeled as heuristics, not written as mandatory rules.
5. Do not append to `standards_intelligence/` files unless the source supports a verified standards-facing clarification.

---

## What is complete

### Phase 0 — NEC exam prep segmentation

**Source package created:**
`control-standards/work/design/project_implementation_gaps/nec_exam_prep_topics/`

### Phase 1 — Circuit analysis promotion into `fundamentals/`

All files exist at `control-standards/rag/training_modules/fundamentals/`:

- [x] `electrical_quantities_and_circuit_language.md`
  - Source: `circuit_analysis_overview_and_linear_elements.md`
  - Covers: voltage, current, resistance, power, circuit topology, linear elements

- [x] `series_parallel_and_divider_methods.md`
  - Source: `series_parallel_and_divider_methods.md`
  - Covers: series/parallel resistance, voltage divider, current divider, topology recognition

- [x] `kirchhoff_laws_and_systematic_analysis.md`
  - Sources: `kcl_and_nodal_analysis.md` + `kvl_and_loop_analysis.md` (merged)
  - Covers: KCL, KVL, nodal analysis, loop analysis, sign-convention discipline

- [x] `equivalent_circuit_methods.md`
  - Source: `source_transformation_and_equivalent_methods.md`
  - Covers: source transformation, Thevenin, Norton, superposition

- [x] `electrical_equations_reference.md`
  - Source: equation set across the circuit-analysis topic files
  - Covers: Ohm's law, power, series/parallel, dividers, KCL/KVL, Thevenin/Norton, capacitor energy

- [x] `passive_components_resistors_capacitors.md`
  - Source: `practical_components_resistors_and_capacitors.md`
  - Covers: resistor and capacitor purpose, rating awareness, polarity, stored-energy caution

- [x] `diodes_transistors_and_switching_basics.md`
  - Source: `practical_components_diodes_and_transistors.md`
  - Covers: diode families, LEDs, zeners, BJT/MOSFET/IGBT basics

### Phase 2 — `fundamentals/` indexing

- [x] `README.md` updated
- [x] `_index.yaml` updated

### Phase 3 — Motors promotion into `electrical_machines/`

All files exist at `control-standards/rag/training_modules/electrical_machines/`:

- [x] `induction_motor_basics.md`
- [x] `dc_motor_basics.md`
- [x] `motor_nameplates_slip_and_torque.md`
- [x] `vfd_fundamentals.md`
- [x] `servo_drive_fundamentals.md`
- [x] `ac_vs_dc_motor_comparison.md`
- [x] `motor_family_comparison.md`
- [x] `brushless_dc_ev_and_drone_motor_comparison.md`
- [x] `vfd_and_servo_architecture_diagrams.md`
- [x] `README.md`, `_index.yaml`

### Phase 4 — Motor design workflows into `motor_systems/`

All files exist at `control-standards/rag/design_framework/motor_systems/`:

- [x] `motor_selection_workflow.md`
- [x] `motor_nameplate_review_checklist.md`
- [x] `star_delta_and_supply_matching_notes.md`
- [x] `vfd_motor_integration_review.md`
- [x] `vfd_commissioning_workflow.md`
- [x] `servo_commissioning_workflow.md`
- [x] `motor_troubleshooting_decision_tree.md`
- [x] `motor_selection_comparison_matrix.md`
- [x] `integrated_motor_drive_architecture_comparison.md`
- [x] `integrated_drive_failure_modes_and_tradeoffs.md`
- [x] `integrated_drive_serviceability_and_field_replacement_review.md`
- [x] `motor_mounted_drive_thermal_and_emc_design_notes.md`
- [x] `industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md`
- [x] `README.md`, `_index.yaml`

Circuit analysis workflows at `control-standards/rag/design_framework/electrical_review/`:

- [x] `ohms_law_and_power_check_workflow.md`
- [x] `basic_resistive_network_review.md`
- [x] `component_selection_basics.md`
- [x] `simple_signal_and_interface_circuit_notes.md`
- [x] `README.md`, `_index.yaml`

### Phase 5 — Commissioning checklists

All files exist at `control-standards/rag/commissioning_checklists/checklists/`:

- [x] `motor_rotation_and_overload_verification.md`
- [x] `motor_nameplate_and_overload_setting.md`
- [x] `basic_circuit_polarity_and_power_checks.md`
- [x] `capacitor_discharge_awareness_check.md`
- [x] `drive_commissioning.md`
- [x] `pre_power_panel_and_incoming_supply_check.md`
- [x] `README.md`, `_index.yaml`

### Phase 6 — Crosswalk gap fills

Both files exist at `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/`:

- [x] `overlap__motors_drives.md`
- [x] `overlap_nfpa79_iec60204__motors_drives.md`

### Phase 7 — NEC application modules

All files exist at `control-standards/rag/training_modules/nec_application/`:

- [x] `nec_code_reading_fundamentals.md`
- [x] `working_space_and_table_navigation.md`
- [x] `motor_and_panel_code_application.md`
- [x] `README.md`, `_index.yaml`

---

## Phase 8 — Update project tracking (remaining)

### Task 8.1 — Run validation

```bash
python3 tools/project_automator.py
```

Expected: clean run with updated structure summary.

Note: `validate_ai_boundaries.py` and `validate_reorg.sh all` have 7 known pre-existing
failures unrelated to this work. Do not use as acceptance gates.

### Task 8.2 — Update `project_state/change_log.md`

Add an entry for Phase 11 completion:

```markdown
### 2026-03-09 — Phase 11 Complete: Electrical Knowledge Integration

Promoted three transcript-derived knowledge sources into the existing RAG layers.
No new parallel layer created.

#### training_modules/fundamentals/ (new)
- 7 new files: circuit quantities, series/parallel, KCL/KVL, equivalent circuits,
  equations reference, passive components, diodes/transistors

#### training_modules/electrical_machines/ (expanded)
- 6 additional files beyond the original 3 motor basics files:
  vfd_fundamentals, servo_drive_fundamentals, comparisons, architecture diagrams

#### training_modules/nec_application/ (new)
- 3 files: code reading, table navigation, motor/panel application

#### design_framework/electrical_review/ (new)
- 4 files: Ohm's law workflow, resistive network review,
  component selection, signal/interface circuit notes

#### design_framework/motor_systems/ (expanded)
- 10 additional workflow and design files beyond the original motor basics

#### commissioning_checklists/checklists/ (expanded)
- 6 files: motor, drive, circuit, and panel commissioning

#### standards_intelligence/crosswalks/overlap_notes/ (gap fill)
- overlap__motors_drives.md
- overlap_nfpa79_iec60204__motors_drives.md
```

### Task 8.3 — Update `project_state/project_state.md`

Mark Phase 11 complete and update the active priorities section.

### Task 8.4 — Commit

```bash
git add project_state/
git commit -m "chore(state): mark Phase 11 complete — electrical knowledge integration"
```

---

## Acceptance criteria

This plan is complete when:

- [x] All circuit-analysis modules exist under `training_modules/fundamentals/`
- [x] All motor modules exist under `training_modules/electrical_machines/`
- [x] All NEC application modules exist under `training_modules/nec_application/`
- [x] All electrical review workflows exist under `design_framework/electrical_review/`
- [x] All motor system workflows exist under `design_framework/motor_systems/`
- [x] All commissioning checklists exist under `commissioning_checklists/checklists/`
- [x] Both motors/drives crosswalk files exist
- [x] Metadata follows current repo convention (`RAG_APPROVED`, not `PROMOTED`)
- [x] No unsupported engineering rules written as mandatory requirements
- [x] No new parallel knowledge layer introduced
- [ ] `python3 tools/project_automator.py` runs cleanly
- [ ] `project_state/` updated to reflect Phase 11 complete
