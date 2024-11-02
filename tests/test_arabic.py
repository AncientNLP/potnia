import pytest
from potnia import arabic
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("arabic_unicode"))
def test_arabic_unicode(test_input, expected):
    result = arabic(test_input)
    assert result == expected, f"Expected: arabic('{test_input}') to produce '{expected}' but got '{result}'"


