import pytest
from potnia import linear_b_mapper
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode"))
def test_linear_b_unicode(test_input, expected):
    assert linear_b_mapper(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("linear_b_transliteration"))
def test_linear_b_transliteration(test_input, expected):
    assert linear_b_mapper.to_transliteration(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("linear_b_tokenize_transliteration"))
def test_tokenize_transliteration_linear_b(test_input, expected):
    print("test_input", test_input)
    print("expected", expected)
    assert linear_b_mapper.tokenize_transliteration(test_input) == expected
