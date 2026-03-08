---
layout: default
title: "IEC 62443 — Industrial Cybersecurity"
description: "IEC 62443 series — IACS security levels, Zone/Conduit model, foundational requirements, and security lifecycle for industrial automation and control systems."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "Cybersecurity"
    url: "/standards/cybersecurity/"
  - name: "IEC 62443"
repo_path: "control-standards/rag/standards_intelligence/international/cybersecurity/iec_62443/"
related_standards:
  - name: "IEC 62061 (SIL machinery)"
    url: "/standards/functional-safety/iec-62061/"
  - name: "ISO 13849-1 (PL machinery)"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 61511 (process safety)"
    url: "/standards/functional-safety/iec-61511/"
  - name: "Networked Safety PLC Scenario"
    url: "/scenarios/networked-safety-plc/"
lifecycle_stage:
  - name: "Safety Architecture"
    slug: "safety-architecture/"
  - name: "Detailed Design"
    slug: "detailed-design/"
---

<div class="page-header">
  <span class="page-header__label">Cybersecurity · IEC 62443</span>
  <h1>IEC 62443 — Industrial Automation and Control System Security</h1>
  <span class="badge badge--complete">Phase 5 Complete</span>
</div>

## Quick Start

- IEC 62443 applies to any networked Industrial Automation and Control System (IACS) — PLCs, DCS, HMIs, historians, SCADA systems, and safety systems with network interfaces.
- Start with the **Zone and Conduit model** (IEC 62443-3-3): group assets by trust level, define all communication paths as explicit Conduits.
- Assign a **Security Level Target (SL-T)** to each Zone from a security risk assessment. Most industrial Zones target SL 2; safety-critical Zones may require SL 3.
- **SL levels (1–4) measure cybersecurity capability — they are not equivalent to SIL levels (1–4) from IEC 62061 / IEC 61511, which measure functional safety probability.** Never substitute one for the other.
- IEC 61511 (2016) requires a security assessment as part of the functional safety lifecycle. Use IEC 62443 to satisfy that requirement.

---

## Standard Series Overview

| Standard | Scope | Audience |
|----------|-------|----------|
| **IEC 62443-2-1** (2010) | IACS security management system (CSMS) — risk assessment, policy, asset inventory | Asset Owner |
| **IEC 62443-2-4** (2015) | Security requirements for System Integrators | System Integrator |
| **IEC 62443-3-2** (2020) | Security risk assessment for system design | System Integrator, Asset Owner |
| **IEC 62443-3-3** (2013) | System security requirements and Security Levels | System Integrator |
| **IEC 62443-4-1** (2018) | Secure product development lifecycle | Product Supplier |
| **IEC 62443-4-2** (2019) | Technical component security requirements | Product Supplier |

**Corpus coverage in this site:** IEC 62443-2-1, 3-3, 4-2, and lifecycle guidance — the parts most directly applicable to an Asset Owner designing and operating an IACS.

---

## Security Levels (SL 1–4)

IEC 62443 defines four Security Levels for Zones. Each level targets a progressively more capable attacker.

| Level | Attacker profile | Typical IACS application |
|-------|-----------------|--------------------------|
| **SL 1** | Unintentional or untargeted attack — basic malware, accidental misconfiguration | Enterprise DMZ, low-consequence operational zones |
| **SL 2** | Intentional attack with simple means — phishing, script-kiddie, generic exploits | Most industrial control and safety Zones |
| **SL 3** | Sophisticated, targeted attack with IACS knowledge — skilled attacker, targeted malware | Critical infrastructure, high-consequence safety systems |
| **SL 4** | Nation-state level, advanced persistent threat — extended resources, insider capability | Reserved for the most critical national infrastructure |

**SL 2 is the standard target for industrial control system Zones.** SL 3 is required when a successful attack would have high-consequence safety or environmental effects.

### SL-T vs. SL-C vs. SL-A

| Designation | Meaning |
|-------------|---------|
| **SL-T (Target)** | Required SL, determined by risk assessment |
| **SL-C (Capability)** | SL the system can achieve, based on design and components |
| **SL-A (Achieved)** | Actual SL achieved after implementation and verification |

Goal: **SL-A ≥ SL-T**. Gaps require documented compensating controls.

---

## SIL vs. SL — Critical Distinction

This is one of the most common points of confusion when functional safety and cybersecurity overlap.

| Attribute | SIL (IEC 62061 / IEC 61511) | SL (IEC 62443) |
|-----------|---------------------------|----------------|
| **Standard family** | Functional safety | Industrial cybersecurity |
| **What it measures** | Probability of dangerous failure per hour (PFHd) | Resistance to cyberattack by a defined threat actor |
| **Range** | SIL 1–4 | SL 1–4 |
| **Methodology** | Quantitative (PFHd calculation, architecture, proof test) | Qualitative/semi-quantitative (threat model, control gap analysis) |
| **Interchangeable?** | **No** — a safety PLC rated SIL 2 does not imply SL 2 cybersecurity capability. These are entirely separate assessments. |

A safety PLC may achieve SIL 3 for functional safety while having SL 1 cybersecurity capability (e.g., default passwords not changed, no network segmentation). Both assessments are required and independent.

---

## Zone and Conduit Model

The Zone/Conduit model is the architectural foundation for IACS cybersecurity design.

<div class="mermaid-wrap">
<pre class="mermaid">
graph TD
    subgraph EZ["Enterprise Zone (SL 1)"]
        ERP[ERP / Business Systems]
        DMZ[DMZ / Historian Mirror]
    end

    subgraph OZ["Operations Zone (SL 1–2)"]
        HIS[Historian]
        EWS[Engineering Workstation]
    end

    subgraph CZ["Control Zone (SL 2)"]
        PLC[Standard PLC]
        HMI[Operator HMI]
        NET[Industrial Network]
    end

    subgraph SZ["Safety Zone (SL 2–3)"]
        SPLC[Safety PLC]
        SIO[Safety I/O]
        SHMI[Safety HMI]
    end

    EZ -- "Conduit: Firewall\n(restricted, logged)" --> OZ
    OZ -- "Conduit: Firewall\n(deny by default)" --> CZ
    CZ -- "Conduit: Firewall or\nData Diode (unidirectional)" --> SZ

    style SZ fill:#ffeeee,stroke:#cc0000
    style CZ fill:#fff8ee,stroke:#cc8800
    style OZ fill:#eeffee,stroke:#008800
    style EZ fill:#eeeeff,stroke:#0000cc
</pre>
</div>

**Design principles:**
- Every Zone has a defined SL-T from the risk assessment.
- Every inter-Zone connection is a documented Conduit with a security control (firewall, data diode, encrypted tunnel).
- The Safety Zone has the most restrictive Conduit — typically unidirectional (data out only) or a dedicated firewall with deny-by-default policy.
- No direct connections between Safety Zone and Enterprise Zone are permitted.

---

## Foundational Requirements (FR)

IEC 62443-3-3 organizes all system security requirements into seven Foundational Requirements:

| FR | Title | Core at SL 2 |
|----|-------|-------------|
| **FR 1** | Identification and Authentication Control | MFA for privileged access via untrusted networks; device authentication |
| **FR 2** | Use Control | Least-privilege authorization; role-based access control |
| **FR 3** | System Integrity | Integrity verification for software and firmware; secure boot |
| **FR 4** | Data Confidentiality | Encryption for sensitive data in transit; no hardcoded credentials |
| **FR 5** | Restricted Data Flow | Zone/Conduit enforcement; deny-by-default at Zone boundaries |
| **FR 6** | Timely Response to Events | Security event logging with timestamps; log integrity protection; SIEM integration |
| **FR 7** | Resource Availability | DoS resistance; control system backup and recovery; tested restore procedures |

**SL 2 adds over SL 1:** MFA for untrusted network access (FR 1 RE 1), deny-by-default conduit policy (FR 5 SR 5.2 RE 1), encrypted data in transit for sensitive data (FR 4), application partitioning (FR 5), SIEM-capable logging (FR 6).

---

## IACS Security Lifecycle

The IEC 62443 security lifecycle mirrors the structure of functional safety lifecycles.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
    A1[Asset\nInventory] --> A2[Security Risk\nAssessment]
    A2 --> A3[Zone/Conduit\nDesign + SL-T]
    A3 --> A4[Gap\nAnalysis]

    A4 --> B1[Network\nSegmentation]
    B1 --> B2[Access Control\nHardening]
    B2 --> B3[Integrity +\nMonitoring Controls]
    B3 --> B4[Security\nVerification\nSL-A ≥ SL-T]

    B4 --> C1[Vulnerability\nMonitoring]
    C1 --> C2[Patch\nManagement]
    C2 --> C3[Periodic\nAudit]
    C3 --> C4[Incident\nResponse]
    C4 --> A2

    subgraph ASSESS["ASSESS"]
        A1; A2; A3; A4
    end
    subgraph IMPLEMENT["IMPLEMENT"]
        B1; B2; B3; B4
    end
    subgraph MAINTAIN["MAINTAIN"]
        C1; C2; C3; C4
    end
</pre>
</div>

---

## Relationship to Functional Safety

The safety boundary and cybersecurity Zone boundary must align. When a safety system has a network interface, it must be assessed under IEC 62443 as well as its safety standard.

| Coordination point | Functional safety requirement | IEC 62443 requirement |
|-------------------|------------------------------|----------------------|
| Risk assessment | Hazard identification and SIL/PL determination | Security risk assessment and SL-T determination |
| System design | Safety architecture (subsystem decomposition) | Zone/Conduit design (safety Zone isolation) |
| Commissioning | Safety system validation (IEC 62061 Clause 8) | Security verification (SL-A assessment) |
| Change management | Safety impact assessment on any SRECS change | Security impact assessment on any Zone change |
| Incident response | Functional safety alarm and shutdown procedure | Cybersecurity incident response; containment must not create new safety hazards |

**IEC 61511:2016 Clause 8.2.4** explicitly requires that a security risk assessment be performed for safety instrumented systems. IEC 62443 is the recognized framework for satisfying that requirement.

---

## Practical Checklist — Safety Zone Cybersecurity

- [ ] Safety Zone defined with documented boundary: which devices are in, which are out.
- [ ] SL-T assigned to the Safety Zone from security risk assessment (typically SL 2 minimum).
- [ ] All Conduits to/from Safety Zone documented: direction, protocol, security control, monitoring.
- [ ] Deny-by-default policy on the Safety Zone Conduit firewall; all permitted traffic explicitly listed.
- [ ] No direct remote access to Safety Zone — remote access routes via a jump server or secure access portal in the Operations Zone.
- [ ] Asset inventory for Safety Zone complete: device make, model, firmware version, network addresses.
- [ ] Default credentials changed on all devices in Safety Zone; accounts with unique credentials per user.
- [ ] Audit logging enabled on Safety Zone devices; logs forwarded to tamper-protected storage or SIEM.
- [ ] Patch management procedure covers Safety Zone devices; vendor authorization for patches confirmed.
- [ ] Incident response plan includes Safety Zone; containment actions pre-approved to avoid new safety hazards.
- [ ] Security verification results documented: SL-A ≥ SL-T confirmed for all FRs at SL 2.
- [ ] Functional safety and cybersecurity assessments cross-referenced in the safety case documentation.

---

## Repository Paths

| Reference | Path |
|-----------|------|
| Security management system | `rag/international/cybersecurity/iec_62443/IEC62443_2_1__security_management.md` |
| System security requirements | `rag/international/cybersecurity/iec_62443/IEC62443_3_3__system_security_requirements.md` |
| Component requirements | `rag/international/cybersecurity/iec_62443/IEC62443_4_2__component_requirements.md` |
| Security lifecycle | `rag/international/cybersecurity/iec_62443/IEC62443_lifecycle.md` |
| Networked Safety PLC scenario | `docs/scenarios/networked-safety-plc/` |
| Software stack routing | `docs/software-stack/` |
