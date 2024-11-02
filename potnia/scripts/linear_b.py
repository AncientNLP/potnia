import re
from dataclasses import dataclass
from ..script import Script

@dataclass
class LinearB(Script):
    config:str = "linear_b"

    def regularize(self, text: str) -> str:
        """
        Applies regularization rules to a given string.

        Args:
            string (str): Text string to be regularized.

        Returns:
            str: Regularized text string.
        """
        text = super().regularize(text)

        # Ensure there are informative characters left in the text
        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""

        return text

    def tokenize_unicode(self, text:str) -> list[str]:
        """
        Tokenizes a unicode string by splitting and joining words with dashes.

        Args:
            text (str): Input text in unicode format.

        Returns:
            list[str]: List of tokenized strings.
        """
        words = ['-'.join(word) for word in text.split()]
        text = ' '.join(words)
        return list(text)


linear_b = LinearB()
