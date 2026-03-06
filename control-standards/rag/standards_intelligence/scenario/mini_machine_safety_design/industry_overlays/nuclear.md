<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: nuclear
-->

# Nuclear Overlay

## What Changes vs Baseline

- The baseline package is not sufficient for nuclear deployment by itself. Nuclear QA, software change control, qualification, cybersecurity, and records management are substantially more rigorous and are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: nuclear quality and safety standard]
- Chemical containment, failure documentation, and maintenance traceability should be elevated from baseline good practice to controlled configuration records. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
- If the skid contributes to plant protection or safety-class functions, process or plant safety rules will supersede the baseline machinery assumptions. [LOCAL: _standards_map.md#special-cases] [TO VERIFY: nuclear safety standard]

## Standards To Prioritize

- baseline machine electrical and documentation requirements as a minimum [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set]
- nuclear QA, software, and cybersecurity standards: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: nuclear QA standard] [TO VERIFY: IEC 62443]
- IEC 61511/61508 only if used as part of a non-nuclear process-safety function, subject to plant rules [LOCAL: _standards_map.md#applicability-matrix-by-project-type]

## Typical Inspection / Acceptance Artifacts

- configuration-controlled design package
- software revision and validation record
- material traceability package
- failure mode / trip response record
- independent verification record
