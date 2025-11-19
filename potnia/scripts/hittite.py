from dataclasses import dataclass
from ..script import Script
import unicodedata
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

    def tokenize_transliteration(self, input_string:str) -> list[str]:
        """
        Tokenizes transliterated text according to specific patterns.

        Args:
            text (str): Input text in transliterated format.

        Returns:
            list[str]: List of tokens
        """
        # Normalize Unicode to NFC (canonical composition)
        input_string = unicodedata.normalize("NFC", input_string)
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
            elif char in ['-','‑','.','+','˽']:
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

    def remove_epigraphic_annotations(self, text):
        """
        Removes some epigraphic annotations that has appeared in the text portion of a few hundred documents in HPM.
        """
        # this kind of parsing probably belongs in Ancient Corpora.
        text = re.sub(r"obv \d+′ ", "", text)
        text = re.sub(r'Frg( \d)+( [VR]s)( [IVX]+)?( \d+)′?', '', text)
        text = re.sub('Ende [VR]s[.]? ?[IVX]*', '', text)
        text = re.sub('[VR]s[.]?[?!]?( lk.)?( Kol.)? ?[IVX/]*[?]* bricht ab', '', text)
        text = re.sub('ca [0-9-]+ (Zeichen|segni)', '', text)

        epigraphic_annotations = [
            'ca. 15 unbeschriebene Zeilenenden Rs. IV bricht ab',
            'ca. 3 Zeilenanfänge unbeschrieben r. Kol. des lk. Rd. bricht ab',
            'ca. 4 unbeschriebene Zeilenanfänge Rs. lk. Kol. bricht ab',
            'ca. 6 Zeilen unbeschrieben // Tafelende Rs. IV bricht ab',
            'erhaltener Teil einer Zeile unbeschrieben Rs. VI bricht ab',
            'erhaltener Teil von ca. 2 Zeilen unbeschrieben Rs. IV bricht ab',
            'erhaltener Teil von ca. 7 Zeilen unbeschrieben Rs. bricht ab',
            'erhaltener Teil von ca 17 Zeilen unbeschrieben Tafelende',
            'erhaltener Teil von ca. 17 Zeilen unbeschrieben Tafelende',
            'unbeschriebene Zeilen, dann bricht der Text ab',
            'nach ca. 2 unbeschriebene Zeilen bricht die Tafel ab',
            'Rs. VI? bricht ca. 3 Zeilen vor Kolumnenende ab',
            'Text bricht ab',
            'lk. Kol. bricht ab',
            'lk. Rd. bricht ab',
            '\" lg=\"Hit\"/>',
            'Kolophon',
            ' "/>',
            'breaks off',
            # other ca formulations
            'ca'
        ]
        for annotation in epigraphic_annotations:
            text = text.replace(annotation, '')

        # túḫ<span class="MaterLect">uḫ</span>-ša should be parsed as túḫ.uḫ-ša
        text = text.replace('túḫuḫ', 'túḫ.uḫ')

        return text

    def to_unicode(self, text: str, regularize: bool = False) -> str:
        """
        Converts transliterated text to unicode format with additional handling for Hittite-specific cases.
        """
        # Remove editorial markers and brackets before tokenization
        text = text.replace('⸢','').replace('⸣','').replace('[','').replace(']','')
        text = text.replace('〈', '').replace('〉', '').replace('〈', '').replace('〉', '')
        text = text.replace('?', '').replace('*', '').strip()

        text = self.remove_epigraphic_annotations(text)

        tokens = self.tokenize_transliteration(text)

        tokens = [
            token if ("MEŠ" in token or "meš" in token)
            else token.replace("(", "").replace(")", "")
            for token in tokens
        ]
        result = []

        for token in tokens:
            # Try the original token first
            unicode_char = self.transliteration_to_unicode_dict.get(token)

            # If no match, try the opposite case
            if unicode_char is None:
                opposite = token.lower() if token.isupper() else token.upper()
                unicode_char = self.transliteration_to_unicode_dict.get(opposite, token)

            result.append(unicode_char)

        return "".join(result)

hittite = Hittite()
