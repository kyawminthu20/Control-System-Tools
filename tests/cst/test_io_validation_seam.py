"""The validated-I/O seam: every generator refuses invalid or colliding input.

These tests pin the safety property that a malformed I/O list can never reach a
deliverable. Duplicate tags used to silently overwrite loop sheets (dict keyed
by tag), and no generator called ``validate()`` — so bad source data produced
plausible-looking, wrong output. Each generator must now reject before it emits.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cst.commissioning.fat_sat import fat_template
from cst.commissioning.loop_sheets import generate_loop_sheets
from cst.panel.bom import generate_bom
from cst.panel.nameplates import legend_plates
from cst.panel.io_list import IOList, IOListError, IOPoint, load_io_list
from cst.panel.wire_schedule import generate_wire_schedule
from cst.plc.tag_db import tags_from_io_list

EXAMPLE = Path(__file__).resolve().parents[2] / "data" / "examples" / "io_list_example.csv"


@pytest.fixture
def example_list() -> IOList:
    return load_io_list(EXAMPLE)


def _colliding_list() -> IOList:
    """Two points sharing a tag and a rack/slot/channel address."""
    return IOList([
        IOPoint("FT-101", "Flow", "AI", rack="0", slot="1", channel="0"),
        IOPoint("FT-101", "Flow (dup)", "AI", rack="0", slot="1", channel="0"),
    ])


def test_loop_sheets_reject_duplicate_tags_instead_of_overwriting() -> None:
    with pytest.raises(IOListError):
        generate_loop_sheets(_colliding_list())


def test_bom_rejects_colliding_io() -> None:
    with pytest.raises(IOListError):
        generate_bom(_colliding_list())


def test_wire_schedule_rejects_colliding_io() -> None:
    with pytest.raises(IOListError):
        generate_wire_schedule(_colliding_list())


def test_tags_from_io_list_rejects_colliding_io() -> None:
    # Protects the Modbus map: duplicate tags would double-map registers.
    with pytest.raises(IOListError):
        tags_from_io_list(_colliding_list())


def test_legend_plates_reject_colliding_io() -> None:
    with pytest.raises(IOListError):
        legend_plates(_colliding_list())


def test_fat_template_rejects_colliding_io() -> None:
    with pytest.raises(IOListError):
        fat_template(_colliding_list())


def test_error_carries_every_problem() -> None:
    with pytest.raises(IOListError) as excinfo:
        generate_bom(_colliding_list())
    text = "\n".join(excinfo.value.problems)
    assert "duplicate tag: FT-101" in text
    assert "address conflict" in text


def test_clean_list_still_generates(example_list: IOList) -> None:
    # The seam must not block valid input — regression guard.
    assert generate_bom(example_list)
    assert generate_wire_schedule(example_list)
    assert generate_loop_sheets(example_list)


def test_design_package_aborts_on_invalid_io() -> None:
    from cst.docgen.design_package import DesignPackage

    package = DesignPackage(project="Demo")
    with pytest.raises(IOListError):
        package.add_io_summary(_colliding_list())


def test_cli_generator_blocks_invalid_csv_and_writes_nothing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from cst.cli import main

    csv_file = tmp_path / "io.csv"
    csv_file.write_text(
        "tag,description,io_type\nFT-101,Flow,AI\nFT-101,Flow dup,AI\n",
        encoding="utf-8",
    )
    out_dir = tmp_path / "sheets"
    rc = main(["loop-sheets", str(csv_file), "--out-dir", str(out_dir)])
    assert rc == 2
    assert not out_dir.exists() or not list(out_dir.iterdir())
    assert "duplicate tag: FT-101" in capsys.readouterr().err
