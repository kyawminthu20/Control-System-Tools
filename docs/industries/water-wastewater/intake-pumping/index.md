---
layout: default
title: "Intake and Raw Water Pumping"
description: "Control system reference for raw water intake screens, wet wells, and pump stations — start permissives, VFD control, and level-based sequencing."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Intake & Pumping"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Intake and Raw Water Pumping</h1>
</div>

<blockquote>
<strong>Scope:</strong> Raw water intake screens, wet wells, and pump stations that lift raw water to the treatment plant headworks. Covers pump start permissives, VFD speed control, multi-pump sequencing, and protection trips.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| IEC 61511 | SIL assessment for wet well Low-Low shutdown (prevents pump damage, dry run) |
| ISA-18.2 | Alarm rationalization — screen dP, suction pressure, motor temperature |
| NEC Art. 430 | Motor branch circuit protection and overload sizing |
| AWWA M17 | Pump station design reference (suction conditions, NPSH, pipe sizing) |

## Pump Station Control Architecture

```mermaid
flowchart TD
    A[Level Sensor LT-101\nWet Well] --> B[PLC]
    C[Pressure PT-101\nSuction] --> B
    D[VFD-101 Status] --> B
    E[ZSO-101\nDischarge Valve] --> B
    B -->|All permissives OK| F[Start Pump P-101\nRamp VFD to setpoint]
    B -->|Any permissive fail| G[Hold / Alarm to SCADA]
    F --> H[Monitor FT-101\nFlow Confirmation]
    H -->|Flow confirmed| I[Normal Operation]
    H -->|No flow 30s| J[Alarm: No Flow — Check Pump/Valve]
```

## Start Permissive Chain

All permissives must be satisfied before any pump start command is accepted. Hardwired to motor control circuit AND mirrored in PLC for SCADA visibility.

```mermaid
flowchart LR
    A[Wet Well Level\nLT-101 > LL setpoint?] -->|Yes| B[Suction Pressure\nPT-101 > minimum?]
    A -->|No| X[HOLD — Wet Well Low-Low]
    B -->|Yes| C[VFD Ready?\nNo active fault]
    B -->|No| Y[HOLD — Suction Loss]
    C -->|Yes| D[Discharge Isolation\nZSO-101 open confirmed?]
    C -->|No| Z[HOLD — VFD Fault]
    D -->|Yes| E[Motor Temp OK?\nTE-101 < 120°C]
    D -->|No| W[HOLD — Valve Not Open]
    E -->|Yes| F[PERMIT — Start Pump]
    E -->|No| V[HOLD — Motor Overtemp]
```

## VFD Speed Control

Raw water pumps run on a flow demand PID loop:

| Parameter | Value |
|---|---|
| Process variable (PV) | Headworks flow FT-201 (m³/h) |
| Setpoint (SP) | Operator-set target production flow |
| Manipulated variable (MV) | VFD speed reference (0–60 Hz) |
| Minimum speed | 20 Hz (prevents suction pipe sedimentation) |
| Acceleration ramp | 5 Hz/s |
| Deceleration ramp | 3 Hz/s |

## Key Engineering Decisions

**Why hardwire the Low-Low level interlock?**
Dry running a vertical turbine pump destroys the pump within seconds. The Low-Low shutdown is a SIF per IEC 61511 — the logic must be in the safety layer (hardwired or Safety PLC), not relying on the process PLC to respond in time.

**Multi-pump sequencing:** Lead pump ramps to 58 Hz before assist pump starts. This prevents simultaneous starting inrush and avoids hunting between pumps. Lead/lag rotation occurs every 24 hours to equalize wear.

**NPSH margin:** Verify net positive suction head available (NPSHA) is ≥ NPSHR + 0.5 m margin at all wet well levels, including Low-Low. Document in pump data sheet.

## Cross-Links

- [Filtration & Clarification](../filtration-clarification/) — downstream of intake
- [Lifecycle — Detailed Design](/verification/lifecycle/detailed-design/)
- [Lifecycle — Commissioning](/implementation/lifecycle-commissioning/)
- [IEC 61511](/standards/functional-safety/iec-61511/)
