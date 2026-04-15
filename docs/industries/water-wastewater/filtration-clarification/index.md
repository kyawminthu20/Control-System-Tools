---
layout: default
title: "Filtration and Clarification"
description: "Control system reference for gravity filtration, pressure filtration, and clarification — filter run/backwash state machine, turbidity control, and coagulant integration."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Filtration & Clarification"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Filtration and Clarification</h1>
</div>

<blockquote>
<strong>Scope:</strong> Rapid gravity filters, pressure filters, and lamella clarifiers. Filter run/backwash state machine, turbidity-driven backwash initiation, filter-to-waste logic, and coagulant dosing integration.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| EPA SWTR | Turbidity < 0.3 NTU in 95% of measurements; < 1 NTU at all times — continuous logging required |
| ISA-18.2 | Alarm priority for turbidity spike, head loss alarm, backwash tank low |
| IEC 61511 | SIF: Filter effluent isolation if turbidity > 1.0 NTU (protects clearwell from contamination) |

## Filter Run / Backwash State Machine

```mermaid
stateDiagram-v2
    [*] --> Standby
    Standby --> Filtering : Start command received
    Filtering --> BackwashInitiate : dP > 2.5m H₂O\nOR runtime > 24h\nOR turbidity spike
    BackwashInitiate --> AirScour : Close effluent valve\nOpen BW supply
    AirScour --> Backwash : Air scour complete (3–5 min)
    Backwash --> Rinse : Backwash complete (8–12 min)
    Rinse --> Filtering : Turbidity < 0.2 NTU for 5 min
    Rinse --> Alarm_FailToReturn : Turbidity still > 0.5 NTU\nafter 2 backwash cycles
    Filtering --> Standby : Stop command
    Alarm_FailToReturn --> Standby : Operator resets
```

## Turbidity-Driven Filter Bypass Logic

```mermaid
flowchart TD
    A[AT-201\nFilter Effluent Turbidity] --> B{Turbidity > 0.3 NTU?}
    B -->|No| C[Normal Operation\nLog to SCADA historian]
    B -->|Yes| D{Duration > 15 min?}
    D -->|No| E[Alarm: High Turbidity\nCheck filter and coagulant dose]
    D -->|Yes| F[Initiate Backwash Sequence]
    F --> G{Post-backwash turbidity\n< 0.2 NTU?}
    G -->|Yes| C
    G -->|No — 2nd cycle| H[Close Filter Effluent Valve XV-201\nAlarm: Filter Offline — Operator Action Required]
    H --> I[Route raw water to adjacent filter\nif available]
```

## Key Engineering Decisions

**Filter-to-waste is non-negotiable after backwash.** Backwash water contains the TSS and organisms removed from the media. Returning this to the clearwell would spike turbidity and could compromise disinfection efficacy. Route to backwash recovery basin or drain — not clearwell.

**Multiple filter sequencing:** Do not backwash more than one filter simultaneously (reduces plant capacity). Stagger backwash triggers by 2-hour minimum offset between filters.

**Turbidity analyzer location:** Sample point must be downstream of the filter bed, upstream of the clearwell. Dead time between the filter and the analyzer determines PID response time.

## Cross-Links

- [Chemical Dosing](../chemical-dosing/) — upstream coagulant affects filter loading
- [Instrumentation Reference](../instrumentation/) — turbidimeter selection and calibration
- [IEC 61511](/standards/functional-safety/iec-61511/)
