<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Mechanical and Electrical Isolation

## Mechanical Isolation Boundary

The local corpus strongly supports electrical isolation and stored electrical energy control, but it does not contain the detailed hydraulic or chemical isolation standards needed for a release-ready mechanical isolation design. Mechanical and fluid isolation requirements in this file are therefore engineering requirements tagged `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: ISO 4413] [TO VERIFY: application-specific chemical handling standard]

## Mechanical Shutoff Points

| Point ID | Isolation Point                                    | Purpose                                                                                     | Baseline Requirement                                                                                             | Source Status                                                                                       |
| -------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| MI-01    | Hydraulic reservoir suction isolation valve        | Allows pump service without draining the entire reservoir.                                  | The HPU should include a service isolation point upstream of the pump.                                           | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                        |
| MI-02    | Hydraulic pressure supply block valve              | Allows maintenance segmentation of the pressure side where permitted by relief-path design. | The design shall not allow pressure isolation without an independent relief or bleed path.                       | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                        |
| MI-03    | Hydraulic dump-to-tank valve                       | Removes motive pressure on safety demand or maintenance isolation.                          | The safety design shall define whether this valve is fail-open or otherwise drives the system to the safe state. | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                        |
| MI-04    | Accumulator block-and-bleed point                  | Enables trapped hydraulic energy discharge before maintenance.                              | Accumulator circuits shall provide visible pressure indication and a bleed-to-zero path.                         | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                        |
| MI-05    | Actuator local bleed point                         | Allows field verification that trapped pressure is zero.                                    | Each trapped actuator section should have a maintenance bleed provision where pressure can remain trapped.       | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]                                        |
| MI-06    | Chemical suction isolation valve at each source    | Prevents chemical feed during maintenance and source changeout.                             | Each chemical pump line shall provide positive suction isolation.                                                | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard] |
| MI-07    | Chemical discharge isolation valve and check valve | Prevents backflow and isolates injection point.                                             | The injection line should include positive isolation and backflow protection.                                    | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard] |
| MI-08    | Containment drain / sample point                   | Allows controlled drain-down of leak tray or process side.                                  | Draining and decontamination points shall be identified in maintenance procedures.                               | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard] |

## Electrical Isolation Points

| Point ID | Isolation Point                                | Requirement                                                                                                                  | Verification Method                | Citations                                                                                                                                                                                                  |
| -------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EI-01    | Main machine disconnect                        | The machine shall provide a main disconnect that is external, clearly marked, and lockable in `OFF`.                         | Inspection and functional test     | [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements] [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#3-lockout--tagout-loto-implications]               |
| EI-02    | Point-of-supply disconnect location            | The disconnect shall be at the machine point of supply and readily accessible.                                               | Layout review and field inspection | [LOCAL: us/nec/NEC_2023__Art670__industrial_machinery.md#1-machine-disconnecting-means]                                                                                                                    |
| EI-03    | Drive disconnect within sight where applicable | Drives requiring local service isolation shall have a disconnect within sight of the drive.                                  | Layout review and inspection       | [LOCAL: us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md#2-vfd-considerations-part-x]                                                                                                     |
| EI-04    | Control-power secondary protection             | Control transformers and DC supplies shall have primary/secondary protection and documented grounding philosophy.            | Schematic review                   | [LOCAL: us/nfpa79/NFPA79_2024__Ch15__transformers_and_power_supplies.md#1-control-power-architectures] [LOCAL: us/nfpa79/NFPA79_2024__Ch15__transformers_and_power_supplies.md#2-grounding-of-secondaries] |
| EI-05    | Panel-door energized-access control            | Doors to energized equipment shall require tool/key access or disconnect interlocking.                                       | Inspection and functional test     | [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#2-enclosure-implications] [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#4-control-panel-design-rules]             |
| EI-06    | STO / contactor isolation for drives           | Where drives are part of a safety function, STO or equivalent certified torque-removal means shall be provided and verified. | Functional test                    | [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations] [TO VERIFY: drive STO certification]                                                            |
| EI-07    | External source identification                 | Any incoming external source not removed by the local disconnect shall be clearly identified.                                | Drawing review and inspection      | [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination]                                                                                                                       |

## E-Stop Categories and Isolation

1. The design shall allocate each stop function to Stop Category 0, 1, or 2 based on the hazard and the required stopping behavior. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
2. Emergency stop shall use only Category 0 or Category 1; Category 2 shall not be used for an emergency stop function. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2-emergency-stop-concepts]
3. The selected stop category for hydraulic motion shall be justified in the risk assessment and safety-function register. Detailed motion-stopping calculations are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: ISO 4413]

## Stored Energy Discharge Requirements

### Electrical Stored Energy

1. Stored electrical energy shall discharge below 60 V within 5 seconds after isolation, or the enclosure shall carry a warning label stating the required wait time. [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause06__protection_against_electric_shock.md#1-protective-measures]
2. Residual-voltage warning labels shall be included in machine markings and documentation where discharge time exceeds immediate touch-safe conditions. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#1-labeling-requirements] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#1-identification-and-labels]

### Hydraulic and Chemical Stored Energy

1. Hydraulic circuits shall provide a documented depressurization method and a field-verifiable zero-pressure check before maintenance. NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]
2. Chemical lines shall provide a documented drain, flush, or double-block-and-bleed maintenance method appropriate to the chemical service. NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard]

## Isolation Verification Procedure

The maintenance isolation verification procedure shall include at least:

1. apply lockout to the main electrical disconnect [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#3-lockout--tagout-loto-implications]
2. verify that hazardous live parts are inaccessible or line-side terminals remain guarded and labeled [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#4-control-panel-design-rules]
3. wait the documented residual-voltage discharge time or measure touch-safe voltage [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests]
4. close mechanical isolation valves and open bleed or dump points until zero pressure is confirmed. Mechanical method details are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]
5. confirm chemical isolation and drain or flush status before opening lines. NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard]
