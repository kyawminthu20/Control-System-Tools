---
layout: default
title: Electrical Review Workflow
description: Fast design-review and bench-troubleshooting workflows for resistive circuits and basic electrical checks.
---

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/workflows/' | relative_url }}">Workflows</a> › Electrical</div>
  <h1>Electrical Review Workflow</h1>
  <p class="page-subtitle">Fast design-review and bench-troubleshooting workflows for resistive circuits: Ohm's law checks, network topology, voltage divider loading, power margin, and component sanity.</p>
  <div class="workflow-meta" style="margin-top:0.75rem;">
    <span class="workflow-badge electrical">Electrical</span>
    <span class="wf-tag">Design Review</span>
    <span class="wf-tag">Calculations</span>
  </div>
</div>

<div class="content-note">
  Use these workflows for quick design review or bench troubleshooting when the circuit is simple enough that first-pass reasoning should be possible from voltage, current, resistance, and power relationships. Escalate to deeper analysis methods when the circuit involves reactive components, switching, or semiconductor SOA.
</div>

---

## Part 1 — Ohm's Law and Power Check

Use for any resistive load, indicator resistor, or simple voltage/current verification.

### Inputs to collect

- Source voltage (V)
- Expected or measured current (I)
- Known or intended resistance (R)
- Component wattage rating if a resistor is involved

### Core equations

| Equation | Use when |
|---|---|
| `V = I × R` | Voltage unknown |
| `I = V / R` | Current unknown |
| `R = V / I` | Resistance unknown |
| `P = V × I` | Power from voltage and current |
| `P = I² × R` | Power from current and resistance |
| `P = V² / R` | Power from voltage and resistance |

### Review sequence

1. Identify the unknown quantity
2. Write the one equation that matches the known values
3. Solve the unknown
4. Cross-check the result for plausibility
5. If a resistor is carrying power, verify wattage margin

### Power-margin rule

Do not stop at theoretical dissipation. Check whether the part has acceptable margin considering:

- Enclosure heat and ambient temperature
- Duty cycle (not all circuits are continuous)
- Tolerance and supply variation

### Common faults this catches

- Indicator resistor correct ohms, insufficient wattage
- Current assumption not matching actual voltage drop across a known resistor
- Mistaken voltage assumption at the load
- Power dissipation overlooked in a dropping resistor

---

## Part 2 — Resistive Network Review

Use for series, parallel, or mixed networks; voltage dividers with loads attached.

### Step 1 — Identify the topology

Classify first:

- **Series** — same current through all elements
- **Parallel** — same voltage across all elements
- **Mixed** — series groups feeding parallel branches
- **Loaded divider** — divider output feeds a real load impedance

If the topology is misread, the rest of the calculation will be wrong.

### Step 2 — Simplify in stages

- Add series resistances directly
- Reduce parallel branches with: `1/R_total = 1/R1 + 1/R2 + ...`
- Collapse the network from the load back toward the source

### Step 3 — Check divider loading

If a divider feeds a real load, verify that the load does not shift the output voltage materially:

- If the load impedance is not much larger than the lower divider leg, the output will shift
- Calculate the loaded output explicitly — do not assume the unloaded divider equation applies

### Step 4 — Verify power ratings

For each resistor carrying meaningful drop or current, check power and confirm margin:

- `P = I² × R`
- `P = V² / R`
- `P = V × I`

Margin above calculated dissipation should account for ambient, duty, and tolerance.

### Common mistakes

| Mistake | Prevention |
|---|---|
| Assuming series when nodes do not support series current | Draw the network; label nodes before calculating |
| Using unloaded divider equation with a real load | Check load impedance vs. divider leg |
| Checking resistance but not wattage | Always run a power check after solving for current |
| Forgetting that parallel equivalent is lower than the smallest branch | `R_parallel < R_min` is a quick sanity check |

### Escalation point

Escalate to nodal, loop, Thévenin, or Norton methods if:

- Multiple interacting sources are present
- The network cannot be simplified cleanly into series/parallel stages
- Reactive components affect the result at operating frequency

---

## Related training

| Module | Topic |
|---|---|
| [Electrical Quantities and Circuit Language]({{ '/training/fundamentals/electrical-quantities/' | relative_url }}) | Voltage, current, resistance, and power basics |
| [Series, Parallel, and Divider Circuits]({{ '/training/fundamentals/series-parallel-dividers/' | relative_url }}) | Network topology and divider analysis |
| [Kirchhoff's Laws and Systematic Analysis]({{ '/training/fundamentals/kirchhoff-laws/' | relative_url }}) | KVL/KCL for multi-source networks |
| [Equivalent Circuit Methods]({{ '/training/fundamentals/equivalent-circuit-methods/' | relative_url }}) | Thévenin, Norton, and superposition |
| [Passive Components]({{ '/training/fundamentals/passive-components/' | relative_url }}) | Resistor, capacitor, and inductor behavior |

## Related workflows

| Workflow | When to use |
|---|---|
| [Motor Selection Workflow]({{ '/workflows/motor-selection/' | relative_url }}) | When resistive checks arise in a motor-circuit design |
| [VFD Commissioning Workflow]({{ '/workflows/vfd-commissioning/' | relative_url }}) | Electrical pre-checks before drive power-up |

{% include trust-boundary.html %}

## Related Checklists

- [Pre-Power Panel and Incoming Supply Check]({{ '/commissioning-templates/pre-power-panel/' | relative_url }})
- [Basic Circuit Polarity and Power Checks]({{ '/commissioning-templates/basic-circuit-polarity/' | relative_url }})
