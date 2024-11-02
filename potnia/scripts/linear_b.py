import re
from dataclasses import dataclass
from ..script import Script

@dataclass
class LinearB(Script):
    """
    Class for handling text transliteration and unicode conversion for Linear B.

    To use the singleton instance, import like so:
    ``from potnia import linear_b``

    Designed especially for texts from DĀMOS (Database of Mycenaean at Oslo): https://damos.hf.uio.no/
    and LiBER (Linear B Electronic Resources): https://liber.cnr.it/

    Attributes:
        config (str): Path to the configuration file or configuration data in string format. 
                      By default, it uses the 'linear_a.yaml file in the 'data' directory.
    """
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
