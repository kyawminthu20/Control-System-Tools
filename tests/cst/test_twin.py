"""Tests for the digital-twin data contract and synchronization-health checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cst.twin.contract import (
    FIELD_SPECS,
    MAX_AUTHORITY_LEVEL,
    REQUIRED_FIELDS,
    TwinContractError,
    TwinPayload,
    authority_ceilings,
    load_payload,
    schema,
    validate_payload,
)
from cst.twin.sync_health import read_sample_csv, sync_health

REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_PAYLOAD = REPO_ROOT / "data" / "examples" / "twin_payload_example.json"
EXAMPLE_SAMPLES = REPO_ROOT / "data" / "examples" / "twin_sync_example.csv"
REGISTER = (
    REPO_ROOT
    / "control-standards"
    / "rag"
    / "design_framework"
    / "ai_integration"
    / "methods.yml"
)


@pytest.fixture
def payload() -> dict:
    return load_payload(EXAMPLE_PAYLOAD)


# --- contract: the happy path -------------------------------------------------


def test_example_payload_is_contract_valid(payload):
    assert validate_payload(payload, authority_ceiling=2) == []


def test_from_mapping_exposes_required_fields_and_extras(payload):
    built = TwinPayload.from_mapping(payload, authority_ceiling=2)
    assert built.asset_id == "PUMP-101"
    assert built.requested_authority == 2
    assert built.value_kind == "predicted"
    # Optional fields land in extras, never as attributes.
    assert built.extras["uncertainty"] == pytest.approx(3.1)
    assert not hasattr(built, "uncertainty")


# --- contract: each required field is individually enforced -------------------


@pytest.mark.parametrize("field", REQUIRED_FIELDS)
def test_each_required_field_is_reported_by_name_when_missing(payload, field):
    del payload[field]
    problems = validate_payload(payload, authority_ceiling=2)
    assert len(problems) == 1
    assert f'"{field}"' in problems[0]
    assert "missing required contract field" in problems[0]


def test_wrong_type_names_the_field_and_expected_type(payload):
    payload["asset_id"] = 101
    (problem,) = validate_payload(payload, authority_ceiling=2)
    assert '"asset_id"' in problem
    assert "expected str" in problem


def test_boolean_does_not_satisfy_an_integer_field(payload):
    # bool subclasses int, so an unguarded isinstance check would accept this
    # and read True as authority level 1.
    payload["requested_authority"] = True
    problems = validate_payload(payload, authority_ceiling=2)
    assert any("boolean" in p for p in problems)


def test_unknown_field_is_rejected(payload):
    payload["vendor_hint"] = "trust me"
    (problem,) = validate_payload(payload, authority_ceiling=2)
    assert '"vendor_hint"' in problem
    assert "not part of the contract" in problem


def test_value_kind_vocabulary_is_closed(payload):
    payload["value_kind"] = "estimated"
    (problem,) = validate_payload(payload, authority_ceiling=2)
    assert "'measured'" in problem and "'predicted'" in problem


# --- contract: the checks that exist for engineering reasons ------------------


def test_inference_cannot_precede_its_own_observation(payload):
    payload["inference_timestamp"] = payload["source_timestamp"] - 5
    problems = validate_payload(payload, authority_ceiling=2)
    assert any("precedes source_timestamp" in p for p in problems)


def test_authority_above_ceiling_names_both_numbers(payload):
    payload["requested_authority"] = 3
    (problem,) = validate_payload(payload, authority_ceiling=2)
    assert "3" in problem and "2" in problem
    assert "exceeds the register ceiling" in problem


def test_authority_within_ceiling_passes(payload):
    payload["requested_authority"] = 1
    assert validate_payload(payload, authority_ceiling=2) == []


def test_level_five_is_flagged_even_with_a_permissive_ceiling(payload):
    # No learned twin output is assigned level 5, so no configured ceiling may
    # authorize it.
    payload["requested_authority"] = MAX_AUTHORITY_LEVEL
    (problem,) = validate_payload(payload, authority_ceiling=MAX_AUTHORITY_LEVEL)
    assert "not assigned to any learned twin output" in problem


def test_authority_outside_the_ladder_is_flagged(payload):
    payload["requested_authority"] = 9
    (problem,) = validate_payload(payload, authority_ceiling=2)
    assert "outside the ladder" in problem


def test_no_ceiling_supplied_skips_only_the_ceiling_check(payload):
    payload["requested_authority"] = 4
    assert validate_payload(payload) == []


def test_stale_payload_is_flagged_against_injected_now(payload):
    (problem,) = validate_payload(
        payload, authority_ceiling=2, now=payload["valid_until"] + 30
    )
    assert "stale" in problem
    assert "30" in problem


def test_fresh_payload_passes_the_staleness_check(payload):
    assert validate_payload(
        payload, authority_ceiling=2, now=payload["valid_until"] - 1
    ) == []


def test_from_mapping_aggregates_every_problem(payload):
    del payload["asset_id"]
    del payload["model_version"]
    payload["value_kind"] = "guessed"
    with pytest.raises(TwinContractError) as excinfo:
        TwinPayload.from_mapping(payload, authority_ceiling=2)
    assert len(excinfo.value.problems) == 3


# --- loading ------------------------------------------------------------------


def test_load_payload_reports_json_position(tmp_path):
    bad = tmp_path / "broken.json"
    bad.write_text('{"asset_id": "A",}', encoding="utf-8")
    with pytest.raises(ValueError, match="not valid JSON"):
        load_payload(bad)


def test_load_payload_rejects_a_non_object(tmp_path):
    arr = tmp_path / "list.json"
    arr.write_text("[1, 2, 3]", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a JSON object"):
        load_payload(arr)


def test_load_payload_missing_file_names_the_path(tmp_path):
    with pytest.raises(FileNotFoundError, match="payload file not found"):
        load_payload(tmp_path / "absent.json")


# --- the register loader ------------------------------------------------------


def test_authority_ceilings_reads_the_real_register():
    ceilings = authority_ceilings(REGISTER)
    assert ceilings["digital_twin_state_sync"] == 2
    assert ceilings["learned_soft_sensor"] == 2
    assert ceilings["pinn_forward_model"] == 1
    assert ceilings["pid_control"] == MAX_AUTHORITY_LEVEL


def test_planned_rows_are_absent_rather_than_zero():
    # "Planned" means no ceiling has been established, which is not the same
    # claim as a ceiling of zero.
    ceilings = authority_ceilings(REGISTER)
    for planned in ("hybrid_chemical_closure", "raman_pls_soft_sensor"):
        assert planned not in ceilings


def test_authority_ceilings_rejects_a_malformed_register(tmp_path):
    bad = tmp_path / "methods.yml"
    bad.write_text("{not json", encoding="utf-8")
    with pytest.raises(ValueError, match="not parseable"):
        authority_ceilings(bad)


def test_authority_ceilings_missing_file_names_the_path(tmp_path):
    with pytest.raises(FileNotFoundError, match="method register not found"):
        authority_ceilings(tmp_path / "absent.yml")


# --- schema (also the anti-drift guard for the published template) ------------


def test_schema_required_matches_the_field_specs():
    assert schema()["required"] == list(REQUIRED_FIELDS)


def test_schema_properties_cover_every_field():
    assert set(schema()["properties"]) == {spec.name for spec in FIELD_SPECS}


def test_schema_constrains_the_authority_level():
    authority = schema()["properties"]["requested_authority"]
    assert authority["minimum"] == 0
    assert authority["maximum"] == MAX_AUTHORITY_LEVEL


def test_schema_is_closed_against_extra_properties():
    assert schema()["additionalProperties"] is False


def test_example_payload_satisfies_the_published_schema_shape():
    published = schema()
    data = json.loads(EXAMPLE_PAYLOAD.read_text(encoding="utf-8"))
    assert set(data) <= set(published["properties"])
    assert set(published["required"]) <= set(data)


# --- synchronization health ---------------------------------------------------


def _regular(n: int = 30, interval: float = 1.0, skew: float = 0.2):
    return [(i * interval, i * interval + skew) for i in range(n)]


def test_regular_series_is_clean():
    health = sync_health(_regular(), max_age_s=5.0)
    assert health.gaps == ()
    assert health.out_of_order_count == 0
    assert health.stale_count == 0
    assert health.warnings == ()
    assert health.median_interval_s == pytest.approx(1.0)


def test_gap_is_detected_with_start_and_duration():
    samples = _regular(10)  # sources 0..9 at 1 s
    resume = 9.0 + 10.0  # a 10 s dropout, then telemetry resumes at 1 s again
    samples += [(resume + i, resume + i + 0.2) for i in range(5)]
    health = sync_health(samples, max_age_s=5.0)
    assert len(health.gaps) == 1
    assert health.gaps[0].duration_s == pytest.approx(10.0)
    assert health.gaps[0].start_s == pytest.approx(9.0)
    assert health.max_gap_s == pytest.approx(10.0)
    assert any("gap" in w for w in health.warnings)


def test_constant_skew_is_measured_without_drift():
    health = sync_health(_regular(skew=0.25), max_age_s=5.0)
    assert health.mean_skew_s == pytest.approx(0.25)
    assert health.max_abs_skew_s == pytest.approx(0.25)
    assert health.skew_drift_s_per_s == pytest.approx(0.0, abs=1e-9)


def test_growing_skew_is_reported_as_drift():
    samples = [(i * 1.0, i * 1.0 + 0.1 + i * 0.01) for i in range(30)]
    health = sync_health(samples, max_age_s=5.0)
    assert health.skew_drift_s_per_s == pytest.approx(0.01, rel=1e-6)
    assert any("drifting" in w for w in health.warnings)


def test_out_of_order_samples_are_counted_and_warned():
    samples = _regular(10)
    samples[5], samples[6] = samples[6], samples[5]
    health = sync_health(samples, max_age_s=5.0)
    assert health.out_of_order_count == 1
    assert any("out of sequence" in w for w in health.warnings)


def test_stale_samples_are_counted_against_max_age():
    samples = _regular(10)
    samples[3] = (samples[3][0], samples[3][0] + 9.0)
    samples[7] = (samples[7][0], samples[7][0] + 8.0)
    health = sync_health(samples, max_age_s=5.0)
    assert health.stale_count == 2
    assert health.stale_fraction == pytest.approx(0.2)
    assert any("freshness bound" in w for w in health.warnings)


def test_negative_skew_is_warned_as_clock_disagreement():
    samples = _regular(10)
    samples[4] = (samples[4][0], samples[4][0] - 0.5)
    health = sync_health(samples, max_age_s=5.0)
    assert any("negative skew" in w for w in health.warnings)


def test_too_few_samples_raises():
    with pytest.raises(ValueError, match="at least 2 samples"):
        sync_health([(0.0, 0.1)], max_age_s=5.0)


def test_non_finite_timestamp_raises():
    with pytest.raises(ValueError, match="non-finite"):
        sync_health([(0.0, 0.1), (float("nan"), 1.1)], max_age_s=5.0)


def test_invalid_bounds_raise():
    with pytest.raises(ValueError, match="max_age_s must be positive"):
        sync_health(_regular(), max_age_s=0.0)
    with pytest.raises(ValueError, match="gap_factor must exceed 1"):
        sync_health(_regular(), max_age_s=5.0, gap_factor=1.0)


def test_report_carries_citations():
    report = sync_health(_regular(), max_age_s=5.0).report()
    assert "References:" in report
    assert "digital_twin.md" in report


# --- CSV reading --------------------------------------------------------------


def test_read_example_samples():
    samples = read_sample_csv(EXAMPLE_SAMPLES)
    assert len(samples) == 60
    assert all(len(s) == 2 for s in samples)


def test_example_samples_show_the_seeded_gap_and_drift():
    health = sync_health(read_sample_csv(EXAMPLE_SAMPLES), max_age_s=5.0)
    assert health.max_gap_s == pytest.approx(12.0)
    assert health.skew_drift_s_per_s > 0


def test_read_sample_csv_rejects_a_short_row(tmp_path):
    f = tmp_path / "s.csv"
    f.write_text("source_ts,acquisition_ts\n1.0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="expected 2 columns"):
        read_sample_csv(f)


def test_read_sample_csv_rejects_non_numeric_body(tmp_path):
    f = tmp_path / "s.csv"
    f.write_text("source_ts,acquisition_ts\n1.0,1.2\nx,y\n", encoding="utf-8")
    with pytest.raises(ValueError, match="not numeric timestamps"):
        read_sample_csv(f)


def test_read_sample_csv_accepts_a_headerless_file(tmp_path):
    f = tmp_path / "s.csv"
    f.write_text("1.0,1.2\n2.0,2.2\n", encoding="utf-8")
    assert read_sample_csv(f) == [(1.0, 1.2), (2.0, 2.2)]


def test_read_sample_csv_rejects_an_empty_file(tmp_path):
    f = tmp_path / "s.csv"
    f.write_text("source_ts,acquisition_ts\n", encoding="utf-8")
    with pytest.raises(ValueError, match="no numeric sample rows"):
        read_sample_csv(f)


# --- published templates (regeneration-freshness guards) ----------------------

PUBLISHED_SCHEMA = REPO_ROOT / "docs" / "assets" / "templates" / "twin_data_contract.schema.json"
PUBLISHED_PAYLOAD = REPO_ROOT / "docs" / "assets" / "templates" / "twin_payload_example.json"


def test_published_schema_matches_the_generated_one():
    """The site's schema must not drift from FIELD_SPECS — regenerate if this fails."""
    published = json.loads(PUBLISHED_SCHEMA.read_text(encoding="utf-8"))
    published.pop("$comment", None)  # the generator's banner, not part of the contract
    assert published == schema()


def test_published_payload_satisfies_the_published_schema():
    """A worked example that violated its own contract would be worse than none."""
    payload = json.loads(PUBLISHED_PAYLOAD.read_text(encoding="utf-8"))
    assert validate_payload(payload, authority_ceiling=2) == []


def test_published_payload_carries_no_banner_key():
    # additionalProperties is false, so a "$comment" here would break the example.
    payload = json.loads(PUBLISHED_PAYLOAD.read_text(encoding="utf-8"))
    assert "$comment" not in payload
