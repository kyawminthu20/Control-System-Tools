---
layout: default
title: "Equalization and Neutralization"
description: "Control system reference for industrial wastewater equalization basins and pH neutralization systems — level-based state machine, pH PID loop, and discharge hold logic."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Equalization & Neutralization"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Equalization and Neutralization</h1>
</div>

<blockquote>
<strong>Scope:</strong> Industrial wastewater equalization basins and pH neutralization systems. Equalization dampens flow and pH variation before downstream biological treatment. Neutralization brings pH within permit range for discharge or further treatment.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| IEC 61511 | SIF: Final effluent pH out-of-range closes discharge valve (SIL 1) |
| EPA CWA (NPDES) | Permit pH limit typically 6.0–9.0; discharge hold logic must be documented |
| ISA-18.2 | Alarm priority for High-High level, pH out-of-range, containment alarm |
| NFPA 820 | If equalization basin is enclosed — evaluate for H₂S generation (acid WW + organic) |

## Equalization Basin Level Control State Machine

```mermaid
stateDiagram-v2
    [*] --> Receiving
    Receiving --> NormalPumping : Level > 40%
    NormalPumping --> HighLevel : Level > 80%
    HighLevel --> NormalPumping : Level drops below 70%\nafter pump rate increase
    HighLevel --> HighHighLevel : Level > 90%
    HighHighLevel --> Alarm_Overflow : Level > 95%
    NormalPumping --> LowLevel : Level < 20%
    LowLevel --> Standby : Level < 10%\nStop transfer pump
    Standby --> Receiving : Level > 20%\nRestart transfer pump
    Alarm_Overflow --> HighLevel : Level drops below 90%\nOperator reset required
```

## pH Neutralization Control Loop

```mermaid
flowchart LR
    A[AT-501\nInfluent pH] --> B{pH < 6.0?}
    B -->|Yes — Acid| C[PID Controller — Caustic\nSP: 7.0\nMV: NaOH pump speed]
    B -->|No| D{pH > 9.0?}
    D -->|Yes — Caustic| E[PID Controller — Acid\nSP: 7.0\nMV: H₂SO₄ pump speed]
    D -->|No| F[Hold — Both pumps off\npH within neutral range]
    C --> G[Neutralization Tank\n5-minute residence time]
    E --> G
    F --> G
    G --> H[AT-502\nNeutralized pH]
    H --> I{6.5 ≤ pH ≤ 8.5?}
    I -->|Yes| J[Release to downstream treatment]
    I -->|No — out of range| B
```

## Key Engineering Decisions

**pH PID loop considerations:** pH is logarithmic — the gain required to move pH from 5 to 6 is far less than from 3 to 4 on the same dose. Use gain scheduling (high gain at extreme pH, low gain near setpoint) or a linearized control law. Without this, the loop will oscillate violently near setpoint and be sluggish at extremes.

**Cascade neutralization:** A single-stage neutralization tank is difficult to control precisely. Two-stage is the industry standard — Stage 1 removes most of the acid/base demand (coarse correction), Stage 2 trims to permit range (fine correction). Each stage has its own pH analyzer and reagent pump.

**Enclosed EQ basin ventilation:** If the facility generates acid waste streams (pH < 4), H₂S can evolve in the equalization basin. Treat the enclosed EQ area as a confined space and evaluate for NFPA 820 hazardous area classification.

## Cross-Links

- [Treatment & Discharge](../treatment-discharge/) — downstream of neutralization
- [Instrumentation Reference](../instrumentation/) — pH analyzer selection
- [IEC 61511](/standards/functional-safety/iec-61511/)
- [NFPA 820 — Wastewater Hazardous Areas](/standards/)
