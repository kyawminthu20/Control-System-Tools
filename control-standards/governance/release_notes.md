# Release Notes
**AI_READ_ACCESS: ALLOWED**

Project-level release snapshots and version history.

## Version 2.0 - Repository Reorganization (2026-03-05)

### Overview
Executed the repository reorganization plan to make `control-standards/` the clear product root and to group standards content by jurisdiction and topic.

### Structural Changes

- moved governance content into `control-standards/governance/`
- moved non-authoritative work into `control-standards/work/`
- moved restricted material into `control-standards/restricted/`
- moved historical material into `control-standards/archive/`
- preserved root export content under `control-standards/exports/legacy_root/`
- repaired the root `rag` compatibility symlink

### Standards Changes

- moved NEC, NFPA 79, and UL 508A into `rag/standards_intelligence/us/`
- moved IEC 60204-1 into `rag/standards_intelligence/international/machinery/`
- moved planned safety standards into `rag/standards_intelligence/international/functional_safety/`
- moved overlap documentation into `rag/standards_intelligence/crosswalks/`

### Documentation Changes

- rewrote startup and orientation docs to match the new structure
- updated the reorganization validator
- generated pre-move manifests and backup snapshot

## Version 1.0 - Initial Release (2026-01-15)

### Overview
Initial establishment of Industrial Automation Intelligence Platform with 12-tool architecture and three-tier knowledge management system.

### Features Delivered

#### Repository Architecture
- Three-tier structure: /rag/ (authoritative), /drafts/ (forbidden), /archive/ (manual)
- AI access control via _index.yaml and AI_READ_ACCESS tags
- Embedded changelog discipline established
- Promotion process with quality gates

#### Tool Modules (Foundation)
1. **Standards Intelligence** - Clause indexes for NEC, NFPA 79, UL 508A, ISO/IEC
2. **Design Framework** - Panel design guide, I/O patterns, constraints
3. **Troubleshooting Decision Engine** - Structure established
4. **Commissioning Checklists** - Framework created
5. **Audit Tool** - Scoring model defined
6. **Design Package Generator** - Kit structure (conveyor, pump, robotic)
7. **Retainer Support Engine** - Service framework
8. **Knowledge Platform** - Navigation structure
9. **UL 508A Panel Automation** - Template system
10. **Training & Cert Builder** - Module structure
11. **IP Library & Licensing** - Catalog framework
12. **Business Metrics Engine** - Metrics schema

#### Knowledge Content
- Core glossary established
- Standards applicability map created
- Design rules engine (wire sizing, grounding, spacing, motor protection, safety)
- Red flags database (10 common compliance issues)
- I/O templates (DI, DO, AI, AO patterns)
- Panel design guide v1

#### Change Management
- Promotion checklist defined
- Design change policy established
- Decision log initialized
- Template library created

### Known Limitations
- Content coverage is foundational; many tool modules need expansion
- Decision trees for troubleshooting not yet populated
- Design package kits need detailed content
- No automation scripts yet implemented
- PDF generation not yet available

### Next Priorities (Future Releases)
- Expand troubleshooting decision trees (digital I/O, analog I/O, networks, motion)
- Complete design guide series (power, I/O, safety, network, motion, PLC software)
- Populate design package kits with full BOMs and diagrams
- Implement validation scripts (validate_ai_boundaries)
- Create report generation automation
- Expand training modules with assessments

---

## Future Versions

### Planned for v1.1
- Complete troubleshooting playbooks
- Expand design framework guides (2-7)
- Add commissioning checklist details
- Implement validation scripts

### Planned for v1.2
- UL 508A automation tooling
- Audit tool scoring implementation
- Business metrics dashboard
- Training module content

### Planned for v2.0
- Interactive decision tree interface
- Automated report generation (MD → PDF)
- Integration with design tools (AutoCAD Electrical, EPLAN)
- Customer portal for licensed content

---

*Version history maintained in reverse chronological order*
