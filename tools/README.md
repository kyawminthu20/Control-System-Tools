# Tools

**AI_READ_ACCESS: ALLOWED**

Local automation and validation scripts for the workspace.

## Current Script Roles

- `validate_ai_boundaries.py`
  - scans `control-standards/rag/` for required metadata and forbidden terms
- `fix_ai_boundaries.py`
  - repairs common metadata issues in AI-readable Markdown files
- `project_automator.py`
  - refreshes the root `STRUCTURE_SUMMARY.md` tree and aggregates generation summaries into `general_change_log.md`
- `generate_rag_index.py`
  - placeholder, not yet implemented
- `validate_reorg.sh`
  - validates the 2026-03-05 repository reorganization deliverables and structure

## Usage

```bash
python3 tools/validate_ai_boundaries.py
python3 tools/fix_ai_boundaries.py
python3 tools/project_automator.py
bash tools/validate_reorg.sh all
```

## Rules

- treat `control-standards/rag/` as the authoritative input for AI-readable automation
- do not use `control-standards/restricted/` as AI-readable source material
- treat `control-standards/work/` as non-authoritative
