# Design: Unified Electrical Knowledge Integration — Phase 11

**Date:** 2026-03-08
**Status:** Approved — queued for implementation
**Approach:** B — Unified electrical knowledge layer

---

## Summary

Integrate three transcript-derived electrical knowledge sources into a new
`control-standards/rag/electrical_intelligence/` layer, parallel to the
existing `standards_intelligence/` folder.

Nothing goes into `standards_intelligence/` unless it is compliance-verified.
All educational and applied engineering content lands in `electrical_intelligence/`.

---

## Sources

| Source | Location | Status |
|---|---|---|
| Circuit analysis + practical electronics | `work/design/project_implementation_gaps/electrical_and_practical_circuit_analysis_topics/` | Segmented, has integration plan |
| Motors (induction, DC) | `work/design/project_implementation_gaps/motors_topics/` | Segmented, has integration plan |
| NEC exam prep | `work/design/electrical exam prep.md` | Raw transcript — needs segmentation first |

EV motor files (`ev_motor_types_overview.md`, `ev_motor_powertrain_configurations.md`)
are held as WIP and not promoted in this phase.

---

## Architecture

`electrical_intelligence/` sits at `control-standards/rag/electrical_intelligence/`,
parallel to `standards_intelligence/`. The existing `rag/training_modules/` and
`rag/design_framework/` folders are not touched.

Standards crosswalk gap fills land inside `standards_intelligence/crosswalks/overlap_notes/`
as before — they are compliance content, not educational content.

```
rag/
├── standards_intelligence/        (existing — unchanged)
└── electrical_intelligence/       (new)
    ├── training_modules/
    │   ├── electrical_fundamentals/
    │   │   ├── electrical_quantities_and_circuit_language.md
    │   │   ├── series_parallel_and_divider_methods.md
    │   │   ├── kirchhoff_laws_and_systematic_analysis.md
    │   │   ├── equivalent_circuit_methods.md
    │   │   └── canonical_equations.md
    │   ├── electronics_basics/
    │   │   ├── resistors_capacitors_and_ratings.md
    │   │   └── diodes_transistors_and_switching.md
    │   ├── electrical_machines/
    │   │   ├── induction_motor_basics.md
    │   │   ├── dc_motor_basics.md
    │   │   └── motor_nameplates_slip_and_torque.md
    │   └── nec_application/
    │       ├── nec_code_reading_fundamentals.md
    │       └── motors_and_panel_code_application.md
    ├── design_framework/
    │   ├── electrical_review/
    │   │   ├── ohms_law_and_power_check_workflow.md
    │   │   ├── basic_resistive_network_review.md
    │   │   └── component_selection_basics.md
    │   └── motor_systems/
    │       ├── motor_selection_workflow.md
    │       ├── motor_nameplate_review_checklist.md
    │       ├── star_delta_and_supply_matching_notes.md
    │       └── vfd_motor_integration_review.md
    └── commissioning_checklists/
        ├── motor_rotation_and_overload_verification.md
        ├── motor_nameplate_and_overload_setting.md
        ├── basic_circuit_polarity_and_power_checks.md
        └── capacitor_discharge_awareness_check.md
```

---

## Source Routing

### Circuit Analysis Topics

| Source File | Destination | Notes |
|---|---|---|
| `circuit_analysis_overview_and_linear_elements.md` | `training_modules/electrical_fundamentals/electrical_quantities_and_circuit_language.md` | Rewrite as teaching module |
| `series_parallel_and_divider_methods.md` | `training_modules/electrical_fundamentals/series_parallel_and_divider_methods.md` + `design_framework/electrical_review/basic_resistive_network_review.md` | Split: theory → training, applied → design_framework |
| `kcl_and_nodal_analysis.md` + `kvl_and_loop_analysis.md` | `training_modules/electrical_fundamentals/kirchhoff_laws_and_systematic_analysis.md` | Merge into one module |
| `source_transformation_and_equivalent_methods.md` | `training_modules/electrical_fundamentals/equivalent_circuit_methods.md` | Teaching module only |
| `practical_ohms_law_power_and_resistor_color_code.md` | `design_framework/electrical_review/ohms_law_and_power_check_workflow.md` | Workflow-first rewrite |
| `practical_components_resistors_and_capacitors.md` | `training_modules/electronics_basics/resistors_capacitors_and_ratings.md` | Teaching + narrow standards links |
| `practical_components_diodes_and_transistors.md` | `training_modules/electronics_basics/diodes_transistors_and_switching.md` | Teaching module only |
| All theory equations | `training_modules/electrical_fundamentals/canonical_equations.md` | New consolidated file |

### Motors Topics

| Source File | Destination | Notes |
|---|---|---|
| `induction_motor_construction_and_rotating_field.md` + `induction_motor_components_induction_and_slip.md` | `training_modules/electrical_machines/induction_motor_basics.md` | Merge into one module |
| `induction_motor_terminal_connections_and_star_delta.md` | `design_framework/motor_systems/star_delta_and_supply_matching_notes.md` | Applied design note |
| `induction_motor_nameplate_and_enclosures.md` | `design_framework/motor_systems/motor_nameplate_review_checklist.md` + `commissioning_checklists/motor_nameplate_and_overload_setting.md` | Split: design artifact + checklist |
| `induction_motor_poles_torque_curves_and_nema_designs.md` | `training_modules/electrical_machines/motor_nameplates_slip_and_torque.md` + `design_framework/motor_systems/motor_selection_workflow.md` | Split: concept → training, selection logic → design_framework |
| `dc_motor_magnetism_stator_and_mechanical_structure.md` + `dc_motor_armature_winding_and_torque_production.md` + `dc_motor_commutator_brushes_and_power_path.md` | `training_modules/electrical_machines/dc_motor_basics.md` | Merge all three |
| Induction + nameplate files (verified NEC 430 + NFPA79 Ch12 anchors) | `standards_intelligence/crosswalks/overlap_notes/overlap__motors_drives.md` + `overlap_nfpa79_iec60204__motors_drives.md` | New crosswalk files |
| `ev_motor_types_overview.md` + `ev_motor_powertrain_configurations.md` | **HOLD — WIP** | Not promoted in Phase 11 |

### NEC Exam Prep

Requires segmentation before routing (Phase 11.0).

| Expected Segment | Destination |
|---|---|
| NEC code-reading method and structure | `training_modules/nec_application/nec_code_reading_fundamentals.md` |
| Motor circuits and branch protection (Art 430) | Addendum to existing `NEC_2023__Art430__motors_motor_circuits_and_controllers.md` |
| Panel and control circuit application (Art 409, 725) | Addenda to existing Art 409 + Art 725 files |
| Grounding and bonding application (Art 250) | Addendum to existing Art 250 file |
| Overcurrent and feeder application (Art 240, 215) | Addenda to existing Art 240 + Art 215 files |
| Practical job-site application notes | `training_modules/nec_application/motors_and_panel_code_application.md` |

Only field-application clarifications and common misreads go into existing NEC files.
Exam-prep reasoning and worked examples stay in `nec_application/` training modules.

---

## Content Rules

- Nothing promoted into `standards_intelligence/` unless compliance-verified against an actual standard.
- Promoted files are rewrites, not copies of transcript summaries.
- Each promoted file declares its source, promotion target, and any narrow standards cross-references.
- EV content stays in `work/design/` until the project deliberately expands scope.

---

## Build Order

| Phase | Work | Depends On |
|---|---|---|
| 11.0 | Segment `electrical exam prep.md` → `nec_exam_prep_topics/` folder | None |
| 11.1 | Scaffold `electrical_intelligence/` tree with `_index.yaml` + `README.md` | None |
| 11.2 | Promote circuit analysis files into `electrical_intelligence/` | 11.1 |
| 11.3 | Promote motor files + commissioning checklists | 11.1 |
| 11.4 | Create missing `overlap__motors_drives.md` crosswalk files | 11.3 |
| 11.5 | Promote NEC exam prep content + addenda to existing NEC files | 11.0 + 11.1 |

Phases 11.0 and 11.1 have no dependencies and can run in parallel.
Phases 11.2 and 11.3 can run in parallel after 11.1.
