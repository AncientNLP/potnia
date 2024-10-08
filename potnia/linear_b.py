import re
import yaml
from .mapper import Mapper

# Function to load the transliteration rules from the YAML file
def load_transliteration_rules(file_path: str):
    with open(file_path, 'r', encoding='utf8') as f:
        rules = yaml.safe_load(f)
    return rules.get('patterns', []), rules.get('complex_symbols', {}), rules.get('special_chars_pattern', '')

# Function to load the regularisation rules from the YAML file
def load_regularisation_rules(file_path: str):
    with open(file_path, 'r', encoding='utf8') as f:
        rules = yaml.safe_load(f)
        
    # Correct the double escaping of backslashes
    corrected_patterns = [(re.sub(r'\\\\', r'\\', pattern), replacement) for pattern, replacement in rules.get('patterns', [])]
    
    return corrected_patterns

# Load patterns to ignore from the YAML file
def load_ignore_patterns(file_path: str):
    with open(file_path, 'r', encoding='utf8') as f:
        rules = yaml.safe_load(f)
    return rules.get('patterns_to_ignore', [])

class LinearBMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_b")
    logograms = ("logograms_common", "logograms_unique_linear_b")
    patterns_to_ignore=load_ignore_patterns("potnia/rules/ignore_patterns.yaml")

    def tokenize_transliteration(self, text: str) -> list[str]:
        """
        Tokenizes Linear B text into individual elements, including words, special characters, and preserving spaces.
        
        Parameters:
        text (str): A string containing Linear B text to be tokenized.
        
        Returns:
        list: A list of tokens extracted from the text.
        """
        
        # Load patterns, complex symbols, and special characters from YAML file
        patterns, complex_symbols, special_chars_pattern = load_transliteration_rules("potnia/rules/transliteration_rules.yaml")
                
        # Reverse the complex_symbols dictionary
        reversed_symbols = {v: k for k, v in complex_symbols.items()}

        # Replace complex symbols with placeholders
        for symbol, placeholder in complex_symbols.items():
            text = text.replace(symbol, placeholder)

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)

        # Space handling
        space_placeholder = "\uE000"  # Placeholder for spaces
        text = re.sub(r' ', space_placeholder, text)
        
        special_chars_pattern = r'(\[|\]|\,|\'|\u27e6|\u27e7|-|\?|<|>|⌞|⌟|⸤|⸥|\||' + re.escape(space_placeholder) + ')'
        tokens = re.split(special_chars_pattern, text)

        # Replace placeholder with actual space and filter empty tokens
        tokenized = [tok if tok != space_placeholder else " " for tok in tokens if tok and tok!="-"]
        
        # Replace placeholder with actual space and filter empty tokens
        tokenized = [tok.replace('fragmentum_A', 'fragmentum A').replace('fragmentum_B', 'fragmentum B') if tok != space_placeholder else " " for tok in tokens if tok and tok != "-"]

        # Restore specific tokens like 'ME±RI' to their original form
        tokenized = [tok.replace('ME±RI', 'ME<±RI>') for tok in tokenized]
        
        # Restore complex symbols using the reversed dictionary
        for placeholder, symbol in reversed_symbols.items():
            tokenized = [tok.replace(placeholder, symbol) for tok in tokenized]
        
        return tokenized if tokenized else [""]
    
    def regularize(self, text: str) -> str:
        
        patterns= load_regularisation_rules("potnia/rules/regularisation_rules.yaml")
   

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)
                    
        text = super().regularize(text)

        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""
        
        return text

linear_b_mapper = LinearBMapper()
