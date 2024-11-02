import re
from functools import reduce
from pathlib import Path
from dataclasses import dataclass

from .data import read_data

@dataclass
class Script():
    """
    The abstract base class for handling text transliteration and unicode conversion.

    Attributes:
        config (str): Path to the configuration file or configuration data in YAML format.
    """
    config:str

    def __post_init__(self):
        """Initializes configuration and sets up mappings, patterns, and regularization rules."""

        if isinstance(self.config, (Path,str)):
            self.config = read_data(self.config)
        assert self.config, f"Configuration not found"

        self.transliteration_to_unicode_dict = self.config.get('mappings', {})
        self.unicode_to_transliteration_dict = {}
        for k, v in self.transliteration_to_unicode_dict.items():
            if v not in self.unicode_to_transliteration_dict:
                self.unicode_to_transliteration_dict[v] = k

        # Load patterns to ignore                
        patterns_to_ignore = self.config.get('patterns_to_ignore', [])
        self.regex_to_ignore = [re.compile(pattern) for pattern in patterns_to_ignore]

        # Load regularization rules
        self.regularization_regex = [
            (re.compile(re.sub(r'\\\\', r'\\', pattern)), replacement) 
            for pattern, replacement in self.config.get('regularization', [])
        ]

        # Load transliteration rules
        self.transliteration_patterns = [ 
            (re.compile(pattern),replacement) 
            for pattern, replacement in self.config.get('tokenization', [])
        ]
        self.complex_symbols = self.config.get('complex_symbols', {})
        self.special_chars_pattern = re.compile(self.config.get('special_chars_pattern', ''))
        self.restore_patterns = [ 
            (re.compile(pattern),replacement) 
            for pattern, replacement in self.config.get('restore_patterns', [])
        ]

        # Reverse the complex_symbols dictionary
        self.reversed_symbols = {v: k for k, v in self.complex_symbols.items()}

    def tokenize_unicode(self, text:str) -> list[str]:
        """
        Tokenizes unicode text according to specific patterns.

        By default, it tokenizes each character as a separate token.
        This method can be overridden in subclasses to provide more complex tokenization.

        Args:
            text (str): Input text in unicode format.

        Returns:
            list[str]: List of tokens
        """
        return list(text)

    def tokenize_transliteration(self, text:str) -> list[str]:
        """
        Tokenizes transliterated text according to specific patterns.

        Args:
            text (str): Input text in transliterated format.

        Returns:
            list[str]: List of tokens
        """
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
        """
        Converts unicode text to transliteration format.

        NB. This function may not work as expected for all scripts/languages
        because there may not be a one-to-one mapping between unicode and transliteration.

        Args:
            text (str): Input text in unicode format.

        Returns:
            str: Transliterated text.
        """
        tokens = self.tokenize_unicode(text)
        return "".join(
            [
                self.unicode_to_transliteration_dict.get(token, token) 
                for token in tokens
            ]
        )

    def to_unicode(self, text:str, regularize:bool=False) -> str:
        """
        Converts transliterated text to unicode format.

        Args:
            text (str): Input text in transliterated format.
            regularize (bool, optional): Whether to apply regularization. Defaults to False.

        Returns:
            str: Text converted to unicode format, optionally regularized.
        """
        tokens = self.tokenize_transliteration(text)
        result = "".join([self.transliteration_to_unicode_dict.get(token, token) for token in tokens])
        if regularize:
            result = self.regularize(result)
        return result

    def __call__(self, text:str, regularize:bool=False) -> str:
        """
        Allows the class instance to be called as a function for unicode conversion.

        Args:
            text (str): Input text in transliterated format.
            regularize (bool, optional): Whether to apply regularization. Defaults to False.

        Returns:
            str: Text converted to unicode format, optionally regularized.
        """
        return self.to_unicode(text, regularize=regularize)
    
    def regularize(self, string: str) -> str:
        """
        Applies regularization rules to a given string.

        Args:
            string (str): Text string to be regularized.

        Returns:
            str: Regularized text string.
        """
        for pattern, replacement in self.regularization_regex:
            string = pattern.sub(replacement, string)

        for regex in self.regex_to_ignore:
            string = regex.sub("", string)
        string = re.sub(r'\s+', ' ', string)
        string = re.sub('mut','',string)
        return string.strip()
