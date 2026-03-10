# Standards Applicability

**AI_READ_ACCESS: ALLOWED**
**CONTENT_CLASS: RAG_APPROVED**
**Status:** Authoritative Reference

## Purpose

This document is the quick-routing layer for choosing the correct standards path by project type, market, and technical topic. Use it with `_standards_map.md` when a project needs a faster answer than a full clause-by-clause standards review. [LOCAL: _standards_map.md#Purpose]

## Project Type → Applicable Standards/Topics

### Conveyor Control System

**Primary Standards**: NEC Articles 430 and 670; NFPA 79 Chapters 4, 5, 7, 8, and 9

**Topics**: motor control, emergency stop, disconnecting means, grounding, control circuits, installation environment

### Pump Skid Control

**Primary Standards**: NEC Articles 430 and 670; NFPA 79 Chapters 4, 5, 8, and 9; IEC 60204-1 for international machinery use

**Topics**: motor protection, control circuits, environmental conditions, grounding, shutdown behavior, skid-machine boundaries

### CNC Machine

**Primary Standards**: NFPA 79, IEC 60204-1, NEC Articles 430 and 670, ISO 13849-1 or IEC 62061

**Topics**: spindle and axis stopping, enclosure door interlocks, drive STO, tool-change interlocks, restart prevention, controller safety partitioning

**See Also**: `reference_models/software_safety_and_intrinsic_safety_standards.md`

**Machine-tool-specific standard**: `TO VERIFY: ISO 16090-1`

### Safety PLC / SIS Software

**Primary Standards**: IEC 61508-3, IEC 61511, IEC 62061, ISO 13849-1/-2, IEC 61131-3, IEC 62443-4-1

**Topics**: safety software lifecycle, application programming, validation, change control, software partitioning, secure development

**See Also**: `reference_models/software_safety_and_intrinsic_safety_standards.md`

### Intrinsically Safe / Hazardous-Area I/O

**Primary Standards**: IEC 60079-11, IEC 60079-14, IEC 60079-25, UL 60079-11, UL 698A

**Topics**: associated apparatus, barriers or isolators, control drawings, cable parameters, installation segregation

**See Also**: `reference_models/software_safety_and_intrinsic_safety_standards.md`

### Robotic Cell Control

**Primary Standards**: NFPA 79 Chapters 8 and 9; ISO 10218; UL 508A if the panel follows a listing path

**Topics**: safety circuits, safeguarding, risk assessment, emergency stop, protective bonding

### UL-Listed Control Panel

**Primary Standards**: UL 508A, NEC Article 409, NEC Article 430, NEC Article 670, and NFPA 79 where the panel is part of industrial machinery

**Topics**: SCCR, wire sizing, spacing and clearance, marking, short-circuit protection

### General Industrial Machinery

**Primary Standards**: NFPA 79, NEC Article 670, IEC 60204-1, ISO 12100, ISO 13849-1, or IEC 62061 depending on market and safety method

**Topics**: machinery scope, operator interaction, disconnecting means, grounding, motion safety, documentation, market-specific compliance path

## Applicability Matrix by Project Type

| Project Type | Primary US Path | Primary International Path | Safety Method |
| --- | --- | --- | --- |
| Standalone industrial control panel | NEC Article 409 plus UL 508A where listing is needed | IEC 60204-1 Clause 11 where used as machine electrical equipment | None unless the panel contains credited safety functions |
| General industrial machinery | NFPA 79 plus NEC Article 670 | IEC 60204-1 plus ISO 12100 | ISO 13849-1 or IEC 62061 for machinery safety functions |
| Pump or dosing skid machine | NFPA 79 plus NEC Articles 430 and 670 | IEC 60204-1 | Machinery path by default; move to IEC 61511 if shutdown functions become process protection layers |
| CNC machine tool | NFPA 79 plus NEC Articles 430 and 670 | IEC 60204-1 plus machine-tool-specific standards | ISO 13849-1 or IEC 62061, with type-C machine-tool detail `TO VERIFY` |
| Process-industry protection function | NEC or NFPA 79 only for electrical implementation in scope | IEC 60204-1 only for the machine-electrical layer in scope | IEC 61511 on top of IEC 61508 |

## Market-Based Selection

### US Market Only

Use NEC as the installation code baseline, NFPA 79 for industrial machinery, and UL 508A when the control panel follows a listing path. This is the default route for US machinery and control-panel projects. [LOCAL: _standards_map.md#US Market Only] [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#2-boundaries-with-other-standards]

### EU or International Machinery

Use IEC 60204-1 for machine electrical requirements, ISO 12100 for risk assessment, and ISO 13849-1 or IEC 62061 for safety-related control functions. [LOCAL: _standards_map.md#EU/CE Marking Path] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Safety Framework]

### Dual US and International

Use NFPA 79 plus IEC 60204-1, then add the applicable machinery safety method and any listing path needed for the US panel scope. This is the route for global machinery intended for both US and international markets. [LOCAL: _standards_map.md#Dual-Compliance Strategy] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Dual-Compliance Strategy]

## Special Cases

- If a protective function is credited as a process safety layer that prevents loss of containment, overfill, overdosing, or other process hazards, route that function to IEC 61511 rather than keeping it only in a machinery-safety workflow. [LOCAL: _standards_map.md#Process Industry] [LOCAL: _index.yaml#regional_routing]
- If the assembly is no longer industrial machinery and is instead treated as standalone building-service or utility equipment, confirm whether NFPA 79 still applies before using the machinery path. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1-applicability-rules]
- If intrinsically safe or hazardous-area loops are added, route the project into the intrinsic-safety standards family instead of treating those circuits as ordinary control wiring. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Intrinsic Safety And Hazardous-Area IO]

## Maintenance Notes

- Use `_standards_map.md` for the more detailed decision matrix and cross-standard notes.
- Use `reference_models/software_safety_and_intrinsic_safety_standards.md` when the question shifts into safety software, redundancy, cybersecurity, or intrinsic safety.

---

*Last Updated: 2026-03-05*
*Changelog: Moved into `routing/` and expanded to align with current scenario citations and market-routing sections.*
