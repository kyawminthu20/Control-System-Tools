<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: NEC_APPLICATION
MODULE_ID: conductor_ocpd_sizing_examples
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["conductor_sizing", "OCPD_sizing", "article_430", "worked_examples", "motor_branch_circuit"]
  systems: ["industrial_control_panel", "machine", "motor_branch_circuit"]
-->

# Conductor and OCPD Sizing Worked Examples

## 0. Purpose

This module works through NEC sizing calculations for motor branch circuits and feeders. It is a companion to the Art 430 workflow module — the focus here is on the arithmetic, the tables, and the common decision points.

## 1. Key tables used

| Table | What it gives |
|-------|---------------|
| Table 430.250 | FLA for 3-phase AC motors (use instead of nameplate) |
| Table 430.248 | FLA for single-phase AC motors |
| Table 310.15(B)(16) | Conductor ampacity at 60°C and 75°C in conduit |
| Table 430.52 | Maximum OCPD size multipliers by type |
| Table 250.122 | EGC minimum size based on upstream OCPD |

## 2. Worked example 1 — single motor, 10 HP, 480V, 3-phase, Design B

**Given:** 10 HP induction motor, 480V, 3-phase, service factor ≥ 1.15, Design B

**Step 1 — Table FLA**
From Table 430.250: **14 A**

**Step 2 — Branch-circuit conductor (Art 430.22)**
Required ampacity = 14 × 1.25 = **17.5 A minimum**
From Table 310.15(B)(16) at 75°C: 12 AWG Cu = 20 A ✓

**Step 3 — Overload relay (Art 430.32(A)(1))**
SF ≥ 1.15 → trip setting = 14 × 1.25 = **17.5 A maximum**
Set relay at or below 17.5 A.

**Step 4 — Branch-circuit OCPD (Art 430.52, Table 430.52)**
Inverse-time CB: 14 × 2.50 = 35 A → next standard size = **35 A CB** (exact standard size)
Dual-element fuse: 14 × 1.75 = 24.5 A → next standard size = **25 A fuse**

**Step 5 — EGC (Table 250.122)**
Upstream OCPD = 35 A CB → **10 AWG Cu EGC minimum**

**Summary:**

| Item | Size |
|------|------|
| Table FLA | 14 A |
| Branch conductor | 12 AWG Cu |
| Overload relay | ≤ 17.5 A |
| Inverse-time CB | 35 A |
| EGC | 10 AWG Cu |

## 3. Worked example 2 — single motor, 25 HP, 460V, 3-phase

**Given:** 25 HP induction motor, 460V, 3-phase, SF = 1.0

**Step 1 — Table FLA**
From Table 430.250: **34 A**

**Step 2 — Branch-circuit conductor**
34 × 1.25 = 42.5 A minimum
From Table 310.15(B)(16) at 75°C: 8 AWG Cu = 50 A ✓

**Step 3 — Overload relay**
SF = 1.0 (< 1.15) → trip setting = 34 × 1.15 = **39.1 A maximum**

**Step 4 — Inverse-time CB**
34 × 2.50 = 85 A → next standard size = **90 A CB**

If motor won't start on 90 A CB (Art 430.52 Exception 1):
Maximum allowed = 34 × 4.00 = 136 A → next standard size = **150 A CB**

**Step 5 — EGC**
Upstream OCPD = 90 A → **8 AWG Cu EGC** (from Table 250.122)

## 4. Worked example 3 — feeder for three motors

**Given:** Feeder serving three motors: 25 HP (34 A), 10 HP (14 A), 5 HP (7.6 A), all 460V, 3-phase

**Art 430.24 feeder formula:**
- Largest motor FLA × 1.25: 34 × 1.25 = 42.5 A
- Remaining motors × 1.00: 14 + 7.6 = 21.6 A
- **Feeder ampacity required = 42.5 + 21.6 = 64.1 A minimum**

From Table 310.15(B)(16) at 75°C: 4 AWG Cu = 85 A ✓

**Feeder OCPD:**
The feeder OCPD protects the feeder conductors. Size it at:
- ≤ 125% of conductor ampacity = 85 × 1.25 = 106 A → **100 A OCPD** (next standard size below 106 A)

Note: the feeder OCPD is not sized from Table 430.52 — that table applies to branch circuits only.

## 5. Quick-reference sizing table — common 3-phase 460/480V motors

| HP | Table FLA (A) | Min branch cond. (75°C Cu) | Max ITB CB | Max DE fuse |
|----|--------------|---------------------------|------------|-------------|
| 1  | 2.1 | 14 AWG | 15 A | 10 A |
| 2  | 3.4 | 14 AWG | 15 A | 10 A |
| 3  | 4.8 | 14 AWG | 15 A | 15 A |
| 5  | 7.6 | 14 AWG | 20 A | 15 A |
| 7.5 | 11 | 14 AWG | 30 A | 20 A |
| 10 | 14 | 12 AWG | 35 A | 25 A |
| 15 | 21 | 10 AWG | 60 A | 40 A |
| 20 | 27 | 10 AWG | 70 A | 50 A |
| 25 | 34 | 8 AWG | 90 A | 60 A |
| 30 | 40 | 8 AWG | 100 A | 70 A |
| 40 | 52 | 6 AWG | 125 A | 90 A |
| 50 | 65 | 4 AWG | 175 A | 110 A |

ITB = inverse-time breaker. DE = dual-element time-delay fuse.
Values from Table 430.250 and Table 430.52 at standard multipliers. Verify against the current edition of the NEC before using in design.

## 6. Common mistakes

| Mistake | Correct approach |
|---------|-----------------|
| Using nameplate FLA for conductor sizing | Use Table 430.250 per Art 430.6(A) |
| Sizing the branch CB to protect conductors for overload | The overload relay does that; the CB handles SCPD only |
| Using the Art 430.52 multiplier for the feeder OCPD | Feeder OCPD protects conductors; size at ≤ conductor ampacity × 1.25 |
| Forgetting to verify EGC size from Table 250.122 | EGC size depends on OCPD rating, not load current |
| Not increasing CB when motor won't start | Use the Art 430.52 Exception; document the reason |

## 7. Engineering takeaway

Motor sizing always requires four separate decisions: conductor, overload, OCPD, and EGC. Each uses a different table and a different multiplier. None can substitute for another. Work through them in sequence to avoid skipping a step.

## Related files

- [NEC Code Reading Fundamentals](./nec_code_reading_fundamentals.md)
- [Practical Article 430 Workflow](./article_430_practical_workflow.md)
- [Branch Circuits vs. Feeders for Motor Loads](./branch_circuits_vs_feeders_motor_loads.md)
- [SCCR Workflow for Industrial Control Panels](./sccr_workflow.md)
