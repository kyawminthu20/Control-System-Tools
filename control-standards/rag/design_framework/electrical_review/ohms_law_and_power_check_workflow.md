<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Ohm's Law and Power Check Workflow

## 0. When to use this

Use this workflow for quick design review or bench troubleshooting when a circuit is simple enough that first-pass reasoning should be possible from voltage, current, resistance, and power relationships.

## 1. Inputs to collect

- source voltage
- expected or measured current
- known resistance or intended load resistance
- component wattage rating if a resistor is involved

## 2. Core equations

- `V = I x R`
- `I = V / R`
- `R = V / I`
- `P = V x I`
- `P = I^2 x R`
- `P = V^2 / R`

## 3. Review sequence

1. Decide what quantity is actually unknown.
2. Write the one equation that matches the known values.
3. Solve the unknown.
4. Cross-check the result for plausibility.
5. If a resistor is carrying power, verify wattage margin.

## 4. Power-margin rule

Do not stop after computing theoretical dissipation.

Check whether the selected part still has acceptable margin after considering:

- enclosure heat
- ambient temperature
- duty cycle
- tolerance and supply variation

## 5. Common failure patterns this catches

- indicator resistor chosen for correct ohms but insufficient wattage
- assumed current that does not match measured drop across a known resistor
- mistaken voltage assumption at the load
- power dissipation overlooked in a dropping resistor

## 6. Escalate when this workflow is no longer enough

Escalate to a deeper review if the circuit involves:

- reactive components that matter to the result
- switching waveforms
- semiconductor SOA or gate-drive design
- safety-related control behavior

## Related standards

- [NEC_2023__Art110__requirements_for_electrical_installations.md](../../standards_intelligence/us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md)
- [NFPA79_2024__Ch09__control_circuits_and_control_functions.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md)
