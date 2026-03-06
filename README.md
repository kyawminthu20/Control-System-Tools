# Control System Tools Workspace

This repository is a workspace for industrial automation standards content, project support material, and local automation.

The canonical product root is [control-standards](</Users/kyawminthu/Dev/Control System Tools/control-standards/README.md>). The canonical authoritative AI-readable knowledge root is `control-standards/rag/`.

## Start Here

- [AGENTS.md](/Users/kyawminthu/Dev/Control System Tools/AGENTS.md)
- [PROJECT_STARTUP_CONTEXT.md](/Users/kyawminthu/Dev/Control System Tools/PROJECT_STARTUP_CONTEXT.md)
- [control-standards/README.md](/Users/kyawminthu/Dev/Control System Tools/control-standards/README.md)
- [STRUCTURE_SUMMARY.md](/Users/kyawminthu/Dev/Control System Tools/STRUCTURE_SUMMARY.md)

## Top-Level Layout

- `control-standards/`: product content and governance
- `tools/`: workspace automation and validation scripts
- `planning/`: migration and reorganization plans
- `data/`: shared raw datasets and captures
- `rag/`: compatibility symlink to `control-standards/rag/`

## Working Rules

- Put authoritative standards and engineering knowledge in `control-standards/rag/`.
- Put process and promotion rules in `control-standards/governance/`.
- Put non-authoritative active work in `control-standards/work/`.
- Put AI-forbidden raw, copyrighted, or vendor content in `control-standards/restricted/`.
- Put historical material in `control-standards/archive/`.

## Primary Workflows

1. Research or author in `control-standards/work/` or `control-standards/restricted/` as appropriate.
2. Promote verified paraphrased content into `control-standards/rag/`.
3. Use `python3 tools/validate_ai_boundaries.py` to check AI-readable content.
4. Use `python3 tools/project_automator.py` to refresh the root structure summary.
