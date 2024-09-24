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
    orcid: 0000-0000-0000-0000
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

The forces on stars, galaxies, and dark matter under external gravitational
fields lead to the dynamical evolution of structures in the universe. The orbits
of these bodies are therefore key to understanding the formation, history, and
future state of galaxies. The field of "galactic dynamics," which aims to model
the gravitating components of galaxies to study their structure and evolution,
is now well-established, commonly taught, and frequently used in astronomy.
Aside from toy problems and demonstrations, the majority of problems require
efficient numerical tools, many of which require the same base code (e.g., for
performing numerical orbit integration).

# Statement of need

The last five years have seen a significant increase in the application of machine learning to the study of ancient scripts. Applications are broad, and include recognition via Optical Character Recognition (OCR), textual restoration, palaeographic analysis, topic modelling, representation learning, decipherment and machine translation [@sommerschieldMachineLearningAncient2023]. A large number of ancient language corpora have been digitised in recent decades, supporting this research. However, while the necessary Unicode blocks for many of these ancient scripts are available, a number of these data sets are still presented as Romanised transliterations.

In response to this situation, we have created [Potnia](https://pypi.org/project/potnia/), an open-source Python language library under the Apache 2.0 license, designed to convert such transliterated texts to Unicode. The session image accompanying this proposal provides an example of Potnia’s conversion process, with a Romanised transliteration of a Linear B text as the input, and the Unicode representation of this same text as the output. This conversion is crucial for downstream machine learning tasks, as tokenisation in the original Unicode script allows for more accurate representation of linguistic structures and mitigates potential biases introduced by transliteration.

Potnia's flexible architecture, built on Python's object-oriented principles, employs string manipulation techniques and regular expressions to handle various complexities inherent in ancient texts, such as uncertain readings, missing elements, and script-specific notations. At present, the library can be used for Linear B texts, with functionality for Linear A, Sumerian, Akkadian, Hittite, Luwian and Etruscan soon to follow.

Potnia's design allows for easy addition of new scripts, each with its own set of rules for tokenisation, regularisation, and character mapping. This extensibility positions us well for future inclusion of additional scripts. To ensure reliability and facilitate open-source contributions, we've implemented a comprehensive test suite using pytest, with test cases defined in YAML files for easy expansion. This approach covers key functionalities across different scripts and simplifies the process of adding new test scenarios as the library grows.


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
