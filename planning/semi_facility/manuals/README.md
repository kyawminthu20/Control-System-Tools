<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_MANUAL_HANDLING
-->

# Manuals

## Purpose

This folder is for manual metadata, manual summaries, and safe derived notes for instruments and devices used in semiconductor facilities.

## Storage policy

- Default to `link-only` plus a summary note.
- Do not commit vendor PDFs until redistribution rights are clear.
- If a manual is public domain or clearly redistributable, record that status in the catalog before storing the file.

## What to extract from each manual

- manufacturer and model family
- device class and intended use
- measurement or actuation principle
- process media and wetted-material compatibility
- cleanliness or purity fit
- electrical power and signal interface
- network or protocol options
- installation constraints
- calibration and maintenance requirements
- diagnostics, failure modes, and alarm implications

## Workflow

1. Add the manual to [Manual Catalog](manual_catalog.md).
2. Create a derived note from [Instrument Manual Note Template](instrument_manual_note_template.md).
3. Link the note from the relevant system note and source register entry.
