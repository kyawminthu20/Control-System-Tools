---
layout: training-module
title: "Conductor Ampacity and Termination Temperature"
description: "This module explains why conductor sizing is not just a table lookup — it requires ampacity correction, bundling adjustment, and terminal temperature checks."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "Electrical Fundamentals"
    url: "/training/fundamentals/"
repo_path: "control-standards/rag/training_modules/fundamentals/conductor_ampacity_and_termination_temperature.md"
---

## Purpose

This module explains why conductor sizing is not just "pick a wire from a table."

It covers the practical relationship between:

- conductor ampacity
- ambient temperature
- bundling of current-carrying conductors
- terminal temperature rating
- conductor overcurrent protection

## Simple explanation

Ampacity is the amount of current a conductor can carry without overheating under the conditions in which it is installed.

In real panel work, the final usable current depends on:

- what wire type is being used
- how many current-carrying conductors are grouped together
- how hot the enclosure is
- what temperature rating the connected terminals allow

## Core idea engineers miss

A conductor may have insulation rated for a higher temperature than the connected terminals.

A common mistake:

1. see a 90 °C conductor
2. take the 90 °C ampacity as the final answer
3. choose the breaker from that higher value

That shortcut is unsafe. The conductor may survive the heat, but the terminal may not.

## Working logic

Use this order:

1. identify the conductor type and installation method
2. find the starting ampacity from the applicable table
3. apply ambient-temperature correction if needed
4. apply bundling adjustment if needed
5. check the terminal temperature limit
6. select the protective device so the conductor is properly protected

## Current-carrying conductor logic

Not every conductor in a raceway or duct is treated the same way for ampacity adjustment.

- Equipment grounding conductors are part of fill and routing, but are not normally counted as current-carrying conductors for ampacity adjustment.
- Neutral conductors require circuit-specific review because some count and some do not.

This is one reason ampacity work cannot be done by wire count alone.

## Practical examples

### Example A: Hot enclosure

A conductor selected under normal room-temperature conditions may no longer be acceptable when placed in a small enclosure containing drives, power supplies, multiple contactors, and poor airflow. The elevated internal temperature changes the ampacity picture.

### Example B: Dense wire duct

A branch conductor that looks acceptable as a standalone run may require derating when routed in a crowded duct with many other current-carrying conductors. Mutual heating reduces allowable ampacity.

### Example C: 90 °C wire on 75 °C terminations

The conductor insulation may support a higher temperature, but the breaker or terminal block may be limited to 75 °C. The final usable ampacity must respect the lower terminal rating.

## Common mistakes

1. Using the highest insulation-column value as the final circuit ampacity
2. Forgetting enclosure heat
3. Forgetting bundling adjustment
4. Choosing the breaker before finishing conductor ampacity review
5. Assuming all neutrals are non-current-carrying
6. Confusing conductor marking with final usable installation rating

## Design takeaway

Ampacity is not a one-step table lookup. It is a sequence:

- table selection
- correction
- adjustment
- terminal check
- protection check

If any one of those steps is skipped, the design can fail review or overheat in service.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/fundamentals/diodes-transistors/' | relative_url }}">&larr; Diodes, Transistors, and Switching Basics</a>
  <a href="{{ '/training/fundamentals/' | relative_url }}">↑ Electrical Fundamentals</a>
  <span></span>
</div>
