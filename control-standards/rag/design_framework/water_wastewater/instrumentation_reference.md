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
