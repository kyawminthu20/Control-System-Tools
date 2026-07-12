# Review: Control System Tools — Standards

The standards section is **well structured and substantially better than a typical standards list**. The scenario-based navigation, lifecycle approach, industry overlays, crosswalks, and trust-boundary notices are strong.

However, I found several technical and publishing issues that should be corrected before treating it as a reliable engineering reference.

## High-priority corrections

### 1. Correct the IEC 60204-1 edition

The site lists:

> IEC 60204-1 — 2018

The current IEC publication should be identified as:

> **IEC 60204-1:2016 + AMD1:2021**

A regional adoption might have another publication year, but the international IEC edition is not properly described as simply “2018.” ([Kyaw Min Thu][1])

Recommended display:

| Standard    | Current reference                     |
| ----------- | ------------------------------------- |
| IEC 60204-1 | IEC 60204-1:2016+A1:2021, Edition 6.1 |

Also distinguish:

* IEC international edition
* EN IEC European adoption
* National adoption, such as BS EN or DIN EN

---

### 2. Do not say ISO 12100 is legally required for CE marking

The site currently says:

> “CE marking requires an ISO 12100 risk assessment as the foundation.”

That is too absolute.

The legal requirement is compliance with the applicable **essential health and safety requirements** and completion of the relevant conformity-assessment process. Harmonized standards such as EN ISO 12100 are generally voluntary, though their use can provide presumption of conformity for requirements they cover. ([Kyaw Min Thu][2])

Replace it with:

> For machinery placed on the EU market, the manufacturer must perform and document a risk assessment and satisfy the applicable essential health and safety requirements. EN ISO 12100 is the commonly used harmonized methodology for risk assessment and risk reduction, but use of the standard is generally voluntary.

This distinction matters legally.

---

### 3. Add the Machinery Regulation transition date

The EU section should clearly distinguish:

* **Machinery Directive 2006/42/EC** — applicable until January 19, 2027
* **Machinery Regulation (EU) 2023/1230** — generally applicable beginning January 20, 2027

The Regulation replaces the Directive on that date. ([EUR-Lex][3])

A visible transition notice is needed:

> **EU transition notice:** Projects placed on the market before January 20, 2027 generally follow Directive 2006/42/EC. Regulation (EU) 2023/1230 generally applies from January 20, 2027. Confirm the applicable transition provisions for the product and placement date.

Without this, the “Global / EU” scenario will soon become incomplete.

---

### 4. Treat ISO 13849-1 and IEC 62061 as alternative design paths

The quick-decision section says:

> Safety functions (PL)? → ISO 13849-1 + IEC 62061

That suggests both standards must be applied together. Usually, the engineer selects an appropriate functional-safety design path:

* **ISO 13849-1** → Performance Level, Category, MTTFd, DCavg, CCF
* **IEC 62061** → SIL / SILCL machinery safety lifecycle

They can coexist in a project, but they should not appear as a mandatory pair.

Recommended wording:

> Machinery safety-related control function → Select ISO 13849-1 **or** IEC 62061 based on the project architecture, required metric, customer specification, and organizational lifecycle.

The site already explains the distinction better in some scenarios, so this is mainly a consistency correction. ([Kyaw Min Thu][1])

---

### 5. Do not imply the NEC edition is universally applicable

The site identifies NEC 2023 as the legal baseline. That is broadly useful, but an installation is governed by the edition adopted by the applicable jurisdiction—not necessarily the newest published edition.

Replace:

> NEC 2023 — legally enforced

With:

> NFPA 70, National Electrical Code — edition adopted by the AHJ. The repository currently references the 2023 edition.

Also add:

> Verify state, city, facility-owner and AHJ amendments before design or installation.

This is especially important for California projects, where the adopted California Electrical Code and local amendments control.

---

### 6. Clarify the relationship among NEC, UL 508A and NFPA 79

The statement:

> UL 508A + NEC Article 409 + NFPA 79

is a useful starting stack, but it needs a scope diagram.

These documents do different jobs:

| Document          | Primary role                                                   |
| ----------------- | -------------------------------------------------------------- |
| NEC / NFPA 70     | Field installation and legally adopted electrical requirements |
| NEC Article 409   | Industrial control panels                                      |
| UL 508A           | Construction and certification of industrial control panels    |
| NFPA 79           | Electrical equipment of industrial machinery                   |
| OSHA requirements | Workplace safety and employer obligations                      |
| Product standard  | Requirements for particular machine or equipment type          |

Important qualification:

> A panel does not automatically need UL listing merely because it is an industrial control panel. Listing may be required by the AHJ, customer, specification, facility policy or local rule.

Your scenario currently says “UL listing required,” which is only correct when that requirement has already been established for the particular project. ([Kyaw Min Thu][2])

Use:

> UL-listed panel required by project specification or AHJ.

---

## Content and publishing problems

### 7. Internal repository labels are leaking into the public site

Public-facing text currently contains labels such as:

* `CORPUS COMPLETE`
* `Complete`
* `Phase 5 Complete`
* `REVIEWED`
* `local corpus`
* repository directory trees

Examples appear directly in the homepage, standards explorer and standards finder. ([Kyaw Min Thu][2])

These labels make the website look like an internal RAG validation dashboard rather than a finished engineering field guide.

Replace them with controlled publication states:

| Internal state | Public label                  |
| -------------- | ----------------------------- |
| Complete       | Published                     |
| Reviewed       | Technically reviewed          |
| To verify      | Review pending                |
| Not in corpus  | Not yet covered               |
| Draft          | Draft — do not use for design |

Keep corpus paths on a developer/contributor page, not the main engineering pages.

---

### 8. Branding and navigation are inconsistent between pages

The homepage uses:

> Control System Standards Atlas

Some internal pages use:

> Control Systems Engineering Field Guide

The homepage navigation omits Communications, while the Standards Finder and Functional Safety pages include Communications and expanded design/manufacturer sections. ([Kyaw Min Thu][2])

This suggests different site builds, templates or navigation configurations were deployed together.

Select one product name. I recommend:

> **Control Systems Engineering Field Guide**

Then use a subtitle:

> Standards, design, commissioning, communications and troubleshooting reference

Also rebuild every page with the same navigation configuration.

---

### 9. The standards relationship arrows need definitions

The relationship graph shows arrows such as:

* IEC 60204-1 → NFPA 79
* UL 508A → NFPA 79
* IEC 62443 → IEC 61508
* IEC 61131-3 → IEC 62061

An arrow can mean many things:

* normative reference
* conceptual dependency
* overlapping scope
* alternative standard
* regional counterpart
* implementation support
* industry overlay

At present, the graph can be misinterpreted as a formal normative hierarchy. ([Kyaw Min Thu][1])

Use typed and labeled relationships:

```text
ISO 12100
  └── risk-assessment foundation ──> ISO 13849-1 / IEC 62061

NFPA 79
  └── installation interface ──> NFPA 70

UL 508A
  └── panel construction overlaps ──> NFPA 79

IEC 62443
  └── cybersecurity overlay ──> control and safety systems
```

Add a legend:

* Solid line: normative or direct application relationship
* Dashed line: conceptual relationship
* Double arrow: regional comparison
* Overlay: additional requirement family

---

### 10. “Complete” is not meaningful enough

A standard may contain hundreds of requirements. Saying it is “Complete” does not tell the reader whether the page contains:

* full clause-by-clause coverage
* only a summary
* application guidance
* worked examples
* verified references
* amendment coverage
* national deviations

Use a coverage table:

| Field                 | Example                        |
| --------------------- | ------------------------------ |
| Edition tracked       | ISO 13849-1:2023               |
| Coverage              | Engineering overview           |
| Clause mapping        | Partial                        |
| Technical review      | Pending                        |
| Last verified         | July 2026                      |
| Official source       | ISO catalogue                  |
| Amendments/corrigenda | Checked / not checked          |
| Intended use          | Education and project planning |

---

## Standards families still missing

For a comprehensive control-system engineering site, the existing list is only the foundation. Add these families next.

### Machine and robotic systems

* ISO 10218-1 and ISO 10218-2 — industrial robots and robot applications
* ISO/TS 15066 — collaborative robot applications
* ANSI/RIA R15.06 — US industrial robot safety
* ANSI B11 series — machinery safety
* IEC 61800-5-2 — functional safety of adjustable-speed drives
* IEC 61800-3 — drive EMC
* IEC 61310 series — indication, marking and actuation
* ISO 14119 — interlocking devices
* ISO 14120 — guards
* ISO 13850 — emergency-stop function
* ISO 13855 — positioning safeguards
* ISO 13857 — safety distances
* IEC 61496 — electro-sensitive protective equipment

### Industrial control panels and electrical equipment

* UL 698A — panels relating to hazardous locations
* UL 1203 — explosion-proof equipment
* UL 943 — GFCIs
* UL 489 and UL 1077 — branch protection versus supplementary protectors
* UL 1008 — transfer switches
* UL 508 / applicable component standards
* CSA C22.2 No. 286 — industrial control panels and assemblies
* CSA C22.1 — Canadian Electrical Code
* NFPA 70E — electrical workplace safety
* IEEE 1584 — arc-flash calculations

### Functional safety

* IEC 61508 Parts 1–7
* IEC 61511 Parts 1–3
* ISA 84 / ANSI/ISA-61511
* IEC 61800-5-2
* IEC 61513 — nuclear I&C safety systems
* ISO 26262 — road vehicles
* IEC 61508 sector-specific standards map

### Industrial cybersecurity

IEC 62443 should be separated by document:

* IEC 62443-2-1 — asset-owner security program
* IEC 62443-2-4 — service providers
* IEC 62443-3-2 — system security risk assessment
* IEC 62443-3-3 — system security requirements and security levels
* IEC 62443-4-1 — secure product development lifecycle
* IEC 62443-4-2 — component technical requirements

Also include:

* NIST SP 800-82
* NIST Cybersecurity Framework
* CISA Cross-Sector Cybersecurity Performance Goals
* ISA/IEC 62443 zones and conduits
* secure remote access
* backup and restore
* patch and vulnerability management

The current “IEC 62443 — Phase 5 Complete” wording should be removed because “Phase 5” is an internal project status, not a useful standards classification. ([Kyaw Min Thu][1])

### Alarm management and process control

* ISA-18.2 / IEC 62682 — alarm management
* ISA-5.1 — instrumentation symbols and identification
* ISA-5.4 — instrument loop diagrams
* ISA-20 — specification forms
* ISA-88 — batch control
* ISA-95 / IEC 62264 — enterprise-control integration
* IEC 61131-3 — PLC programming languages
* IEC 61131-6 — functional safety
* IEC 61499 — distributed automation
* IEC 62541 — OPC UA

### Communications and networks

* IEEE 802.3 — Ethernet
* IEEE 802.1Q — VLANs
* IEEE 1588 — Precision Time Protocol
* IEC 61784 — industrial communication profiles
* IEC 61158 — industrial communication networks
* ODVA EtherNet/IP specifications
* PI PROFINET and PROFIBUS specifications
* Modbus Application Protocol
* EtherCAT Technology Group specifications
* IO-Link / IEC 61131-9
* BACnet / ASHRAE 135
* IEC 61850 — utility automation
* DNP3 / IEEE 1815

### Semiconductor

The semiconductor page should include more than SEMI S2/S8/S14:

* SEMI S10 — risk assessment
* SEMI S22 — electrical design
* SEMI S6 — exhaust ventilation
* SEMI S18 — environmental considerations
* SEMI S23 — energy conservation
* SEMI S26 — emergency power-off
* SEMI F47 — voltage sag immunity
* SEMI E10 — equipment reliability
* SEMI E30 / GEM
* SEMI E37 / HSMS
* SEMI E84 — carrier handoff
* SEMI E87 / E90 / E94 — carrier and substrate tracking/control
* NFPA 318 — semiconductor fabrication facilities

---

## Recommended page architecture

Each standard page should use the same format:

```text
1. Purpose
2. Applicability
3. When it does not apply
4. Current edition and amendment status
5. Legal or contractual status
6. Primary users
7. Inputs required
8. Required engineering outputs
9. Key design requirements
10. Verification and validation requirements
11. Documentation and records
12. Related standards
13. Regional differences
14. Worked example
15. Common mistakes
16. Official publisher reference
17. Review status and last verification date
```

### Example routing record

```yaml
standard: ISO 13849-1
edition: "2023"
family: functional-safety
application:
  equipment: machinery
  function: safety-related-control-system
metric: performance-level
legal_status:
  eu: voluntary-harmonized-standard-when-cited
  us: consensus-standard-or-contractual
inputs:
  - risk assessment
  - required performance level
  - architecture
  - component reliability data
outputs:
  - safety function specification
  - category
  - MTTFd
  - DCavg
  - CCF assessment
  - achieved PL
  - validation record
review:
  state: technical-review-pending
  last_checked: 2026-07-11
```

## Overall assessment

| Area                        | Assessment                             |
| --------------------------- | -------------------------------------- |
| Information architecture    | Strong                                 |
| Scenario navigation         | Strong                                 |
| Standards selection concept | Strong                                 |
| Technical accuracy          | Needs targeted corrections             |
| Edition control             | Needs improvement                      |
| EU legal wording            | Needs correction                       |
| Publication consistency     | Needs improvement                      |
| Coverage breadth            | Good foundation, not yet comprehensive |
| Professional usefulness     | High potential                         |
| Safety/compliance readiness | Educational reference only             |

The biggest immediate fixes are:

1. Change IEC 60204-1 to **2016+A1:2021**.
2. Correct the statement that ISO 12100 is legally required for CE marking.
3. Add the 2027 EU Machinery Regulation transition.
4. Change ISO 13849-1 and IEC 62061 from a mandatory pair to alternative paths.
5. State that the NEC edition depends on AHJ adoption.
6. Remove internal corpus/status terminology.
7. unify site branding and navigation.
8. Label every relationship shown in the standards graph.

[1]: https://kyawminthu20.github.io/Control-System-Tools/standards/ "Standards Explorer — Control System Standards Atlas"
[2]: https://kyawminthu20.github.io/Control-System-Tools/ "Home — Control System Standards Atlas"
[3]: https://eur-lex.europa.eu/EN/legal-content/summary/machinery-safety-requirements.html?utm_source=chatgpt.com "Machinery safety requirements | EUR-Lex - European Union"


# Detailed Standards Audit

I checked the individual standards pages, scenarios, standards finder, relationship graph, and methodology pages—not only the homepage.

## Overall result

The site has a strong structure, but several pages currently contain **safety-significant technical errors**. I would not label the standards section “technically reviewed” until the first five issues below are corrected.

## 1. ISO 12100 is incorrectly used as the PLr risk graph source

### Current problem

The ISO 12100 and ISO 13849-1 pages attribute the following risk parameters to **ISO 12100 Annex A**:

* S1 / S2 — severity
* F1 / F2 — frequency or exposure
* P1 / P2 — possibility of avoidance
* Resulting PLr

That is incorrect.

### Correct relationship

* **ISO 12100** provides the overall machinery risk-assessment and three-step risk-reduction methodology.
* **ISO 13849-1 Annex A** contains the S/F/P risk graph used to estimate the required Performance Level, PLr.
* **IEC 62061 Annex A** has its own method for determining the required SIL.

ISO 12100 does not directly “give PLr.” Your site currently presents these as one process, which could lead engineers to cite the wrong normative source. ([Kyaw Min Thu][1])

### Replace with

> Perform the machinery risk assessment and risk reduction process using ISO 12100. For safety-related control functions designed under ISO 13849-1, estimate PLr using the risk graph in ISO 13849-1 Annex A. When using IEC 62061, determine the required SIL using the method provided by IEC 62061.

This correction must be made on:

* ISO 12100 page
* ISO 13849-1 page
* IEC 62061 page
* Functional Safety family page
* Global machine scenario
* Standards Finder

---

## 2. The IEC 62061 page is based partly on obsolete terminology

### Current problem

The page identifies the standard as:

> IEC 62061:2021

It also heavily uses:

* SILCL
* SRECS terminology
* older subsystem tables
* older technology boundaries

As of July 2026, the current consolidated reference is:

> **IEC 62061:2021 + AMD1:2024 + AMD2:2026**

The 2021 edition also changed important concepts, including replacing the former subsystem **SILCL** concept with the subsystem’s **maximum SIL** and expanding applicability beyond strictly electrical, electronic and programmable electronic technologies. ([Kyaw Min Thu][2])

### Additional IEC 62061 problems

The page currently says IEC 62061 is required when:

> SIL greater than 2 is not achievable with ISO 13849-1.

That is wrong. ISO 13849-1 and IEC 62061 are alternative machinery functional-safety design routes. Selection is based on project requirements, architecture, customer requirements and organizational methodology—not a rule that IEC 62061 begins above PL d or SIL 2. ([Kyaw Min Thu][3])

The worked example calculates:

> PFHd = 8.5 × 10⁻⁸ per hour

That value falls within the numerical **SIL 3 PFHd band**, although the final claim can still be limited by the maximum SIL of the subsystems, architecture and systematic requirements. Calling it simply “meets SIL 2 because it is below 10⁻⁶” omits the lower band boundary and hides the actual limitation.

### Required action

The IEC 62061 page should be revalidated from the current consolidated edition rather than patched line by line.

Use:

```text
Edition tracked:
IEC 62061:2021+A1:2024+A2:2026

Coverage status:
Revalidation required against current consolidated edition
```

---

## 3. The IEC 60204-1 page has several direct errors

### Edition

The site lists:

> IEC 60204-1 — 2018

The current IEC consolidated reference is:

> **IEC 60204-1:2016 + AMD1:2021**

A European or national adoption may have a different publication year, but the website identifies the document as the international IEC standard, so “2018” is not the correct edition label. ([Kyaw Min Thu][4])

### Incorrect lower-voltage threshold

The page says the standard applies to machinery circuits:

> above 25 VAC or 60 VDC

That is not how the official IEC scope is defined. The standard covers electrical equipment of machines beginning at the point of connection to the supply, with an upper limit of **1,000 VAC or 1,500 VDC**. The stated 25 VAC/60 VDC lower threshold should be removed unless it is tied to a specific clause and carefully explained. ([Kyaw Min Thu][4])

### Clause structure is internally wrong

The page says:

> All 15 clauses

But its table:

* starts at Clause 4
* ends at Clause 17
* duplicates technical documentation
* omits Clause 18 verification

At minimum, correct these entries:

| Clause | Subject                                           |
| -----: | ------------------------------------------------- |
|     16 | Marking, warning signs and reference designations |
|     17 | Technical documentation                           |
|     18 | Verification                                      |

Do not describe the page as “complete” while Clause 18 is absent.

### Emergency-stop category error

The page lists emergency stop as potentially using:

* Category 0
* Category 1
* Category 2

General machine stopping functions can be categorized as 0, 1 or 2, but an **emergency-stop function uses Category 0 or Category 1**, selected through the risk assessment. Category 2 is not an emergency-stop category. ([Kyaw Min Thu][4])

### Correct wording

> Stop functions may be Category 0, 1 or 2. An emergency-stop function shall operate as either a Category 0 or Category 1 stop, as determined by the machine risk assessment.

---

## 4. The CE-marking language is legally too absolute

The homepage and Global/EU scenario currently state:

> CE marking requires an ISO 12100 risk assessment.

That wording confuses the legal requirement with the voluntary standards route.

### Correct distinction

EU machinery law requires the manufacturer to:

* perform and document a risk assessment
* identify applicable essential health and safety requirements
* implement suitable risk reduction
* complete the appropriate conformity-assessment process

Use of a harmonized standard such as **EN ISO 12100** is generally voluntary. When properly applied and cited, it may provide presumption of conformity for requirements within its scope. ([Kyaw Min Thu][5])

### Replacement wording

> EU machinery legislation requires a documented risk assessment and compliance with the applicable essential health and safety requirements. EN ISO 12100 is the principal harmonized methodology commonly used to perform and document machinery risk assessment and risk reduction. Its use is generally voluntary but may provide presumption of conformity for the requirements it covers.

### Missing transition notice

The site should also show the exact EU transition:

* Machinery Directive 2006/42/EC continues to apply through **January 19, 2027**.
* Machinery Regulation (EU) 2023/1230 generally applies beginning **January 20, 2027**. ([EUR-Lex][6])

---

## 5. The IEC 62443 page contains outdated editions and unsafe default assumptions

### Outdated editions

The page lists:

| Part          | Website edition |            Update needed |
| ------------- | --------------: | -----------------------: |
| IEC 62443-2-1 |            2010 |                 **2024** |
| IEC 62443-2-4 |            2015 |                 **2023** |
| IEC 62443-3-2 |            2020 |     Current base edition |
| IEC 62443-3-3 |            2013 |     Current base edition |
| IEC 62443-4-1 |            2018 |     Current base edition |
| IEC 62443-4-2 |            2019 | Include COR1:2022 status |

([Kyaw Min Thu][7])

### Zones and conduits are assigned to the wrong part

The site associates the zone-and-conduit risk process mainly with IEC 62443-3-3.

More accurately:

* **IEC 62443-3-2** covers security risk assessment for system design, including partitioning the system under consideration into zones and conduits and establishing target security levels.
* **IEC 62443-3-3** defines system security requirements and security levels. ([IEC Webstore][8])

### Remove default security-level prescriptions

The page currently recommends concepts such as:

* most zones should be SL 2
* safety-critical zones should be SL 3
* enterprise zone SL 1
* control zone SL 2

These can be shown only as an explicitly hypothetical example. IEC 62443 requires the target security level to be derived from the system risk assessment. There is no universal rule that a control zone is SL 2 or a safety zone is SL 3.

Replace with:

> The target security level, SL-T, shall be derived from the documented cybersecurity risk assessment. The examples shown here are illustrative and must not be treated as default security-level assignments.

### Correct SIL statement

The page says IEC 62061 and IEC 61511 use SIL 1–4. That is not correct as a combined statement:

* IEC 62061 machinery applications use SIL 1 through SIL 3.
* IEC 61508 defines SIL 1 through SIL 4.
* IEC 61511 process-sector safety instrumented systems generally operate within SIL 1 through SIL 3.

---

## 6. ISO 13849-1 content needs qualification

The edition:

> ISO 13849-1:2023

is correct. ([Kyaw Min Thu][9])

However, several statements are too deterministic.

### Current claim

> Category 3 + high MTTFd + medium DC achieves PL d.

Better:

> A Category 3 architecture with suitable MTTFd, DCavg, CCF measures and systematic controls can achieve PL d, subject to complete calculation and validation.

Achieved PL depends on more than Category, MTTFd and diagnostic coverage.

### Incorrect PL e numerical band

The page shows PL e as:

> less than 10⁻⁷ per hour

Include the lower bound:

> **10⁻⁸ ≤ PFHd < 10⁻⁷ per hour**

### SISTEMA is not mandatory

The site appears to require a SISTEMA report for every ISO 13849 design. SISTEMA is a useful calculation tool, but use of that particular software is not mandatory. The required output is a documented and validated calculation—not necessarily a SISTEMA file.

Similarly, do not state that every design requires component-level FMEA and fault-injection testing in exactly that form. Validation methods must be appropriate to the design and safety requirements.

---

## 7. NEC edition handling needs two separate fields

The NEC page says:

> Latest edition: 2023

The **2026 NFPA 70 National Electrical Code** has been published. However, the enforceable edition remains the edition adopted by the applicable state, city or AHJ. ([Kyaw Min Thu][10])

Use separate metadata:

```text
Edition covered by this page: NFPA 70, 2023 Edition
Latest published edition: NFPA 70, 2026 Edition
Legally applicable edition: Verify adoption with the AHJ
```

Your NEC page already contains a useful adoption caveat. Keep that warning.

The page’s descriptions of several 2026 changes appear broadly aligned with NFPA’s published change summaries; the main error is calling 2023 the latest published edition.

---

## 8. UL 508A edition metadata is outdated

The site identifies:

> UL 508A — 2022

The better current reference is:

> **UL 508A, Edition 3, originally published April 24, 2018, revised through June 26, 2025**

UL standards are often best identified by edition plus revision date rather than treating each revision year as a new edition. ([Kyaw Min Thu][11])

Also revise this implication:

> Industrial control panel = UL listing required.

A UL-listed panel may be required by:

* the AHJ
* customer specifications
* facility standards
* insurance conditions
* contract requirements

It is not accurate to imply that every industrial control panel must universally be UL listed.

---

## 9. NFPA 79 and UL 508A do not merely “interlock”

The NFPA 79 page says the two standards:

> interlock rather than overlap

That is too categorical.

A better explanation is:

* UL 508A primarily addresses industrial control-panel construction.
* NFPA 79 addresses the electrical equipment of industrial machinery.
* Their scopes are complementary and may overlap around machine control panels.
* Compliance with UL 508A alone does not necessarily address every NFPA 79 machinery requirement. UL itself notes that additional NFPA 79 requirements may apply. ([Kyaw Min Thu][12])

---

## 10. Publishing and consistency problems

### Mixed branding

Most pages use:

> Control Systems Engineering Field Guide

The NEC page still uses:

> Control System Standards Atlas

It also has an older, reduced navigation menu. This indicates that old generated pages or templates remain in the deployed build. ([Kyaw Min Thu][5])

### Internal repository language appears publicly

Public pages contain terms such as:

* Phase 5 Complete
* CORPUS COMPLETE
* local corpus
* repository paths
* RAG corpus
* TO VERIFY

The methodology page clearly explains that the site is AI-assisted and educational, which is good. But internal workflow states should be converted into public review statuses. ([Kyaw Min Thu][13])

Use only:

* Draft
* Technical review pending
* Technically reviewed
* Edition revalidation required
* Published
* Superseded

### Review-date contradiction

The IEC 62061 page was marked reviewed in April 2026 but does not account for the 2024 and 2026 amendments. A page should not retain “reviewed” status after a newer amendment or edition is released unless the review explicitly covers it.

---

## Correction to my earlier graph comment

The **interactive relationship graph does include edge categories and hover labels**, so my earlier statement that the entire graph lacked definitions was too broad.

The remaining issue is the simplified static relationship diagram in the Standards Explorer. That version displays arrows without enough context and can still be mistaken for a formal normative hierarchy. ([Kyaw Min Thu][14])

## Recommended correction order

| Priority | Work                                                                               |
| -------: | ---------------------------------------------------------------------------------- |
|        1 | Correct ISO 12100 versus ISO 13849-1/IEC 62061 risk-assessment routing             |
|        2 | Rebuild IEC 62061 content against 2021+A1:2024+A2:2026                             |
|        3 | Correct IEC 60204-1 edition, scope, clause structure and emergency-stop categories |
|        4 | Rewrite CE-marking legal language and add the January 20, 2027 transition          |
|        5 | Update IEC 62443 editions, zones/conduits ownership and SL-T guidance              |
|        6 | Qualify ISO 13849 calculations and validation claims                               |
|        7 | Correct NEC and UL 508A edition metadata                                           |
|        8 | Clean branding, page templates, statuses and repository language                   |

The strongest parts of the site remain its scenario navigation, standards finder, trust-boundary notices and lifecycle organization. The immediate weakness is not the overall design—it is that several pages mix current standards with older terminology and oversimplified engineering rules.

[1]: https://kyawminthu20.github.io/Control-System-Tools/standards/functional-safety/iso-12100/ "ISO 12100 — Risk Assessment and Risk Reduction — Control Systems Engineering Field Guide"
[2]: https://kyawminthu20.github.io/Control-System-Tools/standards/functional-safety/iec-62061/ "IEC 62061 — Functional Safety, Machinery SIL — Control Systems Engineering Field Guide"
[3]: https://kyawminthu20.github.io/Control-System-Tools/standards/functional-safety/ "Functional Safety Standards — Control Systems Engineering Field Guide"
[4]: https://kyawminthu20.github.io/Control-System-Tools/standards/machinery/iec-60204-1/ "IEC 60204-1 — Electrical Equipment of Machines — Control Systems Engineering Field Guide"
[5]: https://kyawminthu20.github.io/Control-System-Tools/ "Home — Control Systems Engineering Field Guide"
[6]: https://eur-lex.europa.eu/EN/legal-content/summary/machinery-safety-requirements.html?utm_source=chatgpt.com "Machinery safety requirements | EUR-Lex - European Union"
[7]: https://kyawminthu20.github.io/Control-System-Tools/standards/cybersecurity/iec-62443/ "IEC 62443 — Industrial Cybersecurity — Control Systems Engineering Field Guide"
[8]: https://webstore.iec.ch/en/publication/30727?utm_source=chatgpt.com "IEC 62443-3-2:2020"
[9]: https://kyawminthu20.github.io/Control-System-Tools/standards/functional-safety/iso-13849-1/ "ISO 13849-1 — Safety of Machinery, Control Systems (PL) — Control Systems Engineering Field Guide"
[10]: https://kyawminthu20.github.io/Control-System-Tools/standards/us-electrical/nec/ "NEC (NFPA 70) — National Electrical Code — Control Systems Engineering Field Guide"
[11]: https://kyawminthu20.github.io/Control-System-Tools/standards/us-electrical/ul-508a/ "UL 508A — Industrial Control Panels — Control Systems Engineering Field Guide"
[12]: https://kyawminthu20.github.io/Control-System-Tools/standards/us-electrical/nfpa-79/ "NFPA 79 — Electrical Standard for Industrial Machinery — Control Systems Engineering Field Guide"
[13]: https://kyawminthu20.github.io/Control-System-Tools/about/ "About & Methodology — Control Systems Engineering Field Guide"
[14]: https://kyawminthu20.github.io/Control-System-Tools/standards/graph/ "Standards Relationship Graph — Control Systems Engineering Field Guide"


Yes. The site should not be only a **standards summary**. Each standard needs to answer three separate questions:

1. **What does this mean in simple language?**
2. **What does the standard require in engineering detail?**
3. **How do I use it to design an actual machine, panel, network, or safety system?**

At present, the pages are inconsistent. The IEC 60204-1 page is mainly an overview, clause table, and a few notes, while the ISO 13849-1 page contains significantly more technical and design content but places quick explanations, calculations, architecture guidance, and examples into one long page. ([Kyaw Min Thu][1])

# Recommended three-level page structure

Every standard page should use the same navigation:

```text
Overview | Simple Explanation | Engineering Detail | Design Guide
Worked Example | Verification | Templates | Sources
```

A user should be able to select:

* **Learn** — beginner-friendly explanation
* **Understand** — detailed engineering content
* **Design** — practical workflow
* **Verify** — test and document the design

## Level 1 — Simplified explanation

This should be understandable by a technician, junior engineer, project manager, or customer.

Keep it to approximately one screen.

### Required content

```text
What is this standard?
Why does it exist?
When does it apply?
What equipment does it cover?
What problem does it prevent?
What are the five most important requirements?
Which other standards are normally used with it?
```

### Example: IEC 60204-1

> IEC 60204-1 provides electrical design requirements for machinery. It begins at the machine’s electrical supply connection and covers items such as disconnecting means, protection, control circuits, wiring, motors, operator controls, identification, documentation, and verification.

### Simple visual

```text
Building Supply
      │
      ▼
Machine Disconnect
      │
      ▼
Branch Protection
      │
      ├──► Motor Starter / VFD ──► Motor
      │
      ├──► Control Power Supply ──► PLC / I/O
      │
      └──► Safety System ─────────► STO / Contactors
```

### Simple design summary

```text
1. Determine the machine supply.
2. Select the main disconnect.
3. calculate fault-current and protection requirements.
4. Design the protective bonding system.
5. Design power and control circuits.
6. Select wire sizes and identification.
7. Design stop and emergency-stop functions.
8. Produce drawings and documentation.
9. Inspect and test the completed machine.
```

The simplified section should deliberately avoid dense clause references and calculations.

---

# Level 2 — Detailed engineering explanation

This is where the standard is explained accurately and systematically.

## Required metadata

Every page should start with:

| Field                    | Content                                                      |
| ------------------------ | ------------------------------------------------------------ |
| Standard                 | Official designation                                         |
| Edition covered          | Edition and amendments                                       |
| Latest published edition | Current publisher status                                     |
| Region                   | US, EU, international or industry-specific                   |
| Applicable equipment     | Machine, panel, SIS, network, etc.                           |
| Exclusions               | Equipment outside its scope                                  |
| Legal status             | Code, regulation, consensus standard or contractual standard |
| Technical review         | Reviewed, pending or revalidation required                   |
| Last verified            | Exact date                                                   |
| Official source          | Publisher catalogue                                          |
| Related standards        | Connected standards                                          |

The site currently provides some of this information, but edition, coverage, and internal corpus fields are mixed together. For example, the IEC 60204-1 page displays edition, coverage, repository status, and technical validation, but still contains internal repository terminology and inconsistent edition information. ([Kyaw Min Thu][1])

## Detailed section structure

### 1. Scope

Explain:

* Where the standard begins and ends
* Equipment covered
* Equipment excluded
* Voltage or system limitations
* Regional adoption
* Product-specific standards that may take precedence

### 2. Definitions

Provide plain-language and engineering definitions.

Example:

| Term                | Simple meaning                                      | Engineering meaning                                                                                    |
| ------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Protective bonding  | Connecting metal parts to ground                    | Low-impedance fault-current path connecting exposed conductive parts to the protective bonding circuit |
| Safety function     | An action that keeps a hazard controlled            | A control-system function whose failure could increase risk                                            |
| PLr                 | Required reliability of a machinery safety function | Required Performance Level determined using the selected risk-estimation method                        |
| Diagnostic coverage | How well faults are detected                        | Ratio of detected dangerous failures to total dangerous failures                                       |

### 3. Clause-by-clause explanation

Do not merely show a clause title.

Use this format:

| Clause/topic      | What it controls                   | Design implication                                      | Required evidence                     |
| ----------------- | ---------------------------------- | ------------------------------------------------------- | ------------------------------------- |
| Supply disconnect | Isolation of machine power         | Select type, location, rating and lockability           | Schematic, datasheet, inspection      |
| Protection        | Overcurrent and fault protection   | Calculate circuit protection and conductor coordination | Calculations and device schedule      |
| Control circuits  | Reliable command and stop behavior | Define voltage, grounding and fault response            | Control schematic and functional test |
| Documentation     | Information delivered with machine | Prepare complete drawing and manual package             | Document register                     |

### 4. Key technical principles

Explain the engineering reasoning:

* Why the requirement exists
* What hazard it controls
* What design decisions it affects
* What commonly goes wrong
* How it interacts with other standards

### 5. Cross-standard relationships

For example:

```text
ISO 12100
Risk assessment and risk reduction
        │
        ▼
ISO 13849-1 or IEC 62061
Safety-related control-system design
        │
        ▼
IEC 60204-1
Electrical implementation of the machine
        │
        ▼
Verification, validation and technical documentation
```

The current standards explorer already provides standards-family and lifecycle routing, but the individual pages should carry the same relationships directly into design decisions. ([Kyaw Min Thu][2])

---

# Level 3 — How to design

This is the most important missing layer.

A design guide must convert the standard into:

```text
Inputs → Decisions → Calculations → Drawings → Build → Test → Records
```

It should not just say, “Follow IEC 60204-1” or “Use ISO 13849-1.”

## Standard design workflow

Every design guide should contain these stages.

### Stage 1 — Define design inputs

Include a downloadable input form.

Typical inputs:

* Destination market and installation location
* Applicable code edition
* Equipment type
* Supply voltage, frequency and phase
* Available fault current
* Connected load
* Environmental conditions
* Hazardous-location classification
* Machine operating modes
* Hazard and risk assessment
* Safety-function requirements
* Customer specifications
* Listing or certification requirements
* Network and cybersecurity requirements

### Stage 2 — Determine applicable standards

Use a decision tree:

```text
Is it machinery?
 ├─ No → Check process, building, utility or product standards
 └─ Yes
     │
     ├─ US installation?
     │    └─ NEC + NFPA 79 + applicable panel/product standards
     │
     ├─ EU market?
     │    └─ EU machinery legislation + EN ISO 12100
     │       + EN IEC 60204-1 + safety standard
     │
     ├─ Safety-related control function?
     │    └─ ISO 13849-1 or IEC 62061
     │
     └─ Networked control system?
          └─ IEC 62443 risk assessment and security requirements
```

### Stage 3 — Create a requirements matrix

Each project should have a traceability table:

| ID       | Requirement source                | Design requirement                 | Drawing/document  | Verification      |
| -------- | --------------------------------- | ---------------------------------- | ----------------- | ----------------- |
| ELEC-001 | Applicable machinery standard     | Provide lockable supply disconnect | E-001             | Visual inspection |
| ELEC-002 | Circuit-protection requirement    | Protect motor branch circuit       | E-004             | Design review     |
| SAFE-001 | Safety requirements specification | E-stop shall stop hazardous motion | E-010, SW-003     | Functional test   |
| DOC-001  | Documentation requirement         | Provide final electrical drawings  | Document register | Document review   |

This is what makes the website useful for real engineering.

### Stage 4 — Develop the architecture

Show architecture options, not only text.

Example machine control architecture:

```text
Incoming Supply
      │
      ▼
Main Disconnect
      │
      ├──────────────► Auxiliary Transformer
      │                        │
      │                        ▼
      │                    24 VDC PSU
      │                        │
      │          ┌─────────────┴─────────────┐
      │          ▼                           ▼
      │       Standard PLC                Safety PLC
      │          │                           │
      │          ▼                           ▼
      │       Remote I/O              E-stop / Guards
      │                                      │
      ▼                                      ▼
Branch Protection ──► VFD / Servo ───────► STO
      │
      ▼
Motor / Actuator
```

### Stage 5 — Perform calculations

The calculation section depends on the standard.

For electrical-design standards:

* Load calculations
* Full-load current
* Conductor sizing
* Voltage drop
* Short-circuit current
* Interrupting ratings
* SCCR
* Protective-device coordination
* Control-transformer sizing
* Power-supply sizing
* Enclosure heat load
* Grounding and bonding

For functional safety:

* Required PL or SIL
* Architecture or Category
* MTTFd
* DCavg
* CCF
* PFHd
* Mission time
* Response time
* Stopping time
* Safety distance
* Proof-test interval, where applicable

For communications:

* Node count
* Update time
* Requested packet interval
* Network loading
* Multicast traffic
* VLAN and subnet allocation
* Redundancy
* Time synchronization
* Diagnostic coverage
* Cybersecurity-zone assignment

### Stage 6 — Select components

Provide a component-selection checklist:

| Component       | Required design data                                        |
| --------------- | ----------------------------------------------------------- |
| Disconnect      | Voltage, current, utilization category, enclosure rating    |
| Circuit breaker | Voltage, current, interrupting rating, trip characteristics |
| Contactor       | Utilization category, load current, coil voltage, lifecycle |
| Safety relay    | Safety rating, architecture, diagnostics, response time     |
| PLC             | I/O, communications, environment, memory, certifications    |
| VFD             | Motor rating, overload, braking, STO, SCCR, harmonics       |
| Power supply    | Input range, output capacity, reserve, fault response       |
| Enclosure       | Environment, IP/NEMA rating, thermal calculation            |
| Terminal blocks | Current, voltage, conductor range and marking               |

Do not use a product merely because the manufacturer says it is “safety rated.” The design must verify that the device data supports the required function and architecture.

### Stage 7 — Produce required drawings

Each standard page should identify the expected drawing set.

For a machine electrical system:

```text
E-001  Cover sheet and drawing index
E-002  System architecture
E-003  Incoming power and main disconnect
E-004  Power distribution
E-005  Motor/VFD circuits
E-006  24 VDC control-power distribution
E-007  PLC and remote-I/O wiring
E-008  Field-device wiring
E-009  Network architecture
E-010  Safety circuit
E-011  Grounding and bonding
E-012  Panel layout
E-013  Terminal plan
E-014  Cable schedule
E-015  Bill of materials
```

### Stage 8 — Design review

Provide a review checklist divided into:

* Electrical safety
* Functional safety
* Controls
* Communications
* Cybersecurity
* Maintainability
* Documentation
* Compliance

### Stage 9 — Verification and validation

Clearly separate them:

| Activity     | Purpose                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| Verification | Confirm that the design was implemented according to its requirements                                         |
| Validation   | Confirm that the completed system actually performs the intended function under expected and fault conditions |

The website should show:

* Test method
* Acceptance criterion
* Required instrument
* Test result
* Tester
* Date
* Evidence
* Deviation or corrective action

### Stage 10 — Required project outputs

End every standard page with a deliverables list.

```text
□ Applicability assessment
□ Standards register
□ Risk assessment
□ Requirements matrix
□ Electrical calculations
□ Safety-function specification
□ Architecture drawing
□ Electrical schematic
□ Panel layout
□ Bill of materials
□ Software design description
□ Verification plan
□ FAT procedure
□ SAT procedure
□ Validation report
□ Final technical file
```

---

# Worked examples are mandatory

Every important standard should contain at least one complete worked example.

## Example types

### IEC 60204-1

> Design the electrical system for a 480 VAC conveyor machine with a PLC, two VFD motors, 24 VDC field devices, guard switches and an emergency stop.

Show:

* Inputs
* Applicable standards
* One-line diagram
* Load calculation
* Protection selection
* Power-supply sizing
* Wire schedule
* grounding and bonding
* panel layout
* E-stop implementation
* verification checklist

### ISO 13849-1

> Design a guard-door safety function for a robot cell.

Show:

```text
Hazard assessment
      ↓
Safety function definition
      ↓
Determine PLr
      ↓
Select architecture
      ↓
Select input, logic and output devices
      ↓
Calculate MTTFd, DCavg, CCF and PFHd
      ↓
Verify achieved PL
      ↓
Validate normal and fault behavior
```

### IEC 62443

> Design zones and conduits for a PLC, HMI, historian, engineering workstation and remote vendor-access connection.

Show:

* System under consideration
* Asset inventory
* Threat scenarios
* Zones
* Conduits
* Target security levels
* Firewall rules
* Account roles
* Logging
* backup and restore
* patching
* incident response
* verification

---

# Recommended website interface

## Page header

```text
ISO 13849-1 — Safety-Related Control Systems

[Simple] [Detailed] [Design] [Example] [Checklist] [Sources]
```

## Learning-level selector

Place this near the top:

```text
Explanation level:

○ Basic — explain without calculations
○ Engineering — include terminology and requirements
○ Design — include architecture, calculations and validation
```

## Content cards

Use consistent cards:

```text
┌──────────────────────────────────────────┐
│ In simple terms                          │
│ This standard tells you how reliable a  │
│ machinery safety function must be.       │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ Engineering requirement                  │
│ Determine PLr, select an architecture,   │
│ calculate reliability and validate it.   │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ Design output                            │
│ Safety requirements specification,       │
│ calculation record and validation report.│
└──────────────────────────────────────────┘
```

## Warning types

Use visibly different notices:

* **Requirement**
* **Design recommendation**
* **Example**
* **Common mistake**
* **Jurisdiction check**
* **Verification required**

This prevents recommendations from being mistaken for mandatory standard requirements.

# Recommended master template

```markdown
---
title: Standard name
edition_covered:
latest_published:
status:
last_verified:
reviewer:
---

# Standard Name

[Simple Explanation] [Engineering Detail] [Design Guide]
[Worked Example] [Verification] [Downloads] [Sources]

## 1. Sixty-Second Explanation
- What it is
- Why it matters
- When it applies
- What it produces

## 2. System Boundary
- Included equipment
- Excluded equipment
- Beginning and ending points

## 3. Applicability Decision Tree

## 4. Key Terms

## 5. Detailed Requirements
### Requirement group 1
- Purpose
- Requirement
- Design implication
- Required evidence
- Common mistake

## 6. Design Inputs

## 7. Step-by-Step Design Workflow

## 8. Architecture Options

## 9. Calculations

## 10. Component Selection

## 11. Required Drawings

## 12. Worked Example

## 13. Verification and Validation

## 14. Required Documentation

## 15. Commissioning and Maintenance

## 16. Related Standards

## 17. Downloadable Templates

## 18. Official Sources and Edition History

## 19. Review Status and Change Log
```

# Priority for the current website

Start by rebuilding these pages using this three-level model:

1. **IEC 60204-1** — machine electrical design
2. **NFPA 79** — US machinery electrical design
3. **UL 508A** — industrial control-panel design
4. **ISO 12100** — risk-assessment workflow
5. **ISO 13849-1** — PL safety-function design
6. **IEC 62061** — machinery SIL design
7. **IEC 61511** — process SIS design
8. **IEC 62443** — control-system cybersecurity design

The site already has good top-level routing through standards, design, lifecycle, communications, industries, tools, scenarios, and crosswalks. ([Kyaw Min Thu][3]) The next development step should be to connect those sections at the individual-page level:

```text
Standard requirement
        ↓
Design workflow
        ↓
Drawing or calculation
        ↓
Commissioning test
        ↓
Maintenance requirement
```

That would turn the site from a standards catalogue into a practical **control-systems engineering design field guide**.

[1]: https://kyawminthu20.github.io/Control-System-Tools/standards/machinery/iec-60204-1/ "IEC 60204-1 — Electrical Equipment of Machines — Control Systems Engineering Field Guide"
[2]: https://kyawminthu20.github.io/Control-System-Tools/standards/ "Standards Explorer — Control Systems Engineering Field Guide"
[3]: https://kyawminthu20.github.io/Control-System-Tools/ "Home — Control Systems Engineering Field Guide"



---

# Phase 45 Triage Record (2026-07-12)

Claim-by-claim disposition of this review. **Every edition claim was checked against the
official publisher before adoption** (IEC webstore, ISO catalogue/OBP, NFPA, UL Standards,
EUR-Lex). Where the publisher's free text could not settle a claim, it is marked
UNVERIFIABLE and the site carries a verify badge rather than a confident assertion.

## Adopted — confirmed against the publisher

| # | Claim | Verdict |
|---|---|---|
| 1 | PLr comes from ISO 13849-1 Annex A, not ISO 12100 | **CONFIRMED** (ISO OBP: Annex A "can be used for the determination of the PLr"; S/F/P symbols map to A.3.1–A.3.3) |
| 2 | IEC 62061 current ref is 2021+AMD1:2024+AMD2:2026 | **CONFIRMED** — AMD2:2026 is real, published 2026-03-20 (CSV Ed. 2.2) |
| 2 | SILCL replaced by subsystem "maximum SIL"; scope extended beyond E/E/PE | **CONFIRMED** (Ed. 2.0 foreword, verbatim) |
| 3 | IEC 60204-1 edition is 2016+AMD1:2021 (not "2018") | **CONFIRMED** — Ed. 6.1 CSV, 2021-09-15. No 2018 edition exists |
| 3 | The "25 V AC / 60 V DC" lower scope threshold is wrong | **CONFIRMED — the figure was fabricated.** Official Clause 1 sets only an upper limit (1 000 V AC / 1 500 V DC, ≤200 Hz). There is no lower bound |
| 3 | Clause structure wrong; Clause 18 (Verification) missing | **CONFIRMED** — 18 clauses; 16 Marking, 17 Technical documentation, 18 Verification |
| 4 | CE-marking language legally too absolute | **CONFIRMED** — Reg. (EU) 2023/1230 Art. 20(1): harmonised standards confer *presumption of conformity*; use is voluntary |
| 4 | Machinery Regulation transition | **CONFIRMED, with a trap.** 2006/42/EC end of validity **19 Jan 2027**; 2023/1230 applies **20 Jan 2027** — but the original OJ text says *14 January*; only the **corrigendum (OJ L 169, 4.7.2023)** makes it the 20th. Cite Art. 54 as corrected |
| 5 | IEC 62443-2-1 → 2024, 2-4 → 2023; others current | **CONFIRMED** (2-1:2010 withdrawn 2024-08-07; 2-4:2015 withdrawn 2023-12-15) |
| 5 | Zones/conduits + SL-T belong to 62443-3-2, not 3-3 | **CONFIRMED** (3-2 official scope: partitioning the SUC into zones and conduits; establishing SL-T) |
| 5 | No default SL assignments — SL-T must be risk-derived | **CONFIRMED.** No official IEC text prescribes defaults; SL-T is an output of ZCR 5 |
| 6 | ISO 13849-1:2023 is current | **CONFIRMED** (Ed. 4, 2023-04) |
| 6 | Category 3 claims too deterministic; SISTEMA not mandatory | **CONFIRMED** as an engineering matter — qualified on the page |
| 7 | NEC 2026 published; enforceable edition is the AHJ-adopted one | **CONFIRMED** (NFPA errata 70-26-1 against the 2026 edition; NFPA adoption map shows states on far older editions) |
| 8 | UL 508A is Ed. 3 (2018-04-24), revised through 2025-06-26 | **CONFIRMED.** Also: **"UL 508A:2022" is not a valid designation** — no 2022 edition exists |
| 8 | UL listing is not universally required | **CONFIRMED** — driven by AHJ / customer spec / insurance / contract. NEC Art. 409 mandates *marking* (incl. SCCR), not Listing |
| 9 | NFPA 79 and UL 508A scopes overlap, not "interlock" | **CONFIRMED** — UL itself: "reference to NFPA 79 may be needed for additional requirements" |
| 10 | Internal repository labels leaking to the public site | **CONFIRMED** — swept |

## REFUTED — the review was wrong; do not adopt

| # | Review's claim | What the publisher actually says |
|---|---|---|
| 5 | "IEC 61511 process-sector SIS generally operate within SIL 1 through SIL 3" | **WRONG for the current edition.** IEC 61511-1:2016 Clause 1, verbatim, defines "a maximum level of functional safety performance (**SIL 4**)" and a minimum of SIL 1. The "61511 = SIL 1–3" belief comes from **Edition 1**. The site had the same error and it has been corrected to SIL 1–4 |

## REJECTED — conflicts with governance

- **The review's proposed 6-term status vocabulary** (Draft / Technical review pending /
  Technically reviewed / Edition revalidation required / Published / Superseded) is rejected:
  it conflicts with the binding 5-term vocabulary in `governance/CONTENT_STANDARDS.md` §3.
  The *substance* of the complaint (internal labels leaking) was accepted and fixed using the
  **existing** governed vocabulary.
- **Three-level page architecture** (Simple / Engineering / Design-guide + 19-section master
  template) — not actioned here. Partially conflicts with the established Phase-30 eight-section
  template; remains a roadmap backlog item for evaluation.

## UNVERIFIABLE — corrected conservatively, but flagged on the page

| Claim | Why |
|---|---|
| Emergency stop restricted to Stop Category 0 or 1 | Body of Clause 9 is paywalled; the free IEC preview truncates inside Clause 3. The correction (removing Category 2) is the conservative reading and consistent with ISO 13850, but is **not** confirmed word-for-word. Page carries a verify badge |
| IEC 62061 machinery range = SIL 1–3 | The 2021 edition's Clause 1 scope states **no** SIL range (the 2005 edition did). Tables 3/6 are paywalled. Kept as "conventionally SIL 1–3" with a verify badge |
| ISO 13849-1 PL band numbers (incl. PL e ≥ 10⁻⁸) | Table 2 is normative body text, paywalled. The lower bound was added (the review's point stands), but the numbers are flagged for check against the purchased Table 2 |

## Found independently — not in the review

1. **NFPA 79 scope voltage was stale site-wide**: pages said 600 V; the current scope is
   **1000 V or less**. Fixed on the NFPA 79 page, the IEC 60204-1 page, and the crosswalk.
2. **The IEC 60204-1 corpus module was drafted against the superseded 2005 edition.** Evidence:
   its Clause 15 was titled "Accessories and lighting" (the Ed. 5.0 title; Ed. 6 is
   "Socket-outlets and lighting"), and it cited **9.2.5.4.2**, a subclause that does not exist in
   Ed. 6. The module had only 15 clause files, **skipped Clauses 12 (Conductors and cables) and
   13 (Wiring practices) entirely**, merged 16 and 17, and mis-numbered everything from 12 on.
   The module has been renumbered against the official contents; Clauses 12, 13 and 17 were
   created (principles only — depth pass pending).
3. **AI drafting artifacts were published in the corpus** — 22 files ended with a chatbot
   sign-off ("Would you like me to move on to Clause 15?"). All stripped.
