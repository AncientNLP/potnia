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


linear_a = LinearA()