import re
from .data import read_data


class Mapper:
    syllabograms:tuple[str] = tuple()
    logograms:tuple[str] = tuple()
    
    def __init__(self):
        self.syllabograms_dict = read_data(*self.syllabograms)
        self.logograms_dict = read_data(*self.syllabograms)
        self.transliteration_to_unicode_dict = read_data(*self.syllabograms, *self.logograms)
        self.unicode_to_transliteration_dict = {v: k for k, v in self.transliteration_to_unicode_dict.items()}

    def tokenize_unicode(self, text:str) -> list[str]:
        words = ['-'.join(word) for word in text.split()]
        text = ' '.join(words)

        return list(text)

    def tokenize_transliteration(self, text:str) -> list[str]:
        return re.findall(r'[^\s-]+|\s+', text)

    def to_transliteration(self, text:str) -> str:
        return "".join([self.unicode_to_transliteration_dict.get(token, token) for token in self.tokenize_unicode(text)])

    def to_unicode(self, text:str) -> str:
        return "".join([self.transliteration_to_unicode_dict.get(token, token) for token in self.tokenize_transliteration(text)])

    def __call__(self, text:str) -> str:
        return self.to_unicode(text)