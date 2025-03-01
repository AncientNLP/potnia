import re
from dataclasses import dataclass
from ..script import Script

@dataclass
class LinearA(Script):
    """
    Class for handling text transliteration and unicode conversion for Linear A.

    To use the singleton instance, import like so:
    ``from potnia import linear_a``

    Attributes:
        config (str): Path to the configuration file or configuration data in string format. 
                      By default, it uses the 'linear_a.yaml file in the 'data' directory.
    """
    config:str = "linear_a.yaml"

    def tokenize_transliteration(self, input_string: str) -> list[str]:
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

            # Check for special sequences like "[?]" and "[unclassified]"
            if char == '[':
                if input_string[i:i + 3] == '[?]':
                    if token:
                        tokens.append(token)
                    tokens.append("[?]")
                    token = ""
                    i += 3  # Skip past "[?]"
                    continue
                elif input_string[i:i + 14] == '[unclassified]':
                    if token:
                        tokens.append(token)
                    tokens.append("[unclassified]")
                    token = ""
                    i += 14  # Skip past "[unclassified]"
                    continue

            # Handle characters ']', '[', and ' '
            if char in '[] ':
                if token:
                    tokens.append(token)
                    token = ""
                tokens.append(char)
            # Handle other characters
            elif char == '-':
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

    def tokenize_unicode(self, text:str) -> list[str]:
        """
        Tokenizes a unicode string by splitting and joining words with dashes.

        Args:
            text (str): Input text in unicode format.

        Returns:
            list[str]: List of tokenized strings.
        """
        def is_aegean(char):
            return "\U00010000" <= char <= "\U0001007F" or "\U00010600" <= char <= "\U0001077F"

        # Insert hyphens between consecutive Linear B characters
        modified_text = ""
        prev_was_aegean = False

        for char in text:
            if is_aegean(char):
                if prev_was_aegean:
                    modified_text += "-"  # Add hyphen if previous character was also Linear B
                modified_text += char
                prev_was_aegean = True
            else:
                modified_text += char
                prev_was_aegean = False  # Reset flag on encountering a non-Linear B character

        return list(modified_text)


linear_a = LinearA()