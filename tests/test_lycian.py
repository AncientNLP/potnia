import pytest
from potnia import lycian
from .data import expected

@pytest.mark.parametrize("test_input,expected", expected("lycian_unicode"))
def test_lydian_unicode(test_input, expected):
    result = lycian(test_input)
    assert result == expected, f"Expected: lydian('{test_input}') to produce '{expected}' but got '{result}'"


