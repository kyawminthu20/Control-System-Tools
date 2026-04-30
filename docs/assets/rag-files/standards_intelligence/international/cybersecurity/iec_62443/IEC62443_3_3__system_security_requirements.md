# IEC 62443-3-3 — System Security Requirements and Security Levels

**AI_READ_ACCESS: ALLOWED**

## Standard Reference

| Field | Value |
|-------|-------|
| **Standard** | IEC 62443-3-3 |
| **Edition** | 2013 |
| **Full title** | Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels |
| **Audience** | System Integrator (SI); also Asset Owner and Product Supplier |
| **Scope** | System-level security requirements for IACS, organized by Security Level (SL 1–4) and Foundational Requirement (FR) |

---

## Purpose

IEC 62443-3-3 defines what a system must do to achieve a specified Security Level. It is the technical requirements document that complements the management requirements of IEC 62443-2-1. Where 2-1 asks "do you have a security management program?", 3-3 asks "does your system have the specific technical controls needed for SL X?"

---

## Zone and Conduit Model

The Zone/Conduit model is the architectural foundation of IEC 62443-3-3. All security requirements are applied at the Zone level.

### Zones

A **Zone** is a grouping of logical or physical assets that share a common security policy, trust level, and criticality. Examples:

| Zone | Typical contents | Typical SL target |
|------|-----------------|-------------------|
| Safety zone | Safety PLCs, safety I/O, safety-rated HMI | SL 2–3 |
| Control zone | Standard PLCs, DCS controllers, MES-connected systems | SL 2 |
| Operations zone | HMI workstations, historians, engineering workstations | SL 1–2 |
| Site network zone | Plant LAN, routing infrastructure | SL 1–2 |
| Enterprise DMZ | Perimeter network between plant and corporate | SL 1–2 |
| External connections | Remote access, vendor connections | SL 1 with compensating controls |

Zones must be defined based on the security risk assessment (IEC 62443-3-2 or 2-1 process). All assets with a shared security level and common access control requirements belong in the same Zone.

### Conduits

A **Conduit** is the defined communication path between two Zones. Every conduit must be explicitly authorized, documented, and secured. Undocumented connections between Zones are a finding requiring remediation.

Each conduit has:
- **Direction** — unidirectional (data diode) or bidirectional
- **Protocol** — the protocols permitted across the conduit
- **Security control** — the technology enforcing the conduit (firewall, data diode, unidirectional gateway, encrypted tunnel)
- **Monitoring** — whether traffic across the conduit is logged and monitored

A conduit between a higher-SL Zone and a lower-SL Zone must be designed so that a compromise of the lower-SL Zone cannot compromise the higher-SL Zone.

---

## Security Levels (SL 1–4)

IEC 62443 defines four Security Levels for Zones. Each level adds requirements on top of the previous level.

| Level | Protection against | Threat actor description |
|-------|-------------------|--------------------------|
| **SL 1** | Unintentional or coincidental violations | Untargeted attacks; basic malware; accidental misconfiguration |
| **SL 2** | Intentional violation using simple means | Low-resource attacker with generic skills; script-kiddie; phishing |
| **SL 3** | Intentional violation using sophisticated means | Skilled attacker with IACS knowledge; well-resourced; targeted attack |
| **SL 4** | Intentional violation using sophisticated means with extended resources | Nation-state level; advanced persistent threat; insider with full system access |

SL 2 is the most common target for industrial control system Zones. SL 3 is required for critical infrastructure and high-consequence systems. SL 4 is rarely implemented and reserved for the most critical national infrastructure.

### SL-T vs. SL-C vs. SL-A

| Designation | Meaning | Who determines it |
|-------------|---------|-------------------|
| **SL-T (Target)** | The required SL determined by risk assessment | Asset Owner, from risk assessment process |
| **SL-C (Capability)** | The SL that a Zone can achieve, based on its components and design | System Integrator and Product Supplier |
| **SL-A (Achieved)** | The actual SL achieved after implementation and verification | Verified by the Asset Owner or third party |

The goal is SL-A ≥ SL-T. The System Integrator designs the system to achieve SL-C ≥ SL-T; actual achievement (SL-A) is verified through testing and audit. A gap between SL-A and SL-T requires documented compensating controls.

---

## Foundational Requirements (FR)

IEC 62443-3-3 organizes system security requirements into seven Foundational Requirements (FR). Each FR contains multiple System Requirements (SR), and each SR has Requirement Enhancements (RE) that add capabilities for higher SL levels.

| FR | Title | Description |
|----|-------|-------------|
| **FR 1** | Identification and Authentication Control (IAC) | All users, devices, and software processes must be identified and authenticated before access is granted |
| **FR 2** | Use Control (UC) | Authenticated entities must be authorized only for the resources and actions they require; least privilege enforced |
| **FR 3** | System Integrity (SI) | The system must prevent unauthorized changes to hardware, software, firmware, and configuration |
| **FR 4** | Data Confidentiality (DC) | Sensitive data in transit and at rest must be protected from unauthorized disclosure |
| **FR 5** | Restricted Data Flow (RDF) | Communication must be restricted to authorized flows; Zone/Conduit model enforced at network level |
| **FR 6** | Timely Response to Events (TRE) | Security events must be detected, logged, and responded to in a timely manner; audit logs must be protected |
| **FR 7** | Resource Availability (RA) | The IACS must be available to authorized users when needed; denial-of-service resistance required |

> *Terminology: "Confidentiality" here is the IEC 62443 security property (the C in C-I-A) — protection from unauthorized disclosure, not a content-classification label.*

### FR Applicability by SL

Each SR and RE specifies at which SL it becomes required. The pattern is:
- **SL 1:** Basic control — authentication, basic access control, basic integrity checks, audit logging enabled
- **SL 2:** Adds multifactor authentication for high-privilege accounts, stronger integrity controls, encrypted data in transit for sensitive data, network segmentation enforcement, anomaly detection
- **SL 3:** Adds stronger authentication for all access, encryption for all data in transit, intrusion detection, content inspection at conduits, software integrity verification
- **SL 4:** Adds formal verification methods, hardware-enforced trust, extended tamper protection

---

## Selected System Requirements (SR)

### FR 1 — Identification and Authentication Control

| SR | Requirement | SL 1 | SL 2 | SL 3 | SL 4 |
|----|-------------|------|------|------|------|
| SR 1.1 | Human user identification and authentication | Required | Required | Required | Required |
| SR 1.1 RE 1 | Multifactor authentication for untrusted networks | — | Required | Required | Required |
| SR 1.2 | Software process and device identification | Required | Required | Required | Required |
| SR 1.3 | Account management | Required | Required | Required | Required |
| SR 1.4 | Identifier management | Required | Required | Required | Required |
| SR 1.5 | Authenticator management | Required | Required | Required | Required |
| SR 1.7 | Strength of password-based authentication | Required | Required | Required | Required |
| SR 1.8 | Public key infrastructure (PKI) certificates | — | — | Required | Required |

### FR 5 — Restricted Data Flow (Zone/Conduit enforcement)

| SR | Requirement | SL 1 | SL 2 | SL 3 | SL 4 |
|----|-------------|------|------|------|------|
| SR 5.1 | Network segmentation | Required | Required | Required | Required |
| SR 5.2 | Zone boundary protection | Required | Required | Required | Required |
| SR 5.2 RE 1 | Deny by default at conduit | — | Required | Required | Required |
| SR 5.2 RE 2 | Independent verification of conduit controls | — | — | Required | Required |
| SR 5.3 | General purpose person-to-person communication restrictions | Required | Required | Required | Required |
| SR 5.4 | Application partitioning | — | Required | Required | Required |

### FR 7 — Resource Availability

| SR | Requirement | SL 1 | SL 2 | SL 3 | SL 4 |
|----|-------------|------|------|------|------|
| SR 7.1 | Denial of service protection | Required | Required | Required | Required |
| SR 7.2 | Resource management | Required | Required | Required | Required |
| SR 7.3 | Control system backup | Required | Required | Required | Required |
| SR 7.4 | Control system recovery and reconstitution | Required | Required | Required | Required |
| SR 7.6 | Network and security configuration settings | Required | Required | Required | Required |

---

## Relationship to Functional Safety

The safety boundary and the cybersecurity Zone boundary should align. The Zone containing safety PLCs, safety I/O, and safety HMI should have:

- Higher SL-T (typically SL 2 minimum; SL 3 for high-consequence processes)
- No direct external connections — all access via a defined Conduit with a firewall or data diode
- A Conduit to the standard control Zone, not a direct connection
- Audit logging retained for all access events

A compromise of the safety Zone is a safety hazard. This is why IEC 61511 (2016) and later revisions explicitly require a cybersecurity risk assessment to be performed as part of the functional safety lifecycle.

---

## Practical Zone Design Guidance

1. **Define Zones before selecting equipment.** The Zone/Conduit model is a design input, not a retrofit. Zones determine the security requirements that equipment must meet.

2. **Separate safety and standard control Zones.** Even if both run on the same physical network infrastructure, the safety Zone must be bounded by a conduit (firewall or data diode) that prevents the standard control Zone from sending unsolicited traffic to the safety Zone.

3. **Document every conduit.** Undocumented paths are a compliance finding and a risk. This includes USB ports, removable media, engineering laptop connections, and vendor remote access portals.

4. **Assign SL-T from risk assessment, not by assumption.** A common error is to assign SL 1 to all Zones by default without performing a risk assessment. The risk assessment may determine that the safety Zone requires SL 2 or SL 3 based on the consequence of a successful attack.

5. **SL-C is bounded by the weakest component.** If one device in a Zone cannot support multifactor authentication (an SL 2 requirement for FR 1), then the Zone's SL-C is limited to SL 1 for that FR, unless compensating controls (network-level authentication proxy, jump server with MFA) are implemented.