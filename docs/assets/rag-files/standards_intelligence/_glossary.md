# Standards Intelligence Glossary
**AI_READ_ACCESS: ALLOWED**
**CONTENT_CLASS: RAG_APPROVED**
**Status:** Authoritative Reference

## Purpose

Common terminology used across industrial control standards (NEC, NFPA 79, UL 508A, IEC 60204-1, ISO 13849-1, etc.)

## A

**AHJ (Authority Having Jurisdiction)**
- US term for local code enforcement official who approves electrical installations
- Typically fire marshal, electrical inspector, or building inspector
- Has final say on NEC and NFPA compliance

**Ampacity**
- Current-carrying capacity of a conductor in amperes
- Based on conductor size, insulation type, and ambient temperature
- See: NEC Article 310

## B

**Bonding**
- Permanent electrical connection to ensure conductivity between metal parts
- See also: Grounding, Equipotential Bonding
- US term: "Bonding" (NFPA 79 Ch 8, NEC Article 250)
- IEC term: "Equipotential Bonding" (IEC 60204-1 Clause 8)

## C

**CE Marking**
- European conformity marking indicating compliance with EU directives
- Required for machinery sold in European markets
- Based on IEC/ISO standards (IEC 60204-1, ISO 13849-1, ISO 12100)

**Control Circuit**
- Low-voltage circuit for operating control devices (contactors, relays, etc.)
- Typically 24VDC, 120VAC, or 230VAC
- See: NFPA 79 Ch 9, IEC 60204-1 Clause 9, NEC Article 725

**Clearance**
- Air gap distance between conductive parts
- Voltage-dependent minimum spacing
- See: UL 508A Section 4

**Creepage**
- Surface path distance between conductive parts
- Pollution degree dependent
- See: UL 508A Section 4

## D

**Disconnect (Disconnecting Means)**
- Device to isolate electrical equipment from power source
- Must be lockable in OFF position
- See: NFPA 79 Ch 5, IEC 60204-1 Clause 5

## E

**Emergency Stop (E-Stop)**
- Safety function to stop machinery in emergency
- Category 0 (uncontrolled) or Category 1 (controlled stop)
- See: NFPA 79 Ch 9, IEC 60204-1 Clause 9, ISO 13850

**Equipotential Bonding**
- IEC term for protective bonding of conductive parts
- US equivalent: "Grounding and Bonding"
- See: IEC 60204-1 Clause 8

**EGC (Equipment Grounding Conductor)**
- US NEC term for protective earth conductor
- IEC equivalent: PE (Protective Earth)
- See: NEC Article 250, NFPA 79 Ch 8

## F

**Functional Safety**
- Safety achieved through automatic protective systems
- Measured by Performance Level (PL) or Safety Integrity Level (SIL)
- See: ISO 13849-1, IEC 62061, IEC 61508

## G

**Grounding**
- Connection to earth for safety and noise control
- See: NEC Article 250, NFPA 79 Ch 8
- IEC equivalent: "Earthing" or "Equipotential Bonding"

## H

**HMI (Human-Machine Interface)**
- Operator interface devices (pushbuttons, touchscreens, indicator lights)
- See: NFPA 79 Ch 10, IEC 60204-1 Clause 10

## I

**Industrial Control Panel**
- Assembly of components for controlling industrial machinery
- Defined by: NEC Article 409, UL 508A
- May require UL listing

**IP Rating (Ingress Protection)**
- IEC rating for enclosure protection (e.g., IP65)
- First digit: Solid particle protection (0-6)
- Second digit: Liquid protection (0-9)
- See: IEC 60529

## L

**Listing**
- Third-party certification (UL, ETL, CSA)
- Verifies compliance with safety standard
- For control panels: UL 508A listing

## M

**MCCB (Molded Case Circuit Breaker)**
- Type of circuit breaker for overcurrent protection
- Common in industrial panels
- See: NEC Article 240, UL 508A Section 6

## N

**NEC (National Electrical Code)**
- NFPA 70 - US electrical installation code
- Legally adopted by most US jurisdictions
- See: NEC Articles 409, 430, 670 for industrial applications

**NEMA Rating**
- US enclosure rating system (e.g., NEMA 4X)
- Similar to IP ratings but different scale
- See: UL 508A Section 3

## O

**Overcurrent Protection**
- Circuit breakers or fuses to protect against excessive current
- See: NEC Article 240, NFPA 79 Ch 6, UL 508A Section 6

## P

**PE (Protective Earth)**
- IEC term for equipment grounding conductor
- US equivalent: EGC
- Green/yellow striped conductor
- See: IEC 60204-1 Clause 8

**PL (Performance Level)**
- ISO 13849-1 safety rating (PLa to PLe)
- Higher letter = more reliable safety function
- Alternative to SIL rating

**PLC (Programmable Logic Controller)**
- Industrial computer for machine control
- Standard programming per IEC 61131-3

## R

**Risk Assessment**
- Systematic evaluation of machinery hazards
- Required for CE marking
- See: ISO 12100

## S

**SCCR (Short-Circuit Current Rating)**
- Maximum fault current a panel can withstand
- Required for UL 508A listing and NEC Article 409
- Calculated using weakest-link method
- See: UL 508A Section SB, NEC 409.110

**Safety Function**
- Protective function to reduce risk (e-stop, light curtain, safety relay, etc.)
- Rated by PL (ISO 13849-1) or SIL (IEC 62061)

**SIL (Safety Integrity Level)**
- IEC 62061/61508 safety rating (SIL 1 to SIL 3 for machinery)
- Higher number = more reliable safety function
- Alternative to PL rating

## T

**Transformer**
- Device to change voltage levels
- Control transformers: 480V→120V or 400V→230V
- See: NFPA 79 Ch 15, UL 508A Section 11

## U

**UL (Underwriters Laboratories)**
- US testing and certification organization
- UL 508A: Standard for Industrial Control Panels
- UL listing often required for insurance/AHJ approval

## V

**VFD (Variable Frequency Drive)**
- Motor drive for speed control
- Also called: Inverter, Variable Speed Drive (VSD)
- See: NFPA 79 Ch 12, IEC 60204-1 Clause 12

## W

**Wire Sizing**
- Selection of conductor size based on ampacity
- Must account for: continuous current, ambient temperature, bundling
- See: NEC Article 310, UL 508A Section 5

---

## Cross-Standard Term Equivalents

| US Term (NEC/NFPA/UL) | IEC/ISO Term | Description |
|------------------------|--------------|-------------|
| Grounding | Earthing / Equipotential Bonding | Connection to earth |
| EGC | PE (Protective Earth) | Safety ground conductor |
| Disconnecting Means | Isolation / Incoming Supply | Main power disconnect |
| Industrial Control Panel | Control Equipment / Enclosure | Panel assembly |
| NEMA Rating | IP Rating | Enclosure protection rating |
| Circuit Breaker | MCB/MCCB | Overcurrent protective device |
| Emergency Stop | Emergency Switching Off | E-stop function |
| Performance Level (PL) | SIL (in some contexts) | Safety function rating |

## Regional Differences

### Voltage Standards
- **US**: 120V, 208V, 240V, 480V, 600V
- **EU/International**: 230V, 400V (50Hz)

### Frequency
- **US**: 60 Hz
- **EU/International**: 50 Hz

### Wire Colors
- **US Ground**: Green or bare
- **IEC Ground (PE)**: Green/Yellow striped
- **US Neutral**: White or gray
- **IEC Neutral (N)**: Blue

### Component Certification
- **US**: UL, ETL, CSA listed
- **International**: CE marked, IEC/EN certified

---

## Changelog

- 2026-01-15 — Initial glossary created
  - Common terms from NEC, NFPA 79, UL 508A, IEC 60204-1
  - Cross-standard equivalents documented
  - Regional differences noted

**Status**: Ready for expansion as new standards are added

**Usage**: Reference this glossary when translating between US and international standards terminology
