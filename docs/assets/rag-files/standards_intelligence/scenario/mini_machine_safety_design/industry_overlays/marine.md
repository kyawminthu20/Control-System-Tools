<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
INDUSTRY: marine
-->

# Marine Overlay

## What Changes vs Baseline

- Use the baseline electrical architecture only as a starting point; marine deployment usually adds vessel power-quality, motion, vibration, corrosion, and ingress concerns beyond the local machinery corpus. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]
- Washdown and corrosion-resistance requirements will typically be stronger than the baseline industrial environment assumptions. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#2-enclosure-implications]
- Marine standards, vessel integration requirements, and classification rules are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: marine electrical standard] [TO VERIFY: class society rules]

## Standards To Prioritize

- NFPA 79 or IEC 60204-1 baseline only for core machine electrical behavior [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#topic-based-overlap-matrix]
- marine and vessel-specific standards: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: IEC 60092 or equivalent marine standard]
- cybersecurity and remote-access controls if connected to vessel systems: `NOT FOUND IN LOCAL CORPUS – TO VERIFY` [TO VERIFY: IEC 62443]

## Typical Inspection / Acceptance Artifacts

- enclosure and corrosion-resistance review
- cable gland and ingress-protection review
- vessel power interface study
- motion/vibration mounting review
- FAT with marine environmental assumptions documented
