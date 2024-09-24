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
    affiliation: "1" # (Multiple affiliations must be quoted)
  - name: Kabir Manandhar Shrestha
    orcid: 0009-0001-2059-1683
    equal-contrib: true
    affiliation: 2
  - name: Robert Turnbull
    orcid: 0000-0000-0000-0000
    corresponding: true # (This is how to denote the corresponding author)
    equal-contrib: true
    affiliation: 2
affiliations:
 - name: University of Melbourne, Australia
   index: 1
 - name: Melbourne Data Analytics Platform, Australia
   index: 2
date: 23 September 2024
bibliography: JOSS_PotniaDraft.bib

---

# Summary

Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into their respective Unicode representations. The increasing digitization of ancient language corpora has led to significant progress in fields such as Optical Character Recognition (OCR), textual restoration, and palaeographic analysis. However, many of these datasets are still presented in Romanized transliteration rather than their original script in Unicode, despite the availability of Unicode blocks for numerous ancient scripts. This discrepancy presents challenges for accurate linguistic representation and computational analysis.

Potnia addresses this gap by providing a flexible, extensible framework for converting transliterated texts to Unicode. The library's initial release supports Linear B texts, with plans to expand functionality to other ancient languages, including Linear A, Sumerian, and Akkadian. By facilitating the conversion of digitized transliterated corpora into Unicode, Potnia enables more accurate tokenization for downstream tasks such as machine learning-based textual analysis, enhancing the capabilities of digital humanities and computational linguistics in the study of ancient languages.

# Statement of need

The application of machine learning to the study of ancient scripts has grown significantly in recent years, emphasizing the need for datasets represented in their original scripts rather than Romanized transliterations. While the Unicode Standard provides the means to encode most ancient scripts, a substantial portion of data continues to be distributed as transliterations due to legacy digitization practices.

Machine learning algorithms, particularly those focused on natural language processing, perform better when working with the original script rather than a Romanized equivalent. Tokenization in Unicode avoids the loss of linguistic nuance and reduces the biases introduced by transliteration. This is crucial in tasks like Optical Character Recognition, decipherment, and representation learning, where the form of the original script can significantly impact the quality of the model.

Potnia fills a critical gap in the existing software ecosystem by providing a specialized tool for converting Romanized transliterations of ancient texts into Unicode. While general-purpose transliteration tools exist, they often lack the specific handling required for ancient scripts, including dealing with uncertain readings, missing elements, and script-specific notations. Potnia's focus on ancient languages and its extensible architecture make it a valuable asset for researchers working with digitized ancient corpora, enabling more accurate and nuanced computational analysis of these texts.

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

text = "ko-no-so"
unicode_text = linear_b_mapper(text, regularize=True)
print(unicode_text)  # Output: 𐀒𐀜𐀰
```

Potnia's architecture is designed to handle the inherent complexities of ancient scripts. The LinearBMapper class, for instance, extends the base Mapper class to implement specific rules for Linear B, including handling of syllabograms, logograms, and special characters. This modular design allows for easy extension to other ancient scripts.

The library uses PyYAML for efficient data loading and management of character mappings. Regular expressions are extensively used for tokenization and text normalization, ensuring robust handling of various text formats and notations commonly found in transliterated ancient texts.

# Research Application

Potnia’s design and functionality address several key challenges in the analysis of ancient texts:

1. **Unicode Conversion:** By converting transliterated texts into their original scripts in Unicode, Potnia supports more accurate downstream processing, especially for machine learning applications.

2. **Tokenization and Regularization:** The library implements specialized tokenization and regularization strategies to manage unique symbols, uncertain readings, and structural elements of ancient scripts. It handles script-specific rules for dealing with missing or ambiguous elements, improving the accuracy of linguistic analysis.

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

Currently, Potnia supports the Linear B script with forthcoming support for Linear A, Sumerian, and Akkadian. This functionality positions Potnia as an essential tool for researchers working with digitized ancient language corpora.

# Community Guidelines and Future Work

Potnia is open-source software released under the Apache 2.0 license. We welcome contributions from the community, including bug reports, feature requests, and pull requests. Issues can be reported on our GitHub repository 
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
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from xyz, and support from xyz during the xyz of this project.

# References
