from .mapper import Mapper

class LinearAMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_a")
    logograms = ("logograms_common", "logograms_unique_linear_a")


linear_a_mapper = LinearAMapper()