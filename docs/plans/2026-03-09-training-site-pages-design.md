# Design: Training Modules Site Pages

**Date:** 2026-03-09
**Status:** Approved

---

## Summary

Add a `/training/` section to the Jekyll site exposing the 24 RAG training modules
as individual browsable pages. One landing page + 24 individual module pages.
New `Training` section added to the sidebar.

---

## URL Structure

```
docs/training/
├── index.md
├── fundamentals/
│   ├── electrical-quantities/index.md
│   ├── series-parallel-dividers/index.md
│   ├── kirchhoff-laws/index.md
│   ├── equivalent-circuit-methods/index.md
│   ├── electrical-equations-reference/index.md
│   ├── passive-components/index.md
│   ├── diodes-transistors/index.md
│   └── conductor-ampacity/index.md
├── electrical-machines/
│   ├── induction-motor-basics/index.md
│   ├── dc-motor-basics/index.md
│   ├── motor-nameplates-slip-torque/index.md
│   ├── motor-family-comparison/index.md
│   ├── ac-vs-dc-motors/index.md
│   ├── vfd-fundamentals/index.md
│   ├── servo-drive-fundamentals/index.md
│   ├── vfd-servo-architecture/index.md
│   ├── bldc-ev-drone-motors/index.md
│   ├── motor-control-methods/index.md
│   ├── motor-efficiency-losses/index.md
│   ├── motor-vfd-equations/index.md
│   └── servo-feedback-inertia/index.md
└── nec-application/
    ├── nec-code-reading/index.md
    ├── working-space-table-navigation/index.md
    └── motor-panel-code-application/index.md
```

**Total new pages: 25** (1 landing + 24 modules)

---

## RAG Source Mapping

### Fundamentals (8 modules)

| URL slug | RAG source file |
|---|---|
| `electrical-quantities` | `training_modules/fundamentals/electrical_quantities_and_circuit_language.md` |
| `series-parallel-dividers` | `training_modules/fundamentals/series_parallel_and_divider_methods.md` |
| `kirchhoff-laws` | `training_modules/fundamentals/kirchhoff_laws_and_systematic_analysis.md` |
| `equivalent-circuit-methods` | `training_modules/fundamentals/equivalent_circuit_methods.md` |
| `electrical-equations-reference` | `training_modules/fundamentals/electrical_equations_reference.md` |
| `passive-components` | `training_modules/fundamentals/passive_components_resistors_capacitors.md` |
| `diodes-transistors` | `training_modules/fundamentals/diodes_transistors_and_switching_basics.md` |
| `conductor-ampacity` | `training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md` |

### Electrical Machines (13 modules)

| URL slug | RAG source file |
|---|---|
| `induction-motor-basics` | `training_modules/electrical_machines/induction_motor_basics.md` |
| `dc-motor-basics` | `training_modules/electrical_machines/dc_motor_basics.md` |
| `motor-nameplates-slip-torque` | `training_modules/electrical_machines/motor_nameplates_slip_and_torque.md` |
| `motor-family-comparison` | `training_modules/electrical_machines/motor_family_comparison.md` |
| `ac-vs-dc-motors` | `training_modules/electrical_machines/ac_vs_dc_motor_comparison.md` |
| `vfd-fundamentals` | `training_modules/electrical_machines/vfd_fundamentals.md` |
| `servo-drive-fundamentals` | `training_modules/electrical_machines/servo_drive_fundamentals.md` |
| `vfd-servo-architecture` | `training_modules/electrical_machines/vfd_and_servo_architecture_diagrams.md` |
| `bldc-ev-drone-motors` | `training_modules/electrical_machines/brushless_dc_ev_and_drone_motor_comparison.md` |
| `motor-control-methods` | `training_modules/electrical_machines/motor_control_methods_and_operating_regions.md` |
| `motor-efficiency-losses` | `training_modules/electrical_machines/motor_efficiency_power_factor_and_losses.md` |
| `motor-vfd-equations` | `training_modules/electrical_machines/motor_and_vfd_equations_reference.md` |
| `servo-feedback-inertia` | `training_modules/electrical_machines/servo_feedback_and_inertia_matching.md` |

### NEC Application (3 modules)

| URL slug | RAG source file |
|---|---|
| `nec-code-reading` | `training_modules/nec_application/nec_code_reading_fundamentals.md` |
| `working-space-table-navigation` | `training_modules/nec_application/working_space_and_table_navigation.md` |
| `motor-panel-code-application` | `training_modules/nec_application/motor_and_panel_code_application.md` |

---

## Landing Page Layout (`/training/`)

```
[page-header label] Training
[h1] Training Modules
[subtext] Electrical fundamentals, machines, and NEC application — 24 modules

[3-column card row]
  [card] Fundamentals       — 8 modules — circuit theory, components, equations
  [card] Electrical Machines — 13 modules — motors, drives, servo systems
  [card] NEC Application    — 3 modules — code reading, table navigation, application

[full module table]
| Module | Group | Topics |
```

---

## Individual Module Page Layout

```
[breadcrumb] Training > [Group] > [Module Title]
[page-header label] Training Module
[h1] [Module Title]

[content — written fresh from RAG source]

[## Related standards]  ← only where RAG source has standards links

[module-nav footer]
[← Previous]   [↑ Group index]   [Next →]
```

**Front matter pattern:**
```yaml
---
layout: default
title: "VFD Fundamentals"
description: "..."
breadcrumb:
  - name: "Training"
    url: /training/
  - name: "Electrical Machines"
    url: /fundamentals/motors/
repo_path: "control-standards/rag/training_modules/electrical_machines/vfd_fundamentals.md"
---
```

Content is written fresh per page, not auto-included from RAG files.

---

## Sidebar Addition

New `Training` section in `docs/_includes/sidebar.html`, collapsed by default:

```html
<details class="sidebar__section">
  <summary>Training</summary>
  <ul class="sidebar__links">
    <li><a href="/training/">All Modules</a></li>
    <li><a href="/fundamentals/electrical/" class="sub">Fundamentals</a></li>
    <li><a href="/fundamentals/motors/" class="sub">Electrical Machines</a></li>
    <li><a href="/training/nec-application/" class="sub">NEC Application</a></li>
  </ul>
</details>
```

---

## Build Order

| Task | Work |
|---|---|
| 1 | Landing page `docs/training/index.md` + sidebar update |
| 2 | 8 fundamentals module pages |
| 3 | 13 electrical machines module pages |
| 4 | 3 NEC application module pages |
| 5 | Jekyll build verify — confirm page count and no broken links |
| 6 | Update `project_state/` |
