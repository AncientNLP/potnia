import pytest
from potnia import arabic_mapper
from .data import expected


@pytest.mark.parametrize("test_input,expected", expected("arabic_unicode"))
def test_arabic_unicode(test_input, expected):
    assert arabic_mapper(test_input) == expected
