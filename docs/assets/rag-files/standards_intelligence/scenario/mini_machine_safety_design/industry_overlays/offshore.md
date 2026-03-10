<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: offshore
-->

# Offshore Overlay

## What Changes vs Baseline

- Fixed offshore platforms are excluded from NFPA 79 scope in the local corpus, so the baseline package is not sufficient by itself for offshore deployment. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1-applicability-rules]
- Corrosion resistance, enclosure integrity, vibration, motion, cable management, and marine/offshore power-system interfaces will usually be more severe than the baseline environment assumptions. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]
- Offshore fire-and-gas integration, hazardous-area design, and marine classification requirements are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: offshore or marine classification standard]

## Standards To Prioritize

- baseline machine electrical requirements only as a starting point [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#topic-based-overlap-matrix]
- offshore, marine, and hazardous-area standards: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: offshore platform standard] [TO VERIFY: IEC 60079] [TO VERIFY: marine class rules]
- IEC 61511 if the skid contributes to a process shutdown function [LOCAL: _standards_map.md#applicability-matrix-by-project-type]

## Typical Inspection / Acceptance Artifacts

- corrosion and enclosure material review
- offshore hazardous-area assessment
- integrated shutdown and communications interface record
- cable and gland suitability review
- classification-society approval dossier
