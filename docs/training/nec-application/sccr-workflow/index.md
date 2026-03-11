---
layout: training-module
title: "SCCR Workflow for Industrial Control Panels"
description: "Step-by-step workflow for determining a panel's SCCR using the UL 508A component method, and why NEC 409.110 requires SCCR marking on every ICP."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/sccr_workflow.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
---

## Purpose

This module explains what short-circuit current rating (SCCR) means for industrial control panels, why NEC 409.110 requires it to be marked on every panel, and how to determine the SCCR using the UL 508A Supplement SB component method.

---

## What SCCR means

The **short-circuit current rating (SCCR)** of an industrial control panel is the maximum available fault current (in RMS symmetrical amperes) that the panel can safely withstand without creating a fire or shock hazard, given that the proper overcurrent protective devices are in place.

SCCR is a panel-level rating — it accounts for the weakest component in the assembly. A panel may contain a 100 kA-rated main breaker, but if an unprotected contactor with a listed SCCR of only 5 kA is inside, the panel's SCCR is 5 kA until that component is either replaced or properly protected by a current-limiting device.

---

## NEC 409.110 — Marking requirement

NEC 409.110 requires that every **industrial control panel (ICP)** be marked with:

1. The **SCCR** of the panel assembly
2. The **supply voltage, frequency, and phase**
3. The **full-load current** of the panel
4. The **short-circuit current rating** in amperes (same as SCCR)

This marking must appear on or within the panel enclosure so that an installer can compare it to the **available fault current** at the installation point before connecting the panel to the supply.

> **Rule:** The panel SCCR must equal or exceed the available fault current at the point of installation. If the available fault current is 22 kA and the panel SCCR is 18 kA, the panel cannot be installed at that location without modification.

---

## Available fault current — where it comes from

The **available fault current** (AFC) is the maximum current that the utility and premises wiring system can deliver to a given point during a bolted three-phase fault. It depends on:

- Utility transformer kVA rating and impedance
- Length and impedance of service conductors and feeders
- Any current-limiting devices upstream

The AFC is typically provided by the **engineer of record** or the **utility** for the installation. Panel builders must request this value before finalizing the SCCR design. Do not assume a default value.

---

## UL 508A Supplement SB — Component method

UL 508A Supplement SB provides the standard method for calculating or verifying a panel's SCCR based on its components. The method has four steps.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
  A["Step 1\nList all components\nin the panel"]
  B["Step 2\nFind the listed SCCR\nof each component"]
  C["Step 3\nIdentify the\nlimiting component\n(lowest SCCR)"]
  D{"Step 4\nIs limiting SCCR\n≥ required AFC?"}
  E["Panel SCCR =\nlimiting component SCCR\nMark panel accordingly"]
  F["Add current-limiting device\n(fuse or CLCB) to raise SCCR\nof limiting component"]

  A --> B
  B --> C
  C --> D
  D -- Yes --> E
  D -- No --> F
  F --> B

  style E fill:#d4edda,stroke:#28a745
  style F fill:#fff3cd,stroke:#ffc107
</pre>
</div>

### Step 1 — List all components

Compile a complete bill of materials for all components that carry or switch load current:

- Main circuit breaker or fused disconnect
- Branch-circuit breakers or fuses
- Contactors and motor starters
- Overload relays
- Soft starters and VFDs
- Disconnect switches
- Terminal blocks (if current-carrying and not inherently protected)

Control-circuit-only components (relays, PLCs, 24 VDC devices) typically do not affect the panel SCCR because they are isolated from the power circuit.

### Step 2 — Find the listed SCCR of each component

The listed SCCR for each component is found in:

- The component manufacturer's datasheet or listing information
- The UL Component Recognition directory
- The component's installation instructions (which are legally binding under NEC 110.3(B))

**Key fact:** Most standard IEC-type contactors have a default listed SCCR of **5 kA** when unprotected by a current-limiting device. This is the most commonly overlooked limitation.

### Step 3 — Identify the limiting component

The panel SCCR is limited by the **lowest** individual component SCCR among all components that are not protected by a current-limiting device upstream.

**Example panel:**

| Component | Listed SCCR |
|---|---|
| Main 100 A MCCB | 65 kA |
| Branch 30 A fuses (Class J) | 200 kA |
| IEC Contactor (unprotected) | 5 kA |
| Overload relay | 5 kA (with contactor) |

Without further protection, the panel SCCR = **5 kA** (the contactor).

### Step 4 — Use current-limiting devices to raise SCCR

If the limiting component's SCCR is below the required AFC, a **current-limiting fuse or current-limiting circuit breaker (CLCB)** can be placed upstream of that component. The fuse or CLCB, in combination with the downstream component, is evaluated as a pair. Manufacturers publish **coordination tables** (sometimes called "series combination tables") showing the resulting SCCR when specific fuses protect specific contactors.

**Example:** A Class J fuse rated at 30 A upstream of the 5 kA contactor may result in a combination SCCR of 100 kA, per the manufacturer's coordination table.

After adding the current-limiting device, repeat Steps 2 and 3 with the new combination SCCR values.

---

## Practical workflow summary

| Step | Action | Tool / Source |
|---|---|---|
| 1 | Obtain available fault current for installation point | Utility or engineer of record |
| 2 | List all power-circuit components in the panel BOM | Panel drawings, BOM |
| 3 | Find listed SCCR for each component | Datasheets, UL directory |
| 4 | Identify lowest SCCR (limiting component) | Engineering review |
| 5 | Compare limiting SCCR to AFC | Pass if SCCR ≥ AFC |
| 6 | If SCCR < AFC, add current-limiting protection upstream of limiting component | Manufacturer coordination tables |
| 7 | Re-evaluate with new combination ratings | Repeat Steps 3–5 |
| 8 | Mark panel with final SCCR per NEC 409.110 | Panel label |

---

## Common mistakes

| Mistake | Impact | Correct approach |
|---|---|---|
| Assuming 5 kA is acceptable everywhere | Fails at many industrial installations (22 kA+ is common) | Obtain AFC from utility/engineer before panel design |
| Forgetting contactors and overloads in SCCR evaluation | Panel SCCR artificially high; actual protection inadequate | Include every power-circuit component in Step 1 |
| Using generic contactor SCCR without coordination table | 5 kA default does not benefit from upstream fuse unless listed as a pair | Use manufacturer's published combination SCCR data |
| Marking SCCR before confirming AFC | Panel may be shipped to a site where it cannot be legally installed | Confirm AFC before finalizing panel label |
| Confusing SCCR with continuous current rating | SCCR is a fault withstand rating, not a load current rating | Keep both ratings in context |

---

## Practical takeaway

- SCCR is the panel's worst-case fault-current withstand rating — it is the lowest component SCCR in the assembly unless protected by a current-limiting device.
- NEC 409.110 requires every ICP to be marked with its SCCR; inspectors verify this during installation.
- Standard IEC contactors typically default to 5 kA SCCR — always check and always protect with current-limiting fuses if the AFC exceeds 5 kA.
- Use manufacturer combination rating tables to raise the effective SCCR of vulnerable components through coordinated fuse protection.
- The available fault current must be confirmed from the utility or engineer of record — never assume a value.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/nec-application/grounding-bonding-panels/' | relative_url }}">&larr; Grounding and Bonding for Control Panels</a>
  <a href="{{ '/training/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/training/nec-application/conductor-ocpd-sizing/' | relative_url }}">Conductor and OCPD Sizing &rarr;</a>
</div>
