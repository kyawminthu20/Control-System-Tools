<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DESIGN_INTEGRATION_PLAN
-->

# Electrical and Practical Circuit Analysis Topics Integration Plan

## Purpose

This note explains how the current `electrical_and_practical_circuit_analysis_topics` folder can be integrated into the larger project without mixing basic electrical theory with authoritative standards content.

It also identifies:

- what these notes are good for
- where they should be promoted in `rag/`
- which equations and theories should become canonical project assets
- which content should remain transcript-derived WIP only

## Current assessment

This folder is useful, but it is not yet integrated into the project architecture.

Its strengths are:

- the mixed transcript was split into coherent topics
- the files separate theory from practical component basics
- the notes already capture the main engineering ideas at a digestible level

Its weaknesses are:

- there is no routing from these files into canonical `rag` destinations
- equations are mentioned, but there is no single curated equation set for the project
- theory, bench practice, and design-use content are mixed together
- there is no clear promotion target for each file
- the current layout is good for reading, but not yet good for reuse by training, design, or troubleshooting modules

## Important integration rule

These notes should not be promoted directly into `control-standards/rag/standards_intelligence/`.

Most of this folder is electrical theory, not standards interpretation.

The correct integration path is:

1. promote theory into `rag/training_modules/`
2. promote practical calculations into `rag/design_framework/`
3. promote applied checks into `rag/commissioning_checklists/` only where they support field work
4. reference standards only where safety, conductor selection, stored energy, or equipment application overlaps with actual NEC/NFPA/IEC content

## Best fit in the project

### 1. `rag/training_modules/`

This is the best home for most of the current folder.

Recommended initial structure:

- `rag/training_modules/electrical_fundamentals/electrical_quantities_and_circuit_language.md`
- `rag/training_modules/electrical_fundamentals/series_parallel_and_divider_methods.md`
- `rag/training_modules/electrical_fundamentals/kirchhoff_laws_and_systematic_analysis.md`
- `rag/training_modules/electrical_fundamentals/equivalent_circuit_methods.md`
- `rag/training_modules/electronics_basics/resistors_capacitors_and_basic_ratings.md`
- `rag/training_modules/electronics_basics/diodes_transistors_and_switching_basics.md`

These files should be rewritten as clean teaching modules, not transcript summaries.

### 2. `rag/design_framework/`

The practical calculation material should be converted into reusable engineering workflows.

Recommended starter files:

- `rag/design_framework/electrical_review/ohms_law_and_power_check_workflow.md`
- `rag/design_framework/electrical_review/basic_resistive_network_review.md`
- `rag/design_framework/electrical_review/component_selection_basics.md`
- `rag/design_framework/electrical_review/simple_signal_and_interface_circuit_notes.md`

These should answer practical questions such as:

- How do I estimate current quickly from a measured drop?
- How do I check resistor wattage margin?
- When is a divider acceptable and when is it too heavily loaded?
- What simple component classes are appropriate for signal, suppression, switching, or indication?

### 3. `rag/commissioning_checklists/`

Only a small part of this folder belongs here, but some of it is useful.

Recommended checklist seeds:

- basic low-voltage interface circuit polarity check
- resistor power and temperature margin check
- stored-energy capacitor discharge awareness check
- diode orientation and suppression-device verification check

This is secondary to training and design framework work.

### 4. `rag/troubleshooting_engine/`

Some topics are good seeds for basic fault logic, especially where technicians misread simple circuits.

Possible starter nodes:

- unexpected voltage at a divider output
- wrong polarity or diode orientation
- resistor overheating
- capacitor ageing or dried-out smoothing capacitor symptoms
- transistor output not switching load

## Recommended topic layout for the project

The current folder is readable, but the project needs a cleaner reusable layout.

Recommended canonical layout:

### A. Electrical quantities and circuit language

Purpose:
Define voltage, current, resistance, power, nodes, branches, loops, sources, and passive elements.

Simple explanation:
This is the vocabulary layer. If the project wants AI or humans to reason well about circuits, this is the first layer they need.

Key files to derive:

- electrical quantities
- circuit topology vocabulary
- passive vs source elements

### B. Resistive network simplification

Purpose:
Cover series resistance, parallel resistance, divider behavior, and loading effects.

Simple explanation:
This is the "recognize the shape first" layer. Many circuits become easy once the obvious reduction is seen.

Key files to derive:

- series and parallel reduction
- voltage divider behavior
- current divider behavior
- divider loading and limits

### C. Systematic solution methods

Purpose:
Cover KCL, KVL, nodal analysis, and loop analysis.

Simple explanation:
This is the "when the circuit stops being obvious" layer. These methods provide a reliable way to solve circuits that cannot be reduced mentally in one step.

Key files to derive:

- KCL and node analysis
- KVL and loop analysis
- sign convention and setup discipline

### D. Equivalent-circuit methods

Purpose:
Cover source transformations, Thevenin, Norton, and superposition.

Simple explanation:
This is the simplification-tool layer. Instead of solving the original circuit directly, you replace it with an equivalent form that is easier to understand.

Key files to derive:

- source transformation
- Thevenin and Norton equivalents
- superposition

### E. Practical component behavior

Purpose:
Cover resistors, capacitors, diodes, LEDs, zeners, bipolar transistors, MOSFETs, and IGBTs at a basic practical level.

Simple explanation:
This is the "what physical parts actually do" layer. It connects theory to real hardware choices.

Key files to derive:

- resistor basics and power rating
- capacitor basics and stored energy
- diode families and directionality
- transistor families and switching behavior

### F. Practical electrical checks

Purpose:
Turn the theory into quick engineering checks that can be reused in design reviews and troubleshooting.

Simple explanation:
This is the "what should I calculate or verify right now?" layer.

Key files to derive:

- Ohm's law quick checks
- resistor wattage and margin checks
- polarity and orientation checks
- simple measured-voltage-to-current estimation

## Equations that should become canonical project assets

These equations belong in training modules and design-framework notes, not in standards files.

### 1. Ohm's law

Core equations:

- `V = I x R`
- `I = V / R`
- `R = V / I`

Simple explanation:
Voltage is the electrical push, current is the flow, and resistance is how strongly the circuit resists that flow.

Project value:
This is the base calculation for troubleshooting, interface circuits, sensor loads, indicator LEDs, and quick field checks.

### 2. Power relationships

Core equations:

- `P = V x I`
- `P = I^2 x R`
- `P = V^2 / R`

Simple explanation:
Power tells you how fast a component is turning electrical energy into heat or useful work.

Project value:
This is critical for resistor sizing, heat awareness, and simple component survivability checks.

### 3. Series resistance

Core equation:

- `R_eq = R1 + R2 + ... + Rn`

Simple explanation:
If current must pass through each resistor one after another, each one adds more opposition.

Project value:
Useful in ladder-style signal paths and simple loading estimates.

### 4. Parallel resistance

Core equation:

- `1 / R_eq = 1 / R1 + 1 / R2 + ... + 1 / Rn`

Simple explanation:
Parallel branches create extra paths for current, so the total resistance goes down.

Project value:
Useful for load interaction, shunt paths, and equivalent input/load estimation.

### 5. Voltage divider

Core equation for a simple series divider:

- `V_out = V_s x (R_x / R_total)`

For two resistors:

- `V_out = V_s x (R2 / (R1 + R2))`

Simple explanation:
In a series string, the source voltage is split according to how much resistance each part contributes.

Project value:
Useful for reference voltages, signal scaling, and explaining why loading distorts a divider output.

### 6. Current divider

Useful two-branch form:

- `I_x = I_s x (R_other / (R_x + R_other))`

Simple explanation:
In a parallel network, the branch with lower resistance takes more current.

Project value:
Less common in direct design use than voltage dividers, but useful for understanding current sharing.

### 7. Kirchhoff's Current Law

Core equation:

- `sum(I at a node) = 0`

Simple explanation:
Current cannot disappear at a junction. Whatever flows in must flow out.

Project value:
Useful for systematic troubleshooting at connection points and multi-branch logic.

### 8. Kirchhoff's Voltage Law

Core equation:

- `sum(V around a closed loop) = 0`

Simple explanation:
A complete trip around a loop must account for every rise and drop in electrical potential.

Project value:
Useful for source/drop balance and loop-based analysis.

### 9. Nodal current expression

Core equation for a resistor between two nodes:

- `I = (V_a - V_b) / R`

Simple explanation:
The current in a resistor depends on the voltage difference across it and its resistance.

Project value:
This is the practical bridge from Ohm's law to nodal analysis.

### 10. Source transformation

Core relationship:

- `V_s = I_s x R`

Simple explanation:
A voltage source with series resistance and a current source with parallel resistance can represent the same outside behavior.

Project value:
Useful for simplifying drive/interface models and for teaching equivalent thinking.

### 11. Thevenin/Norton relationship

Core relationship:

- `V_th = I_n x R_th`

Simple explanation:
Thevenin and Norton are two equivalent ways to describe the same source network seen from its terminals.

Project value:
Useful for model reduction and load-interaction reasoning.

### 12. Capacitor baseline theory

Recommended core equations for future promotion:

- `C = Q / V`
- `E = 1/2 x C x V^2`

Simple explanation:
A capacitor stores charge and therefore stores energy. The higher the capacitance or voltage, the more stored energy it can hold.

Project value:
Useful when the project talks about stored energy, discharge delay, and capacitor safety around drives and power supplies.

## Theories that should become canonical project explanations

### 1. Circuit abstraction theory

Simple explanation:
Circuit analysis is a middle layer between raw physics and real systems. It is the level where engineering calculations become manageable.

### 2. Topology first, math second

Simple explanation:
Before solving equations, look for the shape of the circuit. Many mistakes happen because engineers jump into algebra before recognizing a simple series, parallel, or divider structure.

### 3. Sign-convention discipline

Simple explanation:
A wrong assumed direction is not a disaster. It only means the answer may come back negative, which tells you the real direction is opposite.

### 4. Equivalent-circuit thinking

Simple explanation:
Sometimes the best way to solve a circuit is not to solve the original circuit directly, but to replace part of it with an equivalent that is easier to understand.

### 5. Real components are not ideal components

Simple explanation:
The equations are clean, but physical parts have tolerances, heat limits, ageing, polarity constraints, and failure modes.

This theory is especially important for:

- capacitors
- diodes
- LEDs
- transistors
- resistor power limits

## File-by-file promotion value

### Highest-value files

- `circuit_analysis_overview_and_linear_elements.md`
  Strong seed for electrical-fundamentals training.
- `series_parallel_and_divider_methods.md`
  Strong seed for both training and design framework.
- `kcl_and_nodal_analysis.md`
  Strong seed for training and troubleshooting logic.
- `kvl_and_loop_analysis.md`
  Strong seed for training and troubleshooting logic.
- `practical_ohms_law_power_and_resistor_color_code.md`
  Strong seed for design framework and practical reviews.

### Medium-value files

- `source_transformation_and_equivalent_methods.md`
  Good for advanced training, less immediately useful for project field workflows.
- `practical_components_resistors_and_capacitors.md`
  Good for training and safety/context modules.
- `practical_components_diodes_and_transistors.md`
  Good for training and basic interface-circuit guidance.

### Lowest-value for direct compliance integration

All files in this folder are low-value for direct standards promotion.

They are not bad content. They are simply not standards-owned content.

## What should map to standards and what should not

### Suitable standards-adjacent links

Only a few narrow areas in this folder should point into standards:

- capacitor stored-energy awareness
  Link to residual-voltage and discharge expectations in `NFPA 79 Ch 7` and `IEC 60204-1 Clause 6`
- component installation and conductor sizing boundaries
  Link to `NEC Article 110`, `NEC Article 310`, and relevant `UL 508A` sections
- drives and motor electronics context
  Link to `NEC Article 430`, `NFPA 79 Ch 12`, and `IEC 60204-1 Clause 12`
- power-limited or control-circuit context
  Link to `NEC Article 725` where appropriate

### Not suitable for `standards_intelligence`

These should remain outside the authoritative standards layer unless independently rewritten:

- KCL/KVL tutorial explanations
- nodal and loop-analysis teaching content
- Thevenin/Norton/superposition teaching content
- resistor color code memory aids
- broad transistor or diode intro material
- transcript-specific analogies and worked examples

## Recommended improvements inside this folder

### 1. Add promotion tags

Each file should declare one of:

- `PROMOTION_TARGET: TRAINING_ONLY`
- `PROMOTION_TARGET: TRAINING_AND_DESIGN_FRAMEWORK_INPUT`
- `PROMOTION_TARGET: CHECKLIST_SEED`
- `PROMOTION_TARGET: HOLD_WIP`

### 2. Add a `Related project targets` section

Each file should point to the canonical destination it should help create.

Example:

- training module target
- design-framework target
- troubleshooting target
- any narrow standards cross-reference if relevant

### 3. Separate theory from component practice more explicitly

The project would reuse this material more easily if the folder were grouped as:

- `circuit_fundamentals`
- `analysis_methods`
- `equivalent_methods`
- `component_basics`
- `practical_checks`

### 4. Create one canonical equations file

A single promoted file should exist in `rag/training_modules/` or `rag/design_framework/` for:

- base electrical quantities
- main resistive-network formulas
- KCL/KVL base statements
- power formulas
- capacitor energy

Right now the equations are spread across multiple notes.

## Recommended implementation order

1. Create `rag/training_modules/electrical_fundamentals/` and promote the theory files first.
2. Create `rag/design_framework/electrical_review/` and promote the practical calculation files second.
3. Create one canonical equation sheet for electrical basics.
4. Add narrow standards cross-links only where stored energy, conductors, drives, or control-circuit rules overlap.
5. Leave the original transcript-derived files in `work/design/` as source notes.

## Short practical conclusion

This folder is valuable, but its value is educational and framework-oriented, not standards-authoritative.

The best integration approach is:

- use theory files to seed training modules
- use practical calculation files to seed design-framework content
- keep equations in one canonical project equation file
- add only narrow, justified links into standards where safety or installation rules actually overlap
