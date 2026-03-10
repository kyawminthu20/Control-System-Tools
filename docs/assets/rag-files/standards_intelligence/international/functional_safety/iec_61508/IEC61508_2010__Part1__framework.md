<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61508
EDITION: 2010

HIERARCHY:
  clause: "Part 1"
  clause_title: "General Requirements"

INDEX_TAGS:
  topics: ["functional_safety", "sil", "safety_lifecycle", "e_e_pe", "risk_based_approach"]
  systems: ["all_industries", "control_system"]
-->

# IEC 61508:2010 — Part 1 — General Requirements and Framework

## 0. Why this matters

IEC 61508 is the parent standard for functional safety of E/E/PE safety-related systems. Understanding it explains why IEC 62061 (machinery) and IEC 61511 (process industry) are structured as they are — both are derived sector standards that adapt and simplify IEC 61508 for their specific application domain.

Most machinery and process engineers never apply IEC 61508 directly. They work with the sector standards because those standards are scoped to their domain and strip out requirements that do not apply. IEC 61508 is the baseline for certification when no sector standard applies (custom safety devices, cross-domain systems, safety device manufacturers certifying products for sale).

## 1. Scope

IEC 61508 covers all E/E/PE (electrical, electronic, programmable electronic) safety-related systems across all industries. The scope is deliberately broad: any system that uses electrical, electronic, or programmable electronic technology to perform or contribute to a safety function is within scope.

Key scope characteristics:
- Applies to the complete safety lifecycle from concept through decommissioning
- Covers safety-related systems regardless of industry (not machinery-specific, not process-specific)
- Applies to both high-demand mode (continuous/frequent operation) and low-demand mode (periodic operation, tested by proof tests)
- Covers the safety-related control system itself, not the equipment under control (EUC)

Sector standards (IEC 62061 for machinery, IEC 61511 for process) narrow this scope to specific application domains, simplifying the requirements by removing provisions that are not applicable to their domain.

## 2. Risk-based approach

IEC 61508 requires a risk-based approach to determining the required SIL. The core principle is:

**Required SIL = gap between existing (residual) risk and tolerable risk**

Key points:
- The standard does not define a single tolerable risk level — that is set by the application context, jurisdiction, or applicable sector standard
- Risk must be estimated for each hazardous event, considering frequency of exposure, probability of occurrence, and severity
- The required risk reduction determines the SIL target for the safety function
- Risk reduction can come from the E/E/PE safety-related system alone or shared across multiple protection layers (LOPA approach in IEC 61511)

The standard provides risk determination methods in Part 5 (informative). Sector standards may prescribe specific risk assessment methods for their domain (e.g., ISO 12100 + risk graph or LOPA).

## 3. SIL levels defined

SIL (Safety Integrity Level) is a discrete level specifying the required probability of failure on demand for a safety function. IEC 61508 defines four SIL levels.

| SIL | PFHd (high-demand mode) | PFDavg (low-demand mode) |
|-----|-------------------------|--------------------------|
| SIL 1 | 10⁻⁶ to < 10⁻⁵ /hr | 10⁻² to < 10⁻¹ |
| SIL 2 | 10⁻⁷ to < 10⁻⁶ /hr | 10⁻³ to < 10⁻² |
| SIL 3 | 10⁻⁸ to < 10⁻⁷ /hr | 10⁻⁴ to < 10⁻³ |
| SIL 4 | 10⁻⁹ to < 10⁻⁸ /hr | 10⁻⁵ to < 10⁻⁴ |

**Mode selection:** Use PFHd for high-demand mode systems (safety function demanded at least once per year — typical machinery applications per IEC 62061). Use PFDavg for low-demand mode systems (safety function rarely demanded, tested periodically — typical process SIS per IEC 61511).

**SIL 4 note:** SIL 4 is designed for nuclear reactors and aviation instrumentation. It is almost never used in industrial automation. IEC 62061 explicitly excludes SIL 4 from machinery applications. Most industrial applications use SIL 1–SIL 3.

## 4. The seven-part structure

| Part | Title | Type | Primary audience |
|------|-------|------|-----------------|
| Part 1 | General requirements | Normative | All users |
| Part 2 | Requirements for E/E/PE safety-related systems (hardware) | Normative | Hardware designers, safety device manufacturers |
| Part 3 | Software requirements | Normative | Software developers, safety PLC application engineers |
| Part 4 | Definitions and abbreviations | Normative | Reference |
| Part 5 | Examples of methods for SIL determination | Informative | Risk assessment practitioners |
| Part 6 | Guidelines on the application of Parts 2 and 3 | Informative | Implementers |
| Part 7 | Overview of techniques and measures | Informative | Implementers |

Parts 1–3 are normative (mandatory). Parts 4–7 are informative or supporting. Most practitioners only need Parts 1, 2, and 3 for implementation; Parts 5–7 provide guidance.

## 5. Relationship to sector standards

IEC 61508 is the root standard. Sector standards derive from it:

| Sector standard | Domain | Simplification relative to IEC 61508 |
|-----------------|--------|--------------------------------------|
| IEC 62061 | Machinery safety control systems | Restricts to high-demand mode; uses PFHd only; simplifies software requirements for application code on certified PLCs |
| IEC 61511 | Process industry SIS | Restricts to low-demand mode; uses PFDavg; allows LOPA for SIL determination; excludes SIL 4 |
| ISA 84 (ANSI/ISA-84.00.01) | Process industry SIS (US) | US adoption of IEC 61511; essentially identical requirements |

**Using the sector standard is preferred over applying IEC 61508 directly** because:
1. Sector standards have eliminated provisions that do not apply to their domain
2. Risk assessment methods are tailored to the domain
3. Hardware tables and SIL claim limits are domain-appropriate
4. Simpler software requirements for application code when using certified safety PLCs

**Apply IEC 61508 directly when:**
- Developing a safety device or safety PLC for sale (manufacturer certification)
- No sector standard exists for the application domain
- The system spans multiple domains (machinery + process + other)
- The certification body requires direct IEC 61508 compliance

## 6. Change log

- 2026-03-06 — Phase 3 corpus creation; Part 1 framework document established.
