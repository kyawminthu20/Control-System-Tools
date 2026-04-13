<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
STATUS: AUTHORED
CATEGORY: SEMI_FACILITY_COMMISSIONING
-->

# Semiconductor Facility Utility System Commissioning Reference

## Purpose

This file provides a structured commissioning and startup framework for semiconductor facility utility systems — gas, UPW, chemical, exhaust, and cleanroom. It is a planning reference for commissioning activities, not a replacement for site-specific commissioning procedures.

## Commissioning phases

Semiconductor facility utility commissioning normally follows four phases:

| Phase | Name | Typical scope |
| --- | --- | --- |
| 1 | Pre-commissioning — mechanical completion | piping integrity, instrumentation installation check, control panel installation, grounding and bonding verification |
| 2 | Loop check and functional test | instrument calibration, loop check, valve stroke test, interlock and shutdown function test |
| 3 | Cold commissioning — utility available, no process media | flush and clean, pressure test, DI water functional run, air and nitrogen run, electrical system verification |
| 4 | Hot commissioning — process media introduction | controlled media introduction, startup sequence validation, alarm and trip set-point verification, documentation sign-off |

## Readiness criteria by phase

### Phase 1 — Mechanical completion

Before proceeding to loop check:
- Piping isometrics marked up as-built or confirmed against installation
- Instrument installations checked against data sheets (range, process connection, orientation)
- Control panel and junction box wiring continuity verified
- Grounding continuity verified per NEC or IEC 60204-1 as applicable
- Valve actuators stroked manually and position feedback verified
- All pressure relief valves and rupture disks installed and records signed

### Phase 2 — Loop check and function test

Before proceeding to cold commissioning:
- All instrument loops checked: sensor reads correctly at board, correct tag, correct engineering units
- All discrete inputs verified: status reads correctly at PLC
- All discrete outputs verified: field device responds to forced output
- All interlocks and trips function-tested: input simulated, output verified
- Cause-and-effect table signed off row by row
- Shutdown reset authority verified (who can reset, from where)

### Phase 3 — Cold commissioning

Before introducing process media:
- System flushed clean per applicable specification (UPW systems per SEMI F61 flush protocol; chemical systems per owner specification)
- Leak test completed and documented
- Control valve and modulating valve tuning completed
- Alarm setpoints entered and verified at HMI/SCADA
- Mode and state logic verified: OFF, MANUAL, AUTO transitions work correctly
- Permissive logic verified: system will not start without preconditions met
- Data historian tags confirmed active where required

### Phase 4 — Hot commissioning

Before declaring system ready for process use:
- Media introduction follows a step-by-step, sign-off-controlled sequence
- Startup sequence runs without deviations requiring manual override
- All alarms and trips verified at or near actual setpoint (challenge test preferred over simulation where safe)
- Operating manual updated with actual setpoints and as-found calibration records
- Handover documentation completed and signed

## System-specific commissioning considerations

### Bulk specialty gas systems

- Purge protocol must be completed and recorded before media introduction
- Gas cabinet door and enclosure interlocks must be verified before first fill
- Gas detection system calibration must be completed before media introduction
- Exhaust proof interlock must be verified: system will not allow media introduction without confirmed exhaust

### UPW systems

- Flush volume and flush criteria must be defined and achieved before reclaim valve opens
- Resistivity, TOC, and particle count acceptance criteria must be met before tool supply is enabled
- Sample point verification should confirm that each quality analyzer reads representative product, not stagnant sample

### Liquid chemical systems

- Secondary containment drain path must be verified before media introduction
- Containment sensor function must be verified before media introduction
- Chemical compatibility check for all wetted surfaces must be documented before first use

### Exhaust and abatement systems

- Fan rotation must be verified before any duct pressurization or media introduction
- Airflow balance must be confirmed before cleanroom or gas cabinet exhaust connections are enabled
- Abatement startup must follow the abatement system vendor's sequence, not a generic utility sequence

### HVAC and cleanroom systems

- Balancing must be completed before particle baseline testing
- Room differential pressure cascade must be confirmed: each room relative to adjacent spaces
- ISO 14644 classification test may require post-balancing settling time before formal particle test

## Documentation minimum for commissioning sign-off

- Loop check sheets: one per instrument loop, signed
- Interlock and shutdown test record: one per C&E row, signed
- Calibration certificates or calibration records for all instruments
- Leak test records with acceptance criterion and result
- Flush records where applicable
- As-built redline markups or confirmed as-built drawings
- Startup sequence record (for Hot Commissioning): actual parameters and any deviations documented
- Handover certificate

## Source anchors

- SEMI F61 — guide to design and operation of a semiconductor UPW system
- SEMI S2/S8 — safety guidelines for semiconductor manufacturing equipment
- ISA-5.1 — for loop check and documentation standards
- NFPA 79 — for industrial control panel and machine commissioning context
- IEC 60204-1 — for machine electrical equipment commissioning context
- IEC 61511 — for safety instrumented system proof test and commissioning context where SIL-rated loops are present
