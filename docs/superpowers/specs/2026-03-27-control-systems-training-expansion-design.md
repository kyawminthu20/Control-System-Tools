---
title: "Control Systems Training Expansion — 7 New Modules"
date: 2026-03-27
status: approved
---

## Summary

Add 7 new training modules to `docs/training/control-systems/` drawn from planning files in `planning/phase_27march26/`. Each file becomes a peer module alongside existing PID and control-theory content. The training catalog data file is updated to register all 7.

`things_to_fix.md` (lifecycle page improvements) is out of scope for this plan.

---

## Source Files

| Planning file | Target slug |
|---|---|
| `control_system_machine_state_model.md` | `machine-state-model/` |
| `interlock_permessive_safetytrips.md` | `interlocks-permissives-safety-trips/` |
| `asynchronous_faults_in_distributed_system.md` | `async-faults-distributed-systems/` |
| `deterministic vs non deterministic control.md` | `deterministic-nondeterministic-control/` |
| `servo_tuning.md` | `servo-tuning/` |
| `vibration_vs_resonance.md` | `vibration-resonance/` |
| `multi_axis_coordination.md` | `multi-axis-coordination/` |

---

## Module Metadata

| Slug | Title | Level | Time | Type |
|---|---|---|---|---|
| `machine-state-model/` | Machine State Model | Intermediate | 25 min | Concept |
| `interlocks-permissives-safety-trips/` | Interlocks, Permissives & Safety Trips | Intermediate | 20 min | Concept |
| `async-faults-distributed-systems/` | Async Faults in Distributed Systems | Advanced | 25 min | Concept |
| `deterministic-nondeterministic-control/` | Deterministic vs Non-Deterministic Control | Intermediate | 20 min | Concept |
| `servo-tuning/` | Servo Tuning Strategy | Advanced | 25 min | Technique |
| `vibration-resonance/` | Vibration and Resonance | Intermediate | 20 min | Concept |
| `multi-axis-coordination/` | Multi-Axis Coordination | Advanced | 25 min | Concept |

---

## Page Structure (each module)

**Frontmatter:**
```yaml
layout: training-module
title: "<Title>"
description: "<one-line description>"
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Control Systems"
    url: "/fundamentals/control/"
related_standards: [] # populated per module where relevant
```

**Body sections** (derived from planning file content):
1. **Purpose** — what the topic is and why it matters
2. **Core Concepts** — key definitions and distinctions (tables where applicable)
3. **How it works / Design approach** — the structured answer a controls engineer gives
4. **Engineering takeaways** — bullet list of durable principles
5. **Related modules** (optional) — links to other control-systems modules where natural

Content is adapted from the planning files. The "What they're testing" framing is dropped; the substance is kept and restructured as reference material.

---

## Data Changes

**`docs/_data/training_catalog.yml`:**
- Add 7 module entries under the `modules:` list, each with: `url`, `group: control-systems`, `group_label: Control Systems`, `title`, `summary`, `level`, `time`, `type`, `prerequisites: []`
- Update `module_count` for the `control-systems` topic group: `7` → `14`

---

## Out of Scope

- `things_to_fix.md` lifecycle page improvements — separate plan
- Changes to learning paths in `training_catalog.yml` (can be added later)
- New navigation entries beyond the catalog data file
