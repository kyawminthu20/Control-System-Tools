<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Verification and Validation Plan

## Verification Philosophy

The machine electrical system shall be verified by inspection, test, and documented records before handover, and the installed system shall be rechecked at site because grounding, fault current, and installation conditions depend on the actual facility. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#0-purpose] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#2-commissioning-alignment] [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#1-installation--listing-requirements-field-rules]

## FAT / SAT Outline

### Factory Acceptance Test (FAT)

The FAT shall cover:

- schematic-to-build verification [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#0-purpose]
- protective bonding continuity [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests]
- insulation and dielectric checks as applicable [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests]
- E-stop, guard, and restart tests [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts]
- disconnect, labeling, and line-side guarding checks [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#4-control-panel-design-rules] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#1-labeling-requirements]
- SCCR and nameplate record review [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr] [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#3-labeling-requirements]
- hydraulic and chemical functional trip tests defined by the project. Detailed normative test method is NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413] [TO VERIFY: application-specific chemical handling standard]

### Site Acceptance Test (SAT)

The SAT shall cover:

- supply verification and disconnect accessibility [LOCAL: us/nec/NEC_2023__Art670__industrial_machinery.md#1-machine-disconnecting-means]
- working-space and installation conformance [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#1-installation--listing-requirements-field-rules]
- site grounding and bonding verification [LOCAL: us/nec/NEC_2023__Art250__grounding_and_bonding.md#0-purpose-for-control-panels]
- available fault current check against machine SCCR [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr]
- integrated line behavior, including external-source identification and trip propagation where multiple panels or machines are linked [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination]
- process-side hydraulic and chemical acceptance checks per site-specific procedures. NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413] [TO VERIFY: IEC 61511]

## Safety Validation Test List

| Test ID | Test                                   | Acceptance Criteria                                                                                                                       | Source                                                                                                                                                                                                                   |
| ------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| VVT-01  | Main disconnect test                   | Main disconnect isolates machine supply, is lockable in `OFF`, and is clearly indicated.                                                  | [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements]                                                                                                                              |
| VVT-02  | E-stop function test                   | Each E-stop overrides all modes, achieves the defined stop, and reset does not restart the machine.                                       | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts]                                                                                                                |
| VVT-03  | Guard interlock test                   | Opening a guard initiates the defined safe-state behavior and inhibits restart until guard closure and reset/start sequence are complete. | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]                                                                                                                     |
| VVT-04  | Unexpected restart test                | Restoration of power does not automatically restart hydraulic or chemical drives.                                                         | [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior]                                                                                           |
| VVT-05  | Protective bonding continuity test     | Protective bonding path demonstrates acceptable continuity.                                                                               | [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests]                                                                                                                 |
| VVT-06  | Residual voltage test                  | Stored electrical energy falls below 60 V within required time or the machine is correctly labeled with wait time.                        | [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures]                                                                                                                         |
| VVT-07  | SCCR documentation review              | Nameplate SCCR and calculation record match installation AFC assumptions.                                                                 | [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr]                                                                                                                       |
| VVT-08  | Hydraulic pressure-relief / trip test  | Pressure trip or relief behavior transitions the hydraulic subsystem to its defined safe state.                                           | [TO VERIFY: ISO 4413]                                                                                                                                                                                                    |
| VVT-09  | Chemical high-high level shutdown test | Simulated high-high level stops dosing and requires deliberate recovery steps.                                                            | [TO VERIFY: IEC 61511] [TO VERIFY: application-specific chemical handling standard]                                                                                                                                      |
| VVT-10  | Leak detection shutdown test           | Leak detection stops dosing and raises alarm.                                                                                             | [TO VERIFY: application-specific chemical handling standard]                                                                                                                                                             |
| VVT-11  | Logger / event integrity check         | Required events are recorded with usable timestamps and clear operator context.                                                           | [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]                                                                                                                                                                        |
| VVT-12  | Documentation package review           | Drawings, I/O list, labels, maintenance instructions, and safety-function test records are complete.                                      | [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set] |

## Documentation Deliverables Checklist

The release package shall include at least:

- general arrangement and block diagram [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set]
- electrical schematics [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
- panel layout and bill of materials [LOCAL: us/nfpa79/NFPA79_2024__Ch11__control_equipment.md#1-panel-construction-implications]
- I/O list and signal list
- cause/effect or trip matrix
- safety functions register
- SCCR calculation record and nameplate schedule [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2-short-circuit-current-rating-sccr]
- grounding and bonding details [LOCAL: us/nec/NEC_2023__Art250__grounding_and_bonding.md#2-bonding-of-enclosures-and-doors]
- conductor schedule / wire numbering [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#1-identification-and-labels]
- lockout and isolation point register
- maintenance and test instructions with intervals [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set]
- FAT report
- SAT report

## Periodic Revalidation

The machine shall be revalidated after:

- control software changes affecting safety or sequencing
- replacement of safety devices or final elements
- field modifications to disconnects, grounding, or power architecture
- integration into a larger line with external sources or propagated safety trips [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#2-final-compliance-alignment] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests]
