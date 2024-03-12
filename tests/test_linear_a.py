import pytest
from potnia import linear_a_mapper
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("linear_a_unicode"))
def test_linear_a_unicode(test_input, expected):
    assert linear_a_mapper(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("linear_a_transliteration"))
def test_linear_a_transliteration(test_input, expected):
    assert linear_a_mapper.to_transliteration(test_input) == expected

