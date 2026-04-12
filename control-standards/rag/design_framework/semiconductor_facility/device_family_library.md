<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: DERIVED_REFERENCE
STATUS: PROMOTED
CATEGORY: SEMI_FACILITY_DEVICE_FAMILIES
SOURCE: planning/semi_facility/instrumentation/device_family_map.md
-->

# Semiconductor Facility Device Family Library

## Purpose

This file groups common instrument device families by engineering function and typical fab utility usage.

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
| Temperature transmitters and RTDs | UPW, chemicals, cleanroom air | accuracy class, immersion length, cleanability | drift, installation error |
| Conductivity and resistivity analyzers | UPW quality and wastewater | sample system, calibration method, cell constant | fouling, sample temperature effects |
| TOC analyzers | UPW TOC monitoring | sample conditioning, response time | fouling, reagent management |
| pH and ORP sensors | scrubber effluent, chemical neutralization | reference junction, coating, maintenance access | junction fouling, coating |
| Dissolved oxygen sensors | wastewater polishing and cooling | membrane fouling, calibration in process | membrane failure, low signal |
| Gas detectors — electrochemical | toxic gas: HF, Cl2, NH3, HCl, and similar | response time, cross-interference, bump-test discipline | sensor expiry, contamination |
| Gas detectors — photoionization | VOC screening | concentration range, correction factors | lamp fouling, high humidity |
| Gas detectors — infrared | combustible or specific gas | gas-specific calibration | window fouling, humidity effects |
| Particle counters | cleanroom classification | isokinetic sampling, location | sampling errors, maintenance intervals |
| Low-DP transmitters | room cascade, AHU filter loading | range overlap with installation noise | clogging, installation-induced error |

## Notes on selection context

- Device family selection always follows media compatibility first, then control criticality, then integration method.
- See `instrumentation_selection.md` for selection principles and documentation minimums.
- See `instrumentation_use_matrix.md` for per-system device mapping.
- See `vendor_families.md` for manufacturer comparison by measurement class.
