<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# NFPA 79 Standards Intelligence Module
**AI_READ_ACCESS: ALLOWED**
**Status:** Foundation Complete - Ready for Content Development

## Overview

This module contains chapter-by-chapter guidance for **NFPA 79 - Electrical Standard for Industrial Machinery (2024 Edition)**. Each chapter file follows a consistent template designed for:

- RAG-safe AI indexing
- Copyright compliance (no copyrighted NFPA text)
- Traceability and audit support
- Control panel engineering focus

## File Structure

All files follow the naming convention:
```
NFPA79_2024__Ch<NN>__<descriptive_slug>.md
```

## Chapter Index

| Ch | Title | Priority | Focus Area |
|----|-------|----------|------------|
| 01 | Administration | Standard | Applicability, scope, enforcement |
| 02 | Definitions | Standard | Terminology, definitions |
| 03 | General Requirements | Standard | Safety philosophy, baseline |
| 04 | General Conditions of Installation | Standard | Environment, accessibility |
| 05 | Disconnecting Means | **HIGH** | Main disconnects, LOTO, isolation |
| 06 | Overcurrent Protection | Standard | Branch circuit protection |
| 07 | Protection Against Electric Shock | Standard | Touch-safe design |
| 08 | Grounding and Bonding | **HIGH** | PE conductor, bonding strategy |
| 09 | Control Circuits and Control Functions | **HIGH** | E-stop, start/stop, safety separation |
| 10 | Operator Interface and Control Devices | Standard | Pushbuttons, HMI, ergonomics |
| 11 | Control Equipment | **HIGH** | Control panels, enclosures (UL 508A overlap) |
| 12 | Motors and Associated Equipment | Standard | Motor control, VFD integration |
| 13 | Appliances and Accessories | Standard | Auxiliary devices |
| 14 | Lighting | Standard | Panel and machine lighting |
| 15 | Transformers and Power Supplies | Standard | Control power architecture |
| 16 | Wiring Methods | Standard | Routing, segregation |
| 17 | Cables and Flexible Cords | Standard | Drag chain, robot cabling |
| 18 | Terminal Blocks, Connectors, and Wiring Devices | Standard | Field wiring interfaces |
| 19 | Marking and Documentation | **HIGH** | Labeling, schematics, audit readiness |
| 20 | System Integration | Standard | Overall compliance coordination |

## Priority Chapters (Recommended Focus)

For control panel engineers, focus on these chapters first:

1. **Chapter 5 - Disconnecting Means**: Most inspected requirement
2. **Chapter 8 - Grounding and Bonding**: Frequent inspection failure area
3. **Chapter 9 - Control Circuits**: Safety-critical design
4. **Chapter 11 - Control Equipment**: Panel construction (strong UL 508A overlap)
5. **Chapter 19 - Marking and Documentation**: Critical for audits and handover

## Template Structure

Each chapter file contains:

### Metadata Header (HTML Comment)
- CONTENT_CLASS, AI_READ_ACCESS, STATUS
- STANDARD_FAMILY, STANDARD_ID, EDITION
- NFPA_HIERARCHY (chapter, chapter_title)
- INDEX_TAGS (topics, systems, risks, components)

### Content Sections
1. **Scope and intent**: Paraphrased purpose
2. **Field rules summary**: Actionable design constraints
3. **Section map**: Section IDs with paraphrased intent (no copyrighted text)
4. **Control-systems interpretation**: How to apply to panels/machines
5. **Verification & commissioning checks**: Pre-power, dry-run, live-run
6. **Decision log**: Engineering decisions made
7. **Change log**: Version history (mandatory)

## Copyright Compliance

**CRITICAL**: These files contain:
- ✅ Chapter/section identifiers
- ✅ Paraphrased intent and engineering guidance
- ✅ Design checklists and interpretation
- ❌ NO copyrighted NFPA text verbatim

Always purchase legitimate copies of NFPA 79 for authoritative reference.

## Cross-References

### NFPA 79 ↔ NEC
- Ch 5 (Disconnecting Means) ↔ NEC 670 (Industrial Machinery)
- Ch 12 (Motors) ↔ NEC 430 (Motors, Motor Circuits, and Controllers)

### NFPA 79 ↔ UL 508A
- Ch 11 (Control Equipment) ↔ UL 508A (entire standard)
- Strong overlap in panel construction, spacing, SCCR

### NFPA 79 ↔ ISO/IEC
- IEC 60204-1 is the international equivalent to NFPA 79
- ISO 13849-1 covers safety-related control functions (Ch 9 overlap)

## Usage Workflow

### For Design Work
1. Identify project type (machine, robot cell, conveyor, etc.)
2. Check [Standards Applicability](../../routing/standards_applicability.md)
3. Review priority chapters relevant to your design
4. Use section maps and checklists during design
5. Cross-reference with design framework patterns

### For Audits
1. Use Chapter 19 (Marking and Documentation) as starting point
2. Check priority chapters for common inspection items
3. Reference red flags database: [../rules_engine/red_flags.yaml](../rules_engine/red_flags.yaml)
4. Document findings using audit tool templates

### For Commissioning
1. Map chapter requirements to commissioning phases
2. Pre-power: Ch 5 (Disconnects), Ch 8 (Grounding)
3. Dry-run: Ch 9 (Control Circuits), Ch 10 (Operator Interface)
4. Live-run: Ch 12 (Motors), Ch 15 (Transformers)
5. Handover: Ch 19 (Documentation)

## Content Development Status

| Status | Description | Action |
|--------|-------------|--------|
| **DRAFT** | Template created, content TODO | Fill in sections from NFPA 79 reference |
| **REVIEWED** | Content filled, under peer review | Complete review process |
| **APPROVED** | Reviewed and approved for RAG use | Ready for AI indexing |
| **DEPRECATED** | Superseded by newer version | Archive and link to current |

Current Status: **All chapters are DRAFT** - templates ready for content development.

## Next Steps

### Immediate (Content Development)
1. Prioritize high-priority chapters (5, 8, 9, 11, 19)
2. Fill in "Field rules summary" sections with actionable guidance
3. Create section maps with paraphrased intent
4. Develop control-systems interpretation for each chapter

### Short-term (Integration)
1. Link chapter content to design framework patterns
2. Connect to audit tool scoring model
3. Integrate with commissioning checklists
4. Build cross-reference map with NEC and UL 508A

### Long-term (Automation)
1. Generate automated compliance checklists from chapter content
2. Build RAG query system for chapter-specific guidance
3. Create chapter-to-project-type recommendation engine
4. Develop automated audit report generation

## Related Files

- [NFPA Clause Index](../clause_index/nfpa79_clause_index.yaml) - Simple clause listing
- [Standards Applicability](../../routing/standards_applicability.md) - When to use NFPA 79
- [Rules Engine](../rules_engine/rules.yaml) - Machine-readable design rules
- [Red Flags](../rules_engine/red_flags.yaml) - Common compliance issues
- [_index.yaml](./_index.yaml) - RAG routing configuration

## Changelog

- 2026-01-15 — Initial NFPA 79 module structure created
  - All 20 chapter files generated with templates
  - _index.yaml created with complete document registry
  - Priority chapters identified
  - Cross-reference framework established
  - Status: DRAFT, ready for content development
