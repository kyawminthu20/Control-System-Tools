def test_work_dirs_has_converted():
    from tools.fe_study.common import WORK_DIRS
    assert "converted" in WORK_DIRS
    assert WORK_DIRS["converted"] == "_converted"


def test_infer_family_doc():
    from tools.fe_study.common import infer_family
    from pathlib import Path
    assert infer_family(Path("planning/FE_Study/How to/SomePLC.doc")) == "howto_doc"


def test_infer_priority_howto_doc():
    from tools.fe_study.common import infer_priority
    assert infer_priority("howto_doc") == "P2"
