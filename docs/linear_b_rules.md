# Linear B Conversion Rules

This document outlines the rules used in the conversion process for Linear B texts. The process involves tokenization, regularization, and handling of special patterns to prepare the text for further analysis.

## 1. Tokenization Rules

Tokenization is the process of breaking down the text into individual elements or tokens. For Linear B, this involves handling various special cases and patterns.

### a) Space Normalization

Before tokenization, spaces are normalized:

- Replace non-breaking spaces (`\u00a0`) with regular spaces.
- Remove combining dot below (`\u0323`) to simplify character representation.

### b) Special Pattern Handling

| Pattern | Regex | Description |
|---------|-------|-------------|
| Separate '?' | `r'(?<=\S)\?'` | Ensures '?' is separated when it follows a character. |
| Combine terms with 'm' or 'f' | ``r'\b({})\s([mf])\b'.format('\|'.join(['BOS', 'SUS', 'OVIS', 'CAP', 'EQU']))`` | Combines terms like 'BOS', 'SUS', 'OVIS', 'CAP', 'EQU' with following 'm' or 'f'. |
| Add hyphen after ']' | `r'\](?=[^\s])'` | Adds hyphen after ']' when followed by non-space. |
| Add hyphen before '[' | `r'(?<=[^\s])\['` | Adds hyphen before '[' when preceded by non-space. |
| Combine '*' with numeral | `r'\* (\d+)'` | Combines '*' with the following numeral. |
| Combine '+' with ideograms | `r'\+ ([^\s]+)'` and `r'([^\s]) \+'` | Combines '+' with surrounding ideograms. |
| Attach 'VAS' | `r'([^\s]+) VAS'` | Attaches 'VAS' to the preceding term. |
| Handle abbreviations | ```*[(rf'\b{term}\s?\.', term + '.') for term in ['vac', 'vest', 'l', 's', 'lat', 'inf', 'mut', 'sup', 'i']]``` | Handles common abbreviations in Linear B texts. |

### c) Tokenization

After applying the special patterns, the text is split on special characters and spaces:

```python
r'(\[|\]|\,|\'|\u27e6|\u27e7|-|' + re.escape(space_placeholder) + ')'
```

This regex splits on brackets, commas, apostrophes, special Unicode characters, hyphens, question marks, and spaces.

The placeholder for spaces is defined as:

```python
space_placeholder = "\uE000"
```

### d) Final Tokenization

Replace the placeholder with actual spaces and filter empty tokens:

```python
tokenized = [tok if tok != space_placeholder else " " for tok in tokens if tok and tok != "-"]
```

2. Regularization Rules
Regularization standardizes certain elements of the text for consistency:

Rule	Regex	Description
Replace square brackets	r'[\[\]]'	Replaces square brackets with "%", standardizing representation of damaged or reconstructed text.

## 3. Patterns to Ignore

Certain patterns are ignored or removed during processing:

- Latin abbreviations and terms:

    ```python
    r"vacat\s*.?", 
    r"lat\s*.", 
    r"inf\s*.", 
    r"i\s*.", 
    r"mut\s*.",
    r"sup\s*.", 
    r"vac\s*.", 
    r"v\s*.", 
    r"vestigia", 
    r"l\s*.", 
    r"s\s*.",
    r"Graffito"
    ```

    These terms often represent editorial comments or descriptions of the tablet state.

- Punctuation marks: `r"[\/\,\'\?]"` Removes certain punctuation that isn't part of the Linear B text.

- Text within double square brackets: `r"⟦.*?⟧"` Often used for editorial deletions or comments.

- The term `"deest"` Latin for "it is missing," often used in editions.
- Angle brackets: `r"[⸤⸥]"` Used in some editions to indicate partially preserved signs.

These rules form the core of the Linear B conversion process, handling various special cases in the transliteration, tokenization, and regularization of the text. The process aims to preserve important linguistic features while standardizing the format for further processing or analysis. This standardization is crucial for consistent treatment of texts across different sources and editions.