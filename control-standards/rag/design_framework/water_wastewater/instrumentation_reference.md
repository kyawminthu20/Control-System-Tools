<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Instrumentation Reference — Water and Wastewater Systems

## 0. Purpose

Instrument selection guide for water and wastewater treatment systems. Covers measurement types, technology selection criteria, loop architecture (4-20mA + HART), calibration requirements, and material compatibility for corrosive and abrasive process streams.

## 1. Measurement Types and Technology Selection

### Flow Measurement

| Technology | Best For | Avoid When |
|---|---|---|
| Electromagnetic (mag) flowmeter | Clean water, slurries with conductivity > 5 µS/cm | Non-conductive fluids (distillate, DI water) |
| Ultrasonic (clamp-on or inline) | Clean liquids, retrofits, no process intrusion | High-solids slurry (signal scattering) |
| Open channel (Parshall flume / V-notch weir + ultrasonic level) | Gravity flow — influent channels, return sludge | Pressurized pipes |
| Vortex flowmeter | Steam, clean gases | Low-flow or highly viscous applications |

**Magnetic flowmeters** are the workhorse of water/WW. Key selection criteria: liner material (PTFE for chemical streams, rubber for slurries), electrode material (316SS for clean water, Hastelloy for chlorine service).

### Level Measurement

| Technology | Best For | Avoid When |
|---|---|---|
| Submersible pressure transducer | Wet wells, open basins, clean liquids | Aerated basins (bubbles cause error) |
| Ultrasonic level | Open tanks, wet wells with foam risk | Dusting or condensation (signal loss) |
| Guided wave radar (GWR) | Closed tanks, chemical storage | Coating or crystallizing media |
| Float switch | Simple high/low point detection | Continuous level |

### Water Quality Analyzers

| Parameter | Technology | Key Consideration |
|---|---|---|
| pH | Glass electrode | Calibrate with 2-point buffer daily; replace electrode every 6–12 months |
| Free chlorine | Amperometric (DPD reagent or membrane) | Sample conditioning required; flow cell must be maintained clean |
| Turbidity | Nephelometric (ISO 7027 method, 90° scatter) | Calibrated with Formazin or StablCal; bubble-free sample path |
| Dissolved oxygen | Optical (luminescent quenching) or galvanic | Optical preferred — no electrolyte replacement, faster response |
| Conductivity | 4-electrode toroidal | Minimal fouling; good for monitoring TDS and breakthrough detection |
| TOC | UV/persulfate oxidation | High maintenance; used for regulatory monitoring, not continuous control |
| H₂S | Electrochemical | Required in biological treatment confined spaces; alarm, not control |

## 2. Loop Architecture — 4-20mA + HART

Standard loop for all process transmitters:

```
Transmitter → 2-wire loop (4-20mA) → Barrier/isolator → AI card (PLC)
HART signal → Multiplexed over same 2-wire pair → Asset management system
```

**Intrinsically safe barriers** required where instruments are in NFPA 820 classified areas (biological treatment, digester areas). Use Zener barriers (passive) or galvanic isolators (active) — active preferred for HART passthrough.

**HART benefits in water/WW:**
- Remote calibration verification without disconnecting loop
- Device status and diagnostics to asset management (e.g., Emerson AMS, ABB Ability)
- Secondary variables (e.g., uncompensated flow, process temperature from same flowmeter)

## 3. Material Compatibility

| Process Stream | Wetted Material | Avoid |
|---|---|---|
| Potable water | 316 SS, PTFE, NSF-61 certified elastomers | Lead, unlined cast iron |
| Chlorine solution (NaOCl) | CPVC, PVDF, Hastelloy C276 | 304 SS, carbon steel (corrodes rapidly) |
| Alum / PAC solution | CPVC, rubber-lined | 316 SS (pitting in high chloride + acid) |
| Caustic (NaOH) | 316 SS, HDPE, CPVC | Aluminum, zinc |
| H₂SO₄ (dilute, < 50%) | HDPE, FRP, rubber-lined | Stainless steel |
| Activated sludge / slurry | Rubber-lined, PTFE-lined mag | Bare 316 SS (erosion) |
| Digester gas (CH₄/CO₂/H₂S) | 316 SS, Hastelloy | Carbon steel (H₂S corrosion) |

## 4. Calibration Requirements

| Instrument | Calibration Frequency | Method | Regulatory Driver |
|---|---|---|---|
| pH analyzer | Daily zero/span verification; 2-point calibration weekly | pH 4.0 and 7.0 buffers | State drinking water regs |
| Turbidity analyzer | Daily verification; Formazin calibration monthly | Calibration standard | EPA SWTR |
| Cl₂ residual analyzer | Daily grab sample comparison | Hach method or equivalent | EPA SWTR |
| Flow meter (mag) | Annual bench calibration or loop validation | Portable ultrasonic check | Regulatory metering |
| DO analyzer | Daily membrane check; calibration against air saturation | 100% air saturation method | Good practice |

## 5. Instrument Tagging Convention — ISA-5.1

Follow ISA-5.1 tagging:
- First letter: measured variable (L=Level, F=Flow, A=Analyzer, P=Pressure, T=Temperature)
- Second letter: modifier or readout (T=Transmitter, C=Controller, I=Indicator, S=Switch)
- Loop number: sequential by process area

Examples: `LT-101` (Level Transmitter, loop 101), `AT-301` (Analyzer Transmitter, loop 301), `FIC-201` (Flow Indicating Controller, loop 201)
