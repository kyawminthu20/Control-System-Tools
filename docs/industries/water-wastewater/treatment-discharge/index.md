---
layout: default
title: "Treatment and Discharge Compliance"
description: "Control system reference for biological wastewater treatment — activated sludge DO control, effluent quality monitoring, permit limit trip logic, and NPDES compliance."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Treatment & Discharge"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Treatment and Discharge Compliance</h1>
</div>

<blockquote>
<strong>Scope:</strong> Biological wastewater treatment (activated sludge / MBR), secondary clarification, effluent disinfection, and discharge permit compliance. Covers DO control, sludge management, online effluent monitoring, permit limit trips, and NPDES record-keeping.
</blockquote>

## Standards Applicability

| Standard | Role in this system |
|---|---|
| EPA CWA / NPDES | Permit limits for TSS, BOD, pH, TN, TP, fecal coliform — monthly average and daily maximum |
| IEC 61511 | SIF: Effluent isolation valve XV-601 closes on permit limit exceedance (SIL 1) |
| NFPA 820 | Hazardous area classification — digester gas (CH₄), confined space H₂S in clarifiers |
| ISA-18.2 | Alarm rationalization for effluent quality, blower failure, sludge blanket high |

## Treatment Train Flow

```mermaid
flowchart LR
    A[Equalized\nInfluent] --> B[Primary Clarifier\nGravity settling\n50–70% TSS removal]
    B --> C[Aeration Basin\nActivated Sludge\nDO controlled at 2.0 mg/L]
    C --> D[Secondary Clarifier\nBiosolid separation\nRAS recycled to aeration]
    D --> E[Tertiary Filtration\nor MBR Permeate]
    E --> F[Disinfection\nUV or NaOCl]
    F --> G{Permit Limits\nMet?}
    G -->|Yes| H[Discharge\nto Receiving Water]
    G -->|No| I[Divert to EQ Basin\nfor Re-treatment]
    B --> J[Primary Sludge\nto Thickening/Digestion]
    D --> K[Waste Activated Sludge\nWAS to Thickening/Digestion]
```

## Permit Limit Trip Logic

```mermaid
flowchart TD
    A[Online Effluent Analyzers\nAT-601 to AT-604] --> B{Any parameter\nexceeds permit limit\nfor > 10 minutes?}
    B -->|No| C[Normal Discharge\nLog all values to historian]
    B -->|Yes| D{Which parameter?}
    D -->|pH outside 6.0–9.0| E[Close XV-601\nAlarm: pH Permit Exceedance]
    D -->|TSS > 30 mg/L| F[Close XV-601\nAlarm: TSS Permit Exceedance]
    D -->|TOC or BOD > limit| G[Close XV-601\nAlarm: Organic Load Exceedance]
    E --> H[Activate Effluent Diversion Pump\nRoute to EQ basin if capacity available]
    F --> H
    G --> H
    H --> I[Log exceedance event:\ntimestamp, parameter, value, duration]
    I --> J[Operator acknowledges\nInvestigates cause]
    J --> K{Parameter returned\nto compliance?}
    K -->|Yes| L[Manual Reset Required\nOperator reopens XV-601]
    K -->|No — EQ full| M[Notify regulatory agency\nper permit conditions]
```

## Dissolved Oxygen Control

The aeration basin blowers run on a cascaded DO PID loop:

| Parameter | Value |
|---|---|
| PV | DO analyzer AT-601 (optical), mid-basin outlet |
| SP | 2.0 mg/L (typical; adjusted 1.5–3.0 mg/L seasonally) |
| MV | Lead blower VFD speed (0–60 Hz) |
| Assist blower | Staged on/off: starts when lead blower hits 58 Hz |
| DO < 1.0 mg/L | Alarm: Low DO — risk of filamentous bulking |
| DO > 4.0 mg/L | Trim blower speed — energy waste without treatment benefit |

## Key Engineering Decisions

**Why is the effluent trip SIL 1?** A permit limit exceedance that reaches the receiving water creates regulatory liability, potential fines, and environmental harm. The trip valve must be in the safety layer and able to close even if the process PLC is faulted. A simple hardwired relay from the pH transmitter to the valve can provide SIL 1 with proper documentation.

**WAS control:** Mixed liquor TSS (MLSS) is the control target. SCADA calculates the daily WAS volume based on MLSS, influent flow, and target SRT (solids retention time). The operator approves each WAS event — never automate WAS without operator oversight, as over-wasting crashes the biological process.

**MBR transmembrane pressure (TMP):** For MBR systems, TMP trend is the primary fouling indicator. TMP rising faster than expected indicates membrane fouling — trigger chemical cleaning before TMP reaches the backpulse limit.

## Cross-Links

- [Equalization & Neutralization](../equalization-neutralization/) — upstream
- [Instrumentation Reference](../instrumentation/) — DO and TSS analyzer selection
- [IEC 61511](/standards/functional-safety/iec-61511/)
- [Lifecycle Stage 6 — Commissioning](/lifecycle/stage-06/)
