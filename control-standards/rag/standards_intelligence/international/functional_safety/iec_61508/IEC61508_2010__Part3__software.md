<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61508
EDITION: 2010

HIERARCHY:
  clause: "Part 3"
  clause_title: "Software Requirements"

INDEX_TAGS:
  topics: ["functional_safety", "software_sil", "safety_software", "safety_plc", "software_lifecycle", "mcdc_coverage"]
  systems: ["all_industries", "control_system", "safety_plc"]
-->

# IEC 61508:2010 — Part 3 — Software Requirements

## 0. Why this matters

Part 3 is what makes IEC 61508 complex to apply directly. Its software requirements are the most extensive of any functional safety standard. The full Part 3 burden includes formal methods, coverage analysis, independent validation, and extensive documentation — requirements that are practical only for safety device manufacturers, not for engineers deploying safety PLCs on machines.

Most organizations use sector standards (IEC 62061 for machinery, IEC 61511 for process) precisely to avoid the full Part 3 burden. Sector standards recognize that when a certified safety PLC is used, the PLC manufacturer has already addressed the firmware-level Part 3 requirements.

Understanding Part 3 also explains why TÜV and UL safety PLC certifications exist: they transfer the Part 3 software burden from the machine builder to the PLC manufacturer.

## 1. Software safety integrity levels

Software SIL must match the overall system SIL. A system cannot claim SIL 3 if the software only meets SIL 2 requirements. Software SIL is achieved through the combination of:

- Software development lifecycle rigor
- Techniques and measures applied at each lifecycle phase (Annex A of Part 3)
- Verification and validation activities matched to the SIL
- Independence requirements (who can develop, review, and validate)

Unlike hardware, software does not wear out. Software SIL reflects the confidence that the software is correct — it is a measure of development process rigor, not a probability of random failure.

## 2. Software lifecycle

Part 3 defines a structured software lifecycle with required activities and documentation at each phase:

| Phase | Activities |
|-------|-----------|
| Software safety requirements specification | Define software safety functions, SIL assignment, constraints |
| Software architecture design | Define structure, modules, data flows, failure handling |
| Software design and development | Detailed module design |
| Software coding | Implementation in target language |
| Module testing | Unit-level verification |
| Integration testing | Module-to-module and software-to-hardware integration |
| Software validation | Confirm software meets safety requirements specification |
| Modification | Change control — all changes revalidated per SIL |

Each phase has required input documents, required output documents, and required review activities. The depth of review and the independence required increases with SIL.

## 3. Key software requirements by SIL

The following table summarizes representative requirements from IEC 61508-3 Annex A. This is not exhaustive — the normative source is Annex A of Part 3.

| SIL | Representative requirements |
|-----|----------------------------|
| SIL 1 | Structured programming, documented test cases, code reviews, configuration management |
| SIL 2 | + Static analysis, formal design reviews, 100% branch coverage in testing, documented failure handling |
| SIL 3 | + Formal methods (highly recommended), MC/DC coverage, independent software validation team, traceability from requirements to test |
| SIL 4 | + Diverse redundancy (two independent software implementations), formal verification of software architecture |

**MC/DC coverage (Modified Condition/Decision Coverage):** A coverage criterion requiring that each condition in a decision has independently affected the decision outcome. Significantly more demanding than statement or branch coverage.

**Formal methods:** Mathematical proof techniques applied to software (e.g., abstract interpretation, model checking, theorem proving). Very rarely applied outside aerospace and nuclear.

## 4. Application software vs embedded software

Part 3 distinguishes between two software types with very different requirements:

| Software type | Definition | Example | Part 3 burden |
|---------------|-----------|---------|---------------|
| Embedded software | Firmware internal to a safety device | Safety PLC operating system and execution environment | Full Part 3 requirements; addressed by device manufacturer |
| Application software | User-written program executed by the safety device | Ladder logic or function block program in a safety PLC | Reduced requirements because the execution environment is already certified |

When a machine builder writes ladder logic in a TÜV-certified safety PLC, they are writing application software only. The certified execution environment (firmware) has already satisfied the Part 3 requirements for embedded software. The machine builder only needs to satisfy reduced application-software requirements, which sector standards (IEC 62061, IEC 61511) have already translated into accessible requirements.

## 5. Why certified safety PLCs simplify Part 3

The certification path for safety PLCs (TÜV Rheinland, TÜV SÜD, UL, Bureau Veritas) evaluates the PLC against IEC 61508 Part 2 and Part 3 for the embedded firmware and hardware. The result is a certificate specifying:

- Maximum SIL the device can be used in (e.g., "suitable for SIL 3 per IEC 61508")
- Hardware fault tolerance class
- Safe failure fraction range
- Maximum useful diagnostic coverage achievable
- Restrictions on application programming (prohibited instructions, constraints on program structure)

When a machine builder uses such a device:
1. The hardware meets Part 2 requirements (certified by the manufacturer)
2. The firmware meets Part 3 requirements (certified by the manufacturer)
3. The machine builder only validates their application software against a reduced set of requirements

This division of responsibility is why safety PLCs dominate industrial functional safety implementations. The alternative — developing custom safety logic on a non-certified processor — would require the machine builder to satisfy all of Part 2 and Part 3 independently, which is prohibitively expensive for most applications.

**Key implication:** The machine builder's Part 3 obligation, when using a certified safety PLC, is limited to:
- Correct specification of safety functions in the application program
- Verification that the application logic matches the safety requirements
- Documented testing of the application code
- Change control for any modifications

This is exactly what IEC 62061 Clause 6 and IEC 61511 Clause 12 describe — the simplified software requirements for application software on pre-certified devices.

## 6. Change log

- 2026-03-06 — Phase 3 corpus creation; Part 3 software requirements document established.
