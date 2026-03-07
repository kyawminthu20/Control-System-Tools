<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "7"
  clause_title: "Validation of PL"

INDEX_TAGS:
  topics: ["validation", "FMEA", "functional_testing", "technical_file", "CE_marking"]
  systems: ["machinery", "control_system", "srp_cs"]
-->

# ISO 13849-1:2023 — Clause 7 — Validation of PL

## 0. Why this clause matters

Validation is mandatory proof that the designed SRP/CS achieves a PL greater than or equal to PLr. Design and calculation alone are not sufficient — the standard requires active confirmation through analysis and testing. A machine with a Category 3/PLd design that has never been validated does not comply with ISO 13849-1. For CE marking under the EU Machinery Regulation, the validation documentation must be retained in the Technical File. The design is legally and technically incomplete without validation.

## 1. Validation plan

A validation plan must be established before validation activities begin. Attempting validation without a plan produces results that cannot be properly assessed. The validation plan must define:

| Plan Element | Required Content |
|-------------|-----------------|
| **Scope** | Which safety functions are covered; which SRP/CS elements are in scope |
| **Methods** | Analytical methods (e.g., FMEA, structured design review) and test methods (functional testing, fault injection) to be applied |
| **Acceptance criteria** | How each safety function's compliance will be confirmed; what constitutes pass/fail |
| **Resources** | Personnel, tools, equipment required for validation |
| **Schedule** | When validation will occur relative to commissioning |

The plan must be approved before testing begins. Retroactive validation plans (written after the test) are not acceptable.

## 2. Analysis methods

Analytical validation confirms by structured review that the design meets the Category and PL requirements:

**FMEA (Failure Mode and Effects Analysis):**
- Performed at the component level for each SRP/CS element.
- For each component, identify all credible dangerous failure modes.
- Determine the effect of each failure mode on the safety function.
- Confirm that the Category's fault tolerance claims hold — that the architecture handles single faults (Category 3) or detects them before next demand (Category 4) as required.

**Fault injection analysis:**
- Analytically (or in test) inject each identified fault mode and trace the response through the system.
- Confirm that the safety function is maintained or that the fault is detected and responded to as the Category requires.

**Structured design review against Category requirements:**
- Verify that each Category requirement (Clause 6) is met in the actual design.
- For Category 3: confirm dual-channel independence, cross-monitoring implementation, and that no single component failure removes both channels simultaneously.
- For Category 4: confirm that DC ≥ 99% claim is justified by the actual diagnostic measures.

## 3. Functional testing

Every safety function must be tested by functional test during validation:

- Confirm that the safety action (de-energize, stop, brake) occurs for every defined initiation event (E-stop pressed, guard opened, light curtain interrupted).
- Confirm that the response time (initiation to safe state) meets the requirement specified in the safety function specification (Clause 4).
- Confirm that manual reset is required before the machine can restart after the safety function has activated — where the specification requires it.
- Test the diagnostic function: for Category 2, 3, and 4 systems, deliberately induce a detectable fault and confirm that the diagnostic measure detects it and responds correctly.

Test results must be recorded with pass/fail criteria and retained.

## 4. Fault exclusion and fault consideration

Not every conceivable fault must be considered in the analysis and test. The standard permits fault exclusion — formally excluding certain faults from consideration — provided the rationale is documented and justified:

| Aspect | Requirement |
|--------|-------------|
| **Faults to consider** | All credible dangerous faults identified in FMEA must be addressed |
| **Fault exclusion** | Faults may be excluded if they are demonstrably unlikely given the application (e.g., simultaneous independent failures of two separate channels due to independent random failure) |
| **Exclusion rationale** | Each exclusion must be documented with the reason (e.g., physical separation makes simultaneous failure highly unlikely) |
| **Annex D reference** | ISO 13849-1 Annex D provides guidance on which faults may be excluded for well-tried components and what conditions justify exclusion |

Common exclusions: short-circuit between separate channels when channels are physically separated by routing or conduit; certain failure modes in well-tried components that have no known dangerous failure mode in that application.

Fault exclusions that are not documented or not justified invalidate the corresponding Category claim.

## 5. Validation documentation

The validation report is a required output of the validation process and must be retained in the Technical File for CE marking. Minimum content:

| Documentation Item | Description |
|-------------------|-------------|
| **Safety function list** | All safety functions validated, each linked to its PLr |
| **FMEA results** | Component-level analysis results for each SRP/CS element |
| **PL calculation** | MTTFd, DC, CCF inputs and achieved PL result for each safety function (typically SISTEMA report) |
| **CCF score sheet** | Completed Annex F scoring for Categories 2, 3, 4 |
| **Test records** | Functional test results: initiation event, expected response, actual response, pass/fail, date, tester |
| **Fault injection records** | Results of fault injection analysis or test |
| **Fault exclusion justification** | List of excluded faults with documented rationale |
| **Conclusion** | Formal statement that each safety function achieves PL ≥ PLr |
| **Reviewer** | Name and competence of the responsible person who conducted or supervised validation |

The Technical File must be retained for the operational life of the machine. For EU Machinery Regulation, this is typically 10 years after the last unit is placed on the market.
