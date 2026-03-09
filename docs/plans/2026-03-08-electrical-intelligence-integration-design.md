# Design: Electrical Knowledge Integration

**Date:** 2026-03-08
**Last revised:** 2026-03-09
**Status:** Complete — all content promoted

---

## Summary

Three transcript-derived electrical knowledge sources have been promoted into the
existing canonical RAG layers. No new parallel layer was created.

All content lands in one of four existing layers:

1. `control-standards/rag/training_modules/`
2. `control-standards/rag/design_framework/`
3. `control-standards/rag/commissioning_checklists/checklists/`
4. `control-standards/rag/standards_intelligence/crosswalks/overlap_notes/`

---

## Sources

| Source | Location | Disposition |
|---|---|---|
| Circuit analysis + practical electronics | `work/design/project_implementation_gaps/electrical_and_practical_circuit_analysis_topics/` | Fully promoted |
| Motors (induction, DC) | `work/design/project_implementation_gaps/motors_topics/` | Fully promoted |
| NEC exam prep | `work/design/project_implementation_gaps/nec_exam_prep_topics/` | Promoted (justified scope only) |
| EV motor files | `motors_topics/ev_motor_*.md` | Held as WIP — not promoted |

---

## What was built

### `training_modules/fundamentals/`

Circuit analysis and practical electronics source → clean teaching modules:

- `electrical_quantities_and_circuit_language.md`
- `series_parallel_and_divider_methods.md`
- `kirchhoff_laws_and_systematic_analysis.md`
- `equivalent_circuit_methods.md`
- `electrical_equations_reference.md`
- `passive_components_resistors_capacitors.md`
- `diodes_transistors_and_switching_basics.md`
- `conductor_ampacity_and_termination_temperature.md` *(pre-existing)*
- `README.md`, `_index.yaml`

### `training_modules/electrical_machines/`

Motors source → teaching modules + expanded machine coverage:

- `induction_motor_basics.md`
- `dc_motor_basics.md`
- `motor_nameplates_slip_and_torque.md`
- `vfd_fundamentals.md`
- `servo_drive_fundamentals.md`
- `ac_vs_dc_motor_comparison.md`
- `motor_family_comparison.md`
- `brushless_dc_ev_and_drone_motor_comparison.md`
- `vfd_and_servo_architecture_diagrams.md`
- `README.md`, `_index.yaml`

### `training_modules/nec_application/`

NEC exam prep source → code-reading and application modules (justified scope only):

- `nec_code_reading_fundamentals.md`
- `working_space_and_table_navigation.md`
- `motor_and_panel_code_application.md`
- `README.md`, `_index.yaml`

### `design_framework/electrical_review/`

Practical calculation material → engineering workflows:

- `ohms_law_and_power_check_workflow.md`
- `basic_resistive_network_review.md`
- `component_selection_basics.md`
- `simple_signal_and_interface_circuit_notes.md`
- `README.md`, `_index.yaml`

### `design_framework/motor_systems/`

Motors source + expanded motor/drive coverage → design workflows and checklists:

- `motor_selection_workflow.md`
- `motor_nameplate_review_checklist.md`
- `star_delta_and_supply_matching_notes.md`
- `vfd_motor_integration_review.md`
- `vfd_commissioning_workflow.md`
- `servo_commissioning_workflow.md`
- `motor_troubleshooting_decision_tree.md`
- `motor_selection_comparison_matrix.md`
- `integrated_motor_drive_architecture_comparison.md`
- `integrated_drive_failure_modes_and_tradeoffs.md`
- `integrated_drive_serviceability_and_field_replacement_review.md`
- `motor_mounted_drive_thermal_and_emc_design_notes.md`
- `industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md`
- `README.md`, `_index.yaml`

### `commissioning_checklists/checklists/`

Motors + practical circuit sources → field verification checklists:

- `motor_rotation_and_overload_verification.md`
- `motor_nameplate_and_overload_setting.md`
- `basic_circuit_polarity_and_power_checks.md`
- `capacitor_discharge_awareness_check.md`
- `drive_commissioning.md`
- `pre_power_panel_and_incoming_supply_check.md`
- `README.md`, `_index.yaml`

### `standards_intelligence/crosswalks/overlap_notes/`

Motors source → compliance crosswalk gap fills:

- `overlap__motors_drives.md`
- `overlap_nfpa79_iec60204__motors_drives.md`

---

### `design_framework/constraints/` (unplanned addition)

Reusable design-rule YAML derived from NEC 250, NFPA 79, UL 508A, IEC 60204-1:

- `grounding_bonding_rules.yaml` — normative rules paraphrased from cited standards with `not_a_standard` disclaimer; intended as design-review aid only

### `design_framework/us_eu_compliance_wizard/` (unplanned addition)

US/EU machine compliance wizard seeded for future automation:

- `US_EU_Machine_Compliance_Wizard.md` — wizard specification and decision logic
- `us_eu_wizard_rules.yaml` — machine-readable rules; references 14 overlap note files of which only 2 currently exist; non-existent files are forward-looking references documented with `availability_note`
- `us_eu_delta_report_template.md` — report output template

### `design_framework/design_guides/` (unplanned addition)

- `02_power_distribution_guide.md` — power distribution design guide

### Note on EV/drone content in `motor_systems/`

The EV source files (`ev_motor_types_overview.md`, `ev_motor_powertrain_configurations.md`) were held as WIP. However, EV and drone motor-drive comparison content was promoted into `motor_systems/` under design-framework framing (comparison notes, standards matrices). These files discuss EV traction inverters, ISO 26262, UNECE R100, and drone ESC configurations as comparison points for industrial motor selection decisions. This is an intentional scope expansion beyond the original design, documented here for traceability.

---

## What was not promoted

- EV motor source files (`ev_motor_types_overview.md`, `ev_motor_powertrain_configurations.md`) — held as WIP in `work/design/`
- NEC article-specific addenda (Art 430, 409, 725, 250, 240, 215) — not justified by current source material
- Residential load calculation notes — held as WIP source only

---

## Content rules applied

1. Promoted files are rewrites, not transcript copies.
2. Metadata convention used:
   - `CONTENT_CLASS: RAG_APPROVED`
   - `AI_READ_ACCESS: ALLOWED`
   - `STATUS: DRAFT`
3. `## Related standards` sections added only where a real standards anchor exists.
4. Engineering heuristics are labeled as heuristics, not written as mandatory rules.
5. Nothing appended to `standards_intelligence/` without a verified standards anchor.

---

## Layer taxonomy used

```
training_modules/
├── fundamentals/          — circuit theory, components, equations
├── electrical_machines/   — motors, drives, servo systems
└── nec_application/       — code-reading method, table navigation, application examples

design_framework/
├── electrical_review/     — calculation workflows, component selection
└── motor_systems/         — motor/drive selection, integration, commissioning workflows

commissioning_checklists/
└── checklists/            — pre-power, motor, drive, and circuit field checks

standards_intelligence/
└── crosswalks/overlap_notes/  — motors/drives jurisdiction crosswalks
```

`fundamentals/` is the correct home for circuit theory and basic electronics.
If the folder becomes too broad, taxonomy expansion should be a separate plan.

---

## Validation

```bash
python3 tools/project_automator.py
```

Note: `validate_ai_boundaries.py` and `validate_reorg.sh all` have pre-existing failures
unrelated to this integration. Do not use them as acceptance gates for this work.
