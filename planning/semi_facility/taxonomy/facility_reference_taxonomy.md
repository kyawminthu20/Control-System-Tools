<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_TAXONOMY
-->

# Facility Reference Taxonomy

## Purpose

Use this map to keep the semiconductor facility library organized by system boundary instead of by random file name.

## Primary domains

| Domain | Typical sub-systems | Typical outputs to capture |
| --- | --- | --- |
| Facility architecture | utility one-lines, campus utility map, tie-in boundaries, redundancy model | boundary notes, system map, utility dependency matrix |
| Bulk specialty gases | bulk pads, gas rooms, VMBs, gas cabinets, purge panels, valve manifolds | P&ID notes, interlock matrix, sequence notes, alarm philosophy |
| Bulk chemicals and wet process | tank farms, day tanks, transfer skids, blend or dose skids, wet benches | material compatibility notes, containment rules, transfer sequence notes |
| Water systems | city water, pretreatment, RO, EDI, UPW generation, reclaim, wastewater neutralization | process maps, analyzer list, control loops, water quality notes |
| Exhaust, abatement, and vacuum | general exhaust, acid exhaust, toxic exhaust, scrubbers, burn-wet, vacuum pumps | cause and effect, fan proof logic, emissions monitoring notes |
| HVAC and cleanroom | MAUs, AHUs, FFUs, chilled water, clean dry air, room pressure cascade | sequence of operations, room matrix, airflow and DP strategy |
| Electrical power and controls | substations, switchgear, UPS, generators, MCCs, PLCs, SCADA, BMS, EMS | one-lines, load lists, IO map, network architecture, alarm routing |
| Safety and EHS | EPO, fire alarm, gas detection, leak detection, spill control, emergency response | shutdown hierarchy, zoning, permissives, testing notes |
| Tool and facility interface | utility hookups, permit-to-run, exhaust prove, host or tool handshakes | interface control notes, handshake tables, responsibility split |
| Instrumentation library | sensors, analyzers, valves, regulators, MFCs, pumps, actuators | model notes, compatibility matrix, calibration notes, failure modes |
| Construction, commissioning, and O&M | FAT or SAT, startup, PM, calibration, proof tests, turnover | checklists, acceptance criteria, maintenance references |
| Standards and codes | SEMI, NFPA, NEC, UL, ISA, ISO, IEC, ASHRAE, local code | applicability map, gap list, local crosswalks |

## Required note types per topic

- `system overview`: what the system does, boundaries, utilities, normal operating intent
- `control philosophy`: permissives, interlocks, trips, shutdown behavior, sequencing
- `instrumentation`: what is measured, typical ranges, common devices, maintenance concerns
- `standards anchors`: the code or standards families that shape the design
- `source record`: where the information came from and how strong it is

## File discipline

- One topic per file.
- Prefer system names over vague titles.
- Separate rough captures from normalized notes.
- Link related manuals and source records instead of duplicating content.
- Mark inferred content clearly so it does not get mistaken for cited guidance.
