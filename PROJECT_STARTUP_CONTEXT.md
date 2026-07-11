# Project Startup Context

**Last Updated:** 2026-03-05
**Purpose:** Fast orientation for a new GPT session in this repository.

## What This Project Is

This workspace is a local industrial automation intelligence repository. It combines:

- standards-oriented RAG content for control panels and machinery compliance
- governance rules for what AI may and may not read
- workspaces for active design and restricted source material
- helper scripts that validate metadata and regenerate structure documentation

## Canonical Structure Right Now

The current source-of-truth knowledge path is:

- `control-standards/rag/`

The highest-signal content today is concentrated in:

- `control-standards/rag/standards_intelligence/`

Current content reality:

- populated: grouped standards content under `us/`, `international/machinery/`, and `crosswalks/`
- scaffolded: planned functional safety folders under `international/functional_safety/`
- mostly scaffolded: `design_framework/`, `commissioning_checklists/`, `training_modules/`
- nearly empty: `troubleshooting_engine/` except for the top-level index file

## How To Read The Repo

Start here, in order:

1. This file
2. [README.md](README.md)
3. [control-standards/README.md](control-standards/README.md)
4. [control-standards/rag/standards_intelligence/_index.yaml](control-standards/rag/standards_intelligence/_index.yaml)
5. [control-standards/rag/standards_intelligence/_standards_map.md](control-standards/rag/standards_intelligence/_standards_map.md)

Then route by task:

- standards/compliance questions: `control-standards/rag/standards_intelligence/`
- process/governance questions: `control-standards/governance/`
- work-in-progress design context: `control-standards/work/design/`
- automation questions: `tools/`
- file layout questions: [STRUCTURE_SUMMARY.md](STRUCTURE_SUMMARY.md) and [control-standards/STRUCTURE_SUMMARY.md](control-standards/STRUCTURE_SUMMARY.md)

## Directory Trust Rules

Use as authoritative:

- `control-standards/rag/`
- `control-standards/governance/`
- `control-standards/templates/`
- `tools/`

Use with caution:

- `control-standards/work/design/`
- `control-standards/exports/`
- `control-standards/archive/`
- `data/`

Do not treat as authoritative:

- `control-standards/work/general/`

Do not use by default:

- `control-standards/restricted/`

## Important Current Caveats

- The root `rag/` path is a compatibility symlink to `control-standards/rag/`.
- Historical migration files and older changelog entries still reference pre-reorg paths. Treat them as historical.
- `.claude/agents/` exists but its agent files are currently empty.
- `.mcp.json` exists but is currently empty.
- `tools/generate_rag_index.py` exists but is currently empty.

## Metadata And Safety Expectations

Authoritative standards files use metadata headers and paraphrased content. Maintain these rules:

- `AI_READ_ACCESS: ALLOWED` for AI-readable authoritative content
- no verbatim copyrighted standards text
- clear status such as `DRAFT`, `REVIEWED`, or `APPROVED`
- preserve traceability and internal routing indexes

## Useful Local Scripts

- `python3 tools/validate_ai_boundaries.py`
- `python3 tools/fix_ai_boundaries.py`
- `python3 tools/project_automator.py`
- `bash tools/validate_reorg.sh all`
