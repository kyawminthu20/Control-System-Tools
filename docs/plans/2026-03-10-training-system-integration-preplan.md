# Training System Integration - Pre-Plan Notes

**Date:** 2026-03-10
**Status:** Planning Prep
**Scope:** Post-Phase 16 candidate work

## Purpose

Prepare the architecture and phase breakdown for the next planning pass after the current queued training work:

- Phase 14 — Training Curriculum Upgrade
- Phase 15 — Training Metadata And Module UX
- Phase 16 — NEC Training Expansion

This note evaluates how to connect the training system to the rest of the site so the platform behaves less like isolated documentation sections and more like a unified engineering knowledge system.

## Current Site Reality

The site already has most of the raw pieces needed for the proposed direction:

- `docs/training/` — concept-learning layer with 24 module pages
- `docs/standards/` — standards reference layer
- `docs/lifecycle/` — engineering process/lifecycle layer
- `docs/scenarios/` — applied project examples
- `docs/crosswalks/` — standard-to-standard routing and decision aids
- `control-standards/rag/design_framework/` — engineering workflows, decision trees, and review content not yet fully surfaced on the site
- `control-standards/rag/commissioning_checklists/` — field-useful checklist content not yet surfaced as a dedicated site section
- `control-standards/rag/standards_intelligence/reference_models/` — machine architecture and reference-model content that could anchor higher-level training routes

## What Is Already Partially Working

### Training -> Standards

Some training module pages already expose `related_standards` and related-standards sections.

This means the site already has the beginnings of a concept -> rule relationship model.

### Standards -> Scenarios / Crosswalks

Standards pages, scenario pages, and crosswalk pages already cross-link in several places.

This means the site already has a rule -> application relationship model, but it is not organized as a consistent training route.

### RAG workflow inventory exists

The canonical RAG already contains workflow-like assets such as:

- motor selection workflow
- motor troubleshooting decision tree
- VFD commissioning workflow
- servo commissioning workflow
- electrical review workflows
- commissioning checklists

The site mostly does not expose these as first-class pages yet.

## Main Architectural Gaps

### 1. No deliberate three-layer navigation model

The site has concept, rule, and application content, but it is not rendered as a clear chain:

- learn the concept
- read the governing rule
- apply it using a workflow, scenario, or checklist

### 2. Workflow content is present in RAG but under-surfaced on the site

There is no dedicated site-level workflow surface today. Lifecycle pages exist, but they are stage-oriented rather than task-oriented.

### 3. Training does not yet express the machine lifecycle

The site already has a lifecycle section, but the training section does not route learners through concept, design, safety, commissioning, and troubleshooting as a machine-builder path.

### 4. Scenario content exists but is not integrated into training

Scenario pages are useful, but they are not currently presented as "engineering scenarios" attached to module learning paths.

### 5. Field engineering content is not a visible top-level destination

Commissioning checklists exist in the canonical RAG, but the site does not yet present a clear Field Engineering or Commissioning Guides surface.

### 6. Reference content is distributed rather than grouped

Equation pages, reference models, and quick-reference material exist, but there is no single Reference Library route for fast lookup.

### 7. Sidebar navigation reflects content silos more than engineering use

The current sidebar separates sections by content family. It does not yet reflect how an engineer moves between learning, standards, design decisions, scenarios, and field work.

## Recommended Post-Phase 16 Phase Breakdown

## Phase 17 Candidate - Cross-Layer Knowledge Routing

**Goal:** Turn training pages into gateways into standards, lifecycle pages, scenarios, and applied engineering routes.

### Core outcomes

- Define a site-wide concept -> rule -> application pattern
- Publish a `Control Systems` training route so the new PID/control-loop corpus can appear on the site as a first-class learning track
- Standardize cross-links on training pages:
  - related standards
  - related workflows
  - related scenarios
  - relevant lifecycle stage
- Extend the training catalog data model to support cross-layer relationships
- Add a machine lifecycle training path on `/training/`
- Add interview-prep and role-based recommendations where they improve discovery

### Likely implementation surfaces

- `docs/_data/training_catalog.yml`
- training landing page and group pages
- `docs/training/control-systems/`
- individual training module pages
- selected standards pages and scenario pages for reciprocal links

### Key open decision

Decide whether "workflows" should become:

1. a new first-class site section such as `/workflows/`, or
2. a distributed pattern expressed through lifecycle pages, scenarios, and related-work blocks on training pages

This decision should be made before writing the full implementation plan.

## Phase 18 Candidate - Field Engineering And Reference Library

**Goal:** Surface high-frequency engineering-use content as dedicated site destinations.

### Core outcomes

- Create a Field Engineering or Commissioning Guides section on the site
- Publish selected commissioning checklists from the canonical RAG as site pages
- Create a Reference Library landing page for:
  - electrical equations
  - motor and drive equations
  - power relationships
  - conductor ampacity references
  - machine architecture references
- Surface decision-tree content for practical engineering choices

### Canonical content already available to reuse

- `commissioning_checklists/checklists/drive_commissioning.md`
- `commissioning_checklists/checklists/motor_rotation_and_overload_verification.md`
- `design_framework/motor_systems/motor_selection_workflow.md`
- `design_framework/motor_systems/motor_troubleshooting_decision_tree.md`
- `design_framework/motor_systems/vfd_commissioning_workflow.md`
- `design_framework/motor_systems/servo_commissioning_workflow.md`
- `standards_intelligence/reference_models/7-Layer Industrial Machine Architecture Model.md`

## Phase 19 Candidate - Safety And Machine Architecture Training Expansion

**Goal:** Fill the biggest conceptual training gap after NEC expansion: machine safety and system architecture.

### Proposed canonical RAG additions

- industrial machine architecture
- safety circuits and categories
- dual-channel safety wiring
- emergency stop architecture
- safety relays vs. safety PLC
- Performance Level vs. SIL

### Standards these modules should connect to

- ISO 13849-1
- IEC 62061
- NFPA 79
- IEC 60204-1
- IEC 62443 for architecture/cybersecurity overlap where relevant

### Why this matters

The site already has deep standards content in functional safety and machine design. Training still lacks a structured learner-facing route into those topics.

## Phase 20 Candidate - Scenario-Driven Learning Layer

**Goal:** Turn selected scenarios into direct engineering-learning routes rather than standalone examples.

### Candidate site scenarios

- selecting a motor for a conveyor
- designing a UL 508A control panel
- sizing and configuring a servo axis for a robot joint
- comparing geared vs. direct-drive eVTOL propulsion architectures using public Archer and Joby motor data

### Public-source application-page rules

Advanced public-source engineering pages should:

- be paraphrased synthesis, not raw transcript dumps
- be labeled as comparative engineering analysis rather than authoritative standards guidance
- stay separate from investment framing or company-performance claims
- link back to the relevant training pages such as motors, drives, and control-systems notes

### Relationship to existing site content

This can reuse the current `docs/scenarios/` section, but the presentation should shift from only "project examples" toward "engineering scenarios" tied to training paths and workflows.

## Planning Guidance

### What belongs in the next full plan

- cross-layer data model
- relationship blocks on training pages
- workflow-surfacing decision
- field engineering section decision
- reference library grouping approach
- scope boundaries between site-only changes and canonical RAG additions

### What should not be mixed into the current Phase 14 plan

- new workflow site section
- new field-engineering section
- safety training corpus expansion
- new scenario families

Those ideas are valid, but they will overload the current training landing-page redesign if merged too early.

## Immediate Recommendation

Finish the queued training work first:

1. Phase 14 — curriculum structure
2. Phase 15 — metadata and module UX
3. Phase 16 — NEC content depth

Then use this pre-plan to write the next implementation plan focused on cross-layer integration rather than only the training landing page.
