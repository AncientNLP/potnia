# Linear B Conversion Rules

This document outlines the rules used in the conversion process for Linear B texts. The process involves tokenization, regularization, and handling of special patterns to prepare the text for further analysis.

## 1. Tokenization Rules

Tokenization is the process of breaking down the text into individual elements or tokens. For Linear B, this involves handling various special cases and patterns.

### a) Space Normalization

Replaces non-breaking spaces and certain diacritic marks with regular spaces and empty strings respectively, cleaning up the text for uniform processing.

- Replace non-breaking spaces (`\u00a0`) with regular spaces.
- Remove combining dot below (`\u0323`) to simplify character representation.

### b) Special Pattern Handling

| Pattern | Regex | Description |
|---------|-------|-------------|
| Combine terms with 'm' or 'f' | `r'\b({})\s([mf])\b'.format('\|'.join(['BOS', 'SUS', 'OVIS', 'CAP', 'EQU']))` to `r'\1\2'`| Combines terms like 'BOS', 'SUS', 'OVIS', 'CAP', 'EQU' with following 'm' or 'f' to form a single token, facilitating cleaner tokenization. |
| Add hyphen after ']' | `r'\](?=[^\s])'` to ` r']-'` | Adds a hyphen right after ']' when it is followed by a non-space character, maintaining syntax integrity in tokenization. |
| Add hyphen before '[' | `r'(?<=[^\s])\['` to `r'-['` | Inserts a hyphen right before '[' when it is preceded by a non-space character, ensuring consistent formatting for special handling. |
| TELA Number Combination | `r"TELA\s+(\d+)"` to `r'TELA\1'` | Combines the term "TELA" with following numbers without spaces. |
| Combine '*' with numeral | `r'\* (\d+)'` to `r'*\1'` | Directly attaches '*' to the following numeral without a space, aiding in recognizing these combinations as distinct tokens. |
| Combine '+' with ideograms | `r'\+ ([^\s]+)'` and `r'([^\s]) \+'` | Merges '+' with adjacent ideograms without space, preserving semantic units in tokenization. |
| Attach 'VAS' | `r'([^\s]+) VAS'` to `r'\1VAS'` | Attaches 'VAS' directly to the preceding term without space, ensuring that it is processed as a single token. |
| Handle abbreviations | `*[(rf'\b{term}\s?\.', term + '.') for term in ['vac', 'vest', 'l', 's', 'lat', 'inf', 'mut', 'sup', 'i']]` | Ensures common abbreviations (like 'vac', 'inf', etc.) are correctly punctuated with a period if missing, standardizing text format. |

Iterates over each pattern-replacement pair, applying them sequentially to the text to ensure all intended formatting and corrections are made.

### c) Space Handling :

Uses a placeholder character to temporarily replace spaces, facilitating token splitting based on special characters and preserved spaces.

```python
space_placeholder = "\uE000"  # Placeholder for spaces
text = re.sub(r' ', space_placeholder, text)
```

### d) Tokenization with Space Placeholder

Splits the text based on special characters and the space placeholder, ensuring that meaningful elements like brackets, commas, and quotation marks are preserved as separate tokens.

```python
special_chars_pattern = r'(\[|\]|\,|\'|\u27e6|\u27e7|-|\?|\u2e24|\u2e25|' + re.escape(space_placeholder) + ')'
tokens = re.split(special_chars_pattern, text)
```

### e) Final Tokenization

Replace the placeholder with actual spaces and filter empty tokens:

```python
tokenized = [tok if tok != space_placeholder else " " for tok in tokens if tok and tok != "-"]
```

These rules form the core of the Linear B conversion process, handling various special cases in the transliteration, tokenization, and regularization of the text. The process aims to preserve important linguistic features while standardizing the format for further processing or analysis. This standardization is crucial for consistent treatment of texts across different sources and editions.

## 2. Regularization Rules:

This list of regular expressions identifies various patterns in the text that should be tokenised as is, but then removed or handled as a special case during regularization.

- `lat., l., inf., i., sup., s., dex., mut, verso, v., v.→, v.↓, Graffito, vacat, vac., deest, α, β, γ, supra sigillum, reliqua pars sine regulis`: Various annotations related epigraphic features of the document, which should be removed at this step.
- `fragmentum, qs, vestigia, vest.` and `][•`: Various annotations or specific punctuation denoting undetermined text parts, which should be handled as wildcards at this step (i.e. converted to `%`).
- `/,'?⸤⸥<>`: Specific punctuation and bracket types, which should be removed at this step.
- `⟦.*?⟧`: Matches text within these special double brackets, which indicate text erasures. Both punctuation and included text should be removed at this step.

