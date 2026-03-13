# FE Study Extraction Tools

Local-first tooling for the ignored FE study archive under `planning/FE_Study/`.

## Scripts

- `inventory_fe_study.py` - create the folder scaffold and manifest
- `extract_fe_study.py` - run local extraction, export DOCX media, and stage OCR work
- `quality_check_fe_study.py` - score extraction outputs and flag likely failures
- `summarize_fe_study.py` - generate per-source summaries from cleaned Markdown

## Support Module

- `common.py` - shared helpers for manifest IO, source classification, path generation,
  DOCX profiling, PDF extraction detection, Markdown rendering, and run logging

## Default Target

All scripts default to the full FE study tree:

```text
planning/FE_Study/
```

Outputs stay inside that ignored tree:

```text
_inventory/
_logs/
_extracted/raw/
_extracted/clean/
_chunks/
_summaries/
_samples/
```

## Usage

Create the manifest and scaffold:

```bash
python3 tools/fe_study/inventory_fe_study.py
```

Run a small pilot:

```bash
python3 tools/fe_study/extract_fe_study.py --source-id automation_fe_handbook_9p5 --source-id automation_module_9
```

Summarize the pilot outputs:

```bash
python3 tools/fe_study/summarize_fe_study.py --source-id automation_fe_handbook_9p5 --source-id automation_module_9
```

Run quality checks on extracted files:

```bash
python3 tools/fe_study/quality_check_fe_study.py --source-id automation_fe_handbook_9p5 --source-id automation_module_9
```

## Common CLI Filters

The runnable scripts support these filters where relevant:

- `--source-root` - override the default `planning/FE_Study/` tree
- `--priority` - restrict to one priority band such as `P1`
- `--family` - restrict to one source family such as `module_docx`
- `--source-id` - target one or more specific manifest rows
- `--status` - restrict by manifest status on extraction and quality-check passes
- `--limit` - cap the number of rows processed in a run

Examples:

```bash
python3 tools/fe_study/extract_fe_study.py --priority P1
python3 tools/fe_study/quality_check_fe_study.py --family module_docx --limit 10
python3 tools/fe_study/summarize_fe_study.py --source-id automation_module_9
```

## Nested Folders

The inventory is recursive. Source IDs and output paths include the relative folder path so files with the same basename in different subfolders do not collide.

## Optional Dependencies

The scripts work with the standard library for inventory, DOCX profiling, DOCX text extraction,
and DOCX media export. PDF text extraction improves if any of these are installed locally:

- `pypdf`
- `PyPDF2`
- `PyMuPDF`
- `pdftotext`

Image-heavy DOCX files and scanned PDFs still need OCR tooling such as `tesseract` or
`ocrmypdf` after the local staging pass.
