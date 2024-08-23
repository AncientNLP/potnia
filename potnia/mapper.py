import re
from .data import read_data


class Mapper:
    syllabograms:tuple[str] = tuple()
    logograms:tuple[str] = tuple()
    patterns_to_ignore = []
    
    def __init__(self):
        self.syllabograms_dict = read_data(*self.syllabograms)
        self.logograms_dict = read_data(*self.syllabograms)
        self.transliteration_to_unicode_dict = read_data(*self.syllabograms, *self.logograms)
        self.unicode_to_transliteration_dict = {}
        for k, v in self.transliteration_to_unicode_dict.items():
            if v not in self.unicode_to_transliteration_dict:
                self.unicode_to_transliteration_dict[v] = k
        self.regex_to_ignore = [re.compile(pattern) for pattern in self.patterns_to_ignore]

    def tokenize_unicode(self, text:str) -> list[str]:
        words = ['-'.join(word) for word in text.split()]
        text = ' '.join(words)

        return list(text)

    def tokenize_transliteration(self, text:str) -> list[str]:
        return re.findall(r'[^\s-]+|\s+', text)

    def to_transliteration(self, text:str) -> str:
        return "".join([self.unicode_to_transliteration_dict.get(token, token) for token in self.tokenize_unicode(text)])

    def to_unicode(self, text:str, regularize:bool=False) -> str:
        tokens = self.tokenize_transliteration(text)
        result = "".join([self.transliteration_to_unicode_dict.get(token, token) for token in tokens])
        if regularize:
            result = self.regularize(result)
        return result

    def __call__(self, text:str, regularize:bool=False) -> str:
        return self.to_unicode(text, regularize=regularize)
    
    def regularize(self, string: str) -> str:
        for regex in self.regex_to_ignore:
            string = re.sub(regex, "", string)
        string = re.sub(r'\s+', ' ', string)
        string = re.sub('mut','',string)
        return string.strip()
