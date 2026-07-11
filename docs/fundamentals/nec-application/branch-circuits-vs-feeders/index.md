---
layout: training-module
title: "Branch Circuits vs. Feeders for Motor Loads"
description: "Understand where a branch circuit ends and a feeder begins, and why motor loads require the 125% conductor multiplier from Article 430."
breadcrumb:
  - name: "Training"
    url: "/fundamentals/"
  - name: "NEC for Machines and Panels"
    url: "/fundamentals/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/branch_circuits_vs_feeders_motor_loads.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
redirect_from:
  - /training/nec-application/branch-circuits-vs-feeders/
---

## Purpose

This module clarifies the boundary between branch circuits and feeders in motor-load systems, explains why motor conductors require the 125% multiplier, and shows how to apply the Article 430 feeder formula when multiple motors share a common feeder.

---

## Branch circuit vs. feeder — the boundary

The NEC defines a **branch circuit** as the conductors between the final overcurrent protective device (OCPD) protecting the circuit and the outlet or load. A **feeder** is everything upstream of that final OCPD, from the service or source panel up to but not including the branch-circuit OCPD.

The dividing line is the **final overcurrent protective device**.

| Segment | From | To | NEC reference |
|---|---|---|---|
| Service conductors | Utility connection | Service OCPD | Art 230 |
| Feeder | Service or source OCPD | Branch-circuit OCPD | Art 215 |
| Branch circuit | Branch-circuit OCPD | Load (motor terminals) | Art 210, Art 430 |

For motor circuits, the branch-circuit OCPD is typically the fuse or circuit breaker that is selected from **Table 430.52**, not necessarily the one that also provides overload protection.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
  SVC["Service / Source Panel"]
  FOCPD["Feeder OCPD\n(Art 215)"]
  BOCPD["Branch-Circuit OCPD\nTable 430.52"]
  DISC["Disconnect\n(Art 430.102)"]
  OLR["Overload Relay\nArt 430.32"]
  MTR["Motor"]

  SVC --> FOCPD
  FOCPD -->|"Feeder conductors\nArt 430.24"| BOCPD
  BOCPD -->|"Branch-circuit conductors\nArt 430.22 (125%)"| DISC
  DISC --> OLR
  OLR --> MTR

  style BOCPD fill:#f5f5dc,stroke:#999
  style FOCPD fill:#dce8f5,stroke:#999
</pre>
</div>

---

## Article 430.22 — Branch-circuit conductor sizing (125% rule)

For a **single motor**, Art 430.22(A) requires that branch-circuit conductors have an ampacity of not less than **125% of the motor full-load current (FLC)** from the NEC tables (Table 430.248 for single-phase, Table 430.250 for three-phase).

> **Do not use the nameplate FLA.** Use the NEC table FLC value. The nameplate full-load amperes (FLA) reflects the actual motor, which may run cooler or hotter than assumed. The table values ensure the conductor is not thermally stressed under normal operation.

**Formula:**

```
Minimum conductor ampacity = FLC (Table 430.250) × 1.25
```

**Example — 10 HP, 460 V, 3-phase motor:**

- Table 430.250 FLC = 14 A
- Minimum conductor ampacity = 14 × 1.25 = **17.5 A**
- Select conductor ≥ 17.5 A → 12 AWG THHN at 75 °C = 25 A ✓

---

## Article 430.24 — Feeder conductor sizing (multiple motors)

When a feeder supplies two or more motors, Art 430.24 sets the minimum feeder conductor ampacity as:

> **125% of the largest motor FLC + 100% of the FLC of all other motors**

**Formula:**

```
Feeder ampacity = (FLC_largest × 1.25) + (FLC_motor2 + FLC_motor3 + ...)
```

**Example — three motors on one feeder (460 V, 3-phase):**

| Motor | HP | Table FLC |
|---|---|---|
| Motor 1 (largest) | 25 HP | 34 A |
| Motor 2 | 10 HP | 14 A |
| Motor 3 | 5 HP | 7.6 A |

```
Feeder ampacity = (34 × 1.25) + 14 + 7.6
               = 42.5 + 14 + 7.6
               = 64.1 A minimum
```

Select the next standard conductor size ≥ 64.1 A at 75 °C.

---

## Key rules summary

| Rule | Article | Requirement |
|---|---|---|
| Branch-circuit conductor ampacity | 430.22(A) | ≥ 125% of table FLC |
| Branch-circuit OCPD | 430.52 + Table 430.52 | Max % of FLC per device type |
| Feeder conductor ampacity | 430.24 | 125% largest + 100% rest |
| Overload protection | 430.32 | Sized at 115–125% of FLA |
| Use NEC table FLC, not nameplate FLA | 430.6(A) | Table values govern sizing |

---

## Common mistake — nameplate FLA vs. table FLC

A frequent field error is pulling the amperage value from the motor nameplate instead of the applicable NEC table.

| Source | Value (10 HP, 460 V, 3Ø) | Status |
|---|---|---|
| Motor nameplate FLA | 12.8 A (example) | Do **not** use for conductor sizing |
| Table 430.250 FLC | 14 A | **Use this for Art 430.22 and 430.24** |

The table value is almost always higher, providing a code-compliant thermal margin. The nameplate FLA may be used for overload relay setting (Art 430.32), but not for conductor ampacity calculation.

---

## Practical takeaway

- The branch circuit begins at the final OCPD (Table 430.52) and ends at the motor.
- Size branch-circuit conductors at 125% of the NEC table FLC, never the nameplate FLA.
- For shared feeders, apply the 430.24 formula: 125% of the largest motor FLC plus 100% of all others.
- Overload relays are downstream of the disconnect and are sized separately from conductors and branch-circuit OCPDs.

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/fundamentals/nec-application/motor-panel-code-application/' | relative_url }}">&larr; Motor and Panel Code Application</a>
  <a href="{{ '/fundamentals/nec-application/' | relative_url }}">↑ NEC for Machines and Panels</a>
  <a href="{{ '/fundamentals/nec-application/disconnecting-means/' | relative_url }}">Disconnecting Means for Machinery &rarr;</a>
</div>
