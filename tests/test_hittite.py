import pytest
from potnia import hittite
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("hittite_unicode"))
def test_hittite_unicode(test_input, expected):
    result = hittite(test_input)
    assert result == expected, f"Expected: hittite('{test_input}') to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("hittite_tokenize_transliteration"))
def test_tokenize_transliteration_hittite(test_input, expected):
    result = hittite.tokenize_transliteration(test_input)
    assert result == expected, f"Expected: hittite.tokenize_transliteration('{test_input}') to produce '{expected}' but got '{result}'"
