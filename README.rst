================================================================
Potnia
================================================================

.. image:: https://raw.githubusercontent.com/AncientNLP/potnia/main/docs/_static/img/PotniaLogo.png

.. start-summary

|pypi badge| |testing badge| |coverage badge| |docs badge| |git3moji badge| |black badge|

.. |pypi badge| image:: https://img.shields.io/pypi/v/potnia
    :target: https://pypi.org/project/potnia/

.. |testing badge| image:: https://github.com/AncientNLP/potnia/actions/workflows/testing.yml/badge.svg
    :target: https://github.com/AncientNLP/potnia/actions
    
.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/e640f26fb59e39e3051de8fbf020de62/raw/coverage.json
    :target: https://ancientnlp.github.io/potnia/coverage/

.. |docs badge| image:: https://github.com/AncientNLP/potnia/actions/workflows/docs.yml/badge.svg
    :target: https://ancientnlp.github.io/potnia
    
.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |git3moji badge| image:: https://img.shields.io/badge/git3moji-%E2%9A%A1%EF%B8%8F%F0%9F%90%9B%F0%9F%93%BA%F0%9F%91%AE%F0%9F%94%A4-fffad8.svg
    :target: https://robinpokorny.github.io/git3moji/



Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into Unicode representations of ther respective native scripts.

Currently the conversion of transliterated Linear B texts into a Unicode representation of the script is fully supported, with functionality for Linear A, Sumero-Akkadian cuneiform, Hittite cuneiform, Luwian hieroglyphs and Etruscan in development.

Contributions are welcome! Please see the `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ file for more information.

.. end-summary


.. start-quickstart

Installation
====================

To install Potnia, run the following command:

.. code-block:: bash

    pip install potnia

To install the latest version from the repository, you can use this command:

.. code-block:: bash

    pip install git+https://github.com/AncientNLP/potnia.git
    
Usage
====================

To convert transliterated Linear B to Linear B Unicode, use the following code:

.. code-block:: python

    >>> from potnia import linear_b_mapper
    >>> linear_b_mapper("a-ri-to-jo")
    '𐀀𐀪𐀵𐀍'


If you wish to regularize the text to remove additional annotations present in the `LiBER <https://liber.cnr.it/index>` and  `DĀMOS <https://damos.hf.uio.no/about/content/>`` transliterations, use the following code:

.. code-block:: python

    >>> linear_b_mapper("e-ke-qe ]-o-na-to , ke-ke-me-na⌞ ⌟ko-to-na GRA qs ] vac.", regularize=True)
    '𐀁𐀐𐀤 %𐀃𐀙𐀵 𐀐𐀐𐀕𐀙 𐀒𐀵𐀙 𐂎 %'

Note that uncertain/missing signs or sections of text are presently being replaced with a wildcard '%' character.

To tokenize transliterated Linear B texts without converting it to Unicode, use the following code:

.. code-block:: python

    >>> linear_b_mapper.tokenize_transliteration("]wa VIR 1 MUL 2 'ko-wa 1' ko-wo 1")
    [']', 'wa', ' ', 'VIR', ' ', '1', ' ', 'MUL', ' ', '2', ' ', "'", 'ko', 'wa', ' ', '1', "'", ' ', 'ko', 'wo', ' ', '1']

Command Line Interface (CLI)
============================

Potnia also provides a command line interface (CLI).

To convert transliterated Linear B to Unicode, use the following command:

.. code-block:: bash

    potnia linear-b "a-ri-to-jo"

To regularize the text, use the following command:

.. code-block:: bash

    potnia linear-b "e-ke-qe ]-o-na-to , ke-ke-me-na⌞ ⌟ko-to-na GRA qs ] vac." --regularize

To see the full set of commands available in the CLI, use the following command:

.. code-block:: bash

    potnia --help

Graphical User Interface (GUI)
==============================

.. image:: https://raw.githubusercontent.com/AncientNLP/potnia/main/docs/_static/img/potnia-gui.png

Potnia also provides a graphical user interface (GUI). To start it, run:

.. code-block:: bash

    potnia gui

This will show a link in the terminal that you can click on to open the GUI in your browser.


Adding New Scripts to Potnia
============================

Potnia allows for the easy integration of new ancient scripts by using a single YAML file per language. This file will contain the mappings for syllabograms, logograms (if applicable), transliteration rules, and regularization patterns. Below are the steps for adding a new script, along with examples.

Steps to Add a New Language
----------------------------

1. **Create a Single YAML Mapping and Rules File**: Define the mappings for syllabograms, logograms (if applicable), and the rules for transliteration and regularization. Here's an example for Linear B:

   .. code-block:: yaml

      mappings:
        syllabograms:
            a: 𐀀
            e: 𐀁
            i: 𐀂
        logograms:
            VIR: 𐂀  # man
            MUL: 𐂁  # woman
        transliteration:
            - ['ro2', '𐁊']
        regularization:
            - ['\\[•~\\]', '']  # Remove uncertain readings
            - ['\\bqs\\b', '%']  # Handle missing elements

2. **Add the New Mapper Class**: Create a `Mapper` class that points to the new YAML file. For example:

   .. code-block:: python

      from dataclasses import dataclass
      from .mapper import Mapper

      @dataclass
      class NewScriptMapper(Mapper):
          config: str = "new_script"  # Refers to the YAML file name

      new_script_mapper = NewScriptMapper()

3. **Write Test Cases**: Add test cases to ensure that the new language’s transliteration and Unicode mapping work as expected. Example:

   .. code-block:: yaml

      test_newscript.yaml:
      "a-e-i": "𐀀𐀁𐀂"
      "VIR MUL": "𐂀𐂁"

4. **Usage Example**: Once the new language is added, it can be used as follows:

   .. code-block:: python

      from potnia import new_script_mapper

      # Convert transliterated text to Unicode
      new_script_mapper("a-e-i")

      # Regularize text
      new_script_mapper("a-[•~]", regularize=True)

This approach centralizes all configuration for a given script into a single YAML file, simplifying the process of adding new languages while maintaining Potnia's flexible and modular design.
    
.. end-quickstart

Credits
====================

.. start-credits

Potnia is developed by:

- Emily Tour (University of Melbourne)
- `Kabir Manandhar Shrestha <https://findanexpert.unimelb.edu.au/profile/892683-kabir-manandhar-shrestha>`_ (Melbourne Data Analytics Platform, University of Melbourne)
- `Dr Robert Turnbull <https://findanexpert.unimelb.edu.au/profile/877006-robert-turnbull>`_ (Melbourne Data Analytics Platform, University of Melbourne)

.. end-credits