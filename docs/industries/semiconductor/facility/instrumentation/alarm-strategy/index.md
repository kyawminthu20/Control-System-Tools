---
layout: default
title: "Alarm and Measurement Strategy"
description: "Alarm philosophy, utility measurement windows, alarm class definitions, and safe-state design for semiconductor facility utility systems."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Semiconductor"
    url: "/industries/semiconductor/"
  - name: "Facility Reference"
    url: "/industries/semiconductor/facility/"
  - name: "Instrumentation"
    url: "/industries/semiconductor/facility/instrumentation/"
  - name: "Alarm Strategy"
---

<div class="page-header">
  <span class="page-header__label">Semiconductor Facility — Instrumentation</span>
  <h1>Alarm and Measurement Strategy</h1>
  <span class="badge badge--new">Phase 23</span>
</div>

This page provides alarm philosophy, utility measurement guidance, and alarm class definitions for semiconductor facility utility systems. These are engineering planning references — not standards limits and not vendor setpoints.

---

## General Alarm Philosophy

- Define the instrument span around a realistic operating envelope, not around the theoretical maximum.
- Distinguish **operator awareness alarms** from **protective interlocks** and **trips**.
- Prefer independent backup sensing for high-consequence overflow, leak, gas release, or exhaust-loss conditions.
- Record who owns response to each event: operator, PLC sequence, shutdown layer, or facility emergency system.

---

## Alarm Classes

Use a staged model with four distinct classes. Every alarm point must be assigned a class before commissioning:

| Class | Meaning | Typical response |
|-------|---------|-----------------|
| `ADVISORY` | Operator awareness or maintenance attention needed | Log and notify; no automatic action required |
| `ALARM` | Condition outside normal bounds requiring operator response | Alarm annunciation; operator acknowledges and acts |
| `INTERLOCK` | Automatic block on start or next step until condition clears | PLC prevents the action; not a trip — system stays in current state |
| `TRIP` | Immediate transition to safe state | PLC initiates safe-state actions automatically |

---

## Utility Measurement Variables

| Utility domain | Variables that usually matter most | Typical planning concern |
|---|---|---|
| UPW | flow, pressure, resistivity, TOC, temperature | Quality loss can matter more than mechanical failure |
| Bulk chemical | level, flow, pressure, temperature, leak | Containment and compatibility drive shutdown behavior |
| Specialty gas | source pressure, line pressure, flow, exhaust proof, gas detection | Isolation and purge logic dominate |
| Exhaust and scrubber | airflow, differential pressure, fan status, liquid chemistry | Loss of capture is often the real trip condition |
| HVAC and cleanroom | room DP, airflow, temperature, humidity, particle count | Product contamination risk can rise before personnel risk |
| Vacuum and low-pressure | chamber or line pressure, pump status, foreline conditions | Wrong gauge technology can invalidate data |

---

## Planning Ranges by Variable Type

### Liquid utility pressure

- Normal operating windows should stay well inside the calibrated span — leave headroom before relief or trip territory.
- Alarm early enough to protect seals, tubing, and downstream tools.
- Add low-pressure alarms for loss-of-supply or pump failure detection before a dry-run trip becomes necessary.

### Gas utility pressure

- Separate source-storage pressure from cabinet, panel, and process-line pressure — they have different normal ranges and different trip priorities.
- For regulated gas service, the normal operating band is narrow compared with upstream supply.
- Use pressure proof together with valve status and flow expectations, not as a stand-alone signal.

### Temperature

- Chemical compatibility and density effects can change with temperature even when the process appears tolerant.
- Tight control is common for water quality, chemical stability, and cleanroom air temperature.
- For cleanroom air, stability and trend behavior matter more than wide-range capability.

### Flow

- Use separate low-flow alarm and no-flow trip behavior where dry running or loss of utility can damage equipment.
- Continuous flow signals often support both control and equipment-protection logic on the same tag — be explicit about which role has priority.
- Document the gas calibration basis for all gas flow signals.

### Low-range pressure and room differential pressure

- Very low DP measurements are easily corrupted by placement, door motion, and tubing errors.
- Pair room DP strategy with door policy and airflow balance assumptions before finalizing setpoints.
- Document whether the signal is for room classification, process protection, or comfort monitoring — they have different calibration and proof requirements.

### Quality analyzers

- Resistivity, conductivity, TOC, pH, ORP, and particle signals depend on sample-system design as much as analyzer selection.
- Alarm thresholds should reflect analyzer response time and actionability — tight setpoints on slow analyzers generate nuisance alarms.
- Analyzer maintenance state should be visible in the SCADA or HMI so operators know when the quality signal is unavailable or suspect.

---

## Safe-State Design

**Alarm design is incomplete until the safe state is defined.** For semiconductor facility systems, safe state typically means:

| Condition | Typical safe state |
|---|---|
| Chemical leak or overfill | Chemical isolation; drain path to containment |
| Gas release | Gas source isolation; maintained or forced exhaust; purge enabled if appropriate |
| Exhaust loss | Tool permit-to-run removed; process tools notified |
| HVAC loss | Cleanroom pressurization strategy; alarms to facility management |
| Pump or heater fault | Device off unless required for hazard mitigation path |

> Safe state is not always "everything off." For some conditions, maintaining exhaust, keeping a pump running, or keeping a valve open is part of the safe response. Document the intent, not just the action.

---

## Cause and Effect Table Structure

A cause-and-effect (C&E) table assigns every input to a class and documents what it drives:

| Tag | Description | Class | Action | Safe state | Reset authority |
|-----|-------------|-------|--------|-----------|----------------|
| PT-101 | Supply pressure low | `ALARM` | Annunciate | — | Operator |
| PT-101 | Supply pressure low-low | `TRIP` | Close XV-101, disable pump | Pump off, supply isolated | Sequence auto-reset when pressure restores + operator confirm |
| FT-201 | Chemical flow no-flow | `INTERLOCK` | Block pump start | — | Condition clear |
| GAS-301 | Gas detector high | `TRIP` | Close source valve, isolate cabinet | Source isolated, exhaust maintained | Operator, after investigation |

Populate one row per alarm class per tag. A tag with both `ALARM` and `TRIP` levels has two rows.

---

## See Also

- [Instrumentation Reference](../) — selection flow and compliance lenses overview
- [Device Family Library](../device-families/) — device families by function and failure mode
- [Vendor Families](../vendor-families/) — manufacturer comparison by measurement class
- [Safety and Shutdown Architecture](../../safety-shutdown/) — shutdown layers and cause-and-effect design
- [Common Control Philosophy](../../control-philosophy/) — permissive, interlock, and trip patterns

---

<div class="trust-boundary">
  {% include trust-boundary.html %}
</div>
