# Folder Structure Summary

<!-- AUTO-GENERATED TREE START -->
## Directory Tree
**Last Auto-Updated:** 2026-07-20 21:00:46

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
├── .github/
│   └── workflows/
│       └── pages.yml
├── .gitignore
├── .mcp.json
├── .python-version
├── AGENTS.md
├── CLAUDE.md
├── Control System Tools.code-workspace
├── PROJECT_STARTUP_CONTEXT.md
├── README.md
├── STRUCTURE_SUMMARY.md
├── control-standards/
│   ├── .gitignore
│   ├── QUICK_START.md
│   ├── README.md
│   ├── STRUCTURE_SUMMARY.md
│   ├── exports/
│   │   ├── README.md
│   │   └── legacy_root/
│   │       └── README.md
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
│   │   │   └── checklists/
│   │   │       ├── README.md
│   │   │       ├── _index.yaml
│   │   │       ├── basic_circuit_polarity_and_power_checks.md
│   │   │       ├── capacitor_discharge_awareness_check.md
│   │   │       ├── drive_commissioning.md
│   │   │       ├── motor_nameplate_and_overload_setting.md
│   │   │       ├── motor_rotation_and_overload_verification.md
│   │   │       └── pre_power_panel_and_incoming_supply_check.md
│   │   ├── design_framework/
│   │   │   ├── README.md
│   │   │   ├── _index.yaml
│   │   │   ├── ai_integration/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── digital_twin.md
│   │   │   │   ├── interfaces_edge.md
│   │   │   │   ├── methods.yml
│   │   │   │   ├── model_families.md
│   │   │   │   ├── safety_boundary.md
│   │   │   │   ├── sources.yml
│   │   │   │   ├── validation_lifecycle.md
│   │   │   │   └── worked_architectures.md
│   │   │   ├── constraints/
│   │   │   │   └── grounding_bonding_rules.yaml
│   │   │   ├── design_guides/
│   │   │   │   └── 02_power_distribution_guide.md
│   │   │   ├── electrical_review/
│   │   │   │   ├── README.md
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── basic_resistive_network_review.md
│   │   │   │   ├── component_selection_basics.md
│   │   │   │   ├── ohms_law_and_power_check_workflow.md
│   │   │   │   └── simple_signal_and_interface_circuit_notes.md
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
│   │   │   ├── semiconductor_facility/
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── alarm_and_measurement_strategy.md
│   │   │   │   ├── bulk_chemical_distribution.md
│   │   │   │   ├── bulk_specialty_gas.md
│   │   │   │   ├── commissioning_reference.md
│   │   │   │   ├── common_control_philosophy.md
│   │   │   │   ├── device_family_library.md
│   │   │   │   ├── exhaust_abatement_vacuum.md
│   │   │   │   ├── gas_cabinet_control_safety_and_interlocks.md
│   │   │   │   ├── hf_control_safety_and_instrumentation.md
│   │   │   │   ├── hvac_and_cleanroom.md
│   │   │   │   ├── instrumentation_selection.md
│   │   │   │   ├── instrumentation_use_matrix.md
│   │   │   │   ├── safety_and_shutdown.md
│   │   │   │   ├── tool_facility_interface.md
│   │   │   │   ├── upw_and_wastewater.md
│   │   │   │   └── vendor_families.md
│   │   │   ├── us_eu_compliance_wizard/
│   │   │   │   ├── README.md
│   │   │   │   ├── US_EU_Machine_Compliance_Wizard.md
│   │   │   │   ├── us_eu_delta_report_template.md
│   │   │   │   └── us_eu_wizard_rules.yaml
│   │   │   ├── water_wastewater/
│   │   │   │   ├── _index.yaml
│   │   │   │   ├── chemical_dosing.md
│   │   │   │   ├── distribution_scada_telemetry.md
│   │   │   │   ├── equalization_and_neutralization.md
│   │   │   │   ├── filtration_and_clarification.md
│   │   │   │   ├── instrumentation_reference.md
│   │   │   │   ├── intake_and_pumping.md
│   │   │   │   ├── overview_and_standards.md
│   │   │   │   └── treatment_and_discharge.md
│   │   │   └── wiring_practices/
│   │   │       ├── README.md
│   │   │       ├── analog_0_10v_wiring.md
│   │   │       ├── analog_4_20ma_wiring.md
│   │   │       ├── comm_cable_installation.md
│   │   │       ├── control_power_distribution.md
│   │   │       ├── emc_noise_mitigation.md
│   │   │       ├── encoder_wiring.md
│   │   │       ├── ipc_wiring.md
│   │   │       ├── motor_starter_wiring.md
│   │   │       ├── panel_grounding_bonding.md
│   │   │       ├── plc_wiring.md
│   │   │       ├── remote_io_wiring.md
│   │   │       ├── rtd_thermocouple_wiring.md
│   │   │       ├── safety_circuit_wiring.md
│   │   │       ├── servo_drive_wiring.md
│   │   │       ├── vfd_wiring.md
│   │   │       └── wire_sizing_workflow.md
│   │   ├── meta/
│   │   │   ├── RAG_DIRECTORY_STATUS.md
│   │   │   └── VERSION_OVERVIEW.md
│   │   ├── process_safety_details/
│   │   │   ├── IEC61511.md
│   │   │   └── UPW_water_skid_scenario.md
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
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause01__scope.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause02__normative_references.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause03__terms_and_definitions.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause04__general_requirements.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause05__incoming_supply.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause07__protection_of_equipment.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause08__equipotential_bonding.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause10__operator_interface.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause11__controlgear.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause12__conductors_and_cables.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause13__wiring_practices.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause14__electric_motors.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause15__socket_outlets_and_lighting.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause16__marking_and_warning_signs.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause17__technical_documentation.md
│   │   │   │   │       ├── IEC60204_1_2016A1__Clause18__verification.md
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
│   │   │   │   ├── bldc_motor_reference.md
│   │   │   │   ├── bldc_pmsm_implementation_guide.md
│   │   │   │   ├── bldc_pmsm_scenarios.md
│   │   │   │   ├── bldc_vs_pmsm_comparison.md
│   │   │   │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│   │   │   │   ├── dc_motor_basics.md
│   │   │   │   ├── induction_motor_basics.md
│   │   │   │   ├── motor_and_vfd_equations_reference.md
│   │   │   │   ├── motor_control_methods_and_operating_regions.md
│   │   │   │   ├── motor_efficiency_power_factor_and_losses.md
│   │   │   │   ├── motor_family_comparison.md
│   │   │   │   ├── motor_nameplates_slip_and_torque.md
│   │   │   │   ├── pmsm_motor_reference.md
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
│   │   │   ├── plc_software/
│   │   │   │   ├── algorithms_equipment_staging.md
│   │   │   │   ├── ladder_logic.md
│   │   │   │   ├── languages_overview.md
│   │   │   │   ├── packml_isa88_isa95.md
│   │   │   │   ├── program_structure.md
│   │   │   │   ├── safety_application_patterns.md
│   │   │   │   ├── state_machines.md
│   │   │   │   └── vendor_architectures.md
│   │   │   └── semiconductor_facility/
│   │   │       ├── README.md
│   │   │       └── hf_handling_controls_materials_and_shutdowns.md
│   │   └── troubleshooting_engine/
│   │       ├── analog_io/
│   │       │   └── analog_signal_faults.md
│   │       ├── decision_trees.yaml
│   │       ├── motion_drives/
│   │       │   ├── motor_wont_start.md
│   │       │   └── vfd_faults.md
│   │       └── networks/
│   │           └── comms_dropouts.md
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
│   │   │   └── README.md
│   │   ├── business_metrics_profit_engine/
│   │   │   └── README.md
│   │   ├── design_package_generator/
│   │   │   └── README.md
│   │   ├── ip_library_licensing/
│   │   │   └── README.md
│   │   ├── knowledge_platform/
│   │   │   └── README.md
│   │   ├── retainer_support_engine/
│   │   │   └── README.md
│   │   └── ul508a_panel_automation/
│   │       └── README.md
│   └── work/
│       ├── README.md
│       ├── design/
│       │   ├── README.md
│       │   ├── conductor_protection_and_ampacity_transcript_summary.md
│       │   ├── control theory.md
│       │   ├── equipment_grounding_conductor_topics/
│       │   │   ├── README.md
│       │   │   ├── egc_cable_methods_ac_and_mc.md
│       │   │   ├── egc_definition_and_effective_fault_path.md
│       │   │   ├── egc_other_listed_systems.md
│       │   │   ├── egc_sizing_and_250_122_notes.md
│       │   │   └── egc_wire_and_raceway_methods.md
│       │   ├── mermaid_diagrams_to_reference.md
│       │   ├── nec_2026_changes_topics/
│       │   │   ├── 2026_nec_codewide_editorial_and_90_3_changes.md
│       │   │   ├── 2026_nec_limited_energy_restructure.md
│       │   │   ├── 2026_nec_medium_voltage_restructure.md
│       │   │   ├── 2026_nec_new_and_relocated_articles.md
│       │   │   ├── 2026_nec_overview_and_2029_transition.md
│       │   │   └── README.md
│       │   ├── nec_210_4_multiwire_branch_circuits_transcript_summary.md
│       │   ├── project_implementation_gaps/
│       │   │   ├── 20260308_status.md
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
│       │   │   └── nec_exam_prep_topics/
│       │   │       ├── INTEGRATION_PLAN.md
│       │   │       ├── README.md
│       │   │       ├── electrical_exam_math_ohms_law_and_power.md
│       │   │       ├── nec_code_reading_and_index_method.md
│       │   │       ├── nec_table_reading_and_working_space_example.md
│       │   │       └── residential_load_calculation_notes.md
│       │   ├── residential_nec_top_articles_transcript_summary.md
│       │   ├── scratch_notes/
│       │   │   └── simple_safety_system_design.md
│       │   ├── types of equipment ground conductors.md
│       │   ├── types of grounding.md
│       │   ├── ul508_spacing.md
│       │   └── voltage_drop_topics/
│       │       ├── README.md
│       │       ├── voltage_drop_energy_code_and_specifications.md
│       │       ├── voltage_drop_fire_pump_notes.md
│       │       ├── voltage_drop_general_basis.md
│       │       └── voltage_drop_recommended_feeder_and_branch_guidance.md
│       ├── general/
│       │   ├── 00_inbox_notes.md
│       │   ├── README.md
│       │   ├── plc_ipc_hardware_intake_2026-07.md
│       │   └── plc_software_intake_2026-07.md
│       └── research/
│           └── ai-ml-control-systems/
│               ├── 49a-findings.md
│               ├── 49c-findings.md
│               ├── 49d-findings.md
│               ├── README.md
│               ├── adversarial-verdicts.md
│               ├── authority-ceilings.md
│               ├── digital-twin-integration.md
│               ├── evidence-table.md
│               ├── research-map.md
│               ├── scientific-domain-integration.md
│               └── source-register.md
├── control-theory-final.png
├── control-theory-mobile-top.png
├── control-theory-overview-full.png
├── data/
│   ├── README.md
│   ├── examples/
│   │   ├── io_list_example.csv
│   │   ├── twin_payload_example.json
│   │   └── twin_sync_example.csv
│   └── standards_tables/
│       ├── README.md
│       ├── samples/
│       │   ├── ampacity_nec_310_16.json
│       │   └── motor_flc_nec_430_250.json
│       └── schemas/
│           ├── ampacity.schema.json
│           └── motor_flc.schema.json
├── docs/
│   ├── .bundle/
│   │   └── config
│   ├── Gemfile
│   ├── Gemfile.lock
│   ├── _config.yml
│   ├── _data/
│   │   ├── ai_methods/
│   │   │   ├── methods.yml
│   │   │   └── sources.yml
│   │   ├── field_checklists.yml
│   │   ├── glossary.yml
│   │   ├── lifecycle_stage_urls.yml
│   │   ├── lifecycle_stages.yml
│   │   ├── manufacturers/
│   │   │   ├── plc_hardware_families.yml
│   │   │   ├── plc_pac.yml
│   │   │   ├── process_instrumentation.yml
│   │   │   ├── scada_hmi.yml
│   │   │   ├── servo_motion.yml
│   │   │   ├── vendor_doc_links.yml
│   │   │   └── vfd.yml
│   │   ├── navigation.yml
│   │   ├── phase26_migration_map.yml
│   │   ├── rag_tree.json
│   │   ├── standards_graph.yml
│   │   └── training_catalog.yml
│   ├── _includes/
│   │   ├── context-panel.html
│   │   ├── rag-tree-nodes.html
│   │   ├── review-meta.html
│   │   ├── sidebar-global.html
│   │   ├── sidebar-section-local.html
│   │   ├── sidebar-training-group.html
│   │   ├── sidebar.html
│   │   ├── stage-nav.html
│   │   ├── standards-graph.html
│   │   ├── topnav.html
│   │   └── trust-boundary.html
│   ├── _layouts/
│   │   ├── default.html
│   │   ├── field-checklist.html
│   │   ├── home.html
│   │   ├── rag-browser.html
│   │   └── training-module.html
│   ├── about/
│   │   └── index.md
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── data/
│   │   │   └── search.json
│   │   ├── images/
│   │   │   ├── design-package/
│   │   │   │   └── control-system-design-package-example.png
│   │   │   └── wire-color-coding/
│   │   │       ├── 00-wire-color-coding-title-banner.png
│   │   │       ├── 01-reference-standards.png
│   │   │       ├── 02-nfpa79-machinery-panel-us.png
│   │   │       ├── 03-iec60204-machinery-panel.png
│   │   │       ├── 04-us-facility-power-distribution.png
│   │   │       ├── 05-plc-24vdc-io-wiring.png
│   │   │       ├── 06-120vac-control-circuit.png
│   │   │       ├── 07-4-20ma-transmitter-hookup.png
│   │   │       ├── 08-intrinsically-safe-wiring.png
│   │   │       ├── 09-vfd-to-motor-wiring.png
│   │   │       ├── 10-servo-motion-system-wiring.png
│   │   │       ├── 11-hvac-building-automation.png
│   │   │       ├── 12-semiconductor-facility-color-map.png
│   │   │       ├── 13-industrial-ethernet-cable-identification.png
│   │   │       ├── 15-important-wiring-notes.png
│   │   │       └── 16-symbol-legend.png
│   │   ├── img/
│   │   │   └── favicon.svg
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   └── rag-browser.js
│   │   ├── rag-files/
│   │   │   ├── commissioning_checklists/
│   │   │   │   └── checklists/
│   │   │   │       ├── basic_circuit_polarity_and_power_checks.md
│   │   │   │       ├── capacitor_discharge_awareness_check.md
│   │   │   │       ├── drive_commissioning.md
│   │   │   │       ├── motor_nameplate_and_overload_setting.md
│   │   │   │       ├── motor_rotation_and_overload_verification.md
│   │   │   │       └── pre_power_panel_and_incoming_supply_check.md
│   │   │   ├── design_framework/
│   │   │   │   ├── ai_integration/
│   │   │   │   │   ├── digital_twin.md
│   │   │   │   │   ├── interfaces_edge.md
│   │   │   │   │   ├── model_families.md
│   │   │   │   │   ├── safety_boundary.md
│   │   │   │   │   ├── validation_lifecycle.md
│   │   │   │   │   └── worked_architectures.md
│   │   │   │   ├── design_guides/
│   │   │   │   │   └── 02_power_distribution_guide.md
│   │   │   │   ├── electrical_review/
│   │   │   │   │   ├── basic_resistive_network_review.md
│   │   │   │   │   ├── component_selection_basics.md
│   │   │   │   │   ├── ohms_law_and_power_check_workflow.md
│   │   │   │   │   └── simple_signal_and_interface_circuit_notes.md
│   │   │   │   ├── motor_systems/
│   │   │   │   │   ├── industrial_vs_ev_vs_drone_motor_drive_standards_matrix.md
│   │   │   │   │   ├── integrated_drive_failure_modes_and_tradeoffs.md
│   │   │   │   │   ├── integrated_drive_serviceability_and_field_replacement_review.md
│   │   │   │   │   ├── integrated_motor_drive_architecture_comparison.md
│   │   │   │   │   ├── motor_cable_and_protection_review.md
│   │   │   │   │   ├── motor_mounted_drive_thermal_and_emc_design_notes.md
│   │   │   │   │   ├── motor_nameplate_review_checklist.md
│   │   │   │   │   ├── motor_selection_comparison_matrix.md
│   │   │   │   │   ├── motor_selection_workflow.md
│   │   │   │   │   ├── motor_symptom_troubleshooting_patterns.md
│   │   │   │   │   ├── motor_troubleshooting_decision_tree.md
│   │   │   │   │   ├── servo_commissioning_workflow.md
│   │   │   │   │   ├── star_delta_and_supply_matching_notes.md
│   │   │   │   │   ├── vfd_commissioning_workflow.md
│   │   │   │   │   └── vfd_motor_integration_review.md
│   │   │   │   ├── semiconductor_facility/
│   │   │   │   │   ├── alarm_and_measurement_strategy.md
│   │   │   │   │   ├── bulk_chemical_distribution.md
│   │   │   │   │   ├── bulk_specialty_gas.md
│   │   │   │   │   ├── commissioning_reference.md
│   │   │   │   │   ├── common_control_philosophy.md
│   │   │   │   │   ├── device_family_library.md
│   │   │   │   │   ├── exhaust_abatement_vacuum.md
│   │   │   │   │   ├── gas_cabinet_control_safety_and_interlocks.md
│   │   │   │   │   ├── hf_control_safety_and_instrumentation.md
│   │   │   │   │   ├── hvac_and_cleanroom.md
│   │   │   │   │   ├── instrumentation_selection.md
│   │   │   │   │   ├── instrumentation_use_matrix.md
│   │   │   │   │   ├── safety_and_shutdown.md
│   │   │   │   │   ├── tool_facility_interface.md
│   │   │   │   │   ├── upw_and_wastewater.md
│   │   │   │   │   └── vendor_families.md
│   │   │   │   ├── us_eu_compliance_wizard/
│   │   │   │   │   ├── US_EU_Machine_Compliance_Wizard.md
│   │   │   │   │   └── us_eu_delta_report_template.md
│   │   │   │   ├── water_wastewater/
│   │   │   │   │   ├── chemical_dosing.md
│   │   │   │   │   ├── distribution_scada_telemetry.md
│   │   │   │   │   ├── equalization_and_neutralization.md
│   │   │   │   │   ├── filtration_and_clarification.md
│   │   │   │   │   ├── instrumentation_reference.md
│   │   │   │   │   ├── intake_and_pumping.md
│   │   │   │   │   ├── overview_and_standards.md
│   │   │   │   │   └── treatment_and_discharge.md
│   │   │   │   └── wiring_practices/
│   │   │   │       ├── analog_0_10v_wiring.md
│   │   │   │       ├── analog_4_20ma_wiring.md
│   │   │   │       ├── comm_cable_installation.md
│   │   │   │       ├── control_power_distribution.md
│   │   │   │       ├── emc_noise_mitigation.md
│   │   │   │       ├── encoder_wiring.md
│   │   │   │       ├── ipc_wiring.md
│   │   │   │       ├── motor_starter_wiring.md
│   │   │   │       ├── panel_grounding_bonding.md
│   │   │   │       ├── plc_wiring.md
│   │   │   │       ├── remote_io_wiring.md
│   │   │   │       ├── rtd_thermocouple_wiring.md
│   │   │   │       ├── safety_circuit_wiring.md
│   │   │   │       ├── servo_drive_wiring.md
│   │   │   │       ├── vfd_wiring.md
│   │   │   │       └── wire_sizing_workflow.md
│   │   │   ├── meta/
│   │   │   │   ├── RAG_DIRECTORY_STATUS.md
│   │   │   │   └── VERSION_OVERVIEW.md
│   │   │   ├── process_safety_details/
│   │   │   │   ├── IEC61511.md
│   │   │   │   └── UPW_water_skid_scenario.md
│   │   │   ├── standards_intelligence/
│   │   │   │   ├── _glossary.md
│   │   │   │   ├── _standards_map.md
│   │   │   │   ├── crosswalks/
│   │   │   │   │   ├── overlap_matrix/
│   │   │   │   │   │   ├── file_structure.md
│   │   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │   │   │   │   ├── standards_decision_workflow.md
│   │   │   │   │   │   ├── standards_overlap.md
│   │   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │   │   │   └── overlap_notes/
│   │   │   │   │       ├── GENERATION_STATUS.md
│   │   │   │   │       ├── file_structure.md
│   │   │   │   │       ├── overlap__motors_drives.md
│   │   │   │   │       ├── overlap__sccr.md
│   │   │   │   │       └── overlap_nfpa79_iec60204__motors_drives.md
│   │   │   │   ├── file_structure.md
│   │   │   │   ├── international/
│   │   │   │   │   ├── cybersecurity/
│   │   │   │   │   │   └── iec_62443/
│   │   │   │   │   │       ├── IEC62443_2_1__security_management.md
│   │   │   │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│   │   │   │   │   │       ├── IEC62443_4_2__component_requirements.md
│   │   │   │   │   │       └── IEC62443_lifecycle.md
│   │   │   │   │   ├── functional_safety/
│   │   │   │   │   │   ├── iec_61508/
│   │   │   │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│   │   │   │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│   │   │   │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│   │   │   │   │   │   │   └── IEC61508_2010__Part3__software.md
│   │   │   │   │   │   ├── iec_61511/
│   │   │   │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│   │   │   │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│   │   │   │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│   │   │   │   │   │   │   └── IEC61511_2016__Part1__framework.md
│   │   │   │   │   │   ├── iec_62061/
│   │   │   │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│   │   │   │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│   │   │   │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│   │   │   │   │   │   │   └── IEC62061_2021__Clause07__subsystem_design.md
│   │   │   │   │   │   ├── iso_12100/
│   │   │   │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│   │   │   │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│   │   │   │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│   │   │   │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│   │   │   │   │   │   │   └── ISO12100_2010__Clause07__risk_reduction.md
│   │   │   │   │   │   └── iso_13849_1/
│   │   │   │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│   │   │   │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│   │   │   │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│   │   │   │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│   │   │   │   │   │       ├── ISO13849_2023__Clause06__categories.md
│   │   │   │   │   │       └── ISO13849_2023__Clause07__validation.md
│   │   │   │   │   ├── hazardous_area/
│   │   │   │   │   │   └── iec_60079/
│   │   │   │   │   │       ├── IEC60079_0__general_requirements.md
│   │   │   │   │   │       ├── IEC60079_10_1__area_classification_gas.md
│   │   │   │   │   │       ├── IEC60079_11__intrinsically_safe_Ex_i.md
│   │   │   │   │   │       ├── IEC60079_14__installation_design.md
│   │   │   │   │   │       ├── IEC60079_17__inspection_maintenance.md
│   │   │   │   │   │       └── IEC60079_1__flameproof_Ex_d.md
│   │   │   │   │   ├── machinery/
│   │   │   │   │   │   └── iec_60204_1/
│   │   │   │   │   │       ├── GENERATION_SUMMARY.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause01__scope.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause02__normative_references.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause03__terms_and_definitions.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause04__general_requirements.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause05__incoming_supply.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause07__protection_of_equipment.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause08__equipotential_bonding.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause10__operator_interface.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause11__controlgear.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause12__conductors_and_cables.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause13__wiring_practices.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause14__electric_motors.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause15__socket_outlets_and_lighting.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause16__marking_and_warning_signs.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause17__technical_documentation.md
│   │   │   │   │   │       ├── IEC60204_1_2016A1__Clause18__verification.md
│   │   │   │   │   │       └── IEC60204_OVERVIEW.md
│   │   │   │   │   ├── offshore/
│   │   │   │   │   │   ├── ABS_offshore_electrical_control.md
│   │   │   │   │   │   └── DNV_OS_D201__electrical_installations.md
│   │   │   │   │   └── semiconductor/
│   │   │   │   │       └── semi/
│   │   │   │   │           ├── SEMI_S14__fire_risk_assessment.md
│   │   │   │   │           ├── SEMI_S2__equipment_safety.md
│   │   │   │   │           └── SEMI_S8__ergonomics.md
│   │   │   │   ├── library_admin/
│   │   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │   │   │   ├── STANDARDS_COMPLETION_STATUS.md
│   │   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │   │   │   └── STANDARDS_PURCHASE_TRACKER.md
│   │   │   │   ├── reference_models/
│   │   │   │   │   ├── 15-Standard Minimum Compliance Stack.md
│   │   │   │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│   │   │   │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│   │   │   │   │   ├── Universal Machine Safety Architecture.md
│   │   │   │   │   └── standards_atlas_diagrams_reference.md
│   │   │   │   ├── routing/
│   │   │   │   │   └── standards_applicability.md
│   │   │   │   ├── scenario/
│   │   │   │   │   ├── cnc_machine_safety_design/
│   │   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   │   ├── system_description.md
│   │   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   │   ├── mini_machine_safety_design/
│   │   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   │   ├── industry_overlays/
│   │   │   │   │   │   │   ├── commercial.md
│   │   │   │   │   │   │   ├── energy.md
│   │   │   │   │   │   │   ├── food_and_beverage.md
│   │   │   │   │   │   │   ├── marine.md
│   │   │   │   │   │   │   ├── medical.md
│   │   │   │   │   │   │   ├── nuclear.md
│   │   │   │   │   │   │   ├── offshore.md
│   │   │   │   │   │   │   ├── petroleum.md
│   │   │   │   │   │   │   └── semiconductor.md
│   │   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   │   ├── system_description.md
│   │   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   │   └── mini_machine_safety_design_v2/
│   │   │   │   │       ├── control_architecture_and_network.md
│   │   │   │   │       ├── hazards_and_risk_assessment.md
│   │   │   │   │       ├── industry_overlays/
│   │   │   │   │       │   ├── commercial.md
│   │   │   │   │       │   ├── energy.md
│   │   │   │   │       │   ├── food_and_beverage.md
│   │   │   │   │       │   ├── marine.md
│   │   │   │   │       │   ├── medical.md
│   │   │   │   │       │   ├── nuclear.md
│   │   │   │   │       │   ├── offshore.md
│   │   │   │   │       │   ├── petroleum.md
│   │   │   │   │       │   └── semiconductor.md
│   │   │   │   │       ├── mechanical_and_electrical_isolation.md
│   │   │   │   │       ├── safety_functions_register.md
│   │   │   │   │       ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │       ├── standards_applicability_matrix.md
│   │   │   │   │       ├── system_description.md
│   │   │   │   │       ├── ul_nec_design_requirements.md
│   │   │   │   │       └── verification_and_validation_plan.md
│   │   │   │   └── us/
│   │   │   │       ├── nec/
│   │   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │   │       │   ├── NEC_2023__Art090__scope_and_purpose.md
│   │   │   │       │   ├── NEC_2023__Art100__definitions.md
│   │   │   │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │   │       │   ├── NEC_2023__Art215__feeders.md
│   │   │   │       │   ├── NEC_2023__Art230__services.md
│   │   │   │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │   │       │   ├── NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md
│   │   │   │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │   │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │   │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │   │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │   │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │   │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │   │       │   ├── NEC_2023__Art500__hazardous_locations_general.md
│   │   │   │       │   ├── NEC_2023__Art504__intrinsically_safe_systems.md
│   │   │   │       │   ├── NEC_2023__Art505__zone_0_1_2_gas_vapors.md
│   │   │   │       │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │   │       │   ├── NEC_2023__Art700_702__emergency_standby_systems.md
│   │   │   │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │   │       │   ├── NEC_COMPLETION_STATUS.md
│   │   │   │       │   └── NEC_OVERVIEW.md
│   │   │   │       ├── nfpa79/
│   │   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │   │       │   ├── NFPA79_2024__Ch01__administration.md
│   │   │   │       │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │   │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │   │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │   │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │   │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │   │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │   │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │   │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │   │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │   │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │   │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │   │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │   │       │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │   │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │   │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │   │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │   │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │   │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │   │       │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │   │       │   └── NFPA_OVERVIEW.md
│   │   │   │       └── ul_508a/
│   │   │   │           ├── GENERATION_SUMMARY.md
│   │   │   │           ├── UL508A_2022__control_circuits_and_devices.md
│   │   │   │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │   │           ├── UL508A_2022__general_construction_requirements.md
│   │   │   │           ├── UL508A_2022__grounding_and_bonding.md
│   │   │   │           ├── UL508A_2022__marking_and_documentation.md
│   │   │   │           ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │   │           ├── UL508A_2022__overcurrent_protection.md
│   │   │   │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │   │           ├── UL508A_2022__scope_and_application.md
│   │   │   │           ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │   │           ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │   │           ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │   │           └── UL508A_OVERVIEW.md
│   │   │   ├── training_modules/
│   │   │   │   ├── control_systems/
│   │   │   │   │   ├── control_theory_overview.md
│   │   │   │   │   ├── industrial_control_loop_architectures.md
│   │   │   │   │   ├── industrial_pid_implementation.md
│   │   │   │   │   ├── pid_control_intuition.md
│   │   │   │   │   ├── pid_control_intuitive_foundation.md
│   │   │   │   │   ├── pid_drone_control.md
│   │   │   │   │   └── pid_heater_control_with_contactor.md
│   │   │   │   ├── electrical_machines/
│   │   │   │   │   ├── ac_vs_dc_motor_comparison.md
│   │   │   │   │   ├── bldc_motor_reference.md
│   │   │   │   │   ├── bldc_pmsm_implementation_guide.md
│   │   │   │   │   ├── bldc_pmsm_scenarios.md
│   │   │   │   │   ├── bldc_vs_pmsm_comparison.md
│   │   │   │   │   ├── brushless_dc_ev_and_drone_motor_comparison.md
│   │   │   │   │   ├── dc_motor_basics.md
│   │   │   │   │   ├── induction_motor_basics.md
│   │   │   │   │   ├── motor_and_vfd_equations_reference.md
│   │   │   │   │   ├── motor_control_methods_and_operating_regions.md
│   │   │   │   │   ├── motor_efficiency_power_factor_and_losses.md
│   │   │   │   │   ├── motor_family_comparison.md
│   │   │   │   │   ├── motor_nameplates_slip_and_torque.md
│   │   │   │   │   ├── pmsm_motor_reference.md
│   │   │   │   │   ├── servo_drive_fundamentals.md
│   │   │   │   │   ├── servo_feedback_and_inertia_matching.md
│   │   │   │   │   ├── vfd_and_servo_architecture_diagrams.md
│   │   │   │   │   └── vfd_fundamentals.md
│   │   │   │   ├── fundamentals/
│   │   │   │   │   ├── conductor_ampacity_and_termination_temperature.md
│   │   │   │   │   ├── diodes_transistors_and_switching_basics.md
│   │   │   │   │   ├── earthing_systems_iec.md
│   │   │   │   │   ├── electrical_equations_reference.md
│   │   │   │   │   ├── electrical_quantities_and_circuit_language.md
│   │   │   │   │   ├── equivalent_circuit_methods.md
│   │   │   │   │   ├── kirchhoff_laws_and_systematic_analysis.md
│   │   │   │   │   ├── passive_components_resistors_capacitors.md
│   │   │   │   │   └── series_parallel_and_divider_methods.md
│   │   │   │   ├── nec_application/
│   │   │   │   │   ├── article_409_practical_workflow.md
│   │   │   │   │   ├── article_430_practical_workflow.md
│   │   │   │   │   ├── branch_circuits_vs_feeders_motor_loads.md
│   │   │   │   │   ├── class1_class2_remote_control_circuits.md
│   │   │   │   │   ├── conductor_ocpd_sizing_examples.md
│   │   │   │   │   ├── disconnecting_means_for_machinery.md
│   │   │   │   │   ├── grounding_bonding_control_panels.md
│   │   │   │   │   ├── motor_and_panel_code_application.md
│   │   │   │   │   ├── nec_code_reading_fundamentals.md
│   │   │   │   │   ├── sccr_workflow.md
│   │   │   │   │   └── working_space_and_table_navigation.md
│   │   │   │   ├── plc_software/
│   │   │   │   │   ├── algorithms_equipment_staging.md
│   │   │   │   │   ├── ladder_logic.md
│   │   │   │   │   ├── languages_overview.md
│   │   │   │   │   ├── packml_isa88_isa95.md
│   │   │   │   │   ├── program_structure.md
│   │   │   │   │   ├── safety_application_patterns.md
│   │   │   │   │   ├── state_machines.md
│   │   │   │   │   └── vendor_architectures.md
│   │   │   │   └── semiconductor_facility/
│   │   │   │       └── hf_handling_controls_materials_and_shutdowns.md
│   │   │   └── troubleshooting_engine/
│   │   │       ├── analog_io/
│   │   │       │   └── analog_signal_faults.md
│   │   │       ├── motion_drives/
│   │   │       │   ├── motor_wont_start.md
│   │   │       │   └── vfd_faults.md
│   │   │       └── networks/
│   │   │           └── comms_dropouts.md
│   │   └── templates/
│   │       ├── ai_model_evidence_ledger.md
│   │       ├── alarm_rationalization.csv
│   │       ├── bom_example.csv
│   │       ├── cause_and_effect_matrix.csv
│   │       ├── commissioning_punch_list.csv
│   │       ├── control_narrative.md
│   │       ├── controls_design_basis.md
│   │       ├── cybersecurity_asset_inventory.csv
│   │       ├── design_package_example.md
│   │       ├── device_firmware_inventory.csv
│   │       ├── electrical_drawing_review_checklist.md
│   │       ├── fat_protocol_example.md
│   │       ├── firewall_comm_matrix.csv
│   │       ├── instrument_index.csv
│   │       ├── io_list_example.csv
│   │       ├── ip_address_register.csv
│   │       ├── legend_plates_example.csv
│   │       ├── loop_sheet_example.md
│   │       ├── management_of_change_form.md
│   │       ├── network_baseline_capture_log.csv
│   │       ├── safety_requirements_spec.md
│   │       ├── standards_applicability_register.csv
│   │       ├── switch_port_schedule.csv
│   │       ├── test_instrument_record.csv
│   │       ├── twin_data_contract.schema.json
│   │       ├── twin_payload_example.json
│   │       ├── vlan_register.csv
│   │       └── wire_schedule_example.csv
│   ├── communications/
│   │   ├── bacnet-ip/
│   │   │   └── index.md
│   │   ├── case-study-intermittent-io/
│   │   │   └── index.md
│   │   ├── copper-ethernet/
│   │   │   └── index.md
│   │   ├── dnp3/
│   │   │   └── index.md
│   │   ├── ethercat/
│   │   │   └── index.md
│   │   ├── ethernet-fundamentals/
│   │   │   └── index.md
│   │   ├── ethernet-ip/
│   │   │   └── index.md
│   │   ├── fiber-optics/
│   │   │   └── index.md
│   │   ├── hart/
│   │   │   └── index.md
│   │   ├── iec-61850/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── io-link/
│   │   │   └── index.md
│   │   ├── managed-switches/
│   │   │   └── index.md
│   │   ├── modbus-rtu-rs485/
│   │   │   └── index.md
│   │   ├── modbus-tcp/
│   │   │   └── index.md
│   │   ├── opc-ua/
│   │   │   └── index.md
│   │   ├── packet-capture-methods/
│   │   │   └── index.md
│   │   ├── profibus-dp/
│   │   │   └── index.md
│   │   ├── profinet/
│   │   │   └── index.md
│   │   ├── rs485-physical-layer/
│   │   │   └── index.md
│   │   ├── wireshark-fundamentals/
│   │   │   └── index.md
│   │   └── wireshark-methodology/
│   │       └── index.md
│   ├── design/
│   │   ├── ai-integration/
│   │   │   ├── digital-twin/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── interfaces/
│   │   │   │   └── index.md
│   │   │   ├── method-register/
│   │   │   │   └── index.md
│   │   │   ├── model-families/
│   │   │   │   └── index.md
│   │   │   ├── safety-boundaries/
│   │   │   │   └── index.md
│   │   │   ├── validation-lifecycle/
│   │   │   │   └── index.md
│   │   │   └── worked-architectures/
│   │   │       └── index.md
│   │   ├── architecture/
│   │   │   ├── compliance-stack/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── machine-architecture-model/
│   │   │   │   └── index.md
│   │   │   └── machine-safety-architecture/
│   │   │       └── index.md
│   │   ├── index.md
│   │   ├── motor-selection/
│   │   │   ├── index.md
│   │   │   └── motor-selection-matrix/
│   │   │       └── index.md
│   │   ├── software-stack/
│   │   │   └── index.md
│   │   ├── wiring/
│   │   │   ├── analog-0-10v/
│   │   │   │   └── index.md
│   │   │   ├── analog-4-20ma/
│   │   │   │   └── index.md
│   │   │   ├── comm-cable/
│   │   │   │   └── index.md
│   │   │   ├── control-power/
│   │   │   │   └── index.md
│   │   │   ├── emc-noise-mitigation/
│   │   │   │   └── index.md
│   │   │   ├── encoder/
│   │   │   │   └── index.md
│   │   │   ├── grounding-bonding/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── ipc/
│   │   │   │   └── index.md
│   │   │   ├── motor-starter/
│   │   │   │   └── index.md
│   │   │   ├── plc/
│   │   │   │   └── index.md
│   │   │   ├── remote-io/
│   │   │   │   └── index.md
│   │   │   ├── rtd-thermocouple/
│   │   │   │   └── index.md
│   │   │   ├── safety-circuit/
│   │   │   │   └── index.md
│   │   │   ├── servo-drive/
│   │   │   │   └── index.md
│   │   │   ├── vfd/
│   │   │   │   └── index.md
│   │   │   ├── wire-color-coding/
│   │   │   │   └── index.md
│   │   │   └── wire-sizing/
│   │   │       └── index.md
│   │   └── workflows/
│   │       ├── electrical-review/
│   │       │   └── index.md
│   │       ├── index.md
│   │       └── motor-selection/
│   │           └── index.md
│   ├── field-engineering/
│   │   └── index.md
│   ├── fundamentals/
│   │   ├── control/
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
│   │   ├── electrical/
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
│   │   ├── motors/
│   │   │   ├── ac-vs-dc-motors/
│   │   │   │   └── index.md
│   │   │   ├── bldc-ev-drone-motors/
│   │   │   │   └── index.md
│   │   │   ├── bldc-pmsm-implementation/
│   │   │   │   └── index.md
│   │   │   ├── bldc-reference/
│   │   │   │   └── index.md
│   │   │   ├── bldc-vs-pmsm/
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
│   │   │   ├── motor-selection-scenarios/
│   │   │   │   └── index.md
│   │   │   ├── motor-vfd-equations/
│   │   │   │   └── index.md
│   │   │   ├── pmsm-reference/
│   │   │   │   └── index.md
│   │   │   ├── servo-drive-fundamentals/
│   │   │   │   └── index.md
│   │   │   ├── servo-feedback-inertia/
│   │   │   │   └── index.md
│   │   │   ├── vfd-fundamentals/
│   │   │   │   └── index.md
│   │   │   └── vfd-servo-architecture/
│   │   │       └── index.md
│   │   ├── nec-application/
│   │   │   ├── article-409-workflow/
│   │   │   │   └── index.md
│   │   │   ├── article-430-workflow/
│   │   │   │   └── index.md
│   │   │   ├── branch-circuits-vs-feeders/
│   │   │   │   └── index.md
│   │   │   ├── class1-class2-circuits/
│   │   │   │   └── index.md
│   │   │   ├── conductor-ocpd-sizing/
│   │   │   │   └── index.md
│   │   │   ├── disconnecting-means/
│   │   │   │   └── index.md
│   │   │   ├── grounding-bonding-panels/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── motor-panel-code-application/
│   │   │   │   └── index.md
│   │   │   ├── nec-code-reading/
│   │   │   │   └── index.md
│   │   │   ├── sccr-workflow/
│   │   │   │   └── index.md
│   │   │   └── working-space-table-navigation/
│   │   │       └── index.md
│   │   └── plc-software/
│   │       ├── algorithms-equipment-staging/
│   │       │   └── index.md
│   │       ├── index.md
│   │       ├── ladder-logic/
│   │       │   └── index.md
│   │       ├── languages-overview/
│   │       │   └── index.md
│   │       ├── packml-isa88-isa95/
│   │       │   └── index.md
│   │       ├── program-structure/
│   │       │   └── index.md
│   │       ├── safety-application-patterns/
│   │       │   └── index.md
│   │       ├── state-machines/
│   │       │   └── index.md
│   │       └── vendor-architectures/
│   │           └── index.md
│   ├── implementation/
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
│   │   ├── semiconductor/
│   │   │   ├── facility/
│   │   │   │   ├── bulk-chemical/
│   │   │   │   │   └── index.md
│   │   │   │   ├── bulk-specialty-gas/
│   │   │   │   │   └── index.md
│   │   │   │   ├── commissioning/
│   │   │   │   │   └── index.md
│   │   │   │   ├── control-philosophy/
│   │   │   │   │   └── index.md
│   │   │   │   ├── crosswalks/
│   │   │   │   │   └── index.md
│   │   │   │   ├── exhaust-abatement/
│   │   │   │   │   └── index.md
│   │   │   │   ├── gas-cabinet/
│   │   │   │   │   └── index.md
│   │   │   │   ├── hvac-cleanroom/
│   │   │   │   │   └── index.md
│   │   │   │   ├── index.md
│   │   │   │   ├── instrumentation/
│   │   │   │   │   ├── alarm-strategy/
│   │   │   │   │   │   └── index.md
│   │   │   │   │   ├── device-families/
│   │   │   │   │   │   └── index.md
│   │   │   │   │   ├── index.md
│   │   │   │   │   └── vendor-families/
│   │   │   │   │       └── index.md
│   │   │   │   ├── safety-shutdown/
│   │   │   │   │   └── index.md
│   │   │   │   ├── tool-facility-interface/
│   │   │   │   │   └── index.md
│   │   │   │   └── upw-wastewater/
│   │   │   │       └── index.md
│   │   │   └── index.md
│   │   └── water-wastewater/
│   │       ├── chemical-dosing/
│   │       │   └── index.md
│   │       ├── distribution-scada/
│   │       │   └── index.md
│   │       ├── equalization-neutralization/
│   │       │   └── index.md
│   │       ├── filtration-clarification/
│   │       │   └── index.md
│   │       ├── index.md
│   │       ├── instrumentation/
│   │       │   └── index.md
│   │       ├── intake-pumping/
│   │       │   └── index.md
│   │       └── treatment-discharge/
│   │           └── index.md
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
│   │   ├── general/
│   │   │   └── index.md
│   │   ├── guides/
│   │   │   ├── commissioning-templates/
│   │   │   │   ├── basic-circuit-polarity/
│   │   │   │   │   └── index.md
│   │   │   │   ├── capacitor-discharge/
│   │   │   │   │   └── index.md
│   │   │   │   ├── drive-commissioning/
│   │   │   │   │   └── index.md
│   │   │   │   ├── index.md
│   │   │   │   ├── motor-nameplate-overload/
│   │   │   │   │   └── index.md
│   │   │   │   ├── motor-rotation-verification/
│   │   │   │   │   └── index.md
│   │   │   │   └── pre-power-panel/
│   │   │   │       └── index.md
│   │   │   ├── servo-commissioning/
│   │   │   │   └── index.md
│   │   │   └── vfd-commissioning/
│   │   │       └── index.md
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
│   │   ├── 2026-03-13-phase19-engineering-workflow-navigation.md
│   │   └── 2026-04-20-phase27-motors-bldc-pmsm-implementation.md
│   ├── repository/
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
│   │   │   ├── 2026-04-11-phase23-facility-build-phases-3-4.md
│   │   │   ├── 2026-04-14-phase26-nav-restructure.md
│   │   │   ├── 2026-04-14-water-wastewater-section.md
│   │   │   ├── 2026-04-16-control-theory-overview-rebuild.md
│   │   │   └── 2026-07-12-phase49a-ai-ml-source-closure.md
│   │   └── specs/
│   │       ├── 2026-03-12-doc-support-design.md
│   │       ├── 2026-03-13-field-engineering-design.md
│   │       ├── 2026-03-14-reference-section-commissioning-templates-design.md
│   │       ├── 2026-03-15-software-safety-stack-phase20-design.md
│   │       ├── 2026-03-27-control-systems-training-expansion-design.md
│   │       ├── 2026-04-14-phase26-nav-restructure-design.md
│   │       ├── 2026-04-14-water-wastewater-section-design.md
│   │       └── 2026-07-12-ai-ml-methods-register-design.md
│   ├── tools/
│   │   ├── crosswalks/
│   │   │   ├── compare/
│   │   │   │   └── index.md
│   │   │   ├── iec60079-nec-500-505/
│   │   │   │   └── index.md
│   │   │   ├── iec61511-iec61508/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── nfpa79-iec60204/
│   │   │   │   └── index.md
│   │   │   ├── standards-decision-workflow/
│   │   │   │   └── index.md
│   │   │   └── ul508a-nec-nfpa79/
│   │   │       └── index.md
│   │   ├── engineering-toolkit/
│   │   │   └── index.md
│   │   ├── glossary/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── manufacturers/
│   │   │   ├── index.md
│   │   │   ├── plc-hardware-families/
│   │   │   │   └── index.md
│   │   │   ├── plc-pac/
│   │   │   │   └── index.md
│   │   │   ├── process-instrumentation/
│   │   │   │   └── index.md
│   │   │   ├── scada-hmi/
│   │   │   │   └── index.md
│   │   │   ├── servo-motion/
│   │   │   │   └── index.md
│   │   │   ├── vendor-documentation/
│   │   │   │   └── index.md
│   │   │   └── vfd-drives/
│   │   │       └── index.md
│   │   ├── rag-browser/
│   │   │   └── index.md
│   │   ├── reference-hub/
│   │   │   └── index.md
│   │   ├── scenarios/
│   │   │   ├── global-machine/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── machine-safety-implementation/
│   │   │   │   └── index.md
│   │   │   ├── networked-safety-plc/
│   │   │   │   └── index.md
│   │   │   ├── offshore-platform-control/
│   │   │   │   └── index.md
│   │   │   ├── oil-gas-process-skid/
│   │   │   │   └── index.md
│   │   │   ├── process-skid/
│   │   │   │   └── index.md
│   │   │   ├── semiconductor-equipment/
│   │   │   │   └── index.md
│   │   │   ├── semiconductor-fab-tool/
│   │   │   │   └── index.md
│   │   │   └── us-industrial-control-panel/
│   │   │       └── index.md
│   │   ├── standards-finder/
│   │   │   └── index.md
│   │   ├── templates/
│   │   │   └── index.md
│   │   └── troubleshooting/
│   │       ├── analog-signal-faults/
│   │       │   └── index.md
│   │       ├── comms-dropouts/
│   │       │   └── index.md
│   │       ├── index.md
│   │       ├── motor-wont-start/
│   │       │   └── index.md
│   │       ├── motors/
│   │       │   └── index.md
│   │       └── vfd-faults/
│   │           └── index.md
│   ├── training/
│   │   └── index.md
│   ├── troubleshooting/
│   │   └── index.md
│   └── verification/
│       └── index.md
├── drawings examples/
│   └── fec5c93b-0ccd-44c6-b4e7-5d7d01acaa07.png
├── governance/
│   ├── AI_WORKFLOW.md
│   ├── CONTENT_STANDARDS.md
│   ├── ENGINEERING_STANDARDS.md
│   ├── PROJECT_ORGANIZATION.md
│   └── ROADMAP.md
├── lifecycle-build-page.png
├── main.py
├── project_state/
│   ├── change_log.md
│   ├── environment.md
│   ├── how_to.md
│   └── project_state.md
├── pyproject.toml
├── rag -> control-standards/rag
├── src/
│   └── cst/
│       ├── __init__.py
│       ├── calc/
│       │   ├── __init__.py
│       │   ├── ampacity.py
│       │   ├── enclosure_thermal.py
│       │   ├── motor_branch.py
│       │   ├── sccr.py
│       │   ├── short_circuit.py
│       │   ├── transformer.py
│       │   └── voltage_drop.py
│       ├── cli.py
│       ├── commissioning/
│       │   ├── __init__.py
│       │   ├── fat_sat.py
│       │   └── loop_sheets.py
│       ├── common/
│       │   ├── __init__.py
│       │   ├── cite.py
│       │   ├── tables.py
│       │   └── units.py
│       ├── diagnostics/
│       │   ├── __init__.py
│       │   ├── modbus_decode.py
│       │   ├── saleae.py
│       │   └── sbm.py
│       ├── docgen/
│       │   ├── __init__.py
│       │   └── design_package.py
│       ├── motion/
│       │   ├── __init__.py
│       │   └── encoder.py
│       ├── panel/
│       │   ├── __init__.py
│       │   ├── bom.py
│       │   ├── io_list.py
│       │   ├── nameplates.py
│       │   └── wire_schedule.py
│       ├── plc/
│       │   ├── __init__.py
│       │   ├── address_map.py
│       │   ├── comms.py
│       │   └── tag_db.py
│       └── twin/
│           ├── __init__.py
│           ├── contract.py
│           └── sync_health.py
├── temp/
│   ├── ai-ml-control-systems-research/
│   │   ├── README.md
│   │   ├── digital-twin-integration.md
│   │   ├── research-map.md
│   │   ├── scientific-domain-integration.md
│   │   └── source-register.md
│   └── wire-color-coding-web-assets/
│       ├── 00-wire-color-coding-title-banner.png
│       ├── 01-reference-standards.png
│       ├── 02-nfpa79-machinery-panel-us.png
│       ├── 03-iec60204-machinery-panel.png
│       ├── 04-us-facility-power-distribution.png
│       ├── 05-plc-24vdc-io-wiring.png
│       ├── 06-120vac-control-circuit.png
│       ├── 07-4-20ma-transmitter-hookup.png
│       ├── 08-intrinsically-safe-wiring.png
│       ├── 09-vfd-to-motor-wiring.png
│       ├── 10-servo-motion-system-wiring.png
│       ├── 11-hvac-building-automation.png
│       ├── 12-semiconductor-facility-color-map.png
│       ├── 13-industrial-ethernet-cable-identification.png
│       ├── 14-legacy-panel-before-after.png
│       ├── 15-important-wiring-notes.png
│       ├── 16-symbol-legend.png
│       ├── README.md
│       └── assets.json
├── tests/
│   ├── __init__.py
│   ├── cst/
│   │   ├── __init__.py
│   │   ├── test_cli.py
│   │   ├── test_commissioning.py
│   │   ├── test_diagnostics.py
│   │   ├── test_docgen.py
│   │   ├── test_enclosure_thermal.py
│   │   ├── test_encoder.py
│   │   ├── test_io_validation_seam.py
│   │   ├── test_modbus_decode.py
│   │   ├── test_panel.py
│   │   ├── test_phase2_calcs.py
│   │   ├── test_plc.py
│   │   ├── test_tables.py
│   │   ├── test_twin.py
│   │   ├── test_units.py
│   │   └── test_voltage_drop.py
│   └── tools/
│       ├── __init__.py
│       ├── fe_study/
│       │   ├── __init__.py
│       │   ├── test_common.py
│       │   ├── test_extract_fe_study.py
│       │   └── test_inventory_fe_study.py
│       ├── test_generate_ai_method_register.py
│       ├── test_release_check.py
│       └── test_validate_corpus_quality.py
├── tools/
│   ├── README.md
│   ├── check_internal_links.py
│   ├── fe_study/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── extract_fe_study.py
│   │   ├── inventory_fe_study.py
│   │   ├── quality_check_fe_study.py
│   │   └── summarize_fe_study.py
│   ├── fix_ai_boundaries.py
│   ├── generate_ai_method_register.py
│   ├── generate_rag_tree.py
│   ├── generate_site_templates.py
│   ├── generate_standards_overview.py
│   ├── project_automator.py
│   ├── release_check.py
│   ├── setup_hooks.sh
│   ├── validate_ai_boundaries.py
│   ├── validate_corpus_quality.py
│   └── validate_reorg.sh
└── uv.lock
```
<!-- AUTO-GENERATED TREE END -->
