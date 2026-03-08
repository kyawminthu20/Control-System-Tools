<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "504"
  article_title: "Intrinsically Safe Systems"

INDEX_TAGS:
  topics: ["intrinsically_safe", "IS", "zener_barrier", "galvanic_isolator", "entity", "FISCO", "hazardous_locations"]
  systems: ["process_control", "oil_gas", "chemical", "instrumentation"]
-->

# NEC 2023 — Article 504 — Intrinsically Safe Systems

## 0. Why this article matters for control engineers

Intrinsic safety (IS) is the preferred wiring method for instrumentation in Class I/II hazardous locations. It eliminates the need for heavy explosion-proof conduit runs to field instruments by limiting circuit energy to levels incapable of causing ignition. For process control engineers designing transmitter loops, level sensors, pressure sensors, and other field instruments in hazardous areas, IS is the standard approach.

## 1. The IS principle

An intrinsically safe circuit is one in which **no spark or thermal effect produced under specified test conditions** (normal operation or specified fault conditions) is capable of causing ignition of a specified gas/dust mixture.

The protection is achieved by limiting two parameters:
- **Voltage (Voc / Ui):** Maximum open-circuit voltage the barrier can supply
- **Current (Isc / Ii):** Maximum short-circuit current the barrier can deliver

Both the field device (transmitter, sensor) and the barrier must have evaluated entity parameters, and those parameters must be compatible.

## 2. Key components

**Intrinsically Safe Apparatus (field device):** Equipment installed in the hazardous area. Examples: 4–20 mA transmitters, thermocouple heads, level floats, solenoid valves rated for IS applications. Marked with Ex ia or Ex ib protection level.

**Associated Apparatus (barrier):** Equipment installed in the safe area (control room, panel) that provides the energy-limiting interface. Two types:

| Type | Description | Advantages |
|------|-------------|------------|
| **Zener Barrier** | Passive; uses Zener diodes + resistor + fuse. Must be connected to a certified ground bus. | Low cost, simple |
| **Galvanic Isolator** | Active; uses transformer isolation. No ground connection required. | Ground-independent, better noise immunity, preferred for new designs |

**IS Interface (barrier panel / backplane):** A structured mounting system for multiple barriers, often DIN-rail mounted in a dedicated IS cabinet section.

## 3. Entity concept and parameter matching (504.10)

When combining IS apparatus with associated apparatus, the following entity parameters must be satisfied:

| Condition | Requirement |
|-----------|-------------|
| Ui ≥ Voc | Field device max input voltage ≥ barrier max output voltage |
| Ii ≥ Isc | Field device max input current ≥ barrier max output current |
| Pi ≥ Po | Field device max input power ≥ barrier max output power |
| Ci + Ccable ≤ Co | Total capacitance ≤ barrier max capacitance |
| Li + Lcable ≤ Lo | Total inductance ≤ barrier max inductance |

Cable capacitance and inductance must be included in the calculation. This is the most common calculation error in IS loop design.

## 4. Wiring requirements (504.20, 504.30)

**Identification:** IS circuit wiring must be identified throughout — either:
- Light blue color (preferred for dedicated IS cable)
- Permanent labeling at all connection points

**Separation:** IS conductors must be physically separated from non-IS conductors. Options:
- Separate conduit or cable tray
- Barrier in the same enclosure (150mm separation in Europe; NEC requires adequate separation)
- Separate IS enclosure or IS section of a panel

**Sealing:** When IS conductors pass through a boundary between a hazardous area and a safe area, sealing may be required depending on the conduit system used. IS systems using open wiring methods (cable, not conduit) in the field do not require seals.

## 5. System documentation requirements (504.80)

A complete IS system installation must maintain documentation including:

- Control drawings for each IS apparatus and associated apparatus
- Entity parameter calculations showing compatibility
- Cable parameter verification
- Installation records with product model numbers and certifications

The AHJ may require submission of these documents for inspection.

## 6. Protection levels

IS protection has two levels, relevant to the area classification:

| Protection Level | NEC | IEC | Area Use |
|-----------------|-----|-----|----------|
| **ia** | Group I–IIC | Ex ia | Class I, Div 1 (Zone 0, 1) |
| **ib** | Group I–IIC | Ex ib | Class I, Div 1 (Zone 1 only) |
| **ic** | — | Ex ic | Zone 2 only |

For Division 1 applications (the most common IS use case), equipment must be rated ia or ib. ia equipment can survive two simultaneous faults; ib can survive one.

## 7. Relationship to FISCO and HART

**FISCO (Fieldbus Intrinsically Safe Concept):** A simplified IS methodology for FOUNDATION Fieldbus and PROFIBUS PA segments in hazardous areas. Uses pre-certified power conditioners and field devices; eliminates the need for individual entity parameter calculations. Preferred for new fieldbus installations.

**HART IS:** Most HART transmitters are available in IS versions. Use the barrier entity parameters to verify compatibility with the specific transmitter model.

## 8. Common design mistakes

1. **Ignoring cable capacitance:** Forgetting to add cable Ci to field device Ci when comparing to barrier Co.
2. **Mixing IS and non-IS in same conduit:** Violates separation requirements; invalidates IS certification.
3. **Using standard barriers for Foundation Fieldbus:** FISCO-rated barriers required for FF; standard Zener barriers cannot supply the required FF current.
4. **Wrong protection level for area:** Using ib-only equipment in Zone 0 or Division 1 areas (where ia is required).
5. **No ground bus for Zener barriers:** Zener barriers MUST connect to an IS ground bus rated for the application; the panel PE is not always adequate.

## 9. Change log

- 2026-03-08 — Initial draft; entity concept, Zener vs galvanic isolator, FISCO bridge.
