---
layout: default
title: "HVAC and Cleanroom Environment"
description: "Cleanroom HVAC systems for semiconductor fabs — make-up air, FFU arrays, room pressure cascade, temperature and humidity control, and particle monitoring."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
    url: "/industries/semiconductor/"
  - name: "Facility Reference"
    url: "/industries/semiconductor/facility/"
  - name: "HVAC and Cleanroom"
---

<div class="page-header">
  <span class="page-header__label">Semiconductor Facility — Environmental Control</span>
  <h1>HVAC and Cleanroom Environment</h1>
  <span class="badge badge--new">Phase 22</span>
</div>

This page covers the environmental-control layer that protects product, process stability, and utility quality inside a semiconductor facility — from room pressure cascade and airflow control through cleanroom classification monitoring.

---

## Scope

- Make-up air units (MAUs) and air-handling units (AHUs)
- Fan-filter units (FFUs) and recirculation systems
- Room pressure cascade management
- Temperature and humidity control
- Cleanliness monitoring (particles, chemical airborne contamination)
- Support utilities that affect environmental performance: chilled water supply, clean dry air

---

## Main Engineering Objectives

- Maintain the required cleanroom classification across all process areas
- Keep differential pressure relationships aligned with contamination-control intent
- Support process temperature and humidity stability at point of use
- Integrate room and utility alarms into an actionable operations model — not just a display

---

## Room Pressure Cascade

Pressure cascade design answers three questions before any sensor is placed:

1. Which rooms must stay most **positive** relative to adjacent spaces? (high-cleanliness process areas)
2. Which rooms must stay most **negative**? (gas or chemical handling, exhaust-dependent enclosures)
3. Which openings — doors, pass-throughs, service penetrations — meaningfully disturb the measurement?

```mermaid
flowchart LR
    Outside[Outside / Corridor] -->|lower pressure| Support[Support / Utility Area]
    Support -->|lower pressure| SubFab[Subfab / Chase]
    SubFab -->|higher pressure| Cleanroom[Cleanroom — Process Areas]
    Cleanroom -->|most positive| Critical[Critical Process Bays]

    style Critical fill:#e8f5e9,stroke:#4caf50
    style Cleanroom fill:#e3f2fd,stroke:#2196f3
    style SubFab fill:#fff8e1,stroke:#ff9800
    style Outside fill:#f5f5f5,stroke:#9e9e9e
```

Room pressure signals serve three distinct purposes — choose measurement strategy accordingly:

| Purpose | Measurement approach |
|---------|---------------------|
| ISO 14644 classification compliance | Per ISO 14644-2; location, frequency, and particle size specified |
| Process protection (real-time) | Fixed room monitors with alarm setpoints; continuous |
| Facilities balancing | Often portable or periodic; not for ongoing safety monitoring |

---

## Environmental Variables

| Variable | Why it matters |
|----------|----------------|
| Room differential pressure | Contamination-control cascade; hazardous area negative pressure |
| Airflow / face velocity | FFU coverage and filter integrity; exhaust makeup |
| Temperature | Process chemistry stability; material dimensional stability |
| Humidity | Electrostatic discharge risk; corrosion on metallic surfaces |
| Particle count | Direct ISO classification measurement; yield impact |
| Chemical airborne contamination (AMC) | Specific to sensitive process areas; not required everywhere |

---

## Control Themes

| Principle | Rationale |
|-----------|-----------|
| Do not use one sensor as the sole representation of a large or dynamic space | Large bays have pressure gradients; a single sensor misrepresents the space |
| Align alarm delays with real room behavior | Door openings create transient DP excursions — delays prevent nuisance alarms without masking real events |
| Document the degraded-utility response, not only total-failure response | Partial chilled water loss or partial AHU failure creates intermediate states that need defined responses |
| Keep room-pressure strategy consistent with hazardous exhaust and chemical areas | Negative-pressure zones for gas/chemical handling must stay negative even during maintenance or fan balancing |

---

## Typical Instrumentation

| Measurement | Device / Method | Notes |
|-------------|-----------------|-------|
| Room differential pressure | Very low DP transducer — capacitance sensing, stable zero | Setra 264/FLEX, Dwyer MagneSense; installation location critical |
| Airflow / face velocity | Thermal anemometer or balancing hood for commissioning; fixed monitors for critical areas | Match sensor to duct or open-face geometry |
| Temperature / humidity | Capacitive humidity and RTD/thermocouple sensor combos | Calibration interval and sensor placement in representative location |
| Particles (routine classification) | Optical airborne particle counter — fixed or portable | ISO 14644-1; calibration per ISO 21501-4 |
| Particles (sub-100 nm) | Condensation particle counter (CPC) | TSI AeroTrak 9001 CPC for nanoscale monitoring |
| AMC (if required) | Chemical-specific monitoring — online or periodic sampling | Application-specific; not universal |

See the [Instrumentation Reference](/industries/semiconductor/facility/instrumentation/) for full device selection guidance.

---

## Common Failure Themes

- **Sensor drift** on low-range room differential pressure — calibration intervals must match the DP range
- **Inadequate sensor placement** — sensors near doors, returns, or penetrations give unrepresentative readings
- **Balancing changes** that quietly invalidate the room model — pressure cascades must be reverified after any HVAC modification
- **Conflict between energy optimization and contamination control** — reducing FFU coverage or airflow volume to save energy can compromise classification without obvious alarm triggers

---

## Documentation Outputs Worth Building

- Room pressure cascade matrix (each room, setpoint, alarm limit, adjacent relationships)
- Environmental monitoring point list (sensor ID, location, measurement, alarm setpoints, calibration interval)
- Cleanroom alarm response matrix (what each alarm means, first response, escalation path)
- Startup and rebalance checklist (after construction, maintenance, or modification)
- ISO 14644-2 monitoring plan (classification frequency, sample volumes, locations)

---

## Standards Anchors

| Standard | Role |
|----------|------|
| ISO 14644-1 | Cleanroom classification — particle concentration limits by ISO class |
| ISO 14644-2 | Monitoring program requirements — frequency, locations, sample volumes |
| ISO 14644-4 | Design and construction of cleanrooms |
| ISO 21501-4 | Calibration of optical particle counters |
| Local building and mechanical codes | HVAC installation, fire protection integration, occupancy |

---

## See Also

- [Exhaust and Abatement Systems](/industries/semiconductor/facility/exhaust-abatement/) — exhaust and ventilation interact with cleanroom pressure cascade
- [Safety and Shutdown Architecture](/industries/semiconductor/facility/safety-shutdown/) — how HVAC fault conditions participate in facility shutdown logic
- [Instrumentation Reference](/industries/semiconductor/facility/instrumentation/) — room DP and particle counter selection
- [Bulk Specialty Gas Systems](/industries/semiconductor/facility/bulk-specialty-gas/) — gas handling areas require negative pressure relative to cleanroom
- [Commissioning Templates](/lifecycle/guides/commissioning-templates/) — field validation checklists
