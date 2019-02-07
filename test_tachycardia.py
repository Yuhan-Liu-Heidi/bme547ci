import pytest


@pytest.mark.parametrize("instr, output", [
    ("tachycardic", True),
    ("TachyCardic", True),
    ("TACHYCARDIC", True),
    (" tachycardic,", True),
    ("taachycardic", False),
    ("tachycrdic", False)])
def test_is_tachycardic(instr, output):
    from tachycardia import is_tachycardic
    result = is_tachycardic(instr)
    assert result == output
