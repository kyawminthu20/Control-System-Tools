<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DESIGN_INTEGRATION_PLAN
-->

# NEC Exam Prep Topics Integration Plan

## Purpose

This note explains how the current `nec_exam_prep_topics` package should feed the project without pretending that a mixed exam-prep transcript is a standards commentary set.

## Current assessment

This source is useful, but narrower than the older electrical-intelligence plan assumed.

The strongest material is:

- NEC code-book navigation and lookup method
- disciplined table-reading
- working-space example reasoning
- basic exam-prep calculation refreshers

The weakest fit for the project is:

- residential dwelling load-calculation teaching material

That section may still be useful later, but it is not central to the control-panel and industrial machinery focus of the repo.

## Promotion targets

### High confidence

- `nec_code_reading_and_index_method.md`
  - promotion target: `rag/training_modules/nec_application/nec_code_reading_fundamentals.md`
  - confidence: `TRAINING_ONLY`

- `nec_table_reading_and_working_space_example.md`
  - promotion target: `rag/training_modules/nec_application/working_space_and_table_navigation.md`
  - confidence: `TRAINING_ONLY`

- `electrical_exam_math_ohms_law_and_power.md`
  - promotion target: `rag/design_framework/electrical_review/ohms_law_and_power_check_workflow.md`
  - secondary target: future fundamentals training refresh
  - confidence: `DESIGN_FRAMEWORK_INPUT`

### Medium confidence

- `nec_code_reading_and_index_method.md`
  - secondary promotion target: add small workflow note to `NEC_OVERVIEW.md`
  - confidence: `STANDARDS_ADDENDUM`

- `nec_table_reading_and_working_space_example.md`
  - secondary promotion target: small training-side link to `NEC_2023__Art110__requirements_for_electrical_installations.md`
  - confidence: `TRAINING_WITH_STANDARDS_LINK`

### Hold / low priority

- `residential_load_calculation_notes.md`
  - promotion target: none for now
  - confidence: `HOLD_WIP`

## Recommended project use

Use this source package to build:

- one NEC code-reading training module
- one table-navigation and working-space training module
- one design-review note for fast Ohm's law and power checks

Do not force this source into motor, grounding, or panel-specific NEC application notes unless there is actual source support or independent standards verification.
