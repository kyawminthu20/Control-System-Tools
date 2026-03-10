<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Integrated Drive Failure Modes and Tradeoffs

## 0. Purpose

Use this note to review the main tradeoffs and failure modes introduced when the drive is integrated with the motor assembly.

## 1. Main tradeoff

Integrated architectures often improve:

- cabinet space
- wiring simplicity
- modularity
- motor-lead length

But they can worsen:

- thermal coupling
- serviceability
- field-environment exposure
- replacement cost per failure event

## 2. Common failure modes

### Thermal overstress

Typical causes:

- motor frame heat
- high ambient
- blocked cooling surfaces
- underestimated duty cycle

### EMC-related malfunction

Typical causes:

- poor grounding or bonding
- noisy field wiring
- feedback wiring too close to switching circuits
- inadequate enclosure treatment

### Enclosure or ingress failure

Typical causes:

- insufficient sealing
- washdown exposure
- vibration loosening
- contamination entry

### Functional or control instability

Typical causes:

- feedback noise
- parameter mismatch
- thermal drift
- insufficient separation of power and low-level signals

### Serviceability failure

Typical causes:

- replacement requires swapping the full assembly
- field diagnosis is poor
- spare strategy does not match integrated packaging

## 3. Tradeoff table

| Benefit | Related risk |
| --- | --- |
| shorter motor leads | field-mounted electronics exposure |
| smaller cabinet | less protected environment |
| modular installation | larger replacement assembly |
| cleaner distributed architecture | harder thermal margin at the motor |
| simpler machine wiring | more product-level complexity in the field |

## 4. Review questions

1. What is gained by integration that could not be achieved with a cabinet-mounted drive?
2. What new failure mode appears because the electronics now sit at the motor?
3. Is replacement strategy still acceptable?
4. Is the environment gentle enough for integrated electronics?
5. Is the architecture easier to install but harder to maintain?

## 5. Practical conclusion

Integrated drive packaging is a trade, not a free improvement. The right choice depends on whether the installation and service advantages outweigh the thermal, environmental, and maintenance costs.

## Related files

- [Motor-Mounted Drive Thermal and EMC Design Notes](./motor_mounted_drive_thermal_and_emc_design_notes.md)
- [Integrated Drive Serviceability and Field Replacement Review](./integrated_drive_serviceability_and_field_replacement_review.md)
