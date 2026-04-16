# Training Site Pages Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a `/training/` section on the Jekyll site with a landing page and 24 individual module pages sourced from the RAG training_modules layer.

**Architecture:** One landing page lists all 24 modules in 3 groups (fundamentals, electrical-machines, nec-application). Each module gets its own `docs/training/<group>/<slug>/index.md` page. Content is written fresh per page from the RAG source. Sidebar gets a new collapsed Training section.

**Tech Stack:** Jekyll 4.2, Markdown front matter, vanilla HTML/CSS (no new dependencies), existing `default` layout, existing `.page-header` / `.badge` CSS classes.

**Design doc:** `docs/plans/2026-03-09-training-site-pages-design.md`

---

## Before You Start

Read these files for layout and front matter patterns:
- `docs/standards/us-electrical/nec/index.md` — front matter pattern
- `docs/industries/offshore/index.md` — recent page pattern
- `docs/_includes/sidebar.html` — sidebar structure
- `docs/training/` RAG sources in `control-standards/rag/training_modules/`

Build command (run after each task to verify):
```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```
Expected output ends with: `done in X seconds` and no errors.

---

## Task 1: Landing Page + Sidebar

**Files:**
- Create: `docs/training/index.md`
- Modify: `docs/_includes/sidebar.html`

**Step 1:** Create `docs/training/index.md`:

```markdown
---
layout: default
title: "Training Modules"
description: "Electrical fundamentals, motors and drives, and NEC application — 24 self-contained training modules."
breadcrumb:
  - name: "Training"
---

<div class="page-header">
  <span class="page-header__label">Training</span>
  <h1>Training Modules</h1>
  <p>24 modules covering electrical fundamentals, motors and drives, and NEC code application. Each module is a self-contained reference derived from the <a href="https://github.com/kyawminthu20/Control-System-Tools/tree/master/control-standards/rag/training_modules">RAG training layer</a>.</p>
</div>

<div class="card-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 2rem;">
  <div class="card">
    <h3>Fundamentals</h3>
    <p>8 modules — circuit theory, passive components, equations, conductor sizing.</p>
    <a href="{{ '/fundamentals/electrical/' | relative_url }}">Browse Fundamentals &rarr;</a>
  </div>
  <div class="card">
    <h3>Electrical Machines</h3>
    <p>13 modules — induction and DC motors, VFDs, servo drives, motor selection.</p>
    <a href="{{ '/fundamentals/motors/' | relative_url }}">Browse Electrical Machines &rarr;</a>
  </div>
  <div class="card">
    <h3>NEC Application</h3>
    <p>3 modules — code reading, table navigation, motor and panel application.</p>
    <a href="{{ '/training/nec-application/' | relative_url }}">Browse NEC Application &rarr;</a>
  </div>
</div>

---

## All Modules

### Fundamentals

| Module | Topics |
|--------|--------|
| [Electrical Quantities and Circuit Language]({{ '/fundamentals/electrical/electrical-quantities/' | relative_url }}) | Voltage, current, resistance, power, circuit topology |
| [Series, Parallel, and Divider Methods]({{ '/fundamentals/electrical/series-parallel-dividers/' | relative_url }}) | Series/parallel reduction, voltage and current dividers |
| [Kirchhoff's Laws and Systematic Analysis]({{ '/fundamentals/electrical/kirchhoff-laws/' | relative_url }}) | KCL, KVL, nodal analysis, loop analysis |
| [Equivalent Circuit Methods]({{ '/fundamentals/electrical/equivalent-circuit-methods/' | relative_url }}) | Thevenin, Norton, source transformation, superposition |
| [Electrical Equations Reference]({{ '/fundamentals/electrical/electrical-equations-reference/' | relative_url }}) | Ohm's law, power, dividers, KCL/KVL, capacitor energy |
| [Passive Components]({{ '/fundamentals/electrical/passive-components/' | relative_url }}) | Resistors, capacitors, ratings, stored energy |
| [Diodes, Transistors, and Switching Basics]({{ '/fundamentals/electrical/diodes-transistors/' | relative_url }}) | Diode families, BJT, MOSFET, IGBT, flyback diodes |
| [Conductor Ampacity and Termination Temperature]({{ '/fundamentals/electrical/conductor-ampacity/' | relative_url }}) | NEC ampacity, temperature ratings, termination limits |

### Electrical Machines

| Module | Topics |
|--------|--------|
| [Induction Motor Basics]({{ '/fundamentals/motors/induction-motor-basics/' | relative_url }}) | Stator, rotating field, rotor, slip, torque production |
| [DC Motor Basics]({{ '/fundamentals/motors/dc-motor-basics/' | relative_url }}) | Armature, commutator, back-EMF, speed control |
| [Motor Nameplates, Slip, and Torque]({{ '/fundamentals/motors/motor-nameplates-slip-torque/' | relative_url }}) | Nameplate data, NEMA designs, torque curve |
| [Motor Family Comparison]({{ '/fundamentals/motors/motor-family-comparison/' | relative_url }}) | Induction, DC, BLDC, PMSM, stepper overview |
| [AC vs DC Motor Comparison]({{ '/fundamentals/motors/ac-vs-dc-motors/' | relative_url }}) | Speed control, maintenance, application selection |
| [VFD Fundamentals]({{ '/fundamentals/motors/vfd-fundamentals/' | relative_url }}) | Rectifier, DC bus, inverter, V/Hz, vector control |
| [Servo Drive Fundamentals]({{ '/fundamentals/motors/servo-drive-fundamentals/' | relative_url }}) | Servo loops, encoder feedback, tuning basics |
| [VFD and Servo Architecture Diagrams]({{ '/fundamentals/motors/vfd-servo-architecture/' | relative_url }}) | System block diagrams, wiring topology |
| [BLDC, EV, and Drone Motor Comparison]({{ '/fundamentals/motors/bldc-ev-drone-motors/' | relative_url }}) | BLDC vs PMSM, EV traction, drone ESC |
| [Motor Control Methods and Operating Regions]({{ '/fundamentals/motors/motor-control-methods/' | relative_url }}) | V/Hz, FOC, DTC, field weakening, constant torque/power |
| [Motor Efficiency, Power Factor, and Losses]({{ '/fundamentals/motors/motor-efficiency-losses/' | relative_url }}) | IE efficiency classes, loss types, power factor correction |
| [Motor and VFD Equations Reference]({{ '/fundamentals/motors/motor-vfd-equations/' | relative_url }}) | Speed, torque, slip, power, VFD sizing equations |
| [Servo Feedback and Inertia Matching]({{ '/fundamentals/motors/servo-feedback-inertia/' | relative_url }}) | Encoder types, inertia ratio, stability limits |

### NEC Application

| Module | Topics |
|--------|--------|
| [NEC Code Reading Fundamentals]({{ '/training/nec-application/nec-code-reading/' | relative_url }}) | Code structure, mandatory language, exceptions, tables |
| [Working Space and Table Navigation]({{ '/training/nec-application/working-space-table-navigation/' | relative_url }}) | Table 110.26, depth/width/height, conditions of maintenance |
| [Motor and Panel Code Application]({{ '/training/nec-application/motor-panel-code-application/' | relative_url }}) | Art 430 sizing, Art 409 SCCR, Art 725 control circuits |
```

**Step 2:** Add Training section to `docs/_includes/sidebar.html`. Find the closing `</nav>` tag and insert before it:

```html
  <details class="sidebar__section">
    <summary>Training</summary>
    <ul class="sidebar__links">
      <li><a href="{{ '/training/' | relative_url }}">All Modules</a></li>
      <li><a href="{{ '/fundamentals/electrical/' | relative_url }}" class="sub">Fundamentals</a></li>
      <li><a href="{{ '/fundamentals/motors/' | relative_url }}" class="sub">Electrical Machines</a></li>
      <li><a href="{{ '/training/nec-application/' | relative_url }}" class="sub">NEC Application</a></li>
    </ul>
  </details>
```

**Step 3:** Build and verify:
```bash
cd /Users/kyawminthu/Dev/Control\ System\ Tools/docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -5
```
Expected: clean build, page count increases by 1.

**Step 4:** Commit:
```bash
git add docs/training/index.md docs/_includes/sidebar.html
git commit -m "feat(site): add training section landing page and sidebar nav"
```

---

## Task 2: Fundamentals Module Pages (8 pages)

**Files to create:**
- `docs/training/fundamentals/electrical-quantities/index.md`
- `docs/training/fundamentals/series-parallel-dividers/index.md`
- `docs/training/fundamentals/kirchhoff-laws/index.md`
- `docs/training/fundamentals/equivalent-circuit-methods/index.md`
- `docs/training/fundamentals/electrical-equations-reference/index.md`
- `docs/training/fundamentals/passive-components/index.md`
- `docs/training/fundamentals/diodes-transistors/index.md`
- `docs/training/fundamentals/conductor-ampacity/index.md`

**RAG sources to read before writing each page:**
```
control-standards/rag/training_modules/fundamentals/electrical_quantities_and_circuit_language.md
control-standards/rag/training_modules/fundamentals/series_parallel_and_divider_methods.md
control-standards/rag/training_modules/fundamentals/kirchhoff_laws_and_systematic_analysis.md
control-standards/rag/training_modules/fundamentals/equivalent_circuit_methods.md
control-standards/rag/training_modules/fundamentals/electrical_equations_reference.md
control-standards/rag/training_modules/fundamentals/passive_components_resistors_capacitors.md
control-standards/rag/training_modules/fundamentals/diodes_transistors_and_switching_basics.md
control-standards/rag/training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md
```

**Step 1:** For each module, read the RAG source file first.

**Step 2:** Write the page using this front matter and structure template:

```markdown
---
layout: default
title: "[Module Title]"
description: "[One sentence description of what this module covers]"
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Fundamentals"
    url: "/fundamentals/electrical/"
repo_path: "control-standards/rag/training_modules/fundamentals/[source_filename].md"
---

<div class="page-header">
  <span class="page-header__label">Training — Fundamentals</span>
  <h1>[Module Title]</h1>
</div>

[Content sections from RAG source — rewrite as clean site prose, preserve structure]

[## Related standards — include only if RAG source has Related standards section]

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/electrical/[prev-slug]/' | relative_url }}">&larr; [Prev Title]</a>
  <a href="{{ '/fundamentals/electrical/' | relative_url }}">↑ Fundamentals</a>
  <a href="{{ '/fundamentals/electrical/[next-slug]/' | relative_url }}">[Next Title] &rarr;</a>
</div>
```

**Module order for prev/next nav (fundamentals):**
1. electrical-quantities
2. series-parallel-dividers
3. kirchhoff-laws
4. equivalent-circuit-methods
5. electrical-equations-reference
6. passive-components
7. diodes-transistors
8. conductor-ampacity

First module: no ← link. Last module: no → link.

**Step 3:** Build and verify — no errors, page count +8.

**Step 4:** Commit:
```bash
git add docs/training/fundamentals/
git commit -m "feat(site): add 8 fundamentals training module pages"
```

---

## Task 3: Electrical Machines Module Pages (13 pages)

**Files to create:**
- `docs/training/electrical-machines/induction-motor-basics/index.md`
- `docs/training/electrical-machines/dc-motor-basics/index.md`
- `docs/training/electrical-machines/motor-nameplates-slip-torque/index.md`
- `docs/training/electrical-machines/motor-family-comparison/index.md`
- `docs/training/electrical-machines/ac-vs-dc-motors/index.md`
- `docs/training/electrical-machines/vfd-fundamentals/index.md`
- `docs/training/electrical-machines/servo-drive-fundamentals/index.md`
- `docs/training/electrical-machines/vfd-servo-architecture/index.md`
- `docs/training/electrical-machines/bldc-ev-drone-motors/index.md`
- `docs/training/electrical-machines/motor-control-methods/index.md`
- `docs/training/electrical-machines/motor-efficiency-losses/index.md`
- `docs/training/electrical-machines/motor-vfd-equations/index.md`
- `docs/training/electrical-machines/servo-feedback-inertia/index.md`

**RAG sources to read:**
```
control-standards/rag/training_modules/electrical_machines/induction_motor_basics.md
control-standards/rag/training_modules/electrical_machines/dc_motor_basics.md
control-standards/rag/training_modules/electrical_machines/motor_nameplates_slip_and_torque.md
control-standards/rag/training_modules/electrical_machines/motor_family_comparison.md
control-standards/rag/training_modules/electrical_machines/ac_vs_dc_motor_comparison.md
control-standards/rag/training_modules/electrical_machines/vfd_fundamentals.md
control-standards/rag/training_modules/electrical_machines/servo_drive_fundamentals.md
control-standards/rag/training_modules/electrical_machines/vfd_and_servo_architecture_diagrams.md
control-standards/rag/training_modules/electrical_machines/brushless_dc_ev_and_drone_motor_comparison.md
control-standards/rag/training_modules/electrical_machines/motor_control_methods_and_operating_regions.md
control-standards/rag/training_modules/electrical_machines/motor_efficiency_power_factor_and_losses.md
control-standards/rag/training_modules/electrical_machines/motor_and_vfd_equations_reference.md
control-standards/rag/training_modules/electrical_machines/servo_feedback_and_inertia_matching.md
```

**Step 1:** For each module, read the RAG source.

**Step 2:** Write each page using the same template as Task 2, with these changes:
- `page-header__label`: `Training — Electrical Machines`
- breadcrumb `name: "Electrical Machines"`, `url: "/fundamentals/motors/"`
- `repo_path` points to the correct `electrical_machines/` source file

**Module order for prev/next nav (electrical-machines):**
1. induction-motor-basics
2. dc-motor-basics
3. motor-nameplates-slip-torque
4. motor-family-comparison
5. ac-vs-dc-motors
6. vfd-fundamentals
7. servo-drive-fundamentals
8. vfd-servo-architecture
9. bldc-ev-drone-motors
10. motor-control-methods
11. motor-efficiency-losses
12. motor-vfd-equations
13. servo-feedback-inertia

**Mermaid note:** If the RAG source contains architecture diagrams described in text, convert them to Mermaid blocks using the existing `<div class="mermaid-wrap"><pre class="mermaid">` pattern. See `docs/lifecycle/index.md` for the exact pattern.

**Step 3:** Build and verify — no errors, page count +13.

**Step 4:** Commit:
```bash
git add docs/training/electrical-machines/
git commit -m "feat(site): add 13 electrical machines training module pages"
```

---

## Task 4: NEC Application Module Pages (3 pages)

**Files to create:**
- `docs/training/nec-application/nec-code-reading/index.md`
- `docs/training/nec-application/working-space-table-navigation/index.md`
- `docs/training/nec-application/motor-panel-code-application/index.md`

**RAG sources to read:**
```
control-standards/rag/training_modules/nec_application/nec_code_reading_fundamentals.md
control-standards/rag/training_modules/nec_application/working_space_and_table_navigation.md
control-standards/rag/training_modules/nec_application/motor_and_panel_code_application.md
```

**Step 1:** Read all three RAG sources.

**Step 2:** Write each page using the same template with:
- `page-header__label`: `Training — NEC Application`
- breadcrumb `name: "NEC Application"`, `url: "/training/nec-application/"`
- Add `related_standards` front matter pointing to existing NEC/NFPA79 pages:

```yaml
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
```

**Module order for prev/next nav (nec-application):**
1. nec-code-reading
2. working-space-table-navigation
3. motor-panel-code-application

**Step 3:** Build and verify — no errors, page count +3.

**Step 4:** Commit:
```bash
git add docs/training/nec-application/
git commit -m "feat(site): add 3 NEC application training module pages"
```

---

## Task 5: Final Build Verification

**Step 1:** Full clean build:
```bash
cd /Users/kyawminthu/Dev/Control\ System\ Tools/docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1 | tail -10
```
Expected: clean build, no errors. Page count should be previous count + 25.

**Step 2:** Verify training pages exist in `_site/`:
```bash
find /Users/kyawminthu/Dev/Control\ System\ Tools/docs/_site/training -name "index.html" | wc -l
```
Expected: `25`

**Step 3:** Spot-check a page renders correctly:
```bash
grep -l "VFD Fundamentals" /Users/kyawminthu/Dev/Control\ System\ Tools/docs/_site/training/electrical-machines/vfd-fundamentals/index.html
```
Expected: file path returned (not empty).

---

## Task 6: Update Project State

**Files:**
- Modify: `project_state/project_state.md` — add Phase 13 Training Pages entry
- Modify: `project_state/change_log.md` — add dated entry

**Step 1:** Add to `project_state/change_log.md`:

```markdown
### 2026-03-09 — Training site pages added

- `docs/training/index.md` — landing page, 24 modules in 3 groups
- `docs/training/fundamentals/` — 8 pages: circuit theory, components, equations
- `docs/training/electrical-machines/` — 13 pages: motors, drives, servo systems
- `docs/training/nec-application/` — 3 pages: code reading, table navigation, application
- Sidebar updated with Training section
```

**Step 2:** Add to `project_state/project_state.md` under Secondary Backlog or as new Phase 13 Training entry.

**Step 3:** Commit:
```bash
git add project_state/
git commit -m "chore(state): add training site pages to project tracking"
```

---

## Task 7: Push to Remote

```bash
cd /Users/kyawminthu/Dev/Control\ System\ Tools && git push origin master
```

Expected: GitHub Actions deploys automatically to GitHub Pages.
