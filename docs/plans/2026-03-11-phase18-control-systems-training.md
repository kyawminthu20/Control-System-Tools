# Phase 18 — Control Systems Training Track

**Date:** 2026-03-11
**Status:** Planning
**Depends on:** Phase 17 complete (workflows section, cross-layer routing)

## Goal

Build the Control Systems training track on the site. All 7 RAG corpus files are ready.
This is the fourth topic group alongside Electrical Fundamentals, Motors & Drives, and NEC.

## RAG Corpus (ready — no new files needed)

All 7 files in `control-standards/rag/training_modules/control_systems/`:

| File | Site module title |
|---|---|
| `control_theory_overview.md` | Control Theory Overview |
| `pid_control_intuitive_foundation.md` | PID Control — Intuitive Foundation |
| `pid_control_intuition.md` | PID Intuition — P, I, and D in Practice |
| `industrial_pid_implementation.md` | Industrial PID Implementation |
| `industrial_control_loop_architectures.md` | Industrial Control Loop Architectures |
| `pid_heater_control_with_contactor.md` | PID Heater Control with Contactor |
| `pid_drone_control.md` | PID in Drone and Motion Control |

## Site Pages to Build

### Group index
- `docs/training/control-systems/index.md` — group landing page (7 modules, intro, entry points)

### Module pages (7)
- `docs/training/control-systems/control-theory-overview/index.md`
- `docs/training/control-systems/pid-foundation/index.md`
- `docs/training/control-systems/pid-intuition/index.md`
- `docs/training/control-systems/industrial-pid/index.md`
- `docs/training/control-systems/control-loop-architectures/index.md`
- `docs/training/control-systems/pid-heater-control/index.md`
- `docs/training/control-systems/pid-drone-control/index.md`

## Data model additions

### training_catalog.yml
- Add `control-systems` topic group (module_count: 7)
- Add 7 module entries with level, time, type, focus, prerequisites, related_workflows
- Add "Control Systems Engineering" learning path
- Add "Control Theory → PID → Application" as a start-here audience entry

### Sidebar
- Add Control Systems link under Training section

### Recommended module sequencing

```
Control Theory Overview (Beginner, Concept)
  └── PID Foundation (Beginner, Concept)
        ├── PID Intuition (Beginner, Concept)
        │     └── Industrial PID Implementation (Intermediate, Code Application)
        │           ├── Control Loop Architectures (Intermediate, Concept)
        │           ├── PID Heater Control (Intermediate, Applied)
        │           └── PID Drone Control (Advanced, Applied)
```

## Cross-layer links

Each module should link to:
- `related_workflows`: Electrical Review Workflow (heater/process modules)
- Related standards: IEC 61511 (process control safety), IEC 62443 (control system cybersecurity)
- Related scenarios: Process Skid, Networked Safety PLC

## Module metadata targets

| Module | Level | Time | Type |
|---|---|---|---|
| Control Theory Overview | Beginner | 20 min | Concept |
| PID Foundation | Beginner | 20 min | Concept |
| PID Intuition | Beginner | 25 min | Concept |
| Industrial PID Implementation | Intermediate | 30 min | Code Application |
| Control Loop Architectures | Intermediate | 25 min | Concept |
| PID Heater Control | Intermediate | 20 min | Applied |
| PID Drone Control | Advanced | 20 min | Applied |

## Fundamentals group addition — IEC Earthing Systems

RAG file promoted: `control-standards/rag/training_modules/fundamentals/earthing_systems_iec.md`
Registered in: `training_modules/fundamentals/_index.yaml` (9 files total)

### Site page to add alongside fundamentals group
- `docs/training/fundamentals/earthing-systems-iec/index.md` — IEC Earthing System Types
- Layout: `training-module`
- Level: Beginner | Time: 20 min | Type: Concept | Focus: Controls / Panel Design
- Prerequisites: Electrical Quantities and Circuit Language
- Related workflows: Electrical Review Workflow
- Cross-link to existing NEC grounding module (`/training/nec-application/grounding-bonding-control-panels/`) as international counterpart
- training_catalog.yml: add module entry; update fundamentals module_count from 8 → 9

## Out of scope for this phase

- Control Systems workflow pages (Phase 19)
- State-space, LQR, MPC, adaptive control modules (future phases)
- IEC 61511 SIS/SIF integration with control loops (future)

## Acceptance criteria

- `/training/control-systems/` exists with 7 module pages
- All pages use `layout: training-module`
- Catalog updated: group entry, 7 module entries, learning path, start-here card
- Sidebar: Control Systems link added under Training
- Jekyll build: clean
