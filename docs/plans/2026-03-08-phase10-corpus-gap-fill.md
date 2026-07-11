# Phase 10: Corpus Gap-Fill (IEC 60079 + SEMI S2/S8/S14) — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add IEC 60079 (6 RAG files) and SEMI S2/S8/S14 (3 RAG files) to the corpus, plus corresponding site pages and family landing pages.

**Architecture:** Same pattern as Phases 3, 5, 8. RAG files under `control-standards/rag/standards_intelligence/`, site pages under `docs/standards/`. All content synthesized — no verbatim standard text. Each RAG file starts with the HTML metadata block.

**Tech Stack:** Markdown, YAML, Jekyll 4.3. Validation: `python3 tools/validate_ai_boundaries.py`.

---

### Task 1: IEC 60079 — Part 0 (General Requirements)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_0__general_requirements.md`

**Step 1: Create directory and file**

```bash
mkdir -p "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079"
```

Write the following content:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-0
EDITION: 2017

IEC_HIERARCHY:
  part: "0"
  part_title: "Explosive Atmospheres — General Requirements"

INDEX_TAGS:
  topics: ["explosive_atmosphere", "equipment_marking", "EPL", "temperature_class", "gas_group", "certification", "ATEX", "IECEx"]
  systems: ["process_control", "oil_gas", "chemical", "hazardous_area"]
-->

# IEC 60079-0 — Explosive Atmospheres: General Requirements

## 0. Why this matters for control engineers

IEC 60079-0 establishes the foundational marking system and general requirements for ALL electrical equipment used in explosive atmospheres. Every piece of Ex-rated equipment carries markings defined in this part. Understanding the marking system allows engineers to select, install, and inspect equipment correctly without needing to read every protection-method standard individually.

## 1. Equipment marking system

All Ex equipment carries a marking string defined in IEC 60079-0. The format is:

```
Ex [protection method(s)] [gas group] T[temp class] [EPL]
```

**Example:** `Ex d IIB T4 Gb`
- `Ex` — certified for explosive atmospheres
- `d` — flameproof protection method (see IEC 60079-1)
- `IIB` — gas group (ethylene and similar)
- `T4` — maximum surface temperature 135°C
- `Gb` — Equipment Protection Level for Zone 1

Multiple protection methods may appear: `Ex de IIC T5 Gc`

## 2. Equipment Protection Levels (EPL)

EPL is the fundamental safety indicator — it replaces older category systems for most purposes:

| EPL | Zone | Protection Level |
|-----|------|-----------------|
| Ga  | Zone 0 | Very high — two independent faults required to cause ignition |
| Gb  | Zone 1 | High — suitable for normal operation and some abnormal conditions |
| Gc  | Zone 2 | Enhanced — suitable for normal operation |
| Da  | Zone 20 | Very high (dust) |
| Db  | Zone 21 | High (dust) |
| Dc  | Zone 22 | Enhanced (dust) |

## 3. Gas groups

Gas groups classify flammable gases by their ignition energy and quenching gap:

| Group | Hazard Level | Typical Gases |
|-------|-------------|--------------|
| IIA   | Lowest | Propane, methane, acetone |
| IIB   | Intermediate | Ethylene, hydrogen sulfide |
| IIC   | Highest | Hydrogen, acetylene |

Equipment marked IIC is suitable for all gas groups. Equipment marked IIA is only suitable for Group IIA gases and must not be used in IIB or IIC atmospheres.

## 4. Temperature classes (T-codes)

The T-code specifies the maximum surface temperature the equipment can reach under worst-case conditions:

| T-code | Max Surface Temp | Typical Use |
|--------|-----------------|-------------|
| T1 | 450°C | Very high autoignition gases |
| T2 | 300°C | |
| T3 | 200°C | Kerosene, fuel oil |
| T4 | 135°C | Most common for process industry |
| T5 | 100°C | Carbon disulfide (rare) |
| T6 | 85°C | Diethyl ether |

**Engineering rule:** Select equipment whose T-code maximum surface temperature is below the autoignition temperature of the hazardous substance at the installation. A margin of at least 50°C below autoignition is recommended by most best-practice guides.

## 5. Protection methods summary

| Code | Method | Standard | Typical Application |
|------|--------|----------|-------------------|
| d | Flameproof enclosure | IEC 60079-1 | Motors, junction boxes |
| e | Increased safety | IEC 60079-7 | Terminal boxes, luminaires |
| i | Intrinsic safety | IEC 60079-11 | Instrumentation, sensors |
| m | Encapsulation | IEC 60079-18 | Small components |
| n | Non-sparking | IEC 60079-15 | Zone 2 only |
| p | Purged/pressurized | IEC 60079-2 | Control panels, analyzers |
| q | Powder/sand filling | IEC 60079-5 | Transformers |
| o | Oil immersion | IEC 60079-6 | Switchgear |

## 6. Certification schemes

| Scheme | Scope | Recognition |
|--------|-------|-------------|
| ATEX | European Union | Mandatory for EU market |
| IECEx | International | Accepted in 55+ countries |
| UL (US) | United States | Required by NEC for listed equipment |
| CSA | Canada | Canadian market |

ATEX and IECEx certificates are mutually recognized in many countries. US installations using NEC Article 505 (Zone classification) can generally accept ATEX/IECEx certified equipment — verify with local AHJ.

## 7. Change log

- 2026-03-08 — Initial draft; marking system, EPL, gas groups, T-codes, protection methods overview.
```

**Step 2: Validate**

```bash
cd "." && python3 tools/validate_ai_boundaries.py 2>&1 | grep "iec_60079"
```
Expected: no output (no violations).

**Step 3: Commit**

```bash
git add "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_0__general_requirements.md"
git commit -m "feat(iec60079-rag): add Part 0 general requirements"
```

---

### Task 2: IEC 60079 — Part 1 (Flameproof Ex d)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_1__flameproof_Ex_d.md`

**Step 1: Create the file**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-1
EDITION: 2014

IEC_HIERARCHY:
  part: "1"
  part_title: "Explosive Atmospheres — Flameproof Enclosures (Ex d)"

INDEX_TAGS:
  topics: ["flameproof", "Ex_d", "enclosure", "flame_path", "cable_gland", "conduit_seal"]
  systems: ["process_control", "oil_gas", "motors", "junction_boxes"]
-->

# IEC 60079-1 — Explosive Atmospheres: Flameproof Enclosures (Ex d)

## 0. Why this matters for control engineers

Flameproof (Ex d) is the most common protection method for motors, solenoid valves, and large terminal boxes in Zone 1 locations. Unlike intrinsic safety which prevents ignition by limiting energy, Ex d allows an internal explosion to occur but contains it — the enclosure is designed to withstand the explosion and cool escaping gases below ignition temperature before they reach the surrounding atmosphere.

## 1. Principle of protection

The Ex d enclosure:
1. **Withstands** internal ignition — the enclosure does not rupture
2. **Quenches** escaping gases — flame paths (gaps at joints and cable entries) are long enough and tight enough to cool gases below their autoignition temperature
3. **Does not ignite** the external atmosphere — surface temperatures stay within the T-code limit

This means Ex d equipment **can** have internal sparking sources (switches, motors, terminals). The enclosure provides the protection, not the internal circuit design.

## 2. Flame path requirements

The flame path is the joint between mating surfaces of the enclosure. Key parameters:

| Parameter | Purpose |
|-----------|---------|
| Gap width (w) | Must not exceed maximum allowable for gas group |
| Flame path length (L) | Minimum length to quench the flame |
| Surface finish | Must be machined — no paint or sealant on flame path surfaces |

Maximum gaps vary by gas group: IIA allows wider gaps than IIC. IIC (hydrogen service) requires the tightest tolerances. **Never apply paint, thread sealant, or anti-seize to flame path surfaces** — this changes the effective gap.

## 3. Cable entry methods

All openings in an Ex d enclosure must be sealed. Three accepted methods:

| Method | Description | Notes |
|--------|-------------|-------|
| Ex d certified cable gland | Gland with integral flame path | Most common; gland must match cable type and enclosure gas group |
| Ex d stopping plug | Blanks unused entries | Must be certified; do not use standard plugs |
| Conduit with conduit sealing fitting | Threaded conduit + EYS/EYC seal filled with sealing compound | Required for NEC conduit systems in Division locations; not typical in IEC Zone installations |

## 4. Installation requirements

- **Do not open** energized Ex d equipment in a hazardous atmosphere — de-energize first and allow cooling if the equipment generates heat
- **Inspect flame paths** at every opening — replace if damaged, corroded, or out of tolerance
- **Fastener torque** — all cover fasteners must be fully engaged; missing fasteners invalidate the protection
- **Conduit drainage** — condensation in conduit must drain away from the Ex d enclosure, not into it
- **Breathing and draining devices** — use only Ex d certified versions

## 5. Common installation errors

- Over-torquing covers causes distortion of flame paths (Ex d enclosures are precision-machined)
- Applying thread compound to threaded flame path entries
- Using non-certified cable glands (standard industrial glands are not Ex d rated)
- Leaving unused entries with standard plugs instead of Ex d certified stopping plugs
- Adding field modifications (extra holes, larger openings) that are not on the certificate

## 6. Change log

- 2026-03-08 — Initial draft; Ex d principle, flame path requirements, cable entry methods, installation errors.
```

**Step 2: Commit**

```bash
git add "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_1__flameproof_Ex_d.md"
git commit -m "feat(iec60079-rag): add Part 1 flameproof Ex d"
```

---

### Task 3: IEC 60079 — Part 10-1 (Area Classification) and Part 11 (IS)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_10_1__area_classification_gas.md`
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_11__intrinsically_safe_Ex_i.md`

**Step 1: Create Part 10-1**

```markdown
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
```

**Step 2: Create Part 11**

```markdown
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
```

**Step 3: Commit both**

```bash
git add "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_10_1__area_classification_gas.md" \
        "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_11__intrinsically_safe_Ex_i.md"
git commit -m "feat(iec60079-rag): add Part 10-1 (area classification) and Part 11 (IS/Ex i)"
```

---

### Task 4: IEC 60079 — Part 14 (Installation) and Part 17 (Inspection)

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_14__installation_design.md`
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_17__inspection_maintenance.md`

**Step 1: Create Part 14**

```markdown
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
```

**Step 2: Create Part 17**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-17
EDITION: 2013

IEC_HIERARCHY:
  part: "17"
  part_title: "Explosive Atmospheres — Inspection and Maintenance of Electrical Installations"

INDEX_TAGS:
  topics: ["inspection", "maintenance", "periodic_inspection", "inspection_grade", "competency", "Ex_records"]
  systems: ["process_control", "oil_gas", "hazardous_area_maintenance"]
-->

# IEC 60079-17 — Explosive Atmospheres: Inspection and Maintenance

## 0. Why this matters for control engineers

Hazardous area equipment degrades over time — flame paths corrode, cable glands loosen, IS parameters drift, and equipment is modified without re-certification. IEC 60079-17 defines the inspection regime that keeps an Ex installation compliant between the initial commissioning inspection (IEC 60079-14) and decommissioning. Many insurance policies and regulatory frameworks require documented inspections per this standard.

## 1. Inspection grades

Three grades of inspection are defined, each with different scope:

| Grade | What is inspected | Typical frequency |
|-------|------------------|------------------|
| **Visual** | External condition — damage, corrosion, nameplate legible, glands tight, no obvious defects | More frequent (continuous or monthly) |
| **Close** | Visual checks + covers removed to verify flame path condition, IS parameters, internal connections | Less frequent (typically annually) |
| **Detailed** | Close checks + full verification against current certificate, entity recalculation, dimensional checks on flame paths | Infrequent (typically every 3–5 years or after incidents) |

The inspection schedule is risk-based: Zone 0/1 installations and equipment in severe environments warrant more frequent inspection.

## 2. Inspection procedure

For each item of Ex equipment:
1. Identify equipment type and protection method from nameplate
2. Refer to the appropriate inspection schedule for that protection method
3. Record findings against each inspection point
4. Classify defects as: no defect / defect not affecting safety / potential hazard / immediate hazard
5. Action defects appropriately (document, repair, or de-energize immediately)

## 3. Competency requirements

IEC 60079-17 requires that inspections be performed by a **competent person** — defined as having:
- Knowledge of the Ex protection concepts relevant to the equipment being inspected
- Knowledge of the applicable installation standards
- Practical experience with the protection methods present
- Understanding of the hazardous substances present

Documented training and qualification (e.g., CompEx, EEHA, or equivalent national scheme) satisfies the competency requirement in most jurisdictions.

## 4. Common inspection findings (defects)

| Defect | Classification | Action |
|--------|---------------|--------|
| Missing or loose cover fasteners (Ex d) | Potential hazard | Repair before next shift |
| Corroded flame path | Potential hazard / immediate hazard (if gap out of tolerance) | Remove from service if gap exceeds limit |
| Non-certified cable gland | Immediate hazard | Replace |
| Unsigned / missing inspection record | Documentation defect | Update records |
| Modified enclosure (extra holes) | Immediate hazard | Remove from service; re-certify or replace |
| IS earth resistance >1 Ω (zener barriers) | Potential hazard | Improve bonding |

## 5. Records

Inspection records must be retained and include:
- Date of inspection
- Inspector name and qualification
- Inspection grade applied
- Equipment identified (tag number, type, certificate number)
- Defects found and actions taken
- Next inspection due date

Records are required for regulatory audits, insurance inspections, and incident investigations. Loss of inspection records is treated as evidence that inspection did not occur.

## 6. Change log

- 2026-03-08 — Initial draft; inspection grades, procedure, competency, common defects, record requirements.
```

**Step 3: Commit both**

```bash
git add "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_14__installation_design.md" \
        "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_17__inspection_maintenance.md"
git commit -m "feat(iec60079-rag): add Part 14 (installation) and Part 17 (inspection)"
```

---

### Task 5: IEC 60079 — _index.yaml

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/_index.yaml`

**Step 1: Create the file**

```yaml
# IEC 60079 Hazardous Area RAG Index
# AI_READ_ACCESS: ALLOWED

version: "1.0"
standard_family: "IEC_60079"
standard_id: "IEC_60079"
standard_title: "Explosive Atmospheres"
edition: "Various (2011–2017)"
jurisdiction: "International"
last_updated: "2026-03-08"

documents:
  - doc_id: "IEC60079-0"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_0__general_requirements.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["equipment_marking", "EPL", "temperature_class", "gas_group", "ATEX", "IECEx"]
    priority: "high"

  - doc_id: "IEC60079-1"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_1__flameproof_Ex_d.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["flameproof", "Ex_d", "flame_path", "cable_gland"]
    priority: "high"

  - doc_id: "IEC60079-10-1"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_10_1__area_classification_gas.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["area_classification", "zone_0", "zone_1", "zone_2", "release_grade", "ventilation"]
    priority: "high"
    related_standards: ["NEC_Art505"]

  - doc_id: "IEC60079-11"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_11__intrinsically_safe_Ex_i.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["intrinsic_safety", "Ex_i", "zener_barrier", "galvanic_isolator", "entity_parameters", "FISCO"]
    priority: "high"
    related_standards: ["NEC_Art504"]

  - doc_id: "IEC60079-14"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_14__installation_design.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["installation_design", "cable_selection", "equipotential_bonding", "initial_inspection"]
    priority: "standard"

  - doc_id: "IEC60079-17"
    path: "rag/standards_intelligence/international/hazardous_area/iec_60079/IEC60079_17__inspection_maintenance.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["inspection", "periodic_inspection", "inspection_grade", "competency"]
    priority: "standard"

coverage_notes:
  complete: ["60079-0", "60079-1", "60079-10-1", "60079-11", "60079-14", "60079-17"]
  planned: ["60079-10-2", "60079-18", "60079-31"]

notes: |
  6 parts covering the core IEC 60079 series for control engineers:
  general requirements, flameproof (Ex d), area classification (gas),
  intrinsic safety (Ex i), installation design, and inspection/maintenance.
```

**Step 2: Validate**

```bash
cd "." && python3 tools/validate_ai_boundaries.py 2>&1 | grep -E "error|iec_60079" | head -10
```
Expected: no errors for iec_60079 files.

**Step 3: Commit**

```bash
git add "control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/_index.yaml"
git commit -m "feat(iec60079-rag): add _index.yaml (6 parts indexed)"
```

---

### Task 6: SEMI S2, S8, S14 RAG files

**Files:**
- Create: `control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S2__equipment_safety.md`
- Create: `control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S8__ergonomics.md`
- Create: `control-standards/rag/standards_intelligence/international/semiconductor/semi/SEMI_S14__fire_risk_assessment.md`
- Create: `control-standards/rag/standards_intelligence/international/semiconductor/semi/_index.yaml`

**Step 1: Create directory**

```bash
mkdir -p "control-standards/rag/standards_intelligence/international/semiconductor/semi"
```

**Step 2: Create SEMI_S2__equipment_safety.md**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S2
EDITION: S2-0200 (current revision)

INDEX_TAGS:
  topics: ["equipment_safety", "electrical_safety", "lockout_tagout", "chemical_safety", "emissions", "interlocks", "grounding"]
  systems: ["semiconductor_equipment", "process_equipment", "fab_equipment"]
-->

# SEMI S2 — Environmental, Health, and Safety Guideline for Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

SEMI S2 is the primary safety standard for semiconductor manufacturing equipment (tools). It covers the complete safety envelope: electrical, mechanical, chemical, radiation, and ergonomic hazards. For control engineers designing tool electrical systems, the electrical safety, interlock, grounding, and documentation sections are directly applicable. S2 compliance is required by most semiconductor fabs as a condition of equipment purchase.

## 1. Electrical safety requirements

### Grounding and bonding
- All conductive equipment surfaces accessible during operation must be grounded
- Ground continuity must be verified before each use if reconnected
- Equipotential bonding between all isolated conductive sections

### Isolation and lockout/tagout (LOTO)
- Equipment must provide means to isolate all energy sources (electrical, pneumatic, hydraulic)
- Lockout provisions: each energy isolation point must accept a padlock
- Stored energy: capacitors must discharge to <50 V within 5 seconds of isolation; or a discharge indicator and interlock must prevent access
- Tagout-only is not acceptable for primary energy isolation in most semiconductor fabs

### Overcurrent protection
- All circuits must be protected against overcurrent
- Branch circuit protection sized per the electrical code (NEC for US fabs)
- Ground fault protection required for circuits in wet/chemical environments

### High-voltage circuits (>50 V AC or >120 V DC)
- Must be enclosed and interlocked — access triggers interlock before opening
- Interlocks must de-energize before panels open; should not be defeatable without deliberate action
- Interlock bypass provisions must be labeled, limited to trained maintenance personnel, and self-resetting or requiring deliberate re-bypass

## 2. Interlock design requirements

S2 requires a risk assessment (typically per ISO 12100 or SEMI S10) to determine required interlock performance. Key requirements:

- Safety interlocks must be independent of the process control system where a single failure could cause injury
- Interlocks must fail to a safe state (de-energize, vent, or stop)
- Interlock status must be monitored — failures must be detected
- Manual reset required after safety interlock actuation (automatic restart prohibited for personnel safety interlocks)

## 3. Chemical and gas safety

Control engineers designing gas cabinet and chemical delivery control systems must address:
- Automatic shutoff valves (normally closed) on all toxic and flammable gas lines
- Pressure switches to detect line breaks and trigger automatic shutoff
- Exhaust flow monitoring — confirm exhaust is flowing before allowing process gas flow
- Gas detector integration — concentration alarms must trigger automatic shutoff and exhaust increase

## 4. Labeling and documentation

Required on every tool:
- Electrical service requirements (voltage, phases, frequency, current)
- Equipment grounding terminal identification
- Warning labels for all hazards (chemical, electrical, laser, RF, UV)
- Emergency stop location identification
- Lockout/tagout procedure posted or attached

Required documents shipped with tool:
- Electrical diagram (schematic)
- Safety interlock list and descriptions
- Hazardous materials inventory (chemicals, gases on tool)
- Installation and utilities requirements

## 5. Relationship to other standards

| Standard | Relationship |
|----------|-------------|
| IEC 60204-1 | International equivalent for machine electrical safety — S2 fabs often require both |
| ISO 12100 | Risk assessment methodology referenced by S2 |
| NFPA 79 | US electrical requirements for the tool — S2 fabs require NEC/NFPA 79 compliance |
| SEMI S14 | Fire risk assessment companion to S2 |
| SEMI S8 | Ergonomics companion to S2 |

## 6. Change log

- 2026-03-08 — Initial draft; electrical safety, LOTO, interlocks, chemical gas safety, labeling, related standards.
```

**Step 3: Create SEMI_S8__ergonomics.md**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S8
EDITION: S8-0706 (current revision)

INDEX_TAGS:
  topics: ["ergonomics", "human_factors", "maintenance_access", "control_placement", "force_limits", "reach_envelope"]
  systems: ["semiconductor_equipment", "fab_equipment"]
-->

# SEMI S8 — Safety Guideline for Ergonomics Engineering of Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

SEMI S8 defines ergonomics requirements for equipment that humans operate and maintain. For control engineers, the most relevant sections govern control placement, display design, and maintenance access — areas where the electrical/controls design directly affects human factors compliance. Non-compliance with S8 is a common reason for equipment rejection during fab qualification.

## 1. Control placement

- Primary controls (E-stop, operator panel) must be reachable without bending, stretching, or awkward postures
- E-stop buttons: no higher than 1,400 mm, no lower than 600 mm from the floor; reachable from normal operator position
- Displays: within the operator's normal visual field; no glare from facility lighting; text legible at normal operating distance
- Frequently used controls: within easy reach (forward reach ≤600 mm from operator's body)

## 2. Force and torque limits

Controls must be operable without excessive force:
- Pushbuttons and switches: actuation force ≤22 N (5 lb)
- Emergency stops: must be easy to actuate under stress — typically mushroom-head, ≤40 N maximum
- Panels and doors for maintenance: opening force ≤222 N (50 lb) for normally accessed panels

For maintenance tasks requiring tools, the torque required to remove fasteners should be within normal hand tool capability without extreme effort.

## 3. Maintenance access

- All field-replaceable items (components, consumables, filters) must be accessible without removing non-related assemblies
- Maintenance access must be achievable without entering confined spaces where hazardous energy is present
- Minimum clearance for maintenance access: 600 mm width, 900 mm height (for full-body access)
- Components requiring frequent access (>once per month): accessible without tools or with common tools only

## 4. Lifting and manual handling

- Single-person lifts within the equipment (replacing modules, loading wafers): ≤16 kg without mechanical assist
- Equipment that requires handling loads >16 kg must provide lifting aids (handles, hoists, carts)
- Consumable containers (chemicals, gases): sized and located for ergonomic handling

## 5. Vibration and noise

- Vibration transmitted to operators during normal use: within ACGIH/ISO 5349 hand-arm vibration limits
- Noise at operator position during normal operation: ≤80 dBA (time-weighted average 8-hour)
- Where noise exceeds 80 dBA, hearing protection requirement must be labeled on the equipment

## 6. Change log

- 2026-03-08 — Initial draft; control placement, force limits, maintenance access, lifting, vibration/noise.
```

**Step 4: Create SEMI_S14__fire_risk_assessment.md**

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S14
EDITION: S14-1110 (current revision)

INDEX_TAGS:
  topics: ["fire_risk_assessment", "flammability", "ignition_sources", "fire_suppression", "cleanroom_fire", "fab_safety"]
  systems: ["semiconductor_equipment", "fab_equipment", "process_equipment"]
-->

# SEMI S14 — Safety Guideline for Fire Risk Assessment and Fire Safety for Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

Semiconductor equipment uses flammable process gases, solvents, and chemicals in a cleanroom environment where fire suppression is complex and fire spread can be rapid. SEMI S14 requires a fire risk assessment for all equipment, and the control system design directly affects fire risk — gas shutoff interlocks, exhaust monitoring, and automatic fire response are control engineering deliverables.

## 1. Fire risk assessment process

The S14 fire risk assessment evaluates:
1. **Ignition sources** — electrical arcs, hot surfaces, static discharge, mechanical friction
2. **Fuel sources** — flammable gases, process chemicals, plastic components, wiring insulation
3. **Oxidizers** — oxygen from air, process oxygen, oxidizing gases
4. **Fire scenarios** — credible combinations of ignition, fuel, and oxidizer
5. **Mitigation measures** — controls, detection, suppression, separation

The assessment result determines the fire protection measures required for each identified scenario.

## 2. Material flammability classification

S14 classifies materials in the equipment by flammability:

| Class | Flammability | Examples | Controls Required |
|-------|-------------|---------|-----------------|
| Non-combustible | Cannot burn | Metals, ceramics | None |
| Limited combustibility | Will not propagate flame | Certain plastics (UL94 V-0) | Minimize mass |
| Combustible | Burns with difficulty | Many plastics | Fire detection + suppression consideration |
| Flammable | Burns readily | Solvents, some polymers | Substitution, isolation, suppression |
| Highly flammable | Burns with vigorous flame | Process gases, low-flash solvents | Substitution preferred; tight controls if unavoidable |

## 3. Ignition source control (controls engineering)

Control engineers must address these ignition sources in equipment design:

- **Electrical arcs:** Use arc-flash-rated enclosures for high-energy circuits; size overcurrent protection to limit arc duration
- **Hot surfaces:** Heater circuits must have over-temperature protection independent of the process controller — a separate thermocouple and hardwired high-temperature cutout
- **Static discharge:** Ground all conductive components; antistatic materials for plastic components near flammable materials
- **Motor overheating:** Motor overload protection must be sized and set correctly; thermal overload relays preferred over circuit breakers alone for continuous-duty motors in enclosed equipment

## 4. Fire detection and response

S14 requires automatic fire detection for equipment containing:
- Flammable or pyrophoric gases
- Flammable liquid volumes above defined thresholds
- Materials that, if on fire, could spread to adjacent equipment or the cleanroom

**Detection methods:** Point heat detectors, optical flame detectors, or aspirating smoke detectors depending on the enclosure environment.

**Automatic response sequence (example for flammable gas equipment):**
1. Fire detected → immediate closure of all flammable gas supply valves
2. Increase exhaust flow to maximum
3. Alert operator (audible + visual)
4. If suppression system present: initiate after delay (allow personnel evacuation)
5. Disable process restart until manual reset by qualified personnel

## 5. Cleanroom-specific considerations

- Cleanroom HVAC systems can spread fire products rapidly — equipment fire control must be self-contained where possible
- Water-based suppression is generally prohibited in cleanrooms (wafer damage, equipment damage, slip hazard)
- Clean agent systems (FM-200, Novec 1230, CO2 for some areas) are the standard approach
- Equipment with local suppression must coordinate with the facility-wide fire alarm and suppression systems

## 6. Change log

- 2026-03-08 — Initial draft; risk assessment process, material classification, ignition source control, fire detection/response, cleanroom considerations.
```

**Step 5: Create _index.yaml**

```yaml
# SEMI S2/S8/S14 RAG Index
# AI_READ_ACCESS: ALLOWED

version: "1.0"
standard_family: "SEMI"
standard_title: "SEMI Safety Guidelines"
jurisdiction: "International (semiconductor industry)"
last_updated: "2026-03-08"

documents:
  - doc_id: "SEMI-S2"
    path: "rag/standards_intelligence/international/semiconductor/semi/SEMI_S2__equipment_safety.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["equipment_safety", "electrical_safety", "lockout_tagout", "interlocks", "chemical_safety"]
    priority: "high"
    related_standards: ["IEC60204-1", "NFPA79", "ISO12100"]

  - doc_id: "SEMI-S8"
    path: "rag/standards_intelligence/international/semiconductor/semi/SEMI_S8__ergonomics.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["ergonomics", "human_factors", "maintenance_access", "control_placement"]
    priority: "standard"

  - doc_id: "SEMI-S14"
    path: "rag/standards_intelligence/international/semiconductor/semi/SEMI_S14__fire_risk_assessment.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    tags:
      topics: ["fire_risk", "flammability", "fire_detection", "cleanroom_fire", "suppression"]
    priority: "high"
    related_standards: ["ISO12100"]

coverage_notes:
  complete: ["S2", "S8", "S14"]
  planned: ["S6", "S22"]
```

**Step 6: Validate and commit**

```bash
cd "." && python3 tools/validate_ai_boundaries.py 2>&1 | grep -E "error|semi" | head -10
```
Expected: no errors.

```bash
git add "control-standards/rag/standards_intelligence/international/semiconductor/semi/"
git commit -m "feat(semi-rag): add SEMI S2 (equipment safety), S8 (ergonomics), S14 (fire risk), _index.yaml"
```

---

### Task 7: IEC 60079 site pages

**Files:**
- Create: `docs/standards/hazardous-area/index.md`
- Create: `docs/standards/hazardous-area/iec-60079/index.md`

**Step 1: Create family landing**

```markdown
---
layout: default
title: "Hazardous Area Standards"
description: "Electrical standards for explosive and hazardous atmospheres — IEC 60079, NEC Article 500–505."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Hazardous Area"
---

<div class="page-header">
  <span class="page-header__label">Standards Family</span>
  <h1>Hazardous Area Electrical Standards</h1>
</div>

Hazardous area standards govern electrical equipment and installations in locations where flammable gases, vapors, dusts, or fibers may be present. Two parallel systems exist — the IEC Zone system (international) and the NEC Class/Division system (US).

## Classification Systems

| System | Standard | Zones/Classes | Used In |
|--------|----------|--------------|---------|
| IEC Zone (gas) | IEC 60079-10-1 | Zone 0, 1, 2 | International, US Art. 505 |
| IEC Zone (dust) | IEC 60079-10-2 | Zone 20, 21, 22 | International |
| NEC Division (gas/dust) | NEC Art. 500–503 | Class I/II/III, Division 1/2 | US (traditional) |
| NEC Zone (IEC-aligned) | NEC Art. 505–506 | Zone 0/1/2, Zone 20/21/22 | US (IEC-aligned) |

Both systems are valid in the US. IEC Zone is preferred for projects using ATEX/IECEx certified equipment.

## Standards in This Family

| Standard | Scope | Corpus Status |
|----------|-------|--------------|
| [IEC 60079 (6 parts)]({{ '/standards/hazardous-area/iec-60079/' | relative_url }}) | Explosive atmosphere equipment and installation | <span class="badge badge--complete">Complete</span> |
| NEC Art. 500–505 | US hazardous location wiring | [See NEC page]({{ '/standards/us-electrical/nec/' | relative_url }}) |

---

<a href="{{ '/standards/' | relative_url }}" class="card__link">&larr; Standards explorer</a>
```

**Step 2: Create IEC 60079 standard page**

```markdown
---
layout: default
title: "IEC 60079 — Explosive Atmospheres"
description: "IEC 60079 series: equipment marking, protection methods (Ex d/i/e/p), area classification, installation, and inspection for hazardous areas."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Hazardous Area"
    url: "/standards/hazardous-area/"
  - name: "IEC 60079"
related_standards:
  - name: "NEC (Art. 500–505)"
    url: "/standards/us-electrical/nec/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
last_reviewed: "2026-03-08"
---

<div class="page-header">
  <span class="page-header__label">International · Hazardous Area</span>
  <h1>IEC 60079 — Explosive Atmospheres</h1>
</div>

<span class="badge badge--complete">Phase 10 Complete</span>

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | IEC 60079 series |
| **Publisher** | International Electrotechnical Commission (IEC) |
| **Scope** | Electrical equipment and installations in explosive atmospheres |
| **Corpus** | 6 parts — general requirements, Ex d, area classification, IS (Ex i), installation, inspection |

---

## Equipment Marking System

All Ex equipment carries a marking string. Example: **`Ex d IIB T4 Gb`**

| Element | Meaning |
|---------|---------|
| `Ex` | Certified for explosive atmospheres |
| `d` | Protection method: flameproof enclosure |
| `IIB` | Gas group: ethylene and similar (IIA < IIB < IIC) |
| `T4` | Max surface temperature: 135°C |
| `Gb` | Equipment Protection Level: Zone 1 |

**EPL → Zone mapping:**

| EPL | Zone | Protection level |
|-----|------|-----------------|
| Ga | Zone 0 | Highest — two independent faults |
| Gb | Zone 1 | High — one fault tolerance |
| Gc | Zone 2 | Enhanced — normal operation |

---

## Zone Classification

Zones are determined per **IEC 60079-10-1** based on release grade and ventilation:

| Zone | Condition |
|------|-----------|
| Zone 0 | Explosive atmosphere continuously present |
| Zone 1 | Explosive atmosphere likely in normal operation |
| Zone 2 | Explosive atmosphere unlikely; brief if present |

A classified area drawing documenting zone extents, gas groups, and T-codes is required.

---

## Protection Methods

| Method | Code | Standard | Zone | Principle |
|--------|------|----------|------|-----------|
| Flameproof enclosure | Ex d | IEC 60079-1 | 1, 2 | Contains internal explosion; quenches escaping gases |
| Intrinsic safety | Ex ia/ib/ic | IEC 60079-11 | 0/1/2 | Limits energy below ignition threshold |
| Increased safety | Ex e | IEC 60079-7 | 1, 2 | Prevents sparks and excess temperature |
| Purged/pressurized | Ex p | IEC 60079-2 | 1, 2 | Maintains positive pressure to exclude atmosphere |
| Encapsulation | Ex m | IEC 60079-18 | 1, 2 | Encapsulates components in compound |
| Non-sparking | Ex nA | IEC 60079-15 | 2 only | Cannot ignite in normal operation |

---

## Intrinsic Safety Quick Reference

IS is the standard approach for process instruments. Key points:

- **Zener barriers** — require IS earth ≤1 Ω; low cost; widely used
- **Galvanic isolators** — no IS earth required; provides isolation; use in floating systems
- **Entity check:** Uo ≤ Ui, Io ≤ Ii, Ci + Ccable ≤ Co, Li + Lcable ≤ Lo

---

## Relationship to NEC

| NEC Article | IEC 60079 Relationship |
|-------------|----------------------|
| Art. 500–503 | Class/Division system — parallel US approach |
| Art. 504 | IS system aligns with IEC 60079-11 |
| Art. 505 | Zone system directly references IEC 60079 equipment certification |

ATEX/IECEx certified equipment is generally accepted in NEC Art. 505 Zone installations — verify with AHJ.

---

## Installation and Inspection Checklist

- [ ] Area classification drawing current and signed
- [ ] Equipment EPL matches zone (Ga→Zone 0, Gb→Zone 1, Gc→Zone 2)
- [ ] Gas group rating ≥ hazardous substance group
- [ ] T-code max surface temp < substance autoignition temp (with margin)
- [ ] Certificate valid — check IECEx/ATEX database, not just nameplate
- [ ] Cable glands Ex-certified and correct type for enclosure and gas group
- [ ] IS earth resistance ≤1 Ω (for zener barrier installations)
- [ ] Entity parameters verified for all IS loops (Ci + Ccable ≤ Co, etc.)
- [ ] Equipotential bonding verified
- [ ] Inspection records current (IEC 60079-17 schedule)

---

<a href="{{ '/standards/hazardous-area/' | relative_url }}" class="card__link">&larr; Hazardous area family</a>
```

**Step 3: Verify build**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -3
```

**Step 4: Commit**

```bash
git add docs/standards/hazardous-area/
git commit -m "feat(site): add hazardous area family landing + IEC 60079 standard page"
```

---

### Task 8: SEMI site pages + update standards index and scenario page

**Files:**
- Create: `docs/standards/semiconductor/index.md`
- Create: `docs/standards/semiconductor/semi/index.md`
- Modify: `docs/standards/index.md`
- Modify: `docs/scenarios/semiconductor-equipment/index.md`

**Step 1: Create semiconductor family landing**

```markdown
---
layout: default
title: "Semiconductor Equipment Standards"
description: "Safety standards for semiconductor manufacturing equipment — SEMI S2, S8, S14."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Semiconductor"
---

<div class="page-header">
  <span class="page-header__label">Standards Family</span>
  <h1>Semiconductor Equipment Standards</h1>
</div>

Semiconductor manufacturing equipment (tools) operates in cleanroom environments with flammable process gases, hazardous chemicals, high voltages, and complex automated processes. The SEMI standards organization publishes safety guidelines specific to this environment.

## Standards in This Family

| Standard | Scope | Corpus Status |
|----------|-------|--------------|
| [SEMI S2/S8/S14]({{ '/standards/semiconductor/semi/' | relative_url }}) | Equipment safety, ergonomics, fire risk | <span class="badge badge--complete">Complete</span> |

---

<a href="{{ '/standards/' | relative_url }}" class="card__link">&larr; Standards explorer</a>
```

**Step 2: Create SEMI standard page**

```markdown
---
layout: default
title: "SEMI S2 / S8 / S14 — Semiconductor Equipment Safety"
description: "SEMI S2 (equipment safety), S8 (ergonomics), S14 (fire risk assessment) for semiconductor manufacturing equipment."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Semiconductor"
    url: "/standards/semiconductor/"
  - name: "SEMI S2/S8/S14"
related_standards:
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
last_reviewed: "2026-03-08"
---

<div class="page-header">
  <span class="page-header__label">International · Semiconductor</span>
  <h1>SEMI S2 / S8 / S14 — Semiconductor Equipment Safety</h1>
</div>

<span class="badge badge--complete">Phase 10 Complete</span>

## Standard Overview

| Standard | Scope |
|----------|-------|
| **SEMI S2** | Environmental, Health, and Safety Guideline for Semiconductor Manufacturing Equipment |
| **SEMI S8** | Ergonomics Engineering of Semiconductor Manufacturing Equipment |
| **SEMI S14** | Fire Risk Assessment and Fire Safety for Semiconductor Manufacturing Equipment |

These guidelines apply to equipment used in semiconductor manufacturing fabs. Compliance is required by most fab operators as a condition of equipment purchase and installation.

---

## SEMI S2 — Equipment Safety Highlights

### Electrical safety (control engineering relevance)

- All conductive surfaces accessible during operation must be grounded
- Interlocks must de-energize high-voltage circuits before panels open — not defeatable without deliberate action
- Interlocks must fail to a safe state; failures must be detected
- Stored energy (capacitors): discharge to <50 V within 5 seconds of isolation, or provide discharge indicator + access interlock
- Manual reset required after safety interlock actuation — no automatic restart

### Lockout/Tagout

- Every energy isolation point must accept a padlock
- Tagout-only is not acceptable for primary energy isolation
- Stored energy procedures required (pneumatic, hydraulic, capacitive)

### Gas and chemical control systems

- Normally-closed automatic shutoff valves on all toxic/flammable gas lines
- Exhaust flow monitoring before permitting process gas flow
- Gas detector integration with automatic shutoff and exhaust increase

---

## SEMI S8 — Ergonomics Key Points

| Requirement | Limit |
|-------------|-------|
| E-stop height | 600–1,400 mm from floor |
| Pushbutton actuation force | ≤22 N |
| E-stop actuation force | ≤40 N |
| Maintenance panel opening force | ≤222 N |
| Single-person lift limit | ≤16 kg |

---

## SEMI S14 — Fire Risk Assessment Key Points

- Risk assessment required for all equipment with flammable/pyrophoric gases or chemicals
- Automatic shutoff of all flammable gas supplies on fire detection
- Over-temperature protection for heater circuits independent of process controller
- Water suppression prohibited in cleanrooms — clean agent systems required
- Local suppression must interface with facility-wide fire alarm system

---

## Relationship to Other Standards

| Standard | Relationship |
|----------|-------------|
| IEC 60204-1 | International machine electrical safety — often required alongside S2 |
| NFPA 79 | US equivalent — required for US-market semiconductor equipment |
| ISO 12100 | Risk assessment methodology referenced by S2 and S14 |
| IEC 62443 | Cybersecurity — applicable to networked semiconductor equipment |

---

<a href="{{ '/standards/semiconductor/' | relative_url }}" class="card__link">&larr; Semiconductor family</a>
```

**Step 3: Update `docs/standards/index.md`**

Find the last standards family section in `docs/standards/index.md` and append two new sections:

```markdown
## Hazardous Area Standards

| Standard | Publisher | Scope | Status |
|----------|-----------|-------|--------|
| [IEC 60079 (6 parts)]({{ '/standards/hazardous-area/iec-60079/' | relative_url }}) | IEC | Explosive atmosphere equipment and installation | <span class="badge badge--complete">Complete</span> |

## Semiconductor Equipment Standards

| Standard | Publisher | Scope | Status |
|----------|-----------|-------|--------|
| [SEMI S2 / S8 / S14]({{ '/standards/semiconductor/semi/' | relative_url }}) | SEMI | Semiconductor equipment safety, ergonomics, fire risk | <span class="badge badge--complete">Complete</span> |
```

**Step 4: Update semiconductor scenario page**

In `docs/scenarios/semiconductor-equipment/index.md`, find the `related_standards` front matter and add:

```yaml
  - name: "SEMI S2/S8/S14"
    url: "/standards/semiconductor/semi/"
  - name: "IEC 60079"
    url: "/standards/hazardous-area/iec-60079/"
```

Also update the badge from `badge--gap` to `badge--complete` for SEMI if it's marked as a gap.

**Step 5: Verify build and page count**

```bash
cd "docs" && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```
Expected: clean build, page count increases by 4.

**Step 6: Commit**

```bash
git add docs/standards/semiconductor/ docs/standards/index.md docs/scenarios/semiconductor-equipment/index.md
git commit -m "feat(site): add semiconductor family + SEMI S2/S8/S14 page; update standards index and scenario"
```

---

### Task 9: Validation and project state update

**Step 1: Run full validation**

```bash
cd "." && python3 tools/validate_ai_boundaries.py 2>&1 | tail -5
```
Expected: no new violations in iec_60079 or semi files. (Pre-existing IEC 62443 violations are unrelated.)

**Step 2: Count new files**

```bash
ls control-standards/rag/standards_intelligence/international/hazardous_area/iec_60079/ | wc -l
ls control-standards/rag/standards_intelligence/international/semiconductor/semi/ | wc -l
```
Expected: 7 (6 RAG files + _index.yaml) and 4 (3 RAG files + _index.yaml).

**Step 3: Update project_state.md** — add Phase 10 as COMPLETE:

```markdown
## Phase 10 Scope — Corpus Gap-Fill (IEC 60079 + SEMI S2/S8/S14) — COMPLETE

### IEC 60079 RAG Corpus
- [x] IEC60079_0__general_requirements.md
- [x] IEC60079_1__flameproof_Ex_d.md
- [x] IEC60079_10_1__area_classification_gas.md
- [x] IEC60079_11__intrinsically_safe_Ex_i.md
- [x] IEC60079_14__installation_design.md
- [x] IEC60079_17__inspection_maintenance.md
- [x] _index.yaml

### SEMI RAG Corpus
- [x] SEMI_S2__equipment_safety.md
- [x] SEMI_S8__ergonomics.md
- [x] SEMI_S14__fire_risk_assessment.md
- [x] _index.yaml

### Site Pages
- [x] docs/standards/hazardous-area/index.md
- [x] docs/standards/hazardous-area/iec-60079/index.md
- [x] docs/standards/semiconductor/index.md
- [x] docs/standards/semiconductor/semi/index.md
- [x] docs/standards/index.md updated (2 new families)
- [x] docs/scenarios/semiconductor-equipment/index.md updated
```

**Step 4: Add change_log.md entry and push**

```bash
git add project_state/ && git commit -m "chore(state): mark Phase 10 complete — IEC 60079 + SEMI corpus and site pages" && git push
```
