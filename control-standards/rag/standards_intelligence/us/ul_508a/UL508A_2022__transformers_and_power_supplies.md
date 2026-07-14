<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: UL
STANDARD_ID: UL_508A
EDITION: 3rd Ed. (2018), revised 2025-06-26

UL_HIERARCHY:
  section: "11"
  title: "Transformers and Power Supplies"

INDEX_TAGS:
  topics: ["transformers", "power_supplies", "control_power"]
-->

# UL 508A — Transformers and Power Supplies

## 0. Scope
This section covers how control transformers and power supplies are selected and integrated to create the panel's internal control-power architecture.

## 1. Control transformer requirements
Control transformers are often used when the panel needs an AC control voltage derived from a higher incoming voltage, such as reducing `480 VAC` to `120 VAC`.

Key practical review points include:

- matching the transformer to the control load
- coordinating primary and secondary protection
- preserving the intended control architecture shown on the drawings

Transformers remain common, but they are not the only acceptable control-power approach.

## 2. Power supply selection and protection
Many modern panels use direct-input power supplies to generate `24 VDC` from the incoming supply without an intermediate `120 VAC` control layer.

This can simplify the architecture when:

- PLCs, HMIs, switches, and communication devices are predominantly `24 VDC`
- the selected power supply has an input range compatible with the panel supply
- branch protection, heat rise, and surge exposure are evaluated

Surge protective devices may be used to protect sensitive electronics such as PLCs, power supplies, displays, and other CPU-based devices from overvoltage events, but they do not replace overcurrent protection.

## 3. Secondary circuit grounding
Secondary and control-power grounding should follow the intended panel architecture and the related grounding rules for the assembly.

The key practical point is that the control-power design should be deliberate:

- do not add grounding casually
- document the secondary arrangement
- make sure the grounding/bonding strategy and device selection are compatible with the rest of the panel

## 4. Change log
- 2026-07-13 — CORRECTION: Normalized edition metadata to UL 508A, 3rd Ed. (2018), revised 2025-06-26; legacy filename retained for link stability.
- 2026-01-15 — Initial draft created
* 2026-03-09 — Added control transformer, direct DC power-supply, and surge-protection guidance from migrated panel note content.
