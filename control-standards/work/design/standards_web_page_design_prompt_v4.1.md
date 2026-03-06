You are in PLANNING MODE ONLY.

Do not write code.
Do not generate HTML, CSS, React, wireframes, or implementation files.

Your task is to produce a high-quality architecture, content, and UX plan for a web interface that explains industrial automation standards and helps engineers navigate the local standards repository during control system design.

The page should function as a **standards intelligence interface**:

• part standards directory  
• part engineering lifecycle guide  
• part standards relationship map  
• part repository navigator

It is not a marketing site and it is not a legal reproduction of standards text.

The output must stay conceptual, structured, and implementation-ready for a later frontend phase.

Never invent clause-level content.
Never reproduce copyrighted standards text.
Paraphrase standards concepts only.

---

PRIMARY AUTHORITATIVE SOURCE ROOT

control-standards/rag/standards_intelligence/

Treat this directory as the authoritative local corpus.

---

PRIMARY AUTHORITATIVE DEPENDENCIES

Use these repository sources as the primary knowledge base:

control-standards/rag/standards_intelligence/\_index.yaml  
control-standards/rag/standards_intelligence/\_standards_map.md  
control-standards/rag/standards_intelligence/routing/standards_applicability.md  
control-standards/rag/standards_intelligence/README.md

If present also consult:

control-standards/rag/standards_intelligence/file_structure.md

---

PRIMARY NAVIGATION STRUCTURE

The web interface should reflect the real repository structure first.

Primary navigation groups:

• us/  
• international/machinery/  
• international/functional_safety/  
• crosswalks/  
• reference_models/  
• scenario/

Do not invent top-level navigation sections that imply folders not present in the repository.

---

REFERENCE MODEL SOURCES

Use these conceptual anchors where appropriate:

reference_models/7-Layer Industrial Machine Architecture Model.md  
reference_models/Universal Machine Safety Architecture.md  
reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md

Optional structural reference:

reference_models/15-Standard Minimum Compliance Stack.md

Only use this if populated and repository-backed.

---

DIAGRAM SOURCES

Preferred diagram source if present:

reference_models/standards_atlas_diagrams_reference.md

If not present treat diagrams as conceptual assets to be created during implementation.

Planning-only diagram source:

control-standards/work/design/mermaid_diagrams_to_reference.md

Use this only as planning guidance.

---

SCENARIO SOURCES

Use scenario packages as realistic design examples.

Primary scenario sources:

scenario/cnc_machine_safety_design/  
scenario/mini_machine_safety_design/  
scenario/mini_machine_safety_design_v2/

Important example files include:

system_description.md  
standards_applicability_matrix.md  
control_architecture_and_network.md  
safety_functions_register.md  
verification_and_validation_plan.md  
industry_overlays/

These provide lifecycle deliverables and standards routing examples.

---

CROSSWALK SOURCES

Use these for standards comparison:

crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md  
crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md  
crosswalks/overlap_matrix/standards_decision_workflow.md

---

REPOSITORY INTERPRETATION RULES

• control-standards/rag/ is authoritative  
• control-standards/work/design/ is planning-only  
• reference_models provide architecture guidance  
• scenario provides example systems  
• library_admin is administrative

If coverage is partial label the topic:

"Limited local coverage" or "TO VERIFY".

---

PAGE GOAL

The interface must help engineers:

• understand standards families  
• understand standards relationships  
• understand lifecycle impact  
• understand machinery vs process safety routing  
• understand PL vs SIL concepts  
• navigate to the correct repository location

---

KEY QUESTIONS THE PAGE SHOULD ANSWER

Where do I start for a US industrial control panel?

Where do I start for a global machine sold in the US and EU?

When should ISO 13849 be used versus IEC 62061 or IEC 61511?

Where do IEC 61131-3, IEC 62443, and intrinsic safety fit?

Which repository folder should I open next?

---

CORE STANDARDS FAMILIES

US Electrical

• NEC  
• NFPA 79  
• UL 508A

International Machinery

• IEC 60204-1

Functional Safety

• ISO 12100  
• ISO 13849-1  
• IEC 62061  
• IEC 61508  
• IEC 61511

Software / Cybersecurity

• IEC 61131-3  
• IEC 62443

Hazardous Area

• IEC 60079 family

Software safety, cybersecurity, and intrinsic safety should appear as **routing topics**, not repository folders.

---

ENGINEERING LIFECYCLE

Show standards influence across lifecycle stages:

Concept  
Standards selection  
Risk assessment  
Safety architecture definition  
Detailed design and part sizing  
Draft design documentation  
Control system build  
Installation  
Pre-commissioning and calibration  
Commissioning and validation  
Maintenance and lifecycle support

For each stage identify:

• standards influence  
• engineering deliverables  
• PL or SIL decision points  
• repository sources

---

SIL VS PL FRAMEWORK

Explain the conceptual relationship between:

ISO 13849 Performance Levels  
IEC 62061 machinery SIL  
IEC 61508 functional safety foundation  
IEC 61511 process safety

Focus on routing logic and architecture implications.

---

INDUSTRY MATRIX

Use repository-backed industries first:

• semiconductor  
• food and beverage  
• energy  
• petroleum / oil and gas  
• marine  
• medical  
• nuclear  
• offshore  
• commercial

These come primarily from:

scenario/mini_machine_safety_design_v2/industry_overlays/

Optional inferred industries may include:

warehouse automation

Label them clearly as inferred examples.

---

DIRECTORY STYLE STANDARDS EXPLORER

The site should behave like a structured standards library.

Primary explorer groups should mirror repository structure:

US standards  
International machinery  
Functional safety  
Crosswalks  
Reference models  
Scenario packages

Secondary conceptual tags may include:

machinery safety  
process safety  
cybersecurity  
intrinsic safety  
software safety

These are tags, not repository folders.

---

WEB LAYOUT DESIGN REQUIREMENTS

The site should follow a **technical documentation portal layout**, not a marketing page.

Preferred structure:

Top navigation bar  
Left directory sidebar  
Main content area  
Right context panel

Example conceptual layout:

Top Navigation

Sidebar Directory | Main Content | Context Panel

The interface should feel similar to:

engineering documentation systems  
technical manuals  
standards reference libraries

Avoid modern marketing aesthetics such as:

large hero graphics  
heavy animations  
startup-style landing sections  
gradient or glass UI styles

Prefer a **technical manual visual style**.

---

TOP NAVIGATION

Top navigation should remain minimal:

Standards  
Lifecycle  
Industries  
Scenarios  
Crosswalks  
Software Stack  
About

The sidebar handles detailed navigation.

---

SIDEBAR DIRECTORY

The sidebar should act as the main **standards explorer**.

Example structure:

Standards

US Electrical  
NEC  
NFPA 79  
UL 508A

Machinery  
ISO 12100  
ISO 13849  
IEC 62061

Functional Safety  
IEC 61508  
IEC 61511

Electrical  
IEC 60204

Cybersecurity  
IEC 62443

Sections should be collapsible.

---

MAIN CONTENT AREA

Main content pages should follow this structure:

Title  
Summary  
Diagram  
Explanation  
Tables or comparisons  
Scenario examples  
Links to related standards

---

CONTEXT PANEL

The right context panel should show:

Related standards  
Lifecycle stage  
Industry usage  
Crosswalk references

This allows users to navigate the standards knowledge graph.

---

VISUAL ANCHORS

Use diagrams such as:

7-layer industrial machine architecture  
standard vs safety control separation  
standards relationship graph  
machinery vs process routing  
lifecycle overlay with standards

Prefer repository diagrams when available.

---

SCENARIO REQUIREMENTS

Include these examples:

US industrial control panel  
Global machine (US + EU)  
Process skid shutdown system  
Networked safety PLC architecture  
Semiconductor equipment compliance

Each scenario must include:

project summary  
starting standards  
repository paths  
next recommended repository click  
assumptions or limitations

---

CONTENT BLOCKS

Hero introduction  
Standards landscape overview  
Standards explorer  
Lifecycle framework  
Machine architecture  
Safety architecture  
Standards family grid  
Industry matrix  
Crosswalk comparisons  
Example scenarios  
Repository navigation guide  
Trust boundaries

---

OUTPUT STRUCTURE

The response must contain:

1 Page objective  
2 Target users and tasks  
3 Information architecture  
4 Section plan  
5 UI component recommendations  
6 Visual direction  
7 Mobile and desktop behavior  
8 Content source mapping  
9 Industry matrix concept  
10 Lifecycle integration explanation  
11 Example scenarios  
12 Risks and integrity warnings  
13 Known content gaps  
14 Implementation backlog

---

Reference to these files they could be useful for content and design inspiration:

/Users/kyawminthu/Dev/Control System Tools/control-standards/work/design/mermaid_diagrams_to_reference.md

/Users/kyawminthu/Dev/Control System Tools/control-standards/work/design/standards_atlas_homepage_wireframe_and_templates.md

FORMATTING RULES

Stay in planning mode.

Use short headings.

Use tables where helpful.

Do not write code.

Do not claim the repository fully covers every standards family.

---

END WITH

Proposed page title  
Proposed subtitle  
Primary CTA  
Secondary CTA  
Assets or diagrams to create next

End with:

"Awaiting approval before implementation."
