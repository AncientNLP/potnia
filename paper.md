---
title: 'Introducing Potnia: A Python language library for the conversion of ancient texts to Unicode'
tags:
  - Python
  - Unicode 
  - ancient texts
  - ancient scripts
  - ancient languages
  - transliteration
  - machine learning
authors:
  - name: Emily Tour
    orcid: 0000-0001-5212-1427
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    corresponding: true
    affiliation: "1" 
  - name: Kabir Manandhar Shrestha
    orcid: 0009-0001-2059-1683
    equal-contrib: true
    affiliation: 2
  - name: Robert Turnbull
    orcid: 0000-0003-1274-6750
    corresponding: false
    equal-contrib: true
    affiliation: 2
affiliations:
 - name: University of Melbourne, Australia
   index: 1
 - name: Melbourne Data Analytics Platform, Australia
   index: 2
date: 23 September 2024
bibliography: paper.bib
---

# Summary

Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into their respective Unicode representations. The increasing digitization of ancient language corpora has led to significant progress in fields such as Optical Character Recognition (OCR), textual restoration, palaeographic analysis and machine translation (reference). However, many of these datasets are still presented in Romanized transliteration, rather than a representation of their original script, despite the availability of Unicode blocks for numerous ancient scripts. This discrepancy presents challenges for accurate linguistic representation and computational analysis.

Potnia addresses this gap by providing a flexible, extensible framework for converting transliterated texts to Unicode. The library's initial release supports texts using the Linear B script, with plans to expand functionality to other ancient scripts, including Linear A, Akkadian cuneiform, Hittite cuneiform, Luwian hieroglyphs and Etruscan. By facilitating the conversion of digitized transliterated corpora into Unicode, Potnia enables more accurate tokenization for downstream tasks such as machine learning-based textual analysis, enhancing the capabilities of digital humanities and computational linguistics in the study of ancient languages.

# Statement of need

The application of machine learning to the study of ancient scripts has grown significantly in recent years, emphasizing the need for datasets represented in their original scripts rather than Romanized transliterations. While the Unicode Standard provides the means to encode a large number of ancient scripts, a substantial portion of data continues to be distributed as transliterations due to legacy digitization practices.

Transliteration is the process of converting text from its original script into a different script, using systematic processes. Its primary intention is to allow those who can understand the secondary script to comprehend the 'spelling' and approximate pronunciation of the original text (reference). Prior to the gradual introduction of relevant Unicode blocks since the 1990s, it was also usually necessary for representing non-Latin scripts on Western computational systems, which were largely confined to letters of the Latin alphabet and a small number of special characters. However, it is well acknowledged that transliteration can only ever achieve an approximation of the original text, with difficulties in mapping exact sound values across different scripts, as well as a broader lack of standardised transliteration practices (references). As such, a range of ambiguities and distortions can arise from the transliteration process, particularly for many ancient scripts and their underlying languages, where our understanding of them continues to evolve. 

For example:
  - Different notation systems can assign the same symbol with different transliterated values (e.g. 𒀞 in Akkadian cuneiform is variously represented as mè in the French tradition, and me3 in the German tradition).
  - Opinions on the values of signs can change over time, which could potentially introduce differences between older and newer transliterations (e.g. 𐀤 in the Linear B script was originally assigned the value pa2, but later updated to 'qa').
  - Transliteration can obscure polyvalency in scripts, where a single sign can represent multiple different values (e.g. 𒄯 in Hittite cuneiform can represent three different phonemes, transliterated as 'ḫar', 'ḫur' and 'mur', as well as three different logograms meaning 'ring', 'thick' and 'lung').

Transliteration has an important place in aiding new learners of an ancient script to understand the pronunciation and orthography of the underlying language it represents (particularly for non-alphabetic scripts, where beginners need to grasp a vast repertoire of unfamiliar signs) (reference). However, we suggest that for language modelling, the aforementioned features of transliteration only add unwanted noise and distortions to the process, and therefore it is preferable to represent digitized texts using the original signs. Some digital corpora for more more well-known ancient language corpora are already offered in using Unicode representations, including ancient Greek (e.g. Perseus) and ancient Hebrew (e.g. dataset name?). Given the increasing availability of Unicode blocks encoding the sign repertoires of less well-resourced ancient scripts, we are now able to offer this functionality through 'Potnia'.

Commonly, transliterations of ancient texts are also heavily annotated, with special characters used to denote a range of features including uncertain readings, missing or damaged elements, erasures, non-textual marks, and annotations by modern transliterators pertaining to structural or physical elements of the document. If not removed or handled appropriately, these have the potential to introduce further noise into language models. Potnia is equipped to provide specific handling of these elements, with tailored tokenization and regularization rules pertaining to both script-specific and corpus-specific conventions. For example, general transliteration rules for the Linear B script have been encoded, in addition to specific conventions used by the different LiBER and DĀMOS datasets, which are the two most comprehensive digitised Linear B corpuses that are currently available.

Potnia's focus on ancient languages and its extensible architecture make it a valuable asset for researchers working with digitized ancient corpora. It facilitates a key pre-processing step in the language modelling pipeline, with the resulting outputs providing a Unicode representation of the texts in their original script, thereby enabling more accurate and nuanced computational analysis of these texts in downstream modelling tasks.

# Implementation

Potnia is implemented in Python, leveraging object-oriented design principles for extensibility. The core functionality revolves around the `Mapper` class, which handles the conversion between transliterated text and Unicode representations. 

Key features of the implementation include:
- Use of YAML files for storing mapping data, allowing for easy updates and additions
- Regular expressions for handling complex patterns in ancient texts
- A flexible tokenization system that can be customized for different scripts
- Comprehensive error handling and input validation

Here's a simple example of using Potnia to convert a Linear B transliteration to Unicode:

```python
from potnia import linear_b_mapper

text = "po-ti-ni-ja"
unicode_text = linear_b_mapper(text, regularize=True)
print(unicode_text)  # Output: 𐀡𐀴𐀛𐀊
```

Potnia's architecture is designed to handle the inherent complexities of ancient scripts. The LinearBMapper class, for instance, extends the base Mapper class to implement specific rules for Linear B, including handling of syllabograms, logograms, and special characters. This modular design allows for easy extension to other ancient scripts.

The library uses PyYAML for efficient data loading and management of character mappings. Regular expressions are extensively used for tokenization and text normalization, ensuring robust handling of various text formats and notations commonly found in transliterated ancient texts.

# Research Application

Potnia’s design and functionality address several key challenges in the analysis of ancient texts:

1. **Unicode Conversion:** By converting transliterated texts into their original scripts in Unicode, Potnia supports more accurate downstream processing, especially for machine learning applications.

2. **Tokenization and Regularization:** The library implements specialized tokenization and regularization strategies to manage characters pertaining to uncertain readings, erasures, non-textual marks, tablet damage and other structural or physical elements of ancient texts, as well as annotations added by modern transliterators. It handles script- and corpus-specific rules for dealing with missing or ambiguous elements, improving the accuracy of linguistic analysis.

3. **Extensibility:** Potnia's design allows for the addition of new scripts by integrating script-specific rules for tokenization and conversion. This makes the library suitable for a wide range of ancient languages, providing a valuable tool for researchers across different fields of ancient studies.

4. **Testing and Reliability:** The library includes a comprehensive test suite, with test cases written in YAML for easy expansion. This ensures the reliability of conversions and simplifies contributions from the open-source community.

5. **Integration with Research Workflows:** Researchers can easily incorporate Potnia into their existing workflows. For example, in a typical research scenario, Potnia could be used to preprocess a corpus of Linear B texts before feeding them into a machine learning model for further analysis:

```python
from potnia import linear_b_mapper
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load corpus
corpus = pd.read_csv('linear_b_corpus.csv')

# Convert transliterations to Unicode
corpus['unicode_text'] = corpus['transliterated_text'].apply(lambda x: linear_b_mapper(x, regularize=True))

# Perform further analysis (e.g., bag-of-words representation)
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(corpus['unicode_text'])

# Continue with machine learning tasks...
```

This integration allows researchers to leverage the benefits of Unicode representation in various computational linguistics tasks, potentially improving the accuracy and interpretability of their analyses.

At present, full functionality for the Linear B script (used to encode the Mycenaean Greek language) is offered within the library. Forthcoming support for for a range of additional scripts is under development, including Linear A, Akkadian cuneiform, Hittite cuneiform, Luwian hieroglyphs and Etruscan. This functionality positions Potnia as an essential tool for researchers working with digitized ancient language corpora.

# Community Guidelines and Future Work

Potnia is open-source software released under the Apache 2.0 license. We welcome contributions from the community, including bug reports, feature requests, and pull requests. Issues can be reported on our GitHub repository .

<!-- 
# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% } -->

# Acknowledgements

We acknowledge support from Brent Davis, Kim Doyle, Man-Hua (Kate) Chu, Anhui (Ellie) Situ and Stavroula (Stephie) Nikoloudis. This research was supported by The University of Melbourne’s Research Computing Services.


# References
