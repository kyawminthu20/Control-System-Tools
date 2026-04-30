# IEC 62443-4-2 — Component Security Requirements

**AI_READ_ACCESS: ALLOWED**

## Standard Reference

| Field | Value |
|-------|-------|
| **Standard** | IEC 62443-4-2 |
| **Edition** | 2019 |
| **Full title** | Security for industrial automation and control systems — Part 4-2: Technical security requirements for IACS components |
| **Audience** | Product Supplier / Developer |
| **Scope** | Technical security requirements for four component types: embedded devices, software applications, host devices, and network devices |

---

## Purpose

IEC 62443-4-2 specifies the security capabilities that IACS components (products) must have to achieve a Component Security Level (SL-C). Product Suppliers use this standard to design, implement, and certify their products. System Integrators use it to select components with sufficient SL-C for their Zone design.

IEC 62443-4-2 is the component-level counterpart to IEC 62443-3-3 (system-level). A system achieves its target SL when all components within each Zone meet or exceed the Zone's SL-C requirements.

---

## Component Types

IEC 62443-4-2 defines requirements for four component categories:

| Component type | Abbreviation | Examples |
|----------------|-------------|----------|
| **Embedded Device** | ED | Safety PLC, safety relay, process controller, smart field device, variable frequency drive with network interface |
| **Software Application** | SA | SCADA software, HMI application, historian software, engineering workstation software |
| **Host Device** | HD | HMI workstation (hardware platform), engineering workstation, historian server |
| **Network Device** | ND | Industrial Ethernet switch, router, firewall, wireless access point, data diode |

For each component type, IEC 62443-4-2 specifies requirements drawn from the seven Foundational Requirements (FR). Not all FRs apply equally to every component type — for example, FR 5 (Restricted Data Flow) applies to embedded devices and network devices but not software applications; FR 7 (Resource Availability) applies to embedded and network devices but has limited applicability to software applications running on a host. The sections below cover the applicable FRs for each type.

---

## Component Security Level (SL-C)

A product's SL-C is the maximum Security Level the component can support in a system. SL-C is:

- Claimed by the Product Supplier based on the features implemented in the product.
- Verified by a certification body (e.g., TÜV, ISASecure) through product evaluation.
- A prerequisite for using a component in a Zone with a given SL-T. The component SL-C must be ≥ the Zone SL-T for the relevant FR.

**Important constraint:** A Zone's achievable SL-C is bounded by the weakest component in the Zone for each FR. If a Zone contains one device with SL-C 1 for FR 1 (authentication), the Zone cannot achieve SL 2 for FR 1 without compensating controls at the system level.

---

## Selected Requirements by Component Type

### Embedded Devices (ED)

Embedded devices are the most constrained component type — they typically have limited CPU, memory, and OS capabilities.

| FR | Key requirements for SL-C 2 | Notes for embedded devices |
|----|----------------------------|---------------------------|
| FR 1 (IAC) | Unique identity per device; authenticate users and remote sessions; enforce account lockout | Some legacy embedded devices cannot support strong authentication — this limits SL-C to 1 |
| FR 2 (UC) | Enforce least-privilege access; separate user and administrative accounts | Role-based access control required at SL-C 2 |
| FR 3 (SI) | Firmware integrity verification on boot; report unauthorized changes | Secure boot required at SL-C 2; hardware root of trust for SL-C 3 |
| FR 4 (DC) | Protect sensitive configuration data at rest | Encryption or secure storage required at SL-C 2 |
| FR 5 (RDF) | Enforce allowed protocols and ports; block unsolicited inbound connections | Stateful filtering or per-port enable/disable |
| FR 6 (TRE) | Log security-relevant events with timestamps; protect log integrity | Syslog or secure log export to SIEM |
| FR 7 (RA) | Continue operating under degraded network conditions; support backup and restore | Must not fail-unsafe when network is disrupted |

**Key point for safety PLCs:** A safety PLC operating in a safety Zone must not fail to a dangerous state due to a cyberattack or network disruption. This is the intersection of cybersecurity and functional safety — the safety function must remain available (FR 7) and the safety system must reject unauthorized commands (FR 1, FR 2).

### Software Applications (SA)

FR 5 (RDF) does not apply to SA — data flow restriction is enforced at the network and host layer, not within the application itself. FR 7 (RA) availability requirements are met at the Host Device (HD) layer for applications running on a general-purpose OS.

| FR | Key requirements for SL-C 2 |
|----|----------------------------|
| FR 1 (IAC) | User authentication with session management; support for directory services (LDAP/AD) |
| FR 2 (UC) | Role-based access control; least privilege for background processes; privilege separation |
| FR 3 (SI) | Application integrity checks; protection against tampering of application files |
| FR 4 (DC) | Encryption of sensitive configuration and credentials; no hardcoded credentials |
| FR 6 (TRE) | Security event logging with user attribution; log tampering protection |

### Host Devices (HD)

Host devices are general-purpose hardware platforms (workstations, servers) running software applications. Their requirements combine OS-level hardening with the SA requirements above.

| FR | Key requirements for SL-C 2 |
|----|----------------------------|
| FR 1 (IAC) | OS-level user authentication; MFA for privileged accounts; screen lock and session timeout |
| FR 2 (UC) | Least-privilege OS accounts; application whitelisting; separation of engineering and operator accounts |
| FR 3 (SI) | OS integrity controls; disable unused services and ports; host-based intrusion detection |
| FR 4 (DC) | Encrypted storage for sensitive data; OS credential store protection; full-disk encryption where supported |
| FR 5 (RDF) | Host-based firewall; restrict inbound/outbound connections to documented protocols and destinations |
| FR 6 (TRE) | OS and application event logging; log forwarding to SIEM; NTP synchronization |
| FR 7 (RA) | OS and application backup and restore; tested recovery procedure; redundant power for critical HMI hosts |

### Network Devices (ND)

| FR | Key requirements for SL-C 2 |
|----|----------------------------|
| FR 1 (IAC) | Authentication for all management access; no default credentials |
| FR 2 (UC) | Role-based management access; read-only and read-write roles |
| FR 3 (SI) | Firmware integrity; configuration integrity; protection against unauthorized configuration changes |
| FR 4 (DC) | Encrypted management traffic (SSH/TLS for CLI and HTTPS for web management); secure storage of credentials; encryption of configuration backups |
| FR 5 (RDF) | Stateful packet inspection; support for VLAN; ability to enforce Zone/Conduit policies |
| FR 6 (TRE) | Syslog for security events; NTP time synchronization for log correlation |
| FR 7 (RA) | Storm control; rate limiting; resilience to broadcast storms and DoS conditions |

---

## Secure Product Development (IEC 62443-4-1)

IEC 62443-4-2 defines what a product must do. IEC 62443-4-1 defines how a product must be developed — the Security Development Lifecycle (SDL) that the Product Supplier must follow.

| IEC 62443-4-1 element | Description |
|----------------------|-------------|
| Security management | Security requirements in the development process; security roles and responsibilities |
| Security requirements | Defining security requirements as a formal input to product design |
| Secure design | Threat modeling; security architecture review; design against security requirements |
| Secure implementation | Secure coding standards; use of approved libraries; prohibition of banned functions |
| Security verification | Security testing: static analysis, dynamic analysis, vulnerability scanning, penetration test |
| Defect management | Security defect tracking; responsible disclosure policy; patch release process |
| Security update management | Defined patch support period; vulnerability notification to customers |
| Security guidelines documentation | Secure installation guide; hardening guide; security capabilities documentation for each component |

A product supplier with IEC 62443-4-1 certification has demonstrated that their development process includes the above elements. This is evidence of process maturity, separate from the product capability claimed under IEC 62443-4-2.

---

## Selecting Components for a Zone

When selecting components for a Zone with a defined SL-T:

1. **Identify the SL-T for the Zone** from the security risk assessment.
2. **For each FR, identify the SL-C requirement** — the component must have SL-C ≥ SL-T for that FR.
3. **Review product documentation and certification** — confirm the claimed SL-C and review the security capabilities document.
4. **Identify gaps** — where a required component cannot meet SL-T, document the gap and implement compensating controls at the system level (additional authentication at a jump server, network-level filtering to compensate for lack of per-device authentication, etc.).
5. **Document the compensating control** — the Asset Owner's CSMS must record every compensating control, its rationale, and its review date.

---

## Common Findings in Component Assessment

> *Terminology: "Data confidentiality" referenced below is the IEC 62443 security property (the C in C-I-A) — protection from unauthorized disclosure, not a content-classification label.*

1. **Default credentials not changed** — many embedded devices ship with default usernames and passwords. FR 1 requires unique credentials; failing to change defaults is an immediate SL-C 1 failure.
2. **No secure boot** — legacy PLCs often have no firmware integrity verification. SL-C 2 for FR 3 requires firmware integrity on boot; compensating controls (physical access control, network-level restriction) must be documented.
3. **Unencrypted management protocols** — devices using Telnet, HTTP, or SNMP v1/v2 in management interfaces cannot meet FR 4 data confidentiality requirements without compensating controls.
4. **No log export** — devices with only internal logs that cannot be exported fail FR 6 requirements at SL-C 2 for centralized monitoring.
5. **Hardcoded credentials in software** — a finding that causes immediate SL-C failure; requires vendor remediation.