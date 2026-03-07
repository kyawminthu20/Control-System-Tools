<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_62061
EDITION: 2021

HIERARCHY:
  clause: "4"
  clause_title: "Scope, Context, and Relationship to IEC 61508"

INDEX_TAGS:
  topics: ["functional_safety", "sil", "srecs", "machinery", "scope", "iec_61508", "iso_13849_1"]
  systems: ["machinery", "control_system"]
-->

# IEC 62061:2021 — Clause 4: Scope, Context, and Relationship to IEC 61508

## 0. Why This Clause Matters

Clause 4 defines the boundaries of IEC 62061 and explains when it applies versus other functional safety standards. Most importantly, it establishes when to use IEC 62061 versus ISO 13849-1 — the two are both valid for machinery safety functions, but they differ in methodology, quantification approach, and which subsystem types they handle best. Choosing the right standard at the project outset avoids rework during design verification and prevents mismatches between the assessment methodology and the technology used in the SRECS.

Getting this decision right matters because:
- Applying ISO 13849-1 to a complex programmable safety controller may not produce adequate coverage of software integrity requirements.
- Applying IEC 62061 to a purely electromechanical interlock system adds unnecessary complexity without benefit.
- Both standards can be applied to different subsystems within the same machine, but that split must be deliberate and documented.

---

## 1. Scope

IEC 62061 applies to the design and integration of safety-related electrical control systems (SRECS) used on machines. Key scope boundaries:

**In scope:**
- Safety-related electrical, electronic, and programmable electronic control systems (E/E/PE systems) on machinery.
- Safety functions implemented in safety PLCs, safety relays, and similar electronic devices.
- Subsystems composed of input devices (sensors, initiators), logic controllers, and output devices (actuators, contactors).
- Integration of subsystems from multiple suppliers into a complete SRECS.
- SIL 1, SIL 2, and SIL 3 safety integrity levels for machinery applications.

**Out of scope:**
- Safety functions implemented exclusively by pneumatic or hydraulic systems without any electrical control element.
- Non-electrical safety systems (mechanical guards, passive barriers).
- SIL 4 — IEC 62061 restricts its scope to SIL 1–3 because SIL 4 is not applicable to typical machinery.
- The standard does not define risk assessment methods — ISO 12100 and ISO/TR 14121-2 provide the risk assessment that generates SIL targets as input to IEC 62061.

**Geographic applicability:**
IEC 62061 is published by IEC and is harmonized under the EU Machinery Directive (and the successor Machinery Regulation 2023/1230). Compliance with IEC 62061 provides presumption of conformity for the safety control system aspects of CE marking. It is recognized globally and referenced in standards from North America, Asia, and other regions as an acceptable methodology.

---

## 2. Relationship to IEC 61508

IEC 62061 is a sector-specific standard derived from IEC 61508 (Functional Safety of E/E/PE Safety-Related Systems). The relationship is hierarchical:

- IEC 61508 is the base standard covering all industries (process, nuclear, transportation, machinery, etc.).
- IEC 62061 is a sector standard that takes the IEC 61508 framework and applies it specifically to machinery.

**Key simplifications IEC 62061 makes relative to IEC 61508:**

1. **Software requirements scoped out for certified subsystems:** When a subsystem uses a certified safety PLC or certified safety device (e.g., a device certified to IEC 61508 at a given SIL), the detailed software safety lifecycle requirements of IEC 61508-3 apply to the device manufacturer, not the machinery builder. The machinery builder only needs to verify the device is used within its certified parameters and that application programming is done appropriately.

2. **SIL 4 excluded:** SIL 4 is not used in machinery applications under IEC 62061, eliminating the most demanding requirements of IEC 61508.

3. **Machinery-specific subsystem architecture:** IEC 62061 defines the input-logic-output decomposition directly, making it easier to apply the framework to typical machine control architectures.

4. **Direct use of manufacturer PFH data:** IEC 62061 explicitly allows using PFHd values published in manufacturer device documentation, reducing the burden of performing full reliability analysis from component-level data.

Using IEC 62061 is explicitly permitted as an alternative to applying IEC 61508 directly for machinery. The standard states this and the EU harmonized standards list confirms it. A machinery builder does not need to apply IEC 61508 directly if they comply with IEC 62061.

---

## 3. IEC 62061 vs. ISO 13849-1 Comparison Table

Both IEC 62061 and ISO 13849-1 are harmonized under the EU Machinery Directive and are acceptable for demonstrating compliance with the Essential Health and Safety Requirements for safety-related control systems. They use different metrics and approaches.

| Aspect | ISO 13849-1 (PL) | IEC 62061 (SIL) |
|--------|-----------------|----------------|
| Metric used | PLa through PLe | SIL 1 through SIL 3 |
| Equivalent levels | PLc approximately equals SIL 1, PLd approximately equals SIL 2, PLe approximately equals SIL 3 | — |
| Best suited for | Electromechanical devices, proven safety components, simpler architectures | Programmable SRECS, complex safety PLCs, multi-supplier system integration |
| Software handling | Limited — prefers proven components with established safety function; complex software requires IEC 61508-3 | Full SIL-appropriate software requirements referenced through IEC 61508-3 when needed |
| Quantitative basis | Safety category (architecture) combined with MTTFd and DC | PFHd sum of individual subsystems |
| Architectural metric | Category (B, 1, 2, 3, 4) | Hardware Fault Tolerance (HFT 0, 1, 2) and Safe Failure Fraction (SFF) |
| Tools commonly used | SISTEMA software (TÜV Rheinland, free) | SISTEMA or structured spreadsheet calculation |
| Can they be used together? | Yes — different subsystems in the same machine can use different standards; joint use requires careful boundary documentation | — |
| Mutual exclusivity | Not mutually exclusive — can be used on different subsystems | — |

**Practical guidance on equivalence:** ISO/TR 62061-1 (published by IEC) provides a mapping table between PL and SIL. The equivalence is approximate because the two methodologies quantify things differently. Do not mix PL and SIL metrics within a single subsystem — apply one standard to each subsystem and sum at the SRECS level using PFHd.

---

## 4. When to Use IEC 62061

IEC 62061 is the preferred or required approach in the following situations:

**Use IEC 62061 when:**

- The SRECS includes a complex programmable safety controller (e.g., a Siemens S7-1200F, Allen-Bradley GuardLogix, Pilz PSS4000, or equivalent certified safety PLC). These devices have published PFH values and are certified to IEC 61508 or IEC 62061 — the IEC 62061 subsystem approach aligns naturally with how their certification data is presented.

- The system integrates subsystems from multiple suppliers, each with their own certified safety devices. IEC 62061 provides a clear framework for allocating SIL targets to each subsystem independently and summing PFHd to verify the total.

- The SIL 2 or SIL 3 target requires rigorous quantification. While ISO 13849-1 can address PLd and PLe, IEC 62061's explicit PFHd summation is often clearer for regulators and notified bodies at higher integrity levels.

- The design team is already working within an IEC 61508 framework (e.g., for a machine that is also classified as a safety instrumented system for process applications). IEC 62061 is the natural extension of that methodology to the machinery context.

- A notified body or customer specification explicitly requires the SIL methodology.

**ISO 13849-1 may be more appropriate when:**
- The SRECS consists primarily of electromechanical safety devices (safety relays, interlock switches, guard switches) without complex programmable logic.
- The team is more familiar with the category/MTTFd/DC approach.
- Existing designs are documented using the category-based architecture.

Both approaches are equally valid for regulatory compliance. The choice should be driven by the technology used, the team's expertise, and the complexity of the system — not by which standard appears simpler on the surface.
