import pytest
from potnia import luwian_mapper
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("luwian_unicode"))
def test_luwian_unicode(test_input, expected):
    assert luwian_mapper(test_input) == expected


@pytest.mark.parametrize("test_input,expected", expected("luwian_tokenize_transliteration"))
def test_tokenize_transliteration_luwian(test_input, expected):
    assert luwian_mapper.tokenize_transliteration(test_input) == expected
