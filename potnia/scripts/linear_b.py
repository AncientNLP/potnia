import re
from dataclasses import dataclass
from ..script import Script

@dataclass
class LinearB(Script):
    config:str = "linear_b"

    # syllabograms = (
    #     "syllabograms_common", 
    #     "syllabograms_unique_linear_b",
    # )
    # logograms = (
    #     "logograms_common", 
    #     "logograms_unique_linear_b",
    # )
    # patterns_to_ignore = "rules/ignore_patterns_linear_b.yaml"
    # regularization_rules = "rules/regularization_rules_linear_b.yaml"
    # transliteration_rules = "rules/transliteration_rules_linear_b.yaml"

    def regularize(self, text: str) -> str:
        text = super().regularize(text)

        # Ensure there are informative characters left in the text
        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""

        return text


linear_b = LinearB()
