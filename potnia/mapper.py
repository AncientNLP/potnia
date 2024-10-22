import re
from functools import reduce

from .data import read_data

class Mapper:
    syllabograms:tuple[str] = tuple()
    logograms:tuple[str] = tuple()
    patterns_to_ignore:tuple[str] = tuple()
    regularization_rules:tuple[str] = tuple()
    transliteration_rules:tuple[str] = tuple()
    
    def __init__(self):
        self.syllabograms_dict = read_data(self.syllabograms)
        self.logograms_dict = read_data(self.syllabograms)
        self.transliteration_to_unicode_dict = read_data(self.syllabograms, self.logograms)
        self.unicode_to_transliteration_dict = {}
        for k, v in self.transliteration_to_unicode_dict.items():
            if v not in self.unicode_to_transliteration_dict:
                self.unicode_to_transliteration_dict[v] = k

        # Load patterns to ignore                
        patterns_to_ignore_dict = read_data(self.patterns_to_ignore)
        self.regex_to_ignore = [re.compile(pattern) for pattern in patterns_to_ignore_dict.get("patterns_to_ignore", [])]

        # Load regularization rules
        regularization_rules = read_data(self.regularization_rules)
        self.regularization_regex = [
            (re.compile(re.sub(r'\\\\', r'\\', pattern)), replacement) 
            for pattern, replacement in regularization_rules.get('patterns', [])
        ]

        # Load transliteration rules
        transliteration_rules = read_data(self.transliteration_rules)
        self.transliteration_patterns = [ 
            (re.compile(pattern),replacement) 
            for pattern, replacement in transliteration_rules.get('patterns', [])
        ]
        self.complex_symbols = transliteration_rules.get('complex_symbols', {})
        self.special_chars_pattern = re.compile(transliteration_rules.get('special_chars_pattern', ''))
        self.restore_patterns = [ 
            (re.compile(pattern),replacement) 
            for pattern, replacement in transliteration_rules.get('restore_patterns', [])
        ]

        # Reverse the complex_symbols dictionary
        self.reversed_symbols = {v: k for k, v in self.complex_symbols.items()}

    def tokenize_unicode(self, text:str) -> list[str]:
        words = ['-'.join(word) for word in text.split()]
        text = ' '.join(words)

        return list(text)

    def tokenize_transliteration(self, text:str) -> list[str]:
        # Replace complex symbols with placeholders
        for symbol, placeholder in self.complex_symbols.items():
            text = text.replace(symbol, placeholder)

        # Apply each pattern replacement in order
        for pattern, replacement in self.transliteration_patterns:
            text = pattern.sub(replacement, text)

        # Handle space replacement with a placeholder
        space_placeholder = "\uE000"  # Placeholder for spaces
        text = text.replace(" ", space_placeholder)

        # Tokenize using the special characters pattern
        tokens = self.special_chars_pattern.split(text)

        # Apply processing to each token and filter out empty tokens
        tokenized = [
            " " if tok == space_placeholder else
            reduce(lambda t, p: p[0].sub(p[1], t), self.restore_patterns, tok)
            for tok in tokens if tok and tok != "-"
        ]

        # Restore complex symbols using the reversed dictionary
        for placeholder, symbol in self.reversed_symbols.items():
            tokenized = [tok.replace(placeholder, symbol) for tok in tokenized]

        return tokenized if tokenized else [""]

    def to_transliteration(self, text:str) -> str:
        return "".join(
            [
                self.unicode_to_transliteration_dict.get(token, token) 
                for token in self.tokenize_unicode(text)
            ]
        )

    def to_unicode(self, text:str, regularize:bool=False) -> str:
        tokens = self.tokenize_transliteration(text)
        result = "".join([self.transliteration_to_unicode_dict.get(token, token) for token in tokens])
        if regularize:
            result = self.regularize(result)
        return result

    def __call__(self, text:str, regularize:bool=False) -> str:
        return self.to_unicode(text, regularize=regularize)
    
    def regularize(self, string: str) -> str:
        for pattern, replacement in self.regularization_regex:
            string = pattern.sub(replacement, string)

        for regex in self.regex_to_ignore:
            string = regex.sub("", string)
        string = re.sub(r'\s+', ' ', string)
        string = re.sub('mut','',string)
        return string.strip()
