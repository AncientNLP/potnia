import pytest
from potnia import lydian
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("lydian_unicode"))
def test_lydian_unicode(test_input, expected):
    result = lydian(test_input)
    assert result == expected, f"Expected: lydian('{test_input}') to produce '{expected}' but got '{result}'"


