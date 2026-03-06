# Control System Standards Atlas — Homepage Wireframe and Page Templates

## 1. Homepage Wireframe

### Desktop Wireframe

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ LOGO / SITE NAME                              Search                     About / GitHub      │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│ Top Nav:  Standards | Lifecycle | Industries | Scenarios | Crosswalks | Software Stack     │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│ LEFT DIRECTORY              │ MAIN CONTENT                                        │ CONTEXT  │
│─────────────────────────────│─────────────────────────────────────────────────────│ PANEL    │
│ Standards                   │ [Hero]                                              │──────────│
│  ▸ US Electrical            │ Control System Standards Atlas                      │ Quick    │
│  ▸ Intl Machinery           │ Navigate standards, lifecycle stages, scenarios,    │ Links    │
│  ▸ Functional Safety        │ and industry routes for controls design.            │          │
│  ▸ Crosswalks               │ [Primary CTA] Explore Standards                     │ Related  │
│  ▸ Reference Models         │ [Secondary CTA] View Lifecycle                      │ Standards│
│  ▸ Scenario Packages        │                                                     │          │
│                             ├─────────────────────────────────────────────────────┤ Lifecycle│
│ Lifecycle                   │ [Section 1] Standards Landscape                     │ Stages   │
│  ▸ Concept                  │ Card grid: US / Machinery / Functional Safety /     │          │
│  ▸ Standards Selection      │ Crosswalks / Reference Models / Scenarios           │ Industries│
│  ▸ Risk Assessment          │                                                     │          │
│  ▸ Safety Architecture      ├─────────────────────────────────────────────────────┤          │
│  ▸ Detailed Design          │ [Section 2] Lifecycle Flow                          │          │
│  ▸ Documentation            │ Concept → Selection → Risk → Safety → Design → ... │          │
│  ▸ Build                    │                                                     │          │
│  ▸ Installation             ├─────────────────────────────────────────────────────┤          │
│  ▸ Commissioning            │ [Section 3] Standards Relationship Graph            │          │
│                             │ ISO 12100 ↔ ISO 13849 ↔ IEC 62061 ↔ IEC 61508 ...  │          │
│ Industries                  │                                                     │          │
│  ▸ Semiconductor            ├─────────────────────────────────────────────────────┤          │
│  ▸ Food & Beverage          │ [Section 4] Industry Matrix                         │          │
│  ▸ Oil & Gas                │ Table: Industry | Risk | Safety | Electrical | ... │          │
│  ▸ Marine                   │                                                     │          │
│  ▸ Medical                  ├─────────────────────────────────────────────────────┤          │
│                             │ [Section 5] Featured Scenarios                      │          │
│ Scenarios                   │ US Panel | Global Machine | Process Skid | Network │          │
│  ▸ US Panel                 │ Safety PLC | Semiconductor Tool                     │          │
│  ▸ Global Machine           │                                                     │          │
│  ▸ Process Skid             ├─────────────────────────────────────────────────────┤          │
│  ▸ Networked Safety PLC     │ [Section 6] Repository Explorer                     │          │
│  ▸ Semiconductor Tool       │ “Open us/ next”  “Open scenario/ next” etc.         │          │
│                             ├─────────────────────────────────────────────────────┤          │
│ Crosswalks                  │ [Section 7] Trust Boundary                          │          │
│  ▸ NFPA79 vs IEC60204       │ Local corpus guidance ≠ purchased standards         │          │
│  ▸ UL508A NEC NFPA79        │                                                     │          │
└─────────────────────────────┴─────────────────────────────────────────────────────┴──────────┘
```

### Tablet Wireframe

```text
┌──────────────────────────────────────────────────────────────────────┐
│ LOGO / SITE NAME                             Search / Menu           │
├──────────────────────────────────────────────────────────────────────┤
│ Top Nav (scrollable): Standards | Lifecycle | Industries | ...      │
├──────────────────────────────────────────────────────────────────────┤
│ MAIN CONTENT                                                         │
│ [Hero]                                                               │
│ [Standards Landscape]                                                │
│ [Lifecycle Flow]                                                     │
│ [Relationship Graph]                                                 │
│ [Industry Matrix]                                                    │
│ [Scenarios]                                                          │
│ [Repository Explorer]                                                │
│ [Trust Boundary]                                                     │
├──────────────────────────────────────────────────────────────────────┤
│ Collapsible Panels                                                   │
│ [Standards Directory] [Lifecycle Stages] [Related Standards]         │
└──────────────────────────────────────────────────────────────────────┘
```

### Mobile Wireframe

```text
┌───────────────────────────────┐
│ LOGO / SITE NAME       ☰      │
├───────────────────────────────┤
│ Search                        │
├───────────────────────────────┤
│ Hero                          │
│ Title                         │
│ Summary                       │
│ CTA buttons                   │
├───────────────────────────────┤
│ Standards Landscape           │
├───────────────────────────────┤
│ Lifecycle Flow                │
├───────────────────────────────┤
│ Standards Graph               │
├───────────────────────────────┤
│ Industry Matrix               │
├───────────────────────────────┤
│ Featured Scenarios            │
├───────────────────────────────┤
│ Repository Explorer           │
├───────────────────────────────┤
│ Trust Boundary                │
└───────────────────────────────┘

Drawer Menu:
- Standards
- Lifecycle
- Industries
- Scenarios
- Crosswalks
- Software Stack
- About
```

---

## 2. Homepage Section Template

### 2.1 Hero
**Purpose:** orient the user immediately.

**Content:**
- Page title
- One-sentence mission
- Primary CTA: Explore Standards
- Secondary CTA: View Lifecycle
- Optional small note: Repository-backed guidance

**Recommended layout:**
- Title and summary on left
- small architecture/lifecycle diagram on right

---

### 2.2 Standards Landscape
**Purpose:** show the site’s core standards families.

**Cards:**
- US Electrical
- International Machinery
- Functional Safety
- Crosswalks
- Reference Models
- Scenarios

Each card should contain:
- one-line description
- 3–5 example standards or files
- “Open section” link

---

### 2.3 Lifecycle Flow
**Purpose:** show how standards enter the engineering process.

**Display:**
- horizontal lifecycle ribbon on desktop
- stacked cards on mobile

**Stages:**
- Concept
- Standards Selection
- Risk Assessment
- Safety Architecture
- Detailed Design
- Documentation
- Build
- Installation
- Pre-Commissioning / Calibration
- Commissioning / Validation
- Maintenance / Lifecycle Support

Each stage should show:
- standards involved
- deliverables
- PL / SIL relevance

---

### 2.4 Standards Relationship Graph
**Purpose:** show interconnectivity.

**Display:**
- Mermaid or SVG graph
- companion legend/chips

**Examples:**
- ISO 12100 → ISO 13849 / IEC 62061
- IEC 61511 → IEC 61508
- NFPA 79 ↔ IEC 60204-1
- UL 508A → NEC
- IEC 62443 overlays multiple routes

---

### 2.5 Industry Matrix
**Purpose:** show standards applicability by industry.

**Columns:**
- Industry
- Risk / Entry Standard
- Safety Framework
- Electrical Framework
- Cybersecurity
- Special Route Notes

**Rows:**
- Semiconductor
- Food & Beverage
- Energy
- Oil & Gas
- Marine
- Medical
- Nuclear
- Offshore
- Commercial
- Warehouse Automation (optional inferred)

---

### 2.6 Featured Scenarios
**Purpose:** convert theory into application.

**Scenario cards:**
- US Industrial Control Panel
- Global Machine (US + EU)
- Chemical / Process Skid
- Networked Safety PLC System
- Semiconductor Equipment Example

Each card should show:
- short summary
- likely starting standards
- one repository path
- one “next click”
- one warning / limitation

---

### 2.7 Repository Explorer
**Purpose:** help the user move into the actual knowledge base.

**Layout:**
- small directory tree preview
- “Start here” quick links

**Quick links examples:**
- New to US machine panels → open `us/`
- Comparing machinery safety frameworks → open `international/functional_safety/`
- Need an example project → open `scenario/`
- Need routing logic → open `routing/standards_applicability.md`

---

### 2.8 Trust Boundary
**Purpose:** prevent misuse.

**Content:**
- Local corpus provides guidance and routing
- Not a substitute for official purchased standards
- Some families are partial or TO VERIFY
- Scenario examples are educational, not legal certification packages

---

## 3. Page Templates

### 3.1 Standards Category Page Template
Example pages:
- /standards/us-electrical
- /standards/functional-safety
- /standards/international-machinery

```text
Page Header
├─ Title
├─ Short summary
├─ Breadcrumbs
└─ Category tags

Section 1: What this family covers
Section 2: Key standards in this family
Section 3: Relationship to other families
Section 4: Lifecycle stages affected
Section 5: Industry usage
Section 6: Example scenarios
Section 7: Repository links
Right Rail: Related standards / crosswalks / next clicks
```

**Use case:** orient users before they open individual standards.

---

### 3.2 Individual Standard Page Template
Example pages:
- /standards/iso-13849-1
- /standards/iec-61511
- /standards/nfpa-79

```text
Header
- Standard name
- Short role summary
- Family label
- Scope label
- Related standards chips

Main sections
1. What this standard is for
2. Where it fits in lifecycle
3. What it commonly connects to
4. Typical project types
5. Related repository content
6. Example scenario link
7. Warnings / local coverage limits

Right rail
- Related standards
- Lifecycle stages
- Industries
- Crosswalks
- Next repository click
```

**Important:** keep it conceptual, not clause-reproduction.

---

### 3.3 Lifecycle Stage Page Template
Example pages:
- /lifecycle/concept
- /lifecycle/detailed-design
- /lifecycle/commissioning

```text
Header
- Stage title
- One-sentence objective
- Previous / next stage navigation

Section 1: Stage purpose
Section 2: Standards influencing this stage
Section 3: PL / SIL role here
Section 4: Deliverables at this stage
Section 5: Typical mistakes / risks
Section 6: Scenario examples
Section 7: Repository-backed source files

Right rail
- Adjacent lifecycle stages
- Related standards
- Key deliverables
- Industry notes
```

---

### 3.4 Industry Page Template
Example pages:
- /industries/semiconductor
- /industries/oil-and-gas
- /industries/medical

```text
Header
- Industry name
- Short profile
- Risk profile badge

Section 1: Typical system types
Section 2: Common hazards
Section 3: Starting standards
Section 4: Safety route
Section 5: Electrical route
Section 6: Cybersecurity / hazardous area route
Section 7: Typical lifecycle emphasis
Section 8: Scenario examples
Section 9: Repository paths

Right rail
- Related industries
- Crosswalks
- Special warnings
- Next repository click
```

---

### 3.5 Scenario Page Template
Example pages:
- /scenarios/us-industrial-control-panel
- /scenarios/process-skid
- /scenarios/semiconductor-tool

```text
Header
- Scenario title
- Summary
- System type tags

Section 1: Project overview
Section 2: Hazard context
Section 3: Starting standards
Section 4: Lifecycle walkthrough
Section 5: Control architecture
Section 6: Safety architecture
Section 7: Documentation deliverables
Section 8: Verification and validation
Section 9: Maintenance / lifecycle support
Section 10: Repository source files

Right rail
- Related standards
- Related lifecycle pages
- Related scenarios
- Next click
```

---

### 3.6 Crosswalk Page Template
Example pages:
- /crosswalks/nfpa-79-vs-iec-60204-1
- /crosswalks/pl-vs-sil

```text
Header
- Comparison title
- One-line summary

Section 1: Why this comparison matters
Section 2: Scope overlap
Section 3: Main differences
Section 4: When to use one vs the other
Section 5: Lifecycle implications
Section 6: Scenario implications
Section 7: Repository source links

Right rail
- Related standards
- Related scenarios
- Industry relevance
```

---

### 3.7 Software Stack Page Template
Example pages:
- /software-stack/plc-and-safety-plc
- /software-stack/opc-ua-mqtt-and-edge

```text
Header
- Stack layer title
- Short summary

Section 1: Where this layer fits
Section 2: Safety relevance
Section 3: Standards and guidance links
Section 4: Common architectures
Section 5: Validation and lifecycle considerations
Section 6: Example scenarios

Right rail
- Related standards
- Related lifecycle pages
- Related diagrams
```

---

## 4. Shared UI Components

### Essential components
- TopNav
- SearchBar
- SidebarDirectory
- PageHeader
- Breadcrumbs
- RelatedStandardsChips
- LifecycleRibbon
- IndustryMatrixTable
- ScenarioCard
- CrosswalkComparisonTable
- TrustBoundaryNotice
- RepositoryPathCard
- NextClickPanel
- RightRail

### Nice-to-have later
- StandardsGraph viewer
- Expandable diagram modal
- Sticky lifecycle navigator
- Compare mode for two standards

---

## 5. Design Rules

### Tone
- technical
- calm
- neutral
- documentation-first

### Avoid
- marketing slogans
- giant decorative hero images
- flashy animation
- glassmorphism / startup visuals
- excessive gradients

### Prefer
- clean borders
- muted colors
- collapsible directory trees
- diagrams with captions
- compact tables
- visible repository paths

---

## 6. Navigation Model

### Primary navigation
- Standards
- Lifecycle
- Industries
- Scenarios
- Crosswalks
- Software Stack
- About

### Secondary navigation
Within each page:
- breadcrumbs
- related standards
- adjacent lifecycle stages
- next recommended repository click

---

## 7. Recommended First Pages to Build

1. Homepage
2. Standards landing page
3. Lifecycle landing page
4. Industry matrix page
5. Scenario landing page
6. ISO 13849 page
7. IEC 61511 page
8. NFPA 79 page
9. Semiconductor industry page
10. Process skid scenario page

---

## 8. Implementation Priority

### Phase 1
- Homepage
- Sidebar directory
- Standards family pages
- Lifecycle landing page
- Industry matrix
- 5 core diagrams

### Phase 2
- Standard detail pages
- Scenario pages
- Crosswalk pages
- Right context panel logic

### Phase 3
- Search
- Comparison mode
- Interactive standards graph
- Printable diagram assets

---

## 9. Suggested Homepage Copy Skeleton

### Title
Control System Standards Atlas

### Subtitle
A repository-backed reference guide for industrial control standards, lifecycle design, and standards routing.

### CTAs
- Explore Standards
- View Lifecycle

### Trust note
Guidance and navigation only. Official standards and project-specific validation remain required.

