from .mapper import Mapper

class ArabicMapper(Mapper):
    syllabograms = "arabic_symbols"
    transliteration_rules = "rules/transliteration_rules_arabic.yaml"
    logograms = None


arabic_mapper = ArabicMapper()