# Content Standards

**Authoritative.** How information is added to the site. Applies to every
page under `docs/` and to anyone — human or AI — writing one.

## 1. Source Discipline

- The corpus (`control-standards/rag/`) is ground truth. Site pages present
  it; they do not invent technical content beyond it. If a page needs
  material the corpus lacks, add it to the corpus first (via the
  [promotion checklist](../control-standards/governance/promotion_checklist_drafts_to_rag.md)),
  then to the site. *"The plan is a target; the corpus is ground truth."*
- After adding/editing corpus files, run `python3 tools/generate_rag_tree.py`
  to refresh the site mirror — it is a manual step and drifts otherwise.

## 2. Copyright Boundary (non-negotiable)

- **Never reproduce standards text or table values.** Paraphrase procedures
  and logic in original language. Cite tables by number ("Table 310.16"),
  quote at most single values inside worked examples.
- Never copy third-party training material, transcripts, vendor screenshots,
  or affiliate content. Original diagrams and original wording only.
- Licensed numeric datasets belong in `data/standards_tables/` (gitignored),
  never in committed files or site pages.

## 3. Status Vocabulary (5 terms, site-wide)

| Status | Meaning |
|---|---|
| **Reviewed** | Author-checked against the identified edition |
| **Partial coverage** | Only selected clauses/topics covered |
| **Review pending** | Content exists; technical validation outstanding |
| **Needs revalidation** | Previously reviewed; edition may be superseded |
| **Planned** | Identified, not yet written |

Never use "Complete", "TO VERIFY", "NOT IN CORPUS", or other retired labels
on site pages. (Corpus files keep their internal authoring flags — the site
is the presentation layer; the raw flags are visible only in the RAG
browser.) New AI-drafted pages start at **Review pending** — an agent never
marks its own work "Reviewed"; only the author does, after checking it.

## 4. Page Anatomy

Every technical page carries:

1. Frontmatter: `layout: default`, `title`, `description`, `breadcrumb`,
   and a `review:` block:
   ```yaml
   review:
     standard: "<governing document/body>"
     edition: "<exact edition, or 'exact governing revision not yet recorded'>"
     status: "Review pending"          # 5-term vocabulary
     coverage: "<one honest line on what is and is not covered>"
     last_reviewed: "Month YYYY"       # content date until status is Reviewed
   ```
   Never write "current published spec" as an edition — record the revision
   or say it is not yet recorded.

   Pages that are pure navigation or redirect stubs may opt out with
   `review_exempt: "<reason>"` instead of a `review:` block — the reason is
   mandatory, a page cannot declare both keys, and the exemption is for pages
   with no technical claims of their own, never a shortcut for content pages.
2. A `page-header` div (label, H1, one-line `<p>`).
3. `related_standards` frontmatter where relevant (feeds the context panel).
4. Internal links to related pages — no orphan pages.

## 5. Page Templates

**Standards detail pages** — the Phase 30 eight-section floor:
Quick Start (5 bullets) → Standard Overview → per-clause/part depth →
Worked Example (concrete numbers, named scenario) → Common Mistakes (5+,
numbered, each with root cause) → Practical Checklist → Lifecycle
Application table → Related Standards.

**Wiring & installation guides** (`docs/design/wiring/`) — the device-wiring
template (see [ROADMAP.md](ROADMAP.md) for the program):
Overview (device + terminal groups, what this guide covers/excludes) →
Before You Start (nameplate data, drawings, tools, de-energize/LOTO
reminder) → Sizing & Protection (conductors, OCPD, overload — computed via
the `cst` toolkit, cited to NEC/NFPA 79/IEC 60204-1) → Power Wiring →
Control / Signal Wiring → Grounding, Shielding & EMC → Common Mistakes
(numbered, root cause) → Verification Checks (checklist, links to
commissioning/loop-sheet templates) → Standards References.
Extra rules for this genre: field practice comes from the knowledge-intake
loop (ROADMAP.md) or is explicitly marked generally-accepted-practice with a
verify note; every guide carries a prominent qualified-personnel /
de-energized-work safety notice; vendor-specific values are never stated as
universal — "consult the device manual" is a required refrain.

**Communications protocol pages** — the six-question structure:
Overview (with one Mermaid architecture diagram) → Where It Is Used →
Network Design → Configuration (device-description files; illustrative
config examples flagged as vendor-defined) → Commissioning Checks
(checklist) → Diagnostics (layered; Wireshark filters with a
verify-against-your-version caveat, or the honest serial-bus toolset) →
Common Faults (symptom/cause/first-check table) → Related Pages.
Physical-layer pages adapt the middle sections to Design Rules /
Installation Practice / Commissioning & Testing / Diagnostics.

## 6. Voice Rules (calibrated engineering language)

- No absolutes: avoid "mandatory", "non-negotiable", "always", "guaranteed",
  "never fails" — write "typically", "normally", "should normally follow",
  "verify against the governing edition". Exception: statements that are
  themselves the standard's requirement may be stated firmly *with the
  citation* (e.g. Art 409.110 SCCR marking).
- No marketing language, no vendor endorsement, no market-position claims
  ("dominant", "best", "simplest") — name vendors only as examples.
- Distinguish requirement / guidance / interpretation / example when the
  difference matters.
- Never conflate an application protocol with a physical layer
  (Modbus ≠ RS-485).
- Examples use RFC1918 addressing and invented tags only. Constructed
  scenarios must say so ("constructed teaching example").
- Applicability caveats sit next to decision tables, not only in the footer.

## 7. Privacy and Confidentiality

- No employer or customer data of any kind: no project names, methods,
  screenshots, naming conventions, network captures, or addresses.
- Packet captures are never published; capture examples are described, not
  attached, unless fully synthetic.
- Author email in git history stays the GitHub noreply address.

## 8. Validation Gates (before any merge touching docs/)

```bash
cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build   # clean build
python3 tools/check_internal_links.py docs/_site            # zero broken links
python3 tools/validate_ai_boundaries.py                     # baseline: no NEW failures
```

Plus: `project_state/` updated (see [AI_WORKFLOW.md](AI_WORKFLOW.md)), and
new pages added to `docs/_data/navigation.yml` and the relevant section
index — no orphan pages.
