<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_FUNDAMENTALS
MODULE_ID: conductor_ampacity_and_termination_temperature
LEARNING_LEVEL: foundational

INDEX_TAGS:
  topics: ["conductors", "ampacity", "termination_temperature", "overcurrent_protection"]
  systems: ["industrial_control_panel", "machine"]
  keywords: ["310.16", "110.14(C)", "bundling", "ambient correction"]
-->

# Conductor Ampacity and Termination Temperature

## 0. Purpose

This module explains why conductor sizing is not just "pick a wire from a table."

It teaches the practical relationship between:

- conductor ampacity
- ambient temperature
- bundling of current-carrying conductors
- terminal temperature rating
- conductor overcurrent protection

## 1. Simple explanation

Ampacity is the amount of current a conductor can carry without overheating under the conditions in which it is installed.

That means the final usable current is affected by more than conductor size alone.

In real panel work, the answer depends on:

- what wire type is being used
- how many current-carrying conductors are grouped together
- how hot the enclosure is
- what temperature rating the connected terminals allow

## 2. Core idea engineers miss

A conductor may have insulation rated for a higher temperature than the connected terminals.

So this is a common mistake:

1. see a 90 C conductor
2. take the 90 C ampacity as the final answer
3. choose the breaker from that higher value

That shortcut is unsafe.

The conductor may be able to survive the heat, but the terminal may not.

## 3. Working logic

Use this order:

1. identify the conductor type and installation method
2. find the starting ampacity from the applicable table
3. apply ambient-temperature correction if needed
4. apply bundling adjustment if needed
5. check the terminal temperature limit
6. select the protective device so the conductor is properly protected

## 4. Current-carrying conductor logic

Not every conductor in a raceway or duct is treated the same way for ampacity adjustment.

- equipment grounding conductors are part of fill and routing, but are not normally counted as current-carrying conductors for ampacity adjustment
- neutral conductors require circuit-specific review because some count and some do not

This is one reason ampacity work cannot be done by wire count alone.

## 5. Practical examples

### Example A: Hot enclosure

You choose a conductor that looks acceptable under normal room-temperature conditions.

Then you place it in a small enclosure with:

- drives
- power supplies
- multiple contactors
- poor airflow

Now the internal temperature is higher, so the original ampacity may no longer be acceptable without correction.

### Example B: Dense wire duct

The wire size looks acceptable when viewed as a single conductor.

But the branch conductors are routed in a crowded duct with many other current-carrying conductors.

Now mutual heating reduces allowable ampacity, so the original wire choice may no longer be acceptable.

### Example C: 90 C wire on 75 C terminations

The conductor insulation may support a higher temperature, but the breaker or terminal block may be limited to a lower temperature rating.

The final usable ampacity must respect the lower terminal rating.

## 6. Common mistakes

1. using the highest insulation-column value as the final circuit ampacity
2. forgetting enclosure heat
3. forgetting bundling adjustment
4. choosing the breaker before finishing conductor ampacity review
5. assuming all neutrals are non-current-carrying
6. confusing conductor marking with final usable installation rating

## 7. Design takeaway

Ampacity is not a one-step table lookup.

It is a sequence:

- table selection
- correction
- adjustment
- terminal check
- protection check

If any one of those steps is skipped, the design can fail review or overheat in service.

## 8. Standards anchors

Use these files for the authoritative project treatment:

- [NEC_2023__Art110__requirements_for_electrical_installations.md](../../standards_intelligence/us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md)
- [NEC_2023__Art240__overcurrent_protection.md](../../standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md)
- [NEC_2023__Art310__conductors_for_general_wiring.md](../../standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md)
- [NFPA79_2024__Ch06__overcurrent_protection.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch06__overcurrent_protection.md)
- [UL508A_2022__wiring_methods_and_conductors.md](../../standards_intelligence/us/ul_508a/UL508A_2022__wiring_methods_and_conductors.md)

## 9. Change log

- 2026-03-09 — Initial training module created from transcript-derived ampacity and conductor-protection notes.
