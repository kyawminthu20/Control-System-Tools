<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-10-1
EDITION: 2015

IEC_HIERARCHY:
  part: "10-1"
  part_title: "Explosive Atmospheres — Classification of Areas — Explosive Gas Atmospheres"

INDEX_TAGS:
  topics: ["area_classification", "zone_0", "zone_1", "zone_2", "release_grade", "ventilation", "hazardous_area_drawing"]
  systems: ["process_control", "oil_gas", "chemical"]
-->

# IEC 60079-10-1 — Area Classification: Explosive Gas Atmospheres

## 0. Why this matters for control engineers

Area classification is the foundation of all hazardous area electrical work. Before selecting any Ex equipment or specifying any installation method, the classified area must be defined — which zones exist, where they extend, and what gas group applies. Control engineers use area classification drawings to specify correct equipment and installation methods.

## 1. Zone definitions

| Zone | Condition | Typical Examples |
|------|-----------|-----------------|
| Zone 0 | Explosive atmosphere present continuously or for long periods | Inside storage tanks, inside process vessels above liquid level |
| Zone 1 | Explosive atmosphere likely to occur in normal operation occasionally | Within 1.5 m of a Zone 0 opening, pump seal areas, compressor rooms |
| Zone 2 | Explosive atmosphere unlikely in normal operation; if present, only briefly | Within 3 m of a Zone 1 boundary, around flanged joints, analyzer buildings |

**Non-hazardous (safe area):** No explosive atmosphere expected even under abnormal conditions.

## 2. Release grades

The Zone is determined by the grade of release from each release source:

| Grade | Frequency | Resulting Zone |
|-------|-----------|---------------|
| Continuous | Present continuously or for long periods | Zone 0 |
| Primary | Likely to occur periodically in normal operation | Zone 1 (typically) |
| Secondary | Not likely in normal operation; only under abnormal conditions | Zone 2 (typically) |

Multiple release sources may overlap, creating larger or higher-severity zones. The worst case in any area determines the zone classification.

## 3. Ventilation effectiveness

Ventilation dilutes released gas and determines how quickly a hazardous atmosphere disperses. Ventilation is rated:

| Grade | Description |
|-------|-------------|
| High | Concentration reduced to below LEL quickly; hazardous area can be reduced in extent |
| Medium | Concentration controlled; Zone 2 typically results from primary releases |
| Low | Cannot prevent or limit explosive atmosphere; may increase Zone extent |

Poor ventilation (Low grade) converts what would be a Zone 2 into a Zone 1 or extends Zone boundaries significantly.

## 4. Area classification process (summary)

1. Identify all release sources (flanges, seals, vents, sample points)
2. Determine grade of release for each source
3. Assess ventilation grade and availability
4. Determine Zone type and extent for each source
5. Combine overlapping zones on the area classification drawing
6. Specify the hazardous substance gas group and autoignition temperature
7. Issue and maintain the classified area drawing

## 5. Area classification documentation

The classified area drawing must show:
- Zone 0, 1, and 2 extents (plan and elevation)
- Zone boundaries with dimensions
- Gas group(s) applicable to each zone
- Basis for classification (release source reference)
- Revision history

**AHJ and inspection requirement:** The area classification drawing is required for initial installation inspection (IEC 60079-14) and periodic inspections (IEC 60079-17). Loss or non-maintenance of the drawing is a common compliance failure.

## 6. Relationship to NEC Article 505

NEC Article 505 implements the IEC Zone system for US installations. Equipment selection and installation follow IEC 60079 series requirements when Zone classification is used. Area classification methodology per IEC 60079-10-1 is applicable to both ATEX/IECEx and US Zone installations.

## 7. Change log

- 2026-03-08 — Initial draft; zone definitions, release grades, ventilation, classification process, drawing requirements.
