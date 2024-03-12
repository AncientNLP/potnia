# import re
# from typing import List
# import yaml

# # Adapted from https://github.com/j-luo93/NeuroDecipher/blob/master/notebooks/Linear_b_simplified.ipynb


# from potnia.mapping import AEGEAN_SYLLABOGRAMS_TO_SYLLABLE

# breakpoint()

# LINEAR_A_SYLLABOGRAMS_TO_SYLLABLE = dict(AEGEAN_SYLLABOGRAMS_TO_SYLLABLE)

# LINEAR_B_SYLLABOGRAMS_TO_SYLLABLE = dict(AEGEAN_SYLLABOGRAMS_TO_SYLLABLE)
# LINEAR_B_SYLLABOGRAMS_TO_SYLLABLE.update({
#     u'𐁃': 'dwe', u'𐁄': 'dwo', u'𐁅': 'nwa', u'𐁆': 'pu2', 
#     u'𐁇': 'pte', u'𐁈': 'ra2', u'𐁉': 'ra3', u'𐁊': 'ro2', u'𐁋': 'ta2', u'𐁌': 'twe', u'𐁍': 'two'
# })



# LINEAR_B_TO_SYLLABLE = {
#     u'𐀀': 'a', u'𐀁': 'e', u'𐀂': 'i', u'𐀃': 'o', u'𐀄': 'u', u'𐀅': 'da', u'𐀆': 'de', 
#     u'𐀇': 'di', u'𐀈': 'do', u'𐀉': 'du', u'𐀊': 'ja', u'𐀋': 'je', u'𐀍': 'jo', 
#     u'𐀎': 'ju', u'𐀏': 'ka', u'𐀐': 'ke', u'𐀑': 'ki', u'𐀒': 'ko', u'𐀓': 'ku', 
#     u'𐀔': 'ma', u'𐀕': 'me', u'𐀖': 'mi', u'𐀗': 'mo', u'𐀘': 'mu', u'𐀙': 'na', 
#     u'𐀚': 'ne', u'𐀛': 'ni', u'𐀜': 'no', u'𐀝': 'nu', u'𐀞': 'pa', u'𐀟': 'pe', 
#     u'𐀠': 'pi', u'𐀡': 'po', u'𐀢': 'pu', u'𐀣': 'qa', u'𐀤': 'qe', u'𐀥': 'qi', 
#     u'𐀦': 'qo', u'𐀨': 'ra', u'𐀩': 're', u'𐀪': 'ri', u'𐀫': 'ro', u'𐀬': 'ru',
#     u'𐀭': 'sa', u'𐀮': 'se', u'𐀯': 'si', u'𐀰': 'so', u'𐀱': 'su', u'𐀲': 'ta', 
#     u'𐀳': 'te', u'𐀴': 'ti', u'𐀵': 'to', u'𐀶': 'tu', u'𐀷': 'wa', u'𐀸': 'we', 
#     u'𐀹': 'wi', u'𐀺': 'wo', u'𐀼': 'za', u'𐀽': 'ze', u'𐀿': 'zo', u'𐁀': 'a2', 
#     u'𐁁': 'a3', u'𐁂': 'au', u'𐁃': 'dwe', u'𐁄': 'dwo', u'𐁅': 'nwa', u'𐁆': 'pu2', 
#     u'𐁇': 'pte', u'𐁈': 'ra2', u'𐁉': 'ra3', u'𐁊': 'ro2', u'𐁋': 'ta2', u'𐁌': 'twe', u'𐁍': 'two'
# }

# SYLLABLE_TO_LINEAR_A
# SYLLABLE_TO_LINEAR_B = {v: k for k, v in LINEAR_B_TO_SYLLABLE.items()}


# # Define a function to tokenize text data from Linear B documents
# def tokenize_linear_b(text:str) -> List[str]:
#     """
#     Tokenizes Linear B text into individual elements, including words and special characters.
    
#     Parameters:
#     text (str): A string containing Linear B text to be tokenized.
    
#     Returns:
#     list: A list of tokens extracted from the text.
#     """
#     # Remove \u0323 from the text
#     text = text.replace('\u0323', '')

#     # Define a regex pattern for special characters treated as separate tokens, including \u27e6 and \u27e7
#     special_chars_pattern = r'(\[|\]|\,|\'|\u27e6|\u27e7)'
#     # Split the text on spaces to get initial tokens
#     tokens = text.split()

#     # Initialize a list to store final tokenized elements
#     tokenized = []

#     # Process each token for further splitting
#     for token in tokens:
#         # Split the token based on special characters
#         split_tokens = re.split(special_chars_pattern, token)
#         # Further split tokens containing hyphens
#         for tok in split_tokens:
#             if tok:  # Ensure token is not empty
#                 if '-' in tok:
#                     # Split on hyphen and include it as a separate token
#                     hyphen_split = re.split('(-)', tok)
#                     tokenized.extend(hyphen_split)
#                 else:
#                     tokenized.append(tok)

#     # Filter out empty tokens
#     tokenized = [tok for tok in tokenized if tok and tok != '-']

#     return tokenized


# def tokenize_linear_a(text:str) -> List[str]:
#     """
#     Tokenizes the input text according to specific rules:
#     - '[?]' is treated as a single token
#     - '[' and ']' are individual tokens
#     - '-' is a token on its own, except when part of '[?]'
#     - Regular words and characters are tokenized based on these delimiters
    
#     Parameters:
#         text (str): The text to tokenize.
    
#     Returns:
#         list[str]: A list of tokens following the specified rules.
#     """
#     # Define a regular expression pattern to match '[?]', '[', ']', and '-',
#     # along with sequences of characters that do not include these special characters
#     pattern = re.compile(r'\[\?\]|[\[\]-]|[^[\]\-]+')
#     tokens = pattern.findall(text)
#     return [token for token in tokens if token != "-"]


# def to_linear_b_word(latin_transliterated_word:str) -> str:
#     syllables = tokenize_linear_b(latin_transliterated_word)
#     symbols = [SYLLABLE_TO_LINEAR_B[syllable] for syllable in syllables]
#     return ''.join(symbols)


# def to_linear_b(latin_transliterated:str) -> str:
#     """ Adapted from https://github.com/j-luo93/NeuroDecipher/blob/master/notebooks/Linear_b_simplified.ipynb """
#     words = re.split(r"\s+", latin_transliterated)
#     words = [to_linear_b_word(word) for word in words]
#     result = ' '.join(words)
#     return result


# def to_linear_a_word(latin_transliterated_word:str) -> str:
#     syllables = tokenize_linear_a(latin_transliterated_word)
#     symbols = [SYLLABLE_TO_LINEAR_A[syllable] for syllable in syllables]
#     return ''.join(symbols)


# def to_linear_a(latin_transliterated:str) -> str:
#     words = re.split(r"\s+", latin_transliterated)
#     words = [to_linear_a_word(word) for word in words]
#     result = ' '.join(words)
#     return result


