import re
from dataclasses import dataclass
from .mapper import Mapper

@dataclass
class ArabicMapper(Mapper):
    config:str = "arabic"

    def to_unicode(self, text:str, regularize:bool=False) -> str:
        # if word ends with 'atun' then make it damataan with taa marbuta
        text = re.sub(r'(\w\w)atun\b', r'\1'+'َ\u0629\u064C', text)
        # if word has uʾ then make it a hamza on top of waw
        text = re.sub(r'uʾ', '\u0624', text)
        # if word ends with 'un' then make it damataan
        text = re.sub(r'(\w\w)un\b', r'\1'+'\u064C', text)
        # if word ends with 'in' then make it kasrataan
        text = re.sub(r'(\w\w)in\b', r'\1'+'\u064D', text)
        # if word ends with 'an' then make it fatatan
        text = re.sub(r'(\w\w)an\b', r'\1'+'\u064Bا', text)
        # definite article
        text = re.sub(r'al-', "ٱل", text)
        # if word starts with 'i' then make it fataan alif
        text = re.sub(r'\b[ia]', 'ا', text)

        text = super().to_unicode(text, regularize)
        arabic_consonants_with_shadda = [
            'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 
            'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 
            'ه', 'و', 'ي'
        ]
        for consonant in arabic_consonants_with_shadda:
            text = re.sub(f'{consonant}{consonant}', f'{consonant}\u0651', text)

        return text


arabic_mapper = ArabicMapper()