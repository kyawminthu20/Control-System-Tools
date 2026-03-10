<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-11
EDITION: 2011

IEC_HIERARCHY:
  part: "11"
  part_title: "Explosive Atmospheres — Intrinsic Safety (Ex i)"

INDEX_TAGS:
  topics: ["intrinsic_safety", "Ex_i", "IS", "zener_barrier", "galvanic_isolator", "entity_parameters", "FISCO", "associated_apparatus"]
  systems: ["process_control", "instrumentation", "oil_gas"]
  related_standards: ["NEC_Art504"]
-->

# IEC 60079-11 — Explosive Atmospheres: Intrinsic Safety (Ex i)

## 0. Why this matters for control engineers

Intrinsic safety is the primary protection method for field instrumentation — temperature transmitters, pressure transmitters, flow meters, level sensors, and similar devices. Unlike Ex d which contains an ignition, IS prevents ignition by limiting electrical energy below the ignition threshold of the gas. IS allows live maintenance and calibration in Zone 0/1 areas (ia level), making it preferred for continuous process instruments.

## 1. IS protection levels

| Level | Zone | Fault tolerance | Typical use |
|-------|------|----------------|-------------|
| ia | Zone 0, 1, 2 | Two faults — remains safe with any two component failures | Most process instruments |
| ib | Zone 1, 2 | One fault — remains safe with any one component failure | Less critical instruments |
| ic | Zone 2 only | No fault tolerance — safe in normal operation only | Zone 2 only applications |

## 2. How IS works

IS limits energy in the hazardous area circuit to levels below those required to ignite the surrounding atmosphere. Two parameters matter:

- **Voltage (U):** Must stay below spark ignition voltage for the gas group
- **Current (I):** Must stay below spark ignition current for the gas group
- **Power (P) and capacitance (C) and inductance (L):** Must stay within defined limits

The **associated apparatus** (barrier or isolator) in the safe area enforces these limits. The **field device** (transmitter, sensor) is designed to operate within IS limits.

## 3. Associated apparatus types

| Type | Description | Advantages | Limitations |
|------|-------------|-----------|------------|
| Zener (shunt) barrier | Zener diodes clamp voltage; fuse limits current; resistor limits energy | Low cost, simple, widely available | Requires intrinsically safe earth (ISE) — a dedicated low-impedance ground ≤1 Ω; does not provide galvanic isolation |
| Galvanic isolator | Isolated IS barrier — transformer or optical coupling | No ISE required; provides galvanic isolation; can be used with ungrounded field devices | Higher cost; consumes more loop power |

**When to use galvanic isolators:** Where the IS earth cannot be guaranteed ≤1 Ω, where multiple ground loops cause measurement errors, or where the process requires isolation from earth.

## 4. Entity concept

The entity concept allows mixing certified components (barriers and field devices) from different manufacturers, provided the entity parameters are compatible:

**Safe area (barrier) parameters:**
- Uo (max open circuit voltage)
- Io (max short circuit current)
- Po (max power output)
- Co (max capacitance the barrier can drive safely)
- Lo (max inductance the barrier can drive safely)

**Hazardous area (field device) parameters:**
- Ui (max input voltage)
- Ii (max input current)
- Pi (max input power)
- Ci (internal capacitance)
- Li (internal inductance)

**Compatibility check:**
- Uo ≤ Ui
- Io ≤ Ii
- Po ≤ Pi
- Ci + Ccable ≤ Co
- Li + Lcable ≤ Lo

Cable capacitance and inductance per meter must be included in the entity calculation.

## 5. FISCO model

The FISCO (Fieldbus Intrinsically Safe Concept) model applies IS to FOUNDATION Fieldbus and PROFIBUS PA installations. It allows multiple field devices on one IS segment, with a single FISCO-certified power conditioner supplying all devices. FISCO eliminates the need for individual entity parameter calculations for each device on the segment.

## 6. Relationship to NEC Article 504

NEC Article 504 implements IEC 60079-11 IS requirements for US installations. The barrier types, entity concept, IS earth requirements, and cable requirements in Art. 504 align with IEC 60079-11. Equipment certified to IEC 60079-11 (ia or ib) is generally acceptable in NEC Art. 504 IS systems — verify with the AHJ.

## 7. Change log

- 2026-03-08 — Initial draft; protection levels, energy limitation principle, barrier types, entity concept, FISCO, NEC 504 relationship.
