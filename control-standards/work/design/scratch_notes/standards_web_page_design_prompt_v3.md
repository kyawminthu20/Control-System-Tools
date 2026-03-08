<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: PLANNING_ONLY
-->

# Standards Web Page Design Prompt V3

Use this prompt to generate a planning-only architecture and UX brief for a standards-focused web page. It is aligned to the current repository structure and explicitly calls out which dependencies are authoritative, partial, or planning-only.

## Prompt

```text
You are in PLANNING MODE ONLY.

Do not write code.
Do not generate HTML, CSS, React, wireframes, or implementation files.

Your task is to produce a high-quality architecture, content, and UX plan for a web interface that explains industrial automation standards and helps engineers navigate the local standards repository during control system design.

This page should feel like a standards intelligence interface:

- part standards navigator
- part engineering decision-support page
- part repository guide

It is not a marketing site and it is not a legal reproduction of standards text.

The output must stay conceptual, structured, and implementation-ready for a later frontend phase.

Do not invent clause-level content.
Do not reproduce copyrighted standards text.
Paraphrase concepts only.

PRIMARY AUTHORITATIVE SOURCE ROOT

- control-standards/rag/standards_intelligence/

PRIMARY AUTHORITATIVE DEPENDENCIES

Use these as the main source set:

- control-standards/rag/standards_intelligence/_index.yaml
- control-standards/rag/standards_intelligence/_standards_map.md
- control-standards/rag/standards_intelligence/routing/standards_applicability.md
- control-standards/rag/standards_intelligence/README.md
- control-standards/rag/standards_intelligence/file_structure.md

Use these standards-family folders as the main navigation structure:

- control-standards/rag/standards_intelligence/us/
- control-standards/rag/standards_intelligence/international/machinery/
- control-standards/rag/standards_intelligence/international/functional_safety/
- control-standards/rag/standards_intelligence/crosswalks/
- control-standards/rag/standards_intelligence/reference_models/
- control-standards/rag/standards_intelligence/scenario/

REFERENCE MODEL DEPENDENCIES

Use these files as conceptual anchors:

- control-standards/rag/standards_intelligence/reference_models/7-Layer Industrial Machine Architecture Model.md
- control-standards/rag/standards_intelligence/reference_models/Universal Machine Safety Architecture.md
- control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
- control-standards/rag/standards_intelligence/reference_models/15-Standard Minimum Compliance Stack.md

DIAGRAM DEPENDENCIES

Preferred diagram source:

- control-standards/rag/standards_intelligence/reference_models/standards_atlas_diagrams_reference.md

Secondary planning-only diagram source:

- control-standards/work/design/mermaid_diagrams_to_reference.md

SCENARIO DEPENDENCIES

Use these scenario packages for realistic examples and lifecycle deliverables:

- control-standards/rag/standards_intelligence/scenario/cnc_machine_safety_design/
- control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design/
- control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/

Especially useful scenario files:

- scenario/mini_machine_safety_design_v2/README.md
- scenario/mini_machine_safety_design_v2/standards_applicability_matrix.md
- scenario/mini_machine_safety_design_v2/control_architecture_and_network.md
- scenario/mini_machine_safety_design_v2/safety_functions_register.md
- scenario/mini_machine_safety_design_v2/verification_and_validation_plan.md
- scenario/mini_machine_safety_design_v2/industry_overlays/
- scenario/cnc_machine_safety_design/README.md
- scenario/cnc_machine_safety_design/standards_applicability_matrix.md

CROSSWALK DEPENDENCIES

Use these for comparison sections:

- control-standards/rag/standards_intelligence/crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md
- control-standards/rag/standards_intelligence/crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md
- control-standards/rag/standards_intelligence/crosswalks/overlap_matrix/standards_decision_workflow.md

REPOSITORY INTERPRETATION RULES

- Treat control-standards/rag/ as authoritative.
- Treat control-standards/work/design/ as planning-only and non-authoritative.
- Treat reference_models/ as routing, architecture, and conceptual guidance.
- Treat scenario/ as realistic design examples and lifecycle-document examples.
- Treat library_admin/ as administrative support, not a primary user-facing source.
- Some functional-safety content is scaffolded or partially populated. Do not overstate repository completeness.
- For IEC 61508, IEC 61511, IEC 62061, ISO 13849-1, IEC 62443, and IEC 60079-family topics, the repository often supports routing and architectural guidance more strongly than clause-level depth.
- If a topic is only partially supported by the local corpus, label it clearly as limited local coverage or TO VERIFY.

PAGE GOAL

The page must help engineers:

- understand the major standards families
- understand how standards connect across machine architecture and lifecycle stages
- understand when to route to US, international machinery, functional safety, software safety, cybersecurity, or intrinsic-safety guidance
- understand when machinery safety differs from process safety
- navigate to the right local repository folder or file next

BUSINESS QUESTIONS THE PAGE SHOULD ANSWER

- Where do I start for a US industrial control panel?
- Where do I start for a global machine sold in the US and EU?
- When should ISO 13849-1 be used versus IEC 62061 or IEC 61511?
- Where do IEC 61131-3, IEC 62443, and intrinsic-safety routing fit?
- Which repository folder or file should I open next?

CORE STANDARDS FAMILIES TO REPRESENT

- US electrical: NEC, NFPA 79, UL 508A
- International machinery: IEC 60204-1
- Functional safety: ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511
- Software, cybersecurity, and intrinsic-safety routing: IEC 61131-3, IEC 62443, IEC 60079 family
- Crosswalks and overlap analysis

Important:

- Software safety, cybersecurity, and intrinsic safety are not separate top-level folders in the repository.
- Present them as route topics anchored by `reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`, not as invented primary directory roots.

ENGINEERING LIFECYCLE INTEGRATION

The page must show how standards influence the control-system lifecycle:

- Concept
- Standards selection
- Risk assessment
- Safety architecture definition
- Detailed design and part sizing
- Draft design documentation
- Control system build and software implementation
- Installation
- Pre-commissioning and calibration
- Commissioning and validation
- Maintenance and lifecycle support

For each stage, identify:

- which standards usually influence that stage
- which typical engineering deliverables appear at that stage
- where PL or SIL decision logic becomes relevant
- which repository files best support that stage

Use scenario package files such as `system_description.md`, `safety_functions_register.md`, `requirements.yaml`, `control_architecture_and_network.md`, and `verification_and_validation_plan.md` as lifecycle evidence.

SIL VS PL FRAMEWORK

The page must explain the conceptual relationship between:

- ISO 13849 Performance Levels
- IEC 62061 machinery SIL
- IEC 61508 foundational functional safety
- IEC 61511 process-industry safety

Focus on:

- when machinery safety routes apply
- when process safety routes apply
- how project type changes the route
- how architecture choices change

Do not include equations or clause-level derivations.

INDUSTRY MATRIX RULES

Use repository-backed industries first:

- semiconductor
- food and beverage
- energy
- petroleum or oil and gas
- marine
- medical
- nuclear
- offshore
- commercial

These are supported most directly by:

- scenario/mini_machine_safety_design_v2/industry_overlays/

Optional illustrative industries:

- warehouse automation or logistics

If included, label them clearly as general machinery examples inferred from the reference models rather than dedicated industry-overlay content.

Do not require agricultural machinery unless you explicitly mark it as outside the current local corpus.

For the industry matrix, show conceptual starting points for:

- risk assessment
- functional safety
- electrical design
- cybersecurity
- hazardous area or intrinsic-safety routing where relevant

DIRECTORY-STYLE EXPLORER RULES

The explorer must reflect the real repository grouping first:

- US standards
- International machinery
- International functional safety
- Crosswalks
- Reference models
- Scenario packages

Then show secondary conceptual tags or routes for:

- software safety
- cybersecurity
- intrinsic safety
- machinery safety
- process safety

Do not invent primary site sections that imply folders not present in the repository.

REFERENCE ARCHITECTURE AND VISUAL ANCHORS

Use these as major visual anchors:

- 7-layer industrial machine architecture
- separation of standard control and safety control
- standards relationship graph
- machinery versus process-safety routing
- lifecycle overlay with standards and deliverables

SCENARIO REQUIREMENTS

Include these example scenarios:

1. UL-listed industrial control panel for the US market
   Source this mainly from:
   - us/ul_508a/
   - us/nec/
   - routing/standards_applicability.md
   - _standards_map.md

2. Robotic or machine-cell style system sold in the US and EU
   Source this mainly from:
   - reference_models/7-Layer Industrial Machine Architecture Model.md
   - reference_models/Universal Machine Safety Architecture.md
   - routing/standards_applicability.md
   - crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md

3. Chemical or process-oriented skid with shutdown logic
   Source this mainly from:
   - scenario/mini_machine_safety_design_v2/
   - reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
   - routing/standards_applicability.md

4. Control system with safety PLC software, networked control, and cybersecurity concerns
   Source this mainly from:
   - reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
   - scenario/mini_machine_safety_design_v2/control_architecture_and_network.md
   - scenario/cnc_machine_safety_design/control_architecture_and_network.md

5. Semiconductor-tool style global compliance example
   Source this mainly from:
   - reference_models/15-Standard Minimum Compliance Stack.md
   - scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md

For each scenario include:

- project summary
- likely starting standards
- repository-backed source paths
- recommended next click in the repository
- one warning about assumptions or incomplete local coverage

CONTENT BLOCKS TO PLAN

The plan should include:

1. Hero introduction
2. Standards landscape overview
3. Repository-backed standards explorer
4. Engineering lifecycle framework
5. Machine architecture model
6. Safety architecture model
7. Standards family grid
8. Industry standards matrix
9. Crosswalk comparisons
10. Example scenarios
11. Repository navigation guide
12. Trust boundaries and limitations

OUTPUT STRUCTURE

Your response must contain:

1. Page objective
2. Target users and top tasks
3. Information architecture
4. Detailed section plan
5. UI component recommendations
6. Visual direction
7. Mobile and desktop behavior
8. Content source mapping
9. Industry matrix concept
10. Lifecycle integration explanation
11. Example scenarios
12. Risks and content integrity warnings
13. Known content gaps and how the UI should label them
14. Implementation backlog

CONTENT SOURCE MAPPING RULES

For every major section:

- cite one or more exact repository paths
- distinguish authoritative source paths from inferred design decisions
- flag limited or scaffolded source coverage where applicable

DIAGRAM USAGE RULES

- Prefer diagrams already defined in `reference_models/standards_atlas_diagrams_reference.md`
- Use `work/design/mermaid_diagrams_to_reference.md` wherever it is needed.
- If a diagram implies a future subpage or route not yet backed by the repository, label it as proposed IA rather than existing structure

FORMATTING RULES

- stay in planning mode
- use short headings
- use tables where helpful
- keep the answer structured and practical
- do not write code
- do not claim the repository fully covers every standards family

END WITH

- proposed page title
- proposed subtitle
- primary CTA
- secondary CTA
- assets or diagrams to create next
- the line: "Awaiting approval before implementation."
```

## Verification Notes

- This version is aligned to the current repository structure.
- It now treats `reference_models/15-Standard Minimum Compliance Stack.md` as a real dependency instead of an empty placeholder.
- It separates true repository navigation groups from conceptual route topics like software safety and cybersecurity.
- It narrows the industry matrix to repository-backed overlays and explicitly labels optional inferred industries.
