import pytest
from potnia import linear_a
from .data import expected

@pytest.mark.parametrize("test_input,expected", expected("linear_a_unicode"))
def test_linear_a_unicode(test_input, expected):
    result = linear_a(test_input)
    assert result == expected, f"Expected: linear_a('{test_input}') to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_a_transliteration"))
def test_linear_a_transliteration(test_input, expected):
    result = linear_a.to_transliteration(test_input)
    assert result == expected, f"Expected: linear_a.to_transliteration('{test_input}') to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_a_unicode_regularized"))
def test_linear_a_unicode_regularized(test_input, expected):
    result = linear_a(test_input, regularize=True)
    assert result == expected, f"Expected: linear_a('{test_input}', regularize=True) to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_a_tokenize_transliteration"))
def test_tokenize_transliteration_linear_a(test_input, expected):
    result = linear_a.tokenize_transliteration(test_input)
    assert result == expected, f"Expected: linear_a.tokenize_transliteration('{test_input}') to produce '{expected}' but got '{result}'"


