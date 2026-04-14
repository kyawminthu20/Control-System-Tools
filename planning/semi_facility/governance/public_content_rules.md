<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: DRAFT
CATEGORY: SEMI_FACILITY_GOVERNANCE
-->

# Public Content Rules

## Purpose

This library is intended to stay public-friendly and reusable. The working rule is simple: store public-safe engineering knowledge, not protected source material.

## Allowed content

- Public manufacturer datasheets, catalog pages, and publicly posted manuals.
- Government, university, and public-library resources.
- Public trade-association summaries, application notes, and conference papers.
- Original engineering summaries, taxonomies, crosswalks, and design notes written in this repo.
- Bibliographic records, document metadata, and source links.
- Paraphrased standards guidance that avoids copyrighted standard text.

## Not allowed

- Licensed standards text copied into the repo.
- Customer drawings, fab-specific packages, or NDA vendor deliverables.
- Verbatim copies of copyrighted manuals beyond short citation-sized excerpts.
- Screenshots, scans, or image dumps with unclear redistribution rights.
- Proprietary setpoints, recipes, tool parameters, or confidential alarm lists.

## Manual handling rule

- Default storage mode is `link-only` plus a derived note.
- If a manual is public but redistribution rights are unclear, do not commit the PDF. Store the citation, URL, and your summary note instead.
- Only commit the original file when redistribution is clearly allowed or the material is public domain.

## Citation minimum

Every reusable note should capture:

- source title
- publisher or manufacturer
- source type
- public URL or local location
- retrieval date
- document revision when known
- note owner or normalizer

## Confidence labels

Use one of these labels inside notes when the strength of evidence matters:

- `PRIMARY_PUBLIC`: direct public source from the publisher, regulator, or standards body summary page
- `SECONDARY_PUBLIC`: consultant, training, or explanatory source
- `LOCAL_DERIVED`: repo-authored summary or crosswalk
- `WORKING_INFERENCE`: engineering inference that still needs stronger source support

## Publish checklist

- The file is paraphrased and free of protected text.
- The source is public or clearly redistributable.
- The note states what is known versus inferred.
- The promotion target is clear.
- Any edition-sensitive standard reference is marked for edition verification.
