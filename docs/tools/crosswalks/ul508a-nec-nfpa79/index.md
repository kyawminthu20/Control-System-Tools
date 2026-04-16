---
layout: default
title: "UL 508A / NEC / NFPA 79 Crosswalk"
description: "Topic-by-topic overlap matrix for the three US standards governing industrial control panels and machinery."
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "UL 508A / NEC / NFPA 79"
repo_path: "control-standards/rag/standards_intelligence/tools/crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md"
related_standards:
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
redirect_from:
  - /crosswalks/ul508a-nec-nfpa79/
  - /crosswalks/ul508a-nec-nfpa79/index.html
---

<div class="page-header">
  <span class="page-header__label">Crosswalk</span>
  <h1>UL 508A / NEC / NFPA 79 — US Standards Overlap</h1>
  <p>Topic-by-topic overlap for US industrial control panel design. Source: <code>rag/tools/crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md</code></p>
</div>

## How the Three Standards Relate

```
NEC (legally enforced — installation code)
   ├── Art. 409: Requires SCCR marking → computed by UL 508A Sec. SB
   └── Art. 670: References NFPA 79 for machine electrical design
                        ↓
                    NFPA 79 (machine electrical design)
                        ↓
                    UL 508A (panel construction and listing)
```

**Each standard owns a layer:** NEC = installation baseline (law); NFPA 79 = machine electrical design; UL 508A = panel construction and listing.

---

## Topic-Based Overlap Matrix

| Topic | NEC | NFPA 79 | UL 508A | Primary Owner |
|-------|-----|---------|---------|---------------|
| Scope / Panel definition | Art. 409, 670 | Scope chapters | Scope | NEC (install), NFPA 79 (machine), UL 508A (panel) |
| Component listing | Art. 110 | General reqs | General construction | NEC + UL |
| Disconnecting means | Install-dependent | **Ch. 5** | Panel disconnect | NFPA 79 (behavior), NEC (install) |
| Overcurrent protection | Art. 240, 430 | Ch. 6 | OCP requirements | NEC + UL 508A |
| **Grounding and bonding** | **Art. 250** | **Ch. 8** | **Sec. 7** | NEC (baseline), NFPA 79 (machine) |
| Wiring methods | Art. 300, 310 | Ch. 16, 17 | Wiring and conductors | NEC (baseline), UL inside panel, NFPA inside machine |
| **Wire sizing** | **Art. 310** | — | **Sec. 5** | NEC / UL 508A Sec. 5 |
| Control circuits | Art. 725 (as applicable) | **Ch. 9** | Control circuit construction | NFPA 79 (behavior) |
| Emergency stop | Indirect | **Ch. 9** | Safety device integration | NFPA 79 (what it must do), UL (how it's built) |
| Panel construction | Art. 409 | Ch. 11 | **Core construction** | **UL 508A** |
| **SCCR** | **Art. 409.110 (requires label)** | Machinery SCCR | **Sec. SB (method)** | NEC requires, UL provides method |
| Marking and documentation | Art. 409 marking | Ch. 19 | Marking | All three overlap |
| Motors / controllers | **Art. 430** | Ch. 12 | Motor controllers | NEC (circuits), UL (panel construction) |
| Control power transformer | General OCP rules | Ch. 15 | Transformer/PSU construction | NFPA 79 + UL 508A |

---

## Critical Interaction: SCCR

SCCR is where NEC and UL 508A interact most critically:

**Step 1 — NEC Article 409.110** requires the panel to be marked with the SCCR.

**Step 2 — UL 508A Supplement SB** provides the approved calculation method (weakest-link method based on component SCCR ratings).

**Step 3** — The calculated SCCR must meet or exceed the available fault current at the installation point. This is confirmed during installation inspection.

---

## Critical Interaction: Grounding

Three standards all address grounding; each adds a layer:

| Standard | What It Covers |
|----------|---------------|
| NEC Art. 250 | Safety grounding baseline — legally required, applies to all electrical installations |
| NFPA 79 Ch. 8 | Machine bonding specifics — door bonding jumpers, PE routing through the machine |
| UL 508A Sec. 7 | Panel bonding workmanship — how PE is connected inside the panel enclosure |

**Key points:**
- Keep "noise grounding" (signal reference) separate from safety bonding — these are not the same function
- Safety/protective grounding exists to clear faults and protect people; functional grounding is for EMC/noise purposes only
- Functional grounding must not compromise the protective-earth path
- Door bonding jumpers are required (hinges and paint can interrupt continuity)
- PE continuity must be maintained throughout the machine and after any field modifications

---

## Emergency Stop — Behavior vs Construction

| Aspect | Standard | Content |
|--------|----------|---------|
| What E-stop must do (functional requirements) | NFPA 79 Ch. 9 | Stop categories (0, 1, 2), de-energization logic |
| How E-stop device is built | UL 508A | Component ratings, contact construction |
| Operator interface labeling | Both | Color, marking requirements |

**Note:** For formal PL or SIL verification of E-stop functions, also apply [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) or [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}).
