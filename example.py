from potnia import linear_b
text = "po-ti-ni-ja"

tokens = linear_b.tokenize_transliteration(text)
print(tokens) # Output: ['po', 'ti', 'ni', 'ja']

unicode_text = linear_b(text)
print(unicode_text) # Output: 𐀡𐀴𐀛𐀊


