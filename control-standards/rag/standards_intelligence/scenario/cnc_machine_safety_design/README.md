<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# CNC Machine Safety Design Scenario

## Scenario Summary

This package defines a compact enclosed CNC machining-center concept that combines:

- one CNC controller for program execution, axis coordination, spindle control, and HMI functions
- one spindle drive and motor
- three servo axes (`X`, `Y`, and `Z`) with optional brake on the vertical axis
- one automatic tool changer and tool magazine
- one enclosed operator access zone with interlocked front door
- one main control panel with drives, PLC or CNC logic, safety logic, HMI, and local event logging
- optional coolant, lubrication, chip handling, and pneumatic or hydraulic workholding support

The baseline concept is intended for indoor industrial metal-cutting machinery at 1000 V AC or less. It is treated as machinery rather than building-service equipment. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#0-scope-and-intent] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause01__scope.md#1-in-scope-machinery]

The baseline package assumes:

- an enclosed CNC machine with powered spindle and servo axes
- operator loading and unloading through an interlocked access door
- safety-related stopping handled by safety-rated logic and drive-safe interfaces rather than by ordinary CNC or HMI commands alone [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]
- machine electrical compliance driven by NFPA 79 and NEC for US use, or IEC 60204-1 plus machine-safety standards for international use [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#2-boundaries-with-other-standards] [LOCAL: _standards_map.md#Market-Based Selection]

The baseline package does not close machine-tool-specific type-C requirements, detailed stop-time-based guard unlocking, or formal PL or SIL target calculations because those methods are not populated in the local corpus. These remain `TO VERIFY`. [TO VERIFY: ISO 16090-1] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061]

## Intended Machine Functions

The concept machine performs these functions:

1. Accept power and initialize the CNC controller, axis drives, spindle drive, and safety logic.
2. Home the machine axes and verify required interlocks and permissives before cycle start.
3. Start the spindle and execute a part program using coordinated `X`, `Y`, and `Z` motion.
4. Perform tool changes using an automatic tool magazine or tool changer when safe conditions are met.
5. Deliver operator status, cycle controls, alarms, and diagnostics through a local HMI.
6. Record selected events such as E-stop demands, guard trips, resets, mode changes, and cycle commands in a non-safety logger. Detailed audit-trail rigor remains `TO VERIFY`. [TO VERIFY: IEC 62443] [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]

## Primary Hazards Addressed

This package addresses these hazards:

- rotating spindle or tool entanglement and contact [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]
- chip, coolant, tool, or workpiece ejection from the machining zone. Detailed machine-tool-specific measures are `TO VERIFY`. [TO VERIFY: ISO 16090-1]
- pinch or crush hazards from moving axes or the tool changer [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]
- unexpected startup or failure to stop [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
- electrical shock and residual voltage after isolation [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md#1-protective-measures]
- stored pneumatic or hydraulic energy where tool clamping, workholding, or automatic doors use fluid power. Detailed fluid-power requirements are `TO VERIFY`. [TO VERIFY: ISO 4413]

## How To Use This Package

1. Read [standards_applicability_matrix.md](./standards_applicability_matrix.md) to determine which standards paths apply to the target market and machine configuration.
2. Use [system_description.md](./system_description.md), [hazards_and_risk_assessment.md](./hazards_and_risk_assessment.md), and [safety_functions_register.md](./safety_functions_register.md) as the baseline CNC machine concept.
3. Use [safety_integrity_and_sil_strategy.md](./safety_integrity_and_sil_strategy.md) to route machine safety functions through `ISO 13849-1` or `IEC 62061`, and use [control_architecture_and_network.md](./control_architecture_and_network.md) for controller and drive architecture.
4. Apply [ul_nec_design_requirements.md](./ul_nec_design_requirements.md) for US electrical build expectations and [mechanical_and_electrical_isolation.md](./mechanical_and_electrical_isolation.md) for lockout, STO, and stored-energy discharge points.
5. Close every `TO VERIFY` item before release to fabrication, FAT, or installation.

## Traceability Approach

Standard-driven statements use one of these tags:

- `[LOCAL: <relative_path_from_standards_intelligence>/<file>#<heading>]`
- `[TO VERIFY: <standard_name>]`

Example:

- The machine shall prevent automatic restart after power restoration. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]

## Local Corpus Boundary

The strongest local support is in:

- NFPA 79 machine electrical requirements [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#2-boundaries-with-other-standards]
- NEC installation, grounding, conductor, motor, and panel requirements [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#0-scope-and-relevance-to-control-panels] [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#0-why-this-article-matters]
- IEC 60204-1 international machine electrical requirements [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Priority Clauses]
- software and safety-routing guidance in the local software standards guide [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Fast Routing]

The weakest local support is in:

- machine-tool-specific type-C CNC requirements [TO VERIFY: ISO 16090-1]
- detailed PL or machinery SIL calculation methods [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061]
- coolant, workholding, chuck, or tool-retention standards specific to CNC machine tools [TO VERIFY: machine-tool-specific safety standard]
- cybersecurity, alarm management, and regulated audit trails [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]
