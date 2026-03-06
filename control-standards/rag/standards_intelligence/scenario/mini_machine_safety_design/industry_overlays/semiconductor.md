<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: semiconductor
-->

# Semiconductor Overlay

## What Changes vs Baseline

- Retain the same machine-electrical baseline from NFPA 79/NEC or IEC 60204-1, but expect significantly tighter controls on chemical compatibility, cleanliness, tubing/piping materials, and exhaust or purge interfaces. Detailed semiconductor standards are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations] [TO VERIFY: SEMI standard]
- Treat chemical leak, overflow, and contamination-prevention functions as high-visibility design items and document them earlier than in the baseline package. Detailed semiconductor chemical requirements are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: SEMI standard] [TO VERIFY: application-specific chemical handling standard]
- If the skid interfaces with fab networks or recipe systems, add cybersecurity and audit controls beyond this baseline. `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: IEC 62443]

## Standards To Prioritize

- NFPA 79 or IEC 60204-1 for machine electrical baseline [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#topic-based-overlap-matrix]
- ISO 12100 plus ISO 13849-1 or IEC 62061 for machine safety functions if international/CE rules apply [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#safety-framework]
- semiconductor-specific standards and chemical compatibility requirements: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: SEMI standard]

## Typical Inspection / Acceptance Artifacts

- chemical compatibility matrix
- leak and overfill trip test record
- cleanliness and materials declaration
- interlock cause/effect matrix
- network and recipe interface change-control record
