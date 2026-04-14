<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_SYSTEM_MAP
-->

# Facility Systems Map

## Purpose

This is the top-level map for the semiconductor facility domains the library should cover.

## Major system families

| System family | Core sub-systems | Primary control focus | Typical reference outputs |
| --- | --- | --- | --- |
| Bulk specialty gas | bulk storage, gas rooms, VMBs, gas cabinets, purge panels | pressure regulation, purge logic, exhaust proof, leak or gas detection, emergency isolation | P&ID notes, cause and effect, valve sequence, alarm matrix |
| Bulk chemical distribution and wet process | bulk storage, day tanks, transfer skids, blend or dose skids, wet benches | containment, compatibility, transfer sequencing, leak detection, temperature and concentration control | material matrix, transfer sequence, interlock matrix |
| Water and wastewater | pretreatment, RO, EDI, UPW, reclaim, neutralization, wastewater segregation | flow, pressure, resistivity, TOC, pH, ORP, tank levels, redundancy | process map, analyzer list, control-loop notes |
| Exhaust, abatement, and vacuum | process exhaust, scrubbers, burn-wet, fan systems, vacuum pumps | flow proof, differential pressure, fan status, emissions support, shutdown dependencies | monitoring matrix, cause and effect, dependency map |
| HVAC and cleanroom | MAUs, AHUs, FFUs, chilled water, clean dry air, room cascade | temperature, humidity, airflow, differential pressure, particle control | room matrix, sequence of operations, sensor map |
| Electrical power and controls | utility feeds, substations, switchgear, UPS, MCCs, panels, PLCs, SCADA, BMS | power quality, redundancy, network segmentation, alarm routing, utility availability | one-lines, IO map, network notes, power dependency matrix |
| Safety and life safety | EPO, fire alarm, gas detection, leak detection, spill controls, emergency response | shutdown hierarchy, zoning, evacuation interfaces, safe state definition | cause and effect, proof-test notes, shutdown hierarchy |
| Tool and facility interface | permits, handshakes, utility prove, status signals, host links | permit-to-run logic, utility readiness, fault ownership, interface boundaries | interface control note, handshake table, boundary matrix |
| Instrumentation library | sensors, analyzers, MFCs, valves, regulators, pumps, actuators | selection by media, cleanliness, accuracy, diagnostics, maintenance burden | device summary notes, manual crosswalk, compatibility matrix |

## Cross-cutting design threads

- Material compatibility affects sensors, valves, tubing, seals, and maintenance frequency.
- Exhaust or ventilation proof is often a prerequisite for gas and chemical enable.
- Leak detection, gas detection, and spill containment must tie back to defined safe states.
- Instrument selection should capture process media, cleanliness class, wetted materials, range, accuracy, diagnostics, and calibration method.
- Alarm philosophy should separate permissives, interlocks, trips, and operator advisories.
- Tool utility handshakes should state who owns the final shutdown action: facility, packaged skid, or tool controller.

## Immediate expansion order

1. Bulk specialty gas
2. Bulk chemical distribution and wet process
3. Water and wastewater
4. Exhaust, abatement, and vacuum
5. HVAC and cleanroom
6. Electrical power and controls
7. Safety and tool interface
