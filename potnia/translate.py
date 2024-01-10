# Adapted from https://github.com/j-luo93/NeuroDecipher/blob/master/notebooks/Linear_b_simplified.ipynb


LINEAR_B_TO_SYLLABLE = {
    u'𐀀': 'a', u'𐀁': 'e', u'𐀂': 'i', u'𐀃': 'o', u'𐀄': 'u', u'𐀅': 'da', u'𐀆': 'de', 
    u'𐀇': 'di', u'𐀈': 'do', u'𐀉': 'du', u'𐀊': 'ja', u'𐀋': 'je', u'𐀍': 'jo', 
    u'𐀎': 'ju', u'𐀏': 'ka', u'𐀐': 'ke', u'𐀑': 'ki', u'𐀒': 'ko', u'𐀓': 'ku', 
    u'𐀔': 'ma', u'𐀕': 'me', u'𐀖': 'mi', u'𐀗': 'mo', u'𐀘': 'mu', u'𐀙': 'na', 
    u'𐀚': 'ne', u'𐀛': 'ni', u'𐀜': 'no', u'𐀝': 'nu', u'𐀞': 'pa', u'𐀟': 'pe', 
    u'𐀠': 'pi', u'𐀡': 'po', u'𐀢': 'pu', u'𐀣': 'qa', u'𐀤': 'qe', u'𐀥': 'qi', 
    u'𐀦': 'qo', u'𐀨': 'ra', u'𐀩': 're', u'𐀪': 'ri', u'𐀫': 'ro', u'𐀬': 'ru',
    u'𐀭': 'sa', u'𐀮': 'se', u'𐀯': 'si', u'𐀰': 'so', u'𐀱': 'su', u'𐀲': 'ta', 
    u'𐀳': 'te', u'𐀴': 'ti', u'𐀵': 'to', u'𐀶': 'tu', u'𐀷': 'wa', u'𐀸': 'we', 
    u'𐀹': 'wi', u'𐀺': 'wo', u'𐀼': 'za', u'𐀽': 'ze', u'𐀿': 'zo', u'𐁀': 'a2', 
    u'𐁁': 'a3', u'𐁂': 'au', u'𐁃': 'dwe', u'𐁄': 'dwo', u'𐁅': 'nwa', u'𐁆': 'pu2', 
    u'𐁇': 'pte', u'𐁈': 'ra2', u'𐁉': 'ra3', u'𐁊': 'ro2', u'𐁋': 'ta2', u'𐁌': 'twe', u'𐁍': 'two'
}

SYLLABLE_TO_LINEAR_B = {v: k for k, v in LINEAR_B_TO_SYLLABLE.items()}


def to_linear_b(latin_transliterated:str) -> str:
    """ Adapted from https://github.com/j-luo93/NeuroDecipher/blob/master/notebooks/Linear_b_simplified.ipynb """
    syllables = latin_transliterated.split('-')
    symbols = [SYLLABLE_TO_LINEAR_B[syllable] for syllable in syllables]
    return ''.join(symbols)
