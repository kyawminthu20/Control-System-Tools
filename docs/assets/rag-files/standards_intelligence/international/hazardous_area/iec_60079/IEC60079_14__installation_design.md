<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-14
EDITION: 2013

IEC_HIERARCHY:
  part: "14"
  part_title: "Explosive Atmospheres — Electrical Installations Design, Selection and Erection"

INDEX_TAGS:
  topics: ["installation_design", "cable_selection", "wiring_segregation", "equipotential_bonding", "initial_inspection", "Ex_documentation"]
  systems: ["process_control", "oil_gas", "hazardous_area_installation"]
-->

# IEC 60079-14 — Explosive Atmospheres: Installation Design

## 0. Why this matters for control engineers

IEC 60079-14 is the installation standard — it governs how Ex equipment is wired, connected, and commissioned. A correctly certified piece of equipment installed incorrectly loses its protection. This standard defines the cable types, segregation rules, bonding requirements, and documentation that make a hazardous area installation legally compliant and actually safe.

## 1. Equipment selection principles

Before installation, verify:
1. Equipment is certified for the zone (EPL matches zone — Ga/Gb/Gc for gas zones)
2. Gas group rating matches or exceeds the hazardous substance group
3. T-code maximum surface temperature is below the substance autoignition temperature (with margin)
4. Certificate is valid and has not been superseded by a withdrawn certificate

**Check the certificate, not just the nameplate.** Certificates can be withdrawn. The IECEx certificate database and ATEX notified body records are authoritative.

## 2. Cable selection

| Cable type | Typical use | Requirements |
|-----------|-------------|-------------|
| Armoured cable (SWA/AWA) | General Ex wiring, Ex d entries | Must be appropriate for the gland type; armour provides mechanical protection |
| Screened instrumentation cable | IS circuits | Screen must be earthed at one point only (typically safe area) for IS circuits |
| Mineral insulated (MI) | High temperature or fire survival | Used where temperature exceeds normal cable rating |

**Cable segregation:** IS wiring must be separated from non-IS wiring (different conduits, trays, or a physical barrier). Mixing IS and non-IS cables can inject energy into IS circuits that exceeds entity parameter limits.

## 3. Equipotential bonding

All metallic structures in the hazardous area must be connected to an equipotential bonding network. This prevents static discharges between structures that could ignite the atmosphere.

- Bond all vessels, pipe-work, steelwork, cable trays, and equipment enclosures
- Bond connections should be accessible for inspection and testing
- Bonding resistance between any two bonded points should be <10 Ω (many authorities require <1 Ω for critical systems)
- IS earth (for zener barriers) requires a dedicated low-impedance bond ≤1 Ω to a known clean earth

## 4. Initial verification

Before energizing a new or modified Ex installation:

1. Verify all equipment certificates are valid for the zone, gas group, and T-code
2. Verify cable entry integrity (glands properly installed, stopping plugs in place)
3. Verify flame paths are undamaged (Ex d) or IS parameters are within limits (Ex i)
4. Verify equipotential bonding continuity
5. Verify that the classified area drawing matches the installed equipment zones
6. Issue a commissioning certificate (required by IEC 60079-14)

## 5. Documentation

Required documentation for an Ex installation:
- Classified area drawing (from IEC 60079-10-1)
- Equipment register (all Ex equipment with certificate numbers)
- IS loop documentation (entity parameter calculations for each IS circuit)
- Inspection and test records
- Commissioning certificate

## 6. Change log

- 2026-03-08 — Initial draft; equipment selection, cable types, segregation, bonding, initial verification, documentation.
