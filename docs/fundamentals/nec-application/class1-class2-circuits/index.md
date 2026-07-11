---
layout: training-module
title: "Class 1, Class 2, and Remote-Control Circuits"
description: "How NEC Article 725 classifies remote-control circuits, what wiring methods each class permits, and how separation rules apply to 24 VDC PLC wiring in machine panels."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "NEC for Machines and Panels"
    url: "/fundamentals/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/class1_class2_remote_control_circuits.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /training/nec-application/class1-class2-circuits/
---

## Purpose

This module explains how NEC Article 725 classifies remote-control, signaling, and power-limited circuits, what wiring rules apply to each class, and how those rules affect 24 VDC PLC I/O wiring and conductor separation inside a machine control panel.

---

## Why Article 725 matters in machine panels

Industrial control panels routinely contain both power wiring (line voltage, motor branch circuits) and control wiring (24 VDC PLC I/O, 120 VAC relay coils, field device signals). Article 725 determines:

- Whether a control circuit is power-limited (Class 2 or 3) or unrestricted (Class 1)
- What conductor sizes, insulation ratings, and wiring methods are acceptable for each class
- Where and how control conductors must be separated from power conductors

Getting the classification wrong leads either to over-wiring a low-energy circuit (using full power-circuit conduit and 14 AWG wire for a 24 V PLC loop) or under-wiring an unrestricted control circuit (routing Class 1 conductors without conduit protection).

---

## Class 1 circuits

Class 1 circuits have no power limitation imposed by NEC Article 725. They follow the same wiring rules as power circuits.

**Key characteristics:**

- No limit on voltage or power imposed by the circuit classification itself
- Must use wiring methods allowed for power circuits — generally conductors in conduit, cable tray, or similar methods
- Minimum conductor size: **14 AWG** for conductors not in a raceway, **18 AWG** for conductors in a raceway (Art 725.49)
- Protection against physical damage, voltage, and current follows Art 240 and Art 310

**When you encounter Class 1 in a machine panel:**

A 120 VAC control circuit running from a control transformer through relay coils to field devices is almost always a Class 1 circuit unless it is supplied from a listed Class 2 or Class 3 power supply. It must be wired with conductors and methods adequate for the voltage and current involved.

Art 725.46 permits Class 1 conductors to occupy the same cable, enclosure, or raceway as power conductors subject to Art 725.48.

---

## Class 2 circuits

Class 2 circuits are power-limited. The supply must be a **listed Class 2 power supply** that limits output power to ≤ 100 VA and voltage to ≤ 30 V (or ≤ 150 V in some configurations — see Table 11(A) and 11(B) in the NEC).

**Key characteristics:**

- Supply must be listed and marked "Class 2"
- Relaxed wiring methods permitted: smaller conductors, lower-rated insulation, unenclosed wiring in some applications
- No minimum conductor size prescribed by Art 725 for Class 2 conductors within the panel (the listing of the power supply controls)
- Conductors must be separated from power and Class 1 conductors (see separation rules below)

**In practice — 24 VDC PLC I/O:**

Most 24 VDC PLC power supplies are listed Class 2 supplies. The I/O field wiring from the PLC output cards to field devices (sensors, solenoids) supplied from a listed Class 2 supply qualifies as a Class 2 circuit. This is the most common Class 2 scenario in machine panels.

---

## Class 3 circuits

Class 3 circuits are also power-limited but at higher voltage levels than Class 2 — up to 150 V, with power limits per Table 11(A)/(B). They require more physical protection than Class 2.

**Key characteristics:**

- Supply must be listed and marked "Class 3"
- Voltage ≤ 150 V, power limited by the listed supply
- More physical protection required than Class 2 (conductors must be protected from physical damage)
- Less common in machine panels than Class 2

---

## Classification decision flowchart

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
  START([Control circuit to classify]) --> Q1{Supplied from a\nlisted Class 2 power supply?}
  Q1 -- Yes --> CL2[Class 2 Circuit\nArt 725.121\nRelaxed wiring methods]
  Q1 -- No --> Q2{Supplied from a\nlisted Class 3 power supply?}
  Q2 -- Yes --> CL3[Class 3 Circuit\nArt 725.121\nPhysical protection required]
  Q2 -- No --> CL1[Class 1 Circuit\nArt 725.41\nPower-circuit wiring rules apply]
  CL2 --> SEP[Apply separation rules\nArt 725.136]
  CL3 --> SEP
  CL1 --> SEP
</pre>
</div>

The key determination is the **supply listing**, not the voltage level alone. A 24 VDC circuit supplied from an unlisted or non-Class-2-marked power supply is a Class 1 circuit and must follow power-circuit wiring rules even though the voltage is low.

---

## Separation rules — Art 725.136

Art 725.136 governs how Class 2 and Class 3 conductors must be separated from power and Class 1 conductors.

**The default rule:** Class 2 and Class 3 conductors must not be placed in the same cable, enclosure, or raceway with power or Class 1 conductors.

**Permitted exceptions (Art 725.136(B)–(D)):**

| Condition | Separation required |
|---|---|
| Class 2 and Class 1 in same enclosure, separated by a barrier | Permitted if barrier maintains separation |
| Class 2 conductors in a cable that is listed for the purpose | May share enclosure with power conductors if listed |
| Class 2 conductors entering an enclosure containing power conductors | Permitted — the enclosure entry point is not the wiring method |

**Practical application in a machine panel:**

The most common compliant approach is to route 24 VDC Class 2 control wiring in a separate wire duct from 120 VAC and line-voltage conductors. Many panel builders use separate duct channels: one for power wiring, one for Class 2 control wiring. A physical barrier (metal divider, separate duct, or listed combination assembly) satisfies the separation requirement.

Where a barrier is impractical — for example, where field wires from a sensor enter the panel and must pass through the same opening as power conductors — the entry point itself is not a violation. Separation is required inside the enclosure once conductors are routed to their destinations.

---

## NFPA 79 color coding and conductor identification

NFPA 79 (Electrical Standard for Industrial Machinery) requires conductor color coding that aligns with, and supplements, NEC requirements.

| Circuit type | NFPA 79 required color |
|---|---|
| 24 VDC control (Class 2, positive) | Blue |
| 120 VAC control (Class 1) | Red |
| AC power conductors — Line | Black (or per phase marking) |
| Grounded conductor (neutral) | White or gray |
| Equipment grounding conductor | Green (or green/yellow stripe) |

Using NFPA 79 color coding inside the panel also serves as documentation of the circuit classification: blue conductors are immediately identifiable as low-voltage Class 2 wiring, red conductors as 120 VAC Class 1 control.

Some panel builders use white or gray for 24 VDC return (negative) — this does not conflict with NEC as long as the insulation is identified at terminations as a DC negative, not an AC grounded conductor.

---

## Common mistakes

| Mistake | Consequence | Correct approach |
|---|---|---|
| Treating any 24 VDC wiring as Class 2 without checking power supply listing | Class 1 rules not applied where required | Verify power supply is listed and marked "Class 2" |
| Routing Class 2 and 120 VAC control wiring in the same wire duct | Art 725.136 violation | Use separate ducts or a listed combination assembly with barrier |
| Using undersized conductors on Class 1 circuits because voltage is low | Overcurrent protection inadequate for conductor | Class 1 = power-circuit rules; use 14 AWG minimum in raceway |
| Ignoring the separation requirement at panel entry points | Misjudging what counts as a wiring method | Entry point is not the wiring method; separate inside the enclosure |
| Assuming Class 2 wiring needs no conduit inside the panel | Physical damage not considered | Class 2 inside a panel does not require conduit but conductors must be protected from damage |

---

## Practical takeaway

The classification of a control circuit as Class 1, 2, or 3 depends entirely on the supply listing, not on voltage level. A 24 VDC circuit from a listed Class 2 supply qualifies for relaxed wiring methods and must be separated from power conductors. A 24 VDC circuit from an unlisted supply is a Class 1 circuit and must follow power-circuit wiring rules.

In machine panels, maintaining physical separation between Class 2 and power wiring — through separate wire ducts or barriers — is the simplest way to achieve compliance with Art 725.136 and alignment with NFPA 79 color-coding requirements.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/nec-application/conductor-ocpd-sizing/' | relative_url }}">&larr; Conductor and OCPD Sizing</a>
  <a href="{{ '/fundamentals/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/fundamentals/nec-application/article-430-workflow/' | relative_url }}">Practical Article 430 Workflow &rarr;</a>
</div>
