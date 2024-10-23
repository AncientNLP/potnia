import pytest
from potnia import hittite_mapper
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("hittite_unicode"))
def test_hittite_unicode(test_input, expected):
    assert hittite_mapper(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("hittite_tokenize_transliteration"))
def test_tokenize_transliteration_hittite(test_input, expected):
    assert hittite_mapper.tokenize_transliteration(test_input) == expected
