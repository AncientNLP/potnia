import re
from dataclasses import dataclass
from .mapper import Mapper

@dataclass
class ArabicMapper(Mapper):
    config:str = "arabic"

    def to_unicode(self, text:str, regularize:bool=False) -> str:
        # if word ends with 'atun' then make it damataan with taa marbuta
        text = re.sub(r'(\w)atun\b', r'\1'+'َ\u0629\u064C', text)
        # if word has uʾ then make it a hamza on top of waw
        text = re.sub(r'uʾ', '\u0624', text)
        # if word ends with 'un' then make it damataan
        text = re.sub(r'(\w)un\b', r'\1'+'\u064C', text)
        # if word ends with 'in' then make it kasrataan
        text = re.sub(r'(\w)in\b', r'\1'+'\u064D', text)
        # if word ends with 'an' then make it fatatan
        text = re.sub(r'(\w)an\b', r'\1'+'\u064Bا', text)


        return super().to_unicode(text, regularize)


arabic_mapper = ArabicMapper()