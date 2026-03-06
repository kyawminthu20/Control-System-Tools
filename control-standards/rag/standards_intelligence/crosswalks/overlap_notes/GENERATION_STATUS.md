# Overlap Notes Generation Status
**AI_READ_ACCESS: ALLOWED**

**Generated:** 2026-01-15
**Location:** `rag/standards_intelligence/crosswalks/overlap_notes/`

## Purpose

Per-topic overlap notes provide detailed:
- Decision rules (which standard wins, when)
- Evidence requirements (what to collect/store)
- Checklists (actionable steps)
- Cross-links (to standards files and overlap matrices)

## Files Required

**Total**: 29 files (28 overlap notes + 1 index)

### Core Files ✅
- [x] `_index.yaml` - Master routing index (CREATED)
- [x] `file_structure.md` - Template reference (existing)
- [x] `GENERATION_STATUS.md` - This file (CREATED)

### US Standards Overlap Notes (14 files)
**Topic**: UL 508A ↔ NEC ↔ NFPA 79

1. [ ] `overlap__scope_boundary.md` - Panel vs machine vs facility scope
2. [ ] `overlap__listing_labeling_instructions.md` - Component listing compliance
3. [ ] `overlap__disconnecting_means.md` - Disconnect requirements
4. [ ] `overlap__overcurrent_protection.md` - OCP and coordination
5. [ ] `overlap__grounding_bonding.md` - Safety grounding requirements
6. [ ] `overlap__wiring_methods_conductors.md` - Wire routing and separation
7. [ ] `overlap__control_functions.md` - Control circuit behavior
8. [ ] `overlap__emergency_stop.md` - E-stop functional requirements
9. [ ] `overlap__panel_construction.md` - Panel layout and workmanship
10. [x] `overlap__sccr.md` - **SCCR determination (CRITICAL)** ✅ CREATED
11. [ ] `overlap__marking_documentation.md` - Labeling requirements
12. [ ] `overlap__motors_drives.md` - Motor protection and drives
13. [ ] `overlap__control_power.md` - Transformers and PSUs
14. [ ] `overlap__multi_panel_machines.md` - Multi-panel SCCR aggregation

### International Overlap Notes (14 files)
**Topic**: NFPA 79 ↔ IEC 60204-1

1. [ ] `overlap_nfpa79_iec60204__scope_boundary.md` - Machine supply boundary
2. [ ] `overlap_nfpa79_iec60204__definitions.md` - Terminology mapping
3. [ ] `overlap_nfpa79_iec60204__general_requirements.md` - General principles
4. [ ] `overlap_nfpa79_iec60204__incoming_supply_disconnect.md` - Disconnect (90%+ equivalent)
5. [ ] `overlap_nfpa79_iec60204__electric_shock_protection.md` - Shock protection
6. [ ] `overlap_nfpa79_iec60204__equipment_protection.md` - Equipment protection
7. [ ] `overlap_nfpa79_iec60204__grounding_bonding.md` - Grounding vs Bonding (direct equivalent)
8. [ ] `overlap_nfpa79_iec60204__control_functions.md` - Control behavior
9. [ ] `overlap_nfpa79_iec60204__operator_interface.md` - HMI and controls
10. [ ] `overlap_nfpa79_iec60204__control_equipment.md` - Panel/enclosure design
11. [ ] `overlap_nfpa79_iec60204__motors_drives.md` - Motor protection
12. [ ] `overlap_nfpa79_iec60204__accessories_lighting.md` - Accessories and lighting
13. [ ] `overlap_nfpa79_iec60204__marking_documentation.md` - US vs EU labeling
14. [ ] `overlap_nfpa79_iec60204__verification.md` - Testing and verification

## Status Summary

| Category | Total | Created | Remaining | Status |
|----------|-------|---------|-----------|--------|
| **Core Files** | 3 | 3 | 0 | ✅ Complete |
| **US Overlap Notes** | 14 | 1 | 13 | 🔄 In Progress |
| **International Notes** | 14 | 0 | 14 | ⏳ Pending |
| **TOTAL** | 31 | 4 | 27 | **13% Complete** |

## Priority for Next Phase

### Critical Priority (Create First) 🔴
1. ✅ `overlap__sccr.md` - SCCR determination (DONE)
2. `overlap__grounding_bonding.md` - Safety-critical grounding
3. `overlap__scope_boundary.md` - Fundamental decision routing
4. `overlap_nfpa79_iec60204__grounding_bonding.md` - US vs IEC grounding

### High Priority (Create Second) ⭐
5. `overlap__disconnecting_means.md` - Disconnect requirements
6. `overlap__emergency_stop.md` - E-stop requirements
7. `overlap__panel_construction.md` - Panel build standards
8. `overlap_nfpa79_iec60204__control_functions.md` - Control behavior
9. `overlap_nfpa79_iec60204__incoming_supply_disconnect.md` - US/IEC disconnect

### Standard Priority (Create Third) ⚪
10-29. Remaining files

## File Template Structure

Each overlap note file contains:

```markdown
<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: [topic_identifier]
[PRIORITY: CRITICAL] (if applicable)
-->

# Overlap Note — [Topic Title]

## Decision rules (who wins)
[Which standard leads, when, and why]

## Evidence required
[Checklist of required documentation]

## Checklist
[Actionable implementation steps]

## Cross-links
[Links to standards files and overlap matrices]

## Changelog
[Version history]
```

## Integration Points

**Overlap Notes** link to:
- Standards files: `../nec/`, `../nfpa79/`, `../ul_508a/`, `../iec_60204_1/`
- Overlap matrices: `../overlap_matrix/`
- Master index: `../_index.yaml`

**Overlap Matrices** reference:
- Per-topic overlap notes for detailed guidance
- Example: "See `_overlap_notes/overlap__sccr.md` for detailed SCCR determination workflow"

## Use Cases

### Use Case 1: Engineer Asks "What SCCR do I need?"
**Route to**: `overlap__sccr.md`
**Provides**:
- Decision rules (NEC requires, UL provides method)
- Step-by-step workflow
- Weakest-link calculation example
- Evidence checklist
- Label format

### Use Case 2: Engineer Asks "How do I ground my panel?"
**Route to**: `overlap__grounding_bonding.md`
**Provides**:
- NEC baseline requirements
- NFPA 79 machine specifics
- UL 508A workmanship details
- Door bonding requirements
- PE conductor sizing

### Use Case 3: Engineer Asks "What's different between US and EU?"
**Route to**: `overlap_nfpa79_iec60204__*` series
**Provides**:
- Terminology mapping (grounding vs bonding)
- Voltage differences (480V vs 400V)
- Component certification (UL vs CE)
- Regional adaptation checklists

## Automation Opportunities

Based on overlap notes, these tools can be built:

**High Automation Potential**:
1. **SCCR Calculator** - Uses `overlap__sccr.md` logic
2. **Grounding Checker** - Uses `overlap__grounding_bonding.md` rules
3. **Dual-Compliance Wizard** - Uses all `overlap_nfpa79_iec60204__*` notes

**Medium Automation Potential**:
4. **Scope Decision Router** - Uses `overlap__scope_boundary.md`
5. **E-stop Validator** - Uses `overlap__emergency_stop.md`
6. **Regional Adapter** - Uses international overlap notes

## Next Actions

### Immediate (Week 1)
1. ✅ Create `_index.yaml` - DONE
2. ✅ Create `overlap__sccr.md` (CRITICAL) - DONE
3. Create remaining 3 critical priority files
4. Create 5 high priority files

### Short-term (Weeks 2-3)
5. Create remaining US overlap notes (6 files)
6. Create all international overlap notes (14 files)
7. Test cross-links and routing

### Integration (Week 4)
8. Link overlap notes to overlap matrices
9. Update master standards index
10. Build SCCR calculator tool (high priority automation)

## Validation Checklist

Before marking complete, verify:
- [ ] All 28 overlap note files created
- [ ] All files follow template structure
- [ ] All cross-links work (no broken references)
- [ ] Decision rules are clear and actionable
- [ ] Evidence checklists are comprehensive
- [ ] Priority levels assigned correctly
- [ ] Automation opportunities documented

## Changelog

- 2026-01-15 — Generation status tracking document created
  - Total files needed: 31 (3 core + 28 overlap notes)
  - Files created: 4 (13% complete)
  - Critical SCCR overlap note completed
  - Priority order established
  - Status: IN PROGRESS

---

**Current Status**: 13% Complete (4 of 31 files)
**Next Step**: Create 3 remaining critical priority files
**Estimated Completion**: Requires systematic generation of 27 remaining files