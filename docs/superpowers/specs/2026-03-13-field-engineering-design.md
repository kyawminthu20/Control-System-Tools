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

**Structure:** A flat YAML list — no top-level key. This differs intentionally from `training_catalog.yml` (which uses `modules:`) to allow the direct Liquid lookup `site.data.field_checklists | where: "url", page.url | first`.

Complete file contents:

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

- title: "Basic Circuit Polarity and Power Checks"
  url: "/field-engineering/basic-circuit-polarity/"
  slug: "basic-circuit-polarity"
  use_context: "Before first energization of a simple low-voltage circuit or interface branch."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/basic_circuit_polarity_and_power_checks.md"
  related_training:
    - title: "Electrical Quantities and Circuit Language"
      url: "/training/fundamentals/electrical-quantities/"
    - title: "Kirchhoff's Laws and Systematic Analysis"
      url: "/training/fundamentals/kirchhoff-laws/"
  related_workflows:
    - title: "Electrical Review Workflow"
      url: "/workflows/electrical-review/"
  related_lifecycle:
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"

- title: "Capacitor Discharge Awareness Check"
  url: "/field-engineering/capacitor-discharge/"
  slug: "capacitor-discharge"
  use_context: "Whenever power electronics, DC buses, filters, or other energy-storage components may retain charge after power removal."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/capacitor_discharge_awareness_check.md"
  related_training:
    - title: "VFD Fundamentals"
      url: "/training/electrical-machines/vfd-fundamentals/"
    - title: "VFD and Servo Drive Architecture"
      url: "/training/electrical-machines/vfd-servo-architecture/"
  related_workflows:
    - title: "VFD Commissioning Workflow"
      url: "/workflows/vfd-commissioning/"
  related_lifecycle:
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"

- title: "Motor Nameplate and Overload Setting"
  url: "/field-engineering/motor-nameplate-overload/"
  slug: "motor-nameplate-overload"
  use_context: "Before energizing a motor branch or releasing a machine for initial run."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/motor_nameplate_and_overload_setting.md"
  related_training:
    - title: "Motor Nameplates, Slip, and Torque"
      url: "/training/electrical-machines/motor-nameplates-slip-torque/"
    - title: "Practical Article 430 Workflow"
      url: "/training/nec-application/article-430-workflow/"
  related_workflows:
    - title: "Motor Selection Workflow"
      url: "/workflows/motor-selection/"
  related_lifecycle:
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"

- title: "Motor Rotation and Overload Verification"
  url: "/field-engineering/motor-rotation-verification/"
  slug: "motor-rotation-verification"
  use_context: "During first powered motor check or post-maintenance motor reconnection."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/motor_rotation_and_overload_verification.md"
  related_training:
    - title: "Induction Motor Basics"
      url: "/training/electrical-machines/induction-motor-basics/"
    - title: "Motor Nameplates, Slip, and Torque"
      url: "/training/electrical-machines/motor-nameplates-slip-torque/"
  related_workflows:
    - title: "Motor Troubleshooting Decision Tree"
      url: "/workflows/motor-troubleshooting/"
  related_lifecycle:
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"

- title: "Drive Commissioning"
  url: "/field-engineering/drive-commissioning/"
  slug: "drive-commissioning"
  use_context: "During first power-up and early verification of a motor-drive system."
  repo_path: "control-standards/rag/commissioning_checklists/checklists/drive_commissioning.md"
  related_training:
    - title: "VFD Fundamentals"
      url: "/training/electrical-machines/vfd-fundamentals/"
    - title: "Servo Drive Fundamentals"
      url: "/training/electrical-machines/servo-drive-fundamentals/"
  related_workflows:
    - title: "VFD Commissioning Workflow"
      url: "/workflows/vfd-commissioning/"
    - title: "Servo Commissioning Workflow"
      url: "/workflows/servo-commissioning/"
  related_lifecycle:
    - title: "Commissioning"
      url: "/lifecycle/commissioning/"
```

---

## Layout

New layout: `docs/_layouts/field-checklist.html`

Mirrors `training-module.html`. Renders:

1. **Page header** — title, breadcrumb (`Field Engineering → <checklist title>`), "When to use" box
2. **Checklist body** — page content wrapped in `<div class="checklist-body">` by the layout; the layout wraps `{{ content }}` in this div so CSS can scope `ul li` styling inside it
3. **Cross-links block** — `<div class="field-checklist__cross-links">` containing Related Training, Related Workflows, Related Lifecycle sub-sections driven by `field_checklists.yml`
4. **Back link** — `<div class="field-checklist__back-link">← All Field Engineering Checklists</div>`

### Data lookup in layout

The layout looks up the current page's metadata using:

```liquid
{% assign checklist = site.data.field_checklists | where: "url", page.url | first %}
```

`field_checklists.yml` is a flat list (no top-level key), matching Jekyll's direct access pattern for flat data files. The `use_context` string and all cross-link arrays are read from this lookup result. The `slug` field in the data file is reserved for future filtering and is not used in the layout.

The "When to use" box renders from `checklist.use_context`, **not** from front matter. The front matter does not include a `use_context` key.

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

Content is the checklist body extracted from the RAG file. `- [ ]` items are written as plain `- ` list items (without the checkbox syntax) so Kramdown does not generate `<input type="checkbox" disabled>` elements. The CSS `::before` pseudo-element on `.checklist-body li` supplies the `☐` symbol instead.

---

## CSS

Additions to `docs/assets/css/main.css`:

### Checklist items

Scoped to `.checklist-body` (the wrapper div the layout injects around `{{ content }}`):

```css
.checklist-body ul {
  list-style: none;
  padding-left: 0;
}
.checklist-body ul li {
  padding: 0.35rem 0 0.35rem 1.75rem;
  position: relative;
  border-bottom: 1px solid var(--color-border);
}
.checklist-body ul li::before {
  content: "☐";
  position: absolute;
  left: 0;
  font-size: 1.1rem;
  color: var(--color-text-muted);
}
```

Checklist items in page content use plain `- ` syntax (not `- [ ]`) to avoid Kramdown generating `<input type="checkbox" disabled>` elements that would conflict with the `::before` symbol.

### Field checklist cards (landing page)

Reuse existing `.workflow-card` grid pattern from workflows section.

### Print additions

```css
@media print {
  .field-checklist__cross-links,
  .field-checklist__back-link { display: none; }

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

Training modules and workflow pages referenced above receive a "Related Checklists" block via two concrete changes:

**`training_catalog.yml`** — Add a `related_checklists` key to each affected module entry (same structure as `related_workflows`):

```yaml
related_checklists:
  - title: "Drive Commissioning Checklist"
    url: "/field-engineering/drive-commissioning/"
```

**`docs/_layouts/training-module.html`** — Add a conditional block after the existing Related Workflows block:

```liquid
{% if module_meta.related_checklists %}
<div class="related-checklists">
  <h4>Related Checklists</h4>
  <ul>
  {% for item in module_meta.related_checklists %}
    <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
  {% endfor %}
  </ul>
</div>
{% endif %}
```

(`module_meta` is the variable name used by `training-module.html` for its data lookup — confirmed in the existing layout.)

**Workflow pages** (e.g. `docs/workflows/vfd-commissioning/index.md`) — Add a "Related Checklists" section to the page body Markdown directly, linking to the relevant checklist pages. No layout change required for workflow pages.

---

## Navigation

### Sidebar

New `Field Engineering` section added to `docs/_includes/sidebar.html`:

```html
<details class="sidebar__section">
  <summary>Field Engineering</summary>
  <ul class="sidebar__links">
    <li><a href="{{ '/field-engineering/' | relative_url }}"{% if page.url == '/field-engineering/' %} class="active"{% endif %}>All Checklists</a></li>
    <li><a href="{{ '/field-engineering/pre-power-panel/' | relative_url }}" class="sub{% if page.url contains 'pre-power-panel' %} active{% endif %}">Pre-Power Panel</a></li>
    <li><a href="{{ '/field-engineering/basic-circuit-polarity/' | relative_url }}" class="sub{% if page.url contains 'basic-circuit-polarity' %} active{% endif %}">Circuit Polarity</a></li>
    <li><a href="{{ '/field-engineering/capacitor-discharge/' | relative_url }}" class="sub{% if page.url contains 'capacitor-discharge' %} active{% endif %}">Capacitor Discharge</a></li>
    <li><a href="{{ '/field-engineering/motor-nameplate-overload/' | relative_url }}" class="sub{% if page.url contains 'motor-nameplate-overload' %} active{% endif %}">Motor Nameplate</a></li>
    <li><a href="{{ '/field-engineering/motor-rotation-verification/' | relative_url }}" class="sub{% if page.url contains 'motor-rotation-verification' %} active{% endif %}">Motor Rotation</a></li>
    <li><a href="{{ '/field-engineering/drive-commissioning/' | relative_url }}" class="sub{% if page.url contains 'drive-commissioning' %} active{% endif %}">Drive Commissioning</a></li>
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
