# Phase 18 Track B — Field Engineering Section Design

**Date:** 2026-03-13
**Status:** Approved
**Author:** Claude Sonnet 4.6

---

## Goal

Surface 6 commissioning checklists from the canonical RAG as a first-class `/field-engineering/` site section. Each checklist becomes a dedicated, print-optimized page with deep cross-links into training, workflows, and lifecycle stages.

---

## URL Structure

```
/field-engineering/
  index.md
  pre-power-panel/index.md
  basic-circuit-polarity/index.md
  capacitor-discharge/index.md
  motor-nameplate-overload/index.md
  motor-rotation-verification/index.md
  drive-commissioning/index.md
```

Seven pages total: one landing + six checklist pages.

---

## RAG Source Files

All six source files are in `control-standards/rag/commissioning_checklists/checklists/`:

| Site page | RAG file |
|---|---|
| `pre-power-panel/` | `pre_power_panel_and_incoming_supply_check.md` |
| `basic-circuit-polarity/` | `basic_circuit_polarity_and_power_checks.md` |
| `capacitor-discharge/` | `capacitor_discharge_awareness_check.md` |
| `motor-nameplate-overload/` | `motor_nameplate_and_overload_setting.md` |
| `motor-rotation-verification/` | `motor_rotation_and_overload_verification.md` |
| `drive-commissioning/` | `drive_commissioning.md` |

---

## Data Model

New file: `docs/_data/field_checklists.yml`

Follows the same catalog pattern as `training_catalog.yml`. Each entry contains:

```yaml
- title: "Pre-Power Panel and Incoming Supply Check"
  url: "/field-engineering/pre-power-panel/"
  slug: "pre-power-panel"
  use_context: "Before first energization of a control panel, machine electrical system, or incoming supply connection."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md"
  related_training:
    - title: "Conductor Ampacity and Termination Temperature"
      url: "/training/fundamentals/conductor-ampacity/"
    - title: "NEC Code Reading Fundamentals"
      url: "/training/nec-application/nec-code-reading/"
    - title: "Practical Article 409 Workflow"
      url: "/training/nec-application/article-409-workflow/"
  related_workflows:
    - title: "Electrical Review Workflow"
      url: "/workflows/electrical-review/"
  related_lifecycle:
    - title: "Detailed Design"
      url: "/lifecycle/detailed-design/"
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"
```

---

## Layout

New layout: `docs/_layouts/field-checklist.html`

Mirrors `training-module.html`. Renders:

1. **Page header** — title, breadcrumb (`Field Engineering → <checklist title>`), "When to use" box from front matter `use_context`
2. **Checklist body** — page content (Markdown `- [ ]` items rendered as `<ul class="checklist">`)
3. **Cross-links block** — Related Training, Related Workflows, Related Lifecycle sections driven by `field_checklists.yml`
4. **Back link** — `← All Field Engineering Checklists`

---

## Page Front Matter

Each checklist page uses:

```yaml
---
layout: field-checklist
title: "Pre-Power Panel and Incoming Supply Check"
description: "..."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md"
---
```

Content is the checklist body extracted from the RAG file, with `- [ ]` items preserved.

---

## CSS

Additions to `docs/assets/css/main.css`:

### Checklist items

```css
ul.checklist {
  list-style: none;
  padding-left: 0;
}
ul.checklist li {
  padding: 0.35rem 0 0.35rem 1.75rem;
  position: relative;
  border-bottom: 1px solid var(--color-border);
}
ul.checklist li::before {
  content: "☐";
  position: absolute;
  left: 0;
  font-size: 1.1rem;
  color: var(--color-text-muted);
}
```

### Field checklist cards (landing page)

Reuse existing `.workflow-card` grid pattern from workflows section.

### Print additions

```css
@media print {
  .field-checklist__cross-links,
  .field-checklist__back-link { display: none; }

  ul.checklist li::before { content: "☐"; }

  .page-header__label { font-size: 0.75rem; }
}
```

Existing `@media print` rules already hide sidebar, topnav, and nav elements.

---

## Cross-linking Map

| Checklist | Related Training | Related Workflows | Related Lifecycle |
|---|---|---|---|
| Pre-Power Panel | Conductor Ampacity, NEC Code Reading, Article 409 | Electrical Review | Detailed Design, Commissioning |
| Basic Circuit Polarity | Electrical Quantities, Kirchhoff's Laws | Electrical Review | Commissioning |
| Capacitor Discharge | VFD Fundamentals, VFD/Servo Architecture | VFD Commissioning | Commissioning |
| Motor Nameplate & Overload | Motor Nameplates/Slip/Torque, Article 430 | Motor Selection | Commissioning |
| Motor Rotation & Overload | Induction Motor Basics, Motor Nameplates | Motor Troubleshooting | Commissioning |
| Drive Commissioning | VFD Fundamentals, Servo Drive Fundamentals | VFD Commissioning, Servo Commissioning | Commissioning |

### Reverse links

Training modules and workflow pages referenced above receive a "Related Checklists" block. This is added by extending `related_workflows` entries in `training_catalog.yml` with checklist URLs, and adding a `related_checklists` block to workflow pages that reference them.

---

## Navigation

### Sidebar

New `Field Engineering` section added to `docs/_includes/sidebar.html`:

```html
<details class="sidebar__section">
  <summary>Field Engineering</summary>
  <ul class="sidebar__links">
    <li><a href="/field-engineering/">All Checklists</a></li>
    <li><a href="/field-engineering/pre-power-panel/" class="sub">Pre-Power Panel</a></li>
    <li><a href="/field-engineering/basic-circuit-polarity/" class="sub">Circuit Polarity</a></li>
    <li><a href="/field-engineering/capacitor-discharge/" class="sub">Capacitor Discharge</a></li>
    <li><a href="/field-engineering/motor-nameplate-overload/" class="sub">Motor Nameplate</a></li>
    <li><a href="/field-engineering/motor-rotation-verification/" class="sub">Motor Rotation</a></li>
    <li><a href="/field-engineering/drive-commissioning/" class="sub">Drive Commissioning</a></li>
  </ul>
</details>
```

---

## Acceptance Criteria

- `/field-engineering/` landing page exists with 6 checklist cards
- All 6 checklist pages use `layout: field-checklist`
- Each page has a "When to use" box, full checklist body, and cross-links block
- Print view hides navigation, shows clean checklist with `☐` boxes
- `field_checklists.yml` drives all metadata
- Sidebar: Field Engineering section with all 6 links
- Jekyll build: clean
