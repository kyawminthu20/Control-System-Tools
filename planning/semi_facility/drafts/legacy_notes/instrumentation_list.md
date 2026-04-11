<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

You’re asking the right question—but this needs structure or it becomes useless fast. In semiconductor facilities, instrumentation must be tied to **process + chemical compatibility + control criticality (safety vs process vs monitoring)**.

Below is a **practical, field-usable instrumentation matrix** aligned to real fab systems (wet, gas, UPW, exhaust, HVAC, CMP, etc.), including **trusted manufacturers + common models** you’ll actually see or spec.

---

# 1. UPW (Ultra Pure Water) System

## Key Measurements

- Flow (high purity, low conductivity)
- Pressure
- Resistivity / Conductivity
- TOC (Total Organic Carbon)
- Temperature
- Level

## Instrumentation

| Measurement     | Instrument Type           | Manufacturer   | Model          |
| --------------- | ------------------------- | -------------- | -------------- |
| Flow            | Electromagnetic Flowmeter | Endress+Hauser | Promag H       |
| Flow (low flow) | Ultrasonic Flowmeter      | Siemens        | SITRANS FST020 |
| Pressure        | Pressure Transmitter      | Rosemount      | 3051S          |
| Resistivity     | Resistivity Analyzer      | Yokogawa       | FLXA402        |
| TOC             | TOC Analyzer              | Sievers        | M9             |
| Level           | Radar Level               | VEGA           | VEGAPULS 64    |
| Temperature     | RTD (Pt100)               | WIKA           | TR10           |

---

# 2. Chemical Wet Bench (Acids, Solvents)

## Key Measurements

- Chemical flow (highly corrosive)
- Tank level
- Temperature
- Leak detection
- pH

## Instrumentation

| Measurement    | Instrument Type       | Manufacturer       | Model            |
| -------------- | --------------------- | ------------------ | ---------------- |
| Flow           | Coriolis (PTFE lined) | Endress+Hauser     | Promass P        |
| Flow (alt)     | Ultrasonic            | Flexim             | FLUXUS F601      |
| Level          | Ultrasonic Level      | Siemens            | SITRANS Probe LU |
| Level (backup) | Float Switch          | Gems Sensors       | LS-7 Series      |
| pH             | pH Sensor             | Mettler Toledo     | InPro 4260i      |
| Temperature    | Thermocouple          | Omega Engineering  | TJ36             |
| Leak Detection | Chemical Leak Sensor  | TTK Leak Detection | FG-ALS           |

---

# 3. Bulk Specialty Gas System (BSGS)

## Key Measurements

- Gas pressure (high & ultra-low)
- Mass flow (critical)
- Gas detection (safety)
- Valve position

## Instrumentation

| Measurement    | Instrument Type            | Manufacturer      | Model         |
| -------------- | -------------------------- | ----------------- | ------------- |
| Flow           | Mass Flow Controller (MFC) | Brooks Instrument | SLA5800       |
| Flow           | MFC                        | MKS Instruments   | GE50A         |
| Pressure       | Capacitance Manometer      | MKS Instruments   | Baratron 627  |
| Pressure       | Pressure Transmitter       | SMC               | ISE Series    |
| Gas Detection  | Toxic Gas Monitor          | Dräger            | Polytron 7000 |
| Valve Feedback | Limit Switch               | Pepperl+Fuchs     | NJ Series     |

---

# 4. Exhaust / Scrubber System

## Key Measurements

- Airflow
- Differential pressure
- pH (scrubber liquid)
- Temperature
- Fan vibration

## Instrumentation

| Measurement           | Instrument Type   | Manufacturer     | Model          |
| --------------------- | ----------------- | ---------------- | -------------- |
| Flow                  | Thermal Mass Flow | Kurz Instruments | 454FTB         |
| Differential Pressure | DP Transmitter    | Rosemount        | 3051CD         |
| pH                    | pH Analyzer       | Endress+Hauser   | Liquiline CM44 |
| Temperature           | RTD               | WIKA             | TR34           |
| Vibration             | Vibration Sensor  | IFM              | VVB Series     |

---

# 5. HVAC / Cleanroom Control

## Key Measurements

- Airflow velocity
- Temperature
- Humidity
- Differential pressure (cleanroom cascade)
- Particle count

## Instrumentation

| Measurement           | Instrument Type      | Manufacturer                   | Model         |
| --------------------- | -------------------- | ------------------------------ | ------------- |
| Airflow               | Air Velocity Sensor  | TSI                            | 8455          |
| Temp/Humidity         | Combo Sensor         | Vaisala                        | HMT330        |
| Differential Pressure | Room Pressure Sensor | Setra                          | 264           |
| Particle Count        | Particle Counter     | Lighthouse Worldwide Solutions | Handheld 3016 |
| CO2                   | CO2 Sensor           | Vaisala                        | GMP252        |

---

# 6. CMP (Chemical Mechanical Planarization)

## Key Measurements

- Slurry flow
- Pressure (downforce)
- Temperature
- Motor current / torque

## Instrumentation

| Measurement      | Instrument Type    | Manufacturer      | Model             |
| ---------------- | ------------------ | ----------------- | ----------------- |
| Flow             | Coriolis Flowmeter | Endress+Hauser    | Promass F         |
| Pressure         | Pressure Sensor    | Honeywell         | FP2000            |
| Temperature      | RTD                | Omega Engineering | PR-21             |
| Motor Monitoring | Power Monitor      | Allen-Bradley     | 1400 Powermonitor |

---

# 7. Chemical Distribution (CDS)

## Key Measurements

- Flow (high accuracy dosing)
- Tank level
- Leak detection
- Valve status

## Instrumentation

| Measurement    | Instrument Type | Manufacturer         | Model       |
| -------------- | --------------- | -------------------- | ----------- |
| Flow           | Coriolis        | Emerson Micro Motion | CMF Series  |
| Level          | Radar           | VEGA                 | VEGAPULS 6X |
| Leak Detection | Rope Sensor     | TTK Leak Detection   | FG-OD       |
| Valve Position | Position Switch | SMC                  | D-M9 Series |

---

# What You Should Notice (Critical Insight)

## 1. Redundancy Pattern

- Level: Radar + float switch
- Flow: Primary + inferred (pressure drop)
- Gas: MFC + pressure cross-check

## 2. Material Compatibility

- UPW → PFA / PVDF / stainless 316L electropolished
- Acids → PTFE / PVDF only
- Toxic gas → orbital welded SS + VCR fittings

## 3. Control Integration

- Analog (4–20 mA / HART) → flow, pressure, pH
- Digital (EtherNet/IP, PROFINET) → advanced analyzers
- Safety hardwired → gas detection, leak, E-stop

## 4. Where Failures Actually Happen (Field Reality)

- pH probes drift → calibration issue
- Coriolis → coating / air bubbles
- DP sensors → clogged impulse lines
- MFC → zero drift / contamination

---

# If You Want Next Level (Recommended)

I can build you:

### 1. PLC/SCADA Tag Architecture

- Naming standard (ISA-5.1 aligned)
- UDT structures (Flow, Pressure, Safety)
- Alarm classes

### 2. Instrument Selection Logic Engine

- Input: chemical + pressure + flow range
- Output: exact instrument + wetted material

### 3. P&ID Template for Semiconductor Systems

- UPW skid
- Chemical delivery
- Gas cabinet
- Scrubber loop

---

If you're serious about becoming a **semiconductor facility control engineer**, this is your baseline.
Next step is not more reading—it's **building a standard library + templates** you can reuse across projects.
