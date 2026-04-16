<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Water and Wastewater Systems — Overview and Standards Stack

## 0. Purpose

This document provides the standards selection framework and industry overview for municipal drinking water treatment and industrial wastewater treatment control systems. Use it to identify which standards apply to a given project scope and in what order to apply them.

## 1. Industry Scope

Water and wastewater control systems span two related but distinct domains:

**Municipal drinking water** systems treat raw surface or groundwater to potable standards before distribution. Key processes: intake screening, coagulation/flocculation, sedimentation, filtration, disinfection (chlorination or UV), and pressurized distribution. Regulatory driver: EPA Safe Drinking Water Act (SDWA).

**Industrial wastewater** systems treat process effluent before discharge to receiving waters or municipal sewer. Key processes: equalization, pH neutralization, primary clarification, biological treatment (activated sludge, MBR), secondary clarification, polishing, and disinfection. Regulatory driver: EPA Clean Water Act (CWA) — NPDES permit limits.

Many facilities operate both — a manufacturing plant may receive potable water from a municipal supply and treat its own process wastewater before discharge.

## 2. Standards Applicability Matrix

| Standard | Municipal Water | Industrial WW | Notes |
|---|---|---|---|
| IEC 61511 | Required (SIS) | Required (SIS) | Applies to safety instrumented functions: high-level shutdown, chemical OT trips, discharge isolation |
| IEC 62443 | Required (SCADA) | Required (SCADA) | Remote RTU telemetry, HMI access, historian connections |
| ISA-18.2 | Required | Required | Alarm management — rationalization, suppression, alarm priority |
| AWWA M31 | Required | N/A | Distribution system design (municipal only) |
| AWWA M36 | Required | N/A | Water audits, distribution water loss |
| EPA SDWA | Required | N/A | Maximum contaminant levels, treatment technique requirements |
| EPA CWA (NPDES) | N/A | Required | Effluent discharge permit limits: TSS, BOD, pH, TN, TP |
| NFPA 820 | N/A | Required | Hazardous area classification — biological treatment areas generate H₂S and CH₄ |
| NFPA 70 (NEC) | Required | Required | Art. 430 (motors), Art. 820 (wastewater), wet/corrosive wiring |
| IEC 60204-1 | Applicable | Applicable | Machinery electrical equipment for packaged treatment systems |

## 3. Standards Selection Guidance

**Start with IEC 61511** to identify safety instrumented functions (SIFs). Common SIFs in water systems:
- High-level shutdown on raw water storage tanks
- Chlorine OT (over-treatment) trip — closes distribution isolation valve if residual exceeds maximum
- UV failure shutdown — closes bypass valve if UV intensity drops below minimum dose
- Overflow prevention — isolation on equalization basin high-high level

**Apply IEC 62443** wherever SCADA communicates over IP networks, including RTU telemetry, remote HMI access, or historian connections. Identify security zones and conduits between them.

**Apply ISA-18.2** to rationalize alarms on every process loop. Water systems are historically over-alarmed. Each alarm must have: priority, setpoint, deadband, response time, required operator action.

**Apply NFPA 820** to any enclosed biological treatment structure. Anaerobic digestion areas are Class I Division 1 or Division 2 for methane; H₂S is present in all biological treatment areas.

## 4. Control System Architecture Pattern

Water/wastewater plants typically use a distributed PLC architecture with a central SCADA server:
- One or more process PLCs (per treatment unit or building)
- Remote I/O drops for field instruments in outlying pump stations
- RTUs for geographically remote sites (booster stations, reservoirs)
- Central SCADA server with historian
- HMI workstations in control room

Communication: Modbus TCP or EtherNet/IP for local PLCs; DNP3 or ICCP over dedicated WAN for remote RTUs.

## 5. Key Regulatory Interface Points

| Requirement | Regulatory Driver | Control System Role |
|---|---|---|
| Continuous turbidity monitoring post-filter | EPA Surface Water Treatment Rule | AI input to SCADA historian — regulatory record |
| Continuous Cl₂ residual logging | EPA SWTR | AI input with 4-hour rolling average logged |
| NPDES effluent sampling | EPA CWA | Effluent composite sampler triggered by SCADA |
| Backflow prevention proof of compliance | State drinking water regs | Valve position feedback logged by SCADA |
| EQ basin level alarm | Facility discharge permit | High-high level triggers alarm and reporting event |