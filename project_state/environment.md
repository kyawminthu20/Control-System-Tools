# Environment

**Last Updated:** 2026-03-06
**Status:** Active

## Purpose

This file tracks everything required to run, validate, and eventually deploy the project.

If a dependency, version, environment variable, toolchain rule, or deployment target changes, update this file.

## Runtime Baseline

- Python requirement from `pyproject.toml`: `>=3.12`
- Local pinned Python version from `.python-version`: `3.13`
- Project package manager/workflow: `uv` is present and preferred, but direct `python3` usage also works for the current codebase

## Current Project Surface

- `main.py` is the current executable entry point
- `tools/` contains the main local automation and validation scripts
- no frontend framework, Node toolchain, or static-site generator is currently defined in the repository

## Required Tools

- `python3`
- `git`
- `bash` or compatible shell for shell scripts

## Recommended Tools

- `uv`

## Dependency Files

- `.python-version`
- `pyproject.toml`
- `uv.lock`

## Current Python Dependencies

- none declared beyond the standard library

## Environment Variables

- none required currently

## Validation And Automation Commands

- `python3 tools/project_automator.py`
- `python3 tools/validate_ai_boundaries.py`
- `python3 tools/fix_ai_boundaries.py`
- `bash tools/validate_reorg.sh all`

## Deployment Target For Phase 1

- GitHub Pages
- personal use
- static output only
- no server-side runtime assumed

## Environment Notes For Future Website Work

- If a frontend framework is added, record its version requirements here.
- If GitHub Actions are added for deployment, record their expectations here.
- If build-time environment variables appear, list them here explicitly.
