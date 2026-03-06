<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: petroleum
-->

# Petroleum Overlay

## What changes vs baseline

- Hazardous classified locations and hydrocarbon process consequences may invalidate the baseline non-classified machinery assumption. NFPA 79 local content explicitly excludes hazardous locations, so external hazardous-area standards are required. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1. Applicability Rules] [TO VERIFY: NEC hazardous location articles]
- Overfill, shutdown, and loss-of-containment functions may become process safety functions instead of ordinary machine interlocks. [LOCAL: routing/standards_applicability.md#Special Cases] [TO VERIFY: IEC 61511]
- Materials, seals, tubing, and drain or vent arrangements shall be reviewed for petroleum service; those criteria are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: petroleum standard]

## Standards to prioritize

- NEC classified-area articles and petroleum facility standards are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: NEC hazardous location articles] [TO VERIFY: petroleum standard]
- IEC 61511 and IEC 61508 shall be added if shutdowns are credited for process risk reduction. [LOCAL: _index.yaml#regional_routing] [TO VERIFY: IEC 61511] [TO VERIFY: IEC 61508]
- Keep NEC, NFPA 79, and IEC 60204-1 only for the machine electrical portions that remain in scope. [LOCAL: routing/standards_applicability.md#Special Cases] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Dual-Compliance Strategy]

## Typical inspection or acceptance artifacts

- Area classification drawing and equipment list. [TO VERIFY: NEC hazardous location articles]
- SIS or independent shutdown narrative with test intervals. [TO VERIFY: IEC 61511]
- Chemical or hydrocarbon compatibility record for wetted parts. [TO VERIFY: petroleum standard]
- Site-specific LOTO and isolation map including vent or drain points. [TO VERIFY: petroleum standard]
