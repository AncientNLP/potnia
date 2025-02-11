from dataclasses import dataclass
from ..script import Script
import re


@dataclass
class Hittite(Script):
    """
    Class for handling text transliteration and unicode conversion to Hittite.

    To use the singleton instance, import like so:
    ``from potnia import hittite``

    Designed especially for texts from the Catalog der Texte der Hethiter (CTH): https://www.hethport.uni-wuerzburg.de/CTH/index.php

    Attributes:
        config (str): Path to the configuration file or configuration data in string format. 
                      By default, it uses the 'hittite.yaml file in the 'data' directory.
    """
    config:str = "hittite"

    def tokenize_transliteration(self, input_string: str) -> list[str]:
        """
        Tokenizes transliterated text according to simple patterns (brackets, dashes, and spaces).
        
        Args:
            input_string (str): Input text in transliterated format.

        Returns:
            list[str]: List of tokens.
        """
        # Apply tokenization patterns from YAML (if applicable)
        for pattern, replacement in self.transliteration_patterns:
            input_string = re.sub(pattern, replacement, input_string)

         # Correctly split on spaces, brackets, or dashes (no empty tokens)
        tokens = re.split(r'(\s+|\[|\]|-)', input_string)
        
        breakpoint()

        # Filter and return only meaningful tokens
        cleaned_tokens = [token for token in tokens if token.strip() or token in [' ', '[', ']', '-']]
        return cleaned_tokens



hittite = Hittite()