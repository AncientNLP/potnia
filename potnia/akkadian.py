from .mapper import Mapper

class AkkadianMapper(Mapper):
    syllabograms = "syllabograms_akkadian_cuneiform"
    logograms = None


akkadian_mapper = AkkadianMapper()