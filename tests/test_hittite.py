import pytest
from potnia import hittite
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("hittite_unicode"))
def test_hittite_unicode(test_input, expected):
    assert hittite(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("hittite_tokenize_transliteration"))
def test_tokenize_transliteration_hittite(test_input, expected):
    assert hittite.tokenize_transliteration(test_input) == expected
