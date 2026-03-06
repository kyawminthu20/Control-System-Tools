<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: energy
-->

# Energy Overlay

## What Changes vs Baseline

- If the skid performs utility, treatment, or process support in an energy facility, review whether chemical shutdowns and pressure trips are now process-safety functions rather than purely machine safety functions. [LOCAL: _standards_map.md#applicability-matrix-by-project-type]
- Integrated systems with multiple skids or packaged units require stronger coordination of external power sources, trip propagation, and unified SCCR assumptions. [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination] [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#2-final-compliance-alignment]
- Site cybersecurity, remote operations, historian integration, and alarm-management requirements are typically stronger than the baseline and are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: IEC 62443] [TO VERIFY: ISA-18.2]

## Standards To Prioritize

- NFPA 79, NEC Articles 670/409/430, or IEC 60204-1 for the machine electrical baseline [LOCAL: routing/standards_applicability.md#pump-skid-control] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#topic-based-overlap-matrix]
- IEC 61511 / IEC 61508 where shutdowns become process safety functions [LOCAL: _standards_map.md#applicability-matrix-by-project-type]
- cybersecurity and alarm-management standards: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] [TO VERIFY: ISA-18.2]

## Typical Inspection / Acceptance Artifacts

- process cause/effect matrix
- shutdown narrative or SRS placeholder
- integrated FAT/SAT with trip propagation tests
- AFC / SCCR coordination record
- network zoning and remote-access review
