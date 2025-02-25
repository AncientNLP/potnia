import re
from dataclasses import dataclass
from ..script import Script

@dataclass
class Lydian(Script):
    """
    Class for handling text transliteration and unicode conversion to Lydian.

    To use the singleton instance, import like so:
    ``from potnia import lydian``

    Attributes:
        config (str): Path to the configuration file or configuration data in string format. 
                      By default, it uses the 'lydian.yaml file in the 'data' directory.
    """
    config:str = "lydian"



lydian = Lydian()