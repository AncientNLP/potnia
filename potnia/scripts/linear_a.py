from dataclasses import dataclass
from ..script import Script
from functools import reduce

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
        
        for symbol, placeholder in self.complex_symbols.items():
            input_string = input_string.replace(symbol, placeholder)
            
        # Apply each pattern replacement in order
        for pattern, replacement in self.transliteration_patterns:
            input_string = pattern.sub(replacement, input_string)
            

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
            
        # Apply processing to each token and filter out empty tokens
        tokens = [
            reduce(lambda t, p: p[0].sub(p[1], t), self.restore_patterns, tok)
            for tok in tokens if tok and tok != "-"
        ]
            
                    # Restore complex symbols using the reversed dictionary
        for placeholder, symbol in self.reversed_symbols.items():
            tokens = [tok.replace(placeholder, symbol) for tok in tokens]
            
        return tokens
    
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


linear_a = LinearA()