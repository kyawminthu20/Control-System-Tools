# Control System Tools Workspace

This repository combines two related concerns:

- an industrial automation standards intelligence knowledge base
- a project workspace for building tools and interfaces on top of that knowledge

The authoritative engineering content lives in `control-standards/rag/`. The active project-tracking workflow lives in `project_state/`.

## Current Project Focus

The repository is currently in **Phase 1** of a personal-use web project intended for **GitHub Pages**.

In this phase, the goal is to turn the existing standards knowledge base into a simple static web experience that helps navigate standards families, architecture models, scenarios, and related engineering guidance.

## Start Here

- [PROJECT_STARTUP_CONTEXT.md](/Users/kyawminthu/Dev/Control System Tools/PROJECT_STARTUP_CONTEXT.md) for repository orientation
- [control-standards/README.md](/Users/kyawminthu/Dev/Control System Tools/control-standards/README.md) for the product root
- [project_state/project_state.md](/Users/kyawminthu/Dev/Control System Tools/project_state/project_state.md) for the current implementation phase and backlog
- [project_state/environment.md](/Users/kyawminthu/Dev/Control System Tools/project_state/environment.md) for runtime and deployment requirements
- [project_state/how_to.md](/Users/kyawminthu/Dev/Control System Tools/project_state/how_to.md) for setup and run instructions
- [project_state/change_log.md](/Users/kyawminthu/Dev/Control System Tools/project_state/change_log.md) for project-level changes

## Repository Roles

- `control-standards/`: product content, standards knowledge, governance, work areas, and archive
- `project_state/`: active project tracking for state, run requirements, and workflow notes
- `tools/`: local automation and validation scripts
- `planning/`: reorganization and planning artifacts
- `data/`: raw or shared datasets

## Important Boundary

The website or application layer is not the authoritative standards source.

Authoritative standards guidance remains in `control-standards/rag/`. Any site or app built in this repository should be treated as a presentation and navigation layer on top of that corpus.
