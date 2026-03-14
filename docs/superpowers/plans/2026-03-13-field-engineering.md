# Field Engineering Section Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Surface 6 commissioning checklists from the canonical RAG as a `/field-engineering/` site section with print-optimized pages and deep cross-links into training, workflows, and lifecycle.

**Architecture:** New `field-checklist` layout reads metadata from a flat `field_checklists.yml` data file via Liquid `where` lookup. Checklist pages use plain `- ` list syntax (not `- [ ]`) so CSS `::before` supplies the `☐` symbol without Kramdown checkbox interference. Reverse links added to `training-module.html` and workflow pages.

**Tech Stack:** Jekyll 4.2, Liquid, Kramdown, vanilla CSS. No JS required.

---

## Chunk 1: Foundation — data file, layout, CSS

### Task 1: Create `docs/_data/field_checklists.yml`

**Files:**
- Create: `docs/_data/field_checklists.yml`

- [ ] Create the file with the complete flat YAML list (no top-level key):

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

- [ ] Commit:

```bash
git add docs/_data/field_checklists.yml
git commit -m "feat(field-engineering): add field_checklists.yml data catalog"
```

---

### Task 2: Create `docs/_layouts/field-checklist.html`

**Files:**
- Create: `docs/_layouts/field-checklist.html`
- Reference: `docs/_layouts/training-module.html` (pattern to mirror)

- [ ] Create the layout:

```html
---
layout: default
---

{% assign checklist = site.data.field_checklists | where: "url", page.url | first %}

<div class="page-header">
  <span class="page-header__label">Field Engineering</span>
  <h1>{{ page.title }}</h1>
  {% if checklist %}
  <div class="checklist-use-context">
    <strong>When to use:</strong> {{ checklist.use_context }}
  </div>
  {% endif %}
</div>

<div class="checklist-body">
{{ content }}
</div>

{% if checklist %}
<div class="field-checklist__cross-links">
  {% if checklist.related_training and checklist.related_training.size > 0 %}
  <div class="cross-links-group">
    <h4>Related Training</h4>
    <ul>
      {% for item in checklist.related_training %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  {% if checklist.related_workflows and checklist.related_workflows.size > 0 %}
  <div class="cross-links-group">
    <h4>Related Workflows</h4>
    <ul>
      {% for item in checklist.related_workflows %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  {% if checklist.related_lifecycle and checklist.related_lifecycle.size > 0 %}
  <div class="cross-links-group">
    <h4>Related Lifecycle Stages</h4>
    <ul>
      {% for item in checklist.related_lifecycle %}
      <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}
</div>
{% endif %}

<div class="field-checklist__back-link">
  <a href="{{ '/field-engineering/' | relative_url }}">&larr; All Field Engineering Checklists</a>
</div>
```

- [ ] Commit:

```bash
git add docs/_layouts/field-checklist.html
git commit -m "feat(field-engineering): add field-checklist layout"
```

---

### Task 3: Add CSS to `docs/assets/css/main.css`

**Files:**
- Modify: `docs/assets/css/main.css` (append to end of file, before any existing `@media print` block — search for `/* === Print` to find the right place)

- [ ] Add checklist-body scoped styles and cross-links styles. Find the print section (`@media print`) and insert before it:

```css
/* === Field Engineering ===================================================== */

.checklist-use-context {
  background: var(--color-bg-alt);
  border-left: 3px solid var(--color-accent);
  padding: 0.6rem 1rem;
  margin: 1rem 0 1.5rem;
  font-size: 0.95rem;
}

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

.field-checklist__cross-links {
  margin-top: 2.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.cross-links-group h4 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-muted);
  margin-bottom: 0.5rem;
}

.cross-links-group ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.cross-links-group ul li {
  margin-bottom: 0.3rem;
  font-size: 0.9rem;
}

.field-checklist__back-link {
  margin-top: 2rem;
  font-size: 0.9rem;
}
```

- [ ] Add print additions inside the existing `@media print { }` block:

```css
  /* Field Engineering print */
  .field-checklist__cross-links,
  .field-checklist__back-link { display: none; }
```

- [ ] Commit:

```bash
git add docs/assets/css/main.css
git commit -m "feat(field-engineering): add checklist-body and cross-links CSS"
```

---

## Chunk 2: Pages — landing and 6 checklist pages

### Task 4: Create `docs/field-engineering/index.md` (landing page)

**Files:**
- Create: `docs/field-engineering/index.md`
- Reference: `docs/workflows/index.md` (card grid pattern to reuse)

- [ ] Create the landing page:

```markdown
---
layout: default
title: "Field Engineering"
description: "Commissioning checklists for control panels, motor branches, drives, and circuit verification — designed for field use and print."
breadcrumb:
  - name: "Field Engineering"
---

<div class="page-header">
  <span class="page-header__label">Field Engineering</span>
  <h1>Field Engineering Checklists</h1>
  <p>Structured checklists for commissioning, first energization, and field verification. Each checklist is printable and links back into relevant training and workflows.</p>
</div>

<div class="workflow-card-grid">
{% for cl in site.data.field_checklists %}
  <div class="workflow-card">
    <h3><a href="{{ cl.url | relative_url }}">{{ cl.title }}</a></h3>
    <p>{{ cl.use_context }}</p>
  </div>
{% endfor %}
</div>

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
These checklists are derived from the canonical RAG corpus. They complement, but do not replace, OEM commissioning instructions, site LOTO procedures, and applicable standards.
</div>
```

- [ ] Verify the `workflow-card-grid` and `workflow-card` CSS classes exist (they do — defined in the Workflows section of `main.css`).

- [ ] Commit:

```bash
git add docs/field-engineering/index.md
git commit -m "feat(field-engineering): add landing page"
```

---

### Task 5: Create 6 checklist pages

**Files:**
- Create: `docs/field-engineering/pre-power-panel/index.md`
- Create: `docs/field-engineering/basic-circuit-polarity/index.md`
- Create: `docs/field-engineering/capacitor-discharge/index.md`
- Create: `docs/field-engineering/motor-nameplate-overload/index.md`
- Create: `docs/field-engineering/motor-rotation-verification/index.md`
- Create: `docs/field-engineering/drive-commissioning/index.md`

**Important:** All checklist items must use plain `- ` syntax, **not** `- [ ]`. The `- [ ]` syntax causes Kramdown to render `<input type="checkbox" disabled>` which conflicts with the CSS `::before` symbol. Convert all `- [ ]` to `- ` when copying from RAG source.

- [ ] Create `docs/field-engineering/pre-power-panel/index.md`:

```markdown
---
layout: field-checklist
title: "Pre-Power Panel and Incoming Supply Check"
description: "Checklist for first energization of a control panel, machine electrical system, or incoming supply connection."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/pre_power_panel_and_incoming_supply_check.md"
---

### Incoming supply review

- Confirm the intended supply type, voltage, frequency, and phase arrangement
- Measure incoming voltage and verify it is appropriate for the equipment basis
- Check for obvious abnormal phase imbalance or upstream wiring irregularity
- Confirm phase sequence where rotation-sensitive equipment is involved

### Upstream protection review

- Confirm feeder breaker or upstream protective device basis
- Confirm disconnect suitability for the application
- Confirm conductor and protection basis have been reviewed together
- Confirm SCCR context has been reviewed where applicable

### Panel inspection before power

- Perform visual inspection for loose conductors, damaged insulation, or unlanded terminals
- Confirm major terminations and lugs have been checked against the intended torque basis
- Confirm no obvious foreign objects, debris, or shipping restraints remain in the enclosure

### Grounding and bonding review

- Confirm the panel frame is bonded as intended
- Confirm the equipment grounding path is continuous to the facility grounding system
- Confirm grounding and bonding conductors are landed and identified as intended

### Control power and staged energization

- Confirm the planned first-power sequence before energization
- Isolate or stage control power where the startup method depends on controlled bring-up
- Confirm drives, power converters, or sensitive electronics are not enabled prematurely

### Stored-energy and insulation awareness

- Identify whether the system includes VFDs, DC buses, filters, or other stored-energy devices
- Follow OEM guidance for discharge waiting time and safe verification before contact
- Review whether insulation-resistance testing is appropriate for the connected equipment before performing it

---

This checklist does not replace OEM commissioning instructions, site LOTO and electrical safety process, or approved startup method statements.
```

- [ ] Create `docs/field-engineering/basic-circuit-polarity/index.md`:

```markdown
---
layout: field-checklist
title: "Basic Circuit Polarity and Power Checks"
description: "Checklist for first energization of a simple low-voltage circuit or interface branch."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/basic_circuit_polarity_and_power_checks.md"
---

- Confirm the intended source voltage is present
- Confirm common/reference is identified consistently
- Confirm polarity-sensitive devices are oriented correctly
- Confirm expected resistor values are installed
- Confirm resistor wattage is appropriate for expected dissipation
- Confirm no obvious shorts exist across the intended load
- Confirm the circuit matches the latest drawing revision

---

If measured values differ materially from the expected values, stop and re-check the circuit before continuing.
```

- [ ] Create `docs/field-engineering/capacitor-discharge/index.md`:

```markdown
---
layout: field-checklist
title: "Capacitor Discharge Awareness Check"
description: "Checklist for safely verifying discharge before working near power electronics, DC buses, or energy-storage components."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/capacitor_discharge_awareness_check.md"
---

- Identify whether the equipment contains significant capacitance or a DC bus
- Follow the OEM waiting-time guidance after power removal
- Verify residual voltage with the correct meter before contact
- Confirm any bleed/discharge path is intact if the design depends on it
- Treat the circuit as energized until verified otherwise

---

This checklist is a reminder layer only. Follow the equipment-specific safety procedure and site LOTO process.
```

- [ ] Create `docs/field-engineering/motor-nameplate-overload/index.md`:

```markdown
---
layout: field-checklist
title: "Motor Nameplate and Overload Setting"
description: "Checklist for verifying motor nameplate data and overload device setting before energizing a motor branch."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/motor_nameplate_and_overload_setting.md"
---

- Record motor nameplate voltage, frequency, phase, and full-load current
- Confirm the installed starter or drive matches the intended motor application
- Confirm overload device type and setting basis
- Confirm the overload setting is not a guess copied from a different motor
- Confirm the motor connection arrangement matches the nameplate or wiring diagram
- Confirm enclosure/environment suitability has been reviewed

---

Overload setting should be based on the actual motor application basis and the selected protection scheme, not on casual field assumption.
```

- [ ] Create `docs/field-engineering/motor-rotation-verification/index.md`:

```markdown
---
layout: field-checklist
title: "Motor Rotation and Overload Verification"
description: "Checklist for first powered motor check or post-maintenance motor reconnection."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/motor_rotation_and_overload_verification.md"
---

- Confirm safe conditions for jog or brief start
- Verify the driven equipment can tolerate rotation check
- Jog the motor and confirm actual rotation direction
- If rotation is wrong, correct the phase arrangement using the approved method
- Observe current and overload behavior during initial run
- Confirm overload does not nuisance-trip under expected no-load or light-load startup
- Stop and investigate immediately if current, sound, vibration, or heating is abnormal

---

Do not convert a wrong-rotation discovery into repeated trial-and-error energization. Correct intentionally, then re-test.
```

- [ ] Create `docs/field-engineering/drive-commissioning/index.md`:

```markdown
---
layout: field-checklist
title: "Drive Commissioning"
description: "Checklist for first power-up and early verification of a motor-drive system."
breadcrumb:
  - name: "Field Engineering"
    url: "/field-engineering/"
repo_path: "control-standards/rag/commissioning_checklists/checklists/drive_commissioning.md"
---

### Pre-power

- Confirm the drive model matches the intended supply and motor application
- Confirm protective earth and bonding connections are complete
- Confirm line, load, braking, and control terminals are landed intentionally
- Confirm motor cable routing and shielding approach match the design basis
- Confirm the driven machine is safe for initial motion checks

### Setup

- Record the motor nameplate data before parameter entry
- Enter or verify the required motor and control parameters
- Confirm the command source and stop behavior are understood

### First power-up

- Power the drive in a controlled state
- Confirm no immediate faults or abnormal indications appear
- Confirm the drive can be safely inhibited or disabled if behavior is unexpected

### First run

- Verify rotation direction using an approved low-risk test method
- Observe current, sound, vibration, and temperature trend during the initial run
- Stop and investigate immediately if abnormal behavior appears

### Handover basis

- Save or record key commissioning parameters
- Record any tuning changes or restrictions for future maintenance

---

Follow site safety procedures and OEM instructions for stored energy, isolation, and enabled motion throughout.
```

- [ ] Run Jekyll build to verify all pages render cleanly before committing:

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: `done in X seconds.` with no errors.

- [ ] Commit:

```bash
git add docs/field-engineering/
git commit -m "feat(field-engineering): add landing page and 6 checklist pages"
```

---

## Chunk 3: Navigation, reverse links, and verification

### Task 6: Update `docs/_includes/sidebar.html`

**Files:**
- Modify: `docs/_includes/sidebar.html`

- [ ] Find the closing `</nav>` tag at the bottom of the file and insert the Field Engineering section immediately before it:

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

- [ ] Commit:

```bash
git add docs/_includes/sidebar.html
git commit -m "feat(field-engineering): add Field Engineering sidebar section"
```

---

### Task 7: Add reverse links — `training-module.html` and `training_catalog.yml`

**Files:**
- Modify: `docs/_layouts/training-module.html`
- Modify: `docs/_data/training_catalog.yml`

**Step A — layout:**

- [ ] In `docs/_layouts/training-module.html`, find the closing `{% endif %}` that wraps the Related Workflows block (after line 45). Add the related_checklists block immediately before it:

```liquid
{% if module_meta.related_checklists and module_meta.related_checklists.size > 0 %}
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

The result should be inside the outer `{% if module_meta %}...{% endif %}` block, after the existing `related_workflows` block, before the closing `{% endif %}`.

**Step B — catalog:**

- [ ] In `docs/_data/training_catalog.yml`, add `related_checklists` to the following modules. Find each by title and add the key after its existing `related_workflows` entry (or after `featured:` if no related_workflows):

**Conductor Ampacity and Termination Temperature** (`/training/fundamentals/conductor-ampacity/`):
```yaml
    related_checklists:
      - title: "Pre-Power Panel and Incoming Supply Check"
        url: "/field-engineering/pre-power-panel/"
```

**Electrical Quantities and Circuit Language** (`/training/fundamentals/electrical-quantities/`):
```yaml
    related_checklists:
      - title: "Basic Circuit Polarity and Power Checks"
        url: "/field-engineering/basic-circuit-polarity/"
```

**Kirchhoff's Laws and Systematic Analysis** (`/training/fundamentals/kirchhoff-laws/`):
```yaml
    related_checklists:
      - title: "Basic Circuit Polarity and Power Checks"
        url: "/field-engineering/basic-circuit-polarity/"
```

**Induction Motor Basics** (`/training/electrical-machines/induction-motor-basics/`):
```yaml
    related_checklists:
      - title: "Motor Rotation and Overload Verification"
        url: "/field-engineering/motor-rotation-verification/"
```

**Motor Nameplates, Slip, and Torque** (`/training/electrical-machines/motor-nameplates-slip-torque/`):
```yaml
    related_checklists:
      - title: "Motor Nameplate and Overload Setting"
        url: "/field-engineering/motor-nameplate-overload/"
      - title: "Motor Rotation and Overload Verification"
        url: "/field-engineering/motor-rotation-verification/"
```

**VFD Fundamentals** (`/training/electrical-machines/vfd-fundamentals/`):
```yaml
    related_checklists:
      - title: "Capacitor Discharge Awareness Check"
        url: "/field-engineering/capacitor-discharge/"
      - title: "Drive Commissioning"
        url: "/field-engineering/drive-commissioning/"
```

**VFD and Servo Drive Architecture** (`/training/electrical-machines/vfd-servo-architecture/`):
```yaml
    related_checklists:
      - title: "Capacitor Discharge Awareness Check"
        url: "/field-engineering/capacitor-discharge/"
```

**Servo Drive Fundamentals** (`/training/electrical-machines/servo-drive-fundamentals/`):
```yaml
    related_checklists:
      - title: "Drive Commissioning"
        url: "/field-engineering/drive-commissioning/"
```

**Practical Article 409 Workflow** (`/training/nec-application/article-409-workflow/`):
```yaml
    related_checklists:
      - title: "Pre-Power Panel and Incoming Supply Check"
        url: "/field-engineering/pre-power-panel/"
```

**Practical Article 430 Workflow** (`/training/nec-application/article-430-workflow/`):
```yaml
    related_checklists:
      - title: "Motor Nameplate and Overload Setting"
        url: "/field-engineering/motor-nameplate-overload/"
```

**NEC Code Reading Fundamentals** (`/training/nec-application/nec-code-reading/`):
```yaml
    related_checklists:
      - title: "Pre-Power Panel and Incoming Supply Check"
        url: "/field-engineering/pre-power-panel/"
```

- [ ] Commit:

```bash
git add docs/_layouts/training-module.html docs/_data/training_catalog.yml
git commit -m "feat(field-engineering): add related_checklists reverse links to training modules"
```

---

### Task 8: Add reverse links to workflow pages

**Files:**
- Modify: `docs/workflows/electrical-review/index.md`
- Modify: `docs/workflows/vfd-commissioning/index.md`
- Modify: `docs/workflows/servo-commissioning/index.md`
- Modify: `docs/workflows/motor-selection/index.md`
- Modify: `docs/workflows/motor-troubleshooting/index.md`

- [ ] Append the following section to the bottom of each workflow page (before the last `---` or at end of file):

**`docs/workflows/electrical-review/index.md`** — append:
```markdown
## Related Checklists

- [Pre-Power Panel and Incoming Supply Check]({{ '/field-engineering/pre-power-panel/' | relative_url }})
- [Basic Circuit Polarity and Power Checks]({{ '/field-engineering/basic-circuit-polarity/' | relative_url }})
```

**`docs/workflows/vfd-commissioning/index.md`** — append:
```markdown
## Related Checklists

- [Capacitor Discharge Awareness Check]({{ '/field-engineering/capacitor-discharge/' | relative_url }})
- [Drive Commissioning]({{ '/field-engineering/drive-commissioning/' | relative_url }})
```

**`docs/workflows/servo-commissioning/index.md`** — append:
```markdown
## Related Checklists

- [Drive Commissioning]({{ '/field-engineering/drive-commissioning/' | relative_url }})
```

**`docs/workflows/motor-selection/index.md`** — append:
```markdown
## Related Checklists

- [Motor Nameplate and Overload Setting]({{ '/field-engineering/motor-nameplate-overload/' | relative_url }})
```

**`docs/workflows/motor-troubleshooting/index.md`** — append:
```markdown
## Related Checklists

- [Motor Rotation and Overload Verification]({{ '/field-engineering/motor-rotation-verification/' | relative_url }})
```

- [ ] Commit:

```bash
git add docs/workflows/
git commit -m "feat(field-engineering): add Related Checklists sections to workflow pages"
```

---

### Task 9: Final build verification and project state update

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

- [ ] Run full Jekyll build:

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```

Expected: clean build, page count increases from 116 to 123 (7 new pages).

- [ ] Verify field-engineering pages were built:

```bash
find docs/_site/field-engineering -name "index.html" | sort
```

Expected: 7 files (landing + 6 checklists).

- [ ] Update `project_state/project_state.md`:
  - Current Phase: `Phase 18 Track B COMPLETE — Field Engineering Section`
  - Next Phase: `Phase 18 Track C QUEUED — Reference Library`
  - Update page count to 123
  - Update site coverage description to include field engineering

- [ ] Update `project_state/change_log.md` with a dated entry describing the 7 new pages, layout, data catalog, CSS, sidebar, and reverse links.

- [ ] Commit everything:

```bash
git add project_state/
git commit -m "docs(project-state): update for Phase 18 Track B completion"
```

- [ ] Push:

```bash
git push origin master
```

---

## Acceptance Checklist

- [ ] `/field-engineering/` landing page renders 6 checklist cards
- [ ] All 6 checklist pages use `layout: field-checklist`
- [ ] Each checklist page shows "When to use" box, `☐`-prefixed list items, and cross-links block
- [ ] Print preview: sidebar hidden, cross-links hidden, `☐` symbols visible
- [ ] Sidebar: Field Engineering section visible with 7 links
- [ ] Active state: correct link highlighted when on each page
- [ ] Training module pages with `related_checklists` show "Related Checklists" block
- [ ] All 5 workflow pages have "Related Checklists" section at bottom
- [ ] Jekyll build: clean, 123 pages
