# Project Folder Organization Plan

**Created:** 2026-03-05 12:08:09 PST
**Status:** Planning Only
**Scope:** Safe reorganization of the repository without losing or overwriting data
**Primary Audience:** Future models and maintainers executing the reorganization

## Intent

Reorganize the repository so it has one clear product root, one clear authoritative knowledge root, and one clear location for automation, while preserving all existing content and migration history.

No files should be deleted during the first execution pass.

## Current Observations

The repository currently mixes product content and workspace infrastructure at the root level:

- authoritative knowledge is under `control-standards/rag/`
- workspace automation is under `tools/`
- product-facing supporting folders also exist at the root:
  - `archive/`
  - `change_management/`
  - `drafts/`
  - `drafts_DO_NOT_READ/`
  - `exports/`
  - `templates/`
  - `data/`

There is also duplication or ambiguity:

- `control-standards/design_drafts/`, `control-standards/drafts/`, and root `drafts/` all represent non-authoritative work areas
- root `exports/` overlaps with `control-standards/exports/`
- root documentation and `control-standards` documentation do not fully agree on the canonical structure
- `rag` at the repo root is a legacy symlink and must be treated as a compatibility risk until validated

## Reorganization Principles

1. Keep one canonical product root: `control-standards/`
2. Keep one canonical authoritative AI-readable root: `control-standards/rag/`
3. Keep workspace and model startup files at the repository root
4. Consolidate duplicated product folders under `control-standards/`
5. Preserve legacy paths until validation is complete
6. Move first, verify second, remove legacy paths last

## Proposed Target Structure

```text
Control System Tools/
├── AGENTS.md
├── PROJECT_STARTUP_CONTEXT.md
├── README.md
├── pyproject.toml
├── planning/
├── docs/
│   ├── STRUCTURE_SUMMARY.md
│   ├── general_change_log.md
│   └── migration/
├── tools/                      # workspace automation scripts
├── control-standards/
│   ├── README.md
│   ├── rag/                    # authoritative AI-readable knowledge
│   ├── governance/             # policies, promotion checklists, decision logs
│   ├── work/                   # in-progress but non-authoritative human work
│   ├── restricted/             # AI-forbidden raw/vendor/copyrighted content
│   ├── archive/                # superseded and historical content
│   ├── exports/                # generated deliverables
│   ├── templates/              # product templates
│   ├── modules/                # business/tool offerings, if rename is adopted
│   └── data/                   # project-specific datasets if consolidation is desired
└── .claude/ .gemini/ .mcp.json
```

## Standards Placement

Authoritative standards should remain inside `control-standards/rag/standards_intelligence/`.

Recommended target layout inside `standards_intelligence/`:

```text
control-standards/rag/standards_intelligence/
├── us/
│   ├── nec/
│   ├── nfpa79/
│   └── ul_508a/
├── international/
│   ├── machinery/
│   │   └── iec_60204_1/
│   └── functional_safety/
│       ├── iso_12100/
│       ├── iso_13849_1/
│       ├── iec_62061/
│       ├── iec_61508/
│       └── iec_61511/
├── crosswalks/
├── _index.yaml
├── _standards_map.md
└── _glossary.md
```

Mapping:

- `nec/` -> `us/nec/`
- `nfpa79/` -> `us/nfpa79/`
- `ul_508a/` -> `us/ul_508a/`
- `iec_60204_1/` -> `international/machinery/iec_60204_1/`
- `iso_12100/`, `iso_13849_1/`, `iec_62061/`, `iec_61508/`, `iec_61511/` -> `international/functional_safety/`
- `_overlap_matrix/` and `_overlap_notes/` -> `crosswalks/`

Do not perform this standards subtree reorganization until all references, indexes, and internal links are accounted for.

## Detailed Execution Plan

### Phase 0: Freeze, Inventory, and Backup

Goal: create a recovery point before any moves.

Actions:

1. Record current state:
   - full file manifest
   - directory tree
   - git status
   - file counts per top-level folder
2. Create a backup snapshot before moving files:
   - git commit if appropriate, or
   - local archive snapshot of the repo, or
   - both
3. Capture critical checksums for high-value folders:
   - `control-standards/rag/`
   - `archive/`
   - `drafts_DO_NOT_READ/`
   - `data/`

Deliverables:

- `planning/manifests/pre_move_manifest.txt`
- `planning/manifests/pre_move_checksums.txt`
- `planning/manifests/pre_move_git_status.txt`

Safety rule:

- no delete operations in this phase

### Phase 1: Clarify Documentation Before Moving Content

Goal: reduce confusion before changing paths.

Actions:

1. Update root `README.md` to describe the current canonical path: `control-standards/rag/`
2. Update `PROJECT_STARTUP_CONTEXT.md` if target naming is finalized
3. Mark legacy paths clearly in documentation:
   - root `drafts/`
   - root `exports/`
   - root `archive/`
   - root `rag` symlink
4. Add a migration note describing the intended destination of each duplicated folder

Deliverables:

- updated root `README.md`
- migration note under `planning/` or `docs/migration/`

Safety rule:

- documentation can change before file moves; data paths should not

### Phase 2: Consolidate Product Support Folders Under `control-standards/`

Goal: move product-specific folders under one product root.

Recommended move map:

| Current Path | Target Path | Notes |
|---|---|---|
| `change_management/` | `control-standards/governance/` | rename during move |
| `archive/` | `control-standards/archive/` | merge if target already exists |
| `exports/` | `control-standards/exports/` | merge carefully; preserve timestamps if possible |
| `templates/` | `control-standards/templates/` | product-specific templates |
| `drafts/` | `control-standards/work/general/` | low-risk notes and inbox material |
| `control-standards/design_drafts/` | `control-standards/work/design/` | existing in-progress design area |
| `control-standards/drafts/` | `control-standards/restricted/legacy_drafts/` | keep non-authoritative and restricted |
| `drafts_DO_NOT_READ/` | `control-standards/restricted/do_not_read/` | preserve AI-forbidden semantics |

Decision gate:

- `data/` may remain at the root if it is shared workspace data
- if it is product-specific only, move it to `control-standards/data/`

Safety rules:

- use move operations that do not overwrite without explicit review
- create target folders first
- merge folder-by-folder, not with a broad bulk move
- after each folder move, compare file counts before proceeding

### Phase 3: Rationalize Standards Content Layout

Goal: keep standards authoritative and grouped by jurisdiction and topic.

Actions:

1. Leave `control-standards/rag/` as the authoritative root
2. Reorganize only inside `control-standards/rag/standards_intelligence/`
3. Update:
   - `_index.yaml`
   - `_standards_map.md`
   - internal markdown links
   - any generated references or path assumptions
4. Keep compatibility notes for old paths until all internal links are corrected

Safety rules:

- do not edit file content and move files in the same batch unless required
- validate all internal references after each standard family move
- move one standard family at a time:
  - US standards first
  - international machinery second
  - functional safety last

### Phase 4: Optional Naming Cleanup

Goal: improve semantics after stable consolidation.

Optional renames:

- `control-standards/tools/` -> `control-standards/modules/`
- root `docs` creation for workspace-level summaries and migration records
- root `STRUCTURE_SUMMARY.md` -> `docs/STRUCTURE_SUMMARY.md`
- root `general_change_log.md` -> `docs/general_change_log.md`

Only do this phase after Phase 2 and Phase 3 validation succeeds.

### Phase 5: Compatibility and Cleanup

Goal: remove ambiguity without breaking consumers.

Actions:

1. Audit the root `rag` symlink:
   - confirm whether any tooling still relies on it
   - confirm whether the symlink target is valid
2. If needed, keep a temporary compatibility note or redirect stub
3. Remove or deprecate legacy paths only after:
   - manifests match
   - docs are updated
   - validators pass
   - no active path dependencies remain

Safety rules:

- do not remove the root `rag` symlink until dependency checks are complete
- prefer explicit deprecation markers before deletion

## No-Data-Loss Controls

These controls are mandatory for execution:

1. Never use destructive delete commands during the first pass
2. Never move and rename multiple unrelated roots in one command
3. Generate pre-move and post-move manifests
4. Compare file counts before and after each migration step
5. Preserve original files until validation is complete
6. Use a rollback snapshot that can restore the full tree
7. Validate critical authoritative folders separately from draft and archive folders

## Validation Checklist

Run after each phase:

1. `git status --short`
2. file-count comparison for moved folders
3. spot-check critical standards files:
   - NEC Article 409
   - NFPA 79 Chapter 9
   - UL 508A SCCR
   - IEC 60204-1 Clause 9
4. run `python3 tools/validate_ai_boundaries.py`
5. run `python3 tools/project_automator.py`
6. manually verify `AGENTS.md` and `PROJECT_STARTUP_CONTEXT.md` still point to the correct structure

Post-move deliverables:

- `planning/manifests/post_move_manifest.txt`
- `planning/manifests/post_move_checksums.txt`
- updated `STRUCTURE_SUMMARY.md`
- updated startup documentation

## Risk Register

### Risk 1: Legacy `rag` symlink

Observed:

- root `rag` is a symlink, not the canonical folder

Risk:

- hidden dependencies may still use it
- symlink target may be stale or external to the intended workspace layout

Mitigation:

- inspect consumers before changing it
- keep it until validation is complete

### Risk 2: Duplicate non-authoritative folders

Observed:

- root `drafts/`
- `control-standards/drafts/`
- `control-standards/design_drafts/`
- `drafts_DO_NOT_READ/`

Risk:

- wrong AI trust level may be applied to the wrong folder

Mitigation:

- consolidate into `work/` and `restricted/`
- update policy docs before or at the same time as the move

### Risk 3: Empty or placeholder integration files

Observed:

- `.claude/agents/` files are empty
- `.mcp.json` is empty
- `tools/generate_rag_index.py` is empty

Risk:

- future models may assume integrations exist when they do not

Mitigation:

- clearly document them as placeholders until implemented

## Recommended Execution Order

Use this order for the real migration:

1. Phase 0
2. Phase 1
3. Phase 2
4. Validate
5. Phase 3
6. Validate
7. Phase 4 if still desired
8. Phase 5
9. Final validation and doc refresh

## Definition of Done

The reorganization is complete when all of the following are true:

- there is one clear product root: `control-standards/`
- there is one clear authoritative knowledge root: `control-standards/rag/`
- product support folders are no longer split between root and product root
- startup docs match the real structure
- validators pass
- pre-move and post-move manifests reconcile
- legacy compatibility paths are either retired or clearly marked

## Handoff Note For Future Models

This file is a planning artifact, not proof that the migration has been executed.

Before making changes, future models should:

1. read `AGENTS.md`
2. read `PROJECT_STARTUP_CONTEXT.md`
3. verify whether this plan is still current against the live tree
4. execute one phase at a time with validation between phases
