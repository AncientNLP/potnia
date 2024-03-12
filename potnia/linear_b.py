from .mapper import Mapper

class LinearBMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_b")
    logograms = ("logograms_common", "logograms_unique_linear_b")


linear_b_mapper = LinearBMapper()