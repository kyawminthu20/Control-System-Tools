---
layout: default
title: "Chemical Dosing Systems"
description: "Control system reference for water treatment chemical dosing — flow-paced chlorination, coagulant dosing, pH correction, over-treatment shutdown, and chemical feed interlock chain."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Chemical Dosing"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Chemical Dosing Systems</h1>
</div>

<blockquote>
<strong>Scope:</strong> Chlorination (disinfection), coagulant/flocculant dosing, and pH correction. Flow-paced dosing with residual feedback trim, over-treatment (OT) shutdown safety logic, and the chemical feed interlock chain.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| EPA SDWA | MCL for disinfection byproducts; SWTR residual requirements at distribution entry |
| IEC 61511 | OT shutdown (XV-301 isolation valve) is a SIF — SIL 1 minimum |
| ISA-18.2 | Alarm rationalization: low residual (early warning), OT alarm, containment high |
| NFPA 70 (NEC) | Chemical room wiring — GFCI in wet areas, corrosion-resistant conduit |

## Dosing Loop — Flow-Paced with Residual Feedback Trim

```mermaid
flowchart LR
    A[FT-301\nRaw Water Flow] --> B[Feedforward\nBase Rate Calculation\nDose × Flow × Concentration factor]
    C[AT-301\nCl₂ Residual Analyzer] --> D[PID Feedback Trim\nSP: 0.5–1.0 mg/L\nTrim limit: ±30% of base]
    B --> E[Sum: Base + Trim\n= Final Dosing Rate]
    D --> E
    E --> F[Metering Pump P-301\n4-20mA Speed Signal]
    F --> G[Injection Point\nUpstream of contact time]
    G --> H[Contact Basin\n30-min retention at design flow]
    H --> C
```

## Chlorine Over-Treatment Shutdown Logic

```mermaid
flowchart TD
    A[AT-301 Cl₂ Residual] --> B{Residual > 3.5 mg/L?}
    B -->|No| C[Normal Operation]
    B -->|Yes| D[Alarm: High Cl₂ Residual\nNotify operator]
    D --> E{Residual > 4.0 mg/L\nfor > 5 minutes?}
    E -->|No| C
    E -->|Yes| F[TRIP: Close XV-301\nDistribution Isolation Valve\nHardwired SIL-1 output]
    F --> G[Alarm: System Isolated — OT Trip\nLog event with timestamp]
    G --> H[Operator investigates\nChecks analyzer calibration\nChecks dosing pump]
    H --> I{Residual confirmed\n< 4.0 mg/L?}
    I -->|Yes| J[Manual Reset Required\nOperator physically resets XV-301]
    I -->|No| K[Maintain Isolation\nEscalate if residual stays high]
```

## Chemical Feed Interlock Chain

```mermaid
flowchart LR
    A[Secondary Containment OK?\nSump float switch clear] -->|Yes| B[Tank Level > LL?\nLT-TANK > 5%]
    A -->|No — HIGH| X[LOCKOUT: All Chemical Pumps\nAlarm: Containment High Level]
    B -->|Yes| C[Process Flow Present?\nFT-301 > 20 m³/h]
    B -->|No| Y[STOP: Pump\nAlarm: Chemical Supply Low]
    C -->|Yes| D[Injection Pressure OK?\nPT-INJECT > 50 kPa]
    C -->|No| Z[STOP: Dosing\nNo flow to dilute into]
    D -->|Yes| E[NORMAL: Dosing Active\nMonitor FT-302 for flow confirmation]
    D -->|No| W[ALARM: No Injection Pressure\nCheck pump and isolation valve]
```

## Key Engineering Decisions

**Why a 5-minute delay on the OT trip?** Chlorine residual analyzers have 2–4 minute response lag due to sample transport and measurement time. A spike reading lasting < 5 minutes is likely an analyzer artifact or short disturbance, not a true system OT condition.

**Why latch the XV-301 closure?** An unacknowledged OT condition could represent a dosing system fault. Forcing a manual reset ensures an operator physically inspects before the system returns to service. This is an IEC 61511 requirement for SIL-rated trips.

**Coagulant dose — no feedback loop:** Turbidity response to coagulant takes 20–40 minutes through the treatment train. Real-time feedback would be unstable. Use jar test results to set dose ratio; use operator trend review to optimize.

## Cross-Links

- [Filtration & Clarification](../filtration-clarification/) — filter performance depends on coagulant dose
- [Instrumentation Reference](../instrumentation/) — Cl₂ analyzer selection and calibration
- [IEC 61511](/standards/functional-safety/iec-61511/)
