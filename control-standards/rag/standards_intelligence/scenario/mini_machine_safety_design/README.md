<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Mini Machine Safety Design Scenario

## Scenario Summary

This package defines a small skid-mounted machine concept that combines:

- one electric-motor-driven hydraulic power unit feeding guarded hydraulic actuators
- two chemical dosing pumps feeding a process header
- a main control panel with PLC, safety logic, HMI, and local data logger
- mechanical shutoff and bleed points for hydraulic and chemical circuits
- electrical isolation, emergency stop, guard interlocks, and documented verification points

The baseline concept is intended for industrial indoor machinery installations at 1000 V AC or less and is structured so it can be adapted to multiple industries through overlay files. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#0-scope-and-intent] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause01__scope.md#1-in-scope-machinery]

The baseline package assumes:

- industrial machinery scope rather than building-service equipment scope [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1-applicability-rules]
- a standard industrial environment unless an overlay invokes washdown, corrosive, outdoor, or other special conditions [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]
- machine electrical compliance driven by NFPA 79 and NEC for US use, or IEC 60204-1 plus functional-safety and risk-assessment standards for international use [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#2-boundaries-with-other-standards] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#safety-framework]

The baseline package does not treat hazardous locations, fixed offshore platforms, or detailed process-safety lifecycle requirements as closed items. These are explicitly outside or beyond the local corpus baseline and are carried as `TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1-applicability-rules] [LOCAL: _standards_map.md#applicability-matrix-by-project-type]

## Intended Machine Functions

The concept machine performs these functions:

1. Start and stop a hydraulic power unit.
2. Energize guarded hydraulic actuators for clamp, lift, or valve-positioning motions.
3. Meter one or two chemicals into a process line using positive-displacement dosing pumps.
4. Present status and commands on a local HMI.
5. Record alarms, trips, commands, and selected process variables in a non-safety logger. Logging, audit trail rigor, and regulated-record controls are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: IEC 62443] [TO VERIFY: ISA-18.2] [TO VERIFY: ISA-101] [TO VERIFY: 21 CFR Part 11]

## Primary Hazards Addressed

The package addresses these hazards:

- electrical shock and residual voltage [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause06__protection_against_electric_shock.md#1-protective-measures]
- unexpected startup and failure to stop [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
- operator access to hazardous motion [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause10__operator_interface.md#2-ergonomic-considerations]
- hydraulic stored energy, pressure release, and fluid injection hazards. Detailed hydraulic normative requirements are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]
- chemical exposure, spill, overfill, and dosing errors. Detailed chemical-handling normative requirements are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: application-specific chemical handling standard]

## How To Use This Package

1. Read [standards_applicability_matrix.md](./standards_applicability_matrix.md) to determine which standards apply to the target market and industry.
2. Use [system_description.md](./system_description.md), [hazards_and_risk_assessment.md](./hazards_and_risk_assessment.md), and [safety_functions_register.md](./safety_functions_register.md) as the baseline machine concept.
3. Apply [ul_nec_design_requirements.md](./ul_nec_design_requirements.md) for US panel and machine electrical requirements, and use [safety_integrity_and_sil_strategy.md](./safety_integrity_and_sil_strategy.md) to decide whether machinery PL/SIL or process SIL methods govern the safety functions.
4. Apply the relevant file in [industry_overlays](./industry_overlays/) for sector-specific deltas.
5. Close every `TO VERIFY` item before releasing a build package, FAT package, or installation package.

## Traceability Approach

Standard-driven statements use one of these tags:

- `[LOCAL: <relative_path_from_standards_intelligence>/<file>#<heading>]`
- `[TO VERIFY: <standard_name>]`

Example:

- The machine shall prevent automatic restart after power restoration. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]

If a detailed requirement is not supported in the local corpus, the requirement is still documented as an engineering placeholder but is labeled `NOT FOUND IN LOCAL CORPUS – TO VERIFY`.

## Local Corpus Boundary

The strongest local support is in:

- NFPA 79 machine electrical requirements [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#2-boundaries-with-other-standards]
- NEC installation, grounding, conductor, motor, and panel requirements [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#0-scope-and-relevance-to-control-panels] [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#0-why-this-article-matters]
- IEC 60204-1 international machine electrical requirements [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#priority-clauses]
- cross-standard selection logic [LOCAL: crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md#topic-based-overlap-matrix] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#topic-based-overlap-matrix]

The weakest local support is in:

- detailed UL 508A clause content, because the local UL 508A library is still draft/template-heavy [LOCAL: us/ul_508a/UL508A_OVERVIEW.md#content-development-status]
- hydraulic safety standard content [TO VERIFY: ISO 4413]
- chemical handling standards [TO VERIFY: application-specific chemical handling standard]
- cybersecurity, alarm management, regulated audit trails, and industry-specific codes [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] [TO VERIFY: ISA-18.2] [TO VERIFY: ISA-101] [TO VERIFY: 21 CFR Part 11]
