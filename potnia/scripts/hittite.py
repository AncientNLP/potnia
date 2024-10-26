from dataclasses import dataclass
from ..script import Script


@dataclass
class Hittite(Script):
    config:str = "hittite"

    def tokenize_transliteration(self, input_string:str) -> list[str]:
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