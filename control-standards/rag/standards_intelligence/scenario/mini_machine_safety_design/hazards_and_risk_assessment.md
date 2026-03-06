<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Hazards and Risk Assessment

## Hazard Inventory

| Hazard ID | Hazard                                      | Typical Initiating Events                                              | Consequences                                            | Baseline Source Status                                                                                                                                                                                                              |
| --------- | ------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HZ-01     | Hydraulic pressure injection / line rupture | Hose failure, overpressure, trapped pressure during maintenance        | Injection injury, fluid release, environmental spill    | Detailed normative source NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                                                                                                                              |
| HZ-02     | Hydraulic stored energy                     | Accumulator charge, trapped cylinder pressure, closed block valves     | Unexpected movement during maintenance, violent release | Detailed normative source NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                                                                                                                              |
| HZ-03     | Chemical exposure                           | Pump seal failure, hose leak, fitting failure, wrong connection        | Exposure, corrosion, inhalation, contamination          | Detailed normative source NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard]                                                                                                       |
| HZ-04     | Chemical spill / overfill                   | Tank high level missed, valve failure, programming error               | Release to environment, slip hazard, product loss       | Process-specific source NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: IEC 61511] [TO VERIFY: application-specific chemical handling standard]                                                                                  |
| HZ-05     | Pinch / crush from actuator motion          | Guard open, unexpected restart, motion command while personnel exposed | Serious injury                                          | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]                                    |
| HZ-06     | Electrical shock                            | Contact with live parts, failed insulation, poor bonding               | Shock, burn, fatal injury                               | [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: us/nec/NEC_2023__Art250__grounding_and_bonding.md#0-purpose-for-control-panels]                                            |
| HZ-07     | Arc / short-circuit incident                | Insufficient SCCR, insufficient interrupting rating, energized access  | Burn, equipment destruction, fire                       | [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr] [LOCAL: us/nec/NEC_2023__Art240__overcurrent_protection.md#2-coordination-with-sccr-short-circuit-current-rating]                |
| HZ-08     | Unexpected startup                          | Power restoration, reset causing restart, PLC fault                    | Motion while personnel exposed                          | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior] |
| HZ-09     | Residual electrical energy                  | VFD capacitor discharge delay, multiple power sources                  | Shock during servicing                                  | [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#1-labeling-requirements]                                         |
| HZ-10     | Thermal / overheating                       | Undersized conductors, poor ventilation, overloaded transformers       | Fire, nuisance trip, reduced component life             | [LOCAL: us/nec/NEC_2023__Art310__conductors_for_general_wiring.md#1-ampacity-and-derating] [LOCAL: us/nfpa79/NFPA79_2024__Ch11__control_equipment.md#1-panel-construction-implications]                                             |

## Risk Reduction Hierarchy

The project shall apply risk reduction in this order:

1. inherently safe design measures
2. safeguarding and protective measures
3. information for use, warnings, and procedures

This hierarchy is a standard machinery-safety principle, but the detailed ISO 12100 source text is NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 12100]

## Baseline Risk Reduction Rules

1. Electrical hazards shall first be reduced by enclosure/barrier design, bonding, overcurrent protection, and disconnecting means. [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements] [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: us/nec/NEC_2023__Art240__overcurrent_protection.md#1-overcurrent-device-selection]
2. Hazardous motion hazards shall be reduced by guards, interlocks, safety-rated stop logic, and prevention of automatic restart. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]
3. Hydraulic and chemical hazards shall be reduced by engineered isolation, pressure relief, containment, leak detection, and maintenance depressurization procedures, but detailed normative requirements are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413] [TO VERIFY: application-specific chemical handling standard]

## Risk Control Mapping

| Hazard                       | Safeguard                                                                                                                | Related Standard(s)                                                                                                                                                                                                                                                                            | Verification Method                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Hydraulic pressure injection | Relief path, guarded hose routing, block-and-bleed maintenance isolation, dump valve to tank.                            | [TO VERIFY: ISO 4413]                                                                                                                                                                                                                                                                          | Hydraulic pressure test, isolation walkdown, maintenance procedure review. |
| Hydraulic stored energy      | Depressurization points, pressure indication, lockable isolation valves, safety-trip dump valve.                         | [TO VERIFY: ISO 4413]                                                                                                                                                                                                                                                                          | Functional test of dump valve, zero-pressure verification, LOTO test.      |
| Chemical exposure / spill    | Secondary containment, leak detection, high-high level trip, closed transfer connections, material-compatibility review. | [TO VERIFY: application-specific chemical handling standard] [TO VERIFY: IEC 61511]                                                                                                                                                                                                            | Spill-drill review, leak simulation, level-trip test, materials review.    |
| Pinch / crush                | Fixed guards, guard switches, emergency stop, safe stop category allocation, restart inhibit.                            | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]                                                                                          | Functional safety test, guard-open test, restart test.                     |
| Electrical shock             | IP2X or equivalent barriers, disconnect, protective bonding, line-side guarding, residual-voltage discharge.             | [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: us/nec/NEC_2023__Art250__grounding_and_bonding.md#2-bonding-of-enclosures-and-doors]                                                                                                  | Visual inspection, continuity test, residual-voltage test.                 |
| Arc / short-circuit incident | SCCR determination, OCP interrupting rating review, working space, warning labeling.                                     | [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr] [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#1-installation--listing-requirements-field-rules]                                                             | Calculation review, label inspection, site AFC comparison.                 |
| Unexpected startup           | No automatic restart on power restoration, safety reset separate from start, de-energize-to-stop.                        | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0-control-philosophy] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior]                                                            | Power-cycle test, reset/start sequence test.                               |
| Thermal / overheating        | Conductor sizing, OCP sizing, transformer inrush sizing, panel heat dissipation.                                         | [LOCAL: us/nec/NEC_2023__Art310__conductors_for_general_wiring.md#1-ampacity-and-derating] [LOCAL: us/nfpa79/NFPA79_2024__Ch11__control_equipment.md#1-panel-construction-implications] [LOCAL: us/nfpa79/NFPA79_2024__Ch15__transformers_and_power_supplies.md#1-control-power-architectures] | Calculation review, thermal inspection, commissioning load test.           |

## Risk Assessment Template

Use the following minimum fields for each hazard review entry:

| Field                   | Description                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------- |
| Hazard ID               | Unique identifier such as `HZ-05`.                                                     |
| Task / Mode             | Operation, cleaning, maintenance, setup, jam clearing, or commissioning task.          |
| Hazard Source           | Hydraulic pressure, motion, live electrical parts, chemical inventory, thermal source. |
| Initiating Event        | What causes the hazardous situation.                                                   |
| Persons Exposed         | Operator, maintenance, commissioning, cleaning, contractor.                            |
| Consequence             | Injury, exposure, release, equipment damage, downtime.                                 |
| Existing Safeguards     | Current hardware, software, procedure, label.                                          |
| Initial Risk Estimate   | NOT FOUND IN LOCAL CORPUS – TO VERIFY method. [TO VERIFY: ISO 12100]                   |
| Required Risk Reduction | Additional design or procedural measure.                                               |
| Safety Function ID      | Link to a safety function if applicable.                                               |
| Verification Method     | Inspection, test, calculation, FAT, SAT, document review.                              |
| Source Reference        | One or more `[LOCAL: ...]` or `[TO VERIFY: ...]` tags.                                 |

## Minimum Assessment Deliverables

The project risk package shall include:

- hazard register
- safety functions register
- cause/effect or trip matrix
- isolation point register
- verification results
- operating and maintenance instructions with testing intervals [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
