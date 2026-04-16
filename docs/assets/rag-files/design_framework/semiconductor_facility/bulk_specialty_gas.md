<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
CATEGORY: SEMI_FACILITY
-->

# Bulk Specialty Gas Systems

## Purpose and boundary

This note covers facility-side gas infrastructure that feeds semiconductor tools and process areas:

- bulk gas storage and source equipment
- gas rooms
- gas cabinets
- valve manifold boxes
- purge panels
- tool interface points

It does not try to document the full internal process-tool gas box design.

## Typical architecture

Common flow path:

`source -> isolation -> regulation -> filtration or purification -> cabinet or panel -> local isolation -> tool interface`

Associated support paths:

- nitrogen purge
- exhausted vent path
- leak detection or gas monitoring
- valve actuation air or nitrogen
- emergency shutdown path

## Main engineering objectives

- maintain gas purity and leak integrity
- provide controlled isolation and purge
- prevent hazardous release into occupied areas
- prove utility availability before enabling flow to the tool
- define safe response to detector alarms, exhaust loss, or fire events

## Typical instrumentation and devices

- source and regulated pressure measurement
- valve position feedback
- MFC or flow measurement where the facility package controls flow
- cabinet status and door or access status where relevant
- hazardous gas detection
- exhaust proof
- purge timing and pressure confirmation

## Control philosophy highlights

- gas flow enable should depend on cabinet or enclosure health, exhaust availability, and absence of active hazard alarms
- shutdown should isolate the source and drive the system toward a proven safe state
- purge sequences need explicit entry and completion criteria
- maintenance mode must not bypass critical shutdown functions

## Common failure and hazard themes

- wrong gas or wrong connection
- small leak in high-purity welded or face-seal system
- exhaust loss causing unsafe accumulation
- regulator, valve, or MFC contamination or drift
- delayed detection because the sensing zone does not match the leak path

## Documentation outputs worth building

- gas system boundary diagram
- cabinet and VMB cause and effect
- source-to-tool pressure hierarchy
- purge sequence narrative
- alarm and shutdown ownership table

## Standards anchors

- SEMI F14 for gas source equipment enclosures
- SEMI F13 for gas source control equipment
- SEMI F6 for secondary containment of hazardous gas piping systems
- SEMI S6 for exhaust ventilation of semiconductor manufacturing equipment
- SEMI S2 and S14 for equipment safety and fire-risk framing
- NFPA 55 and NFPA 318 for facility code context

## Source anchors

- [Public Source Register](../sources/public_source_register.md)
