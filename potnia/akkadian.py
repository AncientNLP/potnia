from .mapper import Mapper
from dataclasses import dataclass


@dataclass
class AkkadianMapper(Mapper):
    config:str = "akkadian"


akkadian_mapper = AkkadianMapper()