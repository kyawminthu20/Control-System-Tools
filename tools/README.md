# Tools

**AI_READ_ACCESS: ALLOWED**

Local automation and validation scripts for the workspace.

## Current Script Roles

- `release_check.py`
  - runs the governed toolkit, corpus, site, generated-mirror, and metadata checks
  - reports legacy metadata debt and fails if that debt increases
- `generate_ai_method_register.py`
  - validates the 40–60-row corpus-owned AI/ML method register
  - publishes exact Jekyll data copies under `docs/_data/ai_methods/`
- `validate_ai_boundaries.py`
  - scans `control-standards/rag/` for required metadata and forbidden terms
- `fix_ai_boundaries.py`
  - repairs common metadata issues in AI-readable Markdown files
- `project_automator.py`
  - refreshes the root `STRUCTURE_SUMMARY.md` tree
- `validate_reorg.sh`
  - legacy reorganization audit; not the current release gate

## Usage

```bash
uv run python tools/release_check.py --profile full
uv run python tools/release_check.py --profile toolkit
uv run python tools/release_check.py --profile corpus
uv run python tools/release_check.py --profile site
python3 tools/validate_ai_boundaries.py
python3 tools/fix_ai_boundaries.py
python3 tools/project_automator.py
python3 tools/generate_ai_method_register.py
```

`release_check.py --profile full` is the release and deployment gate. The
reorganization script is retained only for historical audits because it checks
superseded migration artifacts and invokes a writer.

Git pre-commit can also stage `project_state/change_log.md` alongside the updated structure summary.

## Rules

- treat `control-standards/rag/` as the authoritative input for AI-readable automation
- do not use `control-standards/restricted/` as AI-readable source material
- treat `control-standards/work/` as non-authoritative
