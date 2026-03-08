I reviewed the NEC page. It is structurally solid, but it needs a tighter **compliance-focused update** and a few **content corrections/clarifications**.

## What is already working

The page correctly frames NEC as the **legal installation baseline** in the U.S., and it correctly highlights the central industrial articles: **250, 310, 409, 430, 670, and 725**. It also correctly calls out **409.110 SCCR marking** and the practical relationship between **NEC Article 670** and **NFPA 79**. ([Kyaw Min Thu][1])

## Recommended updates

### 1. Add a clear “Use this page for…” section

Right now the page explains what NEC is, but not how an engineer should use it. Add a short section near the top:

- **Use NEC for:** feeder sizing, branch circuit protection, grounding/bonding, disconnecting means, installation rules, field wiring methods.
- **Do not use NEC alone for:** machine internal wiring details, panel construction method, functional safety validation, risk reduction architecture.

That would make the boundary between **NEC vs NFPA 79 vs UL 508A vs ISO 13849 / IEC 62061** much clearer. The page already implies this, but it should say it directly. ([Kyaw Min Thu][1])

### 2. Tighten the statement about Article 409 and UL 508A

Current wording says Article 409 “requires UL listing or field evaluation.” That is directionally useful, but too compressed. A better phrasing is:

> “NEC Article 409 requires industrial control panels to be suitably marked and installed, and SCCR must be established. Listed/labeled assemblies or an approved method may be used; UL 508A Supplement SB is a common approved method for determining SCCR.”

That is closer to the actual structure of 409.110 and avoids overstating “UL 508A listing” as the only path. ([Kyaw Min Thu][1])

### 3. Add **409.70** and **670.6** to the key article list

Your “Key Articles” table is missing two high-value 2023 items for modern machine/control work:

- **409.70 — Surge Protection**
- **670.6 — Overvoltage Protection**

These matter for industrial machinery and safety circuits, and they are highly relevant to your audience building machine/control content. ([citel.us][2])

### 4. Add a sharper adoption warning

The page says NEC is adopted by most states and local jurisdictions. That is basically fine, but for engineering use the site should say:

> “Always verify the edition adopted by the local AHJ. Many jurisdictions are not on the same NEC cycle.”

That is an important field reality, especially for projects spanning multiple states or retrofit work. The page already references AHJ enforcement, so this is a natural extension. ([Kyaw Min Thu][1])

### 5. Add a “machine builder checklist” block

This page would become much more useful if it ended with a 6–8 line checklist such as:

- Determine available fault current at installation point
- Establish panel SCCR
- Verify feeder and branch-circuit conductor sizing
- Verify motor branch short-circuit/ground-fault protection
- Verify overload protection
- Verify machine disconnecting means
- Verify grounding/bonding
- Verify surge/overvoltage protection where safety circuits are involved

That would convert the page from “reference note” into “engineering tool.” The content basis is already present on the page. ([Kyaw Min Thu][1])

### 6. Clarify NEC vs NFPA 79 relationship more carefully

Your sentence:

> “Article 670 makes NFPA 79 the effective electrical design standard for industrial machinery in the US market.”

is useful, but I would soften it slightly to avoid sounding absolute:

> “For industrial machinery, NEC Article 670 points engineers toward NFPA 79 for many machine electrical design details, while NEC remains the enforceable installation code.”

That is more precise and less likely to be challenged by a reviewer. ([Kyaw Min Thu][1])

### 7. Add a “Not covered here” section

This page should explicitly say NEC does **not** by itself determine:

- PL/SIL target
- safety architecture category
- stop category selection
- guarding strategy
- risk assessment method

That avoids users treating NEC as a full machine safety design standard. ([Kyaw Min Thu][1])

### 8. Improve the page metadata block

Add these fields:

- **Last reviewed date**
- **Edition adoption caveat**
- **Primary audience**: panel designers, machine builders, controls engineers, AHJ-facing documentation
- **Companion standards**: NFPA 79, UL 508A, ISO 12100, ISO 13849-1, IEC 60204-1

That will make the page feel more intentional and operational.

## Best single content update to make now

If you only do one update, do this:

> **Expand the page from “overview” to “decision page” by adding 409.70, 670.6, a machine-builder checklist, and a clearer NEC / NFPA 79 / UL 508A boundary.**

That will give the highest value increase with the least rewrite effort. ([Kyaw Min Thu][1])

## Suggested replacement text for the key relationship section

You could replace the current relationship block with this:

> **NEC is the enforceable installation code.**
> **Article 409** governs industrial control panel installation/marking, including SCCR marking.
> **Article 670** applies to industrial machinery as installed equipment and points to **NFPA 79** for many machine electrical design details.
> **UL 508A** is commonly used to build and evaluate panel construction, including SCCR determination by approved method.
> Functional safety requirements such as PL/SIL are handled separately through standards such as **ISO 13849-1** and **IEC 62061**.

That wording is cleaner and safer.

## Bottom line

The page is good as a **navigation node**, but not yet strong enough as a **working engineering reference**.
The priority fixes are:

1. clarify NEC vs NFPA 79 vs UL 508A boundaries,
2. add **409.70** and **670.6**,
3. soften a few absolute statements,
4. add a practical checklist.

If you want, I can rewrite this NEC page into a stronger production-ready version in your site style.

[1]: https://kyawminthu20.github.io/Control-System-Tools/standards/us-electrical/nec/ "NEC (NFPA 70) — National Electrical Code — Control System Standards Atlas"
[2]: https://citel.us/en/nec-2023-article-409-industrial-control-panels?utm_source=chatgpt.com "NEC 2023 Article 409 Industrial Control Panels"

Below is a **clean rewritten version of your NEC page** designed to fit a **technical standards knowledge base** like your Control-System-Tools site.
It keeps the structure simple, removes ambiguous wording, and makes the page useful for **machine builders and control engineers**.

You can paste this directly into a **Jekyll Markdown page**.

---

# National Electrical Code (NEC)

## Overview

The **National Electrical Code (NEC)** is the primary electrical installation code used in the United States. It defines the minimum safety requirements for the **design, installation, and inspection of electrical systems**.

The NEC is published by the **National Fire Protection Association (NFPA)** as **NFPA 70**.

The purpose of the NEC is to protect people and property from hazards arising from electricity such as:

- Electric shock
- Electrical fires
- Equipment damage
- Arc flash hazards

Unlike many engineering standards, the NEC is typically **adopted into law by state and local governments** and enforced by the **Authority Having Jurisdiction (AHJ)**.

---

## What the NEC Covers

For industrial control systems and machinery, the NEC governs the **electrical installation environment**, including:

- Power distribution systems
- Feeder and branch circuits
- Conductor sizing
- Grounding and bonding
- Short-circuit protection
- Disconnecting means
- Wiring methods
- Industrial control panel installation
- Motor circuits and protection

These rules apply to **how electrical systems are installed in a facility**, not how machines internally function.

---

## What the NEC Does NOT Cover

The NEC does **not** define the full electrical design of industrial machinery or functional safety architecture.

It does not determine:

- Machine risk assessment
- Safety integrity level (SIL)
- Performance level (PL)
- Safety controller architecture
- Guarding strategies
- Emergency stop design categories

These areas are covered by other standards such as:

- **NFPA 79** – Electrical Standard for Industrial Machinery
- **ISO 13849-1** – Safety of machinery (Performance Level)
- **IEC 62061** – Functional Safety of Machinery
- **ISO 12100** – Machine risk assessment

The NEC therefore acts as the **facility installation code**, while other standards govern **machine design and safety systems**.

---

## Key NEC Articles for Control Engineers

The following NEC articles are particularly relevant to **industrial machinery and control systems**.

| Article | Title                         | Relevance                                                                  |
| ------- | ----------------------------- | -------------------------------------------------------------------------- |
| 250     | Grounding and Bonding         | Defines protective grounding requirements for equipment and control panels |
| 300     | Wiring Methods                | Installation rules for cables, conduits, and raceways                      |
| 310     | Conductors for General Wiring | Conductor sizing and insulation ratings                                    |
| 409     | Industrial Control Panels     | SCCR marking and panel installation requirements                           |
| 430     | Motors and Motor Circuits     | Motor branch circuit protection and overload protection                    |
| 670     | Industrial Machinery          | Installation requirements for machines in industrial facilities            |
| 725     | Class 1, 2, and 3 Circuits    | Control and signaling circuits                                             |

---

## Industrial Control Panels (NEC Article 409)

Article 409 governs **industrial control panels installed in facilities**.

Key requirements include:

- Panels must be **properly marked**
- The **Short-Circuit Current Rating (SCCR)** must be determined and displayed
- The panel must be **installed within its rating**

The NEC does not prescribe a single method for determining SCCR.
However, **UL 508A Supplement SB** is commonly used by panel builders to calculate SCCR.

Typical panel markings include:

- Nominal voltage
- Phase
- Frequency
- SCCR
- Panel identification

---

## Industrial Machinery (NEC Article 670)

Article 670 applies to **industrial machines installed in facilities**.

It primarily addresses:

- Machine disconnecting means
- Supply circuit requirements
- Overcurrent protection
- Installation considerations

For many detailed electrical design aspects of machines, Article 670 points engineers toward **NFPA 79**, which provides detailed requirements for:

- Machine control circuits
- Emergency stops
- Safety circuits
- Machine wiring practices

In practice:

- **NEC governs installation in the facility**
- **NFPA 79 governs machine electrical design**

---

## Relationship to Other Standards

Industrial electrical systems typically involve several complementary standards.

| Standard      | Scope                                        |
| ------------- | -------------------------------------------- |
| NEC (NFPA 70) | Electrical installation code enforced by AHJ |
| NFPA 79       | Electrical design of industrial machinery    |
| UL 508A       | Construction of industrial control panels    |
| ISO 12100     | Machine risk assessment                      |
| ISO 13849-1   | Safety control system Performance Levels     |
| IEC 60204-1   | Electrical equipment of machinery            |

Together these standards form the **minimum compliance stack for industrial machines in the U.S.**

---

## Typical Machine Builder Workflow

When designing a machine for the U.S. market, engineers typically follow this sequence:

1. Perform machine **risk assessment** (ISO 12100)
2. Determine required **PL or SIL** level (ISO 13849 / IEC 62061)
3. Design the **safety architecture**
4. Design machine electrical system (NFPA 79)
5. Build control panel (UL 508A)
6. Verify **SCCR and electrical protection**
7. Install equipment according to **NEC requirements**
8. Pass **AHJ inspection**

---

## Practical Compliance Checklist

Before installing a machine in a facility, verify the following:

- Available fault current at installation point
- Control panel SCCR rating
- Feeder and branch circuit protection
- Motor overload protection
- Machine disconnect location
- Proper grounding and bonding
- Proper conductor sizing
- Surge or overvoltage protection where required

---

## Adoption and Enforcement

The NEC is published every **three years**.

However, each state or municipality adopts a specific edition, so the **active code version may vary by jurisdiction**.

Always verify the applicable NEC edition with the **local Authority Having Jurisdiction (AHJ)**.

---

## Summary

The **National Electrical Code** provides the foundational rules for electrical installations in the United States.

For industrial machinery:

- NEC governs **how electrical systems are installed in a facility**
- NFPA 79 governs **how machines are electrically designed**
- UL 508A governs **how industrial control panels are constructed**
- ISO standards govern **machine safety and risk reduction**

Understanding the relationship between these standards is essential for designing compliant industrial automation systems.

---

If you'd like, I can also show you **3 improvements that would make your entire standards site look like a professional engineering reference library** (the NEC page is only one part of the structure).

Your site already has the **right concept**: a standards knowledge base for control engineers. What it needs now is **structure and decision guidance** so engineers can quickly understand _which standard to use and when_.

Below are **three high-impact improvements** that would significantly strengthen the entire site.

---

# 1. Build a “Standards Relationship Map” (Most Important)

Right now, pages exist individually (NEC, NFPA 79, UL 508A, ISO standards).
But engineers need to understand **how they connect in a real machine design**.

Add a **standards relationship diagram** on the homepage and on each standard page.

Example structure:

```
Machine Safety Stack (US Industrial Machinery)

Risk Assessment
│
├─ ISO 12100
│
Safety Architecture
│
├─ ISO 13849
├─ IEC 62061
│
Machine Electrical Design
│
├─ NFPA 79
│
Control Panel Construction
│
├─ UL 508A
│
Electrical Installation
│
├─ NEC (NFPA 70)
```

This will instantly show visitors:

- NEC is **installation**
- NFPA 79 is **machine electrical design**
- UL 508A is **panel construction**
- ISO standards define **safety architecture**

This relationship is the **core concept most engineers struggle with**.

---

# 2. Add “Engineer Decision Guides”

Instead of only explaining standards, add **decision guides**.

Example page:

## Which Standard Applies?

| Situation                                | Primary Standard |
| ---------------------------------------- | ---------------- |
| Installing a control panel in a facility | NEC              |
| Designing machine wiring                 | NFPA 79          |
| Building a control panel                 | UL 508A          |
| Designing safety circuits                | ISO 13849        |
| Performing machine risk assessment       | ISO 12100        |

This transforms the site from:

**Reference library → engineering decision tool**

---

# 3. Add “Machine Design Workflow”

One of the strongest additions would be a **machine lifecycle page** that explains how standards apply during machine design.

Example:

## Industrial Machine Compliance Workflow

1. **Risk Assessment**
   - ISO 12100

2. **Determine Safety Performance Level**
   - ISO 13849 / IEC 62061

3. **Design Safety Circuits**
   - ISO 13849
   - IEC 62061

4. **Design Machine Electrical System**
   - NFPA 79

5. **Build Control Panel**
   - UL 508A

6. **Verify SCCR**
   - UL 508A SB

7. **Install Machine**
   - NEC

8. **Inspection**
   - AHJ / Local Code Authority

This page becomes a **core reference for engineers building machines**.

---

# Additional Improvements (Optional but Valuable)

### Add “Field Engineering Notes”

Example sections:

- Common NEC violations
- SCCR mistakes
- Grounding mistakes
- Control panel installation errors

These practical insights make the site far more useful than a textbook.

---

### Add Industry Variants

Different industries use slightly different compliance stacks.

Example:

| Industry        | Extra Standards |
| --------------- | --------------- |
| Semiconductor   | SEMI S2         |
| Offshore        | ABS / DNV       |
| Nuclear         | IEEE / NRC      |
| Medical         | IEC 60601       |
| Food & Beverage | 3-A / EHEDG     |

---

### Add Quick Reference Tables

Example:

#### Typical Control Voltage Colors (NFPA 79)

| Voltage        | Color  |
| -------------- | ------ |
| 24VDC control  | Blue   |
| AC control     | Red    |
| Safety circuit | Yellow |

---

# One Strategic Recommendation

Your site has the potential to become a **unique reference resource** for:

**Control Engineers + Machine Builders**

There is currently **no well-structured public site** that clearly explains the relationships between:

- NEC
- NFPA 79
- UL 508A
- ISO 13849
- IEC 60204

If you structure this properly, your site could become a **go-to reference for automation engineers**.

---

If you want, I can also show you the **ideal architecture for your entire Control-System-Tools site** (the current structure is good but can be optimized into a professional standards reference system).
