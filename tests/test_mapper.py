from potnia.mapper import Mapper


def test_tokenize_transliteration():
    mapper = Mapper()
    text = "a-ke-re-si-ja"
    assert mapper.tokenize_transliteration(text) == ['a', 'ke', 're', 'si', 'ja']

