<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
STATUS: PROMOTED
CATEGORY: SEMI_FACILITY_ALARM_STRATEGY
SOURCE: planning/semi_facility/instrumentation/measurement_and_alarm_strategy.md
-->

# Measurement and Alarm Strategy

## Purpose

This note provides starting measurement windows and alarm-structure guidance for semiconductor facility utilities.

These are engineering planning ranges only. They are not standards limits and they are not vendor setpoints.

## General alarm philosophy

- Define the instrument span around a realistic operating envelope, not around the theoretical maximum.
- Distinguish operator awareness alarms from protective interlocks and trips.
- Prefer independent backup sensing for high-consequence overflow, leak, gas release, or exhaust-loss conditions.
- Record who owns response to each event: operator, PLC sequence, shutdown layer, or facility emergency system.

## Utility-level starting ranges

| Domain | Variables that usually matter most | Typical planning concern |
| --- | --- | --- |
| UPW | flow, pressure, resistivity, TOC, temperature | quality loss can matter more than immediate mechanical failure |
| Bulk chemical | level, flow, pressure, temperature, leak | containment and compatibility drive shutdown behavior |
| Specialty gas | source pressure, line pressure, flow, exhaust proof, gas detection | isolation and purge logic dominate |
| Exhaust and scrubber | airflow, differential pressure, fan status, liquid chemistry | loss of capture is often the real trip condition |
| HVAC and cleanroom | room DP, airflow, temperature, humidity, particle count | product and contamination risk can rise before personnel risk |
| Vacuum and low-pressure service | chamber or line pressure, pump status, foreline conditions | wrong gauge technology can invalidate data |

## Typical engineering windows

## Liquid utility pressure

- UPW distribution and chemical transfer often sit in low-to-moderate pressure service.
- Use normal operating windows that stay comfortably inside the calibrated span.
- Add alarms early enough to protect seals, tubing, and downstream tools before reaching relief or trip territory.

## Gas utility pressure

- Separate source-storage pressure from cabinet, panel, and process-line pressure.
- For regulated gas service, the normal operating band is usually narrow compared with upstream supply.
- Use pressure proof together with valve status and flow expectations, not as a stand-alone truth source.

## Temperature

- Tight control is common for water quality, chemical stability, and room environment.
- Chemical compatibility and density effects may change with temperature even when the process appears tolerant.
- For cleanroom air, stability and trend behavior often matter more than wide-range capability.

## Flow

- Continuous flow signals often support both control and equipment-protection logic.
- Use separate low-flow alarm and no-flow trip behavior where dry running or loss of utility can damage equipment.
- For gas systems, standardized units and gas calibration basis must be documented.

## Low-range pressure and room differential pressure

- Very low differential pressure measurements are easily corrupted by placement, drafts, door motion, and tubing errors.
- Pair room differential pressure strategy with door policy and airflow balance assumptions.
- Record whether the signal is for room classification, process protection, or comfort monitoring.

## Quality analyzers

- Resistivity, conductivity, TOC, pH, ORP, and particle signals need sample-system discipline.
- Alarm thresholds should reflect actionability and analyzer response time.
- Analyzer maintenance state should be visible so operators know when the quality signal is unavailable or suspect.

## Alarm classes

Use a simple staged model:

- `ADVISORY`: operator awareness or maintenance attention
- `ALARM`: condition outside normal bounds requiring response
- `INTERLOCK`: automatic block on start or next step
- `TRIP`: immediate transition to safe state

## Safe-state reminder

Alarm design is incomplete until the safe state is defined. For semiconductor facility systems, safe state often means:

- chemical isolation
- gas isolation
- maintained or forced exhaust
- purge enabled where appropriate
- pumps or heaters off unless they are part of the hazard-mitigation path

## Best use

Use this note when building:

- tag lists
- cause and effect tables
- alarm philosophy
- sequence narratives
- manual intake notes for new instruments
