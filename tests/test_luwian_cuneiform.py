import pytest
from potnia import luwian_cuneiform
from .data import expected

@pytest.mark.parametrize("test_input,expected", expected("luwian_cuneiform_unicode"))
def test_hittite_unicode(test_input, expected):
    result = luwian_cuneiform(test_input)
    assert result == expected, f"Expected: hittite('{test_input}') to produce '{expected}' but got '{result}'"


