---
layout: default
title: "Exhaust and Abatement Systems"
description: "Process exhaust routing, abatement utilities, and vacuum support for semiconductor fab facilities — SEMI S6, NFPA 318."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
    url: "/industries/semiconductor/"
  - name: "Facility Reference"
    url: "/industries/semiconductor/facility/"
  - name: "Exhaust and Abatement"
review:
  standard: "SEMI S6 · NFPA 318 context"
  edition: "exact governing revisions not yet recorded — verify on the linked standards pages"
  status: "Review pending"
  coverage: "Process exhaust and abatement reference; practice-level, fire code compliance is the AHJ's determination."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Semiconductor Facility — Exhaust Systems</span>
  <h1>Exhaust, Abatement, and Vacuum Systems</h1>
</div>

This page covers facility utility exhaust and abatement infrastructure — including process exhaust routing, toxic and corrosive capture, abatement support systems, and vacuum interfaces where facility connections matter.

---

## Scope

- Process exhaust (general, toxic, corrosive, flammable)
- Wet and dry abatement systems
- Scrubber utilities
- Vacuum support systems (facility-side interfaces)

---

## Main Engineering Objectives

- Maintain capture and safe conveyance of hazardous emissions
- Prove exhaust availability before enabling dependent systems (gas cabinets, wet benches, process tools)
- Monitor abatement health and all utility dependencies
- Avoid false confidence from simple fan-run signals
- Keep shutdown logic aligned with actual containment risk, not just equipment status

---

## Key Control Themes

### Exhaust Proof

Exhaust-dependent systems need stronger proof than motor status alone. Proof method depends on the hazard:

| Proof method | When appropriate |
|-------------|-----------------|
| Fan status signal only | Low-hazard utility exhaust |
| Fan status + airflow confirmation | Moderate-hazard — most process exhaust |
| Airflow + differential pressure + damper position | High-hazard gas or toxic service |
| Independent flow measurement (thermal or DP) | Critical service — fail-safe must survive motor-run contact failure |

> Prove capture, not motor state.

### Abatement Dependencies

Abatement systems depend on multiple supporting utilities. Loss of any dependency can become the actual trip condition:

| Dependency | What happens on loss |
|-----------|---------------------|
| Water supply | Wet scrubber performance fails; neutralization may stop |
| Power | Abatement unit offline; tool permit-to-run may be removed |
| Chemical feed | Neutralization or treatment chemistry unavailable |
| Drain availability | Scrubber recirculation cannot purge safely |
| Instrument air | Valve actuation fails; system may go to fail-closed or fail-open depending design |
| Exhaust path integrity | Back-pressure or flow reversal risk |

Map all abatement dependencies in a formal utility dependency table before startup.

### Vacuum Interfaces

- Match gauge technology to the actual pressure regime and gas composition
- Separate process control measurements from equipment-protection measurements when response time or accuracy requirements differ
- Document contamination and maintenance assumptions for gauges and sample paths — vacuum gauges in process service foul

---

## Typical Instrumentation

| Measurement | Device / Method | Notes |
|-------------|-----------------|-------|
| Airflow (exhaust proof) | Thermal mass flow or differential pressure | Chosen for fouling tolerance and duct mounting; prove capture not motor status |
| Differential pressure (duct / enclosure) | Low DP transmitter | Cabinet negative pressure relative to room |
| pH / ORP (wet scrubbers) | Industrial electrochemical analyzer | Chemical-duty electrodes; calibration discipline |
| Fan vibration | Vibration sensor or condition monitor | Useful for trend-based maintenance before failure |
| Liquid level / recirculation status | Radar or ultrasonic level; flow switch | Scrubber reservoir and recirculation health |
| Vacuum pressure (foreline) | Capacitance manometer | Gas-independent measurement; range and corrosion tolerance |

See the [Instrumentation Reference](/industries/semiconductor/facility/instrumentation/) for full device selection guidance.

---

## Common Failure Themes

- Plugging, condensation, and deposition reducing duct capacity over time
- Wrong proof method for actual hazard — motor status only is not adequate for toxic service
- Missed dependency between exhaust capture and tool permit-to-run logic
- Poor maintenance access leading to disabled or bypassed sensors
- Abatement utility loss that was not modeled as a shutdown condition

---

## Documentation Outputs Worth Building

- Exhaust dependency matrix (which systems depend on which exhaust zones)
- Abatement utility requirement table
- Cause and effect for exhaust-loss events
- Vacuum measurement strategy note (gauge type, range, and sample-path assumptions by point)

---

## Standards Anchors

| Standard | Role |
|----------|------|
| SEMI S6 | Exhaust ventilation for semiconductor manufacturing equipment — the primary reference |
| SEMI S2 / S14 | Equipment-level safety framing — interacts with exhaust design at the tool boundary |
| NFPA 318 | Broader semiconductor facility safety and fire context |
| IEC 61511 | When exhaust-loss shutdown must be analyzed to a formal SIL requirement |

---

## See Also

- [Bulk Specialty Gas Systems](/industries/semiconductor/facility/bulk-specialty-gas/) — exhaust prove is a prerequisite for gas enable
- [Tool-Facility Interface](/industries/semiconductor/facility/tool-facility-interface/) — exhaust status as a permit-to-run input
- [Instrumentation Reference](/industries/semiconductor/facility/instrumentation/) — airflow and differential pressure device selection
- [Safety Architecture (Lifecycle Stage 04)](/lifecycle/safety-architecture/) — safety function design methodology
- [IEC 61511 — SIS Lifecycle](/standards/functional-safety/iec-61511/) — SIL requirements for exhaust-loss shutdown functions
