<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

TOPIC_ID: sccr
PRIORITY: CRITICAL
-->

# Overlap Note — SCCR (Short-Circuit Current Rating)

## Decision rules (who wins)

- **SCCR marking required** → NEC Article 409.110
- **SCCR calculation method** → UL 508A Supplement SB (approved method)
- **SCCR in machinery context** → NFPA 79 (equipment protection)

**Critical**: NEC explicitly references UL 508A Supplement SB as an approved method for determining SCCR.

## Evidence required

### For Each Panel
- [ ] Available fault current at panel location (from building/facility)
- [ ] Component SCCR ratings (from manufacturer datasheets)
- [ ] UL 508A Supplement SB calculation worksheet
- [ ] Panel SCCR label (applied to panel)
- [ ] Photos of applied label

### For Multi-Panel Machines
- [ ] SCCR per panel (all panels)
- [ ] Inter-panel connection diagram
- [ ] Machine-level SCCR basis documentation

## Checklist

### SCCR Determination
- [ ] Obtain available fault current from facility (ask facility engineer or utility)
- [ ] Collect SCCR ratings for ALL components in panel (datasheets)
- [ ] Apply UL 508A SB weakest-link method
- [ ] Identify weakest component (lowest SCCR rating)
- [ ] Panel SCCR = weakest component SCCR (simplified method)
- [ ] Verify panel SCCR ≥ available fault current

### SCCR Labeling (NEC Requirement)
- [ ] Create SCCR label with calculated value
- [ ] Apply label to panel (visible location)
- [ ] Label format: "SHORT-CIRCUIT CURRENT RATING: [value] AMPS"
- [ ] Photo-document label application
- [ ] Record label information in project file

### For UL 508A Listing
- [ ] Submit SCCR calculation to UL examiner
- [ ] Include component datasheets as evidence
- [ ] Include calculation worksheet
- [ ] UL will verify and approve SCCR

### For Multi-Panel Machines
- [ ] Calculate SCCR for each individual panel
- [ ] Label each panel with its SCCR
- [ ] Document machine-level SCCR basis
- [ ] Each panel SCCR contributes to overall machine SCCR

## Workflow: SCCR Determination

```
Step 1: Obtain Available Fault Current
    ↓
Step 2: Collect Component SCCR Ratings
    ↓
Step 3: Apply Weakest-Link Method (UL 508A SB)
    ↓
Step 4: Panel SCCR = Lowest Component SCCR
    ↓
Step 5: Verify: Panel SCCR ≥ Available Fault Current
    ↓
Step 6: Create and Apply SCCR Label
    ↓
Step 7: Store Evidence
```

## UL 508A Supplement SB - Weakest-Link Method

**Simplified Approach** (most common):
- Panel SCCR = SCCR of **weakest component** in panel
- Identify component with lowest SCCR rating
- That becomes the panel SCCR

**Example**:
- Main breaker: 65kA SCCR
- Contactors: 10kA SCCR ← WEAKEST
- Terminal blocks: 20kA SCCR
- Transformers: 10kA SCCR
- **Panel SCCR = 10kA** (weakest link)

**Advanced Methods** (UL 508A SB provides additional methods):
- Series-rated combination method
- Current-limiting device method
- Component testing method

## Common SCCR Values

| Component Type | Typical SCCR Range |
|----------------|-------------------|
| **Molded Case Circuit Breakers** | 10kA - 200kA |
| **Contactors** | 5kA - 100kA |
| **Motor Starters** | 5kA - 100kA |
| **Terminal Blocks** | 6kA - 20kA |
| **Transformers** | 10kA - 25kA |
| **Control Relays** | 6kA - 10kA |
| **VFDs/Drives** | Varies (check datasheet) |

## Common Mistakes

❌ **Wrong**: Assuming panel SCCR without calculation
❌ **Wrong**: Using breaker rating as panel SCCR (ignores other components)
❌ **Wrong**: Forgetting to label the panel (NEC violation)
❌ **Wrong**: Missing one component in weakest-link analysis

✅ **Right**: Calculate using ALL components
✅ **Right**: Use weakest component SCCR
✅ **Right**: Apply label prominently
✅ **Right**: Store evidence for inspection/audit

## Automation Opportunity

**SCCR Calculator Tool** (High Priority):
- Input: BOM with component part numbers
- Tool fetches SCCR ratings from database
- Tool applies weakest-link algorithm
- Output: Panel SCCR value + label text
- Bonus: Auto-generate UL 508A SB worksheet

**Status**: Ready for implementation

## Cross-links

### Standards Files
- NEC: [NEC_2023__Art409__industrial_control_panels.md](../nec/NEC_2023__Art409__industrial_control_panels.md) - Section 409.110 (SCCR marking requirement)
- UL 508A: [UL508A_2022__sccr_short_circuit_current_rating.md](../ul_508a/UL508A_2022__sccr_short_circuit_current_rating.md) - Supplement SB (calculation method)

### Overlap Matrices
- [ul508a_nec_nfpa79_overlap.md](../overlap_matrix/ul508a_nec_nfpa79_overlap.md) - SCCR topic section

## References

- NEC Article 409.110: Requires SCCR marking on industrial control panels
- UL 508A Supplement SB: Approved method for SCCR determination
- UL guidance: Each panel in multi-panel machine needs SCCR

## Changelog

- 2026-01-15 — Initial SCCR overlap note created
  - Decision rules documented
  - Weakest-link method explained
  - Workflow and checklist provided
  - Automation opportunity identified
  - Status: DRAFT (ready for use)

---

**Priority**: CRITICAL - SCCR is the most frequently asked question and a legal requirement (NEC).
**Automation**: High priority for automated SCCR calculator tool.
