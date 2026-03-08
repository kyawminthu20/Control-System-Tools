# NEC (NFPA 70) Standards Intelligence Module
**AI_READ_ACCESS: ALLOWED**
**Status:** Foundation Complete - Ready for Content Development

## Overview

This module contains article-by-article guidance for the **National Electrical Code (NEC) - NFPA 70 (2023 Edition)**, specifically focused on industrial control panel applications. Each article file follows a consistent template designed for:

- RAG-safe AI indexing
- Copyright compliance (no copyrighted NEC text)
- Traceability and audit support
- Industrial control panel engineering focus
- Integration with UL 508A and NFPA 79

## File Structure

All files follow the naming convention:
```
NEC_2023__Art<NNN>__<descriptive_slug>.md
```

## Article Index

### Core Articles (Essential for Every Panel)

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 110 | Requirements for Electrical Installations | **HIGH** | Listing, labeling, installation instructions |
| 250 | Grounding and Bonding | **CRITICAL** | Equipment grounding, bonding strategy |
| 300 | General Wiring Methods | Standard | Routing, mechanical protection |
| 310 | Conductors for General Wiring | **HIGH** | Wire sizing, ampacity, temperature ratings |
| 409 | Industrial Control Panels | **CRITICAL** | Panel definition, SCCR, labeling |

### Commonly Needed Articles (Motors, Power, Controls)

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 430 | Motors, Motor Circuits, and Controllers | **HIGH** | Motor protection, VFD integration |
| 240 | Overcurrent Protection | **HIGH** | Breakers, fuses, SCCR coordination |
| 408 | Switchboards, Switchgear, and Panelboards | Standard | Panel construction (often superseded by 409) |
| 725 | Class 1, Class 2, and Class 3 Remote-Control Circuits | Standard | Control circuit classification |

### As Applicable

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 670 | Industrial Machinery | **HIGH** | Machine disconnects, NFPA 79 overlap |

### General and Definitions

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 90 | Introduction — Scope and Purpose | **HIGH** | NEC scope limits, AHJ authority, adoption process |
| 100 | Definitions | **HIGH** | Authoritative definitions: listed, labeled, grounded, SCCR |

### Power Distribution

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 215 | Feeders | Standard | Feeder conductor sizing, continuous load rule, 125% factor |
| 230 | Services | Standard | Available fault current, service disconnect, neutral-to-ground bond |

### Hazardous Locations

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 500 | Hazardous Locations — General | **HIGH** | Class/Division framework, T-code, equipment selection |
| 504 | Intrinsically Safe Systems | **HIGH** | IS design rules, zener barriers, galvanic isolators |
| 505 | Zone 0, 1, and 2 Locations | Standard | IEC-aligned zone system, ATEX/IECEx equipment use in US |

### Emergency and Standby Power

| Article | Title | Priority | Focus Area |
|---------|-------|----------|------------|
| 700–702 | Emergency / Legally Required / Optional Standby | Standard | Transfer time tiers, ATS requirements, safety system power coordination |

### Planned (Not Yet Created)

- Article 511/514 — Hazardous Locations: motor fuel dispensing, bulk storage (dust environments)
- Article 800/820/830 — Communications Circuits (if applicable)

## Priority Articles (Recommended Focus)

For industrial control panel engineers, focus on these articles first:

1. **Article 409 - Industrial Control Panels**: Defines what an industrial control panel is, SCCR requirements, labeling
2. **Article 250 - Grounding and Bonding**: Safety-critical, frequent inspection failure area
3. **Article 310 - Conductors**: Wire sizing and ampacity calculations
4. **Article 430 - Motors**: Most common control panel loads
5. **Article 110 - General Requirements**: Fundamental listing and installation requirements

## Template Structure

Each article file contains:

### Metadata Header (HTML Comment)
- CONTENT_CLASS, AI_READ_ACCESS, STATUS
- STANDARD_FAMILY: NEC, STANDARD_ID: NFPA_70
- EDITION: 2023
- NEC_HIERARCHY (article, article_title)
- INDEX_TAGS (topics, systems, risks, components)

### Content Sections
1. **Scope and relevance**: Paraphrased purpose for control panels
2. **Field rules summary**: Actionable design constraints
3. **Section map**: Section IDs with paraphrased intent (no copyrighted text)
4. **Control-system interpretation**: How to apply to panels
5. **Test and verification**: What inspectors check
6. **Decision log**: Engineering decisions made
7. **Change log**: Version history (mandatory)

## Copyright Compliance

**CRITICAL**: These files contain:
- ✅ Article/section identifiers
- ✅ Paraphrased intent and engineering guidance
- ✅ Design checklists and interpretation
- ❌ NO copyrighted NEC text verbatim

Always purchase legitimate copies of the NEC for authoritative reference.

## Cross-References

### NEC ↔ UL 508A

| UL 508A Section | Title | Related NEC Articles |
|-----------------|-------|---------------------|
| Section 28 | SCCR | 409 |
| Section 29 | Overcurrent Protection | 240 |
| Section 30 | Wire Sizing | 310 |
| Section 35 | Grounding | 250 |

### NEC ↔ NFPA 79

| NFPA 79 Chapter | Title | Related NEC Articles |
|-----------------|-------|---------------------|
| Chapter 5 | Disconnecting Means | 670 |
| Chapter 8 | Grounding and Bonding | 250 |
| Chapter 11 | Control Equipment | 409 |
| Chapter 12 | Motors | 430 |

### NEC Article Relationships

```
Article 110 (General) → Applies to all installations
    ↓
Article 409 (Industrial Control Panels) → Defines scope
    ↓
Article 250 (Grounding) → Safety foundation
Article 310 (Conductors) → Wire sizing
Article 240 (Overcurrent) → Protection devices
Article 430 (Motors) → Common loads
Article 670 (Machinery) → Machine installations
```

## Usage Workflow

### For Design Work
1. Start with **Article 409** to confirm panel qualifies as industrial control panel
2. Review **Article 250** for grounding strategy
3. Use **Article 310** for all wire sizing calculations
4. Apply **Article 430** for motor circuits
5. Use **Article 240** for overcurrent device selection
6. If machinery installation, reference **Article 670**

### For Audits
1. Check **Article 409** compliance (SCCR label, voltage marking)
2. Verify **Article 250** (EGC sizing, bonding)
3. Audit **Article 110** (listed equipment, installation per instructions)
4. Review **Article 430** (motor protection)
5. Document findings using audit tool templates

### For Commissioning
1. Pre-power: Verify Article 250 (grounding continuity)
2. Pre-power: Check Article 110 (equipment listing)
3. Dry-run: Test Article 430 (motor protection settings)
4. Handover: Confirm Article 409 labeling complete

## Content Development Status

| Status | Description | Action |
|--------|-------------|--------|
| **DRAFT** | Template created, content TODO | Fill in sections from NEC reference |
| **REVIEWED** | Content filled, under peer review | Complete review process |
| **APPROVED** | Reviewed and approved for RAG use | Ready for AI indexing |
| **DEPRECATED** | Superseded by newer version | Archive and link to current |

Current Status: **All articles are DRAFT** - templates ready for content development.

## Common Inspection Failures

### Article 250 - Grounding and Bonding
- **Common Failure**: Undersized equipment grounding conductor (EGC)
- **Quick Check**: Compare EGC size to NEC Table 250.122 based on OCPD rating
- **Fix**: Replace with properly sized EGC

### Article 409 - Industrial Control Panels
- **Common Failure**: Missing or incorrect SCCR label
- **Quick Check**: Verify SCCR label is present and matches calculation
- **Fix**: Calculate SCCR per UL 508A Section 28 and affix label

### Article 430 - Motors
- **Common Failure**: Oversized branch circuit breaker (> 250% FLA)
- **Quick Check**: OCPD rating ≤ 250% of motor FLA (standard motors)
- **Fix**: Downsize breaker or use manufacturer-approved rating

### Article 110 - General Requirements
- **Common Failure**: Equipment not installed per manufacturer instructions
- **Quick Check**: Verify installation manual compliance
- **Fix**: Correct installation per manual, document evidence

## Integration Points

### With Design Framework
- Article 250 rules → [grounding_bonding_rules.yaml](../../design_framework/constraints/grounding_bonding_rules.yaml)
- Article 310 rules → Wire sizing patterns in design guides
- Article 409 rules → Panel design guide

### With Audit Tool
- Article checklists → Audit scoring model
- Common failures → Red flags database
- Inspection focus → Audit report templates

### With UL 508A Panel Automation
- Article 409 SCCR → SCCR calculation worksheet
- Article 310 ampacity → BOM generator wire sizing
- Article 250 EGC → Grounding conductor auto-sizing

## Statistics

| Metric | Count |
|--------|-------|
| Total articles documented | 10 |
| Core articles | 5 |
| Commonly needed articles | 4 |
| As-applicable articles | 1 |
| Articles marked CRITICAL | 2 (250, 409) |
| Articles marked HIGH | 4 (110, 310, 430, 670) |
| Related UL 508A sections | 4 |
| Related NFPA 79 chapters | 4 |

## Next Steps

### Immediate (Content Development)
1. **Fill critical articles first** (250, 409)
   - Article 250: EGC sizing tables, bonding requirements
   - Article 409: SCCR marking, panel definition

2. **Fill high-priority articles** (110, 310, 430, 670)
   - Add field rules summaries
   - Create section maps with paraphrased intent
   - Develop control-panel interpretations

3. **Update STATUS field** as content progresses
   - DRAFT → REVIEWED → APPROVED

### Short-term (Integration)
1. Link NEC articles to UL 508A sections
2. Build cross-reference map with NFPA 79 chapters
3. Connect to design framework constraints
4. Integrate with audit tool scoring

### Long-term (Automation)
1. Automated NEC compliance checking during design
2. Real-time SCCR calculation based on Article 409
3. Wire sizing automation using Article 310 tables
4. Automated audit report generation

## Related Files

- [NEC Clause Index](../clause_index/nec_clause_index.yaml) - Simple article listing
- [Standards Applicability](../../routing/standards_applicability.md) - When to use NEC vs NFPA 79
- [Rules Engine](../rules_engine/rules.yaml) - Machine-readable design rules
- [Red Flags](../rules_engine/red_flags.yaml) - Common compliance issues
- [_index.yaml](./_index.yaml) - RAG routing configuration

## Changelog

- 2026-01-15 — Initial NEC module structure created
  - 10 article files generated with templates
  - _index.yaml created with complete document registry
  - Priority articles identified (2 critical, 4 high)
  - Cross-reference framework with UL 508A and NFPA 79 established
  - Status: DRAFT, ready for content development

---

**Edition Note**: This module uses NEC 2023 Edition. If your jurisdiction requires NEC 2020 or NEC 2026, additional article files may be needed to capture edition-specific changes.
