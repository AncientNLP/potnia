import re
from .mapper import Mapper

class LinearBMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_b")
    logograms = ("logograms_common", "logograms_unique_linear_b")
    patterns_to_ignore = [
        r"vacat\s*\.?",
        r"lat\s*\.",
        r"inf\s*\.",
        r"i\s*\.",
        r"mut\s*\.",
        r"sup\s*\.",
        r"vac\s*\.",
        r"v\s*\.",
        r"vestigia",
        r"l\s*\.",
        r"s\s*\.",
        r"Graffito",
        r"[\/\,\'\?]",
        r"⟦.*?⟧",
    ]

    def tokenize_transliteration(self, text:str) -> list[str]:
        """
        Tokenizes Linear B text into individual elements, including words, special characters, and preserving spaces.
        
        Parameters:
        text (str): A string containing Linear B text to be tokenized.
        
        Returns:
        list: A list of tokens extracted from the text.
        """
        # Normalize spaces and remove specific patterns
        text = text.replace('\u00a0', ' ').replace('\u0323', '')
        
        # List of patterns and their replacements
        patterns = [
            # (r'(?<=\S)\?', ' ?'),  # Ensure '?' is separated when it follows a character
            (r'\b({})\s([mf])\b'.format('|'.join(['BOS', 'SUS', 'OVIS', 'CAP', 'EQU'])), r'\1\2'),  # Combine terms with 'm' or 'f'
            (r'\](?=[^\s])', r']-'),  # Pre-process ']' and '[' for special handling
            (r'(?<=[^\s])\[', r'-['),
            (r'\* (\d+)', r'*\1'),  # Combine '*' with the following numeral
            (r'\+ ([^\s]+)', r'+\1'),  # Combine '+' with surrounding ideograms
            (r'([^\s]) \+', r'\1+'),  # Ensure '+' is properly attached
            (r'([^\s]+) VAS', r'\1VAS'),  # Attach 'VAS' properly
            # Ignore or modify specific patterns
            *[(rf'\b{term}\s?\.', term + '.') for term in ['vac', 'vest', 'l', 's', 'lat', 'inf', 'mut', 'sup', 'i']],  # Refactored for brevity
        ]

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)

        # Space handling
        space_placeholder = "\uE000"  # Placeholder for spaces
        text = re.sub(r' ', space_placeholder, text)

        # Tokenize based on special characters and space placeholder
        special_chars_pattern = r'(\[|\]|\,|\'|\u27e6|\u27e7|-|\?|' + re.escape(space_placeholder) + ')'
        tokens = re.split(special_chars_pattern, text)

        # Replace placeholder with actual space and filter empty tokens
        tokenized = [tok if tok != space_placeholder else " " for tok in tokens if tok and tok!="-"]

        return tokenized if tokenized else [""]

    def regularize(self, text: str) -> str:
        text = re.sub(r"vestigia", "%", text)
        text = re.sub(r"vest\s*\.", "%", text)

        text = super().regularize(text)

        text = re.sub(r'[\[\]]', "%", text)

        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""
        
        return text



linear_b_mapper = LinearBMapper()