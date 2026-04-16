# Phase 14: Training Curriculum Upgrade - Design Document

**Date:** 2026-03-10
**Status:** Approved
**Phase:** Phase 14

## Overview

Upgrade the `/training/` section from a browsable module index into a guided learning surface for industrial control engineering. The redesign should make it obvious where to start, what sequence to follow, how difficult each module is, and which standards pages connect to the training content.

The current URL structure and 24 module pages remain valid. The redesign changes the information architecture, copy, metadata model, and training-specific page components without breaking existing links.

## Problems Being Solved

- The landing page explains repository structure better than learner value.
- There is no "start here" guidance for new visitors.
- The module list is visually flat and hard to scan.
- Difficulty, time, prerequisites, and application focus are missing.
- The NEC track is visibly weaker than the fundamentals and machines tracks.
- The training page is not yet acting as a gateway into the standards library.

## Design Principles

- Learner-first language over internal architecture language.
- Stable URLs and existing module pages stay intact.
- Use one shared metadata source so the landing page and group pages stay consistent.
- Distinguish what can ship in Phase 14 from what depends on Phase 15 and Phase 16.
- Keep the trust boundary visible but move the first practical safety note higher on the page.

## URL Strategy

Keep the current training URLs unchanged:

- `/training/`
- `/fundamentals/electrical/`
- `/fundamentals/motors/`
- `/training/nec-application/`

Change display labels only:

- `Fundamentals` -> `Electrical Fundamentals`
- `Electrical Machines` -> `Motors, Drives, and Motion`
- `NEC Application` -> `NEC for Machines and Panels`

## Page Structure

The new `/training/` landing page should render in this order:

1. Page header with learner-oriented intro
2. Short verification note near the top
3. `Start Here` section with entry points by reader background
4. `Learning Paths` section with named progressions and outcomes
5. `Browse by Topic` cards using the stronger display names above
6. `All Modules` table with metadata columns
7. `Related Standards` block linking into the standards library
8. Existing trust-boundary include at the bottom

## Recommended Intro Copy

**Training Modules**

Practical learning modules for control engineers, automation technicians, and machine designers.

The modules move from electrical fundamentals to motors and drives and finally to NEC code application for machine and panel design.

They are designed for:

- control system engineers
- automation technicians
- panel designers
- machine builders
- engineering students entering industrial automation

Each module is short, focused, and intended to be read in 15-45 minutes.

## Top-of-Page Verification Note

Add a compact note directly below the intro:

> These modules explain engineering concepts and workflows. Always verify compliance decisions using official standards, manufacturer documentation, and professional engineering review.

The full trust boundary remains unchanged at the bottom via the default layout.

## Start Here Content

### New to industrial controls

Modules:

1. Electrical Quantities and Circuit Language
2. Series and Parallel Circuit Behavior
3. Kirchhoff's Laws
4. Equivalent Circuits
5. Electrical Equations Reference

Purpose:

Build the core vocabulary used throughout the rest of the training section.

### Working with motors and drives

Modules:

1. Induction Motor Basics
2. Motor Nameplates, Slip, and Torque
3. Motor Control Methods and Operating Regions
4. VFD Fundamentals
5. Servo Drive Fundamentals

Purpose:

Establish how industrial motors, drives, and motion systems behave in practice.

### Designing control panels or machines

Modules:

1. Conductor Ampacity and Termination Temperature
2. NEC Code Reading Fundamentals
3. Working Space and Table Navigation
4. Motor and Panel Code Application

Purpose:

Route users from electrical design fundamentals into applied code work.

## Learning Paths

### Controls Engineering Foundations

Modules:

1. Electrical Quantities and Circuit Language
2. Series and Parallel Circuit Behavior
3. Kirchhoff's Laws
4. Equivalent Circuits
5. Passive Components
6. Diodes, Transistors, and Switching Basics

Outcome:

Understand the electrical behavior inside industrial control systems.

### Motor and Drive Engineering

Modules:

1. Induction Motor Basics
2. Motor Nameplates, Slip, and Torque
3. Motor Control Methods and Operating Regions
4. VFD Fundamentals
5. Servo Drive Fundamentals
6. Servo Feedback and Inertia Matching
7. Motor and VFD Equations Reference

Outcome:

Understand how industrial motion systems operate and how to size drives and motors.

### Industrial Panel Design (NEC Focus)

Modules:

1. Conductor Ampacity and Termination Temperature
2. NEC Code Reading Fundamentals
3. Working Space and Table Navigation
4. Motor and Panel Code Application

Outcome:

Apply NEC rules during machine and panel design work.

### Troubleshooting and Field Service

Modules:

1. Passive Components
2. Diodes, Transistors, and Switching Basics
3. VFD Fundamentals
4. Servo Drive Fundamentals
5. Motor Control Methods and Operating Regions

Outcome:

Diagnose common faults in industrial equipment and motion systems.

## Metadata Model

Use a shared data file as the source of truth:

- `docs/_data/training_catalog.yml`

Each module record should carry at least:

- `id`
- `title`
- `url`
- `group`
- `group_label`
- `summary`
- `level`
- `time_minutes`
- `focus`
- `type`
- `prerequisites`
- `badges`
- `featured`
- `related_standards`

Example schema:

```yaml
modules:
  - id: vfd-fundamentals
    title: "VFD Fundamentals"
    url: "/fundamentals/motors/vfd-fundamentals/"
    group: "electrical-machines"
    group_label: "Motors, Drives, and Motion"
    summary: "Understand rectifier, DC bus, inverter topology, and the practical motor-system issues a VFD introduces."
    level: "Intermediate"
    time_minutes: 30
    focus: "Variable speed drives"
    type:
      - "Theory"
      - "Application"
    prerequisites:
      - "Induction Motor Basics"
    badges:
      - "Core"
      - "Field Use"
    related_standards:
      - "NEC"
      - "NFPA 79"
      - "IEC 60204-1"
      - "UL 508A"
```

## Rendering Strategy

### Landing page

`docs/training/index.md` should become a data-driven page that loops over:

- `start_here`
- `learning_paths`
- `topic_groups`
- `modules`
- `related_standards`

### Group pages

These pages should be updated to use the same catalog data filtered by group:

- `docs/training/fundamentals/index.md`
- `docs/training/electrical-machines/index.md`
- `docs/training/nec-application/index.md`

Each group page should gain:

- stronger display title
- short audience-focused intro
- recommended entry modules
- module table with metadata columns

### Module pages

Phase 14 should preserve existing module content and URLs.

Phase 15 should extend module pages with:

- metadata chips under the header
- outcome-focused one-line summary
- standardized related-standards block using existing standards pages

## Visual System

Introduce consistent training chips and badges:

- `Core`
- `Advanced`
- `Design`
- `Field Use`
- `Code Application`

Metadata chips should also support:

- level
- time
- type
- prerequisites

The landing page needs stronger hierarchy than the current flat markdown table. Desktop should favor a dense engineering table; mobile should collapse into stacked rows or card-like blocks through CSS.

## Filter Model

The landing page should support lightweight client-side filters for:

- difficulty
- topic/group
- application/focus

No new dependency is required. Vanilla JS is sufficient.

This work is intentionally deferred to Phase 15 so Phase 14 can focus on information architecture and copy first.

## Standards Gateway

Add a `Related Standards` section near the bottom of `/training/` linking to:

- NEC
- UL 508A
- NFPA 79
- IEC 60204-1

This should position the training page as an entry point into the standards library rather than a separate content island.

## Phase Boundaries

### Phase 14

- rewrite the landing page intro and structure
- add `Start Here`
- add `Learning Paths`
- add `Browse by Topic`
- add a metadata-backed all-modules table
- add a top verification note
- add a landing-page related-standards block
- upgrade the three group pages to use the same catalog structure

### Phase 15

- add metadata chips and outcomes to individual module pages
- add lightweight client-side filters and, if needed, page-scoped JS support in the default layout
- standardize module-page related-standards blocks
- refine filtering/sorting if the first pass is too limited

### Phase 16

- expand the NEC training corpus from 3 modules to at least 8-10 modules
- publish matching site pages
- rebalance the NEC track on the landing page once the new content exists

## Out of Scope for Phase 14

- changing training URLs or slug structure
- adding new external dependencies
- rewriting all 24 module pages from scratch
- adding new NEC RAG modules
- changing the global trust-boundary include
