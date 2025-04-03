================================================================
Potnia
================================================================

.. image:: https://raw.githubusercontent.com/AncientNLP/potnia/main/docs/_static/img/PotniaLogo.png

.. start-summary

|pypi badge| |testing badge| |coverage badge| |docs badge| |git3moji badge| |black badge| |JOSS badge|

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

.. |JOSS badge| image:: https://joss.theoj.org/papers/7641150c49e996a21fa0f4dc3aadb258/status.svg
    :target: https://joss.theoj.org/papers/7641150c49e996a21fa0f4dc3aadb258





Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into Unicode representations of ther respective native scripts.

Currently, the scripts supported by Potnia are:

- Linear A
- Linear B
- Hittite cuneiform
- Arabic

Functionality for Luwian hieroglyphs, Sumero-Akkadian cuneiform, Lydian and Etruscan is in development.

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

You can also install Potnia by cloning the repository and installing using poetry. 
This will install all the dependencies required for Potnia from the with the version numbers pinned in the ``poetry.lock`` file. 
Make sure that poetry is installed on your system. If not, see the `instructions <https://python-poetry.org/docs/#installation>`_.
Then follow these steps:

.. code-block:: bash

    git clone https://github.com/AncientNLP/potnia.git
    cd potnia
    poetry install

You can test that Potnia is working by running ``pytest``.

.. note::

    For proper display of ancient script glyphs, please refer to the `Fonts <https://ancientnlp.github.io/potnia/fonts.html>`_  section.

Usage
====================

To convert transliterated Linear B to Linear B Unicode, use the following code:

.. code-block:: python

    >>> from potnia import linear_b
    >>> linear_b("a-ri-to-jo")
    '𐀀𐀪𐀵𐀍'


If you wish to regularize the text to remove additional annotations present in the `LiBER <https://liber.cnr.it/index>`_ 
and  `DĀMOS <https://damos.hf.uio.no/about/content/>`_ transliteration, use the following code:

.. code-block:: python

    >>> linear_b("e-ke-qe ]-o-na-to , ke-ke-me-na⌞ ⌟ko-to-na GRA qs ] vac.", regularize=True)
    '𐀁𐀐𐀤 %𐀃𐀙𐀵 𐀐𐀐𐀕𐀙 𐀒𐀵𐀙 𐂎 %'

Note that uncertain/missing signs or sections of text are presently being replaced with a wildcard '%' character.

To tokenize transliterated Linear B texts without converting it to Unicode, use the following code:

.. code-block:: python

    >>> linear_b.tokenize_transliteration("]wa VIR 1 MUL 2 'ko-wa 1' ko-wo 1")
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

    
.. end-quickstart

Credits
====================

.. start-credits

Potnia is developed by:

- Emily Tour (University of Melbourne)
- `Kabir Manandhar Shrestha <https://findanexpert.unimelb.edu.au/profile/892683-kabir-manandhar-shrestha>`_ (Melbourne Data Analytics Platform, University of Melbourne)
- `Dr Robert Turnbull <https://robturnbull.com>`_ (Melbourne Data Analytics Platform, University of Melbourne)

To cite Potnia, use this reference:

    Tour, Emily, Kabir Manandhar Shrestha, and Robert Turnbull. 'Potnia: A Python Library for the Conversion of Transliterated Ancient Texts to Unicode.' *Journal of Open Source Software* 10, no. 108 (2025): 7725. `doi:10.21105/joss.07725 <https://doi.org/10.21105/joss.07725>`_

You can also use the following BibTeX entries:

.. code-block:: bibtex

    @article{potnia, 
        author       = {Emily Tour and Kabir Manandhar Shrestha and Robert Turnbull},
        title        = {{Potnia: A Python library for the conversion of transliterated ancient texts to Unicode}},
        year         = {2025}, 
        journal      = {Journal of Open Source Software},
        publisher    = {The Open Journal}, 
        volume       = {10}, 
        number       = {108},
        pages        = {7725},
        doi          = {10.21105/joss.07725}, 
        url          = {https://doi.org/10.21105/joss.07725}
    }

    @misc{potnia_release,
        author       = {Emily Tour and Kabir Manandhar Shrestha and Robert Turnbull},
        title        = {{Potnia: A Python library for the conversion of transliterated ancient texts to Unicode}},
        year         = {2025},
        url          = {https://doi.org/10.26188/28721354.v1},
        note         = {Version 0.4.0, Apache License 2.0},
        doi          = {10.26188/28721354.v1}
    }


.. end-credits
