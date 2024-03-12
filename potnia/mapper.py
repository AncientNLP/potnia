import re
from typing import Tuple, List
from .data import read_data


class Mapper:
    syllabograms:Tuple[str] = []
    logograms:Tuple[str] = []
    
    def __init__(self):
        self.syllabograms_dict = read_data(*self.syllabograms)
        self.logograms_dict = read_data(*self.syllabograms)
        self.unicode_to_transliteration_dict = read_data(*self.syllabograms, *self.logograms)
        self.transliteration_to_unicode_dict = {v: k for k, v in self.unicode_to_transliteration_dict.items()}

    def tokenize_unicode(self, text:str) -> List[str]:
        words = ['-'.join(word) for word in text.split()]
        text = ' '.join(words)

        return list(text)

    def tokenize_transliteration(self, text:str) -> List[str]:
        return re.findall(r'[^\s-]+|\s+', text)

    def to_transliteration(self, text:str) -> str:
        return "".join([self.unicode_to_transliteration_dict.get(token, token) for token in self.tokenize_unicode(text)])

    def to_unicode(self, text:str) -> str:
        return "".join([self.transliteration_to_unicode_dict.get(token, token) for token in self.tokenize_transliteration(text)])

    def __call__(self, text:str) -> str:
        return self.to_unicode(text)