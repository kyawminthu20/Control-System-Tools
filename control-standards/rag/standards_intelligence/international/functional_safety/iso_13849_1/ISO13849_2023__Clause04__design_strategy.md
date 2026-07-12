<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "4"
  clause_title: "Design Strategy and Safety Function Specification"

INDEX_TAGS:
  topics: ["performance_level", "safety_function", "design_strategy", "PLr"]
  systems: ["machinery", "control_system", "srp_cs"]
-->

# ISO 13849-1:2023 — Clause 4 — Design Strategy and Safety Function Specification

## 0. Why this clause matters

Clause 4 defines the required safety function specification before any architecture or calculation work begins. You cannot pick a Category or calculate an achieved PL without first knowing the required PL (PLr). This clause establishes what each safety function must do — its initiation, its response, and its required performance — before any hardware or software design decisions are made. Skipping this step is the most common cause of invalid safety design: engineers select Category 3 because "it sounds right" without establishing the PLr that justifies or refutes that choice.

## 1. Safety function specification

Each safety function must be fully specified before design begins. A complete specification includes:

| Specification Element | Description |
|----------------------|-------------|
| **Initiation event** | The signal or condition that triggers the safety function (e.g., E-stop pressed, guard door opened, light curtain beam broken) |
| **Response action** | The controlled action taken to remove or reduce the hazard (e.g., remove drive enable, apply brake, de-energize actuator) |
| **Required PL (PLr)** | Determined from the ISO 13849-1 Annex A risk graph, using S/F/P parameters estimated during the ISO 12100 risk assessment |
| **Response time requirement** | Maximum time from initiation to completed safe state (e.g., ≤ 500 ms stop time) |
| **Reset requirement** | Whether manual reset is required before the machine can restart after the safety function activates |

One safety function specification sheet must exist per distinct safety function. A complex machine with an E-stop, two light curtains, and an interlocked guard requires four separate specifications.

## 2. Design strategy overview

The ISO 13849-1 design strategy is a structured iterative loop:

1. **Specify PLr** — Carry out the machinery risk assessment per ISO 12100, then use the ISO 13849-1 Annex A S/F/P risk graph to determine the required Performance Level for each safety function.
2. **Select Category architecture** — Choose B, 1, 2, 3, or 4 based on the fault tolerance needed to achieve PLr (Clause 6).
3. **Determine MTTFd, DC, CCF** — For the selected architecture, calculate or look up component reliability data (Clause 5).
4. **Calculate achieved PL** — Use the Category + MTTFd + DC combination table (Clause 5) to determine the achieved PL.
5. **Verify achieved PL ≥ PLr** — If achieved PL meets or exceeds PLr, the design is validated. If not, iterate: change Category, select higher MTTFd components, or increase DC.
6. **Validate** — Confirm by analysis and testing per Clause 7.

This loop must be completed and documented for every safety function in the machine.

## 3. PL levels defined

Performance Levels are defined by PFHd (Probability of dangerous Failure per Hour):

| PL | PFHd Range | Interpretation |
|----|-----------|----------------|
| PLa | ≥ 10⁻⁵ /hr to < 10⁻⁴ /hr | Lowest reliability requirement; very low risk |
| PLb | ≥ 3×10⁻⁶ /hr to < 10⁻⁵ /hr | Low–medium risk applications |
| PLc | ≥ 10⁻⁶ /hr to < 3×10⁻⁶ /hr | Medium risk; simple guarding where exposure is occasional |
| PLd | ≥ 10⁻⁷ /hr to < 10⁻⁶ /hr | High risk; most industrial E-stop, light curtains, interlocks |
| PLe | ≥ 10⁻⁸ /hr to < 10⁻⁷ /hr | Highest requirement; rare in standard machinery |

Note: PLa is not the same as "no requirement." Even PLa requires that the safety function works; it just tolerates a higher probability of failure than PLb–PLe.

## 4. Relationship to ISO 12100

ISO 12100 and ISO 13849-1 do different jobs, and the boundary between them matters:

- **ISO 12100** provides the machinery risk assessment and three-step risk reduction
  methodology. It identifies the hazards and the need for safety functions. It does
  not itself output a PLr.
- **ISO 13849-1 Annex A** contains the S/F/P risk graph that estimates the required
  Performance Level (PLr) for each safety-related control function. This is the
  normative source of PLr.
- **IEC 62061** provides its own method for determining a required SIL, for designs
  taking that route instead.

So the sequence is: assess risk per ISO 12100 → for each safety function designed under
ISO 13849-1, estimate PLr with the ISO 13849-1 Annex A risk graph → ISO 13849-1 Clause 4
is the first design step after PLr is determined.

Design practitioners who jump straight to a PLr without an ISO 12100 risk assessment are
not following either standard correctly. The PLr must be justified by risk assessment,
not assumed.
