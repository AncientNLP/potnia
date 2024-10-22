import re
import yaml
from functools import reduce

from .mapper import Mapper


def load_rules(file_path: str, rule_type: str):
    """
    Loads rules from the YAML file based on the specified rule type.

    Parameters:
    file_path (str): Path to the YAML file.
    rule_type (str): The type of rules to load: 'transliteration', 'regularisation', or 'ignore'.

    Returns:
    Depending on the rule_type:
    - 'transliteration': Returns patterns, complex_symbols, special_chars_pattern, restore_patterns.
    - 'regularisation': Returns corrected_patterns.
    - 'ignore': Returns patterns_to_ignore.
    """
    with open(file_path, 'r', encoding='utf8') as f:
        rules = yaml.safe_load(f)

    if rule_type == 'transliteration':
        patterns = rules.get('patterns', [])
        complex_symbols = rules.get('complex_symbols', {})
        special_chars_pattern = rules.get('special_chars_pattern', '')
        restore_patterns = rules.get('restore_patterns', [])
        return patterns, complex_symbols, special_chars_pattern, restore_patterns

    elif rule_type == 'regularisation':
        # Correct the double escaping of backslashes
        corrected_patterns = [
            (re.sub(r'\\\\', r'\\', pattern), replacement) 
            for pattern, replacement in rules.get('patterns', [])
        ]
        return corrected_patterns

    elif rule_type == 'ignore':
        patterns_to_ignore = rules.get('patterns_to_ignore', [])
        return patterns_to_ignore

    else:
        raise ValueError(f"Unknown rule_type: {rule_type}")


class LinearBMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_b")
    logograms = ("logograms_common", "logograms_unique_linear_b")

    # Load ignore patterns using the unified function
    patterns_to_ignore = load_rules("potnia/rules/ignore_patterns.yaml", "ignore")

    def tokenize_transliteration(self, text: str) -> list[str]:
        """
        Tokenizes Linear B text into individual elements, including words, special characters, and preserving spaces.

        Parameters:
        text (str): A string containing Linear B text to be tokenized.

        Returns:
        list: A list of tokens extracted from the text.
        """
        
        # Load transliteration rules
        patterns, complex_symbols, special_chars_pattern, restore_patterns = load_rules(
            "potnia/rules/transliteration_rules.yaml", "transliteration"
        )

        # Reverse the complex_symbols dictionary
        reversed_symbols = {v: k for k, v in complex_symbols.items()}

        # Replace complex symbols with placeholders
        for symbol, placeholder in complex_symbols.items():
            text = text.replace(symbol, placeholder)

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)

        # Handle space replacement with a placeholder
        space_placeholder = "\uE000"  # Placeholder for spaces
        text = text.replace(" ", space_placeholder)

        # Tokenize using the special characters pattern
        tokens = re.split(special_chars_pattern, text)

        # Apply processing to each token and filter out empty tokens
        tokenized = [
            " " if tok == space_placeholder else
            reduce(lambda t, p: re.sub(p[0], p[1], t), restore_patterns, tok)
            for tok in tokens if tok and tok != "-"
        ]

        # Restore complex symbols using the reversed dictionary
        for placeholder, symbol in reversed_symbols.items():
            tokenized = [tok.replace(placeholder, symbol) for tok in tokenized]

        return tokenized if tokenized else [""]

    def regularize(self, text: str) -> str:
        # Load regularisation rules
        patterns = load_rules("potnia/rules/regularisation_rules.yaml", "regularisation")

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)

        text = super().regularize(text)

        # Ensure there are informative characters left in the text
        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""

        return text


linear_b_mapper = LinearBMapper()
