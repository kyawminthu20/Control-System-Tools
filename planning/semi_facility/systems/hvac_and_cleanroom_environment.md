<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_CLEANROOM_ENVIRONMENT
-->

# HVAC and Cleanroom Environment

## Purpose and boundary

This note covers environmental-control systems that protect product, process stability, and utility quality:

- make-up air and air-handling systems
- fan-filter units and recirculation
- room pressure cascade
- temperature and humidity control
- cleanliness monitoring
- support utilities such as chilled water and clean dry air where they affect environmental performance

## Main engineering objectives

- maintain the required cleanliness class
- keep pressure relationships aligned with contamination-control intent
- support process temperature and humidity stability
- integrate room and utility alarms into an actionable operations model

## Pressure-cascade logic

Room pressure strategy should answer:

- which rooms must stay most positive or most negative relative to adjacent spaces
- which doors, pass-throughs, and service openings disturb the measurement
- which signals are for classification, process protection, or facilities balancing

## Environmental variables that matter

- room differential pressure
- airflow and face velocity where relevant
- temperature
- humidity
- particle count
- in some spaces, chemical airborne contamination indicators

## Typical control themes

- avoid using one room sensor as the sole representation of a large or highly dynamic space
- align alarm delays with real room behavior so doors do not create constant nuisance alarms
- document what happens during utility degradation, not only total failure
- keep room-pressure strategy consistent with hazardous exhaust and chemical handling areas

## Common failure themes

- sensor drift on low-range room differential pressure
- inadequate sensor placement
- balancing changes that quietly invalidate the room model
- conflict between energy optimization and contamination-control intent

## Documentation outputs worth building

- room pressure cascade matrix
- environmental monitoring point list
- cleanroom alarm response matrix
- startup and rebalance checklist

## Standards anchors

- ISO 14644 family for cleanroom classification, design, and environmental topics
- local building and mechanical codes for HVAC implementation
- internal contamination-control specifications where the fab imposes tighter limits than generic cleanroom practice

## Source anchors

- [Public Source Register](../sources/public_source_register.md)
