<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# IEC 60204-1 Standards Intelligence Module
**AI_READ_ACCESS: ALLOWED**
**Status:** Foundation Complete - Ready for Content Development

## Overview

This module contains clause-by-clause guidance for **IEC 60204-1 - Electrical Equipment of Machines (2016+AMD1:2021, consolidated Ed. 6.1)**, the **international/global equivalent of NFPA 79**. This standard is used worldwide for machinery electrical design, particularly in EU/CE-marked equipment.

Each clause file follows a consistent template designed for:
- RAG-safe AI indexing
- Copyright compliance (no copyrighted IEC text)
- Traceability and audit support
- Direct mapping to NFPA 79 for US/international comparison
- Integration with ISO 13849 and IEC 62061 for safety functions

## File Structure

All files follow the naming convention:
```
IEC60204_1_2016A1__Clause<NN>__<descriptive_slug>.md
```

## Clause Index

| Clause | Title | Priority | NFPA 79 Equivalent | Focus Area |
|--------|-------|----------|-------------------|------------|
| 1 | Scope | Standard | Ch 1 | Applicability, machinery types |
| 2 | Normative references | Standard | Ch 1 | Required companion standards |
| 3 | Terms, definitions and abbreviated terms | Standard | Ch 2 | Terminology |
| 4 | General requirements | Standard | Ch 4 | Safety philosophy, baseline |
| 5 | Incoming supply conductor terminations and devices for disconnecting and switching off | **HIGH** | Ch 5 | Disconnect, isolation |
| 6 | Protection against electric shock | **HIGH** | Ch 7 | Touch-safe design |
| 7 | Protection of equipment | Standard | Ch 6 | Overcurrent protection |
| 8 | Equipotential bonding | **CRITICAL** | Ch 8 | Grounding strategy |
| 9 | Control circuits and control functions | **CRITICAL** | Ch 9 | E-stop, start/stop, safety |
| 10 | Operator interface and machine-mounted control devices | Standard | Ch 10 | HMI, pushbuttons, ergonomics |
| 11 | Controlgear: location, mounting, and enclosures | **HIGH** | Ch 11 | Enclosures, panel design |
| 12 | Conductors and cables | **HIGH** | Ch 12 | Conductor selection, ampacity |
| 13 | Wiring practices | **HIGH** | Ch 13 | Routing, segregation, terminations |
| 14 | Electric motors and associated equipment | **HIGH** | Ch 14 | Motor control, VFD |
| 15 | Socket-outlets and lighting | Standard | Ch 15 | Lighting, socket-outlets |
| 16 | Marking, warning signs and reference designations | **HIGH** | Ch 16 | Labels, nameplate, designations |
| 17 | Technical documentation | **HIGH** | Ch 19 | Schematics, manuals, parts list |
| 18 | Verification | **HIGH** | - | Testing, commissioning |

## Priority Clauses

For international machinery design, focus on these clauses first:

1. **Clause 8 - Equipotential Bonding**: Safety-critical grounding requirements
2. **Clause 9 - Control Circuits and Functions**: E-stop, safety circuits
3. **Clause 5 - Incoming Supply**: Disconnect and isolation
4. **Clause 16/17 - Marking and technical documentation**: feeds the EU technical file
5. **Clause 18 - Verification**: Testing and validation requirements

## IEC 60204-1 ↔ NFPA 79 Direct Mapping

### Nearly Identical Requirements

| Topic | IEC 60204-1 | NFPA 79 | Notes |
|-------|-------------|---------|-------|
| Disconnecting Means | Clause 5 | Chapter 5 | Similar requirements |
| Grounding/Bonding | Clause 8 | Chapter 8 | IEC uses "equipotential bonding" |
| Control Circuits | Clause 9 | Chapter 9 | Nearly identical |
| Control Equipment | Clause 11 | Chapter 11 | Same scope |
| Marking & Docs | Clause 16 & 17 | Chapter 16 & 19 | Similar, format differs |

### Key Differences

| Aspect | IEC 60204-1 | NFPA 79 |
|--------|-------------|---------|
| **Jurisdiction** | Global/International | United States |
| **Voltage Standards** | 230V, 400V typical | 120V, 480V typical |
| **Component Cert** | CE marking | UL listing |
| **Safety Framework** | Pairs with ISO 13849/IEC 62061 | Standalone |
| **Color Codes** | IEC 60446 | US standards |
| **Risk Assessment** | ISO 12100 required | Not explicitly required |

## Regional Considerations

### For EU/Global Markets
- **Must use**: IEC 60204-1
- **Safety**: ISO 13849-1 or IEC 62061 for safety functions
- **Risk**: ISO 12100 for risk assessment
- **Marking**: CE marking applied by the manufacturer on completion of conformity assessment
- **Components**: IEC/EN certified components

### For US Markets
- **Must use**: NFPA 79
- **Panel**: UL 508A if seeking UL listing
- **Code**: NEC Article 670 (machinery) or 409 (panels)
- **Components**: UL/NEMA certified components

### For Dual US/EU Markets
- Design to **both** IEC 60204-1 and NFPA 79
- Use most restrictive requirement from each
- Document compliance to both standards
- Use dual-certified components where possible

## Integration with Other ISO/IEC Standards

### Safety Standards (Required Companions)
- **ISO 12100**: Risk Assessment (foundation for all safety)
- **ISO 13849-1**: Safety of Machinery - Performance Levels (PL)
- **IEC 62061**: Functional Safety - Safety Integrity Levels (SIL)
- **ISO 13850**: Emergency Stop Function

### Typical Safety Architecture
```
ISO 12100 (Risk Assessment)
    ↓
ISO 13849-1 OR IEC 62061 (Safety Function Requirements)
    ↓
IEC 60204-1 (Electrical Implementation)
```

## Template Structure

Each clause file contains:

### Metadata Header (HTML Comment)
- CONTENT_CLASS, AI_READ_ACCESS, STATUS
- STANDARD_FAMILY: IEC, STANDARD_ID: IEC_60204_1
- EDITION: 2016+AMD1:2021 (CSV Ed. 6.1), JURISDICTION: GLOBAL
- IEC_HIERARCHY: clause + clause_title
- INDEX_TAGS: topics, systems

### Content Sections
1. **Purpose/Scope**: What this clause covers
2. **Clause-specific guidance**: Requirements and interpretation
3. **Comparison to NFPA 79**: US/international differences
4. **Change log**: Version history (mandatory)

## Copyright Compliance

**CRITICAL**: These files contain:
- ✅ Clause identifiers and organizational structure
- ✅ Paraphrased intent and engineering guidance
- ✅ Design checklists and interpretation
- ❌ NO copyrighted IEC text verbatim

Always purchase legitimate copies of IEC 60204-1 for authoritative reference.

## Statistics

| Metric | Count/Value |
|--------|------------|
| Total clauses documented | 18 |
| Clauses marked CRITICAL | 2 (8, 9) |
| Clauses marked HIGH | 9 (5, 6, 11, 12, 13, 14, 16, 17, 18) |
| Clauses marked Standard | 7 |
| NFPA 79 equivalents mapped | 8 |
| Edition | 2016+AMD1:2021 (consolidated CSV Ed. 6.1) |
| Jurisdiction | Global/International |

## Usage Workflow

### For International/EU Machinery Design
1. Start with IEC 60204-1 Clause 1 (scope - verify applicability)
2. Perform risk assessment per ISO 12100
3. Design safety functions per ISO 13849-1 or IEC 62061
4. Apply IEC 60204-1 Clauses 5, 8, 9 (disconnect, bonding, control)
5. Reference Clause 11 for control equipment design
6. Complete per Clause 14 (marking for CE marking)
7. Verify per Clause 15 (testing and validation)

### For Dual US/EU Compliance
1. Design to IEC 60204-1 as baseline
2. Check NFPA 79 for US-specific requirements
3. Use most restrictive from each standard
4. Document compliance to both
5. Use dual-voltage designs (230V/400V and 120V/480V capable)

### For Audits/CE Marking
1. Clause 1: Verify standard applies
2. Clause 14: Check marking and documentation complete
3. Clause 8: Verify equipotential bonding
4. Clause 9: Verify emergency stop and safety circuits
5. Clause 15: Review test/verification records

## Content Development Status

| Status | Description | Action |
|--------|-------------|--------|
| **DRAFT** | Template created, content TODO | Fill in from IEC 60204-1 reference |
| **REVIEWED** | Content filled, under peer review | Complete review process |
| **APPROVED** | Reviewed and approved for RAG use | Ready for AI indexing |
| **DEPRECATED** | Superseded by newer version | Archive and link to current |

Current Status: **All clauses are DRAFT** - templates ready for content development.

## Next Steps

### Immediate (Content Development)
1. **Fill critical clauses first** (8, 9)
   - Clause 8: Equipotential bonding requirements, PE conductor sizing
   - Clause 9: Control circuit design, emergency stop, safety separation

2. **Fill high-priority clauses** (5, 6, 11, 14, 15)
   - Add practical guidance
   - Document IEC vs NFPA differences
   - Create verification checklists

3. **Build IEC ↔ NFPA overlap matrix**
   - Clause-by-clause comparison
   - Regional difference documentation
   - Design decision guide

### Short-term (Integration)
1. Link to NFPA 79 chapters (equivalence mapping)
2. Connect to ISO 13849-1 safety requirements
3. Integrate with design framework patterns
4. Build EU vs US compliance wizard

### Long-term (Tools)
1. Dual-compliance checker (IEC + NFPA)
2. CE marking documentation generator
3. Regional adaptation tool (EU ↔ US)
4. Voltage/component conversion guide

## Related Files

- [IEC Clause Index](../../clause_index/iso_iec_clause_index.yaml) - Simple clause listing
- [Standards Applicability](../../../routing/standards_applicability.md) - When to use IEC vs NFPA
- [NFPA 79 Module](../../NFPA/) - US equivalent standard
- [_index.yaml](./_index.yaml) - RAG routing configuration

## Changelog

- 2026-01-15 — Initial IEC 60204-1 module structure created
  - 15 clause files generated with templates
  - _index.yaml created with complete document registry
  - Priority clauses identified (2 critical, 5 high, 8 standard)
  - Direct mapping to NFPA 79 established
  - Regional considerations documented
  - Status: DRAFT, ready for content development

---

**Edition Note**: This module uses IEC 60204-1:2016+AMD1:2021 CSV (6th Edition). Earlier editions have some differences.

**CE Marking Note**: Content in this module supports IEC 60204-1 compliance but does not replace official CE marking process. Machinery must undergo conformity assessment per relevant EU directives.

**Global Standard**: IEC 60204-1 is recognized worldwide and is the basis for many national standards (EN 60204-1 in Europe, etc.)
