<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

You’re asking the right question—but there is no single “normal range.”
In industrial control, ranges depend on **process type, fluid properties, and equipment class**.

What _does_ exist are **typical engineering ranges** used in design, instrumentation selection, and alarm setting. Below is a structured baseline you can use for semiconductor facilities, HVAC, chemical handling, and general process systems.

---

# 1. Pressure (P)

### Typical Ranges by Application

| Application                        | Liquid Pressure       | Gas Pressure           |
| ---------------------------------- | --------------------- | ---------------------- |
| Ultra-pure water (UPW)             | 2 – 6 bar (30–90 psi) | —                      |
| Chemical delivery (acids/solvents) | 1 – 5 bar             | —                      |
| Process gas (low pressure)         | —                     | 0.1 – 2 bar            |
| Compressed air systems             | —                     | 6 – 8 bar (90–120 psi) |
| Vacuum systems                     | —                     | 1e-3 to 1e-9 Torr      |
| High-pressure systems              | 10 – 300+ bar         | 10 – 300+ bar          |

### Engineering Notes

- Liquids → relatively stable pressure
- Gases → compressible → more fluctuation
- Vacuum → special instrumentation (capacitance manometers, Pirani gauges)

---

# 2. Temperature (T)

### Typical Ranges

| Application                   | Liquids   | Gases        |
| ----------------------------- | --------- | ------------ |
| Cooling water / UPW           | 18 – 25°C | —            |
| Chemical storage              | 10 – 40°C | —            |
| HVAC air systems              | —         | 18 – 27°C    |
| Process gases (semiconductor) | —         | 20 – 200°C   |
| High-temp process (furnace)   | —         | 200 – 1200°C |

### Engineering Notes

- UPW systems are tightly controlled (±1°C)
- Gas temperature impacts density → affects flow accuracy
- Semiconductor processes often require **tight thermal uniformity**

---

# 3. Flow Rate (Q)

### Typical Ranges

| Application       | Liquid Flow       | Gas Flow                             |
| ----------------- | ----------------- | ------------------------------------ |
| UPW distribution  | 10 – 500 L/min    | —                                    |
| Chemical dosing   | 0.1 – 20 L/min    | —                                    |
| HVAC air          | —                 | 500 – 50,000 CFM                     |
| Process gas lines | —                 | 0.1 – 1000 slm (standard liters/min) |
| Bulk transfer     | 100 – 5000+ L/min | —                                    |

### Engineering Notes

- Liquids → measured in L/min, m³/h
- Gases → often **standardized units (SLM, SCCM)**
- Semiconductor gas systems use **mass flow controllers (MFCs)**

---

# 4. Mass Flow (ṁ)

### Typical Ranges

| Application               | Range            |
| ------------------------- | ---------------- |
| Semiconductor process gas | 1 – 10,000 sccm  |
| Industrial gas pipelines  | 10 – 10,000 kg/h |
| Chemical dosing           | 0.01 – 100 kg/h  |
| Fuel gas systems          | 1 – 1000 kg/h    |

### Engineering Notes

- Critical for **stoichiometry and reaction control**
- Independent of temperature/pressure (unlike volumetric flow)
- MFCs are standard in semiconductor fabs

---

# 5. Vibration

### Typical Ranges (ISO 10816 / 20816 guideline basis)

| Condition       | Velocity (mm/s RMS) | Interpretation     |
| --------------- | ------------------- | ------------------ |
| 0 – 2.8 mm/s    | Good                | Normal operation   |
| 2.8 – 7.1 mm/s  | Acceptable          | Monitor            |
| 7.1 – 11.2 mm/s | Alarm               | Maintenance needed |
| >11.2 mm/s      | Danger              | Immediate action   |

### By Equipment Type

| Equipment                       | Typical Range |
| ------------------------------- | ------------- |
| Pumps                           | 1 – 5 mm/s    |
| Motors                          | 1 – 4 mm/s    |
| Compressors                     | 2 – 7 mm/s    |
| Precision tools (semiconductor) | <1 mm/s       |

### Engineering Notes

- High vibration = misalignment, imbalance, cavitation
- Semiconductor tools require **ultra-low vibration**

---

# 6. Fluid-Type Considerations (Critical Insight)

## Liquids

- Incompressible → stable pressure/flow
- Sensitive to:
  - Cavitation
  - Temperature (viscosity changes)

- Typical control focus:
  - Flow stability
  - Pressure protection

## Gases

- Compressible → dynamic behavior
- Sensitive to:
  - Temperature
  - Pressure changes

- Typical control focus:
  - Mass flow accuracy
  - Pressure regulation

---

# 7. Control System Design Ranges (What YOU Should Use)

When designing PLC/SCADA systems:

### Standard Practice

- **Normal Operating Range (NOR):** 60–80% of instrument span
- **Alarm Range:**
  - Low Alarm: ~20–30%
  - High Alarm: ~80–90%

- **Trip Range:**
  - Critical limits (safety shutdown)

### Example (Pressure Sensor 0–10 bar)

- Normal: 3 – 7 bar
- Alarm Low: 2 bar
- Alarm High: 8 bar
- Trip: <1 bar or >9 bar

---

# 8. Semiconductor Facility Context (Important for your role)

Typical systems you’ll deal with:

| System            | Key Parameter Focus                         |
| ----------------- | ------------------------------------------- |
| UPW               | Flow, pressure, temperature                 |
| Chemical delivery | Mass flow, pressure                         |
| Gas cabinets      | Pressure, mass flow, safety interlocks      |
| Exhaust/scrubbers | Flow, pressure, temperature                 |
| HVAC cleanroom    | Airflow, temperature, differential pressure |
| Vacuum systems    | Ultra-low pressure                          |

---

# Bottom Line

- There is no universal “normal”—only **context-specific engineering ranges**
- For control engineers:
  - Define **instrument span**
  - Set **normal operating window**
  - Configure **alarms + interlocks**

---

If you want, I can take this further and build you a:

- **PLC/SCADA parameter template (with tags, alarms, interlocks)**
- **Semiconductor chemical/gas control matrix (ready for implementation)**
- **Standardized engineering “range + alarm philosophy” document**

That would directly fit your new semiconductor facility role.
