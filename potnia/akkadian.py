from dataclasses import dataclass
from .mapper import Mapper


@dataclass
class AkkadianMapper(Mapper):
    config:str = "akkadian"


akkadian_mapper = AkkadianMapper()