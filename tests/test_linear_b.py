import pytest
from potnia import linear_b_mapper
from .data import expected

@pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode"))
def test_linear_b_unicode(test_input, expected):
    result = linear_b_mapper(test_input)
    assert result == expected, f"Expected: linear_b_mapper('{test_input}') to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode_regularized"))
def test_linear_b_unicode_regularized(test_input, expected):
    result = linear_b_mapper(test_input, regularize=True)
    assert result == expected, f"Expected: linear_b_mapper('{test_input}', regularize=True) to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_b_transliteration"))
def test_linear_b_transliteration(test_input, expected):
    result = linear_b_mapper.to_transliteration(test_input)
    assert result == expected, f"Expected: linear_b_mapper.to_transliteration('{test_input}') to produce '{expected}' but got '{result}'"


@pytest.mark.parametrize("test_input,expected", expected("linear_b_tokenize_transliteration"))
def test_tokenize_transliteration_linear_b(test_input, expected):
    result = linear_b_mapper.tokenize_transliteration(test_input)
    assert result == expected, f"Expected: linear_b_mapper.tokenize_transliteration('{test_input}') to produce '{expected}' but got '{result}'"

breakpoint()