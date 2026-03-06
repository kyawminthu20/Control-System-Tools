# Decision Log
**AI_READ_ACCESS: ALLOWED**
**Status:** Authoritative Record

High-level architectural and process decisions for this knowledge repository.

## Format
Each entry should include:
- **Date**: Decision date
- **Decision**: What was decided
- **Rationale**: Why this decision was made
- **Impact**: What changed as a result
- **Participants**: Who was involved

---

## Decisions

### 2026-03-05: Repository Reorganization Executed
**Decision**: Consolidate product-support folders under `control-standards/` and group standards content by jurisdiction and topic.

**Rationale**:
- Removes duplicate roots and conflicting folder narratives
- Makes `control-standards/` the clear product root
- Makes standards navigation more predictable for humans and models

**Impact**:
- `change_management/` became `control-standards/governance/`
- work areas moved under `control-standards/work/`
- restricted material moved under `control-standards/restricted/`
- standards moved into `us/`, `international/`, and `crosswalks/`
- root `rag` compatibility symlink was repaired to point at `control-standards/rag`

**Participants**: Reorganization execution

---

### 2026-01-15: Repository Structure Established
**Decision**: Implement three-tier structure: /rag/ (authoritative, AI-readable), /drafts/ (forbidden to AI), /archive/ (manual-only)

**Rationale**:
- Prevents AI from learning incorrect/incomplete information
- Enforces human review before content becomes authoritative
- Provides clear separation of concerns

**Impact**:
- All AI tools restricted to /rag/** paths only
- Promotion process required for all authoritative content
- Quality gate established

**Participants**: Initial project setup

---

### 2026-01-15: Embedded Changelog Requirement
**Decision**: All RAG files must include embedded changelog at bottom of file

**Rationale**:
- Version tracking without external systems
- Clear audit trail for changes
- Easy to see file evolution at a glance

**Impact**:
- Template updates required
- Promotion checklist includes changelog verification
- All new and updated files must comply

**Participants**: Initial project setup

---

### 2026-01-15: No Copyrighted Standards Text
**Decision**: Clause indexes contain only identifiers and brief intent, never copyrighted text from standards

**Rationale**:
- Legal compliance (standards are copyrighted)
- Encourages legitimate standard purchases
- Focuses on actionable guidance vs. verbatim reproduction

**Impact**:
- Standards intelligence tool design adapted
- All clause index files use approved format
- Training materials emphasize paraphrasing

**Participants**: Initial project setup

---

### 2026-01-15: 12 Tool Framework Established
**Decision**: Organize knowledge repository around 12 distinct tools/modules

**Rationale**:
- Modular design enables à la carte usage
- Each tool addresses specific business need
- Supports licensing and monetization strategy

**Impact**:
- Repository structure reflects 12 tools
- Each tool gets dedicated README and subfolder
- IP licensing catalog organized by tool

**Participants**: Initial project setup

---

*Add new decisions above this line in reverse chronological order*
