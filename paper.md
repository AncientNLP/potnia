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

Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into their respective Unicode representations. Despite the significant progress made in the digitization of ancient language corpora, many of these datasets are still presented in transliterated form rather than in their original scripts. This issue persists even though Unicode blocks exist for many ancient scripts, limiting the precision of linguistic analysis.

Potnia bridges this gap by providing a flexible framework for converting transliterations into Unicode, ensuring more accurate representation of ancient texts. By enabling tokenization and processing in the original script, Potnia enhances tasks such as textual restoration and machine learning-based analysis. The library currently supports Linear B, with future expansions planned for Linear A, Akkadian cuneiform, Hittite cuneiform, Luwian hieroglyphs, and Etruscan. This tool positions itself to be valuable for both computational linguistics and digital humanities, helping researchers work with ancient texts in their original script.

# Statement of Need

While machine learning has increasingly been applied to the study of ancient languages [@sommerschieldMachineLearningAncient2023], some of this progress has involved working with transliterated texts rather than native script formats. Although Unicode standards exist for many ancient scripts, transliterated texts remain prevalent due to historical digitization practices.

Transliteration is the process of converting text from its original script into a different script, using systematic processes. Its primary intention is to allow those who can understand the secondary script to comprehend the 'spelling' and approximate pronunciation of the original text (reference).  Prior to the gradual introduction of relevant Unicode blocks since the 1990s, it was also usually necessary for representing non-Latin scripts on Western computational systems, which were largely confined to letters of the Latin alphabet and a small number of special characters.

Transliteration has an important place in aiding new learners of an ancient script to understand the pronunciation and orthography of the underlying language it represents (particularly for non-alphabetic scripts, where beginners need to grasp a vast repertoire of unfamiliar signs) (reference). However, it is well recognised that this process can only provide an approximate, and often unsatisfactory or disputed, representation of the original script (references). A lack of standardisied approaches to transliteration in particular can introduce significant ambiguity and noise to the dataset, for example:

  - the use of different notation systems (e.g. where 𒀞 in Akkadian cuneiform can be represented as either 'mè' or 'me\u2083');
  - changing opinions on sign values over time, introducing possible differences between older and newer transliterations (e.g. 𐀤 in the Linear B script changing from the accepted value of 'pa2' to 'qa');
  - and the way in which transliteration obscures polyvalency in scripts, where a single sign can represent multiple different values (e.g. 𒄯 in Hittite cuneiform can represent three different phonemes, transliterated as 'ḫar', 'ḫur' and 'mur', as well as three different logograms meaning 'ring', 'thick' and 'lung').

For language modelling tasks, we therefore suggest that representations of texts in their native form are preferable to achieve the most accurate results. A number of digitized corpuses for well-resourced and widely studied ancient languages are now available in Unicode representations of their native script, including the [Perseus] corpus for ancient Greek texts, as well as [TBD] for and biblical Hebrew. However, many other online text corpora for more niche or under-resourced ancient languages remain restricted to their transliterated form (despite the availability of relevant Unicode standards), presumably due to considerations around ease, system limitations and accessibility.

In addition, such transliterations of ancient texts are often heavily annotated, with special characters used to denote a range of features including uncertain readings, missing or damaged elements, erasures, non-textual marks, and annotations by modern transliterators pertaining to structural or physical elements of the document. If not removed or handled appropriately, these have the potential to introduce further noise into language models. 

These are the primary gaps we have aimed to address through the development of Potnia. The library's focus on ancient languages and its extensible architecture make it a valuable asset for researchers working with digitized ancient corpora. It is also equipped to provide specific handling of these elements, with tailored tokenization and regularization rules pertaining to both script-specific and corpus-specific conventions. Potnia therefore enables a key pre-processing step in the language modelling pipeline, with the resulting Unicode outputs of ancient texts enabling more accurate and nuanced computational analysis of these texts in downstream modelling tasks.

Potnia’s development was recognised through its acceptance to [PyCon AU 2024](https://2024.pycon.org.au/program/HMWPGH/), highlighting the need for such a tool within the broader research community.  Potnia, by focusing on the unique requirements of ancient texts, provides a specialized solution that enables more nuanced and accurate analysis of digitized corpora.

# Implementation

Potnia is implemented in Python with an extensible architecture centered around the Mapper class, which converts transliterated texts into Unicode representations. The library is available here - [Potnia on PyPI](https://pypi.org/project/potnia/) and is designed to handle the complexities of ancient scripts through a flexible and customizable framework.

## Key Features

1. **YAML-Based Data Storage:**  Potnia stores script-specific syllabograms and logograms in YAML files, allowing easy updates and additions. This approach ensures scalability when integrating new scripts like Linear A and Akkadian.

    ```yaml
    syllabograms:
      ja: 𐀊
      ni: 𐀛
      po: 𐀡
      ti: 𐀴
    ```

2. **Regular Expressions for Complex Text:** Regular expressions are used to manage uncertain readings, special symbols, and compound tokens. This enables accurate tokenization and conversion of transliterated texts.

3. **Custom Tokenization and Unicode Conversion:** Potnia provides a flexible tokenization system tailored to each script’s unique structure. The to_unicode method converts transliterations into Unicode based on mappings stored in YAML files.

4. **Regularisation of Text:** The regularize method cleans the output by handling missing elements and unnecessary tags, refining the text for downstream use.

    ```python
    # Tokenisation Example
    text = "po-ti-ni-ja"
    tokens = linear_b_mapper.tokenize_transliteration(text)
    print(tokens)  # Output: ['po', '-', 'ti', '-', 'ni', '-', 'ja']

    # Unicode Mapping
    from potnia import linear_b_mapper
    text = "po-ti-ni-ja"
    unicode_text = linear_b_mapper(text, regularize=True)
    print(unicode_text)  # Output: 𐀡𐀴𐀛𐀊
    ```
5. **Comprehensive Testing:** A test suite validates the accuracy of tokenization and conversion. Test cases, defined in YAML files, cover various scripts like Linear B and Linear A, ensuring reliability and facilitating contributions.

    ```python
    @pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode_regularized"))
    def test_linear_b_unicode_regularized(test_input, expected):
        result = linear_b_mapper(test_input, regularize=True)
        assert result == expected
    ```
This design makes Potnia easily extendable, with Linear B fully supported and work underway for other scripts like Linear A and Akkadian.

# Research Application

Potnia’s design and functionality address the following challenges in the analysis of ancient texts:

1. **Extensibility:** Potnia is designed to be highly extensible, allowing researchers to integrate new scripts by defining script-specific rules for tokenization and conversion. This flexibility makes the library suitable for a wide range of ancient languages that are not yet represented in Unicode, providing a valuable tool for researchers across various fields of ancient studies.

2. **Integration with Research Workflows:** Researchers can easily incorporate Potnia into their existing workflows. For example, in a typical research scenario, Potnia could be used to preprocess a corpus of Linear B texts before feeding them into a machine learning model for further analysis:

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

    For instance, Potnia’s functionality is being used as part of a larger project aimed at deciphering Linear A. We are using Potnia to convert Roman transliterations of Linear B tablets into datasets and extend this capability to Linear A. The resulting datasets will be used to train language-specific models for tasks such as text generation and masked language modeling. Future models developed using this library will be released for public use, supporting downstream tasks such as decipherment, textual restoration, and palaeographic analysis. 

# Community Guidelines

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
