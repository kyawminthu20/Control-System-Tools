<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

WIZARD_ID: US_EU_MACHINE_COMPLIANCE
INPUTS: project_profile.yaml
OUTPUTS: us_eu_delta_report.md
-->

# US EU Machine Compliance Wizard

## 0. Purpose

Given a machine profile, this wizard helps determine:

- what standards lead in a US-only, EU-only, or dual-market project
- what design changes are required by market
- what evidence and verification deltas must be captured

It is intended to sit on top of:

- NFPA 79
- IEC 60204-1
- supporting overlap notes and standards files

## 1. Minimum inputs

- market target: `US_ONLY`, `EU_ONLY`, or `BOTH`
- machine type
- supply characteristics
- environment and hazardous-area status
- control-system summary
- documentation maturity

## 2. Decision logic

For each topic:

1. load the applicable overlap note
2. determine the owner standard for the target market
3. produce required changes
4. produce evidence requirements
5. produce verification and commissioning deltas

## 3. Topics covered

- scope boundary
- definitions
- general requirements
- incoming supply disconnect
- electric shock protection
- equipment protection
- grounding and bonding
- control functions
- operator interface
- control equipment
- motors and drives
- accessories and lighting
- marking and documentation
- verification

## 4. Output rules

The wizard output should:

- avoid quoting standards text
- identify the controlling standard by topic
- list design deltas, evidence, and checklist items
- point back to the authoritative standards files and overlap notes

## 5. Current implementation note

This file seeds the design-framework layer. Full automation value depends on completing the missing `overlap_nfpa79_iec60204__*` note set under `standards_intelligence/crosswalks/overlap_notes/`.

## 6. Related files

- [us_eu_wizard_rules.yaml](./us_eu_wizard_rules.yaml)
- [us_eu_delta_report_template.md](./us_eu_delta_report_template.md)
- [standards_decision_workflow.md](../../standards_intelligence/crosswalks/overlap_matrix/standards_decision_workflow.md)

## 7. Change log

- 2026-03-09 — Initial wizard spec created to seed the design-framework module.
