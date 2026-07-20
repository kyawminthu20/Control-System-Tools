"""Coverage for the CLI dispatch layer (cst.cli) and the citation types (cst.common.cite).

These were the two untested modules in the toolkit. The calculators themselves are covered by
their own tests and doctests; this suite exercises the argparse wiring, the exit-code contract,
and the error handling in ``main`` — not the numerics. Only table-free commands are used for
happy-path checks so the tests do not depend on the gitignored licensed standards tables.
"""

from __future__ import annotations

import pytest

from cst.cli import main
from cst.common.cite import CalcResult, Citation


# --- cst.common.cite ---------------------------------------------------------

def test_citation_str_with_note() -> None:
    c = Citation(standard="NEC 2023", clause="210.19(A)", note="branch-circuit sizing")
    assert str(c) == "NEC 2023 210.19(A) — branch-circuit sizing"


def test_citation_str_without_note() -> None:
    assert str(Citation(standard="NFPA 79", clause="Clause 7")) == "NFPA 79 Clause 7"


def test_calcresult_report_includes_all_sections() -> None:
    result = CalcResult(
        name="Voltage drop", value=3.2, unit="%",
        citations=[Citation("NEC 2023", "Chapter 9 Table 8")],
        assumptions=["75 degC copper"],
        warnings=["exceeds recommended 3%"],
        detail={"drop_volts": 3.84},
    )
    report = result.report()
    assert "Voltage drop: 3.2 %" in report
    assert "drop_volts: 3.84" in report
    assert "! exceeds recommended 3%" in report
    assert "- 75 degC copper" in report
    assert "NEC 2023 Chapter 9 Table 8" in report


def test_calcresult_report_minimal_is_single_line() -> None:
    report = CalcResult(name="Airflow", value=42.0, unit="CFM").report()
    assert report == "Airflow: 42 CFM"


# --- cst.cli happy paths (table-free commands) -------------------------------

@pytest.mark.parametrize(
    "argv, expected_substring",
    [
        (["encoder", "--ppr", "1024", "--gear", "5", "--rpm", "3000"], "Counts/motor rev"),
        (["enclosure", "--watts", "350", "--height", "1.6", "--width", "0.8", "--depth", "0.5"], ":"),
        (["fan", "--watts", "400", "--max-temp", "45"], ":"),
        (["fault-current", "--kva", "75", "--volts", "480", "--z", "5"], ":"),
        (["sccr", "--component", "contactor:5", "--component", "breaker:10"], ":"),
    ],
)
def test_command_happy_path(argv, expected_substring, capsys) -> None:
    assert main(argv) == 0
    out = capsys.readouterr().out
    assert out.strip()
    assert expected_substring in out


# --- cst.cli error handling --------------------------------------------------

def test_value_error_returns_2_and_reports_to_stderr(capsys) -> None:
    # temperature_rise rejects a non-positive heat load with ValueError.
    assert main(["enclosure", "--watts", "0", "--height", "1.6", "--width", "0.8", "--depth", "0.5"]) == 2
    err = capsys.readouterr().err
    assert err.startswith("error:")


def test_bad_component_spec_returns_2(capsys) -> None:
    # A --component without ':kA' raises ValueError inside the handler.
    assert main(["sccr", "--component", "contactor"]) == 2
    assert capsys.readouterr().err.startswith("error:")


def test_unknown_command_exits(capsys) -> None:
    with pytest.raises(SystemExit):
        main(["not-a-command"])


def test_missing_subcommand_exits() -> None:
    # The subparser is required=True.
    with pytest.raises(SystemExit):
        main([])


def test_missing_required_argument_exits() -> None:
    with pytest.raises(SystemExit):
        main(["encoder"])  # --ppr is required


# --- cst modbus-decode -------------------------------------------------------

def _demo_capture(tmp_path):
    """A short healthy poll plus one exception response, as a classic pcap."""
    from tests.cst.test_modbus_decode import (
        CLIENT, SERVER, _exception, _pcap, _read_holding_request,
        _read_holding_response, _tcp_segment,
    )
    request = _read_holding_request(1, 100, 2)
    response = _read_holding_response(1, [7, 8])
    bad = _read_holding_request(2, 9999, 1)
    frames = [
        (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, request)),
        (1.01, _tcp_segment(SERVER, CLIENT, 502, 5, 1, response)),
        (2.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1 + len(request), bad)),
        (2.01, _tcp_segment(SERVER, CLIENT, 502, 5, 1 + len(response), _exception(2, 3, 2))),
    ]
    path = tmp_path / "demo.pcap"
    path.write_bytes(_pcap(frames))
    return path


def test_modbus_decode_reports_summary(tmp_path, capsys) -> None:
    assert main(["modbus-decode", str(_demo_capture(tmp_path))]) == 0
    out = capsys.readouterr().out
    assert "frames        : 4" in out
    assert "exceptions    : 1" in out


def test_modbus_decode_optional_sections(tmp_path, capsys) -> None:
    argv = ["modbus-decode", str(_demo_capture(tmp_path)),
            "--addresses", "--exceptions", "--unanswered"]
    assert main(argv) == 0
    out = capsys.readouterr().out
    assert "Illegal Data Address" in out
    assert "100..101" in out
    assert "unanswered requests: 0" in out


def test_modbus_decode_missing_file_returns_2(capsys) -> None:
    assert main(["modbus-decode", "/nonexistent/capture.pcap"]) == 2
    assert capsys.readouterr().err.startswith("error:")


def test_modbus_decode_wrong_port_warns(tmp_path, capsys) -> None:
    """A wrong --port labels every frame a response; that must not pass silently."""
    argv = ["modbus-decode", str(_demo_capture(tmp_path)), "--port", "5020"]
    assert main(argv) == 0
    captured = capsys.readouterr()
    assert "(0 req / 4 resp)" in captured.out
    assert "warning: no requests seen" in captured.err
    assert "--port" in captured.err


def test_modbus_decode_no_frames_returns_2(tmp_path, capsys) -> None:
    """A capture with no Modbus at all is an error, not an empty report."""
    from tests.cst.test_modbus_decode import CLIENT, SERVER, _pcap, _tcp_segment

    path = tmp_path / "http.pcap"
    path.write_bytes(
        _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, b"GET / HTTP/1.1\r\n\r\n"))])
    )
    assert main(["modbus-decode", str(path)]) == 2
    assert "no Modbus TCP frames" in capsys.readouterr().err


# --- twin-validate / twin-sync ------------------------------------------------

_EXAMPLE_PAYLOAD = "data/examples/twin_payload_example.json"
_EXAMPLE_SAMPLES = "data/examples/twin_sync_example.csv"
_REGISTER = "control-standards/rag/design_framework/ai_integration/methods.yml"


def test_twin_validate_example_payload_returns_0(capsys) -> None:
    assert main(["twin-validate", _EXAMPLE_PAYLOAD, "--ceiling", "2"]) == 0
    assert "payload OK" in capsys.readouterr().out


def test_twin_validate_reports_problems_and_returns_1(tmp_path, capsys) -> None:
    import json
    from pathlib import Path

    data = json.loads(Path(_EXAMPLE_PAYLOAD).read_text(encoding="utf-8"))
    del data["model_version"]
    broken = tmp_path / "broken.json"
    broken.write_text(json.dumps(data), encoding="utf-8")

    assert main(["twin-validate", str(broken), "--ceiling", "2"]) == 1
    out = capsys.readouterr().out
    assert "1 problem(s):" in out
    assert "model_version" in out


def test_twin_validate_reads_the_ceiling_from_the_register(capsys) -> None:
    argv = ["twin-validate", _EXAMPLE_PAYLOAD,
            "--register", _REGISTER, "--method-id", "digital_twin_state_sync"]
    assert main(argv) == 0
    assert "payload OK" in capsys.readouterr().out


def test_twin_validate_rejects_both_ceiling_sources(capsys) -> None:
    argv = ["twin-validate", _EXAMPLE_PAYLOAD, "--ceiling", "2",
            "--register", _REGISTER, "--method-id", "digital_twin_state_sync"]
    assert main(argv) == 2
    assert "alternative ways" in capsys.readouterr().err


def test_twin_validate_planned_method_id_explains_itself(capsys) -> None:
    """A Planned row has no established ceiling; that must not read as a typo."""
    argv = ["twin-validate", _EXAMPLE_PAYLOAD,
            "--register", _REGISTER, "--method-id", "hybrid_chemical_closure"]
    assert main(argv) == 2
    assert "still Planned" in capsys.readouterr().err


def test_twin_sync_reports_the_seeded_gap_and_returns_1(capsys) -> None:
    assert main(["twin-sync", _EXAMPLE_SAMPLES, "--max-age", "5"]) == 1
    out = capsys.readouterr().out
    assert "Twin synchronization health" in out
    assert "max gap: 12 s" in out
    assert "References:" in out


def test_twin_sync_clean_series_returns_0(tmp_path, capsys) -> None:
    f = tmp_path / "clean.csv"
    f.write_text(
        "source_ts,acquisition_ts\n"
        + "".join(f"{i}.0,{i}.2\n" for i in range(20)),
        encoding="utf-8",
    )
    assert main(["twin-sync", str(f), "--max-age", "5"]) == 0
    assert "0 gap(s) detected" in capsys.readouterr().out


def test_twin_sync_missing_file_returns_2(capsys) -> None:
    assert main(["twin-sync", "/nonexistent/samples.csv", "--max-age", "5"]) == 2
    assert capsys.readouterr().err.startswith("error:")
