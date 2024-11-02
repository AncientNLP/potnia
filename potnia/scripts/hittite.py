from dataclasses import dataclass
from ..script import Script


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

    def tokenize_transliteration(self, input_string:str) -> list[str]:
        """
        Tokenizes transliterated text according to specific patterns.

        Args:
            text (str): Input text in transliterated format.

        Returns:
            list[str]: List of tokens
        """
        tokens = []
        token = ""
        i = 0

        while i < len(input_string):
            char = input_string[i]

            # Handle characters ']', '[', and ' '
            if char in '[] ':
                if token:
                    tokens.append(token)
                    token = ""
                tokens.append(char)
            # Handle other characters
            elif char in ['-','‑']:
                if token:
                    tokens.append(token)
                    token = ""
            else:
                token += char
            i += 1

        # Add the last token if it exists
        if token:
            tokens.append(token)

        return tokens




hittite = Hittite()