<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_DEVICE_FAMILIES
-->

# Semiconductor Facility Device Family Map

## Purpose

This map groups common device families by engineering function and typical fab utility usage.

## Core device families

| Device family | Typical fab service | Main engineering concern | Typical failure concern |
| --- | --- | --- | --- |
| Pressure transmitters | UPW, chemicals, CDA, gases, exhaust | wetted materials, cleanability, range selection | drift, plugging, diaphragm attack |
| Pressure switches | permissives, fan proof, gas cabinet status | discrete trip point integrity | nuisance trips, hidden setpoint drift |
| Differential pressure transmitters | room cascade, filter loading, exhaust proof | low-range stability, impulse path design | clogging, zero drift |
| Capacitance manometers and vacuum gauges | tool vacuum and low-pressure gas service | pressure regime fit, contamination tolerance | contamination, zero shift |
| Electromagnetic flowmeters | conductive liquids and water systems | conductivity dependence, liner compatibility | coating, grounding issues |
| Coriolis flowmeters | accurate chemical dosing or transfer | compatibility, density effects, cleanability | coating, entrained gas |
| Ultrasonic flowmeters | non-invasive utility monitoring | pipe installation and signal quality | poor coupling, low signal |
| Thermal mass flow sensors | exhaust and gas utilities | gas composition assumptions | fouling, contamination |
| Mass flow controllers and meters | process gas and specialty gas lines | gas calibration, cleanliness, control response | zero drift, contamination |
| Radar and non-contact level | bulk tanks and day tanks | tank geometry, foam, dielectric behavior | false echoes, buildup |
| Point level switches | overfill, backup permissive, dry run protection | compatibility and proof testing | sticking, coating |
| RTDs and temperature transmitters | water, chemicals, air systems | sheath material and location | drift, thermal lag |
| pH and ORP analyzers | wastewater, chemical prep, scrubbers | sample conditioning, calibration, sensor life | coating, reference poisoning |
| Resistivity or conductivity analyzers | UPW generation and distribution | sample integrity and low-level measurement discipline | contamination, temperature error |
| TOC analyzers | UPW quality monitoring | sample handling and maintenance burden | fouling, calibration drift |
| Gas detectors | toxic, corrosive, or flammable gas monitoring | gas-specific sensing method and zoning | poisoning, missed bump tests |
| Liquid leak detection | chemical areas, double-containment, cabinets | sensor placement and compatibility | cable damage, false positives |
| Particle counters | cleanroom and UPW monitoring | sampling method and contamination control | calibration loss, sample bias |
| Valve position feedback | diaphragm valves, actuated shutoffs | proof of isolation or enable | switch misalignment |
| Vibration and condition sensors | pumps, fans, rotating equipment | mounting and interpretation | noise, loose mounting |

## Device-family grouping by system

## Bulk specialty gas

- pressure transmitters and switches
- MFCs and MFMs
- gas detectors
- valve feedback
- leak detection and cabinet status points

## Bulk chemical and wet process

- coriolis or compatible liquid flow measurement
- tank level instruments and overfill switches
- temperature transmitters
- leak detection
- pH, conductivity, or concentration-related analyzers where applicable

## Water and wastewater

- flowmeters
- pressure transmitters
- resistivity or conductivity
- TOC
- pH and ORP
- level and pump condition monitoring

## Exhaust and abatement

- differential pressure
- airflow or thermal mass flow
- pH and ORP for wet scrubbing
- fan status and vibration
- temperature and pressure monitoring

## HVAC and cleanroom

- temperature and humidity
- room differential pressure
- airflow velocity
- particle counters
- chilled-water and air-handling utility sensors

## Selection note

No device family is automatically valid across all semiconductor services. The same measured variable can require very different technologies depending on contamination sensitivity and hazard level.
