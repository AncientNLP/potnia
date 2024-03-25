from .mapper import Mapper

class LinearAMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_a")
    logograms = ("logograms_common", "logograms_unique_linear_a")


    def tokenize_transliteration(self, input_string:str) -> list[str]:
        tokens = []
        token = ""
        i = 0

        while i < len(input_string):
            char = input_string[i]

            # Check for special sequences like "[?]"
            if char == '[' and i + 1 < len(input_string) and input_string[i + 1] == '?':
                if token:
                    tokens.append(token)
                tokens.append("[?]")
                token = ""
                i += 3  # Skip past "[?]"
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


linear_a_mapper = LinearAMapper()