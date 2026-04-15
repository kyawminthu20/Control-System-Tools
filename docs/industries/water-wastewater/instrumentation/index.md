---
layout: default
title: "Instrumentation Reference — Water and Wastewater"
description: "Instrument selection guide for water and wastewater systems — flow, level, water quality analyzers, 4-20mA + HART loop architecture, material compatibility, and calibration requirements."
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Water/Wastewater"
    url: "/industries/water-wastewater/"
  - name: "Instrumentation"
---

<div class="page-header">
  <span class="page-header__label">Water/Wastewater — System Reference</span>
  <h1>Instrumentation Reference</h1>
</div>

<blockquote>
<strong>Scope:</strong> Instrument selection for water and wastewater treatment systems — flow, level, pressure, and water quality analyzers. 4-20mA + HART loop architecture, intrinsic safety for classified areas, material compatibility, and regulatory calibration requirements.
</blockquote>

## Instrument Selection Decision Tree

```mermaid
flowchart TD
    A[What are you measuring?] --> B[Flow]
    A --> C[Level]
    A --> D[Pressure]
    A --> E[Water Quality]
    B --> B1{Fluid type?}
    B1 -->|Clean water / wastewater\nConductivity > 5 µS/cm| B2[Electromagnetic mag flowmeter\nPTFE or rubber liner]
    B1 -->|Open channel\ngravity flow| B3[Ultrasonic + Parshall flume\nor V-notch weir]
    B1 -->|Digester gas| B4[Vortex or thermal mass\nHastelloy wetted parts]
    C --> C1{Open or closed?}
    C1 -->|Open basin / wet well| C2[Submersible pressure transducer\nor non-contacting ultrasonic]
    C1 -->|Closed tank| C3[Guided wave radar\nor DP transmitter]
    D --> D1[Gauge pressure transmitter\n4-20mA, HART\n316 SS diaphragm — potable\nHastelloy — chemical service]
    E --> E1{Parameter?}
    E1 -->|pH| E2[Glass electrode + transmitter\nCalibrate daily]
    E1 -->|Free chlorine| E3[Amperometric analyzer\nor colorimetric\nFlow cell required]
    E1 -->|Turbidity| E4[Nephelometric turbidimeter\nISO 7027 method\n90° scatter geometry]
    E1 -->|Dissolved oxygen| E5[Optical DO sensor\nLuminescent quenching\nNo electrolyte replacement]
    E1 -->|H₂S| E6[Electrochemical cell\nAlarm-only — not for control\nConfined space monitoring]
```

## Analyzer Loop Architecture (4-20mA + HART)

```mermaid
flowchart LR
    A[Process Stream\nSample point] --> B[Flow Cell\nor Submersion Assembly]
    B --> C[Analyzer / Transmitter\n4-20mA output\nHART secondary channel]
    C --> D{Classified Area?\nNFPA 820}
    D -->|Yes| E[IS Barrier / Galvanic Isolator\nZener or active isolator]
    D -->|No| F[Direct to AI card\nor marshalling cabinet]
    E --> G[Analog Input Card\nPLC / DCS]
    F --> G
    G --> H[Engineering Units\nConversion in PLC]
    C --> I[Local Display\nDigital indicator]
    C --> J[HART Communicator\nor Asset Mgmt System\nCalibration records, device diagnostics]
```

## Material Compatibility Quick Reference

| Process Stream | Wetted Material — OK | Avoid |
|---|---|---|
| Potable water | 316 SS, PTFE, NSF 61-certified elastomers | Lead, unlined cast iron |
| NaOCl (sodium hypochlorite) | CPVC, PVDF, Hastelloy C276 | 304 SS, carbon steel |
| Alum / PAC solution | CPVC, rubber-lined | 316 SS (pitting in Cl⁻ + acid) |
| NaOH (caustic) | 316 SS, HDPE, CPVC | Aluminum, zinc |
| H₂SO₄ (dilute, < 50%) | HDPE, FRP, rubber-lined | Stainless steel |
| Activated sludge | Rubber-lined mag, PTFE-lined | Bare 316 SS (erosion) |
| Digester gas (CH₄/H₂S) | 316 SS, Hastelloy | Carbon steel (H₂S corrosion) |

## Calibration Requirements

| Instrument | Frequency | Method | Regulatory Driver |
|---|---|---|---|
| pH analyzer | Daily 2-point verification; full calibration weekly | pH 4.0 and 7.0 buffers | State drinking water regs |
| Turbidity analyzer | Daily verification; monthly Formazin calibration | Calibration standard | EPA SWTR |
| Cl₂ residual analyzer | Daily grab sample comparison by Hach method | DPD colorimetric | EPA SWTR |
| Magnetic flowmeter | Annual; loop validation vs. portable ultrasonic | Portable check meter | Regulatory metering |
| DO analyzer (optical) | Weekly verification; replace cap annually | Air saturation method (100%) | Good practice |
| Level transmitter | Semi-annual; verify against known depth | Physical measurement | Good practice |

## ISA-5.1 Tag Convention

Follow ISA-5.1 for all instrument tags:

| First letter | Measured variable | Second letter | Function |
|---|---|---|---|
| A | Analyzer | T | Transmitter |
| F | Flow | C | Controller |
| L | Level | I | Indicator |
| P | Pressure | S | Switch |
| T | Temperature | E | Element (sensor) |

Examples: `LT-101` Level Transmitter loop 101 · `AT-301` Analyzer Transmitter loop 301 · `FIC-201` Flow Indicating Controller loop 201 · `PSH-402` Pressure Switch High loop 402

## Cross-Links

- [Chemical Dosing](../chemical-dosing/) — Cl₂ analyzer application
- [Filtration & Clarification](../filtration-clarification/) — turbidimeter application
- [Treatment & Discharge](../treatment-discharge/) — DO and TSS analyzer application
- [Lifecycle — Detailed Design](/verification/lifecycle/detailed-design/)
