---
layout: default
title: "Working Space and Table Navigation"
description: "How to read NEC tables and condition statements correctly — using working-space requirements as the training example."
breadcrumb:
  - name: "Training"
    url: "/training/"
  - name: "NEC Application"
    url: "/training/nec-application/"
repo_path: "control-standards/rag/training_modules/nec_application/working_space_and_table_navigation.md"
related_standards:
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
---

<div class="page-header">
  <span class="page-header__label">Training — NEC Application</span>
  <h1>Working Space and Table Navigation</h1>
</div>

## Purpose

This module uses working-space review as a training example for how to read NEC tables and condition statements carefully.

## Why this example matters

Working-space questions are useful training examples because they force the reader to:

- Identify the correct section
- Confirm the correct table
- Interpret voltage category and condition statements

NEC 110.26 defines working space for equipment operating at 1000 V nominal or less to ground. The table requires knowing the voltage to ground and the condition of the space on the opposite side.

## Table-reading discipline

Use this order every time you open an NEC table:

1. Verify the table title
2. Identify the row logic
3. Identify the column logic
4. Read notes and condition descriptions
5. Confirm the answer against the actual equipment condition

## Do not jump straight to the number

A common mistake is to see a familiar table and grab a value before checking:

- Whether the table uses voltage to ground or line-to-line
- Which condition applies (Condition 1, 2, or 3 in Table 110.26(A)(1))
- Whether nearby notes change the result

Conditions 1, 2, and 3 in Table 110.26(A)(1) describe what is on the opposite side of the working space:

| Condition | Description |
|-----------|-------------|
| 1 | Exposed live parts on one side and no live or grounded parts on the other |
| 2 | Exposed live parts on one side and grounded parts on the other |
| 3 | Exposed live parts on both sides |

Getting the condition wrong changes the required depth from roughly 900 mm (3 ft) to 1.2 m (4 ft) or more.

## Practical use outside an exam

The same discipline applies when reading any NEC table in real design work:

- Conductor ampacity tables (310.16) — require temperature column and insulation type
- Ambient correction tables — require confirming the base temperature assumption
- Spacing tables — require confirming voltage class and insulation method
- Grounding conductor sizing tables (250.122) — require using the overcurrent device rating as the row key

## Working takeaway

Tables are not shortcuts around reading.

They are compact rule structures that still require:

- The right section
- The right conditions
- The right interpretation basis

Getting those three things right before reading the number is the discipline that prevents field rejections.

## Related standards

- NEC 2023, Article 110 — Requirements for Electrical Installations
- NEC 2023, Article 310 — Conductors for General Wiring
- NEC 2023, Article 250 — Grounding and Bonding

---

<div style="display:flex; justify-content:space-between; margin-top:2rem; font-size:0.9rem;">
  <a href="{{ '/training/nec-application/nec-code-reading/' | relative_url }}">&larr; NEC Code Reading Fundamentals</a>
  <a href="{{ '/training/nec-application/' | relative_url }}">↑ NEC Application</a>
  <a href="{{ '/training/nec-application/motor-panel-code-application/' | relative_url }}">Motor and Panel Code Application &rarr;</a>
</div>
