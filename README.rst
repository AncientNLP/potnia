Potnia
====================

.. start-badges

|testing badge| |git3moji badge| |black badge|

.. |testing badge| image:: https://github.com/etour-unimelb/potnia/actions/workflows/testing.yml/badge.svg
    :target: https://github.com/etour-unimelb/potnia/actions
    
.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    
.. |git3moji badge| image:: https://img.shields.io/badge/git3moji-%E2%9A%A1%EF%B8%8F%F0%9F%90%9B%F0%9F%93%BA%F0%9F%91%AE%F0%9F%94%A4-fffad8.svg
    :target: https://robinpokorny.github.io/git3moji/

.. end-badges


Potnia is a Python Library to process ancient scripts such as Linear A, Linear B, Sumerian and Akkadian.

Currently Linear B is fully supported, with Linear A, Sumerian and Akkadian in development.

Contributions are welcome! Please see the `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ file for more information.

Installation
====================

To install Potnia, run the following command:

.. code-block:: bash

    pip install potnia

To install the latest version from the repository, you can use this command:

.. code-block:: bash

    pip install git+https://github.com/Linear-A-Decipher/potnia.git
    
Usage
====================

To convert Romanized Linear B to Linear B Unicode, use the following code:

.. code-block:: python

    from potnia import linear_b_mapper

    linear_b_mapper("a-ri-to-jo")

This will return the following output:

.. code-block:: python

    '𐀀𐀪𐀵𐀍'

If you wish to regularize the text to remove markup present in the LiBER or DĀMOS transcriptions, use the following code:

.. code-block:: python

    linear_b_mapper("e-ke-qe ]-o-na-to , ke-ke-me-na⌞ ⌟ko-to-na GRA qs ] vac.", regularize=True)

This will return the following string:

.. code-block:: python

    '𐀁𐀐𐀤 %𐀃𐀙𐀵 𐀐𐀐𐀕𐀙 𐀒𐀵𐀙 𐂎 qs %'

To tokenize Linear B text without converting it to Unicode, use the following code:

.. code-block:: python

    linear_b_mapper.tokenize_transliteration("]wa VIR 1 MUL 2 'ko-wa 1' ko-wo 1")

This will return the following list:

.. code-block:: python

    [']', 'wa', ' ', 'VIR', ' ', '1', ' ', 'MUL', ' ', '2', ' ', "'", 'ko', 'wa', ' ', '1', "'", ' ', 'ko', 'wo', ' ', '1']


Credit
====================

Potnia is developed by:

- Emily Tour (University of Melbourne)
- Kabir Manandhar Shrestha (Melbourne Data Analytics Platform, University of Melbourne)
- Dr Robert Turnbull (Melbourne Data Analytics Platform, University of Melbourne)
