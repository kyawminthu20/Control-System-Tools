<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Power Distribution Design Guide

## 0. Purpose

This guide turns standards requirements into a practical review flow for control-panel and machine power distribution.

Use it when defining:

- incoming supply assumptions
- feeder and branch protection
- conductor sizing
- internal control power architecture
- grounding and bonding evidence

## 1. Where this guide fits

This is not the standard itself.

Use it after identifying the governing standards and before final drawing release.

Primary standards anchors:

- NEC Articles 110, 240, 250, 310, 409, 430, 670
- NFPA 79 Chapters 5, 6, 8, 11, 12, 15, 16
- UL 508A sections for wiring, overcurrent protection, SCCR, grounding, and marking

## 2. Design workflow

### 2.1 Define the supply boundary

Confirm:

- where facility wiring ends and machine or panel wiring begins
- nominal voltage, phase count, and frequency
- available fault current at the point of connection
- whether the assembly is a standalone industrial control panel or part of a machine

If this step is wrong, the rest of the design can be internally consistent but still noncompliant.

### 2.2 Define the main protective architecture

Choose and document:

- incoming disconnecting means
- branch-circuit protection strategy
- supplementary protection only where permitted
- SCCR basis for the full assembly

At this stage, the main rule is simple:

- branch-circuit protective devices protect conductors and supplied equipment
- supplementary protectors do not replace required branch protection

### 2.3 Size conductors using a full sequence

Do not treat conductor sizing as a one-step table lookup.

Use this sequence:

1. determine the load and duty cycle
2. select conductor type and installation method
3. determine base ampacity
4. apply ambient correction if needed
5. apply bundling or proximity adjustment if needed
6. check terminal temperature limits
7. coordinate the final conductor ampacity with the selected OCPD

This sequence is where most practical design errors occur.

### 2.4 Review internal panel power distribution

Check:

- transition from incoming conductors to branch conductors
- power distribution blocks and terminal ratings
- spacing around unfinger-safe power parts
- segregation between higher-voltage power wiring and low-voltage control or communication wiring
- conductor identification and serviceability

### 2.5 Define control power architecture

Document whether the design uses:

- control power transformer plus downstream protection
- direct 24 VDC power supply architecture
- mixed AC and DC control power

Then verify:

- primary and secondary protection
- voltage class separation
- expected inrush behavior
- maintenance and troubleshooting clarity

### 2.6 Grounding and bonding review

Confirm:

- equipment grounding conductor path
- bonding of doors, subpanels, and removable metallic parts where required
- separation between safety grounding intent and any functional/noise-grounding scheme
- terminal and hardware suitability for the selected conductor materials

### 2.7 Documentation package

Before release, the design package should clearly show:

- one-line or power-distribution diagram
- incoming supply assumptions
- conductor sizing basis
- branch protection basis
- SCCR basis
- grounding and bonding basis
- required field labels and markings

## 3. Common review failures

1. choosing the breaker before finishing conductor ampacity review
2. using conductor insulation rating as the final usable ampacity
3. leaving SCCR as an afterthought instead of designing around it
4. mixing high-voltage power and low-voltage control wiring without a clear routing basis
5. failing to define the machine-versus-facility boundary early
6. treating grounding, bonding, and noise control as the same decision

## 4. Minimum evidence checklist

- [ ] Supply voltage, phase, and fault-current assumptions recorded
- [ ] Main disconnect basis recorded
- [ ] OCPD selection basis recorded
- [ ] Conductor sizing basis recorded
- [ ] Terminal temperature limit checked
- [ ] SCCR basis recorded
- [ ] Grounding and bonding basis recorded
- [ ] Field marking requirements recorded

## 5. Related files

- [NEC_2023__Art240__overcurrent_protection.md](../../standards_intelligence/us/nec/NEC_2023__Art240__overcurrent_protection.md)
- [NEC_2023__Art250__grounding_and_bonding.md](../../standards_intelligence/us/nec/NEC_2023__Art250__grounding_and_bonding.md)
- [NEC_2023__Art310__conductors_for_general_wiring.md](../../standards_intelligence/us/nec/NEC_2023__Art310__conductors_for_general_wiring.md)
- [NEC_2023__Art409__industrial_control_panels.md](../../standards_intelligence/us/nec/NEC_2023__Art409__industrial_control_panels.md)
- [NFPA79_2024__Ch06__overcurrent_protection.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch06__overcurrent_protection.md)
- [NFPA79_2024__Ch08__grounding_and_bonding.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch08__grounding_and_bonding.md)
- [UL508A_2022__overcurrent_protection.md](../../standards_intelligence/us/ul_508a/UL508A_2022__overcurrent_protection.md)
- [UL508A_2022__wiring_methods_and_conductors.md](../../standards_intelligence/us/ul_508a/UL508A_2022__wiring_methods_and_conductors.md)
- [grounding_bonding_rules.yaml](../constraints/grounding_bonding_rules.yaml)

## 6. Change log

- 2026-03-09 — Initial guide created to seed the design-framework module and satisfy existing internal references.
