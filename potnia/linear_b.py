import re
from .mapper import Mapper

class LinearBMapper(Mapper):
    syllabograms = ("syllabograms_common", "syllabograms_unique_linear_b")
    logograms = ("logograms_common", "logograms_unique_linear_b")
    patterns_to_ignore = [
        r"vacat\s*\.?",
        r"lat\s*\.",
        r"inf\s*\.",
        r"i\s*\.",
        r"mut\s*\.",
        r"sup\s*\.",
        r"vac\s*\.",
        r"v\s*\.",
        r"vestigia",
        r"l\s*\.",
        r"s\s*\.",
        r"Graffito",
        r"[\/\,\'\?]",
        r"⟦.*?⟧",
        r"deest",
        r"[⸤⸥]",
        r"[\u231e\u231f]",  # Ignore characters ⌞ and ⌟
    ]

    def tokenize_transliteration(self, text:str) -> list[str]:
        """
        Tokenizes Linear B text into individual elements, including words, special characters, and preserving spaces.
        
        Parameters:
        text (str): A string containing Linear B text to be tokenized.
        
        Returns:
        list: A list of tokens extracted from the text.
        """
        # Normalize spaces and remove specific patterns
        text = text.replace('\u00a0', ' ').replace('\u0323', '')
        
        # Remove the '</em>' tag before further processing
        text = text.replace('</em>', '')
        text = text.replace('<em>', '')
        # Special handling to ensure pipes are treated as separate tokens
        text = re.sub(r'\|([^|]+)\|', r'|\1|', text)


        
        # Define placeholders for complex symbols
        complex_symbols = {
            'TELA-[;1+TE': 'PLACEHOLDER_TELA1',
            'TELA;1+TE': 'PLACEHOLDER_TELA2',
            'TELA-[;1]-+TE': 'PLACEHOLDER_TELA3',
            'OVIS]-:m':'PLACEHOLDER_OVIS'
        }
        
        # Reverse the complex_symbols dictionary
        reversed_symbols = {v: k for k, v in complex_symbols.items()}

        # Replace complex symbols with placeholders
        for symbol, placeholder in complex_symbols.items():
            text = text.replace(symbol, placeholder)
        
        # Handle specific compound tokens like 'ME<±RI>'
        text = re.sub(r'ME<±RI>', 'ME±RI', text)
        
        # Normalize the text by replacing double dashes with a single dash
        text = re.sub(r'--', '-', text)
        
        # Combine animal ideograms followed by 'x', 'm', or 'f' without space
        animals = ['EQU', 'SUS', 'OVIS', 'BOS', 'CAP']
        text = re.sub(r'\b(' + '|'.join(animals) + r')\s+(x|m|f)\b', r'\1\2', text)
        
        # Preprocess 'fragmentum A' and 'fragmentum B' to ensure they are not split
        text = re.sub(r'fragmentum A', 'fragmentum_A', text)
        text = re.sub(r'fragmentum B', 'fragmentum_B', text)
        
        
        
        # Explicit tokenization for half brackets
        text = text.replace('⌜', ' ⌜ ').replace('⌝', ' ⌝ ')
        
        text = text.replace('mutila', ' mutila ')
        
        # List of patterns and their replacements
        patterns = [
            # (r'(?<=\S)\?', ' ?'),  # Ensure '?' is separated when it follows a character
            (r'\b({})\s([mf])\b'.format('|'.join(['BOS', 'SUS', 'OVIS', 'CAP', 'EQU'])), r'\1\2'),  # Combine terms with 'm' or 'f'
            (r'\](?=[^\s])', r']-'),  # Pre-process ']' and '[' for special handling
            (r'(?<=[^\s])\[', r'-['),
            (r"TELA\s+(?=[1234x]\b)", r'TELA'), # Existing code for specific cases
            (r"TELA\s+(\d+)", r'TELA \1'), # Updated to handle other numbers with space
            (r'\* (\d+)', r'*\1'),  # Combine '*' with the following numeral
            (r'\+ ([^\s]+)', r'+\1'),  # Combine '+' with surrounding ideograms
            (r'([^\s]) \+', r'\1+'),  # Ensure '+' is properly attached
            (r'([^\s]+) VAS', r'\1VAS'),  # Attach 'VAS' properly
            # Ignore or modify specific patterns
            *[(rf'\b{term}\s?\.', term + '.') for term in ['vac', 'vest', 'l', 's', 'lat', 'inf', 'mut', 'sup', 'i']],  # Refactored for brevity
            (r'\b(supra sigillum|reliqua pars sine regulis|vacat)\b', r'\1'),  # Explicit tokenization
            # Corrected regex pattern to tokenize specific characters            
        ]

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)

        # Space handling
        space_placeholder = "\uE000"  # Placeholder for spaces
        text = re.sub(r' ', space_placeholder, text)

        special_chars_pattern = r'(\[|\]|\,|\'|\u27e6|\u27e7|-|\?|<|>|⌞|⌟|⸤|⸥|\||' + re.escape(space_placeholder) + ')'
        tokens = re.split(special_chars_pattern, text)

        # Replace placeholder with actual space and filter empty tokens
        tokenized = [tok if tok != space_placeholder else " " for tok in tokens if tok and tok!="-"]
        
        # Replace placeholder with actual space and filter empty tokens
        tokenized = [tok.replace('fragmentum_A', 'fragmentum A').replace('fragmentum_B', 'fragmentum B') if tok != space_placeholder else " " for tok in tokens if tok and tok != "-"]

        # Restore specific tokens like 'ME±RI' to their original form
        tokenized = [tok.replace('ME±RI', 'ME<±RI>') for tok in tokenized]
        
        # Restore complex symbols using the reversed dictionary
        for placeholder, symbol in reversed_symbols.items():
            tokenized = [tok.replace(placeholder, symbol) for tok in tokenized]
        
        return tokenized if tokenized else [""]

    def regularize(self, text: str) -> str:
        
        print(text)
        
        patterns = [
            (r'\[?•~•~•~•\]?', '%%%%'),  # Matches '•~•~•~•' or '[•~•~•~•]' with optional brackets
            (r'\[?•~•~•\]?', '%%%'),     # Matches '•~•~•' or '[•~•~•]'
            (r'\[?•~•~\]?', '%%'),       # Matches '•~•~' or '[•~•~]'
            (r'\[?•~•\]?', '%%'),        # Matches '•~•' or '[•~•]'
            (r'\<|\>', ''),              # Remove '<' and '>' characters
        ]
        
        text=text.replace("|","")
        text=text.replace(":","")
        text=text.replace("r.","")
        text=text.replace("[•~]","")
        
        # Remove half brackets
        text = text.replace('⌜', '').replace('⌝', '')
        
        text = text.replace('mutila', '')

        # Apply each pattern replacement in order
        for pattern, replacement in patterns:
            text = re.sub(pattern, replacement, text)
                    
        text = re.sub(r'\[ \]', '[ ]', text)  # Ensure brackets with spaces remain
    
        text = re.sub(r'ro2', '𐁊', text)  # Replace 'ro2' after initial transliterations are done
        text = re.sub(r"vestigia", "%", text)
        # Replace 'qs' only when it appears as a standalone word
        text = re.sub(r'\bqs\b', '%', text)
        text = re.sub(r"vest\s*\.", "%", text)
        text = re.sub(r"\[•\]", "%", text)
        # Additional cleanup for specific phrases and codes
        text = re.sub(r'supra sigillum|CMS \w+\d+[A-Z]* \d+', '', text)
        text = re.sub(r'reliqua pars sine regulis', '', text)
        text = re.sub(r'[αβγ]', '', text)
        text=re.sub(r'v\.→','',text)
        text=re.sub(r'v\.↓','',text)
        text=re.sub(r'v\.','',text)
        text = re.sub(r'\b(vacat|sup. mut.|inf. mut.|deest|X|fragmentum A|fragmentum B|graffito|angustum|prior pars sine regulis|fragmentum C|fragmentum D|fragmentum separatum|α|β|γ|δ|sigillum|)\b', '', text)  
        text = re.sub(r'\b(x|m|f)\b', '', text)  # Remove 'x', 'm', 'f' if standalone (could be adjusted based on context)
        text = re.sub(r'[\[\]]', "%", text)  # Replace standalone brackets with "%"
        
        # Remove any remaining standalone brackets
        text = re.sub(r'[\[\]]', "%", text)
        text = re.sub(r'=[^ ]*', '', text)
        text = re.sub(r'•', "%", text)
        text = re.sub(r'●', "", text)
        text = re.sub(r'dex.', '', text)
        text = re.sub(r'sin.', '', text)        
        # # Handle special sequences with wildcards for uncertainty or missing elements
            
        text = super().regularize(text)
        


        informative_chars = set(list(re.sub(r'[%\s]', "", text)))
        if len(informative_chars) == 0:
            return ""
        
        return text

linear_b_mapper = LinearBMapper()
