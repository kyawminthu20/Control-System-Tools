# Standards Intelligence

**AI_READ_ACCESS: ALLOWED**

This module contains the authoritative standards-oriented RAG content for the repository.

## Current Layout

- Root routing files
  - `_index.yaml`
  - `_glossary.md`
  - `_standards_map.md`
- `us/`
  - `nec/`
  - `nfpa79/`
  - `ul_508a/`
- `international/`
  - `machinery/iec_60204_1/`
  - `functional_safety/`
- `crosswalks/`
  - `overlap_matrix/`
  - `overlap_notes/`
- `routing/`
  - `standards_applicability.md`
- `reference_models/`
  - `software_safety_and_intrinsic_safety_standards.md`
  - architecture and safety model guides
- `library_admin/`
  - portfolio, completion, module-summary, and purchase-tracker docs
- `scenario/`
  - standards-driven machine design packages

## Usage

- Start with `_index.yaml`, `_standards_map.md`, or `routing/standards_applicability.md` to choose the right standards path.
- Use `us/` for US panel and machinery standards.
- Use `international/machinery/` for IEC machinery electrical requirements.
- Use `international/functional_safety/` for planned safety standards such as ISO 13849-1 and IEC 62061.
- Use `reference_models/software_safety_and_intrinsic_safety_standards.md` for safety PLC software, redundancy, PLC language, secure-development, and intrinsic-safety routing.
- Use `crosswalks/` for overlap and comparison work across standards families.
- Use `reference_models/` for reusable machine architecture and safety model references.
- Use `library_admin/` for repository status and procurement tracking; treat those files as administrative support, not the primary standards routing layer.
