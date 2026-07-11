# NEC Missing Articles Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add 8 missing NEC 2023 article files to the RAG corpus covering scope/definitions, hazardous locations, intrinsically safe systems, feeders, services, and emergency/standby systems.

**Architecture:** Each new file follows the exact template of existing articles: HTML comment metadata block + numbered Markdown sections + change log. All content is paraphrased guidance — no verbatim NEC text. After all articles are created, `_index.yaml` and `NEC_COMPLETION_STATUS.md` are updated.

**Tech Stack:** Markdown, YAML front matter, Jekyll 4.2 (site layer only — RAG files are not Jekyll pages).

---

### Task 1: Create Art 90 + Art 100 (Scope and Definitions)

**Files:**
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art090__scope_and_purpose.md`
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art100__definitions.md`

**Step 1: Create Art 90 file**

Write the following content exactly to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art090__scope_and_purpose.md`:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "90"
  article_title: "Introduction — Scope and Purpose"

INDEX_TAGS:
  topics: ["scope", "purpose", "ahj", "adoption", "enforcement"]
  systems: ["all"]
-->

# NEC 2023 — Article 90 — Introduction: Scope and Purpose

## 0. Why this article matters for control engineers

Article 90 defines the legal and jurisdictional framework within which all other NEC articles operate. Understanding its boundaries prevents a common engineering error: applying NEC rules to wiring that is outside its scope (e.g., internal machine wiring governed by NFPA 79) or assuming NEC applies uniformly everywhere (it requires local adoption).

## 1. Purpose and legal status (90.1)

The NEC is a **minimum safety standard**, not a design guide or optimization document. Its purpose is the practical safeguarding of persons and property from hazards arising from the use of electricity. Key points:

- It is a **private standard** published by NFPA, not federal law.
- It becomes legally enforceable only when **adopted by a local AHJ** (city, county, state). Most US jurisdictions adopt a version of the NEC, but editions vary — some jurisdictions use NEC 2017 or 2020 rather than 2023.
- Compliance with NEC does not guarantee a system is efficient, convenient, or adequate for good service. Meeting NEC minimums is the floor, not the ceiling.

## 2. Scope — what NEC covers (90.2(a))

NEC applies to **premises wiring** — electrical conductors, equipment, and raceways installed in or on buildings, structures, or other premises. This includes:

- Industrial facilities, commercial buildings, and residences
- Yards, parking lots, and carnivals
- Mobile homes, recreational vehicles, and floating buildings
- Electric vehicle charging infrastructure

For control engineers: NEC governs the **facility wiring that supplies power to machines** — service entrance, feeders, branch circuits, and the point of connection to the machine.

## 3. What NEC does NOT cover (90.2(b))

The following are explicitly outside NEC scope:

| Excluded Area | Governing Authority |
|---------------|-------------------|
| Utility supply lines (transmission, distribution) | NESC (ANSI C2) |
| Internal wiring of listed factory-assembled equipment | Equipment listing standard (e.g., UL 508A) |
| Wiring in mines | MSHA regulations |
| Ships, watercraft, railway rolling stock | ABYC / FRA standards |
| Internal wiring of industrial machines | NFPA 79 (not NEC) |

**Critical boundary for machine builders:** NFPA 79 governs the electrical equipment on or inside the machine itself. NEC governs the supply wiring from the facility up to the machine's supply terminal (the point of connection defined in Article 670). The machine's main disconnect and supply conductors straddle this boundary.

## 4. AHJ authority (90.4)

The Authority Having Jurisdiction (AHJ) has the final word on:

- Approving equipment, materials, and installations
- Granting special permission for alternative methods
- Requiring safety measures beyond NEC minimums

**Practical implication:** Even if your installation strictly follows NEC, an AHJ can require additional measures. Engage the local AHJ early on non-standard installations, large projects, and anything involving unusual equipment or occupancies.

## 5. Enforcement and inspection

- AHJs typically issue permits before work begins and conduct inspections before energization.
- Non-compliant installations result in failed inspections, required corrections, and delay.
- Listed equipment (UL, ETL, CSA, etc.) is presumed compliant with NEC construction requirements; the AHJ verifies installation compliance.

## 6. Change log

- 2026-03-08 — Initial draft created; established NEC/NFPA 79 scope boundary.
```

**Step 2: Create Art 100 file**

Write the following content exactly to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art100__definitions.md`:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "100"
  article_title: "Definitions"

INDEX_TAGS:
  topics: ["definitions", "terminology", "ahj", "sccr", "listed", "grounding"]
  systems: ["all"]
-->

# NEC 2023 — Article 100 — Definitions

## 0. Why definitions matter

NEC uses precise technical language. Using a term incorrectly leads to misapplied requirements. This file covers definitions most relevant to industrial control panel design and machine installation. All definitions are paraphrased — consult the NEC 2023 official text for exact language.

## 1. Authority and approval

**Authority Having Jurisdiction (AHJ):** The organization, office, or person responsible for enforcing a standard, or their designated representative. In practice: the local electrical inspector, fire marshal, or third-party inspection agency. The AHJ has final approval authority.

**Approved:** Acceptable to the AHJ.

**Listed:** Equipment, materials, or services included in a list published by a nationally recognized testing laboratory (NRTL — e.g., UL, ETL/Intertek, CSA). Listing implies evaluation against an applicable product standard. For industrial control panels, listing to UL 508A satisfies NEC Article 409 requirements.

**Labeled:** Equipment to which a label, symbol, or identifying mark has been affixed by an NRTL. Distinct from listed in some contexts; an item can be labeled but the listing scope matters.

## 2. Circuit types

**Branch Circuit:** The conductors between the last overcurrent protective device and the outlets. In a control panel context: the circuit from the branch circuit breaker to a motor starter, drive, or other load.

**Feeder:** Conductors between the service equipment (or a separately derived system) and the final branch circuit overcurrent device. In a facility: the cable from the main switchgear to a sub-panel or MCC.

**Service:** The conductors and equipment that deliver energy from the serving utility to the premises wiring system. The service ends at the service disconnecting means.

**Separately Derived System:** A premises wiring system whose power is derived from a source of electrical energy having no direct connection to supply circuit conductors other than those established by grounding. Common example: isolation transformer secondary, generator.

## 3. Grounding and bonding

**Ground:** A conducting connection, intentional or accidental, between an electrical circuit/equipment and earth, or to some conducting body that serves in place of earth.

**Grounded (Grounding):** Connected to ground or to a conductive body that extends the ground connection.

**Grounded Conductor:** A system or circuit conductor that is intentionally grounded. In US systems: the neutral conductor.

**Equipment Grounding Conductor (EGC):** The conductive path that provides a fault-current return path and ensures equipment exposed metal parts remain at ground potential. The green wire (or bare wire) in a cable assembly.

**Bonding (Bonded):** Connected to establish electrical continuity and conductivity. Bonding ensures metal parts that could become energized are at the same potential.

**Bonding Jumper:** A conductor or device ensuring required electrical conductivity between metal parts required to be electrically connected.

**Ground Fault:** An unintentional, electrically conducting connection between an ungrounded conductor and normally non-current-carrying conductors, metallic enclosures, metallic raceways, or earth.

## 4. Equipment and installations

**Controller:** A device or group of devices that serves to govern, in some predetermined manner, the electric power delivered to the apparatus to which it is connected. Broader than just a motor starter.

**Disconnecting Means:** A device or group of devices by which the conductors of a circuit can be disconnected from their source of supply.

**Industrial Control Panel (ICP):** An assembly of two or more components consisting of one of the following: (1) power circuit components only, such as motor controllers, overload relays, fused disconnect switches, and circuit breakers; (2) control circuit components only, such as push buttons, pilot lights, selector switches, timers, switches, and control relays; or (3) a combination of power and control circuit components with associated wiring, terminal blocks, pilot devices, and similar components. [See also Art. 409]

**Motor Control Center (MCC):** An assembly of one or more enclosed sections each having a common power bus and primarily containing motor control units. A specialized form of industrial control panel.

**Panelboard:** A single panel or group of panel units designed for assembly in the form of a single panel, including buses and with or without switches and OCPDs for the control of light, heat, or power circuits. Governed by Art. 408.

**Switchboard:** A large single panel, frame, or assembly of panels with switches, buses, instruments, overcurrent devices, and other equipment. Generally accessible from the rear as well as front. Governed by Art. 408.

**Switchgear:** An assembly completely enclosed on all sides and top with sheet metal. More robust than a switchboard; typically rated for higher available fault current.

**Utilization Equipment:** Equipment that uses electric energy for electronic, electromechanical, chemical, heating, lighting, or similar purposes.

## 5. Electrical properties

**Ampacity:** The maximum current a conductor can carry continuously under defined conditions without exceeding its temperature rating.

**Continuous Load:** A load where the maximum current is expected to continue for 3 hours or more. OCPDs and conductors must be sized at 125% of the continuous load.

**Overcurrent:** Current in excess of the rated current of equipment or the ampacity of a conductor. May result from overload, short circuit, or ground fault.

**Short-Circuit Current Rating (SCCR):** The prospective symmetrical fault current at a nominal voltage that the equipment can withstand. Must be marked on industrial control panels per Art. 409.110.

**Voltage to Ground:** For grounded circuits: voltage between the given conductor and the grounded conductor or point. For ungrounded circuits: voltage between the given conductor and any other conductor.

## 6. Locations and wiring environments

**Exposed (as applied to wiring methods):** On or attached to the surface, or behind panels designed to allow access.

**Concealed:** Rendered inaccessible by the structure or finish of the building.

**Wet Location:** An installation where water or other liquids may drip, splash, or flow on the wiring. Outdoor locations and locations subject to saturation with water.

**Damp Location:** A location protected from weather but subject to moderate moisture — partially protected outdoor locations, unheated spaces, cold-storage rooms.

**Dry Location:** Not normally subject to dampness or wetness.

**Raceway:** An enclosed channel of metallic or nonmetallic materials designed for holding wires, cables, or bus bars. Includes conduit, cable tray, wireway.

## 7. Change log

- 2026-03-08 — Initial draft created; focused on terms most relevant to industrial control panel design and machine installation.
```

**Step 3: Verify both files exist**

```bash
ls "control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art090__scope_and_purpose.md" && \
ls "control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art100__definitions.md"
```
Expected: both paths listed without error.

**Step 4: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art090__scope_and_purpose.md \
        control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art100__definitions.md
git commit -m "feat(nec-rag): add Art 90 (scope) and Art 100 (definitions) to corpus"
```

---

### Task 2: Create Art 500 + Art 504 (Hazardous Locations)

**Files:**
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art500__hazardous_locations_general.md`
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art504__intrinsically_safe_systems.md`

**Step 1: Create Art 500 file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art500__hazardous_locations_general.md`:

```markdown
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

## 5. Protection methods for Class I, Division 1

Equipment in the most hazardous locations must use one or more of these protection methods:

| Method | NEC Term | Principle |
|--------|----------|-----------|
| Explosion-proof | XP | Enclosure contains explosion; cools gases before release |
| Intrinsically safe | IS | Circuit energy too low to ignite (see Art. 504) |
| Purged/Pressurized | PX/PY/PZ | Maintains inert gas positive pressure inside enclosure |
| Non-incendive | NI | Circuit/equipment cannot ignite under normal conditions (Div. 2 only) |

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

The Zone classification system (Art. 505/506) aligns directly with IEC 60079. Equipment marked with ATEX or IECEx certification can be used in Zone-classified areas. Zone 0 ≈ Division 1 most hazardous; Zone 1 ≈ Division 1; Zone 2 ≈ Division 2. The mapping is approximate; always verify with the area classification drawing.

## 8. Change log

- 2026-03-08 — Initial draft; established Class/Division/Group/T-code framework with IEC 60079 bridge.
```

**Step 2: Create Art 504 file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art504__intrinsically_safe_systems.md`:

```markdown
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
```

**Step 3: Verify both files exist**

```bash
ls control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art500__hazardous_locations_general.md && \
ls control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art504__intrinsically_safe_systems.md
```

**Step 4: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art500__hazardous_locations_general.md \
        control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art504__intrinsically_safe_systems.md
git commit -m "feat(nec-rag): add Art 500 (hazardous locations) and Art 504 (IS systems)"
```

---

### Task 3: Create Art 505 (Zone Classification — IEC Bridge)

**Files:**
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art505__zone_0_1_2_gas_vapors.md`

**Step 1: Create the file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art505__zone_0_1_2_gas_vapors.md`:

```markdown
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
```

**Step 2: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art505__zone_0_1_2_gas_vapors.md
git commit -m "feat(nec-rag): add Art 505 (Zone 0/1/2 — IEC-aligned hazardous locations)"
```

---

### Task 4: Create Art 215 + Art 230 (Feeders and Services)

**Files:**
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art215__feeders.md`
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art230__services.md`

**Step 1: Create Art 215 file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art215__feeders.md`:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "215"
  article_title: "Feeders"

INDEX_TAGS:
  topics: ["feeders", "conductor_sizing", "overcurrent_protection", "continuous_load", "demand_factor"]
  systems: ["power_distribution", "industrial_control_panel", "MCC"]
-->

# NEC 2023 — Article 215 — Feeders

## 0. Why this article matters

Feeders are the conductors between the service equipment (or separately derived system) and the branch circuit overcurrent devices. In an industrial facility, feeders typically run from the main switchgear or MCC to sub-panels, motor control centers, or individual large loads. Understanding feeder sizing rules is essential for specifying the conductors supplying a control panel or MCC.

## 1. Feeder conductor sizing (215.2)

Feeder conductors must have ampacity not less than the **load calculated per Article 220**, and in no case less than:

- **Non-continuous loads:** 100% of the non-continuous load
- **Continuous loads:** 125% of the continuous load (load on for 3 hours or more)
- **Combined loads:** 125% of continuous + 100% of non-continuous loads

**Practical rule:** For a feeder supplying industrial loads, most loads are continuous. Size the feeder conductors at 125% of the calculated load, then check that the ampacity (from NEC Table 310.12 or 310.15) supports that value at the conductor's temperature rating.

## 2. Feeder overcurrent protection (215.3)

The feeder overcurrent protective device (OCPD — breaker or fuse) must not exceed:

- The **ampacity of the feeder conductors** (from Art. 310)
- Where the load includes motors, apply the maximum OCPD rating per Art. 430, Part IV, to the largest motor, then add the FLA of all other motors plus the non-motor loads

**Note on continuous loads:** Where 100% rated OCPDs are used, the device may be rated at 100% of the continuous load. Standard OCPDs (not marked "100% rated") must be sized so that the continuous load does not exceed 80% of the OCPD rating.

## 3. Feeder for multiple branch circuits (215.2(A))

A feeder supplying multiple branch circuits must have ampacity sufficient for:
- All branch circuit loads simultaneously
- Or the calculated demand load using applicable demand factors from Art. 220

**Demand factors:** Article 220 permits demand factors for certain load types (e.g., lighting in dwelling units, electric dryers). For industrial motor loads, demand factors are not typically applied unless a documented load study justifies a reduced design load.

## 4. Feeder identification (215.12)

Feeders must be identified at each point where they enter an enclosure. The identification must include the origin (e.g., "Panel A, Circuit 12") to allow safe disconnection during maintenance.

## 5. Relationship to Art. 230 and Art. 409

```
Service (Art. 230)
    ↓ Service conductors
Service Disconnecting Means
    ↓ Feeder (Art. 215)
Panelboard / MCC / Sub-panel
    ↓ Branch circuits (Art. 210)
Industrial Control Panel (Art. 409)
```

The feeder is the link between the service equipment and the panel or MCC that contains the branch circuit OCPDs. For machine installations, Article 670 governs from the feeder connection point to the machine.

## 6. Change log

- 2026-03-08 — Initial draft; feeder sizing, continuous load rule, relationship to service and branch circuits.
```

**Step 2: Create Art 230 file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art230__services.md`:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "230"
  article_title: "Services"

INDEX_TAGS:
  topics: ["service_entrance", "service_disconnect", "service_conductors", "available_fault_current", "SCCR"]
  systems: ["power_distribution", "industrial_facility"]
-->

# NEC 2023 — Article 230 — Services

## 0. Why this article matters for control engineers

The service is the origin of all facility wiring. Its characteristics — especially the **available fault current** — determine the SCCR requirements for every panel, MCC, and piece of equipment downstream. Control engineers must understand the service to correctly verify that panel SCCR ratings (Art. 409) are adequate for the installation.

## 1. Service components

A complete service installation includes:

| Component | Description |
|-----------|-------------|
| Service drop / lateral | Utility conductors from the utility grid to the service entrance |
| Service entrance conductors | Conductors from the service point to the service equipment |
| Service equipment | The main disconnect and OCPDs at the service entrance point |
| Metering equipment | Utility revenue meters (utility-owned) |

**Service point:** The junction between the utility facilities and the premises wiring. This is where NEC authority begins. Everything on the utility side of the service point is outside NEC scope.

## 2. Service disconnecting means (230.70, 230.71)

Every service must have a means to disconnect all ungrounded service conductors. Requirements:

- Located at a readily accessible location — nearest the point of entrance, on the exterior or interior of the building
- Cannot be in bathrooms
- Must be clearly marked to identify it as the service disconnect
- **Maximum six disconnects per service** — a single service may have up to six service disconnecting means (six-disconnect rule)

**Industrial facilities** typically use a single main switchgear or main breaker to satisfy the service disconnect requirement, with all downstream distribution originating from that point.

## 3. Available fault current and SCCR (230.67 reference, 110.24)

**Available fault current** at the service entrance is determined by the utility transformer impedance, conductor impedance, and system configuration. Facilities must:

1. Determine the available fault current at the service point (typically from the utility)
2. Verify all service equipment is rated for that available fault current
3. Document the available fault current at the service disconnecting means per NEC 110.24
4. Ensure all downstream equipment (panels, MCCs, drives) has SCCR ≥ available fault current at their installation point

**Typical industrial values:**
- Small commercial/industrial facilities: 10–25 kA available at service
- Large industrial facilities: 42–100 kA or higher at the service point

Available fault current decreases downstream as conductor impedance increases. This is why SCCR requirements for a panel in a remote building are lower than for a panel directly at the main switchgear.

## 4. Service conductor sizing (230.42)

Service entrance conductors must have ampacity not less than the load determined per Art. 220. They are sized similarly to feeders but are not protected from overcurrent at their supply end (the utility connection). Protection is provided by the service equipment OCPD.

## 5. Grounding at the service (250.24)

The neutral conductor is grounded at the service equipment — the **neutral-to-ground bond**. This bond occurs **only at the service**. Downstream panels and separately derived systems must NOT have a neutral-to-ground bond (they connect only the EGC to ground). Creating a second neutral-to-ground bond downstream creates a parallel ground path, causes nuisance breaker trips, and creates safety hazards.

## 6. Change log

- 2026-03-08 — Initial draft; service components, available fault current, neutral-to-ground bond rule.
```

**Step 3: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art215__feeders.md \
        control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art230__services.md
git commit -m "feat(nec-rag): add Art 215 (feeders) and Art 230 (services)"
```

---

### Task 5: Create Art 700–702 (Emergency and Standby Systems)

**Files:**
- Create: `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art700_702__emergency_standby_systems.md`

**Step 1: Create the file**

Write the following content to `control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art700_702__emergency_standby_systems.md`:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "700"
  article_title: "Emergency Systems / Legally Required Standby / Optional Standby"

INDEX_TAGS:
  topics: ["emergency_systems", "standby_power", "transfer_switch", "generator", "UPS", "safety_systems"]
  systems: ["emergency_lighting", "fire_alarm", "safety_PLC", "process_safety"]
-->

# NEC 2023 — Articles 700–702 — Emergency and Standby Systems

## 0. Why these articles matter for control engineers

Safety PLCs, emergency ventilation, fire suppression controls, and process shutdown systems often require power that remains available during a utility outage. Articles 700–702 define three tiers of backup power with different requirements for transfer time, testing, and supervision. Control engineers must identify which tier applies to their system to specify the correct power infrastructure.

## 1. Three-tier system overview

| Article | System Type | Authority Requiring It | Examples |
|---------|-------------|----------------------|---------|
| **700** | Emergency Systems | Government code (legally required) | Egress lighting, exit signs, fire alarm power, elevator recall |
| **701** | Legally Required Standby | Government code (legally required) | HVAC for occupied spaces, sewage disposal, industrial processes required by law |
| **702** | Optional Standby | Owner's choice (not legally required) | Data center UPS, production continuity, SCADA backup power |

## 2. Article 700 — Emergency Systems

**Transfer time:** Emergency systems must transfer to backup supply within **10 seconds** of normal power loss (700.12).

**Acceptable power sources (700.12):**
- Storage batteries (with automatic charger)
- Generator (10-second requirement is a challenge; most generators take 10–15s to reach rated voltage)
- UPS — satisfies 10-second requirement and provides seamless transfer
- Separate service from the utility (where the utility can guarantee independence)

**Wiring requirements:**
- Emergency wiring must be kept **entirely independent** of all other wiring. No shared conduit, enclosures, or junction boxes with normal or standby wiring.
- Exception: Transfer switches and exit fixtures where the emergency wiring terminates.

**Testing:** Emergency systems require:
- Monthly functional tests
- Annual 90-minute full-load tests
- Written records of all tests kept by the owner

**Relevance to control systems:** Fire alarm panels, emergency egress lighting, and life safety systems fall under Art. 700. Their power supplies, conduit, and panel sections must be segregated from the normal power system.

## 3. Article 701 — Legally Required Standby Systems

**Transfer time:** Within **60 seconds** of normal power loss (less stringent than Art. 700).

**Acceptable power sources:** Same as Art. 700. Generators can typically meet the 60-second requirement with proper sequencing controls.

**Wiring:** May share wiring infrastructure with normal systems in some conditions (less strict separation than Art. 700), but must be identified.

**Applications in industrial control:**
- Sewage lift station controls required by environmental permit
- Ventilation for occupied industrial spaces
- Process systems where legal or permit requirements mandate continuity

## 4. Article 702 — Optional Standby Systems

**Transfer time:** No specific requirement; owner determines acceptable outage duration.

**Applications in industrial control:**
- SCADA server power backup
- PLC rack power supply redundancy
- Continuous process systems where production loss (not safety) is the concern
- Data logging and historian systems

**Design note:** Many industrial facilities use Art. 702 UPS systems for control system power, plus Art. 700/701 for legally required systems. The UPS provides seamless transfer for control system continuity; the generator provides extended backup capacity for the UPS and for Art. 700/701 loads after UPS battery depletion.

## 5. Transfer switches

**Automatic Transfer Switch (ATS):** Senses loss of normal power and automatically transfers loads to backup supply. Required for Art. 700 and 701 systems.

**Manual Transfer Switch:** Operator-initiated transfer. Permitted only for Art. 702 (optional standby).

**Transfer switch ratings:**
- Must be rated for the connected load
- Must be rated for available fault current at the installation point
- ATS must indicate the power source currently supplying the load

**Bypass-Isolation Transfer Switch:** Allows maintenance on the ATS while loads remain powered through a bypass path. Recommended for critical industrial applications.

## 6. Safety system power — relevance to functional safety

For safety PLCs and SIL-rated safety instrumented systems:

- Power supply redundancy is often a requirement of the safety lifecycle (IEC 61511)
- The power source classification (Art. 700, 701, or 702) must match the demand of the safety function
- A SIL 2 or SIL 3 safety system requiring power during emergency shutdown may need Art. 700 or 701 power infrastructure
- UPS systems must have sufficient battery runtime to cover the required safe state duration

Coordinate the electrical power architecture (Art. 700–702) with the functional safety architecture (IEC 61511 / ISO 13849) during the design phase.

## 7. Change log

- 2026-03-08 — Initial draft; three-tier structure, transfer time requirements, safety system power coordination.
```

**Step 2: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art700_702__emergency_standby_systems.md
git commit -m "feat(nec-rag): add Art 700-702 (emergency and standby systems)"
```

---

### Task 6: Update _index.yaml, NEC_COMPLETION_STATUS.md, and NEC_OVERVIEW.md

**Files:**
- Modify: `control-standards/rag/standards_intelligence/us/nec/_index.yaml`
- Modify: `control-standards/rag/standards_intelligence/us/nec/NEC_COMPLETION_STATUS.md`
- Modify: `control-standards/rag/standards_intelligence/us/nec/NEC_OVERVIEW.md`

**Step 1: Append new entries to `_index.yaml`**

Read the current `_index.yaml` to find the last entry, then append the following 8 new document entries after the last existing entry (before any trailing content):

```yaml
  - doc_id: "NEC2023-Art090"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art090__scope_and_purpose.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "90"
      article_title: "Introduction — Scope and Purpose"
    tags:
      topics: ["scope", "purpose", "ahj", "adoption"]
      systems: ["all"]
    priority: "high"

  - doc_id: "NEC2023-Art100"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art100__definitions.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "100"
      article_title: "Definitions"
    tags:
      topics: ["definitions", "terminology", "sccr", "listed", "grounding"]
      systems: ["all"]
    priority: "high"

  - doc_id: "NEC2023-Art215"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art215__feeders.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "215"
      article_title: "Feeders"
    tags:
      topics: ["feeders", "conductor_sizing", "continuous_load"]
      systems: ["power_distribution", "industrial_control_panel"]
    priority: "standard"

  - doc_id: "NEC2023-Art230"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art230__services.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "230"
      article_title: "Services"
    tags:
      topics: ["service_entrance", "available_fault_current", "sccr"]
      systems: ["power_distribution", "industrial_facility"]
    priority: "standard"

  - doc_id: "NEC2023-Art500"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art500__hazardous_locations_general.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "500"
      article_title: "Hazardous Locations — General"
    tags:
      topics: ["hazardous_locations", "class_I", "class_II", "division_1", "division_2", "explosion_proof"]
      systems: ["process_control", "oil_gas", "chemical"]
    priority: "high"

  - doc_id: "NEC2023-Art504"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art504__intrinsically_safe_systems.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "504"
      article_title: "Intrinsically Safe Systems"
    tags:
      topics: ["intrinsically_safe", "IS", "zener_barrier", "galvanic_isolator", "FISCO"]
      systems: ["process_control", "instrumentation", "oil_gas"]
    priority: "high"
    related_standards: ["IEC60079-11"]

  - doc_id: "NEC2023-Art505"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art505__zone_0_1_2_gas_vapors.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "505"
      article_title: "Zone 0, 1, and 2 Locations"
    tags:
      topics: ["zone_0", "zone_1", "zone_2", "IEC_60079", "ATEX", "IECEx"]
      systems: ["process_control", "oil_gas"]
    priority: "standard"
    related_standards: ["IEC60079-0", "IEC60079-11"]

  - doc_id: "NEC2023-Art700-702"
    path: "rag/standards_intelligence/us/nec/NEC_2023__Art700_702__emergency_standby_systems.md"
    content_class: "RAG_APPROVED"
    ai_read_access: "ALLOWED"
    nec_hierarchy:
      article: "700"
      article_title: "Emergency / Legally Required Standby / Optional Standby Systems"
    tags:
      topics: ["emergency_systems", "standby_power", "transfer_switch", "UPS", "generator"]
      systems: ["safety_systems", "process_safety", "fire_alarm"]
    priority: "standard"
    related_standards: ["IEC61511", "ISO13849"]
```

**Step 2: Update `NEC_COMPLETION_STATUS.md`**

Update the "Executive Summary" and totals section to reflect 18 articles (10 original + 8 new). Change the total article count from 10 to 18, add a new table row for each new article, and update the "Last Updated" date to 2026-03-08.

**Step 3: Update `NEC_OVERVIEW.md`**

In the "Planned (Not Yet Created)" section, update it to reflect that Art 500/504/505 are now created, and add the new articles to the Article Index table under appropriate sections.

**Step 4: Run validation tool**

```bash
cd "." && python3 tools/validate_ai_boundaries.py 2>&1 | tail -10
```
Expected: no errors in the new files.

**Step 5: Commit**

```bash
git add control-standards/rag/standards_intelligence/us/nec/_index.yaml \
        control-standards/rag/standards_intelligence/us/nec/NEC_COMPLETION_STATUS.md \
        control-standards/rag/standards_intelligence/us/nec/NEC_OVERVIEW.md
git commit -m "feat(nec-rag): update index and status for 8 new articles (18 total)"
```

---

## Verification

After all tasks complete:

```bash
ls control-standards/rag/standards_intelligence/us/nec/NEC_2023__Art*.md | wc -l
```
Expected: `18` files.

```bash
python3 tools/validate_ai_boundaries.py 2>&1 | grep -E "error|warning|OK"
```
Expected: all OK.

Update `project_state/change_log.md` with:

```markdown
## 2026-03-08 — NEC RAG Corpus: 8 New Articles Added

- Added Art 90 (scope and purpose), Art 100 (definitions)
- Added Art 215 (feeders), Art 230 (services)
- Added Art 500 (hazardous locations general), Art 504 (intrinsically safe systems)
- Added Art 505 (Zone 0/1/2 — IEC-aligned)
- Added Art 700–702 (emergency and standby systems)
- Updated _index.yaml: 18 articles now indexed
- Corpus now covers: general, power distribution, hazardous locations, IS systems, emergency power
- File: `control-standards/rag/standards_intelligence/us/nec/`
```
