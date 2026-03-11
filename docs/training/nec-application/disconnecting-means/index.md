---
layout: training-module
title: "Disconnecting Means for Machinery"
description: "NEC and NFPA 79 requirements for motor disconnects — permitted types, in-sight placement, lockout provisions, and VFD-specific rules."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC for Machines and Panels"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/disconnecting_means_for_machinery.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
---

## Purpose

This module covers the placement, type, and lockout requirements for motor disconnecting means under NEC Article 430 and NFPA 79. It also addresses the special case of VFDs, where many engineers place the disconnect incorrectly.

---

## Art 430.102 — The in-sight rule

NEC 430.102(B) requires a **disconnecting means** within sight of each motor and its driven machinery. "Within sight" means the disconnect must be:

- **Visible** from the motor location, and
- **Within 50 feet** of the motor

Both conditions must be satisfied. A disconnect mounted in a panel room on the other side of a wall does not meet the within-sight requirement, even if the distance is less than 50 feet, because it is not visible.

**Exception:** If a disconnect cannot be within sight due to the installation (e.g., motors in continuous-process equipment), it may be located elsewhere, but it must be capable of being locked in the open position. A written safety procedure alone is not a substitute for physical lockout capability.

---

## Permitted disconnect types

NEC 430.109 lists the disconnect types that are permitted for motors:

| Type | Conditions |
|---|---|
| Horsepower-rated motor-circuit switch (fusible or non-fusible) | Rated in HP at operating voltage; most common choice |
| Inverse-time circuit breaker (molded-case, MCCB) | Must be rated for motor duty |
| Molded-case switch (non-automatic) | Permitted; no overcurrent trip function |
| Instantaneous-trip circuit breaker | Only when used as part of a listed combination motor controller |
| Self-protected combination controller | Listed as such |

**Not permitted as a disconnect:** A general-duty toggle switch, a control-circuit switch, or a contactor by itself.

The disconnect must be a **horsepower-rated** device when used as a motor-circuit switch. A standard fusible safety switch rated only in amperes does not meet the requirement unless it also carries an HP rating at the applicable voltage.

---

## NFPA 79 Chapter 6 — Lockable main disconnect

NFPA 79:2021, Clause 6.2 requires the main incoming supply disconnect for industrial machinery to:

- Be **lockable in the open (de-energized) position** using a padlock or hasp
- Remain locked open during maintenance without requiring the lock to be removed to re-energize (i.e., a lockout/tagout (LOTO)-compatible design)
- Be located at the **point of entry of the supply conductors** to the machine or panel enclosure

NFPA 79 also requires that the main disconnect be **capable of being operated by one person** without the use of tools. Enclosed disconnect switches and circuit breakers with external operating handles satisfy this requirement; internal breakers accessed only by opening the panel door do not.

### Lockout provisions checklist

| Requirement | Source | Notes |
|---|---|---|
| Lockable in open position | NFPA 79 §6.2 | Padlock hasp or keyed lock required |
| Accessible without entering hazard zone | OSHA 1910.147 | NEC does not address LOTO directly |
| Operable without tools | NFPA 79 §6.2 | External handle required |
| Marked with function | NEC 430.102, NFPA 79 §6.2 | Label "MAIN DISCONNECT" or similar |

---

## Art 430.112 — Group motor disconnect exception

When multiple motors share the same branch circuit (permitted under Art 430.53 for small motors), Art 430.112 allows a **single disconnecting means** to serve the group, provided:

- Each motor in the group is rated not more than 2 HP, or
- The installation meets the conditions of Art 430.53(A) or 430.53(B)

In most industrial panel designs, each motor has its own branch-circuit OCPD and disconnect. The group exception is most commonly applied to multi-motor machine tools and conveyor systems where all motors run together and the group disconnect is practical.

---

## VFD-specific disconnect rules

Variable frequency drives introduce a common wiring mistake. The disconnect must be placed **upstream of the VFD input**, not between the VFD output and the motor.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
  OCPD["Branch-Circuit OCPD\nTable 430.52"]
  DISC["Disconnect\nArt 430.102"]
  VFD["VFD"]
  MTR["Motor"]

  OCPD --> DISC
  DISC -->|"Input conductors\nto VFD"| VFD
  VFD -->|"Output conductors\nNo disconnect here"| MTR

  style DISC fill:#f5f5dc,stroke:#999
  style MTR fill:#dce8f5,stroke:#999
</pre>
</div>

**Why no disconnect between VFD output and motor?**

A standard motor-circuit switch is not rated to interrupt the PWM output waveform of a VFD under load. Switching the VFD output with a standard disconnect can damage the drive and create arc flash hazards. The VFD itself is the device that controls the motor's de-energization on the output side.

The disconnect on the **input side** of the VFD serves the required isolation function for both the drive and the motor when the drive is de-energized.

**VFD bypass panels:** If a bypass contactor is installed that can connect the motor directly to the supply (bypassing the VFD), a separate disconnect must be evaluated for the bypass path.

---

## Common mistakes

| Mistake | Code reference | Correct approach |
|---|---|---|
| Disconnect not visible from motor | 430.102(B) | Locate within sight or add lockout provision |
| Using an ampere-only rated switch | 430.109 | Use HP-rated motor-circuit switch |
| Placing disconnect between VFD and motor | 430.109, VFD instructions | Locate disconnect at VFD input |
| Panel door as the only disconnect access | NFPA 79 §6.2 | Provide external lockable handle |
| Contactor used as disconnect | 430.109 | Contactors are not rated for isolation duty |

---

## Practical takeaway

- The disconnect must be visible and within 50 feet of the motor.
- Use HP-rated motor-circuit switches or equivalent listed devices.
- NFPA 79 requires the main panel disconnect to be lockable in the open position with an external handle.
- For VFDs, always place the disconnect on the **input** side of the drive.
- Never use a contactor or control-circuit switch as the required disconnecting means.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/nec-application/branch-circuits-vs-feeders/' | relative_url }}">&larr; Branch Circuits vs. Feeders</a>
  <a href="{{ '/training/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/training/nec-application/grounding-bonding-panels/' | relative_url }}">Grounding and Bonding for Control Panels &rarr;</a>
</div>
