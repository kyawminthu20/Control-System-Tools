<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "500"
  article_title: "Hazardous (Classified) Locations — General"

INDEX_TAGS:
  topics: ["hazardous_locations", "classified_locations", "class_I", "class_II", "division_1", "division_2", "explosion_proof", "temperature_code"]
  systems: ["process_control", "oil_gas", "chemical", "dust"]
-->

# NEC 2023 — Article 500 — Hazardous (Classified) Locations: General

## 0. Why this article matters for control engineers

Processes involving flammable gases, vapors, liquids, combustible dust, or ignitable fibers require electrical equipment specifically rated for those environments. Standard industrial equipment can ignite an explosive atmosphere. Article 500 establishes the classification system that all subsequent hazardous location articles (501–506) build upon. Control system designers must know the classification method to specify correct equipment.

## 1. Classification system overview

NEC uses two parallel classification systems:

| System | Articles | Origin | Terminology |
|--------|----------|--------|-------------|
| **Class/Division** | 500–503 | Traditional US | Class I/II/III, Division 1/2 |
| **Zone** | 505–506 | IEC-aligned | Zone 0/1/2 (gas), Zone 20/21/22 (dust) |

Both systems are recognized in NEC 2023. The Zone system (Art. 505/506) aligns with IEC 60079 and is increasingly used for new installations, especially in facilities with global equipment sourcing. Either system may be used, but they cannot be mixed in the same installation area.

## 2. Class system — hazardous material type (500.5)

**Class I — Flammable Gases or Vapors**
Locations where flammable gases, flammable liquid–produced vapors, or combustible liquid–produced vapors are or may be present in quantities sufficient to produce explosive or ignitable mixtures. Examples: petroleum refineries, spray finishing areas, solvent handling, fuel dispensing.

**Class II — Combustible Dust**
Locations where combustible dust is or may be present in quantities sufficient to produce explosive or ignitable mixtures. Examples: grain elevators, flour mills, starch plants, sugar refineries, coal-handling facilities, metal powder processing.

**Class III — Ignitable Fibers / Flyings**
Locations where easily ignitable fibers or flyings are present but not likely to be in suspension in quantities to produce ignitable mixtures. Examples: textile mills, cotton gins, sawmills, woodworking plants.

## 3. Division system — probability of occurrence (500.5)

Within each Class, the **Division** indicates how frequently the hazardous atmosphere exists:

**Division 1:** The hazardous atmosphere exists under **normal operating conditions**, or exists frequently due to repair/maintenance operations, or occurs due to equipment failure that simultaneously causes an ignition hazard.

**Division 2:** The hazardous material is handled in **closed systems** and is only present under abnormal conditions (e.g., container failure, abnormal ventilation loss). The hazardous atmosphere is not normally present.

**Practical implication:**
- Division 1 requires a higher level of protection (e.g., explosion-proof or purged enclosures)
- Division 2 allows some less expensive protection methods (e.g., non-sparking equipment, hermetically sealed contacts)

## 4. Temperature codes (T-codes)

Electrical equipment in hazardous locations must not heat surfaces to a temperature that could ignite the hazardous material. T-codes define the maximum surface temperature:

| T-Code | Max Surface Temp |
|--------|----------------|
| T1 | 450°C |
| T2 | 300°C |
| T3 | 200°C |
| T4 | 135°C |
| T5 | 100°C |
| T6 | 85°C |

Select equipment whose T-code maximum surface temperature is **below the auto-ignition temperature** of the gas or dust present. Equipment must be marked with its T-code.

## 5. Protection methods for Class I locations

**Division 1** (most hazardous) requires one or more of the following:

| Method | NEC Term | Principle |
|--------|----------|-----------|
| Explosion-proof | XP | Enclosure contains explosion; cools gases before release |
| Intrinsically safe | IS | Circuit energy too low to ignite (see Art. 504) |
| Purged/Pressurized | PX/PY/PZ | Maintains inert gas positive pressure inside enclosure |

**Division 2** (less hazardous) allows the above methods plus:

| Method | NEC Term | Principle |
|--------|----------|-----------|
| Non-incendive | NI | Circuit/equipment cannot ignite under normal conditions |
| Hermetically sealed | — | Contacts sealed to prevent contact with atmosphere |

## 6. Area classification documentation (500.4)

The AHJ requires documentation of classified locations. This typically includes:

- A classified area drawing showing extent of each zone
- The Class, Division, and Group for each area
- The basis for classification (ventilation rates, release scenarios)
- Reference to the material's hazardous properties

**Groups:** Class I is further subdivided by the explosive characteristics of the gas:
- Group A: Acetylene
- Group B: Hydrogen (and gases with similar properties)
- Group C: Ethylene, cyclopropane
- Group D: Propane, methane, gasoline, butane

Class II groups:
- Group E: Metal dusts (aluminum, magnesium) — most hazardous
- Group F: Carbon black, coke, coal dust
- Group G: Flour, starch, grain dust, combustible plastic/chemical dust

## 7. Relationship to IEC 60079

The Zone classification system (Art. 505/506) aligns directly with IEC 60079. Equipment marked with ATEX or IECEx certification can be used in Zone-classified areas. Zone 0 (continuous) and Zone 1 (intermittent) both fall within the scope of Division 1; Zone 2 (unlikely, brief) maps to Division 2. The mapping is approximate; always verify with the area classification drawing.

## 8. Change log

- 2026-03-08 — Initial draft; established Class/Division/Group/T-code framework with IEC 60079 bridge.
