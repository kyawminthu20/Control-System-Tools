def test_work_dirs_has_converted():
    from tools.fe_study.common import WORK_DIRS
    assert "converted" in WORK_DIRS
    assert WORK_DIRS["converted"] == "_converted"
