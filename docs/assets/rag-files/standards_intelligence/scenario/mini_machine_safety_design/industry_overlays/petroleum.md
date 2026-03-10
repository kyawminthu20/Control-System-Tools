<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: petroleum
-->

# Petroleum Overlay

## What Changes vs Baseline

- Hazardous locations and process release consequences dominate far more often in petroleum service. NFPA 79 excludes equipment used in hazardous locations from its local baseline scope, so a separate hazardous-area review is mandatory. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1-applicability-rules]
- Chemical dosing and pressure-protection functions are more likely to fall under process-safety methodology than under pure machinery methodology. [LOCAL: _standards_map.md#applicability-matrix-by-project-type]
- Materials, seals, drains, vents, and containment shall be reviewed for hydrocarbon compatibility and environmental release control. Detailed petroleum standards are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: petroleum or hazardous-area standard]

## Standards To Prioritize

- NEC / NFPA 79 or IEC 60204-1 for non-hazloc machine electrical baseline [LOCAL: routing/standards_applicability.md#pump-skid-control]
- IEC 61511 / IEC 61508 for process safety functions [LOCAL: _standards_map.md#applicability-matrix-by-project-type]
- hazardous-location and petroleum-specific standards: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: NEC hazardous locations articles] [TO VERIFY: API / IEC 60079 / petroleum standard]

## Typical Inspection / Acceptance Artifacts

- area-classification review
- process shutdown matrix
- containment and drain-down procedure
- hazardous-energy isolation procedure
- management-of-change record for trip setpoints
