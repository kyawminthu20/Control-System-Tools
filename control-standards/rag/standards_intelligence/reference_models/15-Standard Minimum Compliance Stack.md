<!--
CONTENT_CLASS: DERIVED_REFERENCE
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

**AI_READ_ACCESS: ALLOWED**

Semiconductor equipment builders such as ASML and Applied Materials do not rely on a single machine-safety standard. Instead they maintain an internal **minimum compliance stack**.

The goal is to ensure a tool can be installed in **US, EU, and Asian fabs** without redesign. The list below represents a realistic **baseline stack** used for high-value semiconductor tools.

---

# 15-Standard Minimum Compliance Stack

_(Semiconductor Equipment Architecture)_

These standards cover **five technical domains**:

1. Machine safety
2. Electrical systems
3. Functional safety
4. Hazardous materials & gases
5. Cybersecurity and factory integration

---

# 1. Core Machinery Safety (Foundation)

These are the **first standards applied when designing a machine**.

| Standard    | Purpose                                    |
| ----------- | ------------------------------------------ |
| ISO 12100   | Defines the formal hazard analysis process |
| ISO 13849-1 | Performance Level safety design            |
| IEC 60204-1 | Electrical machine design (international)  |

Why they matter:

```
ISO 12100 → identify hazards
ISO 13849 → design safety functions
IEC 60204 → implement electrical system
```

These three standards form the **core of CE compliance**.

---

# 2. US Electrical Compliance

Most semiconductor tools are installed in **US fabs**, so these are mandatory.

| Standard | Purpose                            |
| -------- | ---------------------------------- |
| NFPA 79  | US machine electrical requirements |
| NFPA 70  | installation code                  |
| UL 508A  | control panel construction         |

Important relationship:

```
NEC Article 670
   ↓
references NFPA 79
```

So the tool must follow **NFPA 79 to be NEC compliant**.

---

# 3. Functional Safety (System-Level)

For complex tools (robots, motion systems, vacuum systems), these standards are used.

| Standard  | Purpose                    |
| --------- | -------------------------- |
| IEC 62061 | SIL-based machinery safety |
| IEC 61508 | foundation standard        |
| ISO 13850 | E-stop design requirements |

Typical semiconductor tool safety level:

```
PL d or PL e
```

---

# 4. Hazardous Materials & Gas Systems

Semiconductor tools use:

- toxic gases
- corrosive chemicals
- high-pressure gas cylinders

Therefore additional standards apply.

| Standard | Purpose                        |
| -------- | ------------------------------ |
| SEMI S2  | semiconductor equipment safety |
| SEMI S8  | operator safety                |
| SEMI S14 | fire hazards in tools          |
| NFPA 318 | fab safety requirements        |

These are **unique to semiconductor fabs**.

---

# 5. Industrial Cybersecurity

Modern semiconductor tools are fully networked.

Therefore cybersecurity standards apply.

| Standard       | Purpose                        |
| -------------- | ------------------------------ |
| IEC 62443      | industrial automation security |
| NIST SP 800-82 | US ICS security guidance       |

Typical fab rule:

```
Tools cannot connect directly to the internet.
```

All communication goes through **factory network gateways**.

---

# Complete Semiconductor Compliance Stack

```
1  ISO 12100
2  ISO 13849-1
3  ISO 13850
4  IEC 60204-1
5  IEC 62061
6  IEC 61508
7  NFPA 79
8  NFPA 70 (NEC)
9  UL 508A
10 SEMI S2
11 SEMI S8
12 SEMI S14
13 NFPA 318
14 IEC 62443
15 NIST SP 800-82
```

This stack ensures compliance with:

- **US regulations**
- **European CE marking**
- **Semiconductor fab safety rules**

---

# Architecture Impact

These standards influence the machine architecture.

Typical semiconductor tool architecture:

```
Factory Network
      │
Tool Controller
      │
PLC / Motion Controller
      │
Safety PLC
      │
Field Devices
```

Safety functions include:

- chamber door interlock
- robot motion safety
- gas leak shutdown
- vacuum chamber safety

---

# Why Semiconductor Tools Use Such a Large Stack

Semiconductor equipment has:

- high voltages
- hazardous gases
- robotics
- vacuum systems
- chemical processing
- automated wafer handling

So **multiple risk domains overlap**.

This is why these machines follow a **multi-standard compliance model**.

---

# How This Fits Your Repository

Your **standards intelligence system** could include a machine scenario like this:

```
scenario/
   semiconductor_tool/
       applicable_standards.md
       safety_architecture.md
       risk_assessment_template.md
       compliance_checklist.md
```

The system could then automatically answer:

```
What standards apply to a wafer etching tool?
```

---

# Practical Advice

Your repository is already structured correctly to support this type of standards reasoning.

The next logical improvement is to add:

```
rag/standards_intelligence/scenario/
```

with machine types such as:

```
robot_cell
chemical_dosing_skid
hydraulic_press
semiconductor_tool
conveyor_system
```