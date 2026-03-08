<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "505"
  article_title: "Zone 0, 1, and 2 Locations — Flammable Gases, Vapors, and Liquids"

INDEX_TAGS:
  topics: ["zone_0", "zone_1", "zone_2", "IEC_60079", "ATEX", "IECEx", "hazardous_locations"]
  systems: ["process_control", "oil_gas", "chemical"]
-->

# NEC 2023 — Article 505 — Zone 0, 1, 2: Flammable Gas Locations (IEC-Aligned)

## 0. Why this article matters

Article 505 provides the IEC-aligned alternative to the Class I, Division 1/2 system from Article 501. It allows use of equipment certified under ATEX (EU) or IECEx (international) directly in US installations, without conversion. For global manufacturers, multi-national facilities, or projects with European equipment sourcing, Article 505 is the preferred classification method.

## 1. Zone definitions

| Zone | Hazard Frequency | Equivalent Division |
|------|-----------------|-------------------|
| **Zone 0** | Explosive atmosphere present **continuously** or for long periods under normal operation | Division 1 (most severe) |
| **Zone 1** | Explosive atmosphere **likely** to occur in normal operation occasionally | Division 1 |
| **Zone 2** | Explosive atmosphere **not likely** to occur in normal operation; if it does, it is for a short period | Division 2 |

Zone 0 requires the highest level of protection (usually only IS ia or special encapsulation). Zone 1 allows IS ia/ib, flameproof (Ex d), purged/pressurized (Ex p), or increased safety (Ex e). Zone 2 allows all Zone 1 methods plus non-sparking (Ex nA) equipment.

## 2. Gas groups (IEC system)

Article 505 uses the IEC gas grouping, which differs from the NEC Class I A–D groups:

| IEC Group | NEC Equivalent | Example Gases |
|-----------|---------------|--------------|
| IIC | Group A + B | Acetylene, hydrogen |
| IIB | Group C | Ethylene |
| IIA | Group D | Propane, methane |

Equipment marked IIC is suitable for all gas groups. Equipment marked IIA is the most common but cannot be used for hydrogen or acetylene atmospheres.

## 3. Equipment marking (505.9)

Equipment for Zone locations carries a marking system defined in IEC 60079-0:

```
Ex [protection method] [gas group] T[temperature code] [protection level]
```

Example: `Ex d IIB T4 Gb`
- `Ex d` — Flameproof enclosure
- `IIB` — Gas Group B (ethylene and similar)
- `T4` — Max surface temperature 135°C
- `Gb` — Equipment Protection Level for Zone 1

Equipment Protection Levels (EPL):
- **Ga** — Zone 0 (highest protection)
- **Gb** — Zone 1
- **Gc** — Zone 2

## 4. Protection methods used in Zone locations

| Method | Code | Applicable Zones | Description |
|--------|------|-----------------|-------------|
| Flameproof enclosure | Ex d | Zone 1, 2 | Enclosure withstands internal explosion; joints cool escaping gases |
| Intrinsic safety | Ex ia/ib | Zone 0/1, 2 | Energy limited below ignition threshold (see Art. 504) |
| Increased safety | Ex e | Zone 1, 2 | Additional measures to prevent sparks/excessive temps |
| Purged/pressurized | Ex p | Zone 1, 2 | Pressurized with clean air/inert gas to keep explosive atm out |
| Encapsulation | Ex m | Zone 1, 2 | Components encapsulated in compound that cannot cause ignition |
| Non-sparking | Ex nA | Zone 2 only | Normal operation cannot cause ignition |

## 5. Relationship to ATEX / IECEx

ATEX (European Directive) and IECEx (international scheme) certified equipment may be used in Article 505 Zone locations, provided it meets all applicable NEC installation requirements. The equipment certification label replaces the need for third-party evaluation in most cases.

**AHJ note:** Confirm local AHJ acceptance of ATEX/IECEx certifications. Most US AHJs accept them for Zone locations, but some require additional documentation.

## 6. Change log

- 2026-03-08 — Initial draft; Zone 0/1/2 definitions, IEC gas groups, ATEX/IECEx bridge.
