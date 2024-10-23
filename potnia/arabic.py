from dataclasses import dataclass
from .mapper import Mapper

@dataclass
class ArabicMapper(Mapper):
    config:str = "arabic"

arabic_mapper = ArabicMapper()