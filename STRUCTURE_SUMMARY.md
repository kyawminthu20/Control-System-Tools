# Workspace Structure Summary

Use this file as a tree reference for the whole workspace. The primary narrative lives in [README.md](/Users/kyawminthu/Dev/Control System Tools/README.md) and [PROJECT_STARTUP_CONTEXT.md](/Users/kyawminthu/Dev/Control System Tools/PROJECT_STARTUP_CONTEXT.md).

<!-- AUTO-GENERATED TREE START -->
## Directory Tree
**Last Auto-Updated:** 2026-04-13 21:26:48

```text
├── .claude/
│   ├── agents/
│   │   ├── rag-reviewer.md
│   │   └── standards-lookup.md
│   ├── settings.json
│   ├── settings.local.json
│   └── skills/
│       ├── explain-code/
│       │   └── SKILL.md
│       ├── new-rag-module/
│       │   └── SKILL.md
│       ├── promote-draft/
│       │   └── SKILL.md
│       └── validate-rag/
│           └── SKILL.md
├── .gemini/
├── .github/
│   └── workflows/
│       └── pages.yml
├── .gitignore
├── .mcp.json
├── .playwright-mcp/
│   ├── console-2026-03-06T07-01-55-004Z.log
│   ├── console-2026-03-08T21-17-22-955Z.log
│   ├── console-2026-03-08T21-19-03-191Z.log
│   ├── console-2026-03-08T21-19-12-540Z.log
│   ├── console-2026-03-09T14-33-31-511Z.log
│   ├── console-2026-03-10T02-49-09-555Z.log
│   ├── console-2026-03-17T00-47-46-956Z.log
│   └── page-2026-03-09T14-32-39-211Z.png
├── .pytest_cache/
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   ├── README.md
│   └── v/
│       └── cache/
│           ├── lastfailed
│           ├── nodeids
│           └── stepwise
├── .python-version
├── .venv/
│   ├── .gitignore
│   ├── .lock
│   ├── CACHEDIR.TAG
│   ├── bin/
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── activate.nu
│   │   ├── activate.ps1
│   │   ├── activate_this.py
│   │   ├── deactivate.bat
│   │   ├── pydoc.bat
│   │   ├── pymupdf
│   │   ├── python -> /Users/kyawminthu/.local/share/uv/python/cpython-3.13.5-macos-aarch64-none/bin/python3.13
│   │   ├── python3 -> python
│   │   └── python3.13 -> python
│   ├── lib/
│   │   └── python3.13/
│   │       └── site-packages/
│   │           ├── PyPDF2/
│   │           │   ├── __init__.py
│   │           │   ├── _cmap.py
│   │           │   ├── _codecs/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── adobe_glyphs.py
│   │           │   │   ├── pdfdoc.py
│   │           │   │   ├── std.py
│   │           │   │   ├── symbol.py
│   │           │   │   └── zapfding.py
│   │           │   ├── _encryption.py
│   │           │   ├── _merger.py
│   │           │   ├── _page.py
│   │           │   ├── _protocols.py
│   │           │   ├── _reader.py
│   │           │   ├── _security.py
│   │           │   ├── _utils.py
│   │           │   ├── _version.py
│   │           │   ├── _writer.py
│   │           │   ├── constants.py
│   │           │   ├── errors.py
│   │           │   ├── filters.py
│   │           │   ├── generic/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _annotations.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── _data_structures.py
│   │           │   │   ├── _fit.py
│   │           │   │   ├── _outline.py
│   │           │   │   ├── _rectangle.py
│   │           │   │   └── _utils.py
│   │           │   ├── pagerange.py
│   │           │   ├── papersizes.py
│   │           │   ├── py.typed
│   │           │   ├── types.py
│   │           │   └── xmp.py
│   │           ├── _virtualenv.pth
│   │           ├── _virtualenv.py
│   │           ├── fitz/
│   │           │   ├── __init__.py
│   │           │   ├── table.py
│   │           │   └── utils.py
│   │           ├── pymupdf/
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _apply_pages.py
│   │           │   ├── _build.py
│   │           │   ├── _extra.so
│   │           │   ├── _mupdf.so
│   │           │   ├── _wxcolors.py
│   │           │   ├── extra.py
│   │           │   ├── libmupdf.dylib
│   │           │   ├── libmupdfcpp.so
│   │           │   ├── mupdf-devel/
│   │           │   │   ├── include/
│   │           │   │   │   └── mupdf/
│   │           │   │   │       ├── classes.h
│   │           │   │   │       ├── classes2.h
│   │           │   │   │       ├── exceptions.h
│   │           │   │   │       ├── extra.h
│   │           │   │   │       ├── fitz/
│   │           │   │   │       │   ├── archive.h
│   │           │   │   │       │   ├── band-writer.h
│   │           │   │   │       │   ├── barcode.h
│   │           │   │   │       │   ├── bidi.h
│   │           │   │   │       │   ├── bitmap.h
│   │           │   │   │       │   ├── buffer.h
│   │           │   │   │       │   ├── color.h
│   │           │   │   │       │   ├── compress.h
│   │           │   │   │       │   ├── compressed-buffer.h
│   │           │   │   │       │   ├── config.h
│   │           │   │   │       │   ├── context.h
│   │           │   │   │       │   ├── crypt.h
│   │           │   │   │       │   ├── deskew.h
│   │           │   │   │       │   ├── device.h
│   │           │   │   │       │   ├── display-list.h
│   │           │   │   │       │   ├── document.h
│   │           │   │   │       │   ├── export.h
│   │           │   │   │       │   ├── filter.h
│   │           │   │   │       │   ├── font.h
│   │           │   │   │       │   ├── geometry.h
│   │           │   │   │       │   ├── getopt.h
│   │           │   │   │       │   ├── glyph-cache.h
│   │           │   │   │       │   ├── glyph.h
│   │           │   │   │       │   ├── hash.h
│   │           │   │   │       │   ├── heap-imp.h
│   │           │   │   │       │   ├── heap.h
│   │           │   │   │       │   ├── hyphen.h
│   │           │   │   │       │   ├── image.h
│   │           │   │   │       │   ├── json.h
│   │           │   │   │       │   ├── link.h
│   │           │   │   │       │   ├── log.h
│   │           │   │   │       │   ├── outline.h
│   │           │   │   │       │   ├── output-svg.h
│   │           │   │   │       │   ├── output.h
│   │           │   │   │       │   ├── path.h
│   │           │   │   │       │   ├── pixmap.h
│   │           │   │   │       │   ├── pool.h
│   │           │   │   │       │   ├── separation.h
│   │           │   │   │       │   ├── shade.h
│   │           │   │   │       │   ├── store.h
│   │           │   │   │       │   ├── story-writer.h
│   │           │   │   │       │   ├── story.h
│   │           │   │   │       │   ├── stream.h
│   │           │   │   │       │   ├── string-util.h
│   │           │   │   │       │   ├── structured-text.h
│   │           │   │   │       │   ├── system.h
│   │           │   │   │       │   ├── text.h
│   │           │   │   │       │   ├── track-usage.h
│   │           │   │   │       │   ├── transition.h
│   │           │   │   │       │   ├── tree.h
│   │           │   │   │       │   ├── types.h
│   │           │   │   │       │   ├── util.h
│   │           │   │   │       │   ├── version.h
│   │           │   │   │       │   ├── write-pixmap.h
│   │           │   │   │       │   ├── writer.h
│   │           │   │   │       │   └── xml.h
│   │           │   │   │       ├── fitz.h
│   │           │   │   │       ├── functions.h
│   │           │   │   │       ├── helpers/
│   │           │   │   │       │   ├── mu-office-lib.h
│   │           │   │   │       │   ├── mu-threads.h
│   │           │   │   │       │   └── pkcs7-openssl.h
│   │           │   │   │       ├── html.h
│   │           │   │   │       ├── internal.h
│   │           │   │   │       ├── memento.h
│   │           │   │   │       ├── pdf/
│   │           │   │   │       │   ├── annot.h
│   │           │   │   │       │   ├── clean.h
│   │           │   │   │       │   ├── cmap.h
│   │           │   │   │       │   ├── crypt.h
│   │           │   │   │       │   ├── document.h
│   │           │   │   │       │   ├── event.h
│   │           │   │   │       │   ├── font.h
│   │           │   │   │       │   ├── form.h
│   │           │   │   │       │   ├── image-rewriter.h
│   │           │   │   │       │   ├── interpret.h
│   │           │   │   │       │   ├── javascript.h
│   │           │   │   │       │   ├── name-table.h
│   │           │   │   │       │   ├── object.h
│   │           │   │   │       │   ├── page.h
│   │           │   │   │       │   ├── parse.h
│   │           │   │   │       │   ├── recolor.h
│   │           │   │   │       │   ├── resource.h
│   │           │   │   │       │   ├── xref.h
│   │           │   │   │       │   └── zugferd.h
│   │           │   │   │       ├── pdf.h
│   │           │   │   │       └── ucdn.h
│   │           │   │   └── lib/
│   │           │   │       └── libmupdf-threads.a
│   │           │   ├── mupdf.py
│   │           │   ├── py.typed
│   │           │   ├── pymupdf.py
│   │           │   ├── table.py
│   │           │   └── utils.py
│   │           ├── pymupdf-1.27.2.dist-info/
│   │           │   ├── COPYING
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── README.md
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   └── entry_points.txt
│   │           ├── pypdf/
│   │           │   ├── __init__.py
│   │           │   ├── _cmap.py
│   │           │   ├── _codecs/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _codecs.py
│   │           │   │   ├── adobe_glyphs.py
│   │           │   │   ├── core_font_metrics.py
│   │           │   │   ├── pdfdoc.py
│   │           │   │   ├── std.py
│   │           │   │   ├── symbol.py
│   │           │   │   └── zapfding.py
│   │           │   ├── _crypt_providers/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── _cryptography.py
│   │           │   │   ├── _fallback.py
│   │           │   │   └── _pycryptodome.py
│   │           │   ├── _doc_common.py
│   │           │   ├── _encryption.py
│   │           │   ├── _font.py
│   │           │   ├── _page.py
│   │           │   ├── _page_labels.py
│   │           │   ├── _protocols.py
│   │           │   ├── _reader.py
│   │           │   ├── _text_extraction/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _layout_mode/
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _fixed_width_page.py
│   │           │   │   │   ├── _text_state_manager.py
│   │           │   │   │   └── _text_state_params.py
│   │           │   │   └── _text_extractor.py
│   │           │   ├── _utils.py
│   │           │   ├── _version.py
│   │           │   ├── _writer.py
│   │           │   ├── annotations/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── _markup_annotations.py
│   │           │   │   └── _non_markup_annotations.py
│   │           │   ├── constants.py
│   │           │   ├── errors.py
│   │           │   ├── filters.py
│   │           │   ├── generic/
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _appearance_stream.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── _data_structures.py
│   │           │   │   ├── _files.py
│   │           │   │   ├── _fit.py
│   │           │   │   ├── _image_inline.py
│   │           │   │   ├── _image_xobject.py
│   │           │   │   ├── _link.py
│   │           │   │   ├── _outline.py
│   │           │   │   ├── _rectangle.py
│   │           │   │   ├── _utils.py
│   │           │   │   └── _viewerpref.py
│   │           │   ├── pagerange.py
│   │           │   ├── papersizes.py
│   │           │   ├── py.typed
│   │           │   ├── types.py
│   │           │   └── xmp.py
│   │           ├── pypdf-6.8.0.dist-info/
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   └── licenses/
│   │           │       └── LICENSE
│   │           └── pypdf2-3.0.1.dist-info/
│   │               ├── INSTALLER
│   │               ├── LICENSE
│   │               ├── METADATA
│   │               ├── RECORD
│   │               ├── REQUESTED
│   │               └── WHEEL
│   └── pyvenv.cfg
├── .worktrees/
│   └── phase-19-nav-refactor/
│       ├── .claude/
│       │   ├── agents/
│       │   │   ├── rag-reviewer.md
│       │   │   └── standards-lookup.md
│       │   ├── settings.json
│       │   └── skills/
│       │       ├── explain-code/
│       │       │   └── SKILL.md
│       │       ├── new-rag-module/
│       │       │   └── SKILL.md
│       │       ├── promote-draft/
│       │       │   └── SKILL.md
│       │       └── validate-rag/
│       │           └── SKILL.md
│       ├── .github/
│       │   └── workflows/
│       │       └── pages.yml
│       ├── .gitignore
│       ├── .mcp.json
│       ├── .python-version
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       ├── PROJECT_STARTUP_CONTEXT.md
│       ├── README.md
│       ├── STRUCTURE_SUMMARY.md
│       ├── control-standards/
│       │   ├── .gitignore
│       │   ├── QUICK_START.md
│       │   ├── README.md
│       │   ├── STRUCTURE_SUMMARY.md
│       │   ├── exports/
│       │   │   ├── README.md
│       │   │   └── legacy_root/
│       │   │       └── README.md
│       │   ├── governance/
│       │   │   ├── README.md
│       │   │   ├── decision_log.md
│       │   │   ├── design_change_policy.md
│       │   │   ├── promotion_checklist_drafts_to_rag.md
│       │   │   └── release_notes.md
│       │   ├── rag/
│       │   │   ├── commissioning_checklists/
│       │   │   │   ├── README.md
│       │   │   │   ├── _index.yaml
│       │   │   │   └── checklists/
│       │   │   │       ├── README.md
│       │   │   │       ├── _index.yaml
│       │   │   │       ├── basic_circuit_polarity_and_power_checks.md
│       │   │   │       ├── capacitor_discharge_awareness_check.md
│       │   │   │       ├── drive_commissioning.md
│       │   │   │       ├── motor_nameplate_and_overload_setting.md
│       │   │   │       ├── motor_rotation_and_overload_verification.md
│       │   │   │       └── pre_power_panel_and_incoming_supply_check.md
│       │   │   ├── design_framework/
│       │   │   │   ├── README.md
│       │   │   │   ├── _index.yaml
│       │   │   │   ├── constraints/
│       │   │   │   │   └── grounding_bonding_rules.yaml
│       │   │   │   ├── design_guides/
│       │   │   │   │   └── 02_power_distribution_guide.md
│       │   │   │   ├── electrical_review/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── _index.yaml
│       │   │   │   │   ├── basic_resistive_network_review.md
│       │   │   │   │   ├── component_selection_basics.md
│       │   │   │   │   ├── ohms_law_and_power_check_workflow.md
│       │   │   │   │   └── simple_signal_and_interface_circuit_notes.md
│       │   │   │   ├── motor_systems/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── _index.yaml
│       │   │   │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│       │   │   │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│       │   │   │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│       │   │   │   │   ├── integrated_motor_drive_architecture_comparison.md
│       │   │   │   │   ├── motor_cable_and_protection_review.md
│       │   │   │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│       │   │   │   │   ├── motor_nameplate_review_checklist.md
│       │   │   │   │   ├── motor_selection_comparison_matrix.md
│       │   │   │   │   ├── motor_selection_workflow.md
│       │   │   │   │   ├── motor_symptom_troubleshooting_patterns.md
│       │   │   │   │   ├── motor_troubleshooting_decision_tree.md
│       │   │   │   │   ├── servo_commissioning_workflow.md
│       │   │   │   │   ├── star_delta_and_supply_matching_notes.md
│       │   │   │   │   ├── vfd_commissioning_workflow.md
│       │   │   │   │   └── vfd_motor_integration_review.md
│       │   │   │   └── us_eu_compliance_wizard/
│       │   │   │       ├── README.md
│       │   │   │       ├── US_EU_Machine_Compliance_Wizard.md
│       │   │   │       ├── us_eu_delta_report_template.md
│       │   │   │       └── us_eu_wizard_rules.yaml
│       │   │   ├── meta/
│       │   │   │   ├── RAG_DIRECTORY_STATUS.md
│       │   │   │   └── VERSION_OVERVIEW.md
│       │   │   ├── standards_intelligence/
│       │   │   │   ├── README.md
│       │   │   │   ├── _glossary.md
│       │   │   │   ├── _index.yaml
│       │   │   │   ├── _standards_map.md
│       │   │   │   ├── crosswalks/
│       │   │   │   │   ├── overlap_matrix/
│       │   │   │   │   │   ├── _index.yaml
│       │   │   │   │   │   ├── file_structure.md
│       │   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│       │   │   │   │   │   ├── standards_decision_workflow.md
│       │   │   │   │   │   ├── standards_overlap.md
│       │   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│       │   │   │   │   └── overlap_notes/
│       │   │   │   │       ├── GENERATION_STATUS.md
│       │   │   │   │       ├── _index.yaml
│       │   │   │   │       ├── file_structure.md
│       │   │   │   │       ├── overlap__motors_drives.md
│       │   │   │   │       ├── overlap__sccr.md
│       │   │   │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│       │   │   │   ├── file_structure.md
│       │   │   │   ├── international/
│       │   │   │   │   ├── cybersecurity/
│       │   │   │   │   │   └── iec_62443/
│       │   │   │   │   │       ├── IEC62443_2_1__security_management.md
│       │   │   │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│       │   │   │   │   │       ├── IEC62443_4_2__component_requirements.md
│       │   │   │   │   │       ├── IEC62443_lifecycle.md
│       │   │   │   │   │       └── _index.yaml
│       │   │   │   │   ├── functional_safety/
│       │   │   │   │   │   ├── iec_61508/
│       │   │   │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│       │   │   │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│       │   │   │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│       │   │   │   │   │   │   ├── IEC61508_2010__Part3__software.md
│       │   │   │   │   │   │   └── _index.yaml
│       │   │   │   │   │   ├── iec_61511/
│       │   │   │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│       │   │   │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│       │   │   │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│       │   │   │   │   │   │   ├── IEC61511_2016__Part1__framework.md
│       │   │   │   │   │   │   └── _index.yaml
│       │   │   │   │   │   ├── iec_62061/
│       │   │   │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│       │   │   │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│       │   │   │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│       │   │   │   │   │   │   ├── IEC62061_2021__Clause07__subsystem_design.md
│       │   │   │   │   │   │   └── _index.yaml
│       │   │   │   │   │   ├── iso_12100/
│       │   │   │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│       │   │   │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│       │   │   │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│       │   │   │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│       │   │   │   │   │   │   ├── ISO12100_2010__Clause07__risk_reduction.md
│       │   │   │   │   │   │   └── _index.yaml
│       │   │   │   │   │   └── iso_13849_1/
│       │   │   │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│       │   │   │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│       │   │   │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│       │   │   │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│       │   │   │   │   │       ├── ISO13849_2023__Clause06__categories.md
│       │   │   │   │   │       ├── ISO13849_2023__Clause07__validation.md
│       │   │   │   │   │       └── _index.yaml
│       │   │   │   │   ├── hazardous_area/
│       │   │   │   │   │   └── iec_60079/
│       │   │   │   │   │       ├── IEC60079_0__general_requirements.md
│       │   │   │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│       │   │   │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│       │   │   │   │   │       ├── IEC60079_14__installation_design.md
│       │   │   │   │   │       ├── IEC60079_17__inspection_maintenance.md
│       │   │   │   │   │       ├── IEC60079_1__flameproof_Ex_d.md
│       │   │   │   │   │       └── _index.yaml
│       │   │   │   │   ├── machinery/
│       │   │   │   │   │   └── iec_60204_1/
│       │   │   │   │   │       ├── GENERATION_SUMMARY.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause01__scope.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause02__normative_references.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause04__general_requirements.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause05__incoming_supply.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause10__operator_interface.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause11__control_equipment.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│       │   │   │   │   │       ├── IEC60204_1_2018__Clause15__verification.md
│       │   │   │   │   │       ├── IEC60204_OVERVIEW.md
│       │   │   │   │   │       ├── README.md
│       │   │   │   │   │       └── _index.yaml
│       │   │   │   │   ├── offshore/
│       │   │   │   │   │   ├── ABS_offshore_electrical_control.md
│       │   │   │   │   │   ├── DNV_OS_D201__electrical_installations.md
│       │   │   │   │   │   └── _index.yaml
│       │   │   │   │   └── semiconductor/
│       │   │   │   │       └── semi/
│       │   │   │   │           ├── SEMI_S14__fire_risk_assessment.md
│       │   │   │   │           ├── SEMI_S2__equipment_safety.md
│       │   │   │   │           ├── SEMI_S8__ergonomics.md
│       │   │   │   │           └── _index.yaml
│       │   │   │   ├── library_admin/
│       │   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── STANDARDS_COMPLETION_STATUS.md
│       │   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│       │   │   │   │   └── STANDARDS_PURCHASE_TRACKER.md
│       │   │   │   ├── reference_models/
│       │   │   │   │   ├── 15-Standard Minimum Compliance Stack.md
│       │   │   │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│       │   │   │   │   ├── Universal Machine Safety Architecture.md
│       │   │   │   │   └── standards_atlas_diagrams_reference.md
│       │   │   │   ├── routing/
│       │   │   │   │   ├── README.md
│       │   │   │   │   └── standards_applicability.md
│       │   │   │   ├── scenario/
│       │   │   │   │   ├── cnc_machine_safety_design/
│       │   │   │   │   │   ├── README.md
│       │   │   │   │   │   ├── control_architecture_and_network.md
│       │   │   │   │   │   ├── hazards_and_risk_assessment.md
│       │   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│       │   │   │   │   │   ├── requirements.yaml
│       │   │   │   │   │   ├── safety_functions_register.md
│       │   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│       │   │   │   │   │   ├── standards_applicability_matrix.md
│       │   │   │   │   │   ├── system_description.md
│       │   │   │   │   │   ├── ul_nec_design_requirements.md
│       │   │   │   │   │   └── verification_and_validation_plan.md
│       │   │   │   │   ├── mini_machine_safety_design/
│       │   │   │   │   │   ├── README.md
│       │   │   │   │   │   ├── control_architecture_and_network.md
│       │   │   │   │   │   ├── hazards_and_risk_assessment.md
│       │   │   │   │   │   ├── industry_overlays/
│       │   │   │   │   │   │   ├── commercial.md
│       │   │   │   │   │   │   ├── energy.md
│       │   │   │   │   │   │   ├── food_and_beverage.md
│       │   │   │   │   │   │   ├── marine.md
│       │   │   │   │   │   │   ├── medical.md
│       │   │   │   │   │   │   ├── nuclear.md
│       │   │   │   │   │   │   ├── offshore.md
│       │   │   │   │   │   │   ├── petroleum.md
│       │   │   │   │   │   │   └── semiconductor.md
│       │   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│       │   │   │   │   │   ├── requirements.yaml
│       │   │   │   │   │   ├── safety_functions_register.md
│       │   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│       │   │   │   │   │   ├── standards_applicability_matrix.md
│       │   │   │   │   │   ├── system_description.md
│       │   │   │   │   │   ├── ul_nec_design_requirements.md
│       │   │   │   │   │   └── verification_and_validation_plan.md
│       │   │   │   │   └── mini_machine_safety_design_v2/
│       │   │   │   │       ├── README.md
│       │   │   │   │       ├── control_architecture_and_network.md
│       │   │   │   │       ├── hazards_and_risk_assessment.md
│       │   │   │   │       ├── industry_overlays/
│       │   │   │   │       │   ├── commercial.md
│       │   │   │   │       │   ├── energy.md
│       │   │   │   │       │   ├── food_and_beverage.md
│       │   │   │   │       │   ├── marine.md
│       │   │   │   │       │   ├── medical.md
│       │   │   │   │       │   ├── nuclear.md
│       │   │   │   │       │   ├── offshore.md
│       │   │   │   │       │   ├── petroleum.md
│       │   │   │   │       │   └── semiconductor.md
│       │   │   │   │       ├── mechanical_and_electrical_isolation.md
│       │   │   │   │       ├── requirements.yaml
│       │   │   │   │       ├── safety_functions_register.md
│       │   │   │   │       ├── safety_integrity_and_sil_strategy.md
│       │   │   │   │       ├── standards_applicability_matrix.md
│       │   │   │   │       ├── system_description.md
│       │   │   │   │       ├── ul_nec_design_requirements.md
│       │   │   │   │       └── verification_and_validation_plan.md
│       │   │   │   └── us/
│       │   │   │       ├── nec/
│       │   │   │       │   ├── GENERATION_SUMMARY.md
│       │   │   │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│       │   │   │       │   ├── NEC_2023__Art100__definitions.md
│       │   │   │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│       │   │   │       │   ├── NEC_2023__Art215__feeders.md
│       │   │   │       │   ├── NEC_2023__Art230__services.md
│       │   │   │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│       │   │   │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│       │   │   │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│       │   │   │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│       │   │   │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│       │   │   │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│       │   │   │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│       │   │   │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│       │   │   │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│       │   │   │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│       │   │   │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│       │   │   │       │   ├── NEC_2023__Art670__industrial_machinery.md
│       │   │   │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│       │   │   │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│       │   │   │       │   ├── NEC_COMPLETION_STATUS.md
│       │   │   │       │   ├── NEC_OVERVIEW.md
│       │   │   │       │   ├── README.md
│       │   │   │       │   └── _index.yaml
│       │   │   │       ├── nfpa79/
│       │   │   │       │   ├── GENERATION_SUMMARY.md
│       │   │   │       │   ├── NFPA79_2024__Ch01__administration.md
│       │   │   │       │   ├── NFPA79_2024__Ch02__definitions.md
│       │   │   │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│       │   │   │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│       │   │   │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│       │   │   │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│       │   │   │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│       │   │   │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│       │   │   │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│       │   │   │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│       │   │   │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│       │   │   │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│       │   │   │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│       │   │   │       │   ├── NFPA79_2024__Ch14__lighting.md
│       │   │   │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│       │   │   │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│       │   │   │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│       │   │   │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│       │   │   │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│       │   │   │       │   ├── NFPA79_2024__Ch20__system_integration.md
│       │   │   │       │   ├── NFPA_OVERVIEW.md
│       │   │   │       │   ├── README.md
│       │   │   │       │   └── _index.yaml
│       │   │   │       └── ul_508a/
│       │   │   │           ├── GENERATION_SUMMARY.md
│       │   │   │           ├── README.md
│       │   │   │           ├── UL508A_2022__control_circuits_and_devices.md
│       │   │   │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│       │   │   │           ├── UL508A_2022__general_construction_requirements.md
│       │   │   │           ├── UL508A_2022__grounding_and_bonding.md
│       │   │   │           ├── UL508A_2022__marking_and_documentation.md
│       │   │   │           ├── UL508A_2022__motor_controllers_and_drives.md
│       │   │   │           ├── UL508A_2022__overcurrent_protection.md
│       │   │   │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│       │   │   │           ├── UL508A_2022__scope_and_application.md
│       │   │   │           ├── UL508A_2022__spacing_creepage_clearance.md
│       │   │   │           ├── UL508A_2022__transformers_and_power_supplies.md
│       │   │   │           ├── UL508A_2022__wiring_methods_and_conductors.md
│       │   │   │           ├── UL508A_OVERVIEW.md
│       │   │   │           └── _index.yaml
│       │   │   ├── training_modules/
│       │   │   │   ├── README.md
│       │   │   │   ├── _index.yaml
│       │   │   │   ├── control_systems/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── _index.yaml
│       │   │   │   │   ├── control_theory_overview.md
│       │   │   │   │   ├── industrial_control_loop_architectures.md
│       │   │   │   │   ├── industrial_pid_implementation.md
│       │   │   │   │   ├── pid_control_intuition.md
│       │   │   │   │   ├── pid_control_intuitive_foundation.md
│       │   │   │   │   ├── pid_drone_control.md
│       │   │   │   │   └── pid_heater_control_with_contactor.md
│       │   │   │   ├── electrical_machines/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── _index.yaml
│       │   │   │   │   ├── ac_vs_dc_motor_comparison.md
│       │   │   │   │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│       │   │   │   │   ├── dc_motor_basics.md
│       │   │   │   │   ├── induction_motor_basics.md
│       │   │   │   │   ├── motor_and_vfd_equations_reference.md
│       │   │   │   │   ├── motor_control_methods_and_operating_regions.md
│       │   │   │   │   ├── motor_efficiency_power_factor_and_losses.md
│       │   │   │   │   ├── motor_family_comparison.md
│       │   │   │   │   ├── motor_nameplates_slip_and_torque.md
│       │   │   │   │   ├── servo_drive_fundamentals.md
│       │   │   │   │   ├── servo_feedback_and_inertia_matching.md
│       │   │   │   │   ├── vfd_and_servo_architecture_diagrams.md
│       │   │   │   │   └── vfd_fundamentals.md
│       │   │   │   ├── fundamentals/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── _index.yaml
│       │   │   │   │   ├── conductor_ampacity_and_termination_temperature.md
│       │   │   │   │   ├── diodes_transistors_and_switching_basics.md
│       │   │   │   │   ├── earthing_systems_iec.md
│       │   │   │   │   ├── electrical_equations_reference.md
│       │   │   │   │   ├── electrical_quantities_and_circuit_language.md
│       │   │   │   │   ├── equivalent_circuit_methods.md
│       │   │   │   │   ├── kirchhoff_laws_and_systematic_analysis.md
│       │   │   │   │   ├── passive_components_resistors_capacitors.md
│       │   │   │   │   └── series_parallel_and_divider_methods.md
│       │   │   │   └── nec_application/
│       │   │   │       ├── README.md
│       │   │   │       ├── _index.yaml
│       │   │   │       ├── article_409_practical_workflow.md
│       │   │   │       ├── article_430_practical_workflow.md
│       │   │   │       ├── branch_circuits_vs_feeders_motor_loads.md
│       │   │   │       ├── class1_class2_remote_control_circuits.md
│       │   │   │       ├── conductor_ocpd_sizing_examples.md
│       │   │   │       ├── disconnecting_means_for_machinery.md
│       │   │   │       ├── grounding_bonding_control_panels.md
│       │   │   │       ├── motor_and_panel_code_application.md
│       │   │   │       ├── nec_code_reading_fundamentals.md
│       │   │   │       ├── sccr_workflow.md
│       │   │   │       └── working_space_and_table_navigation.md
│       │   │   └── troubleshooting_engine/
│       │   │       └── decision_trees.yaml
│       │   ├── templates/
│       │   │   ├── README.md
│       │   │   ├── checklists/
│       │   │   │   └── checklist_template.md
│       │   │   ├── design_guides/
│       │   │   │   └── design_guide_template.md
│       │   │   ├── md_headers/
│       │   │   │   ├── archived_header.md
│       │   │   │   ├── draft_only_header.md
│       │   │   │   └── rag_approved_header.md
│       │   │   ├── reports/
│       │   │   │   └── report_template.md
│       │   │   └── work_notes/
│       │   │       └── work_note_template.md
│       │   ├── tools/
│       │   │   ├── audit_tool/
│       │   │   │   └── README.md
│       │   │   ├── business_metrics_profit_engine/
│       │   │   │   └── README.md
│       │   │   ├── design_package_generator/
│       │   │   │   └── README.md
│       │   │   ├── ip_library_licensing/
│       │   │   │   └── README.md
│       │   │   ├── knowledge_platform/
│       │   │   │   └── README.md
│       │   │   ├── retainer_support_engine/
│       │   │   │   └── README.md
│       │   │   └── ul508a_panel_automation/
│       │   │       └── README.md
│       │   └── work/
│       │       ├── README.md
│       │       ├── design/
│       │       │   ├── 2026 NEC Changes.md
│       │       │   ├── README.md
│       │       │   ├── conductor_protection_and_ampacity_transcript_summary.md
│       │       │   ├── control theory.md
│       │       │   ├── electrical exam prep.md
│       │       │   ├── equipment_grounding_conductor_topics/
│       │       │   │   ├── README.md
│       │       │   │   ├── egc_cable_methods_ac_and_mc.md
│       │       │   │   ├── egc_definition_and_effective_fault_path.md
│       │       │   │   ├── egc_other_listed_systems.md
│       │       │   │   ├── egc_sizing_and_250_122_notes.md
│       │       │   │   └── egc_wire_and_raceway_methods.md
│       │       │   ├── mermaid_diagrams_to_reference.md
│       │       │   ├── mini_machine_safety_design_v2_project_status.md
│       │       │   ├── nec_2026_changes_topics/
│       │       │   │   ├── 2026_nec_codewide_editorial_and_90_3_changes.md
│       │       │   │   ├── 2026_nec_limited_energy_restructure.md
│       │       │   │   ├── 2026_nec_medium_voltage_restructure.md
│       │       │   │   ├── 2026_nec_new_and_relocated_articles.md
│       │       │   │   ├── 2026_nec_overview_and_2029_transition.md
│       │       │   │   └── README.md
│       │       │   ├── nec_210_4_multiwire_branch_circuits_transcript_summary.md
│       │       │   ├── nec_update.md
│       │       │   ├── project_implementation_gaps/
│       │       │   │   ├── 20260308_status.md
│       │       │   │   ├── electrical and practical circuit analysis.md
│       │       │   │   ├── electrical_and_practical_circuit_analysis_topics/
│       │       │   │   │   ├── INTEGRATION_PLAN.md
│       │       │   │   │   ├── README.md
│       │       │   │   │   ├── circuit_analysis_overview_and_linear_elements.md
│       │       │   │   │   ├── equivalent_circuit_methods_topics/
│       │       │   │   │   │   ├── README.md
│       │       │   │   │   │   ├── norton_equivalent_method.md
│       │       │   │   │   │   ├── source_transformation_basics.md
│       │       │   │   │   │   ├── superposition_theorem_notes.md
│       │       │   │   │   │   └── thevenin_equivalent_method.md
│       │       │   │   │   ├── kcl_and_nodal_analysis.md
│       │       │   │   │   ├── kvl_and_loop_analysis.md
│       │       │   │   │   ├── practical_components_diodes_and_transistors.md
│       │       │   │   │   ├── practical_components_resistors_and_capacitors.md
│       │       │   │   │   ├── practical_ohms_law_power_and_resistor_color_code.md
│       │       │   │   │   ├── series_parallel_and_divider_methods.md
│       │       │   │   │   └── source_transformation_and_equivalent_methods.md
│       │       │   │   ├── importance of electrical safety in control panels.md
│       │       │   │   ├── motors.md
│       │       │   │   ├── motors_topics/
│       │       │   │   │   ├── INTEGRATION_PLAN.md
│       │       │   │   │   ├── README.md
│       │       │   │   │   ├── dc_motor_armature_winding_and_torque_production.md
│       │       │   │   │   ├── dc_motor_commutator_brushes_and_power_path.md
│       │       │   │   │   ├── dc_motor_magnetism_stator_and_mechanical_structure.md
│       │       │   │   │   ├── ev_motor_powertrain_configurations.md
│       │       │   │   │   ├── ev_motor_types_overview.md
│       │       │   │   │   ├── induction_motor_components_induction_and_slip.md
│       │       │   │   │   ├── induction_motor_construction_and_rotating_field.md
│       │       │   │   │   ├── induction_motor_nameplate_and_enclosures.md
│       │       │   │   │   ├── induction_motor_poles_torque_curves_and_nema_designs.md
│       │       │   │   │   └── induction_motor_terminal_connections_and_star_delta.md
│       │       │   │   ├── nec_exam_prep_topics/
│       │       │   │   │   ├── INTEGRATION_PLAN.md
│       │       │   │   │   ├── README.md
│       │       │   │   │   ├── electrical_exam_math_ohms_law_and_power.md
│       │       │   │   │   ├── nec_code_reading_and_index_method.md
│       │       │   │   │   ├── nec_table_reading_and_working_space_example.md
│       │       │   │   │   └── residential_load_calculation_notes.md
│       │       │   │   └── temp links.md
│       │       │   ├── residential_nec_top_articles_transcript_summary.md
│       │       │   ├── scratch_notes/
│       │       │   │   └── simple_safety_system_design.md
│       │       │   ├── types of equipment ground conductors.md
│       │       │   ├── types of grounding.md
│       │       │   └── voltage_drop_topics/
│       │       │       ├── README.md
│       │       │       ├── voltage_drop_energy_code_and_specifications.md
│       │       │       ├── voltage_drop_fire_pump_notes.md
│       │       │       ├── voltage_drop_general_basis.md
│       │       │       └── voltage_drop_recommended_feeder_and_branch_guidance.md
│       │       └── general/
│       │           ├── 00_inbox_notes.md
│       │           └── README.md
│       ├── data/
│       │   └── README.md
│       ├── docs/
│       │   ├── .bundle/
│       │   │   └── config
│       │   ├── Gemfile
│       │   ├── Gemfile.lock
│       │   ├── _config.yml
│       │   ├── _data/
│       │   │   ├── field_checklists.yml
│       │   │   ├── glossary.yml
│       │   │   ├── navigation.yml
│       │   │   ├── rag_tree.json
│       │   │   ├── standards_graph.yml
│       │   │   └── training_catalog.yml
│       │   ├── _includes/
│       │   │   ├── context-panel.html
│       │   │   ├── rag-tree-nodes.html
│       │   │   ├── sidebar.html
│       │   │   ├── standards-graph.html
│       │   │   ├── topnav.html
│       │   │   └── trust-boundary.html
│       │   ├── _layouts/
│       │   │   ├── default.html
│       │   │   ├── field-checklist.html
│       │   │   ├── rag-browser.html
│       │   │   └── training-module.html
│       │   ├── about/
│       │   │   └── index.md
│       │   ├── assets/
│       │   │   ├── css/
│       │   │   │   └── main.css
│       │   │   ├── data/
│       │   │   │   └── search.json
│       │   │   ├── img/
│       │   │   │   └── favicon.svg
│       │   │   ├── js/
│       │   │   │   ├── main.js
│       │   │   │   └── rag-browser.js
│       │   │   └── rag-files/
│       │   │       ├── commissioning_checklists/
│       │   │       │   └── checklists/
│       │   │       │       ├── basic_circuit_polarity_and_power_checks.md
│       │   │       │       ├── capacitor_discharge_awareness_check.md
│       │   │       │       ├── drive_commissioning.md
│       │   │       │       ├── motor_nameplate_and_overload_setting.md
│       │   │       │       ├── motor_rotation_and_overload_verification.md
│       │   │       │       └── pre_power_panel_and_incoming_supply_check.md
│       │   │       ├── design_framework/
│       │   │       │   ├── design_guides/
│       │   │       │   │   └── 02_power_distribution_guide.md
│       │   │       │   ├── electrical_review/
│       │   │       │   │   ├── basic_resistive_network_review.md
│       │   │       │   │   ├── component_selection_basics.md
│       │   │       │   │   ├── ohms_law_and_power_check_workflow.md
│       │   │       │   │   └── simple_signal_and_interface_circuit_notes.md
│       │   │       │   ├── motor_systems/
│       │   │       │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│       │   │       │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│       │   │       │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│       │   │       │   │   ├── integrated_motor_drive_architecture_comparison.md
│       │   │       │   │   ├── motor_cable_and_protection_review.md
│       │   │       │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│       │   │       │   │   ├── motor_nameplate_review_checklist.md
│       │   │       │   │   ├── motor_selection_comparison_matrix.md
│       │   │       │   │   ├── motor_selection_workflow.md
│       │   │       │   │   ├── motor_symptom_troubleshooting_patterns.md
│       │   │       │   │   ├── motor_troubleshooting_decision_tree.md
│       │   │       │   │   ├── servo_commissioning_workflow.md
│       │   │       │   │   ├── star_delta_and_supply_matching_notes.md
│       │   │       │   │   ├── vfd_commissioning_workflow.md
│       │   │       │   │   └── vfd_motor_integration_review.md
│       │   │       │   └── us_eu_compliance_wizard/
│       │   │       │       ├── US_EU_Machine_Compliance_Wizard.md
│       │   │       │       └── us_eu_delta_report_template.md
│       │   │       ├── meta/
│       │   │       │   ├── RAG_DIRECTORY_STATUS.md
│       │   │       │   └── VERSION_OVERVIEW.md
│       │   │       ├── standards_intelligence/
│       │   │       │   ├── _glossary.md
│       │   │       │   ├── _standards_map.md
│       │   │       │   ├── crosswalks/
│       │   │       │   │   ├── overlap_matrix/
│       │   │       │   │   │   ├── file_structure.md
│       │   │       │   │   │   ├── nfpa79_iec60204_overlap.md
│       │   │       │   │   │   ├── standards_decision_workflow.md
│       │   │       │   │   │   ├── standards_overlap.md
│       │   │       │   │   │   └── ul508a_nec_nfpa79_overlap.md
│       │   │       │   │   └── overlap_notes/
│       │   │       │   │       ├── GENERATION_STATUS.md
│       │   │       │   │       ├── file_structure.md
│       │   │       │   │       ├── overlap__motors_drives.md
│       │   │       │   │       ├── overlap__sccr.md
│       │   │       │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│       │   │       │   ├── file_structure.md
│       │   │       │   ├── international/
│       │   │       │   │   ├── cybersecurity/
│       │   │       │   │   │   └── iec_62443/
│       │   │       │   │   │       ├── IEC62443_2_1__security_management.md
│       │   │       │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│       │   │       │   │   │       ├── IEC62443_4_2__component_requirements.md
│       │   │       │   │   │       └── IEC62443_lifecycle.md
│       │   │       │   │   ├── functional_safety/
│       │   │       │   │   │   ├── iec_61508/
│       │   │       │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│       │   │       │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│       │   │       │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│       │   │       │   │   │   │   └── IEC61508_2010__Part3__software.md
│       │   │       │   │   │   ├── iec_61511/
│       │   │       │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│       │   │       │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│       │   │       │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│       │   │       │   │   │   │   └── IEC61511_2016__Part1__framework.md
│       │   │       │   │   │   ├── iec_62061/
│       │   │       │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│       │   │       │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│       │   │       │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│       │   │       │   │   │   │   └── IEC62061_2021__Clause07__subsystem_design.md
│       │   │       │   │   │   ├── iso_12100/
│       │   │       │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│       │   │       │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│       │   │       │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│       │   │       │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│       │   │       │   │   │   │   └── ISO12100_2010__Clause07__risk_reduction.md
│       │   │       │   │   │   └── iso_13849_1/
│       │   │       │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│       │   │       │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│       │   │       │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│       │   │       │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│       │   │       │   │   │       ├── ISO13849_2023__Clause06__categories.md
│       │   │       │   │   │       └── ISO13849_2023__Clause07__validation.md
│       │   │       │   │   ├── hazardous_area/
│       │   │       │   │   │   └── iec_60079/
│       │   │       │   │   │       ├── IEC60079_0__general_requirements.md
│       │   │       │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│       │   │       │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│       │   │       │   │   │       ├── IEC60079_14__installation_design.md
│       │   │       │   │   │       ├── IEC60079_17__inspection_maintenance.md
│       │   │       │   │   │       └── IEC60079_1__flameproof_Ex_d.md
│       │   │       │   │   ├── machinery/
│       │   │       │   │   │   └── iec_60204_1/
│       │   │       │   │   │       ├── GENERATION_SUMMARY.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause01__scope.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause02__normative_references.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause04__general_requirements.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause05__incoming_supply.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause10__operator_interface.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause11__control_equipment.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│       │   │       │   │   │       ├── IEC60204_1_2018__Clause15__verification.md
│       │   │       │   │   │       └── IEC60204_OVERVIEW.md
│       │   │       │   │   ├── offshore/
│       │   │       │   │   │   ├── ABS_offshore_electrical_control.md
│       │   │       │   │   │   └── DNV_OS_D201__electrical_installations.md
│       │   │       │   │   └── semiconductor/
│       │   │       │   │       └── semi/
│       │   │       │   │           ├── SEMI_S14__fire_risk_assessment.md
│       │   │       │   │           ├── SEMI_S2__equipment_safety.md
│       │   │       │   │           └── SEMI_S8__ergonomics.md
│       │   │       │   ├── library_admin/
│       │   │       │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│       │   │       │   │   ├── STANDARDS_COMPLETION_STATUS.md
│       │   │       │   │   ├── STANDARDS_MODULES_SUMMARY.md
│       │   │       │   │   └── STANDARDS_PURCHASE_TRACKER.md
│       │   │       │   ├── reference_models/
│       │   │       │   │   ├── 15-Standard Minimum Compliance Stack.md
│       │   │       │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│       │   │       │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│       │   │       │   │   ├── Universal Machine Safety Architecture.md
│       │   │       │   │   └── standards_atlas_diagrams_reference.md
│       │   │       │   ├── routing/
│       │   │       │   │   └── standards_applicability.md
│       │   │       │   ├── scenario/
│       │   │       │   │   ├── cnc_machine_safety_design/
│       │   │       │   │   │   ├── control_architecture_and_network.md
│       │   │       │   │   │   ├── hazards_and_risk_assessment.md
│       │   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│       │   │       │   │   │   ├── safety_functions_register.md
│       │   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│       │   │       │   │   │   ├── standards_applicability_matrix.md
│       │   │       │   │   │   ├── system_description.md
│       │   │       │   │   │   ├── ul_nec_design_requirements.md
│       │   │       │   │   │   └── verification_and_validation_plan.md
│       │   │       │   │   ├── mini_machine_safety_design/
│       │   │       │   │   │   ├── control_architecture_and_network.md
│       │   │       │   │   │   ├── hazards_and_risk_assessment.md
│       │   │       │   │   │   ├── industry_overlays/
│       │   │       │   │   │   │   ├── commercial.md
│       │   │       │   │   │   │   ├── energy.md
│       │   │       │   │   │   │   ├── food_and_beverage.md
│       │   │       │   │   │   │   ├── marine.md
│       │   │       │   │   │   │   ├── medical.md
│       │   │       │   │   │   │   ├── nuclear.md
│       │   │       │   │   │   │   ├── offshore.md
│       │   │       │   │   │   │   ├── petroleum.md
│       │   │       │   │   │   │   └── semiconductor.md
│       │   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│       │   │       │   │   │   ├── safety_functions_register.md
│       │   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│       │   │       │   │   │   ├── standards_applicability_matrix.md
│       │   │       │   │   │   ├── system_description.md
│       │   │       │   │   │   ├── ul_nec_design_requirements.md
│       │   │       │   │   │   └── verification_and_validation_plan.md
│       │   │       │   │   └── mini_machine_safety_design_v2/
│       │   │       │   │       ├── control_architecture_and_network.md
│       │   │       │   │       ├── hazards_and_risk_assessment.md
│       │   │       │   │       ├── industry_overlays/
│       │   │       │   │       │   ├── commercial.md
│       │   │       │   │       │   ├── energy.md
│       │   │       │   │       │   ├── food_and_beverage.md
│       │   │       │   │       │   ├── marine.md
│       │   │       │   │       │   ├── medical.md
│       │   │       │   │       │   ├── nuclear.md
│       │   │       │   │       │   ├── offshore.md
│       │   │       │   │       │   ├── petroleum.md
│       │   │       │   │       │   └── semiconductor.md
│       │   │       │   │       ├── mechanical_and_electrical_isolation.md
│       │   │       │   │       ├── safety_functions_register.md
│       │   │       │   │       ├── safety_integrity_and_sil_strategy.md
│       │   │       │   │       ├── standards_applicability_matrix.md
│       │   │       │   │       ├── system_description.md
│       │   │       │   │       ├── ul_nec_design_requirements.md
│       │   │       │   │       └── verification_and_validation_plan.md
│       │   │       │   └── us/
│       │   │       │       ├── nec/
│       │   │       │       │   ├── GENERATION_SUMMARY.md
│       │   │       │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│       │   │       │       │   ├── NEC_2023__Art100__definitions.md
│       │   │       │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│       │   │       │       │   ├── NEC_2023__Art215__feeders.md
│       │   │       │       │   ├── NEC_2023__Art230__services.md
│       │   │       │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│       │   │       │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│       │   │       │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│       │   │       │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│       │   │       │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│       │   │       │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│       │   │       │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│       │   │       │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│       │   │       │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│       │   │       │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│       │   │       │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│       │   │       │       │   ├── NEC_2023__Art670__industrial_machinery.md
│       │   │       │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│       │   │       │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│       │   │       │       │   ├── NEC_COMPLETION_STATUS.md
│       │   │       │       │   └── NEC_OVERVIEW.md
│       │   │       │       ├── nfpa79/
│       │   │       │       │   ├── GENERATION_SUMMARY.md
│       │   │       │       │   ├── NFPA79_2024__Ch01__administration.md
│       │   │       │       │   ├── NFPA79_2024__Ch02__definitions.md
│       │   │       │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│       │   │       │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│       │   │       │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│       │   │       │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│       │   │       │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│       │   │       │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│       │   │       │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│       │   │       │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│       │   │       │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│       │   │       │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│       │   │       │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│       │   │       │       │   ├── NFPA79_2024__Ch14__lighting.md
│       │   │       │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│       │   │       │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│       │   │       │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│       │   │       │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│       │   │       │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│       │   │       │       │   ├── NFPA79_2024__Ch20__system_integration.md
│       │   │       │       │   └── NFPA_OVERVIEW.md
│       │   │       │       └── ul_508a/
│       │   │       │           ├── GENERATION_SUMMARY.md
│       │   │       │           ├── UL508A_2022__control_circuits_and_devices.md
│       │   │       │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│       │   │       │           ├── UL508A_2022__general_construction_requirements.md
│       │   │       │           ├── UL508A_2022__grounding_and_bonding.md
│       │   │       │           ├── UL508A_2022__marking_and_documentation.md
│       │   │       │           ├── UL508A_2022__motor_controllers_and_drives.md
│       │   │       │           ├── UL508A_2022__overcurrent_protection.md
│       │   │       │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│       │   │       │           ├── UL508A_2022__scope_and_application.md
│       │   │       │           ├── UL508A_2022__spacing_creepage_clearance.md
│       │   │       │           ├── UL508A_2022__transformers_and_power_supplies.md
│       │   │       │           ├── UL508A_2022__wiring_methods_and_conductors.md
│       │   │       │           └── UL508A_OVERVIEW.md
│       │   │       └── training_modules/
│       │   │           ├── control_systems/
│       │   │           │   ├── control_theory_overview.md
│       │   │           │   ├── industrial_control_loop_architectures.md
│       │   │           │   ├── industrial_pid_implementation.md
│       │   │           │   ├── pid_control_intuition.md
│       │   │           │   ├── pid_control_intuitive_foundation.md
│       │   │           │   ├── pid_drone_control.md
│       │   │           │   └── pid_heater_control_with_contactor.md
│       │   │           ├── electrical_machines/
│       │   │           │   ├── ac_vs_dc_motor_comparison.md
│       │   │           │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│       │   │           │   ├── dc_motor_basics.md
│       │   │           │   ├── induction_motor_basics.md
│       │   │           │   ├── motor_and_vfd_equations_reference.md
│       │   │           │   ├── motor_control_methods_and_operating_regions.md
│       │   │           │   ├── motor_efficiency_power_factor_and_losses.md
│       │   │           │   ├── motor_family_comparison.md
│       │   │           │   ├── motor_nameplates_slip_and_torque.md
│       │   │           │   ├── servo_drive_fundamentals.md
│       │   │           │   ├── servo_feedback_and_inertia_matching.md
│       │   │           │   ├── vfd_and_servo_architecture_diagrams.md
│       │   │           │   └── vfd_fundamentals.md
│       │   │           ├── fundamentals/
│       │   │           │   ├── conductor_ampacity_and_termination_temperature.md
│       │   │           │   ├── diodes_transistors_and_switching_basics.md
│       │   │           │   ├── earthing_systems_iec.md
│       │   │           │   ├── electrical_equations_reference.md
│       │   │           │   ├── electrical_quantities_and_circuit_language.md
│       │   │           │   ├── equivalent_circuit_methods.md
│       │   │           │   ├── kirchhoff_laws_and_systematic_analysis.md
│       │   │           │   ├── passive_components_resistors_capacitors.md
│       │   │           │   └── series_parallel_and_divider_methods.md
│       │   │           └── nec_application/
│       │   │               ├── article_409_practical_workflow.md
│       │   │               ├── article_430_practical_workflow.md
│       │   │               ├── branch_circuits_vs_feeders_motor_loads.md
│       │   │               ├── class1_class2_remote_control_circuits.md
│       │   │               ├── conductor_ocpd_sizing_examples.md
│       │   │               ├── disconnecting_means_for_machinery.md
│       │   │               ├── grounding_bonding_control_panels.md
│       │   │               ├── motor_and_panel_code_application.md
│       │   │               ├── nec_code_reading_fundamentals.md
│       │   │               ├── sccr_workflow.md
│       │   │               └── working_space_and_table_navigation.md
│       │   ├── crosswalks/
│       │   │   ├── compare/
│       │   │   │   └── index.md
│       │   │   ├── iec60079-nec-500-505/
│       │   │   │   └── index.md
│       │   │   ├── iec61511-iec61508/
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── nfpa79-iec60204/
│       │   │   │   └── index.md
│       │   │   ├── standards-decision-workflow/
│       │   │   │   └── index.md
│       │   │   └── ul508a-nec-nfpa79/
│       │   │       └── index.md
│       │   ├── engineering-workflow/
│       │   │   └── index.md
│       │   ├── field-engineering/
│       │   │   ├── basic-circuit-polarity/
│       │   │   │   └── index.md
│       │   │   ├── capacitor-discharge/
│       │   │   │   └── index.md
│       │   │   ├── drive-commissioning/
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── motor-nameplate-overload/
│       │   │   │   └── index.md
│       │   │   ├── motor-rotation-verification/
│       │   │   │   └── index.md
│       │   │   └── pre-power-panel/
│       │   │       └── index.md
│       │   ├── glossary/
│       │   │   └── index.md
│       │   ├── index.md
│       │   ├── industries/
│       │   │   ├── commercial/
│       │   │   │   └── index.md
│       │   │   ├── energy/
│       │   │   │   └── index.md
│       │   │   ├── food-and-beverage/
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── marine/
│       │   │   │   └── index.md
│       │   │   ├── medical/
│       │   │   │   └── index.md
│       │   │   ├── nuclear/
│       │   │   │   └── index.md
│       │   │   ├── offshore/
│       │   │   │   └── index.md
│       │   │   ├── petroleum/
│       │   │   │   └── index.md
│       │   │   └── semiconductor/
│       │   │       └── index.md
│       │   ├── lifecycle/
│       │   │   ├── build/
│       │   │   │   └── index.md
│       │   │   ├── commissioning/
│       │   │   │   └── index.md
│       │   │   ├── concept/
│       │   │   │   └── index.md
│       │   │   ├── detailed-design/
│       │   │   │   └── index.md
│       │   │   ├── draft-documentation/
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── installation/
│       │   │   │   └── index.md
│       │   │   ├── maintenance/
│       │   │   │   └── index.md
│       │   │   ├── pre-commissioning/
│       │   │   │   └── index.md
│       │   │   ├── risk-assessment/
│       │   │   │   └── index.md
│       │   │   ├── safety-architecture/
│       │   │   │   └── index.md
│       │   │   ├── safety-wiring/
│       │   │   │   └── index.md
│       │   │   └── standards-selection/
│       │   │       └── index.md
│       │   ├── plans/
│       │   │   ├── 2026-03-05-phase2-design.md
│       │   │   ├── 2026-03-05-phase2-implementation.md
│       │   │   ├── 2026-03-06-phase3-functional-safety-design.md
│       │   │   ├── 2026-03-06-phase3-implementation.md
│       │   │   ├── 2026-03-08-corpus-gap-fill-design.md
│       │   │   ├── 2026-03-08-decision-workflow-enhancements.md
│       │   │   ├── 2026-03-08-electrical-intelligence-integration-design.md
│       │   │   ├── 2026-03-08-electrical-intelligence-integration-plan.md
│       │   │   ├── 2026-03-08-glossary-design.md
│       │   │   ├── 2026-03-08-glossary-implementation.md
│       │   │   ├── 2026-03-08-nec-missing-articles.md
│       │   │   ├── 2026-03-08-nec-page-update.md
│       │   │   ├── 2026-03-08-phase10-corpus-gap-fill.md
│       │   │   ├── 2026-03-08-phase11-industry-overlay-depth-design.md
│       │   │   ├── 2026-03-08-phase11-industry-overlay-depth.md
│       │   │   ├── 2026-03-08-phase9-standards-graph.md
│       │   │   ├── 2026-03-08-standards-graph-design.md
│       │   │   ├── 2026-03-08-theme-switching-design.md
│       │   │   ├── 2026-03-08-theme-switching-implementation.md
│       │   │   ├── 2026-03-09-phase12-offshore-marine-overlay.md
│       │   │   ├── 2026-03-09-rag-browser-design.md
│       │   │   ├── 2026-03-09-training-site-pages-design.md
│       │   │   ├── 2026-03-09-training-site-pages-plan.md
│       │   │   ├── 2026-03-10-phase14-training-curriculum-design.md
│       │   │   ├── 2026-03-10-phase14-training-curriculum-implementation.md
│       │   │   ├── 2026-03-10-phase15-training-module-ux.md
│       │   │   ├── 2026-03-10-phase16-nec-training-expansion.md
│       │   │   ├── 2026-03-10-training-system-integration-preplan.md
│       │   │   ├── 2026-03-11-phase17-cross-layer-routing.md
│       │   │   ├── 2026-03-11-phase18-control-systems-training.md
│       │   │   └── 2026-03-13-phase19-engineering-workflow-navigation.md
│       │   ├── rag-browser/
│       │   │   └── index.md
│       │   ├── reference/
│       │   ├── scenarios/
│       │   │   ├── global-machine/
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── machine-safety-implementation/
│       │   │   │   └── index.md
│       │   │   ├── networked-safety-plc/
│       │   │   │   └── index.md
│       │   │   ├── offshore-platform-control/
│       │   │   │   └── index.md
│       │   │   ├── oil-gas-process-skid/
│       │   │   │   └── index.md
│       │   │   ├── process-skid/
│       │   │   │   └── index.md
│       │   │   ├── semiconductor-equipment/
│       │   │   │   └── index.md
│       │   │   ├── semiconductor-fab-tool/
│       │   │   │   └── index.md
│       │   │   └── us-industrial-control-panel/
│       │   │       └── index.md
│       │   ├── software-stack/
│       │   │   └── index.md
│       │   ├── standards/
│       │   │   ├── cybersecurity/
│       │   │   │   ├── iec-62443/
│       │   │   │   │   └── index.md
│       │   │   │   └── index.md
│       │   │   ├── functional-safety/
│       │   │   │   ├── iec-61508/
│       │   │   │   │   └── index.md
│       │   │   │   ├── iec-61511/
│       │   │   │   │   └── index.md
│       │   │   │   ├── iec-62061/
│       │   │   │   │   └── index.md
│       │   │   │   ├── index.md
│       │   │   │   ├── iso-12100/
│       │   │   │   │   └── index.md
│       │   │   │   └── iso-13849-1/
│       │   │   │       └── index.md
│       │   │   ├── graph/
│       │   │   │   └── index.md
│       │   │   ├── hazardous-area/
│       │   │   │   ├── iec-60079/
│       │   │   │   │   └── index.md
│       │   │   │   └── index.md
│       │   │   ├── index.md
│       │   │   ├── machinery/
│       │   │   │   ├── iec-60204-1/
│       │   │   │   │   └── index.md
│       │   │   │   └── index.md
│       │   │   ├── semiconductor/
│       │   │   │   ├── index.md
│       │   │   │   └── semi/
│       │   │   │       └── index.md
│       │   │   └── us-electrical/
│       │   │       ├── index.md
│       │   │       ├── nec/
│       │   │       │   └── index.md
│       │   │       ├── nfpa-79/
│       │   │       │   └── index.md
│       │   │       └── ul-508a/
│       │   │           └── index.md
│       │   ├── superpowers/
│       │   │   ├── plans/
│       │   │   │   ├── 2026-03-12-fe-study-bugfixes.md
│       │   │   │   ├── 2026-03-13-doc-support.md
│       │   │   │   └── 2026-03-13-field-engineering.md
│       │   │   └── specs/
│       │   │       ├── 2026-03-12-doc-support-design.md
│       │   │       ├── 2026-03-13-field-engineering-design.md
│       │   │       └── 2026-03-14-reference-section-commissioning-templates-design.md
│       │   ├── training/
│       │   │   ├── control-systems/
│       │   │   │   ├── control-loop-architectures/
│       │   │   │   │   └── index.md
│       │   │   │   ├── control-theory-overview/
│       │   │   │   │   └── index.md
│       │   │   │   ├── index.md
│       │   │   │   ├── industrial-pid/
│       │   │   │   │   └── index.md
│       │   │   │   ├── pid-drone-control/
│       │   │   │   │   └── index.md
│       │   │   │   ├── pid-foundation/
│       │   │   │   │   └── index.md
│       │   │   │   ├── pid-heater-control/
│       │   │   │   │   └── index.md
│       │   │   │   └── pid-intuition/
│       │   │   │       └── index.md
│       │   │   ├── electrical-machines/
│       │   │   │   ├── ac-vs-dc-motors/
│       │   │   │   │   └── index.md
│       │   │   │   ├── bldc-ev-drone-motors/
│       │   │   │   │   └── index.md
│       │   │   │   ├── dc-motor-basics/
│       │   │   │   │   └── index.md
│       │   │   │   ├── index.md
│       │   │   │   ├── induction-motor-basics/
│       │   │   │   │   └── index.md
│       │   │   │   ├── motor-control-methods/
│       │   │   │   │   └── index.md
│       │   │   │   ├── motor-efficiency-losses/
│       │   │   │   │   └── index.md
│       │   │   │   ├── motor-family-comparison/
│       │   │   │   │   └── index.md
│       │   │   │   ├── motor-nameplates-slip-torque/
│       │   │   │   │   └── index.md
│       │   │   │   ├── motor-vfd-equations/
│       │   │   │   │   └── index.md
│       │   │   │   ├── servo-drive-fundamentals/
│       │   │   │   │   └── index.md
│       │   │   │   ├── servo-feedback-inertia/
│       │   │   │   │   └── index.md
│       │   │   │   ├── vfd-fundamentals/
│       │   │   │   │   └── index.md
│       │   │   │   └── vfd-servo-architecture/
│       │   │   │       └── index.md
│       │   │   ├── fundamentals/
│       │   │   │   ├── conductor-ampacity/
│       │   │   │   │   └── index.md
│       │   │   │   ├── diodes-transistors/
│       │   │   │   │   └── index.md
│       │   │   │   ├── earthing-systems-iec/
│       │   │   │   │   └── index.md
│       │   │   │   ├── electrical-equations-reference/
│       │   │   │   │   └── index.md
│       │   │   │   ├── electrical-quantities/
│       │   │   │   │   └── index.md
│       │   │   │   ├── equivalent-circuit-methods/
│       │   │   │   │   └── index.md
│       │   │   │   ├── index.md
│       │   │   │   ├── kirchhoff-laws/
│       │   │   │   │   └── index.md
│       │   │   │   ├── passive-components/
│       │   │   │   │   └── index.md
│       │   │   │   └── series-parallel-dividers/
│       │   │   │       └── index.md
│       │   │   ├── index.md
│       │   │   └── nec-application/
│       │   │       ├── article-409-workflow/
│       │   │       │   └── index.md
│       │   │       ├── article-430-workflow/
│       │   │       │   └── index.md
│       │   │       ├── branch-circuits-vs-feeders/
│       │   │       │   └── index.md
│       │   │       ├── class1-class2-circuits/
│       │   │       │   └── index.md
│       │   │       ├── conductor-ocpd-sizing/
│       │   │       │   └── index.md
│       │   │       ├── disconnecting-means/
│       │   │       │   └── index.md
│       │   │       ├── grounding-bonding-panels/
│       │   │       │   └── index.md
│       │   │       ├── index.md
│       │   │       ├── motor-panel-code-application/
│       │   │       │   └── index.md
│       │   │       ├── nec-code-reading/
│       │   │       │   └── index.md
│       │   │       ├── sccr-workflow/
│       │   │       │   └── index.md
│       │   │       └── working-space-table-navigation/
│       │   │           └── index.md
│       │   └── workflows/
│       │       ├── electrical-review/
│       │       │   └── index.md
│       │       ├── index.md
│       │       ├── motor-selection/
│       │       │   └── index.md
│       │       ├── motor-troubleshooting/
│       │       │   └── index.md
│       │       ├── servo-commissioning/
│       │       │   └── index.md
│       │       └── vfd-commissioning/
│       │           └── index.md
│       ├── lifecycle-build-page.png
│       ├── main.py
│       ├── project_state/
│       │   ├── change_log.md
│       │   ├── environment.md
│       │   ├── how_to.md
│       │   └── project_state.md
│       ├── pyproject.toml
│       ├── rag -> control-standards/rag
│       ├── tests/
│       │   ├── __init__.py
│       │   └── tools/
│       │       ├── __init__.py
│       │       └── fe_study/
│       │           ├── __init__.py
│       │           ├── test_common.py
│       │           ├── test_extract_fe_study.py
│       │           └── test_inventory_fe_study.py
│       ├── tools/
│       │   ├── README.md
│       │   ├── fe_study/
│       │   │   ├── README.md
│       │   │   ├── __init__.py
│       │   │   ├── common.py
│       │   │   ├── extract_fe_study.py
│       │   │   ├── inventory_fe_study.py
│       │   │   ├── quality_check_fe_study.py
│       │   │   └── summarize_fe_study.py
│       │   ├── fix_ai_boundaries.py
│       │   ├── generate_rag_index.py
│       │   ├── generate_rag_tree.py
│       │   ├── generate_standards_overview.py
│       │   ├── project_automator.py
│       │   ├── setup_hooks.sh
│       │   ├── validate_ai_boundaries.py
│       │   └── validate_reorg.sh
│       └── uv.lock
├── AGENTS.md
├── CLAUDE.md
├── PROJECT_STARTUP_CONTEXT.md
├── README.md
├── STRUCTURE_SUMMARY.md
├── archive/
│   ├── MIGRATION_GUIDE.md
│   ├── MIGRATION_READY.md
│   ├── MIGRATION_SCRIPT.sh
│   └── PRE_MIGRATION_CHECK.sh
├── control-standards/
│   ├── .gitignore
│   ├── QUICK_START.md
│   ├── README.md
│   ├── STRUCTURE_SUMMARY.md
│   ├── archive/
│   │   ├── README.md
│   │   ├── _archive_old_rag_20260115_221742/
│   │   │   ├── _glossary.md
│   │   │   ├── _index.yaml
│   │   │   ├── _standards_map.md
│   │   │   ├── audit_tool/
│   │   │   │   ├── README.md
│   │   │   │   ├── outputs/
│   │   │   │   └── report_templates/
│   │   │   ├── business_metrics_profit_engine/
│   │   │   │   ├── README.md
│   │   │   │   └── exports/
│   │   │   ├── commissioning_checklists/
│   │   │   │   ├── README.md
│   │   │   │   ├── checklists/
│   │   │   │   └── outputs/
│   │   │   ├── design_framework/
│   │   │   │   ├── README.md
│   │   │   │   ├── constraints/
│   │   │   │   ├── design_guides/
│   │   │   │   │   └── 01_panel_design_guide.md
│   │   │   │   ├── outputs/
│   │   │   │   └── patterns/
│   │   │   │       └── io_templates.yaml
│   │   │   ├── design_package_generator/
│   │   │   │   ├── README.md
│   │   │   │   └── kits/
│   │   │   │       ├── conveyor_control_kit/
│   │   │   │       ├── pump_skid_control_kit/
│   │   │   │       └── robotic_cell_control_kit/
│   │   │   ├── ip_library_licensing/
│   │   │   │   ├── README.md
│   │   │   │   └── export_packages/
│   │   │   ├── knowledge_platform/
│   │   │   │   └── README.md
│   │   │   ├── retainer_support_engine/
│   │   │   │   ├── README.md
│   │   │   │   └── outputs/
│   │   │   ├── standards_intelligence/
│   │   │   │   ├── ISO_IEC/
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── iec_60204_1/
│   │   │   │   ├── NEC/
│   │   │   │   ├── NFPA/
│   │   │   │   ├── UL/
│   │   │   │   ├── clause_index/
│   │   │   │   │   ├── iso_iec_clause_index.yaml
│   │   │   │   │   ├── nec_clause_index.yaml
│   │   │   │   │   ├── nfpa79_clause_index.yaml
│   │   │   │   │   └── ul508a_clause_index.yaml
│   │   │   │   ├── outputs/
│   │   │   │   │   └── standards_guidance_report.md
│   │   │   │   └── rules_engine/
│   │   │   │       ├── red_flags.yaml
│   │   │   │       └── rules.yaml
│   │   │   ├── training_cert_builder/
│   │   │   │   ├── README.md
│   │   │   │   ├── assessments/
│   │   │   │   └── modules/
│   │   │   ├── troubleshooting_decision_engine/
│   │   │   │   ├── README.md
│   │   │   │   ├── decision_trees/
│   │   │   │   ├── outputs/
│   │   │   │   └── playbooks/
│   │   │   └── ul508a_panel_automation/
│   │   │       ├── README.md
│   │   │       ├── outputs/
│   │   │       └── ul_documentation_templates/
│   │   ├── _backup_before_migration_20260115_221742/
│   │   │   ├── new_rag/
│   │   │   │   ├── RAG_DIRECTORY_STATUS.md
│   │   │   │   ├── commissioning_checklists/
│   │   │   │   │   ├── dry_run/
│   │   │   │   │   ├── handover/
│   │   │   │   │   ├── live_run/
│   │   │   │   │   └── pre_power/
│   │   │   │   ├── design_framework/
│   │   │   │   │   ├── control_system_design/
│   │   │   │   │   ├── io_architecture/
│   │   │   │   │   ├── network_architecture/
│   │   │   │   │   ├── power_distribution/
│   │   │   │   │   ├── safety_architecture/
│   │   │   │   │   └── us_eu_compliance_wizard/
│   │   │   │   ├── standards_intelligence/
│   │   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │   │   │   ├── _glossary.md
│   │   │   │   │   ├── _index.yaml
│   │   │   │   │   ├── _overlap_matrix/
│   │   │   │   │   │   ├── _index.yaml
│   │   │   │   │   │   ├── file_structure.md
│   │   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │   │   │   │   ├── standards_decision_workflow.md
│   │   │   │   │   │   ├── standards_overlap.md
│   │   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │   │   │   ├── _overlap_notes/
│   │   │   │   │   │   ├── GENERATION_STATUS.md
│   │   │   │   │   │   ├── _index.yaml
│   │   │   │   │   │   ├── file_structure.md
│   │   │   │   │   │   └── overlap__sccr.md
│   │   │   │   │   ├── _standards_map.md
│   │   │   │   │   ├── iec_60204_1/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause01__scope.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause02__normative_references.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause15__verification.md
│   │   │   │   │   │   ├── IEC60204_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_61508/
│   │   │   │   │   ├── iec_61511/
│   │   │   │   │   ├── iec_62061/
│   │   │   │   │   ├── iso_12100/
│   │   │   │   │   ├── iso_13849_1/
│   │   │   │   │   │   └── file_structure.md
│   │   │   │   │   ├── nec/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │   │   │   │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │   │   │   │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │   │   │   │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │   │   │   │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │   │   │   │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │   │   │   │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │   │   │   │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │   │   │   │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │   │   │   │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │   │   │   │   ├── NEC_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── nfpa79/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch01__administration.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │   │   │   │   ├── NFPA_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── standards_applicability.md
│   │   │   │   │   └── ul_508a/
│   │   │   │   │       ├── GENERATION_SUMMARY.md
│   │   │   │   │       ├── README.md
│   │   │   │   │       ├── UL508A_2022__control_circuits_and_devices.md
│   │   │   │   │       ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │   │   │       ├── UL508A_2022__general_construction_requirements.md
│   │   │   │   │       ├── UL508A_2022__grounding_and_bonding.md
│   │   │   │   │       ├── UL508A_2022__marking_and_documentation.md
│   │   │   │   │       ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │   │   │       ├── UL508A_2022__overcurrent_protection.md
│   │   │   │   │       ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │   │   │       ├── UL508A_2022__scope_and_application.md
│   │   │   │   │       ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │   │   │       ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │   │   │       ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │   │   │       ├── UL508A_OVERVIEW.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── training_modules/
│   │   │   │   │   ├── commissioning/
│   │   │   │   │   ├── fundamentals/
│   │   │   │   │   ├── safety/
│   │   │   │   │   └── troubleshooting/
│   │   │   │   └── troubleshooting_engine/
│   │   │   │       ├── analog_io/
│   │   │   │       ├── decision_trees.yaml
│   │   │   │       ├── digital_io/
│   │   │   │       ├── motion_servo/
│   │   │   │       ├── networks/
│   │   │   │       └── pid_control/
│   │   │   └── old_rag/
│   │   │       ├── _glossary.md
│   │   │       ├── _index.yaml
│   │   │       ├── _standards_map.md
│   │   │       ├── audit_tool/
│   │   │       │   ├── README.md
│   │   │       │   ├── outputs/
│   │   │       │   └── report_templates/
│   │   │       ├── business_metrics_profit_engine/
│   │   │       │   ├── README.md
│   │   │       │   └── exports/
│   │   │       ├── commissioning_checklists/
│   │   │       │   ├── README.md
│   │   │       │   ├── checklists/
│   │   │       │   └── outputs/
│   │   │       ├── design_framework/
│   │   │       │   ├── README.md
│   │   │       │   ├── constraints/
│   │   │       │   ├── design_guides/
│   │   │       │   │   └── 01_panel_design_guide.md
│   │   │       │   ├── outputs/
│   │   │       │   └── patterns/
│   │   │       │       └── io_templates.yaml
│   │   │       ├── design_package_generator/
│   │   │       │   ├── README.md
│   │   │       │   └── kits/
│   │   │       │       ├── conveyor_control_kit/
│   │   │       │       ├── pump_skid_control_kit/
│   │   │       │       └── robotic_cell_control_kit/
│   │   │       ├── ip_library_licensing/
│   │   │       │   ├── README.md
│   │   │       │   └── export_packages/
│   │   │       ├── knowledge_platform/
│   │   │       │   └── README.md
│   │   │       ├── retainer_support_engine/
│   │   │       │   ├── README.md
│   │   │       │   └── outputs/
│   │   │       ├── standards_intelligence/
│   │   │       │   ├── ISO_IEC/
│   │   │       │   │   ├── README.md
│   │   │       │   │   └── iec_60204_1/
│   │   │       │   ├── NEC/
│   │   │       │   ├── NFPA/
│   │   │       │   ├── UL/
│   │   │       │   ├── clause_index/
│   │   │       │   │   ├── iso_iec_clause_index.yaml
│   │   │       │   │   ├── nec_clause_index.yaml
│   │   │       │   │   ├── nfpa79_clause_index.yaml
│   │   │       │   │   └── ul508a_clause_index.yaml
│   │   │       │   ├── outputs/
│   │   │       │   │   └── standards_guidance_report.md
│   │   │       │   └── rules_engine/
│   │   │       │       ├── red_flags.yaml
│   │   │       │       └── rules.yaml
│   │   │       ├── training_cert_builder/
│   │   │       │   ├── README.md
│   │   │       │   ├── assessments/
│   │   │       │   └── modules/
│   │   │       ├── troubleshooting_decision_engine/
│   │   │       │   ├── README.md
│   │   │       │   ├── decision_trees/
│   │   │       │   ├── outputs/
│   │   │       │   └── playbooks/
│   │   │       └── ul508a_panel_automation/
│   │   │           ├── README.md
│   │   │           ├── outputs/
│   │   │           └── ul_documentation_templates/
│   │   ├── old_decision_trees/
│   │   ├── past_audits/
│   │   └── superseded_designs/
│   │       └── work_design/
│   │           ├── README.md
│   │           ├── historical_prompts/
│   │           │   └── scratch_notes/
│   │           │       ├── standards_atlas_homepage_wireframe_and_templates.md
│   │           │       ├── standards_web_page_design_prompt_v1.md
│   │           │       ├── standards_web_page_design_prompt_v3.md
│   │           │       ├── standards_web_page_design_prompt_v4.1.md
│   │           │       └── standards_web_page_design_prompt_v4.md
│   │           ├── promoted_to_rag/
│   │           │   ├── Grounding, System and Equipment [250.4, 2020 NEC].md
│   │           │   ├── spacing creepage clearance.md
│   │           │   └── ul 508a.md
│   │           └── site_source_notes/
│   │               └── decision_workflow.md
│   ├── exports/
│   │   ├── README.md
│   │   ├── docx/
│   │   ├── legacy_root/
│   │   │   ├── README.md
│   │   │   ├── csv/
│   │   │   ├── pdf/
│   │   │   └── snapshots/
│   │   ├── pdf/
│   │   └── reports/
│   ├── governance/
│   │   ├── README.md
│   │   ├── decision_log.md
│   │   ├── design_change_policy.md
│   │   ├── promotion_checklist_drafts_to_rag.md
│   │   └── release_notes.md
│   ├── rag/
│   │   ├── commissioning_checklists/
│   │   │   ├── README.md
│   │   │   ├── _index.yaml
│   │   │   ├── checklists/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── basic_circuit_polarity_and_power_checks.md
│   │   │   │   ├── capacitor_discharge_awareness_check.md
│   │   │   │   ├── drive_commissioning.md
│   │   │   │   ├── motor_nameplate_and_overload_setting.md
│   │   │   │   ├── motor_rotation_and_overload_verification.md
│   │   │   │   └── pre_power_panel_and_incoming_supply_check.md
│   │   │   ├── dry_run/
│   │   │   ├── handover/
│   │   │   ├── live_run/
│   │   │   └── pre_power/
│   │   ├── design_framework/
│   │   │   ├── README.md
│   │   │   ├── _index.yaml
│   │   │   ├── constraints/
│   │   │   │   └── grounding_bonding_rules.yaml
│   │   │   ├── control_system_design/
│   │   │   ├── design_guides/
│   │   │   │   └── 02_power_distribution_guide.md
│   │   │   ├── electrical_review/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── basic_resistive_network_review.md
│   │   │   │   ├── component_selection_basics.md
│   │   │   │   ├── ohms_law_and_power_check_workflow.md
│   │   │   │   └── simple_signal_and_interface_circuit_notes.md
│   │   │   ├── io_architecture/
│   │   │   ├── motor_systems/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│   │   │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│   │   │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│   │   │   │   ├── integrated_motor_drive_architecture_comparison.md
│   │   │   │   ├── motor_cable_and_protection_review.md
│   │   │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│   │   │   │   ├── motor_nameplate_review_checklist.md
│   │   │   │   ├── motor_selection_comparison_matrix.md
│   │   │   │   ├── motor_selection_workflow.md
│   │   │   │   ├── motor_symptom_troubleshooting_patterns.md
│   │   │   │   ├── motor_troubleshooting_decision_tree.md
│   │   │   │   ├── servo_commissioning_workflow.md
│   │   │   │   ├── star_delta_and_supply_matching_notes.md
│   │   │   │   ├── vfd_commissioning_workflow.md
│   │   │   │   └── vfd_motor_integration_review.md
│   │   │   ├── network_architecture/
│   │   │   ├── power_distribution/
│   │   │   ├── safety_architecture/
│   │   │   ├── semiconductor_facility/
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── alarm_and_measurement_strategy.md
│   │   │   │   ├── bulk_chemical_distribution.md
│   │   │   │   ├── bulk_specialty_gas.md
│   │   │   │   ├── commissioning_reference.md
│   │   │   │   ├── common_control_philosophy.md
│   │   │   │   ├── device_family_library.md
│   │   │   │   ├── exhaust_abatement_vacuum.md
│   │   │   │   ├── hvac_and_cleanroom.md
│   │   │   │   ├── instrumentation_selection.md
│   │   │   │   ├── instrumentation_use_matrix.md
│   │   │   │   ├── safety_and_shutdown.md
│   │   │   │   ├── tool_facility_interface.md
│   │   │   │   ├── upw_and_wastewater.md
│   │   │   │   └── vendor_families.md
│   │   │   └── us_eu_compliance_wizard/
│   │   │       ├── README.md
│   │   │       ├── US_EU_Machine_Compliance_Wizard.md
│   │   │       ├── us_eu_delta_report_template.md
│   │   │       └── us_eu_wizard_rules.yaml
│   │   ├── meta/
│   │   │   ├── RAG_DIRECTORY_STATUS.md
│   │   │   └── VERSION_OVERVIEW.md
│   │   ├── standards_intelligence/
│   │   │   ├── README.md
│   │   │   ├── _glossary.md
│   │   │   ├── _index.yaml
│   │   │   ├── _standards_map.md
│   │   │   ├── crosswalks/
│   │   │   │   ├── overlap_matrix/
│   │   │   │   │   ├── _index.yaml
│   │   │   │   │   ├── file_structure.md
│   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │   │   │   ├── standards_decision_workflow.md
│   │   │   │   │   ├── standards_overlap.md
│   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │   │   └── overlap_notes/
│   │   │   │       ├── GENERATION_STATUS.md
│   │   │   │       ├── _index.yaml
│   │   │   │       ├── file_structure.md
│   │   │   │       ├── overlap__motors_drives.md
│   │   │   │       ├── overlap__sccr.md
│   │   │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│   │   │   ├── file_structure.md
│   │   │   ├── international/
│   │   │   │   ├── cybersecurity/
│   │   │   │   │   └── iec_62443/
│   │   │   │   │       ├── IEC62443_2_1__security_management.md
│   │   │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│   │   │   │   │       ├── IEC62443_4_2__component_requirements.md
│   │   │   │   │       ├── IEC62443_lifecycle.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── functional_safety/
│   │   │   │   │   ├── iec_61508/
│   │   │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│   │   │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│   │   │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│   │   │   │   │   │   ├── IEC61508_2010__Part3__software.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_61511/
│   │   │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│   │   │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│   │   │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│   │   │   │   │   │   ├── IEC61511_2016__Part1__framework.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_62061/
│   │   │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause07__subsystem_design.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iso_12100/
│   │   │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause07__risk_reduction.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   └── iso_13849_1/
│   │   │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│   │   │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│   │   │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│   │   │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│   │   │   │   │       ├── ISO13849_2023__Clause06__categories.md
│   │   │   │   │       ├── ISO13849_2023__Clause07__validation.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── hazardous_area/
│   │   │   │   │   └── iec_60079/
│   │   │   │   │       ├── IEC60079_0__general_requirements.md
│   │   │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│   │   │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│   │   │   │   │       ├── IEC60079_14__installation_design.md
│   │   │   │   │       ├── IEC60079_17__inspection_maintenance.md
│   │   │   │   │       ├── IEC60079_1__flameproof_Ex_d.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── machinery/
│   │   │   │   │   └── iec_60204_1/
│   │   │   │   │       ├── GENERATION_SUMMARY.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause01__scope.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause02__normative_references.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │   │   │   │       ├── IEC60204_1_2018__Clause15__verification.md
│   │   │   │   │       ├── IEC60204_OVERVIEW.md
│   │   │   │   │       ├── README.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── offshore/
│   │   │   │   │   ├── ABS_offshore_electrical_control.md
│   │   │   │   │   ├── DNV_OS_D201__electrical_installations.md
│   │   │   │   │   └── _index.yaml
│   │   │   │   └── semiconductor/
│   │   │   │       └── semi/
│   │   │   │           ├── SEMI_S14__fire_risk_assessment.md
│   │   │   │           ├── SEMI_S2__equipment_safety.md
│   │   │   │           ├── SEMI_S8__ergonomics.md
│   │   │   │           └── _index.yaml
│   │   │   ├── library_admin/
│   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │   │   ├── README.md
│   │   │   │   ├── STANDARDS_COMPLETION_STATUS.md
│   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │   │   └── STANDARDS_PURCHASE_TRACKER.md
│   │   │   ├── reference_models/
│   │   │   │   ├── 15-Standard Minimum Compliance Stack.md
│   │   │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│   │   │   │   ├── README.md
│   │   │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│   │   │   │   ├── Universal Machine Safety Architecture.md
│   │   │   │   └── standards_atlas_diagrams_reference.md
│   │   │   ├── routing/
│   │   │   │   ├── README.md
│   │   │   │   └── standards_applicability.md
│   │   │   ├── scenario/
│   │   │   │   ├── cnc_machine_safety_design/
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   ├── requirements.yaml
│   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   ├── system_description.md
│   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   ├── mini_machine_safety_design/
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   ├── industry_overlays/
│   │   │   │   │   │   ├── commercial.md
│   │   │   │   │   │   ├── energy.md
│   │   │   │   │   │   ├── food_and_beverage.md
│   │   │   │   │   │   ├── marine.md
│   │   │   │   │   │   ├── medical.md
│   │   │   │   │   │   ├── nuclear.md
│   │   │   │   │   │   ├── offshore.md
│   │   │   │   │   │   ├── petroleum.md
│   │   │   │   │   │   └── semiconductor.md
│   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   ├── requirements.yaml
│   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   ├── system_description.md
│   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   └── mini_machine_safety_design_v2/
│   │   │   │       ├── README.md
│   │   │   │       ├── control_architecture_and_network.md
│   │   │   │       ├── hazards_and_risk_assessment.md
│   │   │   │       ├── industry_overlays/
│   │   │   │       │   ├── commercial.md
│   │   │   │       │   ├── energy.md
│   │   │   │       │   ├── food_and_beverage.md
│   │   │   │       │   ├── marine.md
│   │   │   │       │   ├── medical.md
│   │   │   │       │   ├── nuclear.md
│   │   │   │       │   ├── offshore.md
│   │   │   │       │   ├── petroleum.md
│   │   │   │       │   └── semiconductor.md
│   │   │   │       ├── mechanical_and_electrical_isolation.md
│   │   │   │       ├── requirements.yaml
│   │   │   │       ├── safety_functions_register.md
│   │   │   │       ├── safety_integrity_and_sil_strategy.md
│   │   │   │       ├── standards_applicability_matrix.md
│   │   │   │       ├── system_description.md
│   │   │   │       ├── ul_nec_design_requirements.md
│   │   │   │       └── verification_and_validation_plan.md
│   │   │   └── us/
│   │   │       ├── nec/
│   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│   │   │       │   ├── NEC_2023__Art100__definitions.md
│   │   │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │       │   ├── NEC_2023__Art215__feeders.md
│   │   │       │   ├── NEC_2023__Art230__services.md
│   │   │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│   │   │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│   │   │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│   │   │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│   │   │       │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│   │   │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │       │   ├── NEC_COMPLETION_STATUS.md
│   │   │       │   ├── NEC_OVERVIEW.md
│   │   │       │   ├── README.md
│   │   │       │   └── _index.yaml
│   │   │       ├── nfpa79/
│   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │       │   ├── NFPA79_2024__Ch01__administration.md
│   │   │       │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │       │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │       │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │       │   ├── NFPA_OVERVIEW.md
│   │   │       │   ├── README.md
│   │   │       │   └── _index.yaml
│   │   │       └── ul_508a/
│   │   │           ├── GENERATION_SUMMARY.md
│   │   │           ├── README.md
│   │   │           ├── UL508A_2022__control_circuits_and_devices.md
│   │   │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │           ├── UL508A_2022__general_construction_requirements.md
│   │   │           ├── UL508A_2022__grounding_and_bonding.md
│   │   │           ├── UL508A_2022__marking_and_documentation.md
│   │   │           ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │           ├── UL508A_2022__overcurrent_protection.md
│   │   │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │           ├── UL508A_2022__scope_and_application.md
│   │   │           ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │           ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │           ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │           ├── UL508A_OVERVIEW.md
│   │   │           └── _index.yaml
│   │   ├── training_modules/
│   │   │   ├── README.md
│   │   │   ├── _index.yaml
│   │   │   ├── commissioning/
│   │   │   ├── control_systems/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── control_theory_overview.md
│   │   │   │   ├── industrial_control_loop_architectures.md
│   │   │   │   ├── industrial_pid_implementation.md
│   │   │   │   ├── pid_control_intuition.md
│   │   │   │   ├── pid_control_intuitive_foundation.md
│   │   │   │   ├── pid_drone_control.md
│   │   │   │   └── pid_heater_control_with_contactor.md
│   │   │   ├── electrical_machines/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── ac_vs_dc_motor_comparison.md
│   │   │   │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│   │   │   │   ├── dc_motor_basics.md
│   │   │   │   ├── induction_motor_basics.md
│   │   │   │   ├── motor_and_vfd_equations_reference.md
│   │   │   │   ├── motor_control_methods_and_operating_regions.md
│   │   │   │   ├── motor_efficiency_power_factor_and_losses.md
│   │   │   │   ├── motor_family_comparison.md
│   │   │   │   ├── motor_nameplates_slip_and_torque.md
│   │   │   │   ├── servo_drive_fundamentals.md
│   │   │   │   ├── servo_feedback_and_inertia_matching.md
│   │   │   │   ├── vfd_and_servo_architecture_diagrams.md
│   │   │   │   └── vfd_fundamentals.md
│   │   │   ├── fundamentals/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── conductor_ampacity_and_termination_temperature.md
│   │   │   │   ├── diodes_transistors_and_switching_basics.md
│   │   │   │   ├── earthing_systems_iec.md
│   │   │   │   ├── electrical_equations_reference.md
│   │   │   │   ├── electrical_quantities_and_circuit_language.md
│   │   │   │   ├── equivalent_circuit_methods.md
│   │   │   │   ├── kirchhoff_laws_and_systematic_analysis.md
│   │   │   │   ├── passive_components_resistors_capacitors.md
│   │   │   │   └── series_parallel_and_divider_methods.md
│   │   │   ├── nec_application/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── article_409_practical_workflow.md
│   │   │   │   ├── article_430_practical_workflow.md
│   │   │   │   ├── branch_circuits_vs_feeders_motor_loads.md
│   │   │   │   ├── class1_class2_remote_control_circuits.md
│   │   │   │   ├── conductor_ocpd_sizing_examples.md
│   │   │   │   ├── disconnecting_means_for_machinery.md
│   │   │   │   ├── grounding_bonding_control_panels.md
│   │   │   │   ├── motor_and_panel_code_application.md
│   │   │   │   ├── nec_code_reading_fundamentals.md
│   │   │   │   ├── sccr_workflow.md
│   │   │   │   └── working_space_and_table_navigation.md
│   │   │   ├── safety/
│   │   │   └── troubleshooting/
│   │   └── troubleshooting_engine/
│   │       ├── analog_io/
│   │       ├── decision_trees.yaml
│   │       ├── digital_io/
│   │       ├── motion_servo/
│   │       ├── networks/
│   │       └── pid_control/
│   ├── restricted/
│   │   ├── README.md
│   │   ├── do_not_read/
│   │   │   ├── DELIVERABLE.md
│   │   │   ├── PROJECT_STRUCTURE 4.59.29 PM.md
│   │   │   ├── QUICK_START.md
│   │   │   ├── README.md
│   │   │   └── control_system_project_template.tar.gz
│   │   └── legacy_drafts/
│   │       ├── README.md
│   │       ├── copied_standard_text/
│   │       ├── raw_notes/
│   │       └── vendor_docs/
│   ├── templates/
│   │   ├── README.md
│   │   ├── checklists/
│   │   │   └── checklist_template.md
│   │   ├── design_guides/
│   │   │   └── design_guide_template.md
│   │   ├── md_headers/
│   │   │   ├── archived_header.md
│   │   │   ├── draft_only_header.md
│   │   │   └── rag_approved_header.md
│   │   ├── reports/
│   │   │   └── report_template.md
│   │   └── work_notes/
│   │       └── work_note_template.md
│   ├── tools/
│   │   ├── audit_tool/
│   │   │   ├── README.md
│   │   │   ├── outputs/
│   │   │   └── report_templates/
│   │   ├── business_metrics_profit_engine/
│   │   │   ├── README.md
│   │   │   └── exports/
│   │   ├── design_package_generator/
│   │   │   ├── README.md
│   │   │   └── kits/
│   │   │       ├── conveyor_control_kit/
│   │   │       ├── pump_skid_control_kit/
│   │   │       └── robotic_cell_control_kit/
│   │   ├── ip_library_licensing/
│   │   │   ├── README.md
│   │   │   └── export_packages/
│   │   ├── knowledge_platform/
│   │   │   └── README.md
│   │   ├── retainer_support_engine/
│   │   │   ├── README.md
│   │   │   └── outputs/
│   │   └── ul508a_panel_automation/
│   │       ├── README.md
│   │       ├── outputs/
│   │       └── ul_documentation_templates/
│   └── work/
│       ├── README.md
│       ├── design/
│       │   ├── 2026 NEC Changes.md
│       │   ├── README.md
│       │   ├── conductor_protection_and_ampacity_transcript_summary.md
│       │   ├── control theory.md
│       │   ├── diagrams/
│       │   ├── electrical exam prep.md
│       │   ├── equipment_grounding_conductor_topics/
│       │   │   ├── README.md
│       │   │   ├── egc_cable_methods_ac_and_mc.md
│       │   │   ├── egc_definition_and_effective_fault_path.md
│       │   │   ├── egc_other_listed_systems.md
│       │   │   ├── egc_sizing_and_250_122_notes.md
│       │   │   └── egc_wire_and_raceway_methods.md
│       │   ├── experiments/
│       │   ├── mermaid_diagrams_to_reference.md
│       │   ├── mini_machine_safety_design_v2_project_status.md
│       │   ├── nec_2026_changes_topics/
│       │   │   ├── 2026_nec_codewide_editorial_and_90_3_changes.md
│       │   │   ├── 2026_nec_limited_energy_restructure.md
│       │   │   ├── 2026_nec_medium_voltage_restructure.md
│       │   │   ├── 2026_nec_new_and_relocated_articles.md
│       │   │   ├── 2026_nec_overview_and_2029_transition.md
│       │   │   └── README.md
│       │   ├── nec_210_4_multiwire_branch_circuits_transcript_summary.md
│       │   ├── nec_update.md
│       │   ├── project_implementation_gaps/
│       │   │   ├── 20260308_status.md
│       │   │   ├── electrical and practical circuit analysis.md
│       │   │   ├── electrical_and_practical_circuit_analysis_topics/
│       │   │   │   ├── INTEGRATION_PLAN.md
│       │   │   │   ├── README.md
│       │   │   │   ├── circuit_analysis_overview_and_linear_elements.md
│       │   │   │   ├── equivalent_circuit_methods_topics/
│       │   │   │   │   ├── README.md
│       │   │   │   │   ├── norton_equivalent_method.md
│       │   │   │   │   ├── source_transformation_basics.md
│       │   │   │   │   ├── superposition_theorem_notes.md
│       │   │   │   │   └── thevenin_equivalent_method.md
│       │   │   │   ├── kcl_and_nodal_analysis.md
│       │   │   │   ├── kvl_and_loop_analysis.md
│       │   │   │   ├── practical_components_diodes_and_transistors.md
│       │   │   │   ├── practical_components_resistors_and_capacitors.md
│       │   │   │   ├── practical_ohms_law_power_and_resistor_color_code.md
│       │   │   │   ├── series_parallel_and_divider_methods.md
│       │   │   │   └── source_transformation_and_equivalent_methods.md
│       │   │   ├── importance of electrical safety in control panels.md
│       │   │   ├── motors.md
│       │   │   ├── motors_topics/
│       │   │   │   ├── INTEGRATION_PLAN.md
│       │   │   │   ├── README.md
│       │   │   │   ├── dc_motor_armature_winding_and_torque_production.md
│       │   │   │   ├── dc_motor_commutator_brushes_and_power_path.md
│       │   │   │   ├── dc_motor_magnetism_stator_and_mechanical_structure.md
│       │   │   │   ├── ev_motor_powertrain_configurations.md
│       │   │   │   ├── ev_motor_types_overview.md
│       │   │   │   ├── induction_motor_components_induction_and_slip.md
│       │   │   │   ├── induction_motor_construction_and_rotating_field.md
│       │   │   │   ├── induction_motor_nameplate_and_enclosures.md
│       │   │   │   ├── induction_motor_poles_torque_curves_and_nema_designs.md
│       │   │   │   └── induction_motor_terminal_connections_and_star_delta.md
│       │   │   ├── nec_exam_prep_topics/
│       │   │   │   ├── INTEGRATION_PLAN.md
│       │   │   │   ├── README.md
│       │   │   │   ├── electrical_exam_math_ohms_law_and_power.md
│       │   │   │   ├── nec_code_reading_and_index_method.md
│       │   │   │   ├── nec_table_reading_and_working_space_example.md
│       │   │   │   └── residential_load_calculation_notes.md
│       │   │   └── temp links.md
│       │   ├── residential_nec_top_articles_transcript_summary.md
│       │   ├── scratch_notes/
│       │   │   └── simple_safety_system_design.md
│       │   ├── types of equipment ground conductors.md
│       │   ├── types of grounding.md
│       │   └── voltage_drop_topics/
│       │       ├── README.md
│       │       ├── voltage_drop_energy_code_and_specifications.md
│       │       ├── voltage_drop_fire_pump_notes.md
│       │       ├── voltage_drop_general_basis.md
│       │       └── voltage_drop_recommended_feeder_and_branch_guidance.md
│       └── general/
│           ├── 00_inbox_notes.md
│           ├── README.md
│           ├── commissioning_notes/
│           ├── design_working/
│           ├── experiments/
│           ├── standards_notes/
│           └── troubleshooting_logs/
├── data/
│   ├── README.md
│   ├── historian_exports/
│   ├── network_captures/
│   └── plc_exports/
├── docs/
│   ├── .bundle/
│   │   └── config
│   ├── .jekyll-cache/
│   │   ├── .gitignore
│   │   └── Jekyll/
│   │       └── Cache/
│   │           ├── Jekyll--Cache/
│   │           │   └── b7/
│   │           │       └── 9606fb3afea5bd1609ed40b622142f1c98125abcfe89a76a661b0e8e343910
│   │           └── Jekyll--Converters--Markdown/
│   │               ├── 00/
│   │               │   ├── a36fe105cbca83ed9530f67a910848a3fb7e2decc6fb938fc1311e08e58ebb
│   │               │   ├── ad78689b54caee65bf7b075c4072843dc6e58c94874aa280a441f9c18b644b
│   │               │   └── b5747d3ed8cacc545cc97cf40d2efab7a24f566939a6aacc6fea6723043269
│   │               ├── 01/
│   │               │   ├── 0666d82831bc0835108bbc6cbb06c19916210343ea56afa448fce639231516
│   │               │   └── 490aeb193504bfbf24410f4a2ca9635a499a3f5f6f946c84532507b40ad03c
│   │               ├── 02/
│   │               │   ├── b745bdefe9bf4c824c0256ef7001b816fad13e7a1a3638905d6b49beb805f3
│   │               │   └── ebbff2a689d2765789d765899c91a9d74657e4db74b6603031b7c0bd6eb72c
│   │               ├── 03/
│   │               │   ├── 436ee6fecf0265cb92d47b4aa51d12bca647ddd4b9f44d699443a5592035fd
│   │               │   └── 85d58d8e81429a93fa2e5375d181b93e320a3b4bb8166de581315acc06b0b6
│   │               ├── 04/
│   │               │   └── 8ae153d1cc2aef54095eadad06148ac1372da0e9f585dc95e40b643279a3ea
│   │               ├── 05/
│   │               │   └── e30a933569bb3be691a61dd9d27d5cb517e9005f7bf22a109eb8a237eab00d
│   │               ├── 06/
│   │               │   ├── 71713d204ebeb2b93aa6fa46e9eb924c81cd4b48b99a63b136f7c176278be9
│   │               │   └── d3a687ff4b25e2062eb633ed15fbe1736c9f6c4345811632c44f80c9c712bd
│   │               ├── 07/
│   │               │   ├── 76b9e4c446f05649bf57c11e9818f9054d577a03aea6aae9270fd3f9a5a44e
│   │               │   └── adda04e9080f67eea12efbddbcb3d7f76c877fd50e902f5f83da4ac384f044
│   │               ├── 0a/
│   │               │   └── 46242bc7af14bf7af61342f0928754a9f55af3b85e5ed37689bdc43e37538f
│   │               ├── 0b/
│   │               │   ├── 277d1c90c99f80c0f2cfc106307d7bcfd747c8ea5b1b6a4ade8749c6e6ef20
│   │               │   ├── 36fd9699ea3c594f2935d5b180504cca916d440e00a16fc4081cc59274562a
│   │               │   ├── 4205bc5068005f51aed34e5f9c4caf5cc22a95ddfe6218fad28eb6a12278b4
│   │               │   └── 7a4716831accfb3c6ed7db6f4bd374733d381c5216654f473051e3e62b4245
│   │               ├── 0c/
│   │               │   ├── 21a7d7aadd1a042168087ad4dd2323df1ae50a4de93a8da4b920963100b904
│   │               │   ├── 3a39ada4f92016c85f3bc042503886310c14593114c91a9c68d423d530942b
│   │               │   ├── a29af28c804d30788fd4d5da9c68dad6599d6bd49d8c113cdfddd9ec3f4368
│   │               │   └── b884b6343a61259ab5eacf2fb4394a401d05919cfd0fc5fcdc94957f0dc271
│   │               ├── 0d/
│   │               │   ├── 0b2dfd9fcde91ec81a829dbc690e60db0c9de83282525b18f277a4434ae4bf
│   │               │   ├── 13eb23d2173fd50fd78814a4c2f7f2c1ad049673f217c51511484eeef6f394
│   │               │   ├── 7a2b779118c9ad2579aea67af3c5911e4fe21a4e2c2d5e500df81db50bcc3f
│   │               │   ├── 8f205a363b0c606f9d6ebef31835545eb5195371819394ff29a1bd428e8055
│   │               │   └── a6f65922f6e117f784b372bf390c599e40d300c4c48b9b71cc5fc2abb0f263
│   │               ├── 0f/
│   │               │   ├── 260c0f2220909dd3e4dd4990c35bacc6ec27c2c18b194b8205187fb96a4ecf
│   │               │   ├── 5293790685d198f5e3c499d4946e60f45ec443a49787d3eca6637dd8f1132a
│   │               │   ├── 5a8256ba0de2191ae6c903cf187a28af4fcc99b6b308c52aca6823299ccac6
│   │               │   └── f175237f59a9b1496dea69ff7e8a19965f28d2520c7319d41f59553b0fd015
│   │               ├── 10/
│   │               │   ├── a0872e84bdec77674c9b5550f33b8913daa1ef35666d88df8345d560547eae
│   │               │   └── da3413b3d068d25f0f0f6333d381ba222d1cdbc1405613dcaeeeba2b097f37
│   │               ├── 11/
│   │               │   ├── 5651ae7b2f4a93060f41e671c1138f714c0175495fd6bfeaa75d7017a4565a
│   │               │   └── 8081aafd27e34ad91d11583ba46f3e7decc0d0f73644905fd0fb7d6508d780
│   │               ├── 12/
│   │               │   ├── 53ee623d4f7b3b5ec4537af00ac2095d43a65f9de7b2adc18f77cccf38bb22
│   │               │   └── 6a727c4516c3680a89601de7e19fb924b1a5bdc1fe7fb81540dbefcd4b7e86
│   │               ├── 13/
│   │               │   ├── 9de8fd38fc8eb4dfe1dff19ec5bf3057994c3cc72c787a96c281876dcffe57
│   │               │   └── eea4c3e5d334d693826e333328812e5374926e0fbec6f6c325d8ed9604d1f0
│   │               ├── 14/
│   │               │   ├── 5a43218083af5c29b09bf909df9f4cc76e59ade1230d85ffa473d65d05f5bb
│   │               │   ├── 5c49ddd4ba343f9549b684618c6712d20b73eb8c689543f3a345383bf3a7d1
│   │               │   ├── c7c0f3f2433296d036c07adf0f83e0407e081788d9f7c65bfe730106a5f4f4
│   │               │   └── f9e341abc6ac38e9cc6a8298046f954fbf6d02f49d3e2ffec9399fc2e95f8e
│   │               ├── 15/
│   │               │   └── 20a9fe1914a393702bbf6c979b685d8a752a4008d15bf3a3a2898148d9a521
│   │               ├── 16/
│   │               │   └── 128c2f7a863b1b2b6234ab7bcaf801793dd4ab4dd1321ebd6c09633010da40
│   │               ├── 18/
│   │               │   ├── 3507bc872de95d948ca2aad8dcf8321dbdc6b965053c4409760688eadb8222
│   │               │   ├── 94e9d75cee6275fe7456cab2534c4169cb6f49d5802986022b81540a8112cd
│   │               │   └── c9c2e2b613b0ca805fdc61b65e919d70e6431fe615b8805a5f5e87baf989d8
│   │               ├── 19/
│   │               │   ├── 11b453a7b71283880d3624077780fe48aaefd82f638d5870794abfb325baef
│   │               │   ├── 4dd135557b4972bfbe4ed66bd4b8b38513a1840cc913b5abbd0efea30a2733
│   │               │   ├── 830317083b72244c744954ea64c129c8ae5c86a047fc7d55e2252276f1fb92
│   │               │   └── 9dbea333b349b2a64d71f9643314febadb768dcf473768c37fb66df58d4527
│   │               ├── 1a/
│   │               │   └── dc5acf9103c26335ce0694afa5e7fe80fea5c01fe5d0be2436f9aba9f8ca12
│   │               ├── 1b/
│   │               │   ├── 8fd71b9d38b1dcd9cc695d3c7e463bc07806c060d197fce7418069e84f77ac
│   │               │   └── aaf0b56cbf68854696ee01829ef68ac4a27363e802fc9ad4c8e62c78e93236
│   │               ├── 1c/
│   │               │   └── 1fe9887c2c3a802b03f157b23d6073851131deac81b5bfbcb46c078956d368
│   │               ├── 1d/
│   │               │   ├── 2d81ad64c017c57b66dc14f338656d1a4abd6b680418e2996b0f722be596e6
│   │               │   └── 73a91f05cece15fc75c605d25ac11a1bc248d7f5cb16a140a1dec9930b555f
│   │               ├── 1e/
│   │               │   ├── 48a3689b1851c7e900cf8573cba53b7c3812c36935d0403c3ead0b5ecb3fa1
│   │               │   ├── 66cf06507d7410aa2c21264d3c2affb5b5ef8e49f1ec94db2a1285d47a9225
│   │               │   ├── a40bb730a09e050e0d130b83f90af7ccf9cb5f12db8907a1f17f734cbb89cc
│   │               │   └── e76252f7f7c3677aa8032f04364ca17e1939fe0c23f3eba350f9d913033b7d
│   │               ├── 1f/
│   │               │   ├── acbf512ceacb9df1f9cc84b9cbe9db9b09c3600652ced2f3553665370b4bbb
│   │               │   └── ecc2fdd009c57f77739f4c8efd3c82c2034598daaf82b6d7e8989bd75f696d
│   │               ├── 21/
│   │               │   ├── 3a6eb88d4d93a5751444e92aa4fb8517a1e06b222112d1218f220efba9316c
│   │               │   ├── 4ce69dabd8554ca035185834f203c3266a54c0d6eb5c6d9a6967f9e807a2ab
│   │               │   └── f23f6b6ccf01bad061aa3952538f401e3ad8e2e67cd0bf71b4b9c185419ea7
│   │               ├── 23/
│   │               │   ├── 10a2e52d8068e80d62b9bcc513338e87235b5f7de581a98baa0c54e1c34895
│   │               │   └── 7ae4631ab84a0848ee51d4ecb6b14d359e0e4555074581c35f903dfdc94737
│   │               ├── 24/
│   │               │   ├── acf13ae9c5b58b350a8a999ace22166b603c017ffb25b9a8da7f76c6d28896
│   │               │   └── edb242d867d57ac61d78eaa8b7f0e26c1362a226de47c5b1008405cd2117d6
│   │               ├── 25/
│   │               │   ├── 5cbfca59e5fe6e714f7c7d1e2fee372056e8b02ec0f015aa69adf87fc9a3f3
│   │               │   ├── 8e30e04480a1d85dfbce1ae190a0d36926dbc8e652e2f007f1afdabe1b4bd9
│   │               │   └── fa1f3f5cf75e082ef4d40f89bd5c0fb26587111d71301d334746f209afcb57
│   │               ├── 26/
│   │               │   ├── 0785d22eb41cc5c77249078677a780cdb9142ae2328e59639d4806b6c1950f
│   │               │   └── a0a645f852592a4807fa5b6a3e8edb0dbe562582d519d2cc1deec947dd6aa4
│   │               ├── 28/
│   │               │   ├── 32477a313a466bb0fe39c91dfeaebe1925eae6b6a662a53115577ef0699cb2
│   │               │   ├── 5b6f314ca288e8140e3b0815e179f5563a5b6fa4a0e855abe1cff68e9fe95f
│   │               │   ├── 626866f3fb869decb709fc758290b6138102ae01f812803a9c05bd1f9d4144
│   │               │   └── b1f2ee513fb5c930f6e83980c3a9d8e84cc57ed5125ba9d1c06112014b8f53
│   │               ├── 2a/
│   │               │   ├── a2e80619f1620666cd536d612c7eb320609bf93834edcf5aca322334f85a7f
│   │               │   ├── aa3f7d45023ddf87b1d0d05b61b38d7d58d66e3010aa79f6a2986399295f5d
│   │               │   └── c3f273f3c3c82839364c9f319ec340b335117d0c2278627c352cdd933122ad
│   │               ├── 2b/
│   │               │   ├── 06ecf0ad580e2fe993f9648cc4bd91a2461f0cb74a8a38a139fbc2f833a386
│   │               │   ├── 1df1b19b5a468913e187313dcf8e21bd90e54fcb0a75b86d6f7f87bf86f888
│   │               │   └── 3954e53e89ea5b825a1964e8992e5acd7180932d83bc19e86e537ec9f2c278
│   │               ├── 2c/
│   │               │   ├── 27700d3c2ee76229c957b35e06dd6e5e6fdb26ff850aa638c3f34daaf6e680
│   │               │   ├── 3c9c485b36a39846dbbf1963f318b90e7ca3aa951832c0abfe029751592f51
│   │               │   └── 9bcd808985cdaa49537e875c91e0ee76020f2c82514987d576738005773fb5
│   │               ├── 2d/
│   │               │   ├── d2aa9c6b18d70106e2dc99bb9588df36a49fe8052a89972a452387ef102970
│   │               │   └── f240f66f0af2038861b9050b6fc78925a5aaac91cf39dc8df01ce206694a8c
│   │               ├── 2e/
│   │               │   └── f22d474511da0bbeb817b73f8b890b07ae6646351859267f08cc4e7c6d851e
│   │               ├── 2f/
│   │               │   └── 5e1412735984ba77818de876dcf7007c5dce7da5d99c244a86b7d4444a7d59
│   │               ├── 30/
│   │               │   └── fbb18d342f33b43ec53dfb8d634427cf3b5a7bea04173b3dd4ad48025e7f45
│   │               ├── 31/
│   │               │   └── dc4b6eda03f83f13fff24585427aaab3d137a586173926a0d1ab717c6363e5
│   │               ├── 32/
│   │               │   ├── 169fcfb4fda480b28401397fde19cbd9e5ff87f555df850bcb13a2d1aaf6b4
│   │               │   └── 5349ab1118ee4ab00c43d4c92f57ebacdd3ac293784c0301ba1f8cc21b2ec8
│   │               ├── 33/
│   │               │   ├── 2fe956ad0da386b9d332f08ce65713ceb9be652477fc20fc8d608a638bea6f
│   │               │   ├── 81791fcac679277532761bd34c13e1f01d2707a7d968135a719da3b7fc264f
│   │               │   ├── b95d3c72b1293a7ca1aa200291cf6491cce8b27ca46349cb20ae2df406a431
│   │               │   ├── e444576406c2d5185663678d1f2a05494cb7ea7e1f6fc1602359aa12139076
│   │               │   └── f71006d652ee55f235e9f005fc6620afcbbf683f2e8332e81378e5d2ae4975
│   │               ├── 34/
│   │               │   └── 086a68851a781a7bda77227a33de3529ad06aecd4587a6edde00a6abea5814
│   │               ├── 36/
│   │               │   ├── 2fb545818ed256bd696d2ae5e4f1d27de89f914edcfb179b818eda8e1b7705
│   │               │   ├── 7a9714db36c9661b038a09467862e21fe9d2f651758bc790fbb7976018cdd6
│   │               │   ├── d582097a42b157b16a059c76c099e57f145550bc3b1266e8823f4c06a7146b
│   │               │   └── d735fcb4600a3c59aab09c322fc0ee6141a8414d7e9ddd5782143916b2ac45
│   │               ├── 38/
│   │               │   ├── 0b419f3d060ea0e1951a0d6245ee53269117f5fe5cf7043c76ba4438be637b
│   │               │   ├── 4a2388507cea747def3af4ea2153d40aaca160c5c589d53eb76bbec75075e1
│   │               │   ├── a0590b263354190faaa38dfe0bb73cafc860c4129f0ea4242aff00d3cb91b1
│   │               │   ├── c077e5dbb32081881860c5e847d2909513875919b15b182dfab32d0341aea6
│   │               │   └── de1662201ef5e677745f5054219d0debaa4c2fcec5c686cc90561c75d46279
│   │               ├── 39/
│   │               │   ├── 05a5f4115608928c4c1bf892740f3662a163ad4fb503f93ee2322eb41487a0
│   │               │   └── 869c0db11031d05c0dc870c0567ab24e49c875e210c76718cb09122c79bfee
│   │               ├── 3a/
│   │               │   ├── 78695388b38b5cceefaf6796b0137877514593543b91af2752d5a17e3d736c
│   │               │   └── ca65754b87c739f59edf7d108574a472160e242f7166740fcb9f905fd4075b
│   │               ├── 3b/
│   │               │   └── ca9d58be429a9e9a507c2c31486d80a475e1c53683e002ba45d40231a51d4d
│   │               ├── 3c/
│   │               │   ├── 0b48fc82605fe676f17415632e8cbd4fb2a2108041b657de120996fe62bf1a
│   │               │   ├── 9898c9a918b09107db81a0512b28e1b5ae1371f3716f51ca850de5ada7f5ee
│   │               │   └── f5a1dd8004e8bb494626da30050a44f8ce5cd3532ce34a2b1f8881414bc49b
│   │               ├── 3d/
│   │               │   ├── f4d444ee0040c89311c2d73c3326794e46176bf3eb9d6c6a849a664aa51167
│   │               │   └── fb4be7eb8ca78a4b849b62ba4911baf3f1635b82549bf0df8c6fd72799abfe
│   │               ├── 3e/
│   │               │   ├── 1e1f43b06cff00e9bd8b3b778c436c9b173dd2e46a7b5b78de0d6ce1697269
│   │               │   ├── 491f2324282db8d41f0167d9241d7c2bb0c494806e124d0531010654a59e7f
│   │               │   └── c8e72b124d343aee970192bb15bf5df70c80eef3cad187ec1df3ed1123db10
│   │               ├── 3f/
│   │               │   ├── 5d843145228916427baf994327ef54fc2141fadb5efc332a3be14a9f8441ce
│   │               │   └── 9f62b0f0f284c54dcbddb4df38b373beb333b63d9ccb16356688fcbc553962
│   │               ├── 40/
│   │               │   └── 244a6d21bbf726760ce4b03466b8a1b68c528300338cf73c3171e846cf28c0
│   │               ├── 41/
│   │               │   └── bff9bf0ce39020837ac05a2c8fc916f4f2f40e51ee12a160bf0267e56dbf3d
│   │               ├── 43/
│   │               │   ├── 1d9d51ba5fee3474961901702c718019f539f51138037b7c89fb430c38b207
│   │               │   ├── 21a07774baad12456eca43d82e762615cbaa95b55b01ccee38de95c9752ac5
│   │               │   ├── 689bfd756be3977f891d973c8497813f8b93cce90338990cb34e44ab72535d
│   │               │   └── d20dbc87e337fd97d051cdc95d2e83a2f7727c2d39c353370b374bdc5487c4
│   │               ├── 45/
│   │               │   ├── 1d199da3fc4eb4913c4062496af6a933e1bc803d68aba072b793205bcad44e
│   │               │   └── 41e094ee9bb219e9ddceef73f08c3f89240e8d81de8419e967461aaf645734
│   │               ├── 46/
│   │               │   └── df773fd5c6fdbfac094f9f2509f676c9a43a743f70d9956168e08ca09d0ada
│   │               ├── 47/
│   │               │   ├── 5cd35ac41d5d1044d139a77696f62523036ea181097292b2e5a7ea60d8064c
│   │               │   └── ddd171ad2a3dba58cf9aececd7a55e96aca2797debf8e69af3da846ec0ad49
│   │               ├── 48/
│   │               │   ├── 711ded23f4d44a83ff66b4c8df126dce4846f218a679579a37c07e4b02f7df
│   │               │   ├── eaf50a3fd41c4a645e8800cec9b3e7bc4f409c81d9b84ae41289c5b3a6423a
│   │               │   ├── ed0004ccf9059e380a5c6e39defdd629ec0f6ca7e07f16db7f61c7595af7a8
│   │               │   └── efeab150b284c85e4fc00a1e5a96e918fb74a14e18cef6f3fb8a409127a1e1
│   │               ├── 4a/
│   │               │   ├── 67fb88704aac3c2bd6bb8c5d17208f2ca69ea25dc191269f9dc1761a8a5049
│   │               │   └── bcfa516046cce0b54e4f47f520b353d8d65a48d64ca324b0abc08121635e92
│   │               ├── 4c/
│   │               │   ├── 22bcda91b7a5a6e3b68dab26914226aaee23ea7d2451d9d87fd585c760a8b6
│   │               │   ├── 3bf1c49ca5aa726d54a1ebf1f63c1b8a76718f67202ebeac8fded59718059d
│   │               │   ├── 4e436f9a453c776dbf011f98d932d615988bb08bddec6051625340e88d012f
│   │               │   └── c13b24eb0a0019b4f4fff2f237b36c8ed17e43d7e7663945b8791a99fa65d1
│   │               ├── 4d/
│   │               │   └── 375658a3dee103e24a7a4bc7f92754e1a7e981bade529055cb96a01c852b8a
│   │               ├── 4e/
│   │               │   ├── 469c2281456ea6b8c3574a8de06961878eeb16282aabec232f3e7cdaa20e7c
│   │               │   ├── 5e0cbf77f93e18242398cc5ab3198abbaa18b586f4039b873f03fcde7c57ef
│   │               │   ├── c44749192e6403d781993ea22db7c4ba02a7889befc85700615b7872d9ce16
│   │               │   ├── d6a389b09b4429688c735a86f8a0f3b92d5176bcd2d9295630442404a5e6b6
│   │               │   └── d7561b2378bcc3783ff908636f33a0687da111975ccbac41d085218d7c9298
│   │               ├── 4f/
│   │               │   ├── 22047c6ccca17ed77b8b96ad6638fc34c17902034215785307430e687d1d47
│   │               │   ├── 7c52e4d53b65b6779e0356710960850c719e84d4345f44cca0a86d785f1e8a
│   │               │   └── f6a3baebc55f69a127eca51eeda6a21b39ed4f11852068669241c01e7da412
│   │               ├── 50/
│   │               │   └── 919781b25775f98ba5cffea379c7a8e81f25471addf7535cc4cd131589a2bb
│   │               ├── 51/
│   │               │   ├── 4ee3fa4b04c732c61e969557de745559fdda5f30d80dce60284d3d6a47c56e
│   │               │   └── a4f9d06653f4296e97fbafd83be390f30238531e258ef51d7f3d472d15cbb2
│   │               ├── 53/
│   │               │   ├── 1251010526f6bec2fcdd5c170b635dc11d6079a2a879af69616ef9b1bf8daf
│   │               │   ├── 3a5829faaa787b1ee6d77d3bdeb72aff57a3359def2c2035e2076de4ec3333
│   │               │   ├── 53a85ed48f127b7ee0a50fe5deb94bbc3a6b0ff1c978f7482d575ec0416090
│   │               │   └── cf8f0c070d169fb3fef827c700769e2a12bed680a6cbc8ee95fecb9494a91c
│   │               ├── 54/
│   │               │   └── b1cee77d814a013a49ea5812b9ba5f72686c8390a7f653da473595396c31de
│   │               ├── 55/
│   │               │   └── 6c562ba8b8aa76e703a7029188edefca6d536d72688a9d6b7aee2c06fbf527
│   │               ├── 56/
│   │               │   └── cee6eb2ecfd36fe8bf42ad458c420366d182b14444c83225acf77adcc38c11
│   │               ├── 57/
│   │               │   ├── 1d79913e456ce411c60f77901a1f6cc72dabca59e88db9dc9d23a232f56d9e
│   │               │   └── c15e82beecb31d830c51abf5f93134b0c1de035d194660ffe1f1fb25357ff1
│   │               ├── 58/
│   │               │   └── 72c0705cd5e683402a13a73210d29c8301a5e3fca7a7e59e50d6053f783924
│   │               ├── 59/
│   │               │   └── 7a6975d9ebb9dc54ec8531e4fc6296b2b4c0d9ce27f5e8431449f5e1b56f49
│   │               ├── 5a/
│   │               │   ├── 37ca080e42967d4a19dd68d8aff80cd9c8eb2dcd02a4d0df11c49a09171ebc
│   │               │   └── b6ffe2e3a90be4534dc7deb10cc2c39a12a07b3db2fdc1407d37c9a24ff07c
│   │               ├── 5b/
│   │               │   ├── b4cee0ce4ebdec75855f7910ccfd56ce0e5b23b07d2e3924308557890541b2
│   │               │   ├── d4b2fa17815610d897c1dbfd754724e6e17f5d8607dfbba9dc9a09b195d453
│   │               │   └── d7fa4c5a9f6512886109baae864d51b7df7e83c59386d96e1730231d996117
│   │               ├── 5c/
│   │               │   ├── 89640df2443aa0d8cc29262765c2de8514a348524c3c271900ab45566232cc
│   │               │   ├── cdb18abe60328a96f7a98b464b9bb2574e3ca7331c6fb80eb22e19c580bfd4
│   │               │   └── d7fc4959305430745f5ed3534b06dd721a74632b616047ebcd1a07d67d17a5
│   │               ├── 5d/
│   │               │   ├── 0789ecd9045f31da1715b883c61d6bbbeb4fc5b983d4091588d7edce429fc9
│   │               │   └── c5c9d9b62f7fc4bdd8f3206f7c30c0e07057aff5aa652d0df26dc53fa9cdec
│   │               ├── 5e/
│   │               │   ├── 4e6869431b397914666f2b29bde912e1e5a98199db701d5f4b288384c7b154
│   │               │   ├── 619d06c5c8bb5b5a02ab90137b2e929833c519d06253c997a89e0e62985ef9
│   │               │   └── 70a6c2a26430305b33b80781fb68b5d28d0c1e71a4d0fda746172479d0e138
│   │               ├── 5f/
│   │               │   ├── 0b833a96ec0aec240d4945019807eaf088d4f47d501e20e79e187b26bd7e79
│   │               │   └── 36b8a4f025d442891deb578f5d9e220b015fb26670be0507ef7584b8a4d30f
│   │               ├── 60/
│   │               │   └── e5949e03b0d5b2d4d37a661c1d9cbad4698b0e7361e80bdd1fb416c0d777ef
│   │               ├── 61/
│   │               │   ├── 4656be7f72414643e18e7201e39583900f8007f9b2f972f8e9d4ddcde26078
│   │               │   ├── 7b86ae8a2522fbb9fcd927669f2caa9520a0f64edc4bcd5d4f4d9d9662884e
│   │               │   └── de4eff5cf53688173ab22458f361af6f6186e4ca4b0eff75f3f55847eab51f
│   │               ├── 63/
│   │               │   ├── 582519d06633dba633befe67088a06e0abdc9e0cbf034d0ec1ca869fa36213
│   │               │   └── 698f5cf1367fa4ffff4e36b5e6a388931590bf13755942da02ab68665a45d6
│   │               ├── 64/
│   │               │   ├── 4029a1cfe36bdbb46311a2d8fefbd9df91fe5691e67f6c8795f54c54ed71f8
│   │               │   ├── 88d6ea4ee61c08079abbea8efee4c41a8639a95898725b0ea2f05087479290
│   │               │   └── f72cfd451333ad8e1f7d8a3a8d1b1e39c649bec4bc6e02b5b7636ff28831e1
│   │               ├── 66/
│   │               │   ├── dbd29f48030fa684e85955734a5f9e6470ea4addf2e8570b97dd925dedfba0
│   │               │   └── e60d5bb9b4a210ee40144d3c33a76878ff86642bca601dc4418fe0542f4175
│   │               ├── 68/
│   │               │   ├── 674790ab6f2c8f70ca711c392e3b8447c742ce245883178e49b1ad414366c2
│   │               │   └── a2d31b07d758ad5a731effd78b6052e7a69b0e44d60d31400db7985c7f743d
│   │               ├── 6a/
│   │               │   └── 5607a3c2d4bc9c8d2ab957b3288615891d5379fab40fba247827d514f3fd16
│   │               ├── 6b/
│   │               │   ├── 5079b8aa71cc7d1e63c57441cf6677a8a972ad712c8930d6c922349b7bfa65
│   │               │   └── b4764c774cd54e6d97a995c8736cd093b8487da21362df4d27e050685d5f2f
│   │               ├── 6c/
│   │               │   └── 6d08fb5ee3326c00c6332725018a3a2a0349ea0291fd9f7d3d98dda94c3aeb
│   │               ├── 6d/
│   │               │   └── 73b3f7ec0671f0ea0621b80664486ad339e05572c4ec34d5f5efbe9fe3a630
│   │               ├── 6e/
│   │               │   ├── 16830ae23f6b7147dd5ef62459f972194df016b6b8708ac3a2a76ad5fcad36
│   │               │   ├── afdda7ae66fcb668d858fcb00343f660db1291525fcd2fc93b71dff5f6eeef
│   │               │   └── d2d979ae7c534e25317b5760827fda5f9be9654c7f9bc524080d062cb4f755
│   │               ├── 6f/
│   │               │   ├── 2c4b9f8c6077793de797f6bd4ddac57b33ccf67e8f8b472df8c86f418082ce
│   │               │   └── 58845b50df9a8812cca8d4f3c3bb9efe5939c5f86489da7aed4af3e344a902
│   │               ├── 70/
│   │               │   ├── 0b78a220adc42a77e52418b87f3d1f9792490c7bc879d960ce9d7b938a2b8e
│   │               │   ├── 11377ba62d5c64fabcbbe1f7ada9bd44663e462adc8ee9869b5afaa994a5ea
│   │               │   └── 6bf1a4e30a45c09272b0ab99a32a2c2b556106edc929b96d7c5b545048fe62
│   │               ├── 71/
│   │               │   ├── 1a1238d3b627bbaff42b2254a63b4c2f1ca9c4c0b03b388d9784a42767490a
│   │               │   ├── 3658bbadd61108d8090898cd8a7120a82a8639a59c84f7a7da6b26fd45ad85
│   │               │   ├── 3a92a6f35e2100179cec7de3c2189ccb03a159f80d22271a8df5d7e554e49e
│   │               │   ├── e3d80553ee51892f80f9fdfe1208f79ee16610e3b2ae9b20050687e18d28ba
│   │               │   └── ee933cfab88aadf41ba80e25123f3d0b31a1aff8ffc1caff3ea7606b5638f0
│   │               ├── 72/
│   │               │   ├── 55489fa02573f75b106e5c8682abf60ced2bddacb7a7a0a91ff57de85872b5
│   │               │   ├── ceb13fd79a594294d73a17d599411f34d2410abf8c489e5b75cc36b1ecd445
│   │               │   └── da3094cd4105a6ce1b3ad064af39b3547a80f48b7fa9c27af487494c4da260
│   │               ├── 73/
│   │               │   ├── 32ea057b36bdf4341c6e27ffec6c3cca83069e1dba97837412eaa7e9a88afa
│   │               │   ├── 35ba9f8cf9173eff2e3a5263dd9212aab4feb976c4998d2ce8b2f156fd4e20
│   │               │   ├── 8eeeadc3edde5b48d7c8f4a0b837f2249178a74a4f1e590b449170fb0beaf2
│   │               │   └── be088e88e1a4e24f1193a5dd0ec3b4bff9c1a2130da3c3e386c676cb4d1d67
│   │               ├── 76/
│   │               │   ├── d5d2ed8c3e2bcef1476c89e6d8ece7a0b379b592f89ff7669668c3b6231cb9
│   │               │   └── f20e4f21d32454e4ccbbabbf6adf78ec95abcb9c60b64a274ab8ad2c3d7ef6
│   │               ├── 77/
│   │               │   ├── 9eba5a7f8bc750731ea4839af7b431fa954e7be32bcf43e1420218230f61a0
│   │               │   └── f62bb178e5e4a8e54cc34653fbeea9b2acb6bfb5b288461e2d4a0fef449c51
│   │               ├── 78/
│   │               │   ├── 260c5e2493d53e1cc9a05b56d01391e6281374e159dd0c1d615536db98aec0
│   │               │   ├── 51e885a060b47c0e50cffebf73062f72f462c32e7fb0986f7f38a4a10c856d
│   │               │   └── d72f211d7e8242c019669ee9e950525f3d103ecaecb388006f9468eda3bfce
│   │               ├── 7a/
│   │               │   ├── 057d9014c25f4b76198a8779e97d958c5f1386f164f8aa91e8b3fae6abd568
│   │               │   └── 646f34f165d7863c70687015ac6416fc81e119cf8f867cf906d1a568711b04
│   │               ├── 7b/
│   │               │   ├── 17204a4edde5c7b40f5cf13ebd13bc1f231e7a098527f049dc2c32ca372b0d
│   │               │   └── 5d4789139aa089f579ca5a2261579849a889cd2a0518e55f94e4f0f8e1e267
│   │               ├── 7c/
│   │               │   └── d161554b00053a66cc4e235679014b5fe8d7ad1d23de69ade797d62549f548
│   │               ├── 7d/
│   │               │   └── 640c28c0705b033a4b16fe740a04e23463bd457462b16aaed9daaf177dd471
│   │               ├── 7e/
│   │               │   ├── 1dbc1110aecfe097d8f86fe19410161e74d12a58a0ea1fef8809ad81124306
│   │               │   └── 2a21f09ccc214270180cffd6a802fcb5da79f6d0afe4ec97ad7f33fbe6c14b
│   │               ├── 7f/
│   │               │   ├── 53770c6fc9a4b6368b5d8693ad59fe612232f13dcf1b8358180f510bc97ee9
│   │               │   ├── 7027e12aa06680a90f1a77627930d1bbb6b99fae0c7268b599dc7497b59264
│   │               │   ├── 717bbdd539c963b4d3792cc2557b18946dc22fb46ae6adfe9d24b02f15fed7
│   │               │   ├── 780be62ae66559f2958cae201152a8de57515d9563b58041cdc0b1fc0b2e02
│   │               │   └── e2d8e61ed89e8fbeb993247d2e993b4823a1037d42e8405e5fcbf0ccfce6d4
│   │               ├── 80/
│   │               │   └── c4a4cbd716179311441280d346ac16f88a7ab2a807d9d67e904d9db008899d
│   │               ├── 82/
│   │               │   ├── 9a24649d56a58ea716d2358df0eab0ef1384fb75d1fee4e24aaa19865fc95c
│   │               │   ├── afffaf890eb3eb648acb05a6e440402892ef5d79d578a74f25dceeb2cc5375
│   │               │   └── db9282a41f8ceb74337cc24f994ddd1137e2b346f1c9383cfab0ede2d8e4e0
│   │               ├── 83/
│   │               │   └── 26304b9b5c9b85589e43e687240c4cd3895fbbf9158ce9e2f6ee8f0a1c1f05
│   │               ├── 84/
│   │               │   ├── 037b81072b618eae23cfedea88dd902d2aab86f8be2b0dc569f40d7a02a301
│   │               │   ├── 12f5fc6d1d405b15c91c69192c1e59db8e602fb381ccebd1847582a21e5062
│   │               │   └── b1e0eacbf30e2919561e86db5d4f15b41366cd6e1c421514cbf0241c0ead23
│   │               ├── 85/
│   │               │   ├── 240a3bc12bf8031b3001ce02aebecffee307ad000a3b165bde5a480e7a9db3
│   │               │   ├── 3c0517e90f41087238183992506ab1dcab0812e79ecc0ac824f5dbd192c2d0
│   │               │   ├── a4839cb8073e327e801b4aa1e33f94c4937090077ebfde95cb2157f5a41f17
│   │               │   ├── dc7dfbefba038b38ed877dee171ab0379a3c066a68d3bb779044f285536d8e
│   │               │   └── fc8f1d8aaa1881f365e5e03e485dc3ce0f1f31decbe705adc3080b8940277f
│   │               ├── 86/
│   │               │   ├── 3d7ed639b8b82416c54c6fcc958364c0a1fe727eba0dcf978ee29bdf9a72c2
│   │               │   ├── 9a6a5a81f672108dfffada926867d557e9682a58665200d2e885730cc5346c
│   │               │   └── f079e0bd8b9038c3095e1cf9b88e6b02c49850f44220dea21ef1b21af3ff73
│   │               ├── 87/
│   │               │   └── 1686face6576b6a485f96aa26c6973e6887fac4998abeb537da5c87e23a891
│   │               ├── 88/
│   │               │   └── 5e351ca3285ead12e042590b6b17cddea7ad39f89e110193509a4552ac6c71
│   │               ├── 8a/
│   │               │   └── 5f7fe2c7b7bcaff10bdd94c629e55da4e16c43d23080b8a72d33bfff77e36e
│   │               ├── 8d/
│   │               │   ├── 34517b3dd5991cee32673c06bb5238239de74e203aba4fd345a30195c0bfea
│   │               │   ├── 3731fdae1abac3da592591a765e14c80789838f36437bf040f8f22ae98b247
│   │               │   └── 99840ecd27baac6d482eb9a22207cbc2c34887ed1121820d184bf4f412e3a5
│   │               ├── 8e/
│   │               │   ├── df08a102bedc23ab42de87dbf54934931dce8d42506c6dda59ad8f0d871863
│   │               │   └── f58efc408c8cb8ab399c3dff03f93136aeb545b18fc01e3e2b3562c935ad47
│   │               ├── 8f/
│   │               │   ├── c1213ea092e22c325fa5ad42f2e3bcae32d7f5f3cef57979a008f427e9d7d0
│   │               │   ├── c35debd57a70e7da2c78f170e045e4d102baced397c98c465d14b8aacfc0cb
│   │               │   └── cb4f06ec334eadf27f365cb5f7b336e280ce0098dea2bb6ba5ab8e8ce654b9
│   │               ├── 90/
│   │               │   ├── d0c6e6e1a73f80f71859853a73acd40bee51d2bc988e04a11fe083da772745
│   │               │   └── fca1a2deef1b934f9bb5438d1c73f281fb28adb69411d098a987807b8639bb
│   │               ├── 91/
│   │               │   └── 3aaf4403b9ade2e9f77cde5a51086d883027e51b0b707507b44b9013f63f25
│   │               ├── 92/
│   │               │   ├── 30f4b80d002be761647dc1a75a979c7a5d7d5339fedc4cdae2aeeb9d366031
│   │               │   ├── 4fe926ec4cd47e0304801483afc663a1829e779476c492f7be2996fdb7717c
│   │               │   └── b9caa5fd19144b5bd1bba6ec83668f106f81e52903398f269d8cb64f18c1aa
│   │               ├── 93/
│   │               │   ├── bb233e11bc2c0ee283a50df81625bd96310a463a6272519bb2d17dc9ec8249
│   │               │   ├── d25d398c9e08c2301355683b178c779ce59aa9ce3056660ff59bd272735a3c
│   │               │   └── e5fa072965f32738d7767877cb20b6279ac7f2555c37f1be3b552c85d35455
│   │               ├── 94/
│   │               │   ├── 1fb96cea93f9e4de6876a74fe5aedc60ca3e14cada21420abc4488aff39c2a
│   │               │   ├── a1c51ed5afc909b8a8ae5ad84f56ff19bb2ccb320ef92544ad5d87ec4f4318
│   │               │   └── b500a557b849d4c2351f2bdad0b278443afc136578add3dac23dad20f1c909
│   │               ├── 95/
│   │               │   └── 2157769a5cf041b4b4160baff199aca772a943443d75a0ebc8cf970d098ec7
│   │               ├── 96/
│   │               │   ├── 1552b77abf7c171167c78e370c1b403869756e788ec52c1be9fdbff7b2908a
│   │               │   ├── 548cd7978f6d736e237787cf88afa86207b1212fb7edce91414caf17932807
│   │               │   └── 70373548b8fa21531676109ad338263fb0a92ecb19520d1831a8b62897e439
│   │               ├── 97/
│   │               │   ├── 59a78d5a5de5a720763161b898db970d2b1c61b5f7c10ecb6201e8f18a905e
│   │               │   └── d23d31ea0445b3b6da9f1a8a635409921070890558218fda8c55ed2d518699
│   │               ├── 98/
│   │               │   └── b154ebeefb18f0d89106cabf20003ebc5ea1045b8c401c014b8a639e24d30b
│   │               ├── 99/
│   │               │   ├── 3b2e539fe78345305353b50889f5937ea3066259287aebc64199cba861ffc8
│   │               │   └── eaf45d52ebca24fd87659e14a6479150fe84e9f7b813a7e0a981168b872934
│   │               ├── 9a/
│   │               │   └── ea98b42c3fd3ed0ec3b101f80bb4a8c0024a278215223e457c09f26c80181a
│   │               ├── 9b/
│   │               │   ├── a0636916275e6e99e67285f32c59acdb77ff27c219d746b7ac036e013a5bf3
│   │               │   └── c4024f9f30d4f17a7689e9224daa9922c1ae7cdb80c160b2f488a07dc4accd
│   │               ├── 9c/
│   │               │   ├── ce64096a34a558a31ba7ff9d177d232c0206705337bde319aceb17a3670eb0
│   │               │   └── ea9e1a172baec1d72e5738a091ed5066a8a6f8bcc1d7083ae43b853668632e
│   │               ├── 9e/
│   │               │   └── e8395fb54bf31c3255759e33371ac3cca37971a584f000386cef6ecc86d43f
│   │               ├── 9f/
│   │               │   ├── 09412d4907979d035e6548c38ac8ff04ccc98e23cae749e631d2b50c6d57a8
│   │               │   ├── 0e6d130c33953c267f289912624ec90236ba04e1fea879afb620d74d640c1f
│   │               │   ├── 268a25ddba1977aa562ac6c829d53c34fd9f1f309cc49dc4288ced9d95329f
│   │               │   └── b764b2824046cb629e2e55be7f91d6a7b8dc17e53df77c33cea5b8b2ff4a83
│   │               ├── a0/
│   │               │   └── 3bdfb1cd3e5236a4a20b33b00b729ee81d3865bee5bd0f1211010827d87df3
│   │               ├── a1/
│   │               │   ├── 34d32eb0310385cb512029719285ff593d4f1e73199db60afe326ae7ff16b9
│   │               │   ├── 5ecfa1352fd1fa0ed4d8abcbd7a0f54e10d833ec5b3d6f964d261e29e1753a
│   │               │   ├── 633bc37c5c2af18441ad8edd0709c9703282b6175111c15aa528a12558360f
│   │               │   └── 8be9e521dc3643b9cd9f175fc1d6ca4f29060d87c2b32e9f5a3a46fdd1f6e5
│   │               ├── a2/
│   │               │   ├── 008498838f12fc2bcc11e79114fa931afa9bdf99f72b669830314e45b216d6
│   │               │   ├── 2fb0f1aa03d1dc417bd06f071b0527cc1bf6801f29ffb391320e95f34e373e
│   │               │   ├── 8e2ef91e74d4e0d9af056141b1aa5c6a84d61d339e66103419b15ddf62e9ec
│   │               │   ├── b5b04839f2871d9e7fba964420ab2d8ecb5a621f563ff0f0f2aac69f04b38c
│   │               │   ├── de30270327b4720fa912c0c5835ee4a494851c404902f557063c7c6f87e6cb
│   │               │   └── f1a550f4aaa3403d4c76d634e36f971106732575b443ca5a94c13d0e3a3c17
│   │               ├── a4/
│   │               │   ├── 1427898500cf5d7e3b8efd42288b3521bcd5fd99607ea2dbad9df968c11618
│   │               │   ├── b4c6d625ca850c26e0225567ebce4c0638799f6665a4af6bb55c000958867d
│   │               │   └── c48f9eea773cfa7b5217d4e72b9e7b339c0675ecca8a4d8dc7bb9aabf545ea
│   │               ├── a5/
│   │               │   ├── a05f1a9e381dfc1db1572709008dfcfcbdff8330167a126885d5b081953ac7
│   │               │   └── ce0567a59bbb95a147ad313bdbb5e9a6f80e3b1071ac421f6b3d4183b96d22
│   │               ├── a6/
│   │               │   ├── 53538fe99ac7aa8c2784e88c9d92b750598971c2a7eed80d2e3124535862f8
│   │               │   ├── aa48554c535aede630a881f7192ce9e95db5ef23951641aa4756255e8a09dd
│   │               │   ├── c854957225d3db55f54fdb940986da035643315225dcaeaa7bd886a9a0b042
│   │               │   └── ea9eca2f0fd8b821ed941651a07f433957b83e4deed7e7231cf6f689d8ccf4
│   │               ├── a7/
│   │               │   ├── 3f96d849ce9d605cf862ad34599f0797b1920c1d3e2fc4c887cb59c33b8a65
│   │               │   ├── a1686235e700798f611e91717196640383636363ec80d768c330cc6d8fe63f
│   │               │   └── c9953c4ebd86cca4c4959b2aa29e4743a9108178dcc0fe2c3e672a21b5e802
│   │               ├── a8/
│   │               │   ├── cc23ddb51c0e74be6674354c198d3d03ecfcee7d23d30baf5ba29bb0cd66f6
│   │               │   └── d5fc70fdb86905526b9579890182017fa01cb8571dda5c983235fcf551f5d2
│   │               ├── a9/
│   │               │   └── d9e4328b199389820b0cd55f632524fd054ac61dffaab2787fd86dd17983ab
│   │               ├── aa/
│   │               │   ├── 491722413603cca1f3a47fdec15a02158cf3829169095d28cc6473049523e3
│   │               │   ├── 88f9b05f0d5dedbc4801e7af4f3c103d5ba81abe808d0b75bf565419c33e6b
│   │               │   ├── a0e30c6839aad6c40e9c9b20774f284767a710b28fc48c0f23c51d8fef870f
│   │               │   └── dc531eb827c1a74688a3a10621186abed6f579f7173fd599fb774d7563e5f0
│   │               ├── ab/
│   │               │   ├── 33b54f032203b8633e2fdde0f9857f0350e262a479cd0e9050d467a519b21b
│   │               │   ├── bb62bdd2991c0e0ae466c64f16527e36fbc886947b58a4d474ac03c39936b7
│   │               │   └── c096fde5c0e7519fcb17be19bb3c86cf6b3c8079896129a98aa010da7c13a1
│   │               ├── ac/
│   │               │   ├── 8fe3840390f9835a8904237c7054bd4ee0aceae92eeadc588a9d5c7d3877e3
│   │               │   ├── b418e8347c01680d53a837227020a598007cf23fa79e4991a57cfc392f7891
│   │               │   └── fe077647bfb75ea56955606afdc05a16184b45b35ea23f77763424ec1bef5c
│   │               ├── ad/
│   │               │   ├── 3462c1503ba1d909cacc959f8ee96424190038a5ac7ced5f5fc7dd6839910a
│   │               │   ├── 3de1e36946a4311545bc36a4eeec565a8d126a3fd220cf5adc3d64ee6a24d4
│   │               │   └── 735f32cf2dabab4943bc477308d1b8228f03912e913c37b70439f1458dfeed
│   │               ├── ae/
│   │               │   └── a98b8058482a0b71c9b67d339eb45b3b0e746af96a11cdbfab810c099a84b1
│   │               ├── af/
│   │               │   └── 9bc10db82a427568dca37ac69bd91aa0aeea461a1c2b411c9b895ca2e54aeb
│   │               ├── b1/
│   │               │   ├── 5e85f8317026c4c8fd9dd5a796a01defe46c6db350d7e87c7c9f8ed44efe9b
│   │               │   ├── 862fbfc67a832597de78bc9a0fcc57660ff2366c2922ad0a209c4222b4e34c
│   │               │   └── b1474612d10ff3165c55a57c3803dcb4d3de4ca0b28baae44ddd8f21fde553
│   │               ├── b2/
│   │               │   └── e5bca22395754bc7201e96b2b02289851cce6945b939836f8b35506f65dc1e
│   │               ├── b3/
│   │               │   ├── 28d3db6d0c11bed2ccb7065759d8d3f6bbd9428f9cd1eb8ae5d424d3befc20
│   │               │   └── 2e91870e7fc06f71cbcd0f5d01adfa5c97f9b918010403c59ada91097e061a
│   │               ├── b4/
│   │               │   └── 9d4b8050e207fc3da10561630d43cdd5f6b4fdaf85f0423fb8a58f20e41f29
│   │               ├── b5/
│   │               │   └── 962ee97213d04243717791ac01e6d190aff82508812a68cf21bfa3df56b4ca
│   │               ├── b6/
│   │               │   └── 29a1f5443ef3c95546f1d5ac0af5bb2e293900cb9e6aa7b0916cd1d00e5780
│   │               ├── b7/
│   │               │   └── f9051511b52b858877c30e7f1f7780086d2b191419c957581ba72443d071d1
│   │               ├── b8/
│   │               │   └── f65d0e5d7de5d1ba951ae9bd32c722d3a728d14d79046d3e41a0810942a6b2
│   │               ├── b9/
│   │               │   ├── 03ac58ab61a396e1ccb8c8ac90f164d0c10280e67126a7c690f61b5107df66
│   │               │   └── 36e833f0aee9829a7dd35393c778ee816d7d2ec3433e7629c9d2513aa329b3
│   │               ├── bb/
│   │               │   ├── bd0bff386c7a32cddaa9368e87d7d37334dad57fd1afeb1baa539cebc87eda
│   │               │   └── fe3ab18beb5fcda58c6892131246fb6f851a2ff74a2f5570b5f7cc8f1c55b4
│   │               ├── bc/
│   │               │   ├── 2182b903304de3399dd66e8e016958f809a95d85c34d4cdf8ede6fc990423d
│   │               │   ├── 498617ff317d4eb32e87184e871237a7a531f705f21c7c75ab2ed0175d030d
│   │               │   └── 9b9008b516d662fb4b9d50157abf207e986b47230c7ed3de750e0a08a7c90a
│   │               ├── bd/
│   │               │   └── 04567b1e53def214466bc668a8de2e7589a36e2a8ce2f0fee60040ecf96c8d
│   │               ├── be/
│   │               │   ├── 316f2201fe24eb666a2f2a7161fa1bfcddf0176b10a22762b438dc7fa5d6e6
│   │               │   ├── 90d1aecef2a3d8606f486dcb4935895ba142c3b47d37fd75c618da489dbda0
│   │               │   ├── 95676f875dbe1ed653aa3270940d5093114ed4c507112aa643f2dee829be14
│   │               │   └── d21474221fb80bbc58a462fadc38218f33ffdf2014402acc53301d3e5f7d65
│   │               ├── bf/
│   │               │   ├── 0386dbedfe7ec8677664d564b9cb953804e901af82f9df6413b5ee0f3e7a74
│   │               │   ├── 65d720ecd5a870a551b6e2af2f9ed1545a91a612119f071a4d7145892e8801
│   │               │   ├── 6bc0b2ee31345100572fb539a65f9bbb7ae04b3392d53f663e0c9bed14384d
│   │               │   ├── 7f5ce9b224e1586bb092e1804e2f8559d0b6d6fed9778967482044f70eadaf
│   │               │   └── d07b602ef853a54e29acc2fe17bd6b8308bb1e6848b7ca146c5fad1432431d
│   │               ├── c1/
│   │               │   └── 8e3fce589275c09a49f1a4cc7677ad37b290a8c78dbe1646be80feb378da27
│   │               ├── c2/
│   │               │   ├── a59d3cec722642525d9639514c6f4fd24c0292d5668a14c5a7c36bee5cbbb7
│   │               │   └── f0bde65540068b225bee9daff2571ba7705273b4e4e031db34b01fafaacb97
│   │               ├── c3/
│   │               │   └── 10195511914fa4ee2be29d017309cf6860ad2442004b75baaa2c66f23d7a63
│   │               ├── c4/
│   │               │   └── 75fb16a0a38c10c1dfdabab30c1b77e378d30ee1498bdb8f6399b29145ac1c
│   │               ├── c6/
│   │               │   └── 2958920b36c903d5d4a8a929142031bfead7b56c6285a604aa895e9fab31a4
│   │               ├── c9/
│   │               │   ├── 11c02bd1785fb880ed3ac38bc81f6e6b9ea57882cd81253c23af31529c48f8
│   │               │   ├── 8d8eb119a9df9a1795ee53ae9206a5e893eff63a1e928602cb159299853f9d
│   │               │   ├── c3da26f95bb86eb05aeb70cfd28850446cb9d2577313e1ebd7eaeb879bc270
│   │               │   └── d5e20a5f7b3fca081d0e9fefda3ed37bceb84e645a9d71e24adc07baece46b
│   │               ├── ca/
│   │               │   ├── 14ebbed9e097e62b5bde018598738bf2e80f069b094b9e699872e7c357404f
│   │               │   └── 239969b62a2fcca75b33ef39916facae28865072df9e9d6cd3804e42acb906
│   │               ├── cb/
│   │               │   ├── 2747846fce151666135aebce8a8af85eb1eea8cdbde7f7e7ea77f795066b00
│   │               │   ├── cfdb47266f87707944aaaf87a8dc65d1bef287c103906a72e569d898fa290a
│   │               │   └── ed25237d7f7171e724523fc6fd0f70df22bfad69b264149117aa8356936332
│   │               ├── cc/
│   │               │   ├── a9fa886acaa133db21f1926d719845ab48c2d55a0e74f9d3be42b01c3ff902
│   │               │   ├── cca6c3bfd574eb97bcbac50bcd9a577ae1f9ef049eee6ad1ca713bcf09be0a
│   │               │   └── fc43bd7f53cf442c4a213d44d83cf4bb48642d2e0eddd75b84fa02ee74ff4e
│   │               ├── cd/
│   │               │   ├── 2755f57f370fa80ebbd08c755b23defe581bdaf21250da0728bc34e6d27587
│   │               │   └── dbdb42226d3b3d711b52f649688ab7aa0fb3f57159d7db698296d1a0142485
│   │               ├── ce/
│   │               │   ├── 4fab0bc413aaf97e0cdab703ffe132db6108cb63ab8619f7c323ac2597554d
│   │               │   ├── 56e418f60022276340ba06bab420db1a39b86f2417cf2b901f88438c6ac08f
│   │               │   └── 75477f57775470765c49fe0564da2e4cd356688f21e2ae54ca74a5d88b17dc
│   │               ├── cf/
│   │               │   └── 92a9502650587c6b587bf0bd2fbe8408688be12db457cf57d12d7fa7447406
│   │               ├── d0/
│   │               │   ├── 6458512c8688899759a1f46c220edb9c29ef2ebc88a4df0c5af9fb7bad856e
│   │               │   ├── 9587fd60259be768347c635d658258d05b350c405bfd8808c3167617c15992
│   │               │   └── e9d3b7f4e2a951fed4c190fc0951c8be6ff9994cb7829688a7f991a71536e3
│   │               ├── d1/
│   │               │   ├── 974bd06596719580558f58eb297118a7afe09a544da9e1eefaa77295f81aa1
│   │               │   └── adf2390a11c4437b01dfbf3a0bdf78750fd0ee85614df683fe95428b8d6199
│   │               ├── d2/
│   │               │   └── abc77d850e0b605a6959769e27a56397c4c526e257de1ae37d95e423776b10
│   │               ├── d3/
│   │               │   ├── 74f462f2e961eb74c5ee4308c5ec20b01af02d6a41ea7c4d6770c64cb92729
│   │               │   ├── 7d7c3f2450e4cc06c78ae44aea15a83296b89f721e11f9da8ab9586e1ab823
│   │               │   └── a338e0c4d9ac6358543cf4a87c49672f9ebbf2738a215e7662826e1e38c446
│   │               ├── d4/
│   │               │   └── c7cd40aed60ca4551d05eb3af6f8f44a3b2116a00491eca3c1574f50786aa5
│   │               ├── d5/
│   │               │   ├── 111862e21b074fd55a766bb7a7dffb623901146c2450513b4ed8168352858d
│   │               │   ├── 6e8b5aa0b2d353831ffa874a40ac4a3b567b7f9ddb9f7fb04188d1a585ec04
│   │               │   └── bd3094d0ad18bb35e581c2994241c11383381cd4bd274ec339b250c609ea6c
│   │               ├── d6/
│   │               │   └── 06482ef8e35693c72ffb62dcfe1da6b62ddd869a17b478a2397da14b3ef59d
│   │               ├── d7/
│   │               │   ├── 92c6bf5ca0cb6a01484eb838c34af15433bcb0da692b9084a472d9c4b505d9
│   │               │   └── f7adf488444d2844a903cbd405a853b75987b9a73c4d36dc716c8ca01fb3c0
│   │               ├── d8/
│   │               │   ├── 2926753f513fd8557263c0003c7618ac35a95d5b8c4acd57ade2cab28e343c
│   │               │   ├── 460058dd46e923c304cee7010502aba8c4093fd64832454cd7047c0adc7473
│   │               │   ├── 7b73fecef1847299e33ccda85a905e1f60a0edbcef8403c29bc966ee7ac074
│   │               │   └── f175350649049d225a294fe5600ee57d2b4b525922a16ec2d998fe960c0f3e
│   │               ├── d9/
│   │               │   ├── 758cca43dab9b7a0ba8fbd6ad2ef743596a876f8698993dc12899db4060df2
│   │               │   └── d29ddcf7532786a17bd26fce1a2531c5ee4b81363470a4244c18d19b3c243b
│   │               ├── da/
│   │               │   ├── 306950097910af4da2a8ddac5c0b94a5163e5622e022fb023dc13fddf8b0b6
│   │               │   └── 9b6e9297bd8a1639b1fe969ffb27871e756c7c47cdaa8b1bd8d3170e3f4369
│   │               ├── db/
│   │               │   └── 7c3c9c966126e8cdb8da24f8ba985679e20d453b433c7558e61a7420ded00a
│   │               ├── dc/
│   │               │   ├── b4b01dfbf24b39d2ba359117133e02f3dbbc51ac1be23f4921ab97d4a0590e
│   │               │   └── fea998fe1fd8b380872a1aece45a0dc84ea6c2a026018414e86ea08222b1b1
│   │               ├── de/
│   │               │   └── a955960dbc5181167151665d3e830e75e182aa1fef649ce5dad2a1d9902ec1
│   │               ├── df/
│   │               │   ├── aa9dbda13a908135da34734e4769f2c726960b521036afe2a4bc7f8c73ffc0
│   │               │   ├── b4f236aae87abb1af2c130f9a4ff24d8c53a3013f1eebd24fa995c591a47ae
│   │               │   ├── ec92bcae9c2f53c49835dd78fa7e9e7c044dd1ef756421bd8233b8c15fa9f2
│   │               │   └── f7d668778dbb778cfe4f4703ce8a8d4095a76ec5ce6b1a55f00228a7e94b69
│   │               ├── e0/
│   │               │   └── 778b7e8d6167d102f441cf4ea108beea4f2c145f4516d6aa4648dbb88d40b9
│   │               ├── e1/
│   │               │   └── 6915de1ee145b4551bf365486a617cad9de4723e8bd4e1108200e9fbcef526
│   │               ├── e2/
│   │               │   ├── d9192f674a47c18f902a92fe4fc98f89c0062c9562f00820862078e936178e
│   │               │   └── f5e4f0610544d12a1700fc9ae5ac503ef11da01cc70cbd7ba6bd5b34692f0d
│   │               ├── e3/
│   │               │   └── b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
│   │               ├── e4/
│   │               │   ├── 5357e75c488a7e619aec090ceaff01c1fd600d0fe1877056a63f64d1ec5ab1
│   │               │   ├── b64b15e73b5ba6fb44e2ecda13b540b24d0f577717b8093ac395e1ab7006e0
│   │               │   └── bd289bc0bbfb364d99dfb54983c08b42ba2a4e667dc40d363533c56c27f214
│   │               ├── e5/
│   │               │   └── 4d3484396d913125c7a386ae59d7ef7bcc69ecf0afcbda0b1fd80e80aa2db2
│   │               ├── e7/
│   │               │   ├── 591df7f6a1e22bb4ce1410b0b80cbd19b54bed12c2fe21711e096493b127aa
│   │               │   ├── 71c382aa34051b00868eff65d922b969dc3bb7b1eaae356637abf78f9be551
│   │               │   └── b6f769d82755c23796d1feaf48b792bf193a9a87ec0d01bcee2f895a767418
│   │               ├── e8/
│   │               │   ├── 5ffcf7b887834d43c47f95dd38f4ddfdd9e16c8b6443d6e18b567bf3ba67da
│   │               │   ├── b82b1b0d2c78573a11b54863535661f880a9935ffe4641a9d5eeac39ce74d4
│   │               │   └── cd2b80809d08cf17aa2578e03457589071f49e71bbd0a32053b375ff846d91
│   │               ├── e9/
│   │               │   ├── ce90c2051f34bd54fb944dc57d0682e7973bb52370b1e13840b53ddc91baf7
│   │               │   └── f2ade5075d3887096811dee42eba2fc278372544291fd0931322986bcf724e
│   │               ├── ea/
│   │               │   └── df3dfe34d237e72b57a6f65a765e995f6d280ae9df43d31475c6ddd56ab30c
│   │               ├── ec/
│   │               │   ├── d17e47e0304b97e3053158ee6fea211c3c949698a943728b651e0765236800
│   │               │   └── efc47866f04b4cb51f19249be0bf418b0dc28b8273d07495bfd8643be5fd74
│   │               ├── ed/
│   │               │   └── bc97ede5832fc84913b39dc6483c59021402f4de631cca082a5825bba5b22b
│   │               ├── ef/
│   │               │   └── 9b418fe6d5b61442f4b657aade1facd1a59dc9711b98ed15734e7f98c0f24b
│   │               ├── f0/
│   │               │   ├── a4c151db1732425700a0a0debff752719fc29b3301d807f4076c2a59050731
│   │               │   └── b89e14291a70d88d3e45722847e23bd3984c057ed0c3fac53befa4a56630d7
│   │               ├── f1/
│   │               │   ├── 4de0c2dfa4009076ed6ba8d42c9b22d122562a5d0f63fef83c1d37c980aa05
│   │               │   └── d424c78c7c9a6a795478d164142ed1374982b2fd5992284fb7e5b883321b9b
│   │               ├── f2/
│   │               │   └── 48a81c51e97671fae488a6b4296eece2c592cb3e97fcf690b7b7fb05c693bc
│   │               ├── f3/
│   │               │   ├── 0c1b0b2b49a84b9eb009e72831e908a624eb4a2294acc0b60a87e128c01ae3
│   │               │   ├── b168a44843930852194a72f9a154ef5aeb96f96c03c00923257e26d27dcfaa
│   │               │   └── fb33e621d3dca3b6434263fca47a9bed398a8333f18b65e5d1eb96378a87f5
│   │               ├── f5/
│   │               │   ├── 05f9e59bcbcbefe728741dbe56c5a63e0ecaccaab13bd0110de46777999698
│   │               │   ├── 4a0a4603bf0196ccba25bbd61af4fec2f076342936e6ec71d6678bb4e01404
│   │               │   ├── a233c0d68ebb396d40d965960388e3352d65058121cc7cf334d98e3c49d8a6
│   │               │   └── b80038560fcf9a261cbea1885a8159694af4cf323829648b4a28c4263f9fe1
│   │               ├── f6/
│   │               │   └── 5cd8a0bbb88a838309164c51364f7a4aade6eb52086ca1c3c73c4de227ad93
│   │               ├── f7/
│   │               │   ├── 2d7790d1106deb1f7ac1ff6c32129d4a1589255106d93b80646b4c8b2d6eae
│   │               │   └── 690fda0971875d1656dc43caaa16e293769389e581f248afb60fda797c4d30
│   │               ├── f8/
│   │               │   └── b28f2f369a116a0bc836715bb247545af571b053c7cf25c30a6a11842a0c09
│   │               ├── f9/
│   │               │   └── f58353edf6419ff056fdabc3eeb6ed2a4f8d1c981793c21d9763c637ea515d
│   │               ├── fa/
│   │               │   ├── 6b22431dbfa224b47e0a419b8b4c32b6fa68310debefb5a885f59fa28d492d
│   │               │   └── 7e3898b35bd6336f764b2de29f0c1ff11b73239574bd17c491fce466ecaf2d
│   │               ├── fb/
│   │               │   └── 0422c3c68f4f71369e98fa8c56ebdfd01a93d4a635cfc106e570b7e3fbe12f
│   │               ├── fc/
│   │               │   └── 7fd42ac2ea9db79760e7459de6ef1c2141001780d192ab516c5d1e23fe17ba
│   │               ├── fd/
│   │               │   ├── 16240c479439aeb448a11e06d8d6c63e95859523d2a5d7673926dc32eed4b9
│   │               │   ├── 45420ed5d0ee9bdc229ae5394a95d074082406b908e17afe4dd45effd68abe
│   │               │   ├── 527170967d14120cac36196685f0f75623c060496026a0c89cc63e987a6a63
│   │               │   ├── 97c85c0328dee2e695e52e6999b5e829104c01a8abbbccdea6575bcfc13f37
│   │               │   └── af8159150bc679d8337ef5a4200d901204d5d436413abf6c200b3cfe5debdd
│   │               └── ff/
│   │                   └── 53519b248ff454ddfcf3a89948c58f7e90e72582d058fa1e98be3e57259d59
│   ├── Gemfile
│   ├── Gemfile.lock
│   ├── _config.yml
│   ├── _data/
│   │   ├── field_checklists.yml
│   │   ├── glossary.yml
│   │   ├── navigation.yml
│   │   ├── rag_tree.json
│   │   ├── standards_graph.yml
│   │   └── training_catalog.yml
│   ├── _includes/
│   │   ├── context-panel.html
│   │   ├── rag-tree-nodes.html
│   │   ├── sidebar.html
│   │   ├── standards-graph.html
│   │   ├── topnav.html
│   │   └── trust-boundary.html
│   ├── _layouts/
│   │   ├── default.html
│   │   ├── field-checklist.html
│   │   ├── rag-browser.html
│   │   └── training-module.html
│   ├── _site/
│   │   ├── about/
│   │   │   └── index.html
│   │   ├── assets/
│   │   │   ├── css/
│   │   │   │   └── main.css
│   │   │   ├── data/
│   │   │   │   └── search.json
│   │   │   ├── img/
│   │   │   │   └── favicon.svg
│   │   │   ├── js/
│   │   │   │   ├── main.js
│   │   │   │   └── rag-browser.js
│   │   │   └── rag-files/
│   │   │       ├── commissioning_checklists/
│   │   │       │   └── checklists/
│   │   │       │       ├── basic_circuit_polarity_and_power_checks.md
│   │   │       │       ├── capacitor_discharge_awareness_check.md
│   │   │       │       ├── drive_commissioning.md
│   │   │       │       ├── motor_nameplate_and_overload_setting.md
│   │   │       │       ├── motor_rotation_and_overload_verification.md
│   │   │       │       └── pre_power_panel_and_incoming_supply_check.md
│   │   │       ├── design_framework/
│   │   │       │   ├── design_guides/
│   │   │       │   │   └── 02_power_distribution_guide.md
│   │   │       │   ├── electrical_review/
│   │   │       │   │   ├── basic_resistive_network_review.md
│   │   │       │   │   ├── component_selection_basics.md
│   │   │       │   │   ├── ohms_law_and_power_check_workflow.md
│   │   │       │   │   └── simple_signal_and_interface_circuit_notes.md
│   │   │       │   ├── motor_systems/
│   │   │       │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│   │   │       │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│   │   │       │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│   │   │       │   │   ├── integrated_motor_drive_architecture_comparison.md
│   │   │       │   │   ├── motor_cable_and_protection_review.md
│   │   │       │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│   │   │       │   │   ├── motor_nameplate_review_checklist.md
│   │   │       │   │   ├── motor_selection_comparison_matrix.md
│   │   │       │   │   ├── motor_selection_workflow.md
│   │   │       │   │   ├── motor_symptom_troubleshooting_patterns.md
│   │   │       │   │   ├── motor_troubleshooting_decision_tree.md
│   │   │       │   │   ├── servo_commissioning_workflow.md
│   │   │       │   │   ├── star_delta_and_supply_matching_notes.md
│   │   │       │   │   ├── vfd_commissioning_workflow.md
│   │   │       │   │   └── vfd_motor_integration_review.md
│   │   │       │   └── us_eu_compliance_wizard/
│   │   │       │       ├── US_EU_Machine_Compliance_Wizard.md
│   │   │       │       └── us_eu_delta_report_template.md
│   │   │       ├── meta/
│   │   │       │   ├── RAG_DIRECTORY_STATUS.md
│   │   │       │   └── VERSION_OVERVIEW.md
│   │   │       ├── standards_intelligence/
│   │   │       │   ├── crosswalks/
│   │   │       │   │   ├── overlap_matrix/
│   │   │       │   │   │   ├── file_structure.md
│   │   │       │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │       │   │   │   ├── standards_decision_workflow.md
│   │   │       │   │   │   ├── standards_overlap.md
│   │   │       │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │       │   │   └── overlap_notes/
│   │   │       │   │       ├── GENERATION_STATUS.md
│   │   │       │   │       ├── file_structure.md
│   │   │       │   │       ├── overlap__motors_drives.md
│   │   │       │   │       ├── overlap__sccr.md
│   │   │       │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│   │   │       │   ├── file_structure.md
│   │   │       │   ├── international/
│   │   │       │   │   ├── cybersecurity/
│   │   │       │   │   │   └── iec_62443/
│   │   │       │   │   │       ├── IEC62443_2_1__security_management.md
│   │   │       │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│   │   │       │   │   │       ├── IEC62443_4_2__component_requirements.md
│   │   │       │   │   │       └── IEC62443_lifecycle.md
│   │   │       │   │   ├── functional_safety/
│   │   │       │   │   │   ├── iec_61508/
│   │   │       │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│   │   │       │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│   │   │       │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│   │   │       │   │   │   │   └── IEC61508_2010__Part3__software.md
│   │   │       │   │   │   ├── iec_61511/
│   │   │       │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│   │   │       │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│   │   │       │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│   │   │       │   │   │   │   └── IEC61511_2016__Part1__framework.md
│   │   │       │   │   │   ├── iec_62061/
│   │   │       │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│   │   │       │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│   │   │       │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│   │   │       │   │   │   │   └── IEC62061_2021__Clause07__subsystem_design.md
│   │   │       │   │   │   ├── iso_12100/
│   │   │       │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│   │   │       │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│   │   │       │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│   │   │       │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│   │   │       │   │   │   │   └── ISO12100_2010__Clause07__risk_reduction.md
│   │   │       │   │   │   └── iso_13849_1/
│   │   │       │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│   │   │       │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│   │   │       │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│   │   │       │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│   │   │       │   │   │       ├── ISO13849_2023__Clause06__categories.md
│   │   │       │   │   │       └── ISO13849_2023__Clause07__validation.md
│   │   │       │   │   ├── hazardous_area/
│   │   │       │   │   │   └── iec_60079/
│   │   │       │   │   │       ├── IEC60079_0__general_requirements.md
│   │   │       │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│   │   │       │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│   │   │       │   │   │       ├── IEC60079_14__installation_design.md
│   │   │       │   │   │       ├── IEC60079_17__inspection_maintenance.md
│   │   │       │   │   │       └── IEC60079_1__flameproof_Ex_d.md
│   │   │       │   │   ├── machinery/
│   │   │       │   │   │   └── iec_60204_1/
│   │   │       │   │   │       ├── GENERATION_SUMMARY.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause01__scope.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause02__normative_references.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │   │       │   │   │       ├── IEC60204_1_2018__Clause15__verification.md
│   │   │       │   │   │       └── IEC60204_OVERVIEW.md
│   │   │       │   │   ├── offshore/
│   │   │       │   │   │   ├── ABS_offshore_electrical_control.md
│   │   │       │   │   │   └── DNV_OS_D201__electrical_installations.md
│   │   │       │   │   └── semiconductor/
│   │   │       │   │       └── semi/
│   │   │       │   │           ├── SEMI_S14__fire_risk_assessment.md
│   │   │       │   │           ├── SEMI_S2__equipment_safety.md
│   │   │       │   │           └── SEMI_S8__ergonomics.md
│   │   │       │   ├── library_admin/
│   │   │       │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │       │   │   ├── STANDARDS_COMPLETION_STATUS.md
│   │   │       │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │       │   │   └── STANDARDS_PURCHASE_TRACKER.md
│   │   │       │   ├── reference_models/
│   │   │       │   │   ├── 15-Standard Minimum Compliance Stack.md
│   │   │       │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│   │   │       │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│   │   │       │   │   ├── Universal Machine Safety Architecture.md
│   │   │       │   │   └── standards_atlas_diagrams_reference.md
│   │   │       │   ├── routing/
│   │   │       │   │   └── standards_applicability.md
│   │   │       │   ├── scenario/
│   │   │       │   │   ├── cnc_machine_safety_design/
│   │   │       │   │   │   ├── control_architecture_and_network.md
│   │   │       │   │   │   ├── hazards_and_risk_assessment.md
│   │   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │       │   │   │   ├── safety_functions_register.md
│   │   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │       │   │   │   ├── standards_applicability_matrix.md
│   │   │       │   │   │   ├── system_description.md
│   │   │       │   │   │   ├── ul_nec_design_requirements.md
│   │   │       │   │   │   └── verification_and_validation_plan.md
│   │   │       │   │   ├── mini_machine_safety_design/
│   │   │       │   │   │   ├── control_architecture_and_network.md
│   │   │       │   │   │   ├── hazards_and_risk_assessment.md
│   │   │       │   │   │   ├── industry_overlays/
│   │   │       │   │   │   │   ├── commercial.md
│   │   │       │   │   │   │   ├── energy.md
│   │   │       │   │   │   │   ├── food_and_beverage.md
│   │   │       │   │   │   │   ├── marine.md
│   │   │       │   │   │   │   ├── medical.md
│   │   │       │   │   │   │   ├── nuclear.md
│   │   │       │   │   │   │   ├── offshore.md
│   │   │       │   │   │   │   ├── petroleum.md
│   │   │       │   │   │   │   └── semiconductor.md
│   │   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │       │   │   │   ├── safety_functions_register.md
│   │   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │       │   │   │   ├── standards_applicability_matrix.md
│   │   │       │   │   │   ├── system_description.md
│   │   │       │   │   │   ├── ul_nec_design_requirements.md
│   │   │       │   │   │   └── verification_and_validation_plan.md
│   │   │       │   │   └── mini_machine_safety_design_v2/
│   │   │       │   │       ├── control_architecture_and_network.md
│   │   │       │   │       ├── hazards_and_risk_assessment.md
│   │   │       │   │       ├── industry_overlays/
│   │   │       │   │       │   ├── commercial.md
│   │   │       │   │       │   ├── energy.md
│   │   │       │   │       │   ├── food_and_beverage.md
│   │   │       │   │       │   ├── marine.md
│   │   │       │   │       │   ├── medical.md
│   │   │       │   │       │   ├── nuclear.md
│   │   │       │   │       │   ├── offshore.md
│   │   │       │   │       │   ├── petroleum.md
│   │   │       │   │       │   └── semiconductor.md
│   │   │       │   │       ├── mechanical_and_electrical_isolation.md
│   │   │       │   │       ├── safety_functions_register.md
│   │   │       │   │       ├── safety_integrity_and_sil_strategy.md
│   │   │       │   │       ├── standards_applicability_matrix.md
│   │   │       │   │       ├── system_description.md
│   │   │       │   │       ├── ul_nec_design_requirements.md
│   │   │       │   │       └── verification_and_validation_plan.md
│   │   │       │   └── us/
│   │   │       │       ├── nec/
│   │   │       │       │   ├── GENERATION_SUMMARY.md
│   │   │       │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│   │   │       │       │   ├── NEC_2023__Art100__definitions.md
│   │   │       │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │       │       │   ├── NEC_2023__Art215__feeders.md
│   │   │       │       │   ├── NEC_2023__Art230__services.md
│   │   │       │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │       │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│   │   │       │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │       │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │       │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │       │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │       │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │       │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │       │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│   │   │       │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│   │   │       │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│   │   │       │       │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │       │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│   │   │       │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │       │       │   ├── NEC_COMPLETION_STATUS.md
│   │   │       │       │   └── NEC_OVERVIEW.md
│   │   │       │       ├── nfpa79/
│   │   │       │       │   ├── GENERATION_SUMMARY.md
│   │   │       │       │   ├── NFPA79_2024__Ch01__administration.md
│   │   │       │       │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │       │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │       │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │       │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │       │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │       │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │       │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │       │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │       │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │       │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │       │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │       │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │       │       │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │       │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │       │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │       │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │       │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │       │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │       │       │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │       │       │   └── NFPA_OVERVIEW.md
│   │   │       │       └── ul_508a/
│   │   │       │           ├── GENERATION_SUMMARY.md
│   │   │       │           ├── UL508A_2022__control_circuits_and_devices.md
│   │   │       │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │       │           ├── UL508A_2022__general_construction_requirements.md
│   │   │       │           ├── UL508A_2022__grounding_and_bonding.md
│   │   │       │           ├── UL508A_2022__marking_and_documentation.md
│   │   │       │           ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │       │           ├── UL508A_2022__overcurrent_protection.md
│   │   │       │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │       │           ├── UL508A_2022__scope_and_application.md
│   │   │       │           ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │       │           ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │       │           ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │       │           └── UL508A_OVERVIEW.md
│   │   │       └── training_modules/
│   │   │           ├── control_systems/
│   │   │           │   ├── control_theory_overview.md
│   │   │           │   ├── industrial_control_loop_architectures.md
│   │   │           │   ├── industrial_pid_implementation.md
│   │   │           │   ├── pid_control_intuition.md
│   │   │           │   ├── pid_control_intuitive_foundation.md
│   │   │           │   ├── pid_drone_control.md
│   │   │           │   └── pid_heater_control_with_contactor.md
│   │   │           ├── electrical_machines/
│   │   │           │   ├── ac_vs_dc_motor_comparison.md
│   │   │           │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│   │   │           │   ├── dc_motor_basics.md
│   │   │           │   ├── induction_motor_basics.md
│   │   │           │   ├── motor_and_vfd_equations_reference.md
│   │   │           │   ├── motor_control_methods_and_operating_regions.md
│   │   │           │   ├── motor_efficiency_power_factor_and_losses.md
│   │   │           │   ├── motor_family_comparison.md
│   │   │           │   ├── motor_nameplates_slip_and_torque.md
│   │   │           │   ├── servo_drive_fundamentals.md
│   │   │           │   ├── servo_feedback_and_inertia_matching.md
│   │   │           │   ├── vfd_and_servo_architecture_diagrams.md
│   │   │           │   └── vfd_fundamentals.md
│   │   │           ├── fundamentals/
│   │   │           │   ├── conductor_ampacity_and_termination_temperature.md
│   │   │           │   ├── diodes_transistors_and_switching_basics.md
│   │   │           │   ├── earthing_systems_iec.md
│   │   │           │   ├── electrical_equations_reference.md
│   │   │           │   ├── electrical_quantities_and_circuit_language.md
│   │   │           │   ├── equivalent_circuit_methods.md
│   │   │           │   ├── kirchhoff_laws_and_systematic_analysis.md
│   │   │           │   ├── passive_components_resistors_capacitors.md
│   │   │           │   └── series_parallel_and_divider_methods.md
│   │   │           └── nec_application/
│   │   │               ├── article_409_practical_workflow.md
│   │   │               ├── article_430_practical_workflow.md
│   │   │               ├── branch_circuits_vs_feeders_motor_loads.md
│   │   │               ├── class1_class2_remote_control_circuits.md
│   │   │               ├── conductor_ocpd_sizing_examples.md
│   │   │               ├── disconnecting_means_for_machinery.md
│   │   │               ├── grounding_bonding_control_panels.md
│   │   │               ├── motor_and_panel_code_application.md
│   │   │               ├── nec_code_reading_fundamentals.md
│   │   │               ├── sccr_workflow.md
│   │   │               └── working_space_and_table_navigation.md
│   │   ├── commissioning-templates/
│   │   │   ├── basic-circuit-polarity/
│   │   │   │   └── index.html
│   │   │   ├── capacitor-discharge/
│   │   │   │   └── index.html
│   │   │   ├── drive-commissioning/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── motor-nameplate-overload/
│   │   │   │   └── index.html
│   │   │   ├── motor-rotation-verification/
│   │   │   │   └── index.html
│   │   │   └── pre-power-panel/
│   │   │       └── index.html
│   │   ├── crosswalks/
│   │   │   ├── compare/
│   │   │   │   └── index.html
│   │   │   ├── iec60079-nec-500-505/
│   │   │   │   └── index.html
│   │   │   ├── iec61511-iec61508/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── nfpa79-iec60204/
│   │   │   │   └── index.html
│   │   │   ├── standards-decision-workflow/
│   │   │   │   └── index.html
│   │   │   └── ul508a-nec-nfpa79/
│   │   │       └── index.html
│   │   ├── engineering-workflow/
│   │   │   └── index.html
│   │   ├── field-engineering/
│   │   │   └── index.html
│   │   ├── glossary/
│   │   │   └── index.html
│   │   ├── index.html
│   │   ├── industries/
│   │   │   ├── commercial/
│   │   │   │   └── index.html
│   │   │   ├── energy/
│   │   │   │   └── index.html
│   │   │   ├── food-and-beverage/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── marine/
│   │   │   │   └── index.html
│   │   │   ├── medical/
│   │   │   │   └── index.html
│   │   │   ├── nuclear/
│   │   │   │   └── index.html
│   │   │   ├── offshore/
│   │   │   │   └── index.html
│   │   │   ├── petroleum/
│   │   │   │   └── index.html
│   │   │   └── semiconductor/
│   │   │       ├── facility/
│   │   │       │   ├── bulk-chemical/
│   │   │       │   │   └── index.html
│   │   │       │   ├── bulk-specialty-gas/
│   │   │       │   │   └── index.html
│   │   │       │   ├── commissioning/
│   │   │       │   │   └── index.html
│   │   │       │   ├── control-philosophy/
│   │   │       │   │   └── index.html
│   │   │       │   ├── crosswalks/
│   │   │       │   │   └── index.html
│   │   │       │   ├── exhaust-abatement/
│   │   │       │   │   └── index.html
│   │   │       │   ├── hvac-cleanroom/
│   │   │       │   │   └── index.html
│   │   │       │   ├── index.html
│   │   │       │   ├── instrumentation/
│   │   │       │   │   ├── alarm-strategy/
│   │   │       │   │   │   └── index.html
│   │   │       │   │   ├── device-families/
│   │   │       │   │   │   └── index.html
│   │   │       │   │   ├── index.html
│   │   │       │   │   └── vendor-families/
│   │   │       │   │       └── index.html
│   │   │       │   ├── safety-shutdown/
│   │   │       │   │   └── index.html
│   │   │       │   ├── tool-facility-interface/
│   │   │       │   │   └── index.html
│   │   │       │   └── upw-wastewater/
│   │   │       │       └── index.html
│   │   │       └── index.html
│   │   ├── lifecycle/
│   │   │   ├── build/
│   │   │   │   └── index.html
│   │   │   ├── commissioning/
│   │   │   │   └── index.html
│   │   │   ├── concept/
│   │   │   │   └── index.html
│   │   │   ├── detailed-design/
│   │   │   │   └── index.html
│   │   │   ├── draft-documentation/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── installation/
│   │   │   │   └── index.html
│   │   │   ├── maintenance/
│   │   │   │   └── index.html
│   │   │   ├── management-of-change/
│   │   │   │   └── index.html
│   │   │   ├── pre-commissioning/
│   │   │   │   └── index.html
│   │   │   ├── risk-assessment/
│   │   │   │   └── index.html
│   │   │   ├── safety-architecture/
│   │   │   │   └── index.html
│   │   │   ├── safety-requirements-spec/
│   │   │   │   └── index.html
│   │   │   ├── safety-wiring/
│   │   │   │   └── index.html
│   │   │   └── standards-selection/
│   │   │       └── index.html
│   │   ├── plans/
│   │   │   ├── 2026-03-05-phase2-design.md
│   │   │   ├── 2026-03-05-phase2-implementation.md
│   │   │   ├── 2026-03-06-phase3-functional-safety-design.md
│   │   │   ├── 2026-03-06-phase3-implementation.md
│   │   │   ├── 2026-03-08-corpus-gap-fill-design.md
│   │   │   ├── 2026-03-08-decision-workflow-enhancements.md
│   │   │   ├── 2026-03-08-electrical-intelligence-integration-design.md
│   │   │   ├── 2026-03-08-electrical-intelligence-integration-plan.md
│   │   │   ├── 2026-03-08-glossary-design.md
│   │   │   ├── 2026-03-08-glossary-implementation.md
│   │   │   ├── 2026-03-08-nec-missing-articles.md
│   │   │   ├── 2026-03-08-nec-page-update.md
│   │   │   ├── 2026-03-08-phase10-corpus-gap-fill.md
│   │   │   ├── 2026-03-08-phase11-industry-overlay-depth-design.md
│   │   │   ├── 2026-03-08-phase11-industry-overlay-depth.md
│   │   │   ├── 2026-03-08-phase9-standards-graph.md
│   │   │   ├── 2026-03-08-standards-graph-design.md
│   │   │   ├── 2026-03-08-theme-switching-design.md
│   │   │   ├── 2026-03-08-theme-switching-implementation.md
│   │   │   ├── 2026-03-09-phase12-offshore-marine-overlay.md
│   │   │   ├── 2026-03-09-rag-browser-design.md
│   │   │   ├── 2026-03-09-training-site-pages-design.md
│   │   │   ├── 2026-03-09-training-site-pages-plan.md
│   │   │   ├── 2026-03-10-phase14-training-curriculum-design.md
│   │   │   ├── 2026-03-10-phase14-training-curriculum-implementation.md
│   │   │   ├── 2026-03-10-phase15-training-module-ux.md
│   │   │   ├── 2026-03-10-phase16-nec-training-expansion.md
│   │   │   ├── 2026-03-10-training-system-integration-preplan.md
│   │   │   ├── 2026-03-11-phase17-cross-layer-routing.md
│   │   │   ├── 2026-03-11-phase18-control-systems-training.md
│   │   │   └── 2026-03-13-phase19-engineering-workflow-navigation.md
│   │   ├── rag-browser/
│   │   │   └── index.html
│   │   ├── reference/
│   │   │   ├── architecture/
│   │   │   │   ├── compliance-stack/
│   │   │   │   │   └── index.html
│   │   │   │   ├── index.html
│   │   │   │   ├── machine-architecture-model/
│   │   │   │   │   └── index.html
│   │   │   │   └── machine-safety-architecture/
│   │   │   │       └── index.html
│   │   │   ├── index.html
│   │   │   └── motor-systems/
│   │   │       ├── index.html
│   │   │       └── motor-selection-matrix/
│   │   │           └── index.html
│   │   ├── scenarios/
│   │   │   ├── global-machine/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── machine-safety-implementation/
│   │   │   │   └── index.html
│   │   │   ├── networked-safety-plc/
│   │   │   │   └── index.html
│   │   │   ├── offshore-platform-control/
│   │   │   │   └── index.html
│   │   │   ├── oil-gas-process-skid/
│   │   │   │   └── index.html
│   │   │   ├── process-skid/
│   │   │   │   └── index.html
│   │   │   ├── semiconductor-equipment/
│   │   │   │   └── index.html
│   │   │   ├── semiconductor-fab-tool/
│   │   │   │   └── index.html
│   │   │   └── us-industrial-control-panel/
│   │   │       └── index.html
│   │   ├── software-stack/
│   │   │   └── index.html
│   │   ├── standards/
│   │   │   ├── cybersecurity/
│   │   │   │   ├── iec-62443/
│   │   │   │   │   └── index.html
│   │   │   │   └── index.html
│   │   │   ├── functional-safety/
│   │   │   │   ├── iec-61508/
│   │   │   │   │   └── index.html
│   │   │   │   ├── iec-61511/
│   │   │   │   │   └── index.html
│   │   │   │   ├── iec-62061/
│   │   │   │   │   └── index.html
│   │   │   │   ├── index.html
│   │   │   │   ├── iso-12100/
│   │   │   │   │   └── index.html
│   │   │   │   └── iso-13849-1/
│   │   │   │       └── index.html
│   │   │   ├── graph/
│   │   │   │   └── index.html
│   │   │   ├── hazardous-area/
│   │   │   │   ├── iec-60079/
│   │   │   │   │   └── index.html
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── machinery/
│   │   │   │   ├── iec-60204-1/
│   │   │   │   │   └── index.html
│   │   │   │   └── index.html
│   │   │   ├── semiconductor/
│   │   │   │   ├── index.html
│   │   │   │   └── semi/
│   │   │   │       └── index.html
│   │   │   └── us-electrical/
│   │   │       ├── index.html
│   │   │       ├── nec/
│   │   │       │   └── index.html
│   │   │       ├── nfpa-79/
│   │   │       │   └── index.html
│   │   │       └── ul-508a/
│   │   │           └── index.html
│   │   ├── superpowers/
│   │   │   ├── plans/
│   │   │   │   ├── 2026-03-12-fe-study-bugfixes.md
│   │   │   │   ├── 2026-03-13-doc-support.md
│   │   │   │   ├── 2026-03-13-field-engineering.md
│   │   │   │   ├── 2026-03-14-phase19-navigation-refactor.md
│   │   │   │   ├── 2026-03-15-phase20-software-safety-stack.md
│   │   │   │   ├── 2026-03-21-lifecycle-page-expansion.md
│   │   │   │   └── 2026-04-11-phase23-facility-build-phases-3-4.md
│   │   │   └── specs/
│   │   │       ├── 2026-03-12-doc-support-design.md
│   │   │       ├── 2026-03-13-field-engineering-design.md
│   │   │       ├── 2026-03-14-reference-section-commissioning-templates-design.md
│   │   │       ├── 2026-03-15-software-safety-stack-phase20-design.md
│   │   │       └── 2026-03-27-control-systems-training-expansion-design.html
│   │   ├── training/
│   │   │   ├── control-systems/
│   │   │   │   ├── async-faults-distributed-systems/
│   │   │   │   │   └── index.html
│   │   │   │   ├── control-loop-architectures/
│   │   │   │   │   └── index.html
│   │   │   │   ├── control-theory-overview/
│   │   │   │   │   └── index.html
│   │   │   │   ├── deterministic-nondeterministic-control/
│   │   │   │   │   └── index.html
│   │   │   │   ├── index.html
│   │   │   │   ├── industrial-pid/
│   │   │   │   │   └── index.html
│   │   │   │   ├── interlocks-permissives-safety-trips/
│   │   │   │   │   └── index.html
│   │   │   │   ├── machine-state-model/
│   │   │   │   │   └── index.html
│   │   │   │   ├── multi-axis-coordination/
│   │   │   │   │   └── index.html
│   │   │   │   ├── pid-drone-control/
│   │   │   │   │   └── index.html
│   │   │   │   ├── pid-foundation/
│   │   │   │   │   └── index.html
│   │   │   │   ├── pid-heater-control/
│   │   │   │   │   └── index.html
│   │   │   │   ├── pid-intuition/
│   │   │   │   │   └── index.html
│   │   │   │   ├── servo-tuning/
│   │   │   │   │   └── index.html
│   │   │   │   └── vibration-resonance/
│   │   │   │       └── index.html
│   │   │   ├── electrical-machines/
│   │   │   │   ├── ac-vs-dc-motors/
│   │   │   │   │   └── index.html
│   │   │   │   ├── bldc-ev-drone-motors/
│   │   │   │   │   └── index.html
│   │   │   │   ├── dc-motor-basics/
│   │   │   │   │   └── index.html
│   │   │   │   ├── index.html
│   │   │   │   ├── induction-motor-basics/
│   │   │   │   │   └── index.html
│   │   │   │   ├── motor-control-methods/
│   │   │   │   │   └── index.html
│   │   │   │   ├── motor-efficiency-losses/
│   │   │   │   │   └── index.html
│   │   │   │   ├── motor-family-comparison/
│   │   │   │   │   └── index.html
│   │   │   │   ├── motor-nameplates-slip-torque/
│   │   │   │   │   └── index.html
│   │   │   │   ├── motor-vfd-equations/
│   │   │   │   │   └── index.html
│   │   │   │   ├── servo-drive-fundamentals/
│   │   │   │   │   └── index.html
│   │   │   │   ├── servo-feedback-inertia/
│   │   │   │   │   └── index.html
│   │   │   │   ├── vfd-fundamentals/
│   │   │   │   │   └── index.html
│   │   │   │   └── vfd-servo-architecture/
│   │   │   │       └── index.html
│   │   │   ├── fundamentals/
│   │   │   │   ├── conductor-ampacity/
│   │   │   │   │   └── index.html
│   │   │   │   ├── diodes-transistors/
│   │   │   │   │   └── index.html
│   │   │   │   ├── earthing-systems-iec/
│   │   │   │   │   └── index.html
│   │   │   │   ├── electrical-equations-reference/
│   │   │   │   │   └── index.html
│   │   │   │   ├── electrical-quantities/
│   │   │   │   │   └── index.html
│   │   │   │   ├── equivalent-circuit-methods/
│   │   │   │   │   └── index.html
│   │   │   │   ├── index.html
│   │   │   │   ├── kirchhoff-laws/
│   │   │   │   │   └── index.html
│   │   │   │   ├── passive-components/
│   │   │   │   │   └── index.html
│   │   │   │   └── series-parallel-dividers/
│   │   │   │       └── index.html
│   │   │   ├── index.html
│   │   │   └── nec-application/
│   │   │       ├── article-409-workflow/
│   │   │       │   └── index.html
│   │   │       ├── article-430-workflow/
│   │   │       │   └── index.html
│   │   │       ├── branch-circuits-vs-feeders/
│   │   │       │   └── index.html
│   │   │       ├── class1-class2-circuits/
│   │   │       │   └── index.html
│   │   │       ├── conductor-ocpd-sizing/
│   │   │       │   └── index.html
│   │   │       ├── disconnecting-means/
│   │   │       │   └── index.html
│   │   │       ├── grounding-bonding-panels/
│   │   │       │   └── index.html
│   │   │       ├── index.html
│   │   │       ├── motor-panel-code-application/
│   │   │       │   └── index.html
│   │   │       ├── nec-code-reading/
│   │   │       │   └── index.html
│   │   │       ├── sccr-workflow/
│   │   │       │   └── index.html
│   │   │       └── working-space-table-navigation/
│   │   │           └── index.html
│   │   └── workflows/
│   │       ├── electrical-review/
│   │       │   └── index.html
│   │       ├── index.html
│   │       ├── motor-selection/
│   │       │   └── index.html
│   │       ├── motor-troubleshooting/
│   │       │   └── index.html
│   │       ├── servo-commissioning/
│   │       │   └── index.html
│   │       └── vfd-commissioning/
│   │           └── index.html
│   ├── about/
│   │   └── index.md
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── data/
│   │   │   └── search.json
│   │   ├── img/
│   │   │   └── favicon.svg
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   └── rag-browser.js
│   │   └── rag-files/
│   │       ├── commissioning_checklists/
│   │       │   └── checklists/
│   │       │       ├── basic_circuit_polarity_and_power_checks.md
│   │       │       ├── capacitor_discharge_awareness_check.md
│   │       │       ├── drive_commissioning.md
│   │       │       ├── motor_nameplate_and_overload_setting.md
│   │       │       ├── motor_rotation_and_overload_verification.md
│   │       │       └── pre_power_panel_and_incoming_supply_check.md
│   │       ├── design_framework/
│   │       │   ├── design_guides/
│   │       │   │   └── 02_power_distribution_guide.md
│   │       │   ├── electrical_review/
│   │       │   │   ├── basic_resistive_network_review.md
│   │       │   │   ├── component_selection_basics.md
│   │       │   │   ├── ohms_law_and_power_check_workflow.md
│   │       │   │   └── simple_signal_and_interface_circuit_notes.md
│   │       │   ├── motor_systems/
│   │       │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│   │       │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│   │       │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│   │       │   │   ├── integrated_motor_drive_architecture_comparison.md
│   │       │   │   ├── motor_cable_and_protection_review.md
│   │       │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│   │       │   │   ├── motor_nameplate_review_checklist.md
│   │       │   │   ├── motor_selection_comparison_matrix.md
│   │       │   │   ├── motor_selection_workflow.md
│   │       │   │   ├── motor_symptom_troubleshooting_patterns.md
│   │       │   │   ├── motor_troubleshooting_decision_tree.md
│   │       │   │   ├── servo_commissioning_workflow.md
│   │       │   │   ├── star_delta_and_supply_matching_notes.md
│   │       │   │   ├── vfd_commissioning_workflow.md
│   │       │   │   └── vfd_motor_integration_review.md
│   │       │   └── us_eu_compliance_wizard/
│   │       │       ├── US_EU_Machine_Compliance_Wizard.md
│   │       │       └── us_eu_delta_report_template.md
│   │       ├── meta/
│   │       │   ├── RAG_DIRECTORY_STATUS.md
│   │       │   └── VERSION_OVERVIEW.md
│   │       ├── standards_intelligence/
│   │       │   ├── _glossary.md
│   │       │   ├── _standards_map.md
│   │       │   ├── crosswalks/
│   │       │   │   ├── overlap_matrix/
│   │       │   │   │   ├── file_structure.md
│   │       │   │   │   ├── nfpa79_iec60204_overlap.md
│   │       │   │   │   ├── standards_decision_workflow.md
│   │       │   │   │   ├── standards_overlap.md
│   │       │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │       │   │   └── overlap_notes/
│   │       │   │       ├── GENERATION_STATUS.md
│   │       │   │       ├── file_structure.md
│   │       │   │       ├── overlap__motors_drives.md
│   │       │   │       ├── overlap__sccr.md
│   │       │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│   │       │   ├── file_structure.md
│   │       │   ├── international/
│   │       │   │   ├── cybersecurity/
│   │       │   │   │   └── iec_62443/
│   │       │   │   │       ├── IEC62443_2_1__security_management.md
│   │       │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│   │       │   │   │       ├── IEC62443_4_2__component_requirements.md
│   │       │   │   │       └── IEC62443_lifecycle.md
│   │       │   │   ├── functional_safety/
│   │       │   │   │   ├── iec_61508/
│   │       │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│   │       │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│   │       │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│   │       │   │   │   │   └── IEC61508_2010__Part3__software.md
│   │       │   │   │   ├── iec_61511/
│   │       │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│   │       │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│   │       │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│   │       │   │   │   │   └── IEC61511_2016__Part1__framework.md
│   │       │   │   │   ├── iec_62061/
│   │       │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│   │       │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│   │       │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│   │       │   │   │   │   └── IEC62061_2021__Clause07__subsystem_design.md
│   │       │   │   │   ├── iso_12100/
│   │       │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│   │       │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│   │       │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│   │       │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│   │       │   │   │   │   └── ISO12100_2010__Clause07__risk_reduction.md
│   │       │   │   │   └── iso_13849_1/
│   │       │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│   │       │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│   │       │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│   │       │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│   │       │   │   │       ├── ISO13849_2023__Clause06__categories.md
│   │       │   │   │       └── ISO13849_2023__Clause07__validation.md
│   │       │   │   ├── hazardous_area/
│   │       │   │   │   └── iec_60079/
│   │       │   │   │       ├── IEC60079_0__general_requirements.md
│   │       │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│   │       │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│   │       │   │   │       ├── IEC60079_14__installation_design.md
│   │       │   │   │       ├── IEC60079_17__inspection_maintenance.md
│   │       │   │   │       └── IEC60079_1__flameproof_Ex_d.md
│   │       │   │   ├── machinery/
│   │       │   │   │   └── iec_60204_1/
│   │       │   │   │       ├── GENERATION_SUMMARY.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause01__scope.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause02__normative_references.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │       │   │   │       ├── IEC60204_1_2018__Clause15__verification.md
│   │       │   │   │       └── IEC60204_OVERVIEW.md
│   │       │   │   ├── offshore/
│   │       │   │   │   ├── ABS_offshore_electrical_control.md
│   │       │   │   │   └── DNV_OS_D201__electrical_installations.md
│   │       │   │   └── semiconductor/
│   │       │   │       └── semi/
│   │       │   │           ├── SEMI_S14__fire_risk_assessment.md
│   │       │   │           ├── SEMI_S2__equipment_safety.md
│   │       │   │           └── SEMI_S8__ergonomics.md
│   │       │   ├── library_admin/
│   │       │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │       │   │   ├── STANDARDS_COMPLETION_STATUS.md
│   │       │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │       │   │   └── STANDARDS_PURCHASE_TRACKER.md
│   │       │   ├── reference_models/
│   │       │   │   ├── 15-Standard Minimum Compliance Stack.md
│   │       │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│   │       │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│   │       │   │   ├── Universal Machine Safety Architecture.md
│   │       │   │   └── standards_atlas_diagrams_reference.md
│   │       │   ├── routing/
│   │       │   │   └── standards_applicability.md
│   │       │   ├── scenario/
│   │       │   │   ├── cnc_machine_safety_design/
│   │       │   │   │   ├── control_architecture_and_network.md
│   │       │   │   │   ├── hazards_and_risk_assessment.md
│   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│   │       │   │   │   ├── safety_functions_register.md
│   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │       │   │   │   ├── standards_applicability_matrix.md
│   │       │   │   │   ├── system_description.md
│   │       │   │   │   ├── ul_nec_design_requirements.md
│   │       │   │   │   └── verification_and_validation_plan.md
│   │       │   │   ├── mini_machine_safety_design/
│   │       │   │   │   ├── control_architecture_and_network.md
│   │       │   │   │   ├── hazards_and_risk_assessment.md
│   │       │   │   │   ├── industry_overlays/
│   │       │   │   │   │   ├── commercial.md
│   │       │   │   │   │   ├── energy.md
│   │       │   │   │   │   ├── food_and_beverage.md
│   │       │   │   │   │   ├── marine.md
│   │       │   │   │   │   ├── medical.md
│   │       │   │   │   │   ├── nuclear.md
│   │       │   │   │   │   ├── offshore.md
│   │       │   │   │   │   ├── petroleum.md
│   │       │   │   │   │   └── semiconductor.md
│   │       │   │   │   ├── mechanical_and_electrical_isolation.md
│   │       │   │   │   ├── safety_functions_register.md
│   │       │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │       │   │   │   ├── standards_applicability_matrix.md
│   │       │   │   │   ├── system_description.md
│   │       │   │   │   ├── ul_nec_design_requirements.md
│   │       │   │   │   └── verification_and_validation_plan.md
│   │       │   │   └── mini_machine_safety_design_v2/
│   │       │   │       ├── control_architecture_and_network.md
│   │       │   │       ├── hazards_and_risk_assessment.md
│   │       │   │       ├── industry_overlays/
│   │       │   │       │   ├── commercial.md
│   │       │   │       │   ├── energy.md
│   │       │   │       │   ├── food_and_beverage.md
│   │       │   │       │   ├── marine.md
│   │       │   │       │   ├── medical.md
│   │       │   │       │   ├── nuclear.md
│   │       │   │       │   ├── offshore.md
│   │       │   │       │   ├── petroleum.md
│   │       │   │       │   └── semiconductor.md
│   │       │   │       ├── mechanical_and_electrical_isolation.md
│   │       │   │       ├── safety_functions_register.md
│   │       │   │       ├── safety_integrity_and_sil_strategy.md
│   │       │   │       ├── standards_applicability_matrix.md
│   │       │   │       ├── system_description.md
│   │       │   │       ├── ul_nec_design_requirements.md
│   │       │   │       └── verification_and_validation_plan.md
│   │       │   └── us/
│   │       │       ├── nec/
│   │       │       │   ├── GENERATION_SUMMARY.md
│   │       │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│   │       │       │   ├── NEC_2023__Art100__definitions.md
│   │       │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │       │       │   ├── NEC_2023__Art215__feeders.md
│   │       │       │   ├── NEC_2023__Art230__services.md
│   │       │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │       │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│   │       │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │       │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │       │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │       │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │       │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │       │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │       │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│   │       │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│   │       │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│   │       │       │   ├── NEC_2023__Art670__industrial_machinery.md
│   │       │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│   │       │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │       │       │   ├── NEC_COMPLETION_STATUS.md
│   │       │       │   └── NEC_OVERVIEW.md
│   │       │       ├── nfpa79/
│   │       │       │   ├── GENERATION_SUMMARY.md
│   │       │       │   ├── NFPA79_2024__Ch01__administration.md
│   │       │       │   ├── NFPA79_2024__Ch02__definitions.md
│   │       │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │       │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │       │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │       │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │       │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │       │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │       │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │       │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │       │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │       │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │       │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │       │       │   ├── NFPA79_2024__Ch14__lighting.md
│   │       │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │       │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │       │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │       │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │       │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │       │       │   ├── NFPA79_2024__Ch20__system_integration.md
│   │       │       │   └── NFPA_OVERVIEW.md
│   │       │       └── ul_508a/
│   │       │           ├── GENERATION_SUMMARY.md
│   │       │           ├── UL508A_2022__control_circuits_and_devices.md
│   │       │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │       │           ├── UL508A_2022__general_construction_requirements.md
│   │       │           ├── UL508A_2022__grounding_and_bonding.md
│   │       │           ├── UL508A_2022__marking_and_documentation.md
│   │       │           ├── UL508A_2022__motor_controllers_and_drives.md
│   │       │           ├── UL508A_2022__overcurrent_protection.md
│   │       │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │       │           ├── UL508A_2022__scope_and_application.md
│   │       │           ├── UL508A_2022__spacing_creepage_clearance.md
│   │       │           ├── UL508A_2022__transformers_and_power_supplies.md
│   │       │           ├── UL508A_2022__wiring_methods_and_conductors.md
│   │       │           └── UL508A_OVERVIEW.md
│   │       └── training_modules/
│   │           ├── control_systems/
│   │           │   ├── control_theory_overview.md
│   │           │   ├── industrial_control_loop_architectures.md
│   │           │   ├── industrial_pid_implementation.md
│   │           │   ├── pid_control_intuition.md
│   │           │   ├── pid_control_intuitive_foundation.md
│   │           │   ├── pid_drone_control.md
│   │           │   └── pid_heater_control_with_contactor.md
│   │           ├── electrical_machines/
│   │           │   ├── ac_vs_dc_motor_comparison.md
│   │           │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│   │           │   ├── dc_motor_basics.md
│   │           │   ├── induction_motor_basics.md
│   │           │   ├── motor_and_vfd_equations_reference.md
│   │           │   ├── motor_control_methods_and_operating_regions.md
│   │           │   ├── motor_efficiency_power_factor_and_losses.md
│   │           │   ├── motor_family_comparison.md
│   │           │   ├── motor_nameplates_slip_and_torque.md
│   │           │   ├── servo_drive_fundamentals.md
│   │           │   ├── servo_feedback_and_inertia_matching.md
│   │           │   ├── vfd_and_servo_architecture_diagrams.md
│   │           │   └── vfd_fundamentals.md
│   │           ├── fundamentals/
│   │           │   ├── conductor_ampacity_and_termination_temperature.md
│   │           │   ├── diodes_transistors_and_switching_basics.md
│   │           │   ├── earthing_systems_iec.md
│   │           │   ├── electrical_equations_reference.md
│   │           │   ├── electrical_quantities_and_circuit_language.md
│   │           │   ├── equivalent_circuit_methods.md
│   │           │   ├── kirchhoff_laws_and_systematic_analysis.md
│   │           │   ├── passive_components_resistors_capacitors.md
│   │           │   └── series_parallel_and_divider_methods.md
│   │           └── nec_application/
│   │               ├── article_409_practical_workflow.md
│   │               ├── article_430_practical_workflow.md
│   │               ├── branch_circuits_vs_feeders_motor_loads.md
│   │               ├── class1_class2_remote_control_circuits.md
│   │               ├── conductor_ocpd_sizing_examples.md
│   │               ├── disconnecting_means_for_machinery.md
│   │               ├── grounding_bonding_control_panels.md
│   │               ├── motor_and_panel_code_application.md
│   │               ├── nec_code_reading_fundamentals.md
│   │               ├── sccr_workflow.md
│   │               └── working_space_and_table_navigation.md
│   ├── commissioning-templates/
│   │   ├── basic-circuit-polarity/
│   │   │   └── index.md
│   │   ├── capacitor-discharge/
│   │   │   └── index.md
│   │   ├── drive-commissioning/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── motor-nameplate-overload/
│   │   │   └── index.md
│   │   ├── motor-rotation-verification/
│   │   │   └── index.md
│   │   └── pre-power-panel/
│   │       └── index.md
│   ├── crosswalks/
│   │   ├── compare/
│   │   │   └── index.md
│   │   ├── iec60079-nec-500-505/
│   │   │   └── index.md
│   │   ├── iec61511-iec61508/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── nfpa79-iec60204/
│   │   │   └── index.md
│   │   ├── standards-decision-workflow/
│   │   │   └── index.md
│   │   └── ul508a-nec-nfpa79/
│   │       └── index.md
│   ├── engineering-workflow/
│   │   └── index.md
│   ├── field-engineering/
│   │   └── index.md
│   ├── glossary/
│   │   └── index.md
│   ├── index.md
│   ├── industries/
│   │   ├── commercial/
│   │   │   └── index.md
│   │   ├── energy/
│   │   │   └── index.md
│   │   ├── food-and-beverage/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── marine/
│   │   │   └── index.md
│   │   ├── medical/
│   │   │   └── index.md
│   │   ├── nuclear/
│   │   │   └── index.md
│   │   ├── offshore/
│   │   │   └── index.md
│   │   ├── petroleum/
│   │   │   └── index.md
│   │   └── semiconductor/
│   │       ├── facility/
│   │       │   ├── bulk-chemical/
│   │       │   │   └── index.md
│   │       │   ├── bulk-specialty-gas/
│   │       │   │   └── index.md
│   │       │   ├── commissioning/
│   │       │   │   └── index.md
│   │       │   ├── control-philosophy/
│   │       │   │   └── index.md
│   │       │   ├── crosswalks/
│   │       │   │   └── index.md
│   │       │   ├── exhaust-abatement/
│   │       │   │   └── index.md
│   │       │   ├── hvac-cleanroom/
│   │       │   │   └── index.md
│   │       │   ├── index.md
│   │       │   ├── instrumentation/
│   │       │   │   ├── alarm-strategy/
│   │       │   │   │   └── index.md
│   │       │   │   ├── device-families/
│   │       │   │   │   └── index.md
│   │       │   │   ├── index.md
│   │       │   │   └── vendor-families/
│   │       │   │       └── index.md
│   │       │   ├── safety-shutdown/
│   │       │   │   └── index.md
│   │       │   ├── tool-facility-interface/
│   │       │   │   └── index.md
│   │       │   └── upw-wastewater/
│   │       │       └── index.md
│   │       └── index.md
│   ├── lifecycle/
│   │   ├── build/
│   │   │   └── index.md
│   │   ├── commissioning/
│   │   │   └── index.md
│   │   ├── concept/
│   │   │   └── index.md
│   │   ├── detailed-design/
│   │   │   └── index.md
│   │   ├── draft-documentation/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── installation/
│   │   │   └── index.md
│   │   ├── maintenance/
│   │   │   └── index.md
│   │   ├── management-of-change/
│   │   │   └── index.md
│   │   ├── pre-commissioning/
│   │   │   └── index.md
│   │   ├── risk-assessment/
│   │   │   └── index.md
│   │   ├── safety-architecture/
│   │   │   └── index.md
│   │   ├── safety-requirements-spec/
│   │   │   └── index.md
│   │   ├── safety-wiring/
│   │   │   └── index.md
│   │   └── standards-selection/
│   │       └── index.md
│   ├── plans/
│   │   ├── 2026-03-05-phase2-design.md
│   │   ├── 2026-03-05-phase2-implementation.md
│   │   ├── 2026-03-06-phase3-functional-safety-design.md
│   │   ├── 2026-03-06-phase3-implementation.md
│   │   ├── 2026-03-08-corpus-gap-fill-design.md
│   │   ├── 2026-03-08-decision-workflow-enhancements.md
│   │   ├── 2026-03-08-electrical-intelligence-integration-design.md
│   │   ├── 2026-03-08-electrical-intelligence-integration-plan.md
│   │   ├── 2026-03-08-glossary-design.md
│   │   ├── 2026-03-08-glossary-implementation.md
│   │   ├── 2026-03-08-nec-missing-articles.md
│   │   ├── 2026-03-08-nec-page-update.md
│   │   ├── 2026-03-08-phase10-corpus-gap-fill.md
│   │   ├── 2026-03-08-phase11-industry-overlay-depth-design.md
│   │   ├── 2026-03-08-phase11-industry-overlay-depth.md
│   │   ├── 2026-03-08-phase9-standards-graph.md
│   │   ├── 2026-03-08-standards-graph-design.md
│   │   ├── 2026-03-08-theme-switching-design.md
│   │   ├── 2026-03-08-theme-switching-implementation.md
│   │   ├── 2026-03-09-phase12-offshore-marine-overlay.md
│   │   ├── 2026-03-09-rag-browser-design.md
│   │   ├── 2026-03-09-training-site-pages-design.md
│   │   ├── 2026-03-09-training-site-pages-plan.md
│   │   ├── 2026-03-10-phase14-training-curriculum-design.md
│   │   ├── 2026-03-10-phase14-training-curriculum-implementation.md
│   │   ├── 2026-03-10-phase15-training-module-ux.md
│   │   ├── 2026-03-10-phase16-nec-training-expansion.md
│   │   ├── 2026-03-10-training-system-integration-preplan.md
│   │   ├── 2026-03-11-phase17-cross-layer-routing.md
│   │   ├── 2026-03-11-phase18-control-systems-training.md
│   │   └── 2026-03-13-phase19-engineering-workflow-navigation.md
│   ├── rag-browser/
│   │   └── index.md
│   ├── reference/
│   │   ├── architecture/
│   │   │   ├── compliance-stack/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── machine-architecture-model/
│   │   │   │   └── index.md
│   │   │   └── machine-safety-architecture/
│   │   │       └── index.md
│   │   ├── index.md
│   │   └── motor-systems/
│   │       ├── index.md
│   │       └── motor-selection-matrix/
│   │           └── index.md
│   ├── scenarios/
│   │   ├── global-machine/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── machine-safety-implementation/
│   │   │   └── index.md
│   │   ├── networked-safety-plc/
│   │   │   └── index.md
│   │   ├── offshore-platform-control/
│   │   │   └── index.md
│   │   ├── oil-gas-process-skid/
│   │   │   └── index.md
│   │   ├── process-skid/
│   │   │   └── index.md
│   │   ├── semiconductor-equipment/
│   │   │   └── index.md
│   │   ├── semiconductor-fab-tool/
│   │   │   └── index.md
│   │   └── us-industrial-control-panel/
│   │       └── index.md
│   ├── software-stack/
│   │   └── index.md
│   ├── standards/
│   │   ├── cybersecurity/
│   │   │   ├── iec-62443/
│   │   │   │   └── index.md
│   │   │   └── index.md
│   │   ├── functional-safety/
│   │   │   ├── iec-61508/
│   │   │   │   └── index.md
│   │   │   ├── iec-61511/
│   │   │   │   └── index.md
│   │   │   ├── iec-62061/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── iso-12100/
│   │   │   │   └── index.md
│   │   │   └── iso-13849-1/
│   │   │       └── index.md
│   │   ├── graph/
│   │   │   └── index.md
│   │   ├── hazardous-area/
│   │   │   ├── iec-60079/
│   │   │   │   └── index.md
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── machinery/
│   │   │   ├── iec-60204-1/
│   │   │   │   └── index.md
│   │   │   └── index.md
│   │   ├── semiconductor/
│   │   │   ├── index.md
│   │   │   └── semi/
│   │   │       └── index.md
│   │   └── us-electrical/
│   │       ├── index.md
│   │       ├── nec/
│   │       │   └── index.md
│   │       ├── nfpa-79/
│   │       │   └── index.md
│   │       └── ul-508a/
│   │           └── index.md
│   ├── superpowers/
│   │   ├── plans/
│   │   │   ├── 2026-03-12-fe-study-bugfixes.md
│   │   │   ├── 2026-03-13-doc-support.md
│   │   │   ├── 2026-03-13-field-engineering.md
│   │   │   ├── 2026-03-14-phase19-navigation-refactor.md
│   │   │   ├── 2026-03-15-phase20-software-safety-stack.md
│   │   │   ├── 2026-03-21-lifecycle-page-expansion.md
│   │   │   └── 2026-04-11-phase23-facility-build-phases-3-4.md
│   │   └── specs/
│   │       ├── 2026-03-12-doc-support-design.md
│   │       ├── 2026-03-13-field-engineering-design.md
│   │       ├── 2026-03-14-reference-section-commissioning-templates-design.md
│   │       ├── 2026-03-15-software-safety-stack-phase20-design.md
│   │       └── 2026-03-27-control-systems-training-expansion-design.md
│   ├── training/
│   │   ├── control-systems/
│   │   │   ├── async-faults-distributed-systems/
│   │   │   │   └── index.md
│   │   │   ├── control-loop-architectures/
│   │   │   │   └── index.md
│   │   │   ├── control-theory-overview/
│   │   │   │   └── index.md
│   │   │   ├── deterministic-nondeterministic-control/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── industrial-pid/
│   │   │   │   └── index.md
│   │   │   ├── interlocks-permissives-safety-trips/
│   │   │   │   └── index.md
│   │   │   ├── machine-state-model/
│   │   │   │   └── index.md
│   │   │   ├── multi-axis-coordination/
│   │   │   │   └── index.md
│   │   │   ├── pid-drone-control/
│   │   │   │   └── index.md
│   │   │   ├── pid-foundation/
│   │   │   │   └── index.md
│   │   │   ├── pid-heater-control/
│   │   │   │   └── index.md
│   │   │   ├── pid-intuition/
│   │   │   │   └── index.md
│   │   │   ├── servo-tuning/
│   │   │   │   └── index.md
│   │   │   └── vibration-resonance/
│   │   │       └── index.md
│   │   ├── electrical-machines/
│   │   │   ├── ac-vs-dc-motors/
│   │   │   │   └── index.md
│   │   │   ├── bldc-ev-drone-motors/
│   │   │   │   └── index.md
│   │   │   ├── dc-motor-basics/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── induction-motor-basics/
│   │   │   │   └── index.md
│   │   │   ├── motor-control-methods/
│   │   │   │   └── index.md
│   │   │   ├── motor-efficiency-losses/
│   │   │   │   └── index.md
│   │   │   ├── motor-family-comparison/
│   │   │   │   └── index.md
│   │   │   ├── motor-nameplates-slip-torque/
│   │   │   │   └── index.md
│   │   │   ├── motor-vfd-equations/
│   │   │   │   └── index.md
│   │   │   ├── servo-drive-fundamentals/
│   │   │   │   └── index.md
│   │   │   ├── servo-feedback-inertia/
│   │   │   │   └── index.md
│   │   │   ├── vfd-fundamentals/
│   │   │   │   └── index.md
│   │   │   └── vfd-servo-architecture/
│   │   │       └── index.md
│   │   ├── fundamentals/
│   │   │   ├── conductor-ampacity/
│   │   │   │   └── index.md
│   │   │   ├── diodes-transistors/
│   │   │   │   └── index.md
│   │   │   ├── earthing-systems-iec/
│   │   │   │   └── index.md
│   │   │   ├── electrical-equations-reference/
│   │   │   │   └── index.md
│   │   │   ├── electrical-quantities/
│   │   │   │   └── index.md
│   │   │   ├── equivalent-circuit-methods/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── kirchhoff-laws/
│   │   │   │   └── index.md
│   │   │   ├── passive-components/
│   │   │   │   └── index.md
│   │   │   └── series-parallel-dividers/
│   │   │       └── index.md
│   │   ├── index.md
│   │   └── nec-application/
│   │       ├── article-409-workflow/
│   │       │   └── index.md
│   │       ├── article-430-workflow/
│   │       │   └── index.md
│   │       ├── branch-circuits-vs-feeders/
│   │       │   └── index.md
│   │       ├── class1-class2-circuits/
│   │       │   └── index.md
│   │       ├── conductor-ocpd-sizing/
│   │       │   └── index.md
│   │       ├── disconnecting-means/
│   │       │   └── index.md
│   │       ├── grounding-bonding-panels/
│   │       │   └── index.md
│   │       ├── index.md
│   │       ├── motor-panel-code-application/
│   │       │   └── index.md
│   │       ├── nec-code-reading/
│   │       │   └── index.md
│   │       ├── sccr-workflow/
│   │       │   └── index.md
│   │       └── working-space-table-navigation/
│   │           └── index.md
│   ├── vendor/
│   │   └── bundle/
│   │       └── ruby/
│   │           └── 2.6.0/
│   │               ├── bin/
│   │               │   ├── jekyll
│   │               │   ├── kramdown
│   │               │   ├── listen
│   │               │   ├── rake
│   │               │   ├── rougify
│   │               │   └── safe_yaml
│   │               ├── build_info/
│   │               ├── cache/
│   │               │   ├── addressable-2.8.9.gem
│   │               │   ├── colorator-1.1.0.gem
│   │               │   ├── concurrent-ruby-1.3.6.gem
│   │               │   ├── em-websocket-0.5.3.gem
│   │               │   ├── eventmachine-1.2.7.gem
│   │               │   ├── ffi-1.17.3.gem
│   │               │   ├── forwardable-extended-2.6.0.gem
│   │               │   ├── google-protobuf-3.23.4-arm64-darwin.gem
│   │               │   ├── http_parser.rb-0.8.1.gem
│   │               │   ├── i18n-1.14.8.gem
│   │               │   ├── jekyll-4.3.4.gem
│   │               │   ├── jekyll-sass-converter-3.0.0.gem
│   │               │   ├── jekyll-seo-tag-2.8.0.gem
│   │               │   ├── jekyll-watch-2.2.1.gem
│   │               │   ├── kramdown-2.5.2.gem
│   │               │   ├── kramdown-parser-gfm-1.1.0.gem
│   │               │   ├── liquid-4.0.4.gem
│   │               │   ├── listen-3.10.0.gem
│   │               │   ├── logger-1.7.0.gem
│   │               │   ├── mercenary-0.4.0.gem
│   │               │   ├── pathutil-0.16.2.gem
│   │               │   ├── public_suffix-5.1.1.gem
│   │               │   ├── rake-13.3.1.gem
│   │               │   ├── rb-fsevent-0.11.2.gem
│   │               │   ├── rb-inotify-0.11.1.gem
│   │               │   ├── rexml-3.4.4.gem
│   │               │   ├── rouge-3.30.0.gem
│   │               │   ├── safe_yaml-1.0.5.gem
│   │               │   ├── sass-embedded-1.58.3-arm64-darwin.gem
│   │               │   ├── sass-embedded-1.58.3.gem
│   │               │   ├── terminal-table-3.0.2.gem
│   │               │   ├── unicode-display_width-2.6.0.gem
│   │               │   └── webrick-1.9.2.gem
│   │               ├── doc/
│   │               ├── extensions/
│   │               │   └── universal-darwin-25/
│   │               │       └── 2.6.0/
│   │               │           ├── eventmachine-1.2.7/
│   │               │           │   ├── fastfilereaderext.bundle
│   │               │           │   ├── gem.build_complete
│   │               │           │   ├── gem_make.out
│   │               │           │   ├── mkmf.log
│   │               │           │   └── rubyeventmachine.bundle
│   │               │           ├── ffi-1.17.3/
│   │               │           │   ├── ffi_c.bundle
│   │               │           │   ├── gem.build_complete
│   │               │           │   ├── gem_make.out
│   │               │           │   └── mkmf.log
│   │               │           ├── http_parser.rb-0.8.1/
│   │               │           │   ├── gem.build_complete
│   │               │           │   ├── gem_make.out
│   │               │           │   └── ruby_http_parser.bundle
│   │               │           └── sass-embedded-1.58.3/
│   │               │               ├── gem.build_complete
│   │               │               └── gem_make.out
│   │               ├── gems/
│   │               │   ├── addressable-2.8.9/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   └── lib/
│   │               │   │       ├── addressable/
│   │               │   │       │   ├── idna/
│   │               │   │       │   │   ├── native.rb
│   │               │   │       │   │   └── pure.rb
│   │               │   │       │   ├── idna.rb
│   │               │   │       │   ├── template.rb
│   │               │   │       │   ├── uri.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── addressable.rb
│   │               │   ├── colorator-1.1.0/
│   │               │   │   ├── Gemfile
│   │               │   │   ├── History.markdown
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.markdown
│   │               │   │   ├── Rakefile
│   │               │   │   ├── colorator.gemspec
│   │               │   │   └── lib/
│   │               │   │       ├── colorator/
│   │               │   │       │   └── core_ext.rb
│   │               │   │       └── colorator.rb
│   │               │   ├── concurrent-ruby-1.3.6/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── ext/
│   │               │   │   │   └── concurrent-ruby/
│   │               │   │   │       ├── ConcurrentRubyService.java
│   │               │   │   │       └── com/
│   │               │   │   │           └── concurrent_ruby/
│   │               │   │   │               └── ext/
│   │               │   │   │                   ├── AtomicReferenceLibrary.java
│   │               │   │   │                   ├── JRubyMapBackendLibrary.java
│   │               │   │   │                   ├── JavaAtomicBooleanLibrary.java
│   │               │   │   │                   ├── JavaAtomicFixnumLibrary.java
│   │               │   │   │                   ├── JavaSemaphoreLibrary.java
│   │               │   │   │                   ├── SynchronizationLibrary.java
│   │               │   │   │                   ├── jsr166e/
│   │               │   │   │                   │   ├── ConcurrentHashMap.java
│   │               │   │   │                   │   ├── ConcurrentHashMapV8.java
│   │               │   │   │                   │   ├── LongAdder.java
│   │               │   │   │                   │   ├── Striped64.java
│   │               │   │   │                   │   └── nounsafe/
│   │               │   │   │                   │       ├── ConcurrentHashMapV8.java
│   │               │   │   │                   │       ├── LongAdder.java
│   │               │   │   │                   │       └── Striped64.java
│   │               │   │   │                   └── jsr166y/
│   │               │   │   │                       └── ThreadLocalRandom.java
│   │               │   │   └── lib/
│   │               │   │       └── concurrent-ruby/
│   │               │   │           ├── concurrent/
│   │               │   │           │   ├── agent.rb
│   │               │   │           │   ├── array.rb
│   │               │   │           │   ├── async.rb
│   │               │   │           │   ├── atom.rb
│   │               │   │           │   ├── atomic/
│   │               │   │           │   │   ├── atomic_boolean.rb
│   │               │   │           │   │   ├── atomic_fixnum.rb
│   │               │   │           │   │   ├── atomic_markable_reference.rb
│   │               │   │           │   │   ├── atomic_reference.rb
│   │               │   │           │   │   ├── count_down_latch.rb
│   │               │   │           │   │   ├── cyclic_barrier.rb
│   │               │   │           │   │   ├── event.rb
│   │               │   │           │   │   ├── fiber_local_var.rb
│   │               │   │           │   │   ├── java_count_down_latch.rb
│   │               │   │           │   │   ├── locals.rb
│   │               │   │           │   │   ├── lock_local_var.rb
│   │               │   │           │   │   ├── mutex_atomic_boolean.rb
│   │               │   │           │   │   ├── mutex_atomic_fixnum.rb
│   │               │   │           │   │   ├── mutex_count_down_latch.rb
│   │               │   │           │   │   ├── mutex_semaphore.rb
│   │               │   │           │   │   ├── read_write_lock.rb
│   │               │   │           │   │   ├── reentrant_read_write_lock.rb
│   │               │   │           │   │   ├── semaphore.rb
│   │               │   │           │   │   └── thread_local_var.rb
│   │               │   │           │   ├── atomic_reference/
│   │               │   │           │   │   ├── atomic_direct_update.rb
│   │               │   │           │   │   ├── mutex_atomic.rb
│   │               │   │           │   │   └── numeric_cas_wrapper.rb
│   │               │   │           │   ├── atomics.rb
│   │               │   │           │   ├── collection/
│   │               │   │           │   │   ├── copy_on_notify_observer_set.rb
│   │               │   │           │   │   ├── copy_on_write_observer_set.rb
│   │               │   │           │   │   ├── java_non_concurrent_priority_queue.rb
│   │               │   │           │   │   ├── lock_free_stack.rb
│   │               │   │           │   │   ├── map/
│   │               │   │           │   │   │   ├── mri_map_backend.rb
│   │               │   │           │   │   │   ├── non_concurrent_map_backend.rb
│   │               │   │           │   │   │   ├── synchronized_map_backend.rb
│   │               │   │           │   │   │   └── truffleruby_map_backend.rb
│   │               │   │           │   │   ├── non_concurrent_priority_queue.rb
│   │               │   │           │   │   ├── ruby_non_concurrent_priority_queue.rb
│   │               │   │           │   │   ├── ruby_timeout_queue.rb
│   │               │   │           │   │   └── timeout_queue.rb
│   │               │   │           │   ├── concern/
│   │               │   │           │   │   ├── deprecation.rb
│   │               │   │           │   │   ├── dereferenceable.rb
│   │               │   │           │   │   ├── logging.rb
│   │               │   │           │   │   ├── obligation.rb
│   │               │   │           │   │   └── observable.rb
│   │               │   │           │   ├── concurrent_ruby.jar
│   │               │   │           │   ├── configuration.rb
│   │               │   │           │   ├── constants.rb
│   │               │   │           │   ├── dataflow.rb
│   │               │   │           │   ├── delay.rb
│   │               │   │           │   ├── errors.rb
│   │               │   │           │   ├── exchanger.rb
│   │               │   │           │   ├── executor/
│   │               │   │           │   │   ├── abstract_executor_service.rb
│   │               │   │           │   │   ├── cached_thread_pool.rb
│   │               │   │           │   │   ├── executor_service.rb
│   │               │   │           │   │   ├── fixed_thread_pool.rb
│   │               │   │           │   │   ├── immediate_executor.rb
│   │               │   │           │   │   ├── indirect_immediate_executor.rb
│   │               │   │           │   │   ├── java_executor_service.rb
│   │               │   │           │   │   ├── java_single_thread_executor.rb
│   │               │   │           │   │   ├── java_thread_pool_executor.rb
│   │               │   │           │   │   ├── ruby_executor_service.rb
│   │               │   │           │   │   ├── ruby_single_thread_executor.rb
│   │               │   │           │   │   ├── ruby_thread_pool_executor.rb
│   │               │   │           │   │   ├── safe_task_executor.rb
│   │               │   │           │   │   ├── serial_executor_service.rb
│   │               │   │           │   │   ├── serialized_execution.rb
│   │               │   │           │   │   ├── serialized_execution_delegator.rb
│   │               │   │           │   │   ├── simple_executor_service.rb
│   │               │   │           │   │   ├── single_thread_executor.rb
│   │               │   │           │   │   ├── thread_pool_executor.rb
│   │               │   │           │   │   └── timer_set.rb
│   │               │   │           │   ├── executors.rb
│   │               │   │           │   ├── future.rb
│   │               │   │           │   ├── hash.rb
│   │               │   │           │   ├── immutable_struct.rb
│   │               │   │           │   ├── ivar.rb
│   │               │   │           │   ├── map.rb
│   │               │   │           │   ├── maybe.rb
│   │               │   │           │   ├── mutable_struct.rb
│   │               │   │           │   ├── mvar.rb
│   │               │   │           │   ├── options.rb
│   │               │   │           │   ├── promise.rb
│   │               │   │           │   ├── promises.rb
│   │               │   │           │   ├── re_include.rb
│   │               │   │           │   ├── scheduled_task.rb
│   │               │   │           │   ├── set.rb
│   │               │   │           │   ├── settable_struct.rb
│   │               │   │           │   ├── synchronization/
│   │               │   │           │   │   ├── abstract_lockable_object.rb
│   │               │   │           │   │   ├── abstract_object.rb
│   │               │   │           │   │   ├── abstract_struct.rb
│   │               │   │           │   │   ├── condition.rb
│   │               │   │           │   │   ├── full_memory_barrier.rb
│   │               │   │           │   │   ├── jruby_lockable_object.rb
│   │               │   │           │   │   ├── lock.rb
│   │               │   │           │   │   ├── lockable_object.rb
│   │               │   │           │   │   ├── mutex_lockable_object.rb
│   │               │   │           │   │   ├── object.rb
│   │               │   │           │   │   ├── safe_initialization.rb
│   │               │   │           │   │   └── volatile.rb
│   │               │   │           │   ├── synchronization.rb
│   │               │   │           │   ├── thread_safe/
│   │               │   │           │   │   ├── synchronized_delegator.rb
│   │               │   │           │   │   ├── util/
│   │               │   │           │   │   │   ├── adder.rb
│   │               │   │           │   │   │   ├── data_structures.rb
│   │               │   │           │   │   │   ├── power_of_two_tuple.rb
│   │               │   │           │   │   │   ├── striped64.rb
│   │               │   │           │   │   │   ├── volatile.rb
│   │               │   │           │   │   │   └── xor_shift_random.rb
│   │               │   │           │   │   └── util.rb
│   │               │   │           │   ├── timer_task.rb
│   │               │   │           │   ├── tuple.rb
│   │               │   │           │   ├── tvar.rb
│   │               │   │           │   ├── utility/
│   │               │   │           │   │   ├── engine.rb
│   │               │   │           │   │   ├── monotonic_time.rb
│   │               │   │           │   │   ├── native_extension_loader.rb
│   │               │   │           │   │   ├── native_integer.rb
│   │               │   │           │   │   └── processor_counter.rb
│   │               │   │           │   └── version.rb
│   │               │   │           ├── concurrent-ruby.rb
│   │               │   │           └── concurrent.rb
│   │               │   ├── em-websocket-0.5.3/
│   │               │   │   ├── .gitignore
│   │               │   │   ├── CHANGELOG.rdoc
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENCE
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── em-websocket.gemspec
│   │               │   │   ├── examples/
│   │               │   │   │   ├── echo.rb
│   │               │   │   │   ├── multicast.rb
│   │               │   │   │   ├── ping.rb
│   │               │   │   │   └── test.html
│   │               │   │   ├── lib/
│   │               │   │   │   ├── em-websocket/
│   │               │   │   │   │   ├── close03.rb
│   │               │   │   │   │   ├── close05.rb
│   │               │   │   │   │   ├── close06.rb
│   │               │   │   │   │   ├── close75.rb
│   │               │   │   │   │   ├── connection.rb
│   │               │   │   │   │   ├── debugger.rb
│   │               │   │   │   │   ├── framing03.rb
│   │               │   │   │   │   ├── framing04.rb
│   │               │   │   │   │   ├── framing05.rb
│   │               │   │   │   │   ├── framing07.rb
│   │               │   │   │   │   ├── framing76.rb
│   │               │   │   │   │   ├── handler.rb
│   │               │   │   │   │   ├── handler03.rb
│   │               │   │   │   │   ├── handler05.rb
│   │               │   │   │   │   ├── handler06.rb
│   │               │   │   │   │   ├── handler07.rb
│   │               │   │   │   │   ├── handler08.rb
│   │               │   │   │   │   ├── handler13.rb
│   │               │   │   │   │   ├── handler75.rb
│   │               │   │   │   │   ├── handler76.rb
│   │               │   │   │   │   ├── handshake.rb
│   │               │   │   │   │   ├── handshake04.rb
│   │               │   │   │   │   ├── handshake75.rb
│   │               │   │   │   │   ├── handshake76.rb
│   │               │   │   │   │   ├── masking04.rb
│   │               │   │   │   │   ├── message_processor_03.rb
│   │               │   │   │   │   ├── message_processor_06.rb
│   │               │   │   │   │   ├── version.rb
│   │               │   │   │   │   └── websocket.rb
│   │               │   │   │   └── em-websocket.rb
│   │               │   │   └── spec/
│   │               │   │       ├── helper.rb
│   │               │   │       ├── integration/
│   │               │   │       │   ├── common_spec.rb
│   │               │   │       │   ├── draft03_spec.rb
│   │               │   │       │   ├── draft05_spec.rb
│   │               │   │       │   ├── draft06_spec.rb
│   │               │   │       │   ├── draft13_spec.rb
│   │               │   │       │   ├── draft75_spec.rb
│   │               │   │       │   ├── draft76_spec.rb
│   │               │   │       │   ├── gte_03_examples.rb
│   │               │   │       │   └── shared_examples.rb
│   │               │   │       └── unit/
│   │               │   │           ├── framing_spec.rb
│   │               │   │           ├── handshake_spec.rb
│   │               │   │           └── masking_spec.rb
│   │               │   ├── eventmachine-1.2.7/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── GNU
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.md
│   │               │   │   ├── docs/
│   │               │   │   │   ├── DocumentationGuidesIndex.md
│   │               │   │   │   ├── GettingStarted.md
│   │               │   │   │   └── old/
│   │               │   │   │       ├── ChangeLog
│   │               │   │   │       ├── DEFERRABLES
│   │               │   │   │       ├── EPOLL
│   │               │   │   │       ├── INSTALL
│   │               │   │   │       ├── KEYBOARD
│   │               │   │   │       ├── LEGAL
│   │               │   │   │       ├── LIGHTWEIGHT_CONCURRENCY
│   │               │   │   │       ├── PURE_RUBY
│   │               │   │   │       ├── RELEASE_NOTES
│   │               │   │   │       ├── SMTP
│   │               │   │   │       ├── SPAWNED_PROCESSES
│   │               │   │   │       └── TODO
│   │               │   │   ├── examples/
│   │               │   │   │   ├── guides/
│   │               │   │   │   │   └── getting_started/
│   │               │   │   │   │       ├── 01_eventmachine_echo_server.rb
│   │               │   │   │   │       ├── 02_eventmachine_echo_server_that_recognizes_exit_command.rb
│   │               │   │   │   │       ├── 03_simple_chat_server.rb
│   │               │   │   │   │       ├── 04_simple_chat_server_step_one.rb
│   │               │   │   │   │       ├── 05_simple_chat_server_step_two.rb
│   │               │   │   │   │       ├── 06_simple_chat_server_step_three.rb
│   │               │   │   │   │       ├── 07_simple_chat_server_step_four.rb
│   │               │   │   │   │       └── 08_simple_chat_server_step_five.rb
│   │               │   │   │   └── old/
│   │               │   │   │       ├── ex_channel.rb
│   │               │   │   │       ├── ex_queue.rb
│   │               │   │   │       ├── ex_tick_loop_array.rb
│   │               │   │   │       ├── ex_tick_loop_counter.rb
│   │               │   │   │       └── helper.rb
│   │               │   │   ├── ext/
│   │               │   │   │   ├── .sitearchdir.time
│   │               │   │   │   ├── Makefile
│   │               │   │   │   ├── binder.cpp
│   │               │   │   │   ├── binder.h
│   │               │   │   │   ├── binder.o
│   │               │   │   │   ├── cmain.cpp
│   │               │   │   │   ├── cmain.o
│   │               │   │   │   ├── ed.cpp
│   │               │   │   │   ├── ed.h
│   │               │   │   │   ├── ed.o
│   │               │   │   │   ├── em.cpp
│   │               │   │   │   ├── em.h
│   │               │   │   │   ├── em.o
│   │               │   │   │   ├── eventmachine.h
│   │               │   │   │   ├── extconf.rb
│   │               │   │   │   ├── fastfilereader/
│   │               │   │   │   │   ├── .sitearchdir.time
│   │               │   │   │   │   ├── Makefile
│   │               │   │   │   │   ├── extconf.rb
│   │               │   │   │   │   ├── fastfilereaderext.bundle
│   │               │   │   │   │   ├── mapper.cpp
│   │               │   │   │   │   ├── mapper.h
│   │               │   │   │   │   ├── mapper.o
│   │               │   │   │   │   ├── rubymain.cpp
│   │               │   │   │   │   └── rubymain.o
│   │               │   │   │   ├── kb.cpp
│   │               │   │   │   ├── kb.o
│   │               │   │   │   ├── page.cpp
│   │               │   │   │   ├── page.h
│   │               │   │   │   ├── page.o
│   │               │   │   │   ├── pipe.cpp
│   │               │   │   │   ├── pipe.o
│   │               │   │   │   ├── project.h
│   │               │   │   │   ├── rubyeventmachine.bundle
│   │               │   │   │   ├── rubymain.cpp
│   │               │   │   │   ├── rubymain.o
│   │               │   │   │   ├── ssl.cpp
│   │               │   │   │   ├── ssl.h
│   │               │   │   │   └── ssl.o
│   │               │   │   ├── java/
│   │               │   │   │   ├── .classpath
│   │               │   │   │   ├── .project
│   │               │   │   │   └── src/
│   │               │   │   │       └── com/
│   │               │   │   │           └── rubyeventmachine/
│   │               │   │   │               ├── EmReactor.java
│   │               │   │   │               ├── EmReactorException.java
│   │               │   │   │               ├── EventableChannel.java
│   │               │   │   │               ├── EventableDatagramChannel.java
│   │               │   │   │               └── EventableSocketChannel.java
│   │               │   │   ├── lib/
│   │               │   │   │   ├── em/
│   │               │   │   │   │   ├── buftok.rb
│   │               │   │   │   │   ├── callback.rb
│   │               │   │   │   │   ├── channel.rb
│   │               │   │   │   │   ├── completion.rb
│   │               │   │   │   │   ├── connection.rb
│   │               │   │   │   │   ├── deferrable/
│   │               │   │   │   │   │   └── pool.rb
│   │               │   │   │   │   ├── deferrable.rb
│   │               │   │   │   │   ├── file_watch.rb
│   │               │   │   │   │   ├── future.rb
│   │               │   │   │   │   ├── iterator.rb
│   │               │   │   │   │   ├── messages.rb
│   │               │   │   │   │   ├── pool.rb
│   │               │   │   │   │   ├── process_watch.rb
│   │               │   │   │   │   ├── processes.rb
│   │               │   │   │   │   ├── protocols/
│   │               │   │   │   │   │   ├── header_and_content.rb
│   │               │   │   │   │   │   ├── httpclient.rb
│   │               │   │   │   │   │   ├── httpclient2.rb
│   │               │   │   │   │   │   ├── line_and_text.rb
│   │               │   │   │   │   │   ├── line_protocol.rb
│   │               │   │   │   │   │   ├── linetext2.rb
│   │               │   │   │   │   │   ├── memcache.rb
│   │               │   │   │   │   │   ├── object_protocol.rb
│   │               │   │   │   │   │   ├── postgres3.rb
│   │               │   │   │   │   │   ├── saslauth.rb
│   │               │   │   │   │   │   ├── smtpclient.rb
│   │               │   │   │   │   │   ├── smtpserver.rb
│   │               │   │   │   │   │   ├── socks4.rb
│   │               │   │   │   │   │   ├── stomp.rb
│   │               │   │   │   │   │   └── tcptest.rb
│   │               │   │   │   │   ├── protocols.rb
│   │               │   │   │   │   ├── pure_ruby.rb
│   │               │   │   │   │   ├── queue.rb
│   │               │   │   │   │   ├── resolver.rb
│   │               │   │   │   │   ├── spawnable.rb
│   │               │   │   │   │   ├── streamer.rb
│   │               │   │   │   │   ├── threaded_resource.rb
│   │               │   │   │   │   ├── tick_loop.rb
│   │               │   │   │   │   ├── timers.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   ├── eventmachine.rb
│   │               │   │   │   ├── fastfilereaderext.bundle
│   │               │   │   │   ├── jeventmachine.rb
│   │               │   │   │   └── rubyeventmachine.bundle
│   │               │   │   ├── rakelib/
│   │               │   │   │   ├── package.rake
│   │               │   │   │   ├── test.rake
│   │               │   │   │   └── test_pure.rake
│   │               │   │   └── tests/
│   │               │   │       ├── client.crt
│   │               │   │       ├── client.key
│   │               │   │       ├── dhparam.pem
│   │               │   │       ├── em_test_helper.rb
│   │               │   │       ├── test_attach.rb
│   │               │   │       ├── test_basic.rb
│   │               │   │       ├── test_channel.rb
│   │               │   │       ├── test_completion.rb
│   │               │   │       ├── test_connection_count.rb
│   │               │   │       ├── test_connection_write.rb
│   │               │   │       ├── test_defer.rb
│   │               │   │       ├── test_deferrable.rb
│   │               │   │       ├── test_epoll.rb
│   │               │   │       ├── test_error_handler.rb
│   │               │   │       ├── test_exc.rb
│   │               │   │       ├── test_file_watch.rb
│   │               │   │       ├── test_fork.rb
│   │               │   │       ├── test_futures.rb
│   │               │   │       ├── test_handler_check.rb
│   │               │   │       ├── test_hc.rb
│   │               │   │       ├── test_httpclient.rb
│   │               │   │       ├── test_httpclient2.rb
│   │               │   │       ├── test_idle_connection.rb
│   │               │   │       ├── test_inactivity_timeout.rb
│   │               │   │       ├── test_ipv4.rb
│   │               │   │       ├── test_ipv6.rb
│   │               │   │       ├── test_iterator.rb
│   │               │   │       ├── test_kb.rb
│   │               │   │       ├── test_line_protocol.rb
│   │               │   │       ├── test_ltp.rb
│   │               │   │       ├── test_ltp2.rb
│   │               │   │       ├── test_many_fds.rb
│   │               │   │       ├── test_next_tick.rb
│   │               │   │       ├── test_object_protocol.rb
│   │               │   │       ├── test_pause.rb
│   │               │   │       ├── test_pending_connect_timeout.rb
│   │               │   │       ├── test_pool.rb
│   │               │   │       ├── test_process_watch.rb
│   │               │   │       ├── test_processes.rb
│   │               │   │       ├── test_proxy_connection.rb
│   │               │   │       ├── test_pure.rb
│   │               │   │       ├── test_queue.rb
│   │               │   │       ├── test_resolver.rb
│   │               │   │       ├── test_running.rb
│   │               │   │       ├── test_sasl.rb
│   │               │   │       ├── test_send_file.rb
│   │               │   │       ├── test_servers.rb
│   │               │   │       ├── test_shutdown_hooks.rb
│   │               │   │       ├── test_smtpclient.rb
│   │               │   │       ├── test_smtpserver.rb
│   │               │   │       ├── test_sock_opt.rb
│   │               │   │       ├── test_spawn.rb
│   │               │   │       ├── test_ssl_args.rb
│   │               │   │       ├── test_ssl_dhparam.rb
│   │               │   │       ├── test_ssl_ecdh_curve.rb
│   │               │   │       ├── test_ssl_extensions.rb
│   │               │   │       ├── test_ssl_methods.rb
│   │               │   │       ├── test_ssl_protocols.rb
│   │               │   │       ├── test_ssl_verify.rb
│   │               │   │       ├── test_stomp.rb
│   │               │   │       ├── test_system.rb
│   │               │   │       ├── test_threaded_resource.rb
│   │               │   │       ├── test_tick_loop.rb
│   │               │   │       ├── test_timers.rb
│   │               │   │       ├── test_ud.rb
│   │               │   │       └── test_unbind_reason.rb
│   │               │   ├── ffi-1.17.3/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── COPYING
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE
│   │               │   │   ├── LICENSE.SPECS
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── Steepfile
│   │               │   │   ├── ext/
│   │               │   │   │   └── ffi_c/
│   │               │   │   │       ├── .sitearchdir.time
│   │               │   │   │       ├── AbstractMemory.c
│   │               │   │   │       ├── AbstractMemory.h
│   │               │   │   │       ├── AbstractMemory.o
│   │               │   │   │       ├── ArrayType.c
│   │               │   │   │       ├── ArrayType.h
│   │               │   │   │       ├── ArrayType.o
│   │               │   │   │       ├── Buffer.c
│   │               │   │   │       ├── Buffer.o
│   │               │   │   │       ├── Call.c
│   │               │   │   │       ├── Call.h
│   │               │   │   │       ├── Call.o
│   │               │   │   │       ├── ClosurePool.c
│   │               │   │   │       ├── ClosurePool.h
│   │               │   │   │       ├── ClosurePool.o
│   │               │   │   │       ├── DynamicLibrary.c
│   │               │   │   │       ├── DynamicLibrary.h
│   │               │   │   │       ├── DynamicLibrary.o
│   │               │   │   │       ├── Function.c
│   │               │   │   │       ├── Function.h
│   │               │   │   │       ├── Function.o
│   │               │   │   │       ├── FunctionInfo.c
│   │               │   │   │       ├── FunctionInfo.o
│   │               │   │   │       ├── LastError.c
│   │               │   │   │       ├── LastError.h
│   │               │   │   │       ├── LastError.o
│   │               │   │   │       ├── LongDouble.c
│   │               │   │   │       ├── LongDouble.h
│   │               │   │   │       ├── LongDouble.o
│   │               │   │   │       ├── Makefile
│   │               │   │   │       ├── MappedType.c
│   │               │   │   │       ├── MappedType.h
│   │               │   │   │       ├── MappedType.o
│   │               │   │   │       ├── MemoryPointer.c
│   │               │   │   │       ├── MemoryPointer.h
│   │               │   │   │       ├── MemoryPointer.o
│   │               │   │   │       ├── MethodHandle.c
│   │               │   │   │       ├── MethodHandle.h
│   │               │   │   │       ├── MethodHandle.o
│   │               │   │   │       ├── Platform.c
│   │               │   │   │       ├── Platform.h
│   │               │   │   │       ├── Platform.o
│   │               │   │   │       ├── Pointer.c
│   │               │   │   │       ├── Pointer.h
│   │               │   │   │       ├── Pointer.o
│   │               │   │   │       ├── Struct.c
│   │               │   │   │       ├── Struct.h
│   │               │   │   │       ├── Struct.o
│   │               │   │   │       ├── StructByValue.c
│   │               │   │   │       ├── StructByValue.h
│   │               │   │   │       ├── StructByValue.o
│   │               │   │   │       ├── StructLayout.c
│   │               │   │   │       ├── StructLayout.o
│   │               │   │   │       ├── Thread.c
│   │               │   │   │       ├── Thread.h
│   │               │   │   │       ├── Thread.o
│   │               │   │   │       ├── Type.c
│   │               │   │   │       ├── Type.h
│   │               │   │   │       ├── Type.o
│   │               │   │   │       ├── Types.c
│   │               │   │   │       ├── Types.h
│   │               │   │   │       ├── Types.o
│   │               │   │   │       ├── Variadic.c
│   │               │   │   │       ├── Variadic.o
│   │               │   │   │       ├── compat.h
│   │               │   │   │       ├── extconf.h
│   │               │   │   │       ├── extconf.rb
│   │               │   │   │       ├── ffi.c
│   │               │   │   │       ├── ffi.o
│   │               │   │   │       ├── ffi_c.bundle
│   │               │   │   │       ├── libffi/
│   │               │   │   │       │   ├── .allow-ai-service
│   │               │   │   │       │   ├── .ci/
│   │               │   │   │       │   │   ├── Containerfile.ppc64le
│   │               │   │   │       │   │   ├── ar-lib
│   │               │   │   │       │   │   ├── bfin-sim.exp
│   │               │   │   │       │   │   ├── build-cross-in-container.sh
│   │               │   │   │       │   │   ├── build-in-container.sh
│   │               │   │   │       │   │   ├── build.sh
│   │               │   │   │       │   │   ├── compile
│   │               │   │   │       │   │   ├── install.sh
│   │               │   │   │       │   │   ├── m32r-sim.exp
│   │               │   │   │       │   │   ├── moxie-sim.exp
│   │               │   │   │       │   │   ├── msvs-detect
│   │               │   │   │       │   │   ├── or1k-sim.exp
│   │               │   │   │       │   │   ├── powerpc-eabisim.exp
│   │               │   │   │       │   │   ├── site.exp
│   │               │   │   │       │   │   ├── unix-noexec.exp
│   │               │   │   │       │   │   └── wine-sim.exp
│   │               │   │   │       │   ├── .gail-labels
│   │               │   │   │       │   ├── .gitattributes
│   │               │   │   │       │   ├── .github/
│   │               │   │   │       │   │   ├── issue_template.md
│   │               │   │   │       │   │   └── workflows/
│   │               │   │   │       │   │       ├── build.yml
│   │               │   │   │       │   │       ├── emscripten.yml
│   │               │   │   │       │   │       ├── label-new-issue.yaml
│   │               │   │   │       │   │       └── tarball.yml
│   │               │   │   │       │   ├── .gitignore
│   │               │   │   │       │   ├── ChangeLog.old
│   │               │   │   │       │   ├── LICENSE
│   │               │   │   │       │   ├── LICENSE-BUILDTOOLS
│   │               │   │   │       │   ├── Makefile.am
│   │               │   │   │       │   ├── Makefile.in
│   │               │   │   │       │   ├── README.md
│   │               │   │   │       │   ├── acinclude.m4
│   │               │   │   │       │   ├── autogen.sh
│   │               │   │   │       │   ├── compile
│   │               │   │   │       │   ├── config.guess
│   │               │   │   │       │   ├── config.sub
│   │               │   │   │       │   ├── configure
│   │               │   │   │       │   ├── configure.ac
│   │               │   │   │       │   ├── configure.host
│   │               │   │   │       │   ├── doc/
│   │               │   │   │       │   │   ├── Makefile.am
│   │               │   │   │       │   │   ├── Makefile.in
│   │               │   │   │       │   │   ├── libffi.texi
│   │               │   │   │       │   │   └── version.texi
│   │               │   │   │       │   ├── fficonfig.h.in
│   │               │   │   │       │   ├── generate-darwin-source-and-headers.py
│   │               │   │   │       │   ├── include/
│   │               │   │   │       │   │   ├── Makefile.am
│   │               │   │   │       │   │   ├── Makefile.in
│   │               │   │   │       │   │   ├── ffi.h.in
│   │               │   │   │       │   │   ├── ffi_cfi.h
│   │               │   │   │       │   │   ├── ffi_common.h
│   │               │   │   │       │   │   └── tramp.h
│   │               │   │   │       │   ├── install-sh
│   │               │   │   │       │   ├── libffi.map.in
│   │               │   │   │       │   ├── libffi.pc.in
│   │               │   │   │       │   ├── libffi.xcodeproj/
│   │               │   │   │       │   │   └── project.pbxproj
│   │               │   │   │       │   ├── libtool-ldflags
│   │               │   │   │       │   ├── libtool-version
│   │               │   │   │       │   ├── ltmain.sh
│   │               │   │   │       │   ├── m4/
│   │               │   │   │       │   │   ├── asmcfi.m4
│   │               │   │   │       │   │   ├── ax_append_flag.m4
│   │               │   │   │       │   │   ├── ax_cc_maxopt.m4
│   │               │   │   │       │   │   ├── ax_cflags_warn_all.m4
│   │               │   │   │       │   │   ├── ax_check_compile_flag.m4
│   │               │   │   │       │   │   ├── ax_compiler_vendor.m4
│   │               │   │   │       │   │   ├── ax_configure_args.m4
│   │               │   │   │       │   │   ├── ax_enable_builddir.m4
│   │               │   │   │       │   │   ├── ax_gcc_archflag.m4
│   │               │   │   │       │   │   ├── ax_gcc_x86_cpuid.m4
│   │               │   │   │       │   │   ├── ax_prepend_flag.m4
│   │               │   │   │       │   │   └── ax_require_defined.m4
│   │               │   │   │       │   ├── make_sunver.pl
│   │               │   │   │       │   ├── man/
│   │               │   │   │       │   │   ├── Makefile.am
│   │               │   │   │       │   │   ├── Makefile.in
│   │               │   │   │       │   │   ├── ffi.3
│   │               │   │   │       │   │   ├── ffi_call.3
│   │               │   │   │       │   │   ├── ffi_prep_cif.3
│   │               │   │   │       │   │   └── ffi_prep_cif_var.3
│   │               │   │   │       │   ├── missing
│   │               │   │   │       │   ├── msvc_build/
│   │               │   │   │       │   │   └── aarch64/
│   │               │   │   │       │   │       ├── Ffi_staticLib.sln
│   │               │   │   │       │   │       ├── Ffi_staticLib.vcxproj
│   │               │   │   │       │   │       ├── Ffi_staticLib.vcxproj.filters
│   │               │   │   │       │   │       ├── Ffi_staticLib.vcxproj.user
│   │               │   │   │       │   │       └── aarch64_include/
│   │               │   │   │       │   │           ├── ffi.h
│   │               │   │   │       │   │           └── fficonfig.h
│   │               │   │   │       │   ├── msvcc.sh
│   │               │   │   │       │   ├── src/
│   │               │   │   │       │   │   ├── aarch64/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   ├── sysv.S
│   │               │   │   │       │   │   │   └── win64_armasm.S
│   │               │   │   │       │   │   ├── alpha/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   └── osf.S
│   │               │   │   │       │   │   ├── arc/
│   │               │   │   │       │   │   │   ├── arcompact.S
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   └── ffitarget.h
│   │               │   │   │       │   │   ├── arm/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   ├── sysv.S
│   │               │   │   │       │   │   │   └── sysv_msvc_arm32.S
│   │               │   │   │       │   │   ├── avr32/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── bfin/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── closures.c
│   │               │   │   │       │   │   ├── cris/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── csky/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── debug.c
│   │               │   │   │       │   │   ├── dlmalloc.c
│   │               │   │   │       │   │   ├── frv/
│   │               │   │   │       │   │   │   ├── eabi.S
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   └── ffitarget.h
│   │               │   │   │       │   │   ├── ia64/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── ia64_flags.h
│   │               │   │   │       │   │   │   └── unix.S
│   │               │   │   │       │   │   ├── java_raw_api.c
│   │               │   │   │       │   │   ├── kvx/
│   │               │   │   │       │   │   │   ├── asm.h
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── loongarch64/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── m32r/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── m68k/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── m88k/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── obsd.S
│   │               │   │   │       │   │   ├── metag/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── microblaze/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── mips/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── n32.S
│   │               │   │   │       │   │   │   └── o32.S
│   │               │   │   │       │   │   ├── moxie/
│   │               │   │   │       │   │   │   ├── eabi.S
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   └── ffitarget.h
│   │               │   │   │       │   │   ├── or1k/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── pa/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffi64.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── hpux32.S
│   │               │   │   │       │   │   │   ├── hpux64.S
│   │               │   │   │       │   │   │   └── linux.S
│   │               │   │   │       │   │   ├── powerpc/
│   │               │   │   │       │   │   │   ├── aix.S
│   │               │   │   │       │   │   │   ├── aix_closure.S
│   │               │   │   │       │   │   │   ├── asm.h
│   │               │   │   │       │   │   │   ├── darwin.S
│   │               │   │   │       │   │   │   ├── darwin_closure.S
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffi_darwin.c
│   │               │   │   │       │   │   │   ├── ffi_linux64.c
│   │               │   │   │       │   │   │   ├── ffi_powerpc.h
│   │               │   │   │       │   │   │   ├── ffi_sysv.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   ├── linux64.S
│   │               │   │   │       │   │   │   ├── linux64_closure.S
│   │               │   │   │       │   │   │   ├── ppc_closure.S
│   │               │   │   │       │   │   │   ├── sysv.S
│   │               │   │   │       │   │   │   └── t-aix
│   │               │   │   │       │   │   ├── prep_cif.c
│   │               │   │   │       │   │   ├── raw_api.c
│   │               │   │   │       │   │   ├── riscv/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── s390/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── sh/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── sh64/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── sysv.S
│   │               │   │   │       │   │   ├── sparc/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffi64.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   ├── v8.S
│   │               │   │   │       │   │   │   └── v9.S
│   │               │   │   │       │   │   ├── tile/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   └── tile.S
│   │               │   │   │       │   │   ├── tramp.c
│   │               │   │   │       │   │   ├── types.c
│   │               │   │   │       │   │   ├── vax/
│   │               │   │   │       │   │   │   ├── elfbsd.S
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   └── ffitarget.h
│   │               │   │   │       │   │   ├── wasm/
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   └── ffitarget.h
│   │               │   │   │       │   │   ├── x86/
│   │               │   │   │       │   │   │   ├── asmnames.h
│   │               │   │   │       │   │   │   ├── ffi.c
│   │               │   │   │       │   │   │   ├── ffi64.c
│   │               │   │   │       │   │   │   ├── ffitarget.h
│   │               │   │   │       │   │   │   ├── ffiw64.c
│   │               │   │   │       │   │   │   ├── internal.h
│   │               │   │   │       │   │   │   ├── internal64.h
│   │               │   │   │       │   │   │   ├── sysv.S
│   │               │   │   │       │   │   │   ├── sysv_intel.S
│   │               │   │   │       │   │   │   ├── unix64.S
│   │               │   │   │       │   │   │   ├── win64.S
│   │               │   │   │       │   │   │   └── win64_intel.S
│   │               │   │   │       │   │   └── xtensa/
│   │               │   │   │       │   │       ├── ffi.c
│   │               │   │   │       │   │       ├── ffitarget.h
│   │               │   │   │       │   │       └── sysv.S
│   │               │   │   │       │   ├── stamp-h.in
│   │               │   │   │       │   └── testsuite/
│   │               │   │   │       │       ├── Makefile.am
│   │               │   │   │       │       ├── Makefile.in
│   │               │   │   │       │       ├── config/
│   │               │   │   │       │       │   └── default.exp
│   │               │   │   │       │       ├── emscripten/
│   │               │   │   │       │       │   ├── build-tests.sh
│   │               │   │   │       │       │   ├── build.sh
│   │               │   │   │       │       │   ├── conftest.py
│   │               │   │   │       │       │   ├── node-tests.sh
│   │               │   │   │       │       │   ├── test.html
│   │               │   │   │       │       │   └── test_libffi.py
│   │               │   │   │       │       ├── lib/
│   │               │   │   │       │       │   ├── libffi.exp
│   │               │   │   │       │       │   ├── target-libpath.exp
│   │               │   │   │       │       │   └── wrapper.exp
│   │               │   │   │       │       ├── libffi.bhaible/
│   │               │   │   │       │       │   ├── Makefile
│   │               │   │   │       │       │   ├── README
│   │               │   │   │       │       │   ├── alignof.h
│   │               │   │   │       │       │   ├── bhaible.exp
│   │               │   │   │       │       │   ├── test-call.c
│   │               │   │   │       │       │   ├── test-callback.c
│   │               │   │   │       │       │   └── testcases.c
│   │               │   │   │       │       ├── libffi.call/
│   │               │   │   │       │       │   ├── align_mixed.c
│   │               │   │   │       │       │   ├── align_stdcall.c
│   │               │   │   │       │       │   ├── bpo_38748.c
│   │               │   │   │       │       │   ├── call.exp
│   │               │   │   │       │       │   ├── callback.c
│   │               │   │   │       │       │   ├── callback2.c
│   │               │   │   │       │       │   ├── callback3.c
│   │               │   │   │       │       │   ├── callback4.c
│   │               │   │   │       │       │   ├── err_bad_typedef.c
│   │               │   │   │       │       │   ├── ffitest.h
│   │               │   │   │       │       │   ├── float.c
│   │               │   │   │       │       │   ├── float1.c
│   │               │   │   │       │       │   ├── float2.c
│   │               │   │   │       │       │   ├── float3.c
│   │               │   │   │       │       │   ├── float4.c
│   │               │   │   │       │       │   ├── float_va.c
│   │               │   │   │       │       │   ├── longjmp.c
│   │               │   │   │       │       │   ├── many.c
│   │               │   │   │       │       │   ├── many2.c
│   │               │   │   │       │       │   ├── many_double.c
│   │               │   │   │       │       │   ├── many_mixed.c
│   │               │   │   │       │       │   ├── negint.c
│   │               │   │   │       │       │   ├── offsets.c
│   │               │   │   │       │       │   ├── overread.c
│   │               │   │   │       │       │   ├── pr1172638.c
│   │               │   │   │       │       │   ├── promotion.c
│   │               │   │   │       │       │   ├── pyobjc_tc.c
│   │               │   │   │       │       │   ├── return_dbl.c
│   │               │   │   │       │       │   ├── return_dbl1.c
│   │               │   │   │       │       │   ├── return_dbl2.c
│   │               │   │   │       │       │   ├── return_fl.c
│   │               │   │   │       │       │   ├── return_fl1.c
│   │               │   │   │       │       │   ├── return_fl2.c
│   │               │   │   │       │       │   ├── return_fl3.c
│   │               │   │   │       │       │   ├── return_ldl.c
│   │               │   │   │       │       │   ├── return_ll.c
│   │               │   │   │       │       │   ├── return_ll1.c
│   │               │   │   │       │       │   ├── return_sc.c
│   │               │   │   │       │       │   ├── return_sl.c
│   │               │   │   │       │       │   ├── return_uc.c
│   │               │   │   │       │       │   ├── return_ul.c
│   │               │   │   │       │       │   ├── s55.c
│   │               │   │   │       │       │   ├── strlen.c
│   │               │   │   │       │       │   ├── strlen2.c
│   │               │   │   │       │       │   ├── strlen3.c
│   │               │   │   │       │       │   ├── strlen4.c
│   │               │   │   │       │       │   ├── struct1.c
│   │               │   │   │       │       │   ├── struct10.c
│   │               │   │   │       │       │   ├── struct2.c
│   │               │   │   │       │       │   ├── struct3.c
│   │               │   │   │       │       │   ├── struct4.c
│   │               │   │   │       │       │   ├── struct5.c
│   │               │   │   │       │       │   ├── struct6.c
│   │               │   │   │       │       │   ├── struct7.c
│   │               │   │   │       │       │   ├── struct8.c
│   │               │   │   │       │       │   ├── struct9.c
│   │               │   │   │       │       │   ├── struct_by_value_2.c
│   │               │   │   │       │       │   ├── struct_by_value_3.c
│   │               │   │   │       │       │   ├── struct_by_value_3f.c
│   │               │   │   │       │       │   ├── struct_by_value_4.c
│   │               │   │   │       │       │   ├── struct_by_value_4f.c
│   │               │   │   │       │       │   ├── struct_by_value_big.c
│   │               │   │   │       │       │   ├── struct_by_value_small.c
│   │               │   │   │       │       │   ├── struct_int_float.c
│   │               │   │   │       │       │   ├── struct_return_2H.c
│   │               │   │   │       │       │   ├── struct_return_8H.c
│   │               │   │   │       │       │   ├── uninitialized.c
│   │               │   │   │       │       │   ├── va_1.c
│   │               │   │   │       │       │   ├── va_2.c
│   │               │   │   │       │       │   ├── va_3.c
│   │               │   │   │       │       │   ├── va_struct1.c
│   │               │   │   │       │       │   ├── va_struct2.c
│   │               │   │   │       │       │   ├── va_struct3.c
│   │               │   │   │       │       │   └── x32.c
│   │               │   │   │       │       ├── libffi.closures/
│   │               │   │   │       │       │   ├── closure.exp
│   │               │   │   │       │       │   ├── closure_fn0.c
│   │               │   │   │       │       │   ├── closure_fn1.c
│   │               │   │   │       │       │   ├── closure_fn2.c
│   │               │   │   │       │       │   ├── closure_fn3.c
│   │               │   │   │       │       │   ├── closure_fn4.c
│   │               │   │   │       │       │   ├── closure_fn5.c
│   │               │   │   │       │       │   ├── closure_fn6.c
│   │               │   │   │       │       │   ├── closure_loc_fn0.c
│   │               │   │   │       │       │   ├── closure_simple.c
│   │               │   │   │       │       │   ├── cls_12byte.c
│   │               │   │   │       │       │   ├── cls_16byte.c
│   │               │   │   │       │       │   ├── cls_18byte.c
│   │               │   │   │       │       │   ├── cls_19byte.c
│   │               │   │   │       │       │   ├── cls_1_1byte.c
│   │               │   │   │       │       │   ├── cls_20byte.c
│   │               │   │   │       │       │   ├── cls_20byte1.c
│   │               │   │   │       │       │   ├── cls_24byte.c
│   │               │   │   │       │       │   ├── cls_2byte.c
│   │               │   │   │       │       │   ├── cls_3_1byte.c
│   │               │   │   │       │       │   ├── cls_3byte1.c
│   │               │   │   │       │       │   ├── cls_3byte2.c
│   │               │   │   │       │       │   ├── cls_3float.c
│   │               │   │   │       │       │   ├── cls_4_1byte.c
│   │               │   │   │       │       │   ├── cls_4byte.c
│   │               │   │   │       │       │   ├── cls_5_1_byte.c
│   │               │   │   │       │       │   ├── cls_5byte.c
│   │               │   │   │       │       │   ├── cls_64byte.c
│   │               │   │   │       │       │   ├── cls_6_1_byte.c
│   │               │   │   │       │       │   ├── cls_6byte.c
│   │               │   │   │       │       │   ├── cls_7_1_byte.c
│   │               │   │   │       │       │   ├── cls_7byte.c
│   │               │   │   │       │       │   ├── cls_8byte.c
│   │               │   │   │       │       │   ├── cls_9byte1.c
│   │               │   │   │       │       │   ├── cls_9byte2.c
│   │               │   │   │       │       │   ├── cls_align_double.c
│   │               │   │   │       │       │   ├── cls_align_float.c
│   │               │   │   │       │       │   ├── cls_align_longdouble.c
│   │               │   │   │       │       │   ├── cls_align_longdouble_split.c
│   │               │   │   │       │       │   ├── cls_align_longdouble_split2.c
│   │               │   │   │       │       │   ├── cls_align_pointer.c
│   │               │   │   │       │       │   ├── cls_align_sint16.c
│   │               │   │   │       │       │   ├── cls_align_sint32.c
│   │               │   │   │       │       │   ├── cls_align_sint64.c
│   │               │   │   │       │       │   ├── cls_align_uint16.c
│   │               │   │   │       │       │   ├── cls_align_uint32.c
│   │               │   │   │       │       │   ├── cls_align_uint64.c
│   │               │   │   │       │       │   ├── cls_dbls_struct.c
│   │               │   │   │       │       │   ├── cls_double.c
│   │               │   │   │       │       │   ├── cls_double_va.c
│   │               │   │   │       │       │   ├── cls_float.c
│   │               │   │   │       │       │   ├── cls_longdouble.c
│   │               │   │   │       │       │   ├── cls_longdouble_va.c
│   │               │   │   │       │       │   ├── cls_many_mixed_args.c
│   │               │   │   │       │       │   ├── cls_many_mixed_float_double.c
│   │               │   │   │       │       │   ├── cls_multi_schar.c
│   │               │   │   │       │       │   ├── cls_multi_sshort.c
│   │               │   │   │       │       │   ├── cls_multi_sshortchar.c
│   │               │   │   │       │       │   ├── cls_multi_uchar.c
│   │               │   │   │       │       │   ├── cls_multi_ushort.c
│   │               │   │   │       │       │   ├── cls_multi_ushortchar.c
│   │               │   │   │       │       │   ├── cls_pointer.c
│   │               │   │   │       │       │   ├── cls_pointer_stack.c
│   │               │   │   │       │       │   ├── cls_schar.c
│   │               │   │   │       │       │   ├── cls_sint.c
│   │               │   │   │       │       │   ├── cls_sshort.c
│   │               │   │   │       │       │   ├── cls_struct_va1.c
│   │               │   │   │       │       │   ├── cls_uchar.c
│   │               │   │   │       │       │   ├── cls_uint.c
│   │               │   │   │       │       │   ├── cls_uint_va.c
│   │               │   │   │       │       │   ├── cls_ulong_va.c
│   │               │   │   │       │       │   ├── cls_ulonglong.c
│   │               │   │   │       │       │   ├── cls_ushort.c
│   │               │   │   │       │       │   ├── err_bad_abi.c
│   │               │   │   │       │       │   ├── ffitest.h
│   │               │   │   │       │       │   ├── huge_struct.c
│   │               │   │   │       │       │   ├── nested_struct.c
│   │               │   │   │       │       │   ├── nested_struct1.c
│   │               │   │   │       │       │   ├── nested_struct10.c
│   │               │   │   │       │       │   ├── nested_struct11.c
│   │               │   │   │       │       │   ├── nested_struct12.c
│   │               │   │   │       │       │   ├── nested_struct13.c
│   │               │   │   │       │       │   ├── nested_struct2.c
│   │               │   │   │       │       │   ├── nested_struct3.c
│   │               │   │   │       │       │   ├── nested_struct4.c
│   │               │   │   │       │       │   ├── nested_struct5.c
│   │               │   │   │       │       │   ├── nested_struct6.c
│   │               │   │   │       │       │   ├── nested_struct7.c
│   │               │   │   │       │       │   ├── nested_struct8.c
│   │               │   │   │       │       │   ├── nested_struct9.c
│   │               │   │   │       │       │   ├── problem1.c
│   │               │   │   │       │       │   ├── single_entry_structs1.c
│   │               │   │   │       │       │   ├── single_entry_structs2.c
│   │               │   │   │       │       │   ├── single_entry_structs3.c
│   │               │   │   │       │       │   ├── stret_large.c
│   │               │   │   │       │       │   ├── stret_large2.c
│   │               │   │   │       │       │   ├── stret_medium.c
│   │               │   │   │       │       │   ├── stret_medium2.c
│   │               │   │   │       │       │   ├── testclosure.c
│   │               │   │   │       │       │   ├── unwindtest.cc
│   │               │   │   │       │       │   └── unwindtest_ffi_call.cc
│   │               │   │   │       │       ├── libffi.complex/
│   │               │   │   │       │       │   ├── cls_align_complex.inc
│   │               │   │   │       │       │   ├── cls_align_complex_double.c
│   │               │   │   │       │       │   ├── cls_align_complex_float.c
│   │               │   │   │       │       │   ├── cls_align_complex_longdouble.c
│   │               │   │   │       │       │   ├── cls_complex.inc
│   │               │   │   │       │       │   ├── cls_complex_double.c
│   │               │   │   │       │       │   ├── cls_complex_float.c
│   │               │   │   │       │       │   ├── cls_complex_longdouble.c
│   │               │   │   │       │       │   ├── cls_complex_struct.inc
│   │               │   │   │       │       │   ├── cls_complex_struct_double.c
│   │               │   │   │       │       │   ├── cls_complex_struct_float.c
│   │               │   │   │       │       │   ├── cls_complex_struct_longdouble.c
│   │               │   │   │       │       │   ├── cls_complex_va.inc
│   │               │   │   │       │       │   ├── cls_complex_va_double.c
│   │               │   │   │       │       │   ├── cls_complex_va_float.c
│   │               │   │   │       │       │   ├── cls_complex_va_longdouble.c
│   │               │   │   │       │       │   ├── complex.exp
│   │               │   │   │       │       │   ├── complex.inc
│   │               │   │   │       │       │   ├── complex_defs_double.inc
│   │               │   │   │       │       │   ├── complex_defs_float.inc
│   │               │   │   │       │       │   ├── complex_defs_longdouble.inc
│   │               │   │   │       │       │   ├── complex_double.c
│   │               │   │   │       │       │   ├── complex_float.c
│   │               │   │   │       │       │   ├── complex_int.c
│   │               │   │   │       │       │   ├── complex_longdouble.c
│   │               │   │   │       │       │   ├── ffitest.h
│   │               │   │   │       │       │   ├── many_complex.inc
│   │               │   │   │       │       │   ├── many_complex_double.c
│   │               │   │   │       │       │   ├── many_complex_float.c
│   │               │   │   │       │       │   ├── many_complex_longdouble.c
│   │               │   │   │       │       │   ├── return_complex.inc
│   │               │   │   │       │       │   ├── return_complex1.inc
│   │               │   │   │       │       │   ├── return_complex1_double.c
│   │               │   │   │       │       │   ├── return_complex1_float.c
│   │               │   │   │       │       │   ├── return_complex1_longdouble.c
│   │               │   │   │       │       │   ├── return_complex2.inc
│   │               │   │   │       │       │   ├── return_complex2_double.c
│   │               │   │   │       │       │   ├── return_complex2_float.c
│   │               │   │   │       │       │   ├── return_complex2_longdouble.c
│   │               │   │   │       │       │   ├── return_complex_double.c
│   │               │   │   │       │       │   ├── return_complex_float.c
│   │               │   │   │       │       │   └── return_complex_longdouble.c
│   │               │   │   │       │       ├── libffi.go/
│   │               │   │   │       │       │   ├── aa-direct.c
│   │               │   │   │       │       │   ├── closure1.c
│   │               │   │   │       │       │   ├── ffitest.h
│   │               │   │   │       │       │   ├── go.exp
│   │               │   │   │       │       │   └── static-chain.h
│   │               │   │   │       │       └── libffi.threads/
│   │               │   │   │       │           ├── ffitest.h
│   │               │   │   │       │           ├── threads.exp
│   │               │   │   │       │           └── tsan.c
│   │               │   │   │       ├── libffi.bsd.mk
│   │               │   │   │       ├── libffi.darwin.mk
│   │               │   │   │       ├── libffi.gnu.mk
│   │               │   │   │       ├── libffi.mk
│   │               │   │   │       ├── libffi.vc.mk
│   │               │   │   │       ├── libffi.vc64.mk
│   │               │   │   │       ├── rbffi.h
│   │               │   │   │       └── rbffi_endian.h
│   │               │   │   ├── ffi.gemspec
│   │               │   │   ├── lib/
│   │               │   │   │   ├── ffi/
│   │               │   │   │   │   ├── abstract_memory.rb
│   │               │   │   │   │   ├── autopointer.rb
│   │               │   │   │   │   ├── buffer.rb
│   │               │   │   │   │   ├── callback.rb
│   │               │   │   │   │   ├── compat.rb
│   │               │   │   │   │   ├── data_converter.rb
│   │               │   │   │   │   ├── dynamic_library.rb
│   │               │   │   │   │   ├── enum.rb
│   │               │   │   │   │   ├── errno.rb
│   │               │   │   │   │   ├── ffi.rb
│   │               │   │   │   │   ├── function.rb
│   │               │   │   │   │   ├── io.rb
│   │               │   │   │   │   ├── library.rb
│   │               │   │   │   │   ├── library_path.rb
│   │               │   │   │   │   ├── managedstruct.rb
│   │               │   │   │   │   ├── memorypointer.rb
│   │               │   │   │   │   ├── platform/
│   │               │   │   │   │   │   ├── aarch64-darwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── aarch64-freebsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── aarch64-freebsd12/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── aarch64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── aarch64-openbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── aarch64-windows/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── arm-freebsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── arm-freebsd12/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── arm-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── hppa1.1-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── hppa2.0-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-cygwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-darwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-freebsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-freebsd12/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-gnu/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-netbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-openbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-solaris/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── i386-windows/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── ia64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── loongarch64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mips-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mips64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mips64el-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mipsel-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mipsisa32r6-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mipsisa32r6el-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mipsisa64r6-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── mipsisa64r6el-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc-aix/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc-darwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc-openbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── powerpc64le-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── riscv64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── s390-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── s390x-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sparc-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sparc-solaris/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sparcv9-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sparcv9-openbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sparcv9-solaris/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── sw_64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-cygwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-darwin/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-dragonflybsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-freebsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-freebsd12/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-haiku/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-linux/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-msys/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-netbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-openbsd/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   ├── x86_64-solaris/
│   │               │   │   │   │   │   │   └── types.conf
│   │               │   │   │   │   │   └── x86_64-windows/
│   │               │   │   │   │   │       └── types.conf
│   │               │   │   │   │   ├── platform.rb
│   │               │   │   │   │   ├── pointer.rb
│   │               │   │   │   │   ├── struct.rb
│   │               │   │   │   │   ├── struct_by_reference.rb
│   │               │   │   │   │   ├── struct_layout.rb
│   │               │   │   │   │   ├── struct_layout_builder.rb
│   │               │   │   │   │   ├── tools/
│   │               │   │   │   │   │   ├── const_generator.rb
│   │               │   │   │   │   │   ├── generator.rb
│   │               │   │   │   │   │   ├── generator_task.rb
│   │               │   │   │   │   │   └── struct_generator.rb
│   │               │   │   │   │   ├── types.rb
│   │               │   │   │   │   ├── union.rb
│   │               │   │   │   │   ├── variadic.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   ├── ffi.rb
│   │               │   │   │   └── ffi_c.bundle
│   │               │   │   ├── samples/
│   │               │   │   │   ├── getlogin.rb
│   │               │   │   │   ├── getpid.rb
│   │               │   │   │   ├── gettimeofday.rb
│   │               │   │   │   ├── hello.rb
│   │               │   │   │   ├── hello_ractor.rb
│   │               │   │   │   ├── inotify.rb
│   │               │   │   │   ├── pty.rb
│   │               │   │   │   ├── qsort.rb
│   │               │   │   │   └── qsort_ractor.rb
│   │               │   │   └── sig/
│   │               │   │       ├── ffi/
│   │               │   │       │   ├── abstract_memory.rbs
│   │               │   │       │   ├── auto_pointer.rbs
│   │               │   │       │   ├── buffer.rbs
│   │               │   │       │   ├── data_converter.rbs
│   │               │   │       │   ├── dynamic_library.rbs
│   │               │   │       │   ├── enum.rbs
│   │               │   │       │   ├── errno.rbs
│   │               │   │       │   ├── function.rbs
│   │               │   │       │   ├── library.rbs
│   │               │   │       │   ├── native_type.rbs
│   │               │   │       │   ├── platform.rbs
│   │               │   │       │   ├── pointer.rbs
│   │               │   │       │   ├── struct.rbs
│   │               │   │       │   ├── struct_by_reference.rbs
│   │               │   │       │   ├── struct_by_value.rbs
│   │               │   │       │   ├── struct_layout.rbs
│   │               │   │       │   ├── struct_layout_builder.rbs
│   │               │   │       │   └── type.rbs
│   │               │   │       └── ffi.rbs
│   │               │   ├── forwardable-extended-2.6.0/
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE
│   │               │   │   ├── Rakefile
│   │               │   │   └── lib/
│   │               │   │       └── forwardable/
│   │               │   │           ├── extended/
│   │               │   │           │   └── version.rb
│   │               │   │           └── extended.rb
│   │               │   ├── google-protobuf-3.23.4-arm64-darwin/
│   │               │   │   ├── ext/
│   │               │   │   │   └── google/
│   │               │   │   │       └── protobuf_c/
│   │               │   │   │           ├── convert.c
│   │               │   │   │           ├── convert.h
│   │               │   │   │           ├── defs.c
│   │               │   │   │           ├── defs.h
│   │               │   │   │           ├── extconf.rb
│   │               │   │   │           ├── map.c
│   │               │   │   │           ├── map.h
│   │               │   │   │           ├── message.c
│   │               │   │   │           ├── message.h
│   │               │   │   │           ├── protobuf.c
│   │               │   │   │           ├── protobuf.h
│   │               │   │   │           ├── repeated_field.c
│   │               │   │   │           ├── repeated_field.h
│   │               │   │   │           ├── ruby-upb.c
│   │               │   │   │           ├── ruby-upb.h
│   │               │   │   │           ├── third_party/
│   │               │   │   │           │   └── utf8_range/
│   │               │   │   │           │       ├── LICENSE
│   │               │   │   │           │       ├── naive.c
│   │               │   │   │           │       ├── range2-neon.c
│   │               │   │   │           │       ├── range2-sse.c
│   │               │   │   │           │       └── utf8_range.h
│   │               │   │   │           └── wrap_memcpy.c
│   │               │   │   └── lib/
│   │               │   │       └── google/
│   │               │   │           ├── 2.6/
│   │               │   │           │   └── protobuf_c.bundle
│   │               │   │           ├── 2.7/
│   │               │   │           │   └── protobuf_c.bundle
│   │               │   │           ├── 3.0/
│   │               │   │           │   └── protobuf_c.bundle
│   │               │   │           ├── 3.1/
│   │               │   │           │   └── protobuf_c.bundle
│   │               │   │           ├── 3.2/
│   │               │   │           │   └── protobuf_c.bundle
│   │               │   │           ├── protobuf/
│   │               │   │           │   ├── any_pb.rb
│   │               │   │           │   ├── api_pb.rb
│   │               │   │           │   ├── descriptor_dsl.rb
│   │               │   │           │   ├── descriptor_pb.rb
│   │               │   │           │   ├── duration_pb.rb
│   │               │   │           │   ├── empty_pb.rb
│   │               │   │           │   ├── field_mask_pb.rb
│   │               │   │           │   ├── message_exts.rb
│   │               │   │           │   ├── plugin_pb.rb
│   │               │   │           │   ├── repeated_field.rb
│   │               │   │           │   ├── source_context_pb.rb
│   │               │   │           │   ├── struct_pb.rb
│   │               │   │           │   ├── timestamp_pb.rb
│   │               │   │           │   ├── type_pb.rb
│   │               │   │           │   ├── well_known_types.rb
│   │               │   │           │   └── wrappers_pb.rb
│   │               │   │           └── protobuf.rb
│   │               │   ├── http_parser.rb-0.8.1/
│   │               │   │   ├── .github/
│   │               │   │   │   └── workflows/
│   │               │   │   │       ├── linux.yml
│   │               │   │   │       └── windows.yml
│   │               │   │   ├── .gitignore
│   │               │   │   ├── .gitmodules
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE-MIT
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── bench/
│   │               │   │   │   ├── standalone.rb
│   │               │   │   │   └── thin.rb
│   │               │   │   ├── ext/
│   │               │   │   │   └── ruby_http_parser/
│   │               │   │   │       ├── .gitignore
│   │               │   │   │       ├── .sitearchdir.time
│   │               │   │   │       ├── Makefile
│   │               │   │   │       ├── RubyHttpParserService.java
│   │               │   │   │       ├── ext_help.h
│   │               │   │   │       ├── extconf.rb
│   │               │   │   │       ├── org/
│   │               │   │   │       │   └── ruby_http_parser/
│   │               │   │   │       │       └── RubyHttpParser.java
│   │               │   │   │       ├── ruby_http_parser.bundle
│   │               │   │   │       ├── ruby_http_parser.c
│   │               │   │   │       ├── ruby_http_parser.o
│   │               │   │   │       ├── ryah_http_parser.c
│   │               │   │   │       ├── ryah_http_parser.h
│   │               │   │   │       ├── ryah_http_parser.o
│   │               │   │   │       └── vendor/
│   │               │   │   │           ├── .gitkeep
│   │               │   │   │           ├── http-parser/
│   │               │   │   │           │   ├── AUTHORS
│   │               │   │   │           │   ├── LICENSE-MIT
│   │               │   │   │           │   ├── Makefile
│   │               │   │   │           │   ├── README.md
│   │               │   │   │           │   ├── bench.c
│   │               │   │   │           │   ├── contrib/
│   │               │   │   │           │   │   ├── parsertrace.c
│   │               │   │   │           │   │   └── url_parser.c
│   │               │   │   │           │   ├── http_parser.c
│   │               │   │   │           │   ├── http_parser.gyp
│   │               │   │   │           │   ├── http_parser.h
│   │               │   │   │           │   └── test.c
│   │               │   │   │           └── http-parser-java/
│   │               │   │   │               ├── AUTHORS
│   │               │   │   │               ├── LICENSE-MIT
│   │               │   │   │               ├── Makefile
│   │               │   │   │               ├── README.md
│   │               │   │   │               ├── TODO
│   │               │   │   │               ├── build.xml
│   │               │   │   │               ├── ext/
│   │               │   │   │               │   └── primitives.jar
│   │               │   │   │               ├── http_parser.c
│   │               │   │   │               ├── http_parser.gyp
│   │               │   │   │               ├── http_parser.h
│   │               │   │   │               ├── src/
│   │               │   │   │               │   ├── Http-parser.java.iml
│   │               │   │   │               │   ├── impl/
│   │               │   │   │               │   │   └── http_parser/
│   │               │   │   │               │   │       ├── FieldData.java
│   │               │   │   │               │   │       ├── HTTPCallback.java
│   │               │   │   │               │   │       ├── HTTPDataCallback.java
│   │               │   │   │               │   │       ├── HTTPErrorCallback.java
│   │               │   │   │               │   │       ├── HTTPException.java
│   │               │   │   │               │   │       ├── HTTPMethod.java
│   │               │   │   │               │   │       ├── HTTPParser.java
│   │               │   │   │               │   │       ├── HTTPParserUrl.java
│   │               │   │   │               │   │       ├── ParserSettings.java
│   │               │   │   │               │   │       ├── ParserType.java
│   │               │   │   │               │   │       ├── Util.java
│   │               │   │   │               │   │       └── lolevel/
│   │               │   │   │               │   │           ├── HTTPCallback.java
│   │               │   │   │               │   │           ├── HTTPDataCallback.java
│   │               │   │   │               │   │           ├── HTTPErrorCallback.java
│   │               │   │   │               │   │           ├── HTTPParser.java
│   │               │   │   │               │   │           └── ParserSettings.java
│   │               │   │   │               │   └── test/
│   │               │   │   │               │       └── http_parser/
│   │               │   │   │               │           └── lolevel/
│   │               │   │   │               │               ├── Message.java
│   │               │   │   │               │               ├── ParseUrl.java
│   │               │   │   │               │               ├── Requests.java
│   │               │   │   │               │               ├── Responses.java
│   │               │   │   │               │               ├── Test.java
│   │               │   │   │               │               ├── TestHeaderOverflowError.java
│   │               │   │   │               │               ├── TestLoaderNG.java
│   │               │   │   │               │               ├── TestNoOverflowLongBody.java
│   │               │   │   │               │               ├── UnitTest.java
│   │               │   │   │               │               ├── Upgrade.java
│   │               │   │   │               │               ├── Url.java
│   │               │   │   │               │               ├── Util.java
│   │               │   │   │               │               └── WrongContentLength.java
│   │               │   │   │               ├── test.c
│   │               │   │   │               ├── tests.dumped
│   │               │   │   │               ├── tests.utf8
│   │               │   │   │               └── tools/
│   │               │   │   │                   ├── byte_constants.rb
│   │               │   │   │                   ├── const_char.rb
│   │               │   │   │                   ├── lowcase.rb
│   │               │   │   │                   └── parse_tests.rb
│   │               │   │   ├── http_parser.rb.gemspec
│   │               │   │   ├── lib/
│   │               │   │   │   ├── http/
│   │               │   │   │   │   └── parser.rb
│   │               │   │   │   ├── http_parser.rb
│   │               │   │   │   └── ruby_http_parser.bundle
│   │               │   │   └── tasks/
│   │               │   │       ├── compile.rake
│   │               │   │       ├── fixtures.rake
│   │               │   │       ├── spec.rake
│   │               │   │       └── submodules.rake
│   │               │   ├── i18n-1.14.8/
│   │               │   │   ├── MIT-LICENSE
│   │               │   │   ├── README.md
│   │               │   │   └── lib/
│   │               │   │       ├── i18n/
│   │               │   │       │   ├── backend/
│   │               │   │       │   │   ├── base.rb
│   │               │   │       │   │   ├── cache.rb
│   │               │   │       │   │   ├── cache_file.rb
│   │               │   │       │   │   ├── cascade.rb
│   │               │   │       │   │   ├── chain.rb
│   │               │   │       │   │   ├── fallbacks.rb
│   │               │   │       │   │   ├── flatten.rb
│   │               │   │       │   │   ├── gettext.rb
│   │               │   │       │   │   ├── interpolation_compiler.rb
│   │               │   │       │   │   ├── key_value.rb
│   │               │   │       │   │   ├── lazy_loadable.rb
│   │               │   │       │   │   ├── memoize.rb
│   │               │   │       │   │   ├── metadata.rb
│   │               │   │       │   │   ├── pluralization.rb
│   │               │   │       │   │   ├── simple.rb
│   │               │   │       │   │   └── transliterator.rb
│   │               │   │       │   ├── backend.rb
│   │               │   │       │   ├── config.rb
│   │               │   │       │   ├── exceptions.rb
│   │               │   │       │   ├── gettext/
│   │               │   │       │   │   ├── helpers.rb
│   │               │   │       │   │   └── po_parser.rb
│   │               │   │       │   ├── gettext.rb
│   │               │   │       │   ├── interpolate/
│   │               │   │       │   │   └── ruby.rb
│   │               │   │       │   ├── locale/
│   │               │   │       │   │   ├── fallbacks.rb
│   │               │   │       │   │   ├── tag/
│   │               │   │       │   │   │   ├── parents.rb
│   │               │   │       │   │   │   ├── rfc4646.rb
│   │               │   │       │   │   │   └── simple.rb
│   │               │   │       │   │   └── tag.rb
│   │               │   │       │   ├── locale.rb
│   │               │   │       │   ├── middleware.rb
│   │               │   │       │   ├── tests/
│   │               │   │       │   │   ├── basics.rb
│   │               │   │       │   │   ├── defaults.rb
│   │               │   │       │   │   ├── interpolation.rb
│   │               │   │       │   │   ├── link.rb
│   │               │   │       │   │   ├── localization/
│   │               │   │       │   │   │   ├── date.rb
│   │               │   │       │   │   │   ├── date_time.rb
│   │               │   │       │   │   │   ├── procs.rb
│   │               │   │       │   │   │   └── time.rb
│   │               │   │       │   │   ├── localization.rb
│   │               │   │       │   │   ├── lookup.rb
│   │               │   │       │   │   ├── pluralization.rb
│   │               │   │       │   │   └── procs.rb
│   │               │   │       │   ├── tests.rb
│   │               │   │       │   ├── utils.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── i18n.rb
│   │               │   ├── jekyll-4.3.4/
│   │               │   │   ├── .rubocop.yml
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.markdown
│   │               │   │   ├── exe/
│   │               │   │   │   └── jekyll
│   │               │   │   ├── lib/
│   │               │   │   │   ├── blank_template/
│   │               │   │   │   │   ├── _config.yml
│   │               │   │   │   │   ├── _layouts/
│   │               │   │   │   │   │   └── default.html
│   │               │   │   │   │   ├── _sass/
│   │               │   │   │   │   │   └── base.scss
│   │               │   │   │   │   ├── assets/
│   │               │   │   │   │   │   └── css/
│   │               │   │   │   │   │       └── main.scss
│   │               │   │   │   │   └── index.md
│   │               │   │   │   ├── jekyll/
│   │               │   │   │   │   ├── cache.rb
│   │               │   │   │   │   ├── cleaner.rb
│   │               │   │   │   │   ├── collection.rb
│   │               │   │   │   │   ├── command.rb
│   │               │   │   │   │   ├── commands/
│   │               │   │   │   │   │   ├── build.rb
│   │               │   │   │   │   │   ├── clean.rb
│   │               │   │   │   │   │   ├── doctor.rb
│   │               │   │   │   │   │   ├── help.rb
│   │               │   │   │   │   │   ├── new.rb
│   │               │   │   │   │   │   ├── new_theme.rb
│   │               │   │   │   │   │   ├── serve/
│   │               │   │   │   │   │   │   ├── live_reload_reactor.rb
│   │               │   │   │   │   │   │   ├── livereload_assets/
│   │               │   │   │   │   │   │   │   └── livereload.js
│   │               │   │   │   │   │   │   ├── mime_types_charset.json
│   │               │   │   │   │   │   │   ├── servlet.rb
│   │               │   │   │   │   │   │   └── websockets.rb
│   │               │   │   │   │   │   └── serve.rb
│   │               │   │   │   │   ├── configuration.rb
│   │               │   │   │   │   ├── converter.rb
│   │               │   │   │   │   ├── converters/
│   │               │   │   │   │   │   ├── identity.rb
│   │               │   │   │   │   │   ├── markdown/
│   │               │   │   │   │   │   │   └── kramdown_parser.rb
│   │               │   │   │   │   │   ├── markdown.rb
│   │               │   │   │   │   │   └── smartypants.rb
│   │               │   │   │   │   ├── convertible.rb
│   │               │   │   │   │   ├── deprecator.rb
│   │               │   │   │   │   ├── document.rb
│   │               │   │   │   │   ├── drops/
│   │               │   │   │   │   │   ├── collection_drop.rb
│   │               │   │   │   │   │   ├── document_drop.rb
│   │               │   │   │   │   │   ├── drop.rb
│   │               │   │   │   │   │   ├── excerpt_drop.rb
│   │               │   │   │   │   │   ├── jekyll_drop.rb
│   │               │   │   │   │   │   ├── site_drop.rb
│   │               │   │   │   │   │   ├── static_file_drop.rb
│   │               │   │   │   │   │   ├── theme_drop.rb
│   │               │   │   │   │   │   ├── unified_payload_drop.rb
│   │               │   │   │   │   │   └── url_drop.rb
│   │               │   │   │   │   ├── entry_filter.rb
│   │               │   │   │   │   ├── errors.rb
│   │               │   │   │   │   ├── excerpt.rb
│   │               │   │   │   │   ├── external.rb
│   │               │   │   │   │   ├── filters/
│   │               │   │   │   │   │   ├── date_filters.rb
│   │               │   │   │   │   │   ├── grouping_filters.rb
│   │               │   │   │   │   │   └── url_filters.rb
│   │               │   │   │   │   ├── filters.rb
│   │               │   │   │   │   ├── frontmatter_defaults.rb
│   │               │   │   │   │   ├── generator.rb
│   │               │   │   │   │   ├── hooks.rb
│   │               │   │   │   │   ├── inclusion.rb
│   │               │   │   │   │   ├── layout.rb
│   │               │   │   │   │   ├── liquid_extensions.rb
│   │               │   │   │   │   ├── liquid_renderer/
│   │               │   │   │   │   │   ├── file.rb
│   │               │   │   │   │   │   └── table.rb
│   │               │   │   │   │   ├── liquid_renderer.rb
│   │               │   │   │   │   ├── log_adapter.rb
│   │               │   │   │   │   ├── mime.types
│   │               │   │   │   │   ├── page.rb
│   │               │   │   │   │   ├── page_excerpt.rb
│   │               │   │   │   │   ├── page_without_a_file.rb
│   │               │   │   │   │   ├── path_manager.rb
│   │               │   │   │   │   ├── plugin.rb
│   │               │   │   │   │   ├── plugin_manager.rb
│   │               │   │   │   │   ├── profiler.rb
│   │               │   │   │   │   ├── publisher.rb
│   │               │   │   │   │   ├── reader.rb
│   │               │   │   │   │   ├── readers/
│   │               │   │   │   │   │   ├── collection_reader.rb
│   │               │   │   │   │   │   ├── data_reader.rb
│   │               │   │   │   │   │   ├── layout_reader.rb
│   │               │   │   │   │   │   ├── page_reader.rb
│   │               │   │   │   │   │   ├── post_reader.rb
│   │               │   │   │   │   │   ├── static_file_reader.rb
│   │               │   │   │   │   │   └── theme_assets_reader.rb
│   │               │   │   │   │   ├── regenerator.rb
│   │               │   │   │   │   ├── related_posts.rb
│   │               │   │   │   │   ├── renderer.rb
│   │               │   │   │   │   ├── site.rb
│   │               │   │   │   │   ├── static_file.rb
│   │               │   │   │   │   ├── stevenson.rb
│   │               │   │   │   │   ├── tags/
│   │               │   │   │   │   │   ├── highlight.rb
│   │               │   │   │   │   │   ├── include.rb
│   │               │   │   │   │   │   ├── link.rb
│   │               │   │   │   │   │   └── post_url.rb
│   │               │   │   │   │   ├── theme.rb
│   │               │   │   │   │   ├── theme_builder.rb
│   │               │   │   │   │   ├── url.rb
│   │               │   │   │   │   ├── utils/
│   │               │   │   │   │   │   ├── ansi.rb
│   │               │   │   │   │   │   ├── exec.rb
│   │               │   │   │   │   │   ├── internet.rb
│   │               │   │   │   │   │   ├── platforms.rb
│   │               │   │   │   │   │   ├── thread_event.rb
│   │               │   │   │   │   │   └── win_tz.rb
│   │               │   │   │   │   ├── utils.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   ├── jekyll.rb
│   │               │   │   │   ├── site_template/
│   │               │   │   │   │   ├── .gitignore
│   │               │   │   │   │   ├── 404.html
│   │               │   │   │   │   ├── _config.yml
│   │               │   │   │   │   ├── _posts/
│   │               │   │   │   │   │   └── 0000-00-00-welcome-to-jekyll.markdown.erb
│   │               │   │   │   │   ├── about.markdown
│   │               │   │   │   │   └── index.markdown
│   │               │   │   │   └── theme_template/
│   │               │   │   │       ├── CODE_OF_CONDUCT.md.erb
│   │               │   │   │       ├── Gemfile
│   │               │   │   │       ├── LICENSE.txt.erb
│   │               │   │   │       ├── README.md.erb
│   │               │   │   │       ├── _layouts/
│   │               │   │   │       │   ├── default.html
│   │               │   │   │       │   ├── page.html
│   │               │   │   │       │   └── post.html
│   │               │   │   │       ├── example/
│   │               │   │   │       │   ├── _config.yml.erb
│   │               │   │   │       │   ├── _post.md
│   │               │   │   │       │   ├── index.html
│   │               │   │   │       │   └── style.scss
│   │               │   │   │       ├── gitignore.erb
│   │               │   │   │       └── theme.gemspec.erb
│   │               │   │   └── rubocop/
│   │               │   │       ├── jekyll/
│   │               │   │       │   ├── assert_equal_literal_actual.rb
│   │               │   │       │   ├── no_p_allowed.rb
│   │               │   │       │   └── no_puts_allowed.rb
│   │               │   │       └── jekyll.rb
│   │               │   ├── jekyll-sass-converter-3.0.0/
│   │               │   │   └── lib/
│   │               │   │       ├── jekyll/
│   │               │   │       │   ├── converters/
│   │               │   │       │   │   ├── sass.rb
│   │               │   │       │   │   └── scss.rb
│   │               │   │       │   └── source_map_page.rb
│   │               │   │       ├── jekyll-sass-converter/
│   │               │   │       │   └── version.rb
│   │               │   │       └── jekyll-sass-converter.rb
│   │               │   ├── jekyll-seo-tag-2.8.0/
│   │               │   │   ├── .github/
│   │               │   │   │   └── workflows/
│   │               │   │   │       ├── ci.yml
│   │               │   │   │       ├── release.yml
│   │               │   │   │       ├── scripts/
│   │               │   │   │       │   ├── memprof
│   │               │   │   │       │   └── memprof.rb
│   │               │   │   │       └── third-party.yml
│   │               │   │   ├── .gitignore
│   │               │   │   ├── .rspec
│   │               │   │   ├── .rubocop.yml
│   │               │   │   ├── .rubocop_todo.yml
│   │               │   │   ├── Gemfile
│   │               │   │   ├── History.markdown
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── docs/
│   │               │   │   │   ├── README.md
│   │               │   │   │   ├── _config.yml
│   │               │   │   │   ├── _layouts/
│   │               │   │   │   │   └── default.html
│   │               │   │   │   ├── advanced-usage.md
│   │               │   │   │   ├── installation.md
│   │               │   │   │   └── usage.md
│   │               │   │   ├── jekyll-seo-tag.gemspec
│   │               │   │   ├── lib/
│   │               │   │   │   ├── jekyll-seo-tag/
│   │               │   │   │   │   ├── author_drop.rb
│   │               │   │   │   │   ├── drop.rb
│   │               │   │   │   │   ├── filters.rb
│   │               │   │   │   │   ├── image_drop.rb
│   │               │   │   │   │   ├── json_ld.rb
│   │               │   │   │   │   ├── json_ld_drop.rb
│   │               │   │   │   │   ├── url_helper.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   ├── jekyll-seo-tag.rb
│   │               │   │   │   └── template.html
│   │               │   │   └── script/
│   │               │   │       ├── bootstrap
│   │               │   │       ├── cibuild
│   │               │   │       ├── release
│   │               │   │       └── site
│   │               │   ├── jekyll-watch-2.2.1/
│   │               │   │   └── lib/
│   │               │   │       ├── jekyll/
│   │               │   │       │   ├── commands/
│   │               │   │       │   │   └── watch.rb
│   │               │   │       │   └── watcher.rb
│   │               │   │       ├── jekyll-watch/
│   │               │   │       │   └── version.rb
│   │               │   │       └── jekyll-watch.rb
│   │               │   ├── kramdown-2.5.2/
│   │               │   │   ├── AUTHORS
│   │               │   │   ├── CONTRIBUTERS
│   │               │   │   ├── COPYING
│   │               │   │   ├── README.md
│   │               │   │   ├── VERSION
│   │               │   │   ├── bin/
│   │               │   │   │   └── kramdown
│   │               │   │   ├── data/
│   │               │   │   │   └── kramdown/
│   │               │   │   │       ├── document.html
│   │               │   │   │       └── document.latex
│   │               │   │   ├── lib/
│   │               │   │   │   ├── kramdown/
│   │               │   │   │   │   ├── converter/
│   │               │   │   │   │   │   ├── base.rb
│   │               │   │   │   │   │   ├── hash_ast.rb
│   │               │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   ├── kramdown.rb
│   │               │   │   │   │   │   ├── latex.rb
│   │               │   │   │   │   │   ├── man.rb
│   │               │   │   │   │   │   ├── math_engine/
│   │               │   │   │   │   │   │   └── mathjax.rb
│   │               │   │   │   │   │   ├── remove_html_tags.rb
│   │               │   │   │   │   │   ├── syntax_highlighter/
│   │               │   │   │   │   │   │   ├── minted.rb
│   │               │   │   │   │   │   │   └── rouge.rb
│   │               │   │   │   │   │   ├── syntax_highlighter.rb
│   │               │   │   │   │   │   └── toc.rb
│   │               │   │   │   │   ├── converter.rb
│   │               │   │   │   │   ├── document.rb
│   │               │   │   │   │   ├── element.rb
│   │               │   │   │   │   ├── error.rb
│   │               │   │   │   │   ├── options.rb
│   │               │   │   │   │   ├── parser/
│   │               │   │   │   │   │   ├── base.rb
│   │               │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   ├── kramdown/
│   │               │   │   │   │   │   │   ├── abbreviation.rb
│   │               │   │   │   │   │   │   ├── autolink.rb
│   │               │   │   │   │   │   │   ├── blank_line.rb
│   │               │   │   │   │   │   │   ├── block_boundary.rb
│   │               │   │   │   │   │   │   ├── blockquote.rb
│   │               │   │   │   │   │   │   ├── codeblock.rb
│   │               │   │   │   │   │   │   ├── codespan.rb
│   │               │   │   │   │   │   │   ├── emphasis.rb
│   │               │   │   │   │   │   │   ├── eob.rb
│   │               │   │   │   │   │   │   ├── escaped_chars.rb
│   │               │   │   │   │   │   │   ├── extensions.rb
│   │               │   │   │   │   │   │   ├── footnote.rb
│   │               │   │   │   │   │   │   ├── header.rb
│   │               │   │   │   │   │   │   ├── horizontal_rule.rb
│   │               │   │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   │   ├── html_entity.rb
│   │               │   │   │   │   │   │   ├── line_break.rb
│   │               │   │   │   │   │   │   ├── link.rb
│   │               │   │   │   │   │   │   ├── list.rb
│   │               │   │   │   │   │   │   ├── math.rb
│   │               │   │   │   │   │   │   ├── paragraph.rb
│   │               │   │   │   │   │   │   ├── smart_quotes.rb
│   │               │   │   │   │   │   │   ├── table.rb
│   │               │   │   │   │   │   │   └── typographic_symbol.rb
│   │               │   │   │   │   │   ├── kramdown.rb
│   │               │   │   │   │   │   └── markdown.rb
│   │               │   │   │   │   ├── parser.rb
│   │               │   │   │   │   ├── utils/
│   │               │   │   │   │   │   ├── configurable.rb
│   │               │   │   │   │   │   ├── entities.rb
│   │               │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   ├── lru_cache.rb
│   │               │   │   │   │   │   ├── string_scanner.rb
│   │               │   │   │   │   │   └── unidecoder.rb
│   │               │   │   │   │   ├── utils.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── kramdown.rb
│   │               │   │   ├── man/
│   │               │   │   │   └── man1/
│   │               │   │   │       └── kramdown.1
│   │               │   │   └── test/
│   │               │   │       ├── run_tests.rb
│   │               │   │       ├── test_files.rb
│   │               │   │       ├── test_location.rb
│   │               │   │       ├── test_string_scanner_kramdown.rb
│   │               │   │       └── testcases/
│   │               │   │           ├── block/
│   │               │   │           │   ├── 01_blank_line/
│   │               │   │           │   │   ├── spaces.html
│   │               │   │           │   │   ├── spaces.text
│   │               │   │           │   │   ├── tabs.html
│   │               │   │           │   │   └── tabs.text
│   │               │   │           │   ├── 02_eob/
│   │               │   │           │   │   ├── beginning.html
│   │               │   │           │   │   ├── beginning.text
│   │               │   │           │   │   ├── end.html
│   │               │   │           │   │   ├── end.text
│   │               │   │           │   │   ├── middle.html
│   │               │   │           │   │   └── middle.text
│   │               │   │           │   ├── 03_paragraph/
│   │               │   │           │   │   ├── indented.html
│   │               │   │           │   │   ├── indented.html.gfm
│   │               │   │           │   │   ├── indented.text
│   │               │   │           │   │   ├── line_break_last_line.html
│   │               │   │           │   │   ├── line_break_last_line.text
│   │               │   │           │   │   ├── no_newline_at_end.html
│   │               │   │           │   │   ├── no_newline_at_end.text
│   │               │   │           │   │   ├── one_para.html
│   │               │   │           │   │   ├── one_para.text
│   │               │   │           │   │   ├── standalone_image.html
│   │               │   │           │   │   ├── standalone_image.text
│   │               │   │           │   │   ├── to_kramdown.kramdown
│   │               │   │           │   │   ├── to_kramdown.text
│   │               │   │           │   │   ├── two_para.html
│   │               │   │           │   │   ├── two_para.text
│   │               │   │           │   │   ├── with_html_to_native.html
│   │               │   │           │   │   ├── with_html_to_native.options
│   │               │   │           │   │   └── with_html_to_native.text
│   │               │   │           │   ├── 04_header/
│   │               │   │           │   │   ├── atx_header.html
│   │               │   │           │   │   ├── atx_header.text
│   │               │   │           │   │   ├── atx_header_no_newline_at_end.html
│   │               │   │           │   │   ├── atx_header_no_newline_at_end.text
│   │               │   │           │   │   ├── header_type_offset.html
│   │               │   │           │   │   ├── header_type_offset.kramdown
│   │               │   │           │   │   ├── header_type_offset.latex
│   │               │   │           │   │   ├── header_type_offset.options
│   │               │   │           │   │   ├── header_type_offset.text
│   │               │   │           │   │   ├── setext_header.html
│   │               │   │           │   │   ├── setext_header.text
│   │               │   │           │   │   ├── setext_header_no_newline_at_end.html
│   │               │   │           │   │   ├── setext_header_no_newline_at_end.text
│   │               │   │           │   │   ├── with_auto_id_prefix.html
│   │               │   │           │   │   ├── with_auto_id_prefix.options
│   │               │   │           │   │   ├── with_auto_id_prefix.text
│   │               │   │           │   │   ├── with_auto_id_stripping.html
│   │               │   │           │   │   ├── with_auto_id_stripping.options
│   │               │   │           │   │   ├── with_auto_id_stripping.text
│   │               │   │           │   │   ├── with_auto_ids.html
│   │               │   │           │   │   ├── with_auto_ids.options
│   │               │   │           │   │   ├── with_auto_ids.text
│   │               │   │           │   │   ├── with_header_links.html
│   │               │   │           │   │   ├── with_header_links.options
│   │               │   │           │   │   ├── with_header_links.text
│   │               │   │           │   │   ├── with_line_break.html
│   │               │   │           │   │   └── with_line_break.text
│   │               │   │           │   ├── 05_blockquote/
│   │               │   │           │   │   ├── indented.html
│   │               │   │           │   │   ├── indented.text
│   │               │   │           │   │   ├── lazy.html
│   │               │   │           │   │   ├── lazy.text
│   │               │   │           │   │   ├── nested.html
│   │               │   │           │   │   ├── nested.text
│   │               │   │           │   │   ├── no_newline_at_end.html
│   │               │   │           │   │   ├── no_newline_at_end.text
│   │               │   │           │   │   ├── very_long_line.html
│   │               │   │           │   │   ├── very_long_line.text
│   │               │   │           │   │   ├── with_code_blocks.html
│   │               │   │           │   │   └── with_code_blocks.text
│   │               │   │           │   ├── 06_codeblock/
│   │               │   │           │   │   ├── disable-highlighting.html
│   │               │   │           │   │   ├── disable-highlighting.options
│   │               │   │           │   │   ├── disable-highlighting.text
│   │               │   │           │   │   ├── error.html
│   │               │   │           │   │   ├── error.text
│   │               │   │           │   │   ├── guess_lang_css_class.html
│   │               │   │           │   │   ├── guess_lang_css_class.options
│   │               │   │           │   │   ├── guess_lang_css_class.text
│   │               │   │           │   │   ├── highlighting-minted-with-opts.latex
│   │               │   │           │   │   ├── highlighting-minted-with-opts.options
│   │               │   │           │   │   ├── highlighting-minted-with-opts.text
│   │               │   │           │   │   ├── highlighting-minted.latex
│   │               │   │           │   │   ├── highlighting-minted.options
│   │               │   │           │   │   ├── highlighting-minted.text
│   │               │   │           │   │   ├── highlighting-opts.html
│   │               │   │           │   │   ├── highlighting-opts.options
│   │               │   │           │   │   ├── highlighting-opts.text
│   │               │   │           │   │   ├── highlighting.html
│   │               │   │           │   │   ├── highlighting.options
│   │               │   │           │   │   ├── highlighting.text
│   │               │   │           │   │   ├── issue_gh45.html
│   │               │   │           │   │   ├── issue_gh45.test
│   │               │   │           │   │   ├── lazy.html
│   │               │   │           │   │   ├── lazy.text
│   │               │   │           │   │   ├── no_newline_at_end.html
│   │               │   │           │   │   ├── no_newline_at_end.text
│   │               │   │           │   │   ├── no_newline_at_end_1.html
│   │               │   │           │   │   ├── no_newline_at_end_1.text
│   │               │   │           │   │   ├── normal.html
│   │               │   │           │   │   ├── normal.text
│   │               │   │           │   │   ├── rouge/
│   │               │   │           │   │   │   ├── disabled.html
│   │               │   │           │   │   │   ├── disabled.options
│   │               │   │           │   │   │   ├── disabled.text
│   │               │   │           │   │   │   ├── multiple.html
│   │               │   │           │   │   │   ├── multiple.options
│   │               │   │           │   │   │   ├── multiple.text
│   │               │   │           │   │   │   ├── simple.html
│   │               │   │           │   │   │   ├── simple.options
│   │               │   │           │   │   │   └── simple.text
│   │               │   │           │   │   ├── tilde_syntax.html
│   │               │   │           │   │   ├── tilde_syntax.text
│   │               │   │           │   │   ├── whitespace.html
│   │               │   │           │   │   ├── whitespace.text
│   │               │   │           │   │   ├── with_blank_line.html
│   │               │   │           │   │   ├── with_blank_line.text
│   │               │   │           │   │   ├── with_eob_marker.html
│   │               │   │           │   │   ├── with_eob_marker.text
│   │               │   │           │   │   ├── with_ial.html
│   │               │   │           │   │   ├── with_ial.text
│   │               │   │           │   │   ├── with_lang_in_fenced_block.html
│   │               │   │           │   │   ├── with_lang_in_fenced_block.options
│   │               │   │           │   │   ├── with_lang_in_fenced_block.text
│   │               │   │           │   │   ├── with_lang_in_fenced_block_any_char.html
│   │               │   │           │   │   ├── with_lang_in_fenced_block_any_char.options
│   │               │   │           │   │   ├── with_lang_in_fenced_block_any_char.text
│   │               │   │           │   │   ├── with_lang_in_fenced_block_name_with_dash.html
│   │               │   │           │   │   ├── with_lang_in_fenced_block_name_with_dash.options
│   │               │   │           │   │   └── with_lang_in_fenced_block_name_with_dash.text
│   │               │   │           │   ├── 07_horizontal_rule/
│   │               │   │           │   │   ├── error.html
│   │               │   │           │   │   ├── error.text
│   │               │   │           │   │   ├── normal.html
│   │               │   │           │   │   ├── normal.text
│   │               │   │           │   │   ├── sepspaces.html
│   │               │   │           │   │   ├── sepspaces.text
│   │               │   │           │   │   ├── septabs.html
│   │               │   │           │   │   └── septabs.text
│   │               │   │           │   ├── 08_list/
│   │               │   │           │   │   ├── brackets_in_item.latex
│   │               │   │           │   │   ├── brackets_in_item.text
│   │               │   │           │   │   ├── escaping.html
│   │               │   │           │   │   ├── escaping.text
│   │               │   │           │   │   ├── item_ial.html
│   │               │   │           │   │   ├── item_ial.text
│   │               │   │           │   │   ├── lazy.html
│   │               │   │           │   │   ├── lazy.text
│   │               │   │           │   │   ├── lazy_and_nested.html
│   │               │   │           │   │   ├── lazy_and_nested.text
│   │               │   │           │   │   ├── list_and_hr.html
│   │               │   │           │   │   ├── list_and_hr.text
│   │               │   │           │   │   ├── list_and_others.html
│   │               │   │           │   │   ├── list_and_others.text
│   │               │   │           │   │   ├── mixed.html
│   │               │   │           │   │   ├── mixed.text
│   │               │   │           │   │   ├── nested.html
│   │               │   │           │   │   ├── nested.text
│   │               │   │           │   │   ├── nested_compact.kramdown
│   │               │   │           │   │   ├── nested_compact.text
│   │               │   │           │   │   ├── other_first_element.html
│   │               │   │           │   │   ├── other_first_element.text
│   │               │   │           │   │   ├── simple_ol.html
│   │               │   │           │   │   ├── simple_ol.text
│   │               │   │           │   │   ├── simple_ul.html
│   │               │   │           │   │   ├── simple_ul.text
│   │               │   │           │   │   ├── single_item.html
│   │               │   │           │   │   ├── single_item.text
│   │               │   │           │   │   ├── special_cases.html
│   │               │   │           │   │   └── special_cases.text
│   │               │   │           │   ├── 09_html/
│   │               │   │           │   │   ├── cdata_section.html
│   │               │   │           │   │   ├── cdata_section.text
│   │               │   │           │   │   ├── comment.html
│   │               │   │           │   │   ├── comment.text
│   │               │   │           │   │   ├── content_model/
│   │               │   │           │   │   │   ├── deflists.html
│   │               │   │           │   │   │   ├── deflists.options
│   │               │   │           │   │   │   ├── deflists.text
│   │               │   │           │   │   │   ├── tables.html
│   │               │   │           │   │   │   ├── tables.options
│   │               │   │           │   │   │   └── tables.text
│   │               │   │           │   │   ├── html5_attributes.html
│   │               │   │           │   │   ├── html5_attributes.text
│   │               │   │           │   │   ├── html_after_block.html
│   │               │   │           │   │   ├── html_after_block.text
│   │               │   │           │   │   ├── html_and_codeblocks.html
│   │               │   │           │   │   ├── html_and_codeblocks.options
│   │               │   │           │   │   ├── html_and_codeblocks.text
│   │               │   │           │   │   ├── html_and_headers.html
│   │               │   │           │   │   ├── html_and_headers.text
│   │               │   │           │   │   ├── html_to_native/
│   │               │   │           │   │   │   ├── code.html
│   │               │   │           │   │   │   ├── code.text
│   │               │   │           │   │   │   ├── comment.html
│   │               │   │           │   │   │   ├── comment.text
│   │               │   │           │   │   │   ├── emphasis.html
│   │               │   │           │   │   │   ├── emphasis.text
│   │               │   │           │   │   │   ├── entity.html
│   │               │   │           │   │   │   ├── entity.text
│   │               │   │           │   │   │   ├── header.html
│   │               │   │           │   │   │   ├── header.options
│   │               │   │           │   │   │   ├── header.text
│   │               │   │           │   │   │   ├── list_dl.html
│   │               │   │           │   │   │   ├── list_dl.text
│   │               │   │           │   │   │   ├── list_ol.html
│   │               │   │           │   │   │   ├── list_ol.text
│   │               │   │           │   │   │   ├── list_ul.html
│   │               │   │           │   │   │   ├── list_ul.text
│   │               │   │           │   │   │   ├── options
│   │               │   │           │   │   │   ├── paragraph.html
│   │               │   │           │   │   │   ├── paragraph.text
│   │               │   │           │   │   │   ├── table_normal.html
│   │               │   │           │   │   │   ├── table_normal.text
│   │               │   │           │   │   │   ├── table_simple.html
│   │               │   │           │   │   │   ├── table_simple.text
│   │               │   │           │   │   │   ├── typography.html
│   │               │   │           │   │   │   └── typography.text
│   │               │   │           │   │   ├── invalid_html_1.html
│   │               │   │           │   │   ├── invalid_html_1.text
│   │               │   │           │   │   ├── invalid_html_2.html
│   │               │   │           │   │   ├── invalid_html_2.text
│   │               │   │           │   │   ├── markdown_attr.html
│   │               │   │           │   │   ├── markdown_attr.text
│   │               │   │           │   │   ├── not_parsed.html
│   │               │   │           │   │   ├── not_parsed.text
│   │               │   │           │   │   ├── parse_as_raw.html
│   │               │   │           │   │   ├── parse_as_raw.htmlinput
│   │               │   │           │   │   ├── parse_as_raw.options
│   │               │   │           │   │   ├── parse_as_raw.text
│   │               │   │           │   │   ├── parse_as_span.html
│   │               │   │           │   │   ├── parse_as_span.htmlinput
│   │               │   │           │   │   ├── parse_as_span.options
│   │               │   │           │   │   ├── parse_as_span.text
│   │               │   │           │   │   ├── parse_block_html.html
│   │               │   │           │   │   ├── parse_block_html.options
│   │               │   │           │   │   ├── parse_block_html.text
│   │               │   │           │   │   ├── processing_instruction.html
│   │               │   │           │   │   ├── processing_instruction.text
│   │               │   │           │   │   ├── simple.html
│   │               │   │           │   │   ├── simple.options
│   │               │   │           │   │   ├── simple.text
│   │               │   │           │   │   ├── standalone_image_in_div.htmlinput
│   │               │   │           │   │   ├── standalone_image_in_div.text
│   │               │   │           │   │   ├── table.kramdown
│   │               │   │           │   │   ├── table.text
│   │               │   │           │   │   ├── textarea.html
│   │               │   │           │   │   ├── textarea.text
│   │               │   │           │   │   ├── xml.html
│   │               │   │           │   │   └── xml.text
│   │               │   │           │   ├── 10_ald/
│   │               │   │           │   │   ├── simple.html
│   │               │   │           │   │   └── simple.text
│   │               │   │           │   ├── 11_ial/
│   │               │   │           │   │   ├── auto_id_and_ial.html
│   │               │   │           │   │   ├── auto_id_and_ial.options
│   │               │   │           │   │   ├── auto_id_and_ial.text
│   │               │   │           │   │   ├── nested.html
│   │               │   │           │   │   ├── nested.text
│   │               │   │           │   │   ├── simple.html
│   │               │   │           │   │   └── simple.text
│   │               │   │           │   ├── 12_extension/
│   │               │   │           │   │   ├── comment.html
│   │               │   │           │   │   ├── comment.text
│   │               │   │           │   │   ├── ignored.html
│   │               │   │           │   │   ├── ignored.text
│   │               │   │           │   │   ├── nomarkdown.html
│   │               │   │           │   │   ├── nomarkdown.kramdown
│   │               │   │           │   │   ├── nomarkdown.latex
│   │               │   │           │   │   ├── nomarkdown.text
│   │               │   │           │   │   ├── options.html
│   │               │   │           │   │   ├── options.text
│   │               │   │           │   │   ├── options2.html
│   │               │   │           │   │   ├── options2.text
│   │               │   │           │   │   ├── options3.html
│   │               │   │           │   │   └── options3.text
│   │               │   │           │   ├── 13_definition_list/
│   │               │   │           │   │   ├── auto_ids.html
│   │               │   │           │   │   ├── auto_ids.text
│   │               │   │           │   │   ├── definition_at_beginning.html
│   │               │   │           │   │   ├── definition_at_beginning.text
│   │               │   │           │   │   ├── deflist_ial.html
│   │               │   │           │   │   ├── deflist_ial.text
│   │               │   │           │   │   ├── item_ial.html
│   │               │   │           │   │   ├── item_ial.text
│   │               │   │           │   │   ├── multiple_terms.html
│   │               │   │           │   │   ├── multiple_terms.text
│   │               │   │           │   │   ├── no_def_list.html
│   │               │   │           │   │   ├── no_def_list.text
│   │               │   │           │   │   ├── para_wrapping.html
│   │               │   │           │   │   ├── para_wrapping.text
│   │               │   │           │   │   ├── separated_by_eob.html
│   │               │   │           │   │   ├── separated_by_eob.text
│   │               │   │           │   │   ├── simple.html
│   │               │   │           │   │   ├── simple.text
│   │               │   │           │   │   ├── styled_terms.html
│   │               │   │           │   │   ├── styled_terms.text
│   │               │   │           │   │   ├── too_much_space.html
│   │               │   │           │   │   ├── too_much_space.text
│   │               │   │           │   │   ├── with_blocks.html
│   │               │   │           │   │   └── with_blocks.text
│   │               │   │           │   ├── 14_table/
│   │               │   │           │   │   ├── empty_tag_in_cell.html
│   │               │   │           │   │   ├── empty_tag_in_cell.options
│   │               │   │           │   │   ├── empty_tag_in_cell.text
│   │               │   │           │   │   ├── errors.html
│   │               │   │           │   │   ├── errors.text
│   │               │   │           │   │   ├── escaping.html
│   │               │   │           │   │   ├── escaping.text
│   │               │   │           │   │   ├── footer.html
│   │               │   │           │   │   ├── footer.text
│   │               │   │           │   │   ├── header.html
│   │               │   │           │   │   ├── header.text
│   │               │   │           │   │   ├── no_table.html
│   │               │   │           │   │   ├── no_table.text
│   │               │   │           │   │   ├── simple.html
│   │               │   │           │   │   ├── simple.text
│   │               │   │           │   │   ├── table_with_footnote.html
│   │               │   │           │   │   ├── table_with_footnote.latex
│   │               │   │           │   │   └── table_with_footnote.text
│   │               │   │           │   ├── 15_math/
│   │               │   │           │   │   ├── gh_128.html
│   │               │   │           │   │   ├── gh_128.text
│   │               │   │           │   │   ├── no_engine.html
│   │               │   │           │   │   ├── no_engine.options
│   │               │   │           │   │   ├── no_engine.text
│   │               │   │           │   │   ├── normal.html
│   │               │   │           │   │   └── normal.text
│   │               │   │           │   └── 16_toc/
│   │               │   │           │       ├── no_toc.html
│   │               │   │           │       ├── no_toc.text
│   │               │   │           │       ├── toc_exclude.html
│   │               │   │           │       ├── toc_exclude.options
│   │               │   │           │       ├── toc_exclude.text
│   │               │   │           │       ├── toc_levels.html
│   │               │   │           │       ├── toc_levels.options
│   │               │   │           │       ├── toc_levels.text
│   │               │   │           │       ├── toc_with_footnotes.html
│   │               │   │           │       ├── toc_with_footnotes.options
│   │               │   │           │       ├── toc_with_footnotes.text
│   │               │   │           │       ├── toc_with_links.html
│   │               │   │           │       ├── toc_with_links.options
│   │               │   │           │       └── toc_with_links.text
│   │               │   │           ├── cjk-line-break.html
│   │               │   │           ├── cjk-line-break.options
│   │               │   │           ├── cjk-line-break.text
│   │               │   │           ├── encoding.html
│   │               │   │           ├── encoding.text
│   │               │   │           ├── man/
│   │               │   │           │   ├── example.man
│   │               │   │           │   ├── example.text
│   │               │   │           │   ├── heading-name-dash-description.man
│   │               │   │           │   ├── heading-name-dash-description.text
│   │               │   │           │   ├── heading-name-description.man
│   │               │   │           │   ├── heading-name-description.text
│   │               │   │           │   ├── heading-name-section-description.man
│   │               │   │           │   ├── heading-name-section-description.text
│   │               │   │           │   ├── heading-name-section.man
│   │               │   │           │   ├── heading-name-section.text
│   │               │   │           │   ├── heading-name.man
│   │               │   │           │   ├── heading-name.text
│   │               │   │           │   ├── sections.man
│   │               │   │           │   ├── sections.text
│   │               │   │           │   ├── text-escaping.man
│   │               │   │           │   └── text-escaping.text
│   │               │   │           └── span/
│   │               │   │               ├── 01_link/
│   │               │   │               │   ├── empty.html
│   │               │   │               │   ├── empty.text
│   │               │   │               │   ├── empty_title.htmlinput
│   │               │   │               │   ├── empty_title.text
│   │               │   │               │   ├── image_in_a.html
│   │               │   │               │   ├── image_in_a.text
│   │               │   │               │   ├── imagelinks.html
│   │               │   │               │   ├── imagelinks.text
│   │               │   │               │   ├── inline.html
│   │               │   │               │   ├── inline.text
│   │               │   │               │   ├── latex_escaping.latex
│   │               │   │               │   ├── latex_escaping.text
│   │               │   │               │   ├── link_defs.html
│   │               │   │               │   ├── link_defs.text
│   │               │   │               │   ├── link_defs_with_ial.html
│   │               │   │               │   ├── link_defs_with_ial.text
│   │               │   │               │   ├── links_with_angle_brackets.html
│   │               │   │               │   ├── links_with_angle_brackets.text
│   │               │   │               │   ├── reference.html
│   │               │   │               │   ├── reference.options
│   │               │   │               │   └── reference.text
│   │               │   │               ├── 02_emphasis/
│   │               │   │               │   ├── empty.html
│   │               │   │               │   ├── empty.text
│   │               │   │               │   ├── errors.html
│   │               │   │               │   ├── errors.text
│   │               │   │               │   ├── nesting.html
│   │               │   │               │   ├── nesting.text
│   │               │   │               │   ├── normal.html
│   │               │   │               │   ├── normal.options
│   │               │   │               │   └── normal.text
│   │               │   │               ├── 03_codespan/
│   │               │   │               │   ├── empty.html
│   │               │   │               │   ├── empty.text
│   │               │   │               │   ├── errors.html
│   │               │   │               │   ├── errors.text
│   │               │   │               │   ├── highlighting-minted.latex
│   │               │   │               │   ├── highlighting-minted.options
│   │               │   │               │   ├── highlighting-minted.text
│   │               │   │               │   ├── highlighting.html
│   │               │   │               │   ├── highlighting.text
│   │               │   │               │   ├── normal-css-class.html
│   │               │   │               │   ├── normal-css-class.options
│   │               │   │               │   ├── normal-css-class.text
│   │               │   │               │   ├── normal.html
│   │               │   │               │   ├── normal.text
│   │               │   │               │   └── rouge/
│   │               │   │               │       ├── disabled.html
│   │               │   │               │       ├── disabled.options
│   │               │   │               │       ├── disabled.text
│   │               │   │               │       ├── simple.html
│   │               │   │               │       ├── simple.options
│   │               │   │               │       └── simple.text
│   │               │   │               ├── 04_footnote/
│   │               │   │               │   ├── backlink_inline.html
│   │               │   │               │   ├── backlink_inline.options
│   │               │   │               │   ├── backlink_inline.text
│   │               │   │               │   ├── backlink_text.html
│   │               │   │               │   ├── backlink_text.options
│   │               │   │               │   ├── backlink_text.text
│   │               │   │               │   ├── definitions.html
│   │               │   │               │   ├── definitions.latex
│   │               │   │               │   ├── definitions.text
│   │               │   │               │   ├── footnote_link_text.html
│   │               │   │               │   ├── footnote_link_text.options
│   │               │   │               │   ├── footnote_link_text.text
│   │               │   │               │   ├── footnote_nr.html
│   │               │   │               │   ├── footnote_nr.latex
│   │               │   │               │   ├── footnote_nr.options
│   │               │   │               │   ├── footnote_nr.text
│   │               │   │               │   ├── footnote_prefix.html
│   │               │   │               │   ├── footnote_prefix.options
│   │               │   │               │   ├── footnote_prefix.text
│   │               │   │               │   ├── inside_footnote.html
│   │               │   │               │   ├── inside_footnote.text
│   │               │   │               │   ├── markers.html
│   │               │   │               │   ├── markers.latex
│   │               │   │               │   ├── markers.options
│   │               │   │               │   ├── markers.text
│   │               │   │               │   ├── placement.html
│   │               │   │               │   ├── placement.options
│   │               │   │               │   ├── placement.text
│   │               │   │               │   ├── regexp_problem.html
│   │               │   │               │   ├── regexp_problem.options
│   │               │   │               │   ├── regexp_problem.text
│   │               │   │               │   ├── without_backlink.html
│   │               │   │               │   ├── without_backlink.options
│   │               │   │               │   └── without_backlink.text
│   │               │   │               ├── 05_html/
│   │               │   │               │   ├── across_lines.html
│   │               │   │               │   ├── across_lines.text
│   │               │   │               │   ├── button.html
│   │               │   │               │   ├── button.text
│   │               │   │               │   ├── invalid.html
│   │               │   │               │   ├── invalid.text
│   │               │   │               │   ├── link_with_mailto.html
│   │               │   │               │   ├── link_with_mailto.text
│   │               │   │               │   ├── mark_element.html
│   │               │   │               │   ├── mark_element.text
│   │               │   │               │   ├── markdown_attr.html
│   │               │   │               │   ├── markdown_attr.text
│   │               │   │               │   ├── normal.html
│   │               │   │               │   ├── normal.text
│   │               │   │               │   ├── raw_span_elements.html
│   │               │   │               │   ├── raw_span_elements.text
│   │               │   │               │   ├── xml.html
│   │               │   │               │   └── xml.text
│   │               │   │               ├── abbreviations/
│   │               │   │               │   ├── abbrev.html
│   │               │   │               │   ├── abbrev.text
│   │               │   │               │   ├── abbrev_defs.html
│   │               │   │               │   ├── abbrev_defs.text
│   │               │   │               │   ├── abbrev_in_html.html
│   │               │   │               │   ├── abbrev_in_html.text
│   │               │   │               │   ├── in_footnote.html
│   │               │   │               │   └── in_footnote.text
│   │               │   │               ├── autolinks/
│   │               │   │               │   ├── url_links.html
│   │               │   │               │   └── url_links.text
│   │               │   │               ├── escaped_chars/
│   │               │   │               │   ├── normal.html
│   │               │   │               │   └── normal.text
│   │               │   │               ├── extension/
│   │               │   │               │   ├── comment.html
│   │               │   │               │   ├── comment.text
│   │               │   │               │   ├── ignored.html
│   │               │   │               │   ├── ignored.text
│   │               │   │               │   ├── nomarkdown.html
│   │               │   │               │   ├── nomarkdown.text
│   │               │   │               │   ├── options.html
│   │               │   │               │   └── options.text
│   │               │   │               ├── ial/
│   │               │   │               │   ├── simple.html
│   │               │   │               │   └── simple.text
│   │               │   │               ├── line_breaks/
│   │               │   │               │   ├── normal.html
│   │               │   │               │   ├── normal.latex
│   │               │   │               │   └── normal.text
│   │               │   │               ├── math/
│   │               │   │               │   ├── no_engine.html
│   │               │   │               │   ├── no_engine.options
│   │               │   │               │   ├── no_engine.text
│   │               │   │               │   ├── normal.html
│   │               │   │               │   └── normal.text
│   │               │   │               └── text_substitutions/
│   │               │   │                   ├── entities.html
│   │               │   │                   ├── entities.options
│   │               │   │                   ├── entities.text
│   │               │   │                   ├── entities_as_char.html
│   │               │   │                   ├── entities_as_char.options
│   │               │   │                   ├── entities_as_char.text
│   │               │   │                   ├── entities_as_input.html
│   │               │   │                   ├── entities_as_input.options
│   │               │   │                   ├── entities_as_input.text
│   │               │   │                   ├── entities_numeric.html
│   │               │   │                   ├── entities_numeric.options
│   │               │   │                   ├── entities_numeric.text
│   │               │   │                   ├── entities_symbolic.html
│   │               │   │                   ├── entities_symbolic.options
│   │               │   │                   ├── entities_symbolic.text
│   │               │   │                   ├── greaterthan.html
│   │               │   │                   ├── greaterthan.text
│   │               │   │                   ├── lowerthan.html
│   │               │   │                   ├── lowerthan.text
│   │               │   │                   ├── typography.html
│   │               │   │                   ├── typography.options
│   │               │   │                   ├── typography.text
│   │               │   │                   ├── typography_subst.html
│   │               │   │                   ├── typography_subst.latex
│   │               │   │                   ├── typography_subst.options
│   │               │   │                   └── typography_subst.text
│   │               │   ├── kramdown-parser-gfm-1.1.0/
│   │               │   │   ├── CONTRIBUTERS
│   │               │   │   ├── COPYING
│   │               │   │   ├── VERSION
│   │               │   │   ├── lib/
│   │               │   │   │   ├── kramdown/
│   │               │   │   │   │   └── parser/
│   │               │   │   │   │       ├── gfm/
│   │               │   │   │   │       │   └── options.rb
│   │               │   │   │   │       └── gfm.rb
│   │               │   │   │   └── kramdown-parser-gfm.rb
│   │               │   │   └── test/
│   │               │   │       ├── test_files.rb
│   │               │   │       └── testcases/
│   │               │   │           ├── atx_header.html
│   │               │   │           ├── atx_header.text
│   │               │   │           ├── backticks_syntax.html
│   │               │   │           ├── backticks_syntax.options
│   │               │   │           ├── backticks_syntax.text
│   │               │   │           ├── codeblock_fenced.html
│   │               │   │           ├── codeblock_fenced.options
│   │               │   │           ├── codeblock_fenced.text
│   │               │   │           ├── hard_line_breaks.html
│   │               │   │           ├── hard_line_breaks.text
│   │               │   │           ├── hard_line_breaks_off.html
│   │               │   │           ├── hard_line_breaks_off.options
│   │               │   │           ├── hard_line_breaks_off.text
│   │               │   │           ├── header_ids.html
│   │               │   │           ├── header_ids.options
│   │               │   │           ├── header_ids.text
│   │               │   │           ├── header_ids_with_prefix.html
│   │               │   │           ├── header_ids_with_prefix.options
│   │               │   │           ├── header_ids_with_prefix.text
│   │               │   │           ├── no_typographic.html
│   │               │   │           ├── no_typographic.options
│   │               │   │           ├── no_typographic.text
│   │               │   │           ├── paragraph_end-disabled.html
│   │               │   │           ├── paragraph_end-disabled.options
│   │               │   │           ├── paragraph_end-disabled.text
│   │               │   │           ├── paragraph_end.html
│   │               │   │           ├── paragraph_end.text
│   │               │   │           ├── strikethrough.html
│   │               │   │           ├── strikethrough.text
│   │               │   │           ├── task_list.html
│   │               │   │           ├── task_list.text
│   │               │   │           ├── two_para_hard_line_breaks.html
│   │               │   │           └── two_para_hard_line_breaks.text
│   │               │   ├── liquid-4.0.4/
│   │               │   │   ├── History.md
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.md
│   │               │   │   ├── lib/
│   │               │   │   │   ├── liquid/
│   │               │   │   │   │   ├── block.rb
│   │               │   │   │   │   ├── block_body.rb
│   │               │   │   │   │   ├── condition.rb
│   │               │   │   │   │   ├── context.rb
│   │               │   │   │   │   ├── document.rb
│   │               │   │   │   │   ├── drop.rb
│   │               │   │   │   │   ├── errors.rb
│   │               │   │   │   │   ├── expression.rb
│   │               │   │   │   │   ├── extensions.rb
│   │               │   │   │   │   ├── file_system.rb
│   │               │   │   │   │   ├── forloop_drop.rb
│   │               │   │   │   │   ├── i18n.rb
│   │               │   │   │   │   ├── interrupts.rb
│   │               │   │   │   │   ├── lexer.rb
│   │               │   │   │   │   ├── locales/
│   │               │   │   │   │   │   └── en.yml
│   │               │   │   │   │   ├── parse_context.rb
│   │               │   │   │   │   ├── parse_tree_visitor.rb
│   │               │   │   │   │   ├── parser.rb
│   │               │   │   │   │   ├── parser_switching.rb
│   │               │   │   │   │   ├── profiler/
│   │               │   │   │   │   │   └── hooks.rb
│   │               │   │   │   │   ├── profiler.rb
│   │               │   │   │   │   ├── range_lookup.rb
│   │               │   │   │   │   ├── resource_limits.rb
│   │               │   │   │   │   ├── standardfilters.rb
│   │               │   │   │   │   ├── strainer.rb
│   │               │   │   │   │   ├── tablerowloop_drop.rb
│   │               │   │   │   │   ├── tag.rb
│   │               │   │   │   │   ├── tags/
│   │               │   │   │   │   │   ├── assign.rb
│   │               │   │   │   │   │   ├── break.rb
│   │               │   │   │   │   │   ├── capture.rb
│   │               │   │   │   │   │   ├── case.rb
│   │               │   │   │   │   │   ├── comment.rb
│   │               │   │   │   │   │   ├── continue.rb
│   │               │   │   │   │   │   ├── cycle.rb
│   │               │   │   │   │   │   ├── decrement.rb
│   │               │   │   │   │   │   ├── for.rb
│   │               │   │   │   │   │   ├── if.rb
│   │               │   │   │   │   │   ├── ifchanged.rb
│   │               │   │   │   │   │   ├── include.rb
│   │               │   │   │   │   │   ├── increment.rb
│   │               │   │   │   │   │   ├── raw.rb
│   │               │   │   │   │   │   ├── table_row.rb
│   │               │   │   │   │   │   └── unless.rb
│   │               │   │   │   │   ├── template.rb
│   │               │   │   │   │   ├── tokenizer.rb
│   │               │   │   │   │   ├── utils.rb
│   │               │   │   │   │   ├── variable.rb
│   │               │   │   │   │   ├── variable_lookup.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── liquid.rb
│   │               │   │   └── test/
│   │               │   │       ├── fixtures/
│   │               │   │       │   └── en_locale.yml
│   │               │   │       ├── integration/
│   │               │   │       │   ├── assign_test.rb
│   │               │   │       │   ├── blank_test.rb
│   │               │   │       │   ├── block_test.rb
│   │               │   │       │   ├── capture_test.rb
│   │               │   │       │   ├── context_test.rb
│   │               │   │       │   ├── document_test.rb
│   │               │   │       │   ├── drop_test.rb
│   │               │   │       │   ├── error_handling_test.rb
│   │               │   │       │   ├── filter_test.rb
│   │               │   │       │   ├── hash_ordering_test.rb
│   │               │   │       │   ├── output_test.rb
│   │               │   │       │   ├── parse_tree_visitor_test.rb
│   │               │   │       │   ├── parsing_quirks_test.rb
│   │               │   │       │   ├── render_profiling_test.rb
│   │               │   │       │   ├── security_test.rb
│   │               │   │       │   ├── standard_filter_test.rb
│   │               │   │       │   ├── tags/
│   │               │   │       │   │   ├── break_tag_test.rb
│   │               │   │       │   │   ├── continue_tag_test.rb
│   │               │   │       │   │   ├── for_tag_test.rb
│   │               │   │       │   │   ├── if_else_tag_test.rb
│   │               │   │       │   │   ├── include_tag_test.rb
│   │               │   │       │   │   ├── increment_tag_test.rb
│   │               │   │       │   │   ├── raw_tag_test.rb
│   │               │   │       │   │   ├── standard_tag_test.rb
│   │               │   │       │   │   ├── statements_test.rb
│   │               │   │       │   │   ├── table_row_test.rb
│   │               │   │       │   │   └── unless_else_tag_test.rb
│   │               │   │       │   ├── template_test.rb
│   │               │   │       │   ├── trim_mode_test.rb
│   │               │   │       │   └── variable_test.rb
│   │               │   │       ├── test_helper.rb
│   │               │   │       └── unit/
│   │               │   │           ├── block_unit_test.rb
│   │               │   │           ├── condition_unit_test.rb
│   │               │   │           ├── context_unit_test.rb
│   │               │   │           ├── file_system_unit_test.rb
│   │               │   │           ├── i18n_unit_test.rb
│   │               │   │           ├── lexer_unit_test.rb
│   │               │   │           ├── parser_unit_test.rb
│   │               │   │           ├── regexp_unit_test.rb
│   │               │   │           ├── strainer_unit_test.rb
│   │               │   │           ├── tag_unit_test.rb
│   │               │   │           ├── tags/
│   │               │   │           │   ├── case_tag_unit_test.rb
│   │               │   │           │   ├── for_tag_unit_test.rb
│   │               │   │           │   └── if_tag_unit_test.rb
│   │               │   │           ├── template_unit_test.rb
│   │               │   │           ├── tokenizer_unit_test.rb
│   │               │   │           └── variable_unit_test.rb
│   │               │   ├── listen-3.10.0/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── CONTRIBUTING.md
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── bin/
│   │               │   │   │   └── listen
│   │               │   │   └── lib/
│   │               │   │       ├── listen/
│   │               │   │       │   ├── adapter/
│   │               │   │       │   │   ├── base.rb
│   │               │   │       │   │   ├── bsd.rb
│   │               │   │       │   │   ├── config.rb
│   │               │   │       │   │   ├── darwin.rb
│   │               │   │       │   │   ├── linux.rb
│   │               │   │       │   │   ├── polling.rb
│   │               │   │       │   │   └── windows.rb
│   │               │   │       │   ├── adapter.rb
│   │               │   │       │   ├── backend.rb
│   │               │   │       │   ├── change.rb
│   │               │   │       │   ├── cli.rb
│   │               │   │       │   ├── directory.rb
│   │               │   │       │   ├── error.rb
│   │               │   │       │   ├── event/
│   │               │   │       │   │   ├── config.rb
│   │               │   │       │   │   ├── loop.rb
│   │               │   │       │   │   ├── processor.rb
│   │               │   │       │   │   └── queue.rb
│   │               │   │       │   ├── file.rb
│   │               │   │       │   ├── fsm.rb
│   │               │   │       │   ├── listener/
│   │               │   │       │   │   └── config.rb
│   │               │   │       │   ├── listener.rb
│   │               │   │       │   ├── logger.rb
│   │               │   │       │   ├── monotonic_time.rb
│   │               │   │       │   ├── options.rb
│   │               │   │       │   ├── queue_optimizer.rb
│   │               │   │       │   ├── record/
│   │               │   │       │   │   ├── entry.rb
│   │               │   │       │   │   └── symlink_detector.rb
│   │               │   │       │   ├── record.rb
│   │               │   │       │   ├── silencer/
│   │               │   │       │   │   └── controller.rb
│   │               │   │       │   ├── silencer.rb
│   │               │   │       │   ├── thread.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── listen.rb
│   │               │   ├── logger-1.7.0/
│   │               │   │   ├── .document
│   │               │   │   ├── .rdoc_options
│   │               │   │   ├── BSDL
│   │               │   │   ├── COPYING
│   │               │   │   ├── README.md
│   │               │   │   └── lib/
│   │               │   │       ├── logger/
│   │               │   │       │   ├── errors.rb
│   │               │   │       │   ├── formatter.rb
│   │               │   │       │   ├── log_device.rb
│   │               │   │       │   ├── period.rb
│   │               │   │       │   ├── severity.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── logger.rb
│   │               │   ├── mercenary-0.4.0/
│   │               │   │   ├── .gitignore
│   │               │   │   ├── .rspec
│   │               │   │   ├── .rubocop.yml
│   │               │   │   ├── .rubocop_todo.yml
│   │               │   │   ├── .travis.yml
│   │               │   │   ├── Gemfile
│   │               │   │   ├── History.markdown
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── examples/
│   │               │   │   │   ├── help_dialogue.rb
│   │               │   │   │   ├── logging.rb
│   │               │   │   │   └── trace.rb
│   │               │   │   ├── lib/
│   │               │   │   │   ├── mercenary/
│   │               │   │   │   │   ├── command.rb
│   │               │   │   │   │   ├── option.rb
│   │               │   │   │   │   ├── presenter.rb
│   │               │   │   │   │   ├── program.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── mercenary.rb
│   │               │   │   ├── mercenary.gemspec
│   │               │   │   ├── script/
│   │               │   │   │   ├── bootstrap
│   │               │   │   │   ├── cibuild
│   │               │   │   │   ├── console
│   │               │   │   │   ├── examples
│   │               │   │   │   └── fmt
│   │               │   │   └── spec/
│   │               │   │       ├── command_spec.rb
│   │               │   │       ├── option_spec.rb
│   │               │   │       ├── presenter_spec.rb
│   │               │   │       ├── program_spec.rb
│   │               │   │       └── spec_helper.rb
│   │               │   ├── pathutil-0.16.2/
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE
│   │               │   │   ├── Rakefile
│   │               │   │   └── lib/
│   │               │   │       ├── pathutil/
│   │               │   │       │   ├── helpers.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── pathutil.rb
│   │               │   ├── public_suffix-5.1.1/
│   │               │   │   ├── .yardopts
│   │               │   │   ├── 2.0-Upgrade.md
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── SECURITY.md
│   │               │   │   ├── data/
│   │               │   │   │   └── list.txt
│   │               │   │   └── lib/
│   │               │   │       ├── public_suffix/
│   │               │   │       │   ├── domain.rb
│   │               │   │       │   ├── errors.rb
│   │               │   │       │   ├── list.rb
│   │               │   │       │   ├── rule.rb
│   │               │   │       │   └── version.rb
│   │               │   │       └── public_suffix.rb
│   │               │   ├── rake-13.3.1/
│   │               │   │   ├── History.rdoc
│   │               │   │   ├── MIT-LICENSE
│   │               │   │   ├── README.rdoc
│   │               │   │   ├── doc/
│   │               │   │   │   ├── command_line_usage.rdoc
│   │               │   │   │   ├── example/
│   │               │   │   │   │   ├── Rakefile1
│   │               │   │   │   │   ├── Rakefile2
│   │               │   │   │   │   ├── a.c
│   │               │   │   │   │   ├── b.c
│   │               │   │   │   │   └── main.c
│   │               │   │   │   ├── glossary.rdoc
│   │               │   │   │   ├── jamis.rb
│   │               │   │   │   ├── proto_rake.rdoc
│   │               │   │   │   ├── rake.1
│   │               │   │   │   ├── rakefile.rdoc
│   │               │   │   │   └── rational.rdoc
│   │               │   │   ├── exe/
│   │               │   │   │   └── rake
│   │               │   │   ├── lib/
│   │               │   │   │   ├── rake/
│   │               │   │   │   │   ├── application.rb
│   │               │   │   │   │   ├── backtrace.rb
│   │               │   │   │   │   ├── clean.rb
│   │               │   │   │   │   ├── cloneable.rb
│   │               │   │   │   │   ├── cpu_counter.rb
│   │               │   │   │   │   ├── default_loader.rb
│   │               │   │   │   │   ├── dsl_definition.rb
│   │               │   │   │   │   ├── early_time.rb
│   │               │   │   │   │   ├── ext/
│   │               │   │   │   │   │   ├── core.rb
│   │               │   │   │   │   │   └── string.rb
│   │               │   │   │   │   ├── file_creation_task.rb
│   │               │   │   │   │   ├── file_list.rb
│   │               │   │   │   │   ├── file_task.rb
│   │               │   │   │   │   ├── file_utils.rb
│   │               │   │   │   │   ├── file_utils_ext.rb
│   │               │   │   │   │   ├── invocation_chain.rb
│   │               │   │   │   │   ├── invocation_exception_mixin.rb
│   │               │   │   │   │   ├── late_time.rb
│   │               │   │   │   │   ├── linked_list.rb
│   │               │   │   │   │   ├── loaders/
│   │               │   │   │   │   │   └── makefile.rb
│   │               │   │   │   │   ├── multi_task.rb
│   │               │   │   │   │   ├── name_space.rb
│   │               │   │   │   │   ├── packagetask.rb
│   │               │   │   │   │   ├── phony.rb
│   │               │   │   │   │   ├── private_reader.rb
│   │               │   │   │   │   ├── promise.rb
│   │               │   │   │   │   ├── pseudo_status.rb
│   │               │   │   │   │   ├── rake_module.rb
│   │               │   │   │   │   ├── rake_test_loader.rb
│   │               │   │   │   │   ├── rule_recursion_overflow_error.rb
│   │               │   │   │   │   ├── scope.rb
│   │               │   │   │   │   ├── task.rb
│   │               │   │   │   │   ├── task_argument_error.rb
│   │               │   │   │   │   ├── task_arguments.rb
│   │               │   │   │   │   ├── task_manager.rb
│   │               │   │   │   │   ├── tasklib.rb
│   │               │   │   │   │   ├── testtask.rb
│   │               │   │   │   │   ├── thread_history_display.rb
│   │               │   │   │   │   ├── thread_pool.rb
│   │               │   │   │   │   ├── trace_output.rb
│   │               │   │   │   │   ├── version.rb
│   │               │   │   │   │   └── win32.rb
│   │               │   │   │   └── rake.rb
│   │               │   │   └── rake.gemspec
│   │               │   ├── rb-fsevent-0.11.2/
│   │               │   │   ├── .gitignore
│   │               │   │   ├── Gemfile
│   │               │   │   ├── Guardfile
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── bin/
│   │               │   │   │   └── fsevent_watch
│   │               │   │   ├── ext/
│   │               │   │   │   ├── LICENSE
│   │               │   │   │   ├── fsevent_watch/
│   │               │   │   │   │   ├── FSEventsFix.c
│   │               │   │   │   │   ├── FSEventsFix.h
│   │               │   │   │   │   ├── TSICTString.c
│   │               │   │   │   │   ├── TSICTString.h
│   │               │   │   │   │   ├── cli.c
│   │               │   │   │   │   ├── cli.h
│   │               │   │   │   │   ├── common.h
│   │               │   │   │   │   ├── compat.c
│   │               │   │   │   │   ├── compat.h
│   │               │   │   │   │   ├── defines.h
│   │               │   │   │   │   ├── main.c
│   │               │   │   │   │   ├── signal_handlers.c
│   │               │   │   │   │   └── signal_handlers.h
│   │               │   │   │   └── rakefile.rb
│   │               │   │   ├── lib/
│   │               │   │   │   ├── otnetstring.rb
│   │               │   │   │   ├── rb-fsevent/
│   │               │   │   │   │   ├── fsevent.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── rb-fsevent.rb
│   │               │   │   └── rb-fsevent.gemspec
│   │               │   ├── rb-inotify-0.11.1/
│   │               │   │   ├── .github/
│   │               │   │   │   └── workflows/
│   │               │   │   │       └── test.yaml
│   │               │   │   ├── .gitignore
│   │               │   │   ├── .yardopts
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE.md
│   │               │   │   ├── README.md
│   │               │   │   ├── lib/
│   │               │   │   │   ├── rb-inotify/
│   │               │   │   │   │   ├── errors.rb
│   │               │   │   │   │   ├── event.rb
│   │               │   │   │   │   ├── native/
│   │               │   │   │   │   │   └── flags.rb
│   │               │   │   │   │   ├── native.rb
│   │               │   │   │   │   ├── notifier.rb
│   │               │   │   │   │   ├── version.rb
│   │               │   │   │   │   └── watcher.rb
│   │               │   │   │   └── rb-inotify.rb
│   │               │   │   ├── rb-inotify.gemspec
│   │               │   │   └── spec/
│   │               │   │       ├── inotify_spec.rb
│   │               │   │       ├── notifier_spec.rb
│   │               │   │       └── spec_helper.rb
│   │               │   ├── rexml-3.4.4/
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── NEWS.md
│   │               │   │   ├── README.md
│   │               │   │   ├── doc/
│   │               │   │   │   └── rexml/
│   │               │   │   │       ├── context.rdoc
│   │               │   │   │       ├── tasks/
│   │               │   │   │       │   ├── rdoc/
│   │               │   │   │       │   │   ├── child.rdoc
│   │               │   │   │       │   │   ├── document.rdoc
│   │               │   │   │       │   │   ├── element.rdoc
│   │               │   │   │       │   │   ├── node.rdoc
│   │               │   │   │       │   │   └── parent.rdoc
│   │               │   │   │       │   └── tocs/
│   │               │   │   │       │       ├── child_toc.rdoc
│   │               │   │   │       │       ├── document_toc.rdoc
│   │               │   │   │       │       ├── element_toc.rdoc
│   │               │   │   │       │       ├── master_toc.rdoc
│   │               │   │   │       │       ├── node_toc.rdoc
│   │               │   │   │       │       └── parent_toc.rdoc
│   │               │   │   │       └── tutorial.rdoc
│   │               │   │   └── lib/
│   │               │   │       ├── rexml/
│   │               │   │       │   ├── attlistdecl.rb
│   │               │   │       │   ├── attribute.rb
│   │               │   │       │   ├── cdata.rb
│   │               │   │       │   ├── child.rb
│   │               │   │       │   ├── comment.rb
│   │               │   │       │   ├── doctype.rb
│   │               │   │       │   ├── document.rb
│   │               │   │       │   ├── dtd/
│   │               │   │       │   │   ├── attlistdecl.rb
│   │               │   │       │   │   ├── dtd.rb
│   │               │   │       │   │   ├── elementdecl.rb
│   │               │   │       │   │   ├── entitydecl.rb
│   │               │   │       │   │   └── notationdecl.rb
│   │               │   │       │   ├── element.rb
│   │               │   │       │   ├── encoding.rb
│   │               │   │       │   ├── entity.rb
│   │               │   │       │   ├── formatters/
│   │               │   │       │   │   ├── default.rb
│   │               │   │       │   │   ├── pretty.rb
│   │               │   │       │   │   └── transitive.rb
│   │               │   │       │   ├── functions.rb
│   │               │   │       │   ├── instruction.rb
│   │               │   │       │   ├── light/
│   │               │   │       │   │   └── node.rb
│   │               │   │       │   ├── namespace.rb
│   │               │   │       │   ├── node.rb
│   │               │   │       │   ├── output.rb
│   │               │   │       │   ├── parent.rb
│   │               │   │       │   ├── parseexception.rb
│   │               │   │       │   ├── parsers/
│   │               │   │       │   │   ├── baseparser.rb
│   │               │   │       │   │   ├── lightparser.rb
│   │               │   │       │   │   ├── pullparser.rb
│   │               │   │       │   │   ├── sax2parser.rb
│   │               │   │       │   │   ├── streamparser.rb
│   │               │   │       │   │   ├── treeparser.rb
│   │               │   │       │   │   ├── ultralightparser.rb
│   │               │   │       │   │   └── xpathparser.rb
│   │               │   │       │   ├── quickpath.rb
│   │               │   │       │   ├── rexml.rb
│   │               │   │       │   ├── sax2listener.rb
│   │               │   │       │   ├── security.rb
│   │               │   │       │   ├── source.rb
│   │               │   │       │   ├── streamlistener.rb
│   │               │   │       │   ├── text.rb
│   │               │   │       │   ├── undefinednamespaceexception.rb
│   │               │   │       │   ├── validation/
│   │               │   │       │   │   ├── relaxng.rb
│   │               │   │       │   │   ├── validation.rb
│   │               │   │       │   │   └── validationexception.rb
│   │               │   │       │   ├── xmldecl.rb
│   │               │   │       │   ├── xmltokens.rb
│   │               │   │       │   ├── xpath.rb
│   │               │   │       │   └── xpath_parser.rb
│   │               │   │       └── rexml.rb
│   │               │   ├── rouge-3.30.0/
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE
│   │               │   │   ├── bin/
│   │               │   │   │   └── rougify
│   │               │   │   ├── lib/
│   │               │   │   │   ├── rouge/
│   │               │   │   │   │   ├── cli.rb
│   │               │   │   │   │   ├── demos/
│   │               │   │   │   │   │   ├── abap
│   │               │   │   │   │   │   ├── actionscript
│   │               │   │   │   │   │   ├── ada
│   │               │   │   │   │   │   ├── apache
│   │               │   │   │   │   │   ├── apex
│   │               │   │   │   │   │   ├── apiblueprint
│   │               │   │   │   │   │   ├── applescript
│   │               │   │   │   │   │   ├── armasm
│   │               │   │   │   │   │   ├── augeas
│   │               │   │   │   │   │   ├── awk
│   │               │   │   │   │   │   ├── batchfile
│   │               │   │   │   │   │   ├── bbcbasic
│   │               │   │   │   │   │   ├── bibtex
│   │               │   │   │   │   │   ├── biml
│   │               │   │   │   │   │   ├── bpf
│   │               │   │   │   │   │   ├── brainfuck
│   │               │   │   │   │   │   ├── brightscript
│   │               │   │   │   │   │   ├── bsl
│   │               │   │   │   │   │   ├── c
│   │               │   │   │   │   │   ├── ceylon
│   │               │   │   │   │   │   ├── cfscript
│   │               │   │   │   │   │   ├── clean
│   │               │   │   │   │   │   ├── clojure
│   │               │   │   │   │   │   ├── cmake
│   │               │   │   │   │   │   ├── cmhg
│   │               │   │   │   │   │   ├── coffeescript
│   │               │   │   │   │   │   ├── common_lisp
│   │               │   │   │   │   │   ├── conf
│   │               │   │   │   │   │   ├── console
│   │               │   │   │   │   │   ├── coq
│   │               │   │   │   │   │   ├── cpp
│   │               │   │   │   │   │   ├── crystal
│   │               │   │   │   │   │   ├── csharp
│   │               │   │   │   │   │   ├── css
│   │               │   │   │   │   │   ├── csvs
│   │               │   │   │   │   │   ├── cuda
│   │               │   │   │   │   │   ├── cypher
│   │               │   │   │   │   │   ├── cython
│   │               │   │   │   │   │   ├── d
│   │               │   │   │   │   │   ├── dafny
│   │               │   │   │   │   │   ├── dart
│   │               │   │   │   │   │   ├── datastudio
│   │               │   │   │   │   │   ├── diff
│   │               │   │   │   │   │   ├── digdag
│   │               │   │   │   │   │   ├── docker
│   │               │   │   │   │   │   ├── dot
│   │               │   │   │   │   │   ├── ecl
│   │               │   │   │   │   │   ├── eex
│   │               │   │   │   │   │   ├── eiffel
│   │               │   │   │   │   │   ├── elixir
│   │               │   │   │   │   │   ├── elm
│   │               │   │   │   │   │   ├── email
│   │               │   │   │   │   │   ├── epp
│   │               │   │   │   │   │   ├── erb
│   │               │   │   │   │   │   ├── erlang
│   │               │   │   │   │   │   ├── escape
│   │               │   │   │   │   │   ├── factor
│   │               │   │   │   │   │   ├── fluent
│   │               │   │   │   │   │   ├── fortran
│   │               │   │   │   │   │   ├── freefem
│   │               │   │   │   │   │   ├── fsharp
│   │               │   │   │   │   │   ├── gdscript
│   │               │   │   │   │   │   ├── ghc-cmm
│   │               │   │   │   │   │   ├── ghc-core
│   │               │   │   │   │   │   ├── gherkin
│   │               │   │   │   │   │   ├── glsl
│   │               │   │   │   │   │   ├── go
│   │               │   │   │   │   │   ├── gradle
│   │               │   │   │   │   │   ├── graphql
│   │               │   │   │   │   │   ├── groovy
│   │               │   │   │   │   │   ├── hack
│   │               │   │   │   │   │   ├── haml
│   │               │   │   │   │   │   ├── handlebars
│   │               │   │   │   │   │   ├── haskell
│   │               │   │   │   │   │   ├── haxe
│   │               │   │   │   │   │   ├── hcl
│   │               │   │   │   │   │   ├── hlsl
│   │               │   │   │   │   │   ├── hocon
│   │               │   │   │   │   │   ├── hql
│   │               │   │   │   │   │   ├── html
│   │               │   │   │   │   │   ├── http
│   │               │   │   │   │   │   ├── hylang
│   │               │   │   │   │   │   ├── idlang
│   │               │   │   │   │   │   ├── idris
│   │               │   │   │   │   │   ├── igorpro
│   │               │   │   │   │   │   ├── ini
│   │               │   │   │   │   │   ├── io
│   │               │   │   │   │   │   ├── irb
│   │               │   │   │   │   │   ├── irb_output
│   │               │   │   │   │   │   ├── isabelle
│   │               │   │   │   │   │   ├── isbl
│   │               │   │   │   │   │   ├── j
│   │               │   │   │   │   │   ├── janet
│   │               │   │   │   │   │   ├── java
│   │               │   │   │   │   │   ├── javascript
│   │               │   │   │   │   │   ├── jinja
│   │               │   │   │   │   │   ├── jsl
│   │               │   │   │   │   │   ├── json
│   │               │   │   │   │   │   ├── json-doc
│   │               │   │   │   │   │   ├── jsonnet
│   │               │   │   │   │   │   ├── jsp
│   │               │   │   │   │   │   ├── jsx
│   │               │   │   │   │   │   ├── julia
│   │               │   │   │   │   │   ├── kotlin
│   │               │   │   │   │   │   ├── lasso
│   │               │   │   │   │   │   ├── lean
│   │               │   │   │   │   │   ├── liquid
│   │               │   │   │   │   │   ├── literate_coffeescript
│   │               │   │   │   │   │   ├── literate_haskell
│   │               │   │   │   │   │   ├── livescript
│   │               │   │   │   │   │   ├── llvm
│   │               │   │   │   │   │   ├── lua
│   │               │   │   │   │   │   ├── lustre
│   │               │   │   │   │   │   ├── lutin
│   │               │   │   │   │   │   ├── m68k
│   │               │   │   │   │   │   ├── magik
│   │               │   │   │   │   │   ├── make
│   │               │   │   │   │   │   ├── markdown
│   │               │   │   │   │   │   ├── mason
│   │               │   │   │   │   │   ├── mathematica
│   │               │   │   │   │   │   ├── matlab
│   │               │   │   │   │   │   ├── meson
│   │               │   │   │   │   │   ├── minizinc
│   │               │   │   │   │   │   ├── moonscript
│   │               │   │   │   │   │   ├── mosel
│   │               │   │   │   │   │   ├── msgtrans
│   │               │   │   │   │   │   ├── mxml
│   │               │   │   │   │   │   ├── nasm
│   │               │   │   │   │   │   ├── nesasm
│   │               │   │   │   │   │   ├── nginx
│   │               │   │   │   │   │   ├── nial
│   │               │   │   │   │   │   ├── nim
│   │               │   │   │   │   │   ├── nix
│   │               │   │   │   │   │   ├── objective_c
│   │               │   │   │   │   │   ├── objective_cpp
│   │               │   │   │   │   │   ├── ocaml
│   │               │   │   │   │   │   ├── ocl
│   │               │   │   │   │   │   ├── openedge
│   │               │   │   │   │   │   ├── opentype_feature_file
│   │               │   │   │   │   │   ├── pascal
│   │               │   │   │   │   │   ├── perl
│   │               │   │   │   │   │   ├── php
│   │               │   │   │   │   │   ├── plaintext
│   │               │   │   │   │   │   ├── plist
│   │               │   │   │   │   │   ├── plsql
│   │               │   │   │   │   │   ├── pony
│   │               │   │   │   │   │   ├── postscript
│   │               │   │   │   │   │   ├── powershell
│   │               │   │   │   │   │   ├── praat
│   │               │   │   │   │   │   ├── prolog
│   │               │   │   │   │   │   ├── prometheus
│   │               │   │   │   │   │   ├── properties
│   │               │   │   │   │   │   ├── protobuf
│   │               │   │   │   │   │   ├── puppet
│   │               │   │   │   │   │   ├── python
│   │               │   │   │   │   │   ├── q
│   │               │   │   │   │   │   ├── qml
│   │               │   │   │   │   │   ├── r
│   │               │   │   │   │   │   ├── racket
│   │               │   │   │   │   │   ├── reasonml
│   │               │   │   │   │   │   ├── rego
│   │               │   │   │   │   │   ├── rescript
│   │               │   │   │   │   │   ├── robot_framework
│   │               │   │   │   │   │   ├── ruby
│   │               │   │   │   │   │   ├── rust
│   │               │   │   │   │   │   ├── sas
│   │               │   │   │   │   │   ├── sass
│   │               │   │   │   │   │   ├── scala
│   │               │   │   │   │   │   ├── scheme
│   │               │   │   │   │   │   ├── scss
│   │               │   │   │   │   │   ├── sed
│   │               │   │   │   │   │   ├── shell
│   │               │   │   │   │   │   ├── sieve
│   │               │   │   │   │   │   ├── slice
│   │               │   │   │   │   │   ├── slim
│   │               │   │   │   │   │   ├── smalltalk
│   │               │   │   │   │   │   ├── smarty
│   │               │   │   │   │   │   ├── sml
│   │               │   │   │   │   │   ├── solidity
│   │               │   │   │   │   │   ├── sparql
│   │               │   │   │   │   │   ├── sqf
│   │               │   │   │   │   │   ├── sql
│   │               │   │   │   │   │   ├── ssh
│   │               │   │   │   │   │   ├── stan
│   │               │   │   │   │   │   ├── stata
│   │               │   │   │   │   │   ├── supercollider
│   │               │   │   │   │   │   ├── swift
│   │               │   │   │   │   │   ├── systemd
│   │               │   │   │   │   │   ├── syzlang
│   │               │   │   │   │   │   ├── syzprog
│   │               │   │   │   │   │   ├── tap
│   │               │   │   │   │   │   ├── tcl
│   │               │   │   │   │   │   ├── terraform
│   │               │   │   │   │   │   ├── tex
│   │               │   │   │   │   │   ├── toml
│   │               │   │   │   │   │   ├── tsx
│   │               │   │   │   │   │   ├── ttcn3
│   │               │   │   │   │   │   ├── tulip
│   │               │   │   │   │   │   ├── turtle
│   │               │   │   │   │   │   ├── twig
│   │               │   │   │   │   │   ├── typescript
│   │               │   │   │   │   │   ├── vala
│   │               │   │   │   │   │   ├── vb
│   │               │   │   │   │   │   ├── vcl
│   │               │   │   │   │   │   ├── velocity
│   │               │   │   │   │   │   ├── verilog
│   │               │   │   │   │   │   ├── vhdl
│   │               │   │   │   │   │   ├── viml
│   │               │   │   │   │   │   ├── vue
│   │               │   │   │   │   │   ├── wollok
│   │               │   │   │   │   │   ├── xml
│   │               │   │   │   │   │   ├── xojo
│   │               │   │   │   │   │   ├── xpath
│   │               │   │   │   │   │   ├── xquery
│   │               │   │   │   │   │   ├── yaml
│   │               │   │   │   │   │   ├── yang
│   │               │   │   │   │   │   └── zig
│   │               │   │   │   │   ├── formatter.rb
│   │               │   │   │   │   ├── formatters/
│   │               │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   ├── html_inline.rb
│   │               │   │   │   │   │   ├── html_legacy.rb
│   │               │   │   │   │   │   ├── html_line_highlighter.rb
│   │               │   │   │   │   │   ├── html_line_table.rb
│   │               │   │   │   │   │   ├── html_linewise.rb
│   │               │   │   │   │   │   ├── html_pygments.rb
│   │               │   │   │   │   │   ├── html_table.rb
│   │               │   │   │   │   │   ├── null.rb
│   │               │   │   │   │   │   ├── terminal256.rb
│   │               │   │   │   │   │   ├── terminal_truecolor.rb
│   │               │   │   │   │   │   └── tex.rb
│   │               │   │   │   │   ├── guesser.rb
│   │               │   │   │   │   ├── guessers/
│   │               │   │   │   │   │   ├── disambiguation.rb
│   │               │   │   │   │   │   ├── filename.rb
│   │               │   │   │   │   │   ├── glob_mapping.rb
│   │               │   │   │   │   │   ├── mimetype.rb
│   │               │   │   │   │   │   ├── modeline.rb
│   │               │   │   │   │   │   ├── source.rb
│   │               │   │   │   │   │   └── util.rb
│   │               │   │   │   │   ├── lexer.rb
│   │               │   │   │   │   ├── lexers/
│   │               │   │   │   │   │   ├── abap.rb
│   │               │   │   │   │   │   ├── actionscript.rb
│   │               │   │   │   │   │   ├── ada.rb
│   │               │   │   │   │   │   ├── apache/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── apache.rb
│   │               │   │   │   │   │   ├── apex.rb
│   │               │   │   │   │   │   ├── apiblueprint.rb
│   │               │   │   │   │   │   ├── apple_script.rb
│   │               │   │   │   │   │   ├── armasm.rb
│   │               │   │   │   │   │   ├── augeas.rb
│   │               │   │   │   │   │   ├── awk.rb
│   │               │   │   │   │   │   ├── batchfile.rb
│   │               │   │   │   │   │   ├── bbcbasic.rb
│   │               │   │   │   │   │   ├── bibtex.rb
│   │               │   │   │   │   │   ├── biml.rb
│   │               │   │   │   │   │   ├── bpf.rb
│   │               │   │   │   │   │   ├── brainfuck.rb
│   │               │   │   │   │   │   ├── brightscript.rb
│   │               │   │   │   │   │   ├── bsl.rb
│   │               │   │   │   │   │   ├── c.rb
│   │               │   │   │   │   │   ├── ceylon.rb
│   │               │   │   │   │   │   ├── cfscript.rb
│   │               │   │   │   │   │   ├── clean.rb
│   │               │   │   │   │   │   ├── clojure.rb
│   │               │   │   │   │   │   ├── cmake.rb
│   │               │   │   │   │   │   ├── cmhg.rb
│   │               │   │   │   │   │   ├── coffeescript.rb
│   │               │   │   │   │   │   ├── common_lisp.rb
│   │               │   │   │   │   │   ├── conf.rb
│   │               │   │   │   │   │   ├── console.rb
│   │               │   │   │   │   │   ├── coq.rb
│   │               │   │   │   │   │   ├── cpp.rb
│   │               │   │   │   │   │   ├── crystal.rb
│   │               │   │   │   │   │   ├── csharp.rb
│   │               │   │   │   │   │   ├── css.rb
│   │               │   │   │   │   │   ├── csvs.rb
│   │               │   │   │   │   │   ├── cuda.rb
│   │               │   │   │   │   │   ├── cypher.rb
│   │               │   │   │   │   │   ├── cython.rb
│   │               │   │   │   │   │   ├── d.rb
│   │               │   │   │   │   │   ├── dafny.rb
│   │               │   │   │   │   │   ├── dart.rb
│   │               │   │   │   │   │   ├── datastudio.rb
│   │               │   │   │   │   │   ├── diff.rb
│   │               │   │   │   │   │   ├── digdag.rb
│   │               │   │   │   │   │   ├── docker.rb
│   │               │   │   │   │   │   ├── dot.rb
│   │               │   │   │   │   │   ├── ecl.rb
│   │               │   │   │   │   │   ├── eex.rb
│   │               │   │   │   │   │   ├── eiffel.rb
│   │               │   │   │   │   │   ├── elixir.rb
│   │               │   │   │   │   │   ├── elm.rb
│   │               │   │   │   │   │   ├── email.rb
│   │               │   │   │   │   │   ├── epp.rb
│   │               │   │   │   │   │   ├── erb.rb
│   │               │   │   │   │   │   ├── erlang.rb
│   │               │   │   │   │   │   ├── escape.rb
│   │               │   │   │   │   │   ├── factor.rb
│   │               │   │   │   │   │   ├── fluent.rb
│   │               │   │   │   │   │   ├── fortran.rb
│   │               │   │   │   │   │   ├── freefem.rb
│   │               │   │   │   │   │   ├── fsharp.rb
│   │               │   │   │   │   │   ├── gdscript.rb
│   │               │   │   │   │   │   ├── ghc_cmm.rb
│   │               │   │   │   │   │   ├── ghc_core.rb
│   │               │   │   │   │   │   ├── gherkin/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── gherkin.rb
│   │               │   │   │   │   │   ├── glsl.rb
│   │               │   │   │   │   │   ├── go.rb
│   │               │   │   │   │   │   ├── gradle.rb
│   │               │   │   │   │   │   ├── graphql.rb
│   │               │   │   │   │   │   ├── groovy.rb
│   │               │   │   │   │   │   ├── hack.rb
│   │               │   │   │   │   │   ├── haml.rb
│   │               │   │   │   │   │   ├── handlebars.rb
│   │               │   │   │   │   │   ├── haskell.rb
│   │               │   │   │   │   │   ├── haxe.rb
│   │               │   │   │   │   │   ├── hcl.rb
│   │               │   │   │   │   │   ├── hlsl.rb
│   │               │   │   │   │   │   ├── hocon.rb
│   │               │   │   │   │   │   ├── hql.rb
│   │               │   │   │   │   │   ├── html.rb
│   │               │   │   │   │   │   ├── http.rb
│   │               │   │   │   │   │   ├── hylang.rb
│   │               │   │   │   │   │   ├── idlang.rb
│   │               │   │   │   │   │   ├── idris.rb
│   │               │   │   │   │   │   ├── igorpro.rb
│   │               │   │   │   │   │   ├── ini.rb
│   │               │   │   │   │   │   ├── io.rb
│   │               │   │   │   │   │   ├── irb.rb
│   │               │   │   │   │   │   ├── isabelle.rb
│   │               │   │   │   │   │   ├── isbl/
│   │               │   │   │   │   │   │   └── builtins.rb
│   │               │   │   │   │   │   ├── isbl.rb
│   │               │   │   │   │   │   ├── j.rb
│   │               │   │   │   │   │   ├── janet.rb
│   │               │   │   │   │   │   ├── java.rb
│   │               │   │   │   │   │   ├── javascript.rb
│   │               │   │   │   │   │   ├── jinja.rb
│   │               │   │   │   │   │   ├── jsl.rb
│   │               │   │   │   │   │   ├── json.rb
│   │               │   │   │   │   │   ├── json_doc.rb
│   │               │   │   │   │   │   ├── jsonnet.rb
│   │               │   │   │   │   │   ├── jsp.rb
│   │               │   │   │   │   │   ├── jsx.rb
│   │               │   │   │   │   │   ├── julia.rb
│   │               │   │   │   │   │   ├── kotlin.rb
│   │               │   │   │   │   │   ├── lasso/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── lasso.rb
│   │               │   │   │   │   │   ├── lean.rb
│   │               │   │   │   │   │   ├── liquid.rb
│   │               │   │   │   │   │   ├── literate_coffeescript.rb
│   │               │   │   │   │   │   ├── literate_haskell.rb
│   │               │   │   │   │   │   ├── livescript.rb
│   │               │   │   │   │   │   ├── llvm/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── llvm.rb
│   │               │   │   │   │   │   ├── lua/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── lua.rb
│   │               │   │   │   │   │   ├── lustre.rb
│   │               │   │   │   │   │   ├── lutin.rb
│   │               │   │   │   │   │   ├── m68k.rb
│   │               │   │   │   │   │   ├── magik.rb
│   │               │   │   │   │   │   ├── make.rb
│   │               │   │   │   │   │   ├── markdown.rb
│   │               │   │   │   │   │   ├── mason.rb
│   │               │   │   │   │   │   ├── mathematica/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── mathematica.rb
│   │               │   │   │   │   │   ├── matlab/
│   │               │   │   │   │   │   │   ├── builtins.rb
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── matlab.rb
│   │               │   │   │   │   │   ├── meson.rb
│   │               │   │   │   │   │   ├── minizinc.rb
│   │               │   │   │   │   │   ├── moonscript.rb
│   │               │   │   │   │   │   ├── mosel.rb
│   │               │   │   │   │   │   ├── msgtrans.rb
│   │               │   │   │   │   │   ├── mxml.rb
│   │               │   │   │   │   │   ├── nasm.rb
│   │               │   │   │   │   │   ├── nesasm.rb
│   │               │   │   │   │   │   ├── nginx.rb
│   │               │   │   │   │   │   ├── nial.rb
│   │               │   │   │   │   │   ├── nim.rb
│   │               │   │   │   │   │   ├── nix.rb
│   │               │   │   │   │   │   ├── objective_c/
│   │               │   │   │   │   │   │   └── common.rb
│   │               │   │   │   │   │   ├── objective_c.rb
│   │               │   │   │   │   │   ├── objective_cpp.rb
│   │               │   │   │   │   │   ├── ocaml/
│   │               │   │   │   │   │   │   └── common.rb
│   │               │   │   │   │   │   ├── ocaml.rb
│   │               │   │   │   │   │   ├── ocl.rb
│   │               │   │   │   │   │   ├── openedge.rb
│   │               │   │   │   │   │   ├── opentype_feature_file.rb
│   │               │   │   │   │   │   ├── pascal.rb
│   │               │   │   │   │   │   ├── perl.rb
│   │               │   │   │   │   │   ├── php/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── php.rb
│   │               │   │   │   │   │   ├── plain_text.rb
│   │               │   │   │   │   │   ├── plist.rb
│   │               │   │   │   │   │   ├── plsql.rb
│   │               │   │   │   │   │   ├── pony.rb
│   │               │   │   │   │   │   ├── postscript.rb
│   │               │   │   │   │   │   ├── powershell.rb
│   │               │   │   │   │   │   ├── praat.rb
│   │               │   │   │   │   │   ├── prolog.rb
│   │               │   │   │   │   │   ├── prometheus.rb
│   │               │   │   │   │   │   ├── properties.rb
│   │               │   │   │   │   │   ├── protobuf.rb
│   │               │   │   │   │   │   ├── puppet.rb
│   │               │   │   │   │   │   ├── python.rb
│   │               │   │   │   │   │   ├── q.rb
│   │               │   │   │   │   │   ├── qml.rb
│   │               │   │   │   │   │   ├── r.rb
│   │               │   │   │   │   │   ├── racket.rb
│   │               │   │   │   │   │   ├── reasonml.rb
│   │               │   │   │   │   │   ├── rego.rb
│   │               │   │   │   │   │   ├── rescript.rb
│   │               │   │   │   │   │   ├── robot_framework.rb
│   │               │   │   │   │   │   ├── ruby.rb
│   │               │   │   │   │   │   ├── rust.rb
│   │               │   │   │   │   │   ├── sas.rb
│   │               │   │   │   │   │   ├── sass/
│   │               │   │   │   │   │   │   └── common.rb
│   │               │   │   │   │   │   ├── sass.rb
│   │               │   │   │   │   │   ├── scala.rb
│   │               │   │   │   │   │   ├── scheme.rb
│   │               │   │   │   │   │   ├── scss.rb
│   │               │   │   │   │   │   ├── sed.rb
│   │               │   │   │   │   │   ├── shell.rb
│   │               │   │   │   │   │   ├── sieve.rb
│   │               │   │   │   │   │   ├── slice.rb
│   │               │   │   │   │   │   ├── slim.rb
│   │               │   │   │   │   │   ├── smalltalk.rb
│   │               │   │   │   │   │   ├── smarty.rb
│   │               │   │   │   │   │   ├── sml.rb
│   │               │   │   │   │   │   ├── solidity.rb
│   │               │   │   │   │   │   ├── sparql.rb
│   │               │   │   │   │   │   ├── sqf/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── sqf.rb
│   │               │   │   │   │   │   ├── sql.rb
│   │               │   │   │   │   │   ├── ssh.rb
│   │               │   │   │   │   │   ├── stan.rb
│   │               │   │   │   │   │   ├── stata.rb
│   │               │   │   │   │   │   ├── supercollider.rb
│   │               │   │   │   │   │   ├── swift.rb
│   │               │   │   │   │   │   ├── systemd.rb
│   │               │   │   │   │   │   ├── syzlang.rb
│   │               │   │   │   │   │   ├── syzprog.rb
│   │               │   │   │   │   │   ├── tap.rb
│   │               │   │   │   │   │   ├── tcl.rb
│   │               │   │   │   │   │   ├── terraform.rb
│   │               │   │   │   │   │   ├── tex.rb
│   │               │   │   │   │   │   ├── toml.rb
│   │               │   │   │   │   │   ├── tsx.rb
│   │               │   │   │   │   │   ├── ttcn3.rb
│   │               │   │   │   │   │   ├── tulip.rb
│   │               │   │   │   │   │   ├── turtle.rb
│   │               │   │   │   │   │   ├── twig.rb
│   │               │   │   │   │   │   ├── typescript/
│   │               │   │   │   │   │   │   └── common.rb
│   │               │   │   │   │   │   ├── typescript.rb
│   │               │   │   │   │   │   ├── vala.rb
│   │               │   │   │   │   │   ├── varnish.rb
│   │               │   │   │   │   │   ├── vb.rb
│   │               │   │   │   │   │   ├── velocity.rb
│   │               │   │   │   │   │   ├── verilog.rb
│   │               │   │   │   │   │   ├── vhdl.rb
│   │               │   │   │   │   │   ├── viml/
│   │               │   │   │   │   │   │   └── keywords.rb
│   │               │   │   │   │   │   ├── viml.rb
│   │               │   │   │   │   │   ├── vue.rb
│   │               │   │   │   │   │   ├── wollok.rb
│   │               │   │   │   │   │   ├── xml.rb
│   │               │   │   │   │   │   ├── xojo.rb
│   │               │   │   │   │   │   ├── xpath.rb
│   │               │   │   │   │   │   ├── xquery.rb
│   │               │   │   │   │   │   ├── yaml.rb
│   │               │   │   │   │   │   ├── yang.rb
│   │               │   │   │   │   │   └── zig.rb
│   │               │   │   │   │   ├── plugins/
│   │               │   │   │   │   │   └── redcarpet.rb
│   │               │   │   │   │   ├── regex_lexer.rb
│   │               │   │   │   │   ├── template_lexer.rb
│   │               │   │   │   │   ├── tex_theme_renderer.rb
│   │               │   │   │   │   ├── text_analyzer.rb
│   │               │   │   │   │   ├── theme.rb
│   │               │   │   │   │   ├── themes/
│   │               │   │   │   │   │   ├── base16.rb
│   │               │   │   │   │   │   ├── bw.rb
│   │               │   │   │   │   │   ├── colorful.rb
│   │               │   │   │   │   │   ├── github.rb
│   │               │   │   │   │   │   ├── gruvbox.rb
│   │               │   │   │   │   │   ├── igor_pro.rb
│   │               │   │   │   │   │   ├── magritte.rb
│   │               │   │   │   │   │   ├── molokai.rb
│   │               │   │   │   │   │   ├── monokai.rb
│   │               │   │   │   │   │   ├── monokai_sublime.rb
│   │               │   │   │   │   │   ├── pastie.rb
│   │               │   │   │   │   │   ├── thankful_eyes.rb
│   │               │   │   │   │   │   └── tulip.rb
│   │               │   │   │   │   ├── token.rb
│   │               │   │   │   │   ├── util.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── rouge.rb
│   │               │   │   └── rouge.gemspec
│   │               │   ├── safe_yaml-1.0.5/
│   │               │   │   ├── .gitignore
│   │               │   │   ├── .travis.yml
│   │               │   │   ├── CHANGES.md
│   │               │   │   ├── Gemfile
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── bin/
│   │               │   │   │   └── safe_yaml
│   │               │   │   ├── bundle_install_all_ruby_versions.sh
│   │               │   │   ├── lib/
│   │               │   │   │   ├── safe_yaml/
│   │               │   │   │   │   ├── deep.rb
│   │               │   │   │   │   ├── libyaml_checker.rb
│   │               │   │   │   │   ├── load.rb
│   │               │   │   │   │   ├── parse/
│   │               │   │   │   │   │   ├── date.rb
│   │               │   │   │   │   │   ├── hexadecimal.rb
│   │               │   │   │   │   │   └── sexagesimal.rb
│   │               │   │   │   │   ├── psych_handler.rb
│   │               │   │   │   │   ├── psych_resolver.rb
│   │               │   │   │   │   ├── resolver.rb
│   │               │   │   │   │   ├── safe_to_ruby_visitor.rb
│   │               │   │   │   │   ├── store.rb
│   │               │   │   │   │   ├── syck_hack.rb
│   │               │   │   │   │   ├── syck_node_monkeypatch.rb
│   │               │   │   │   │   ├── syck_resolver.rb
│   │               │   │   │   │   ├── transform/
│   │               │   │   │   │   │   ├── to_boolean.rb
│   │               │   │   │   │   │   ├── to_date.rb
│   │               │   │   │   │   │   ├── to_float.rb
│   │               │   │   │   │   │   ├── to_integer.rb
│   │               │   │   │   │   │   ├── to_nil.rb
│   │               │   │   │   │   │   ├── to_symbol.rb
│   │               │   │   │   │   │   └── transformation_map.rb
│   │               │   │   │   │   ├── transform.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── safe_yaml.rb
│   │               │   │   ├── run_specs_all_ruby_versions.sh
│   │               │   │   ├── safe_yaml.gemspec
│   │               │   │   └── spec/
│   │               │   │       ├── exploit.1.9.2.yaml
│   │               │   │       ├── exploit.1.9.3.yaml
│   │               │   │       ├── issue48.txt
│   │               │   │       ├── issue49.yml
│   │               │   │       ├── libyaml_checker_spec.rb
│   │               │   │       ├── psych_resolver_spec.rb
│   │               │   │       ├── resolver_specs.rb
│   │               │   │       ├── safe_yaml_spec.rb
│   │               │   │       ├── spec_helper.rb
│   │               │   │       ├── store_spec.rb
│   │               │   │       ├── support/
│   │               │   │       │   └── exploitable_back_door.rb
│   │               │   │       ├── syck_resolver_spec.rb
│   │               │   │       ├── transform/
│   │               │   │       │   ├── base64_spec.rb
│   │               │   │       │   ├── to_date_spec.rb
│   │               │   │       │   ├── to_float_spec.rb
│   │               │   │       │   ├── to_integer_spec.rb
│   │               │   │       │   └── to_symbol_spec.rb
│   │               │   │       └── yaml_spec.rb
│   │               │   ├── sass-embedded-1.58.3/
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.md
│   │               │   │   ├── ext/
│   │               │   │   │   └── sass/
│   │               │   │   │       ├── Rakefile
│   │               │   │   │       ├── embedded.rb
│   │               │   │   │       ├── embedded_sass_pb.rb
│   │               │   │   │       ├── expand-archive.ps1
│   │               │   │   │       ├── package.json
│   │               │   │   │       └── sass_embedded/
│   │               │   │   │           ├── dart-sass-embedded
│   │               │   │   │           └── src/
│   │               │   │   │               ├── LICENSE
│   │               │   │   │               ├── dart
│   │               │   │   │               └── dart-sass-embedded.snapshot
│   │               │   │   └── lib/
│   │               │   │       ├── sass/
│   │               │   │       │   ├── compile_error.rb
│   │               │   │       │   ├── compile_result.rb
│   │               │   │       │   ├── embedded/
│   │               │   │       │   │   ├── async.rb
│   │               │   │       │   │   ├── channel.rb
│   │               │   │       │   │   ├── compiler.rb
│   │               │   │       │   │   ├── dispatcher.rb
│   │               │   │       │   │   ├── host/
│   │               │   │       │   │   │   ├── function_registry.rb
│   │               │   │       │   │   │   ├── importer_registry.rb
│   │               │   │       │   │   │   ├── logger_registry.rb
│   │               │   │       │   │   │   └── value_protofier.rb
│   │               │   │       │   │   ├── host.rb
│   │               │   │       │   │   ├── protofier.rb
│   │               │   │       │   │   ├── structifier.rb
│   │               │   │       │   │   ├── varint.rb
│   │               │   │       │   │   └── version.rb
│   │               │   │       │   ├── embedded.rb
│   │               │   │       │   ├── logger/
│   │               │   │       │   │   ├── silent.rb
│   │               │   │       │   │   ├── source_location.rb
│   │               │   │       │   │   └── source_span.rb
│   │               │   │       │   ├── script_error.rb
│   │               │   │       │   ├── value/
│   │               │   │       │   │   ├── argument_list.rb
│   │               │   │       │   │   ├── boolean.rb
│   │               │   │       │   │   ├── color.rb
│   │               │   │       │   │   ├── function.rb
│   │               │   │       │   │   ├── fuzzy_math.rb
│   │               │   │       │   │   ├── list.rb
│   │               │   │       │   │   ├── map.rb
│   │               │   │       │   │   ├── null.rb
│   │               │   │       │   │   ├── number/
│   │               │   │       │   │   │   └── unit.rb
│   │               │   │       │   │   ├── number.rb
│   │               │   │       │   │   └── string.rb
│   │               │   │       │   └── value.rb
│   │               │   │       └── sass-embedded.rb
│   │               │   ├── sass-embedded-1.58.3-arm64-darwin/
│   │               │   │   ├── LICENSE
│   │               │   │   ├── README.md
│   │               │   │   ├── ext/
│   │               │   │   │   └── sass/
│   │               │   │   │       ├── embedded.rb
│   │               │   │   │       ├── embedded_sass_pb.rb
│   │               │   │   │       └── sass_embedded/
│   │               │   │   │           ├── dart-sass-embedded
│   │               │   │   │           └── src/
│   │               │   │   │               ├── LICENSE
│   │               │   │   │               ├── dart
│   │               │   │   │               └── dart-sass-embedded.snapshot
│   │               │   │   └── lib/
│   │               │   │       ├── sass/
│   │               │   │       │   ├── compile_error.rb
│   │               │   │       │   ├── compile_result.rb
│   │               │   │       │   ├── embedded/
│   │               │   │       │   │   ├── async.rb
│   │               │   │       │   │   ├── channel.rb
│   │               │   │       │   │   ├── compiler.rb
│   │               │   │       │   │   ├── dispatcher.rb
│   │               │   │       │   │   ├── host/
│   │               │   │       │   │   │   ├── function_registry.rb
│   │               │   │       │   │   │   ├── importer_registry.rb
│   │               │   │       │   │   │   ├── logger_registry.rb
│   │               │   │       │   │   │   └── value_protofier.rb
│   │               │   │       │   │   ├── host.rb
│   │               │   │       │   │   ├── protofier.rb
│   │               │   │       │   │   ├── structifier.rb
│   │               │   │       │   │   ├── varint.rb
│   │               │   │       │   │   └── version.rb
│   │               │   │       │   ├── embedded.rb
│   │               │   │       │   ├── logger/
│   │               │   │       │   │   ├── silent.rb
│   │               │   │       │   │   ├── source_location.rb
│   │               │   │       │   │   └── source_span.rb
│   │               │   │       │   ├── script_error.rb
│   │               │   │       │   ├── value/
│   │               │   │       │   │   ├── argument_list.rb
│   │               │   │       │   │   ├── boolean.rb
│   │               │   │       │   │   ├── color.rb
│   │               │   │       │   │   ├── function.rb
│   │               │   │       │   │   ├── fuzzy_math.rb
│   │               │   │       │   │   ├── list.rb
│   │               │   │       │   │   ├── map.rb
│   │               │   │       │   │   ├── null.rb
│   │               │   │       │   │   ├── number/
│   │               │   │       │   │   │   └── unit.rb
│   │               │   │       │   │   ├── number.rb
│   │               │   │       │   │   └── string.rb
│   │               │   │       │   └── value.rb
│   │               │   │       └── sass-embedded.rb
│   │               │   ├── terminal-table-3.0.2/
│   │               │   │   ├── .github/
│   │               │   │   │   └── workflows/
│   │               │   │   │       └── ci.yml
│   │               │   │   ├── .gitignore
│   │               │   │   ├── Gemfile
│   │               │   │   ├── History.rdoc
│   │               │   │   ├── LICENSE.txt
│   │               │   │   ├── Manifest
│   │               │   │   ├── README.md
│   │               │   │   ├── Rakefile
│   │               │   │   ├── Todo.rdoc
│   │               │   │   ├── examples/
│   │               │   │   │   ├── data.csv
│   │               │   │   │   ├── examples.rb
│   │               │   │   │   ├── examples_unicode.rb
│   │               │   │   │   ├── issue100.rb
│   │               │   │   │   ├── issue111.rb
│   │               │   │   │   ├── issue118.rb
│   │               │   │   │   ├── issue95.rb
│   │               │   │   │   ├── show_csv_table.rb
│   │               │   │   │   └── strong_separator.rb
│   │               │   │   ├── lib/
│   │               │   │   │   ├── terminal-table/
│   │               │   │   │   │   ├── cell.rb
│   │               │   │   │   │   ├── import.rb
│   │               │   │   │   │   ├── row.rb
│   │               │   │   │   │   ├── separator.rb
│   │               │   │   │   │   ├── style.rb
│   │               │   │   │   │   ├── table.rb
│   │               │   │   │   │   ├── table_helper.rb
│   │               │   │   │   │   ├── util.rb
│   │               │   │   │   │   └── version.rb
│   │               │   │   │   └── terminal-table.rb
│   │               │   │   └── terminal-table.gemspec
│   │               │   ├── unicode-display_width-2.6.0/
│   │               │   │   ├── CHANGELOG.md
│   │               │   │   ├── MIT-LICENSE.txt
│   │               │   │   ├── README.md
│   │               │   │   ├── data/
│   │               │   │   │   └── display_width.marshal.gz
│   │               │   │   └── lib/
│   │               │   │       └── unicode/
│   │               │   │           ├── display_width/
│   │               │   │           │   ├── constants.rb
│   │               │   │           │   ├── index.rb
│   │               │   │           │   ├── no_string_ext.rb
│   │               │   │           │   └── string_ext.rb
│   │               │   │           └── display_width.rb
│   │               │   └── webrick-1.9.2/
│   │               │       ├── Gemfile
│   │               │       ├── LICENSE.txt
│   │               │       ├── README.md
│   │               │       ├── Rakefile
│   │               │       ├── lib/
│   │               │       │   ├── webrick/
│   │               │       │   │   ├── accesslog.rb
│   │               │       │   │   ├── cgi.rb
│   │               │       │   │   ├── compat.rb
│   │               │       │   │   ├── config.rb
│   │               │       │   │   ├── cookie.rb
│   │               │       │   │   ├── htmlutils.rb
│   │               │       │   │   ├── httpauth/
│   │               │       │   │   │   ├── authenticator.rb
│   │               │       │   │   │   ├── basicauth.rb
│   │               │       │   │   │   ├── digestauth.rb
│   │               │       │   │   │   ├── htdigest.rb
│   │               │       │   │   │   ├── htgroup.rb
│   │               │       │   │   │   ├── htpasswd.rb
│   │               │       │   │   │   └── userdb.rb
│   │               │       │   │   ├── httpauth.rb
│   │               │       │   │   ├── httpproxy.rb
│   │               │       │   │   ├── httprequest.rb
│   │               │       │   │   ├── httpresponse.rb
│   │               │       │   │   ├── https.rb
│   │               │       │   │   ├── httpserver.rb
│   │               │       │   │   ├── httpservlet/
│   │               │       │   │   │   ├── abstract.rb
│   │               │       │   │   │   ├── cgi_runner.rb
│   │               │       │   │   │   ├── cgihandler.rb
│   │               │       │   │   │   ├── erbhandler.rb
│   │               │       │   │   │   ├── filehandler.rb
│   │               │       │   │   │   └── prochandler.rb
│   │               │       │   │   ├── httpservlet.rb
│   │               │       │   │   ├── httpstatus.rb
│   │               │       │   │   ├── httputils.rb
│   │               │       │   │   ├── httpversion.rb
│   │               │       │   │   ├── log.rb
│   │               │       │   │   ├── server.rb
│   │               │       │   │   ├── ssl.rb
│   │               │       │   │   ├── utils.rb
│   │               │       │   │   └── version.rb
│   │               │       │   └── webrick.rb
│   │               │       ├── sig/
│   │               │       │   ├── accesslog.rbs
│   │               │       │   ├── cgi.rbs
│   │               │       │   ├── compat.rbs
│   │               │       │   ├── config.rbs
│   │               │       │   ├── cookie.rbs
│   │               │       │   ├── htmlutils.rbs
│   │               │       │   ├── httpauth/
│   │               │       │   │   ├── authenticator.rbs
│   │               │       │   │   ├── basicauth.rbs
│   │               │       │   │   ├── digestauth.rbs
│   │               │       │   │   ├── htdigest.rbs
│   │               │       │   │   ├── htgroup.rbs
│   │               │       │   │   ├── htpasswd.rbs
│   │               │       │   │   └── userdb.rbs
│   │               │       │   ├── httpauth.rbs
│   │               │       │   ├── httpproxy.rbs
│   │               │       │   ├── httprequest.rbs
│   │               │       │   ├── httpresponse.rbs
│   │               │       │   ├── https.rbs
│   │               │       │   ├── httpserver.rbs
│   │               │       │   ├── httpservlet/
│   │               │       │   │   ├── abstract.rbs
│   │               │       │   │   ├── cgi_runner.rbs
│   │               │       │   │   ├── cgihandler.rbs
│   │               │       │   │   ├── erbhandler.rbs
│   │               │       │   │   ├── filehandler.rbs
│   │               │       │   │   └── prochandler.rbs
│   │               │       │   ├── httpservlet.rbs
│   │               │       │   ├── httpstatus.rbs
│   │               │       │   ├── httputils.rbs
│   │               │       │   ├── httpversion.rbs
│   │               │       │   ├── log.rbs
│   │               │       │   ├── manifest.yaml
│   │               │       │   ├── server.rbs
│   │               │       │   ├── ssl.rbs
│   │               │       │   ├── utils.rbs
│   │               │       │   └── version.rbs
│   │               │       └── webrick.gemspec
│   │               └── specifications/
│   │                   ├── addressable-2.8.9.gemspec
│   │                   ├── colorator-1.1.0.gemspec
│   │                   ├── concurrent-ruby-1.3.6.gemspec
│   │                   ├── em-websocket-0.5.3.gemspec
│   │                   ├── eventmachine-1.2.7.gemspec
│   │                   ├── ffi-1.17.3.gemspec
│   │                   ├── forwardable-extended-2.6.0.gemspec
│   │                   ├── google-protobuf-3.23.4-arm64-darwin.gemspec
│   │                   ├── http_parser.rb-0.8.1.gemspec
│   │                   ├── i18n-1.14.8.gemspec
│   │                   ├── jekyll-4.3.4.gemspec
│   │                   ├── jekyll-sass-converter-3.0.0.gemspec
│   │                   ├── jekyll-seo-tag-2.8.0.gemspec
│   │                   ├── jekyll-watch-2.2.1.gemspec
│   │                   ├── kramdown-2.5.2.gemspec
│   │                   ├── kramdown-parser-gfm-1.1.0.gemspec
│   │                   ├── liquid-4.0.4.gemspec
│   │                   ├── listen-3.10.0.gemspec
│   │                   ├── logger-1.7.0.gemspec
│   │                   ├── mercenary-0.4.0.gemspec
│   │                   ├── pathutil-0.16.2.gemspec
│   │                   ├── public_suffix-5.1.1.gemspec
│   │                   ├── rake-13.3.1.gemspec
│   │                   ├── rb-fsevent-0.11.2.gemspec
│   │                   ├── rb-inotify-0.11.1.gemspec
│   │                   ├── rexml-3.4.4.gemspec
│   │                   ├── rouge-3.30.0.gemspec
│   │                   ├── safe_yaml-1.0.5.gemspec
│   │                   ├── sass-embedded-1.58.3-arm64-darwin.gemspec
│   │                   ├── sass-embedded-1.58.3.gemspec
│   │                   ├── terminal-table-3.0.2.gemspec
│   │                   ├── unicode-display_width-2.6.0.gemspec
│   │                   └── webrick-1.9.2.gemspec
│   └── workflows/
│       ├── electrical-review/
│       │   └── index.md
│       ├── index.md
│       ├── motor-selection/
│       │   └── index.md
│       ├── motor-troubleshooting/
│       │   └── index.md
│       ├── servo-commissioning/
│       │   └── index.md
│       └── vfd-commissioning/
│           └── index.md
├── lifecycle-build-page.png
├── main.py
├── project_state/
│   ├── change_log.md
│   ├── environment.md
│   ├── how_to.md
│   └── project_state.md
├── pyproject.toml
├── rag -> control-standards/rag
├── tests/
│   ├── __init__.py
│   └── tools/
│       ├── __init__.py
│       └── fe_study/
│           ├── __init__.py
│           ├── test_common.py
│           ├── test_extract_fe_study.py
│           └── test_inventory_fe_study.py
├── tools/
│   ├── README.md
│   ├── fe_study/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── extract_fe_study.py
│   │   ├── inventory_fe_study.py
│   │   ├── quality_check_fe_study.py
│   │   └── summarize_fe_study.py
│   ├── fix_ai_boundaries.py
│   ├── generate_rag_index.py
│   ├── generate_rag_tree.py
│   ├── generate_standards_overview.py
│   ├── project_automator.py
│   ├── setup_hooks.sh
│   ├── validate_ai_boundaries.py
│   └── validate_reorg.sh
└── uv.lock
```
<!-- AUTO-GENERATED TREE END -->
