===========================
Adding New Scripts to Potnia
============================

Potnia allows for the easy integration of new ancient scripts by using a single YAML file per script. This file will contain the mappings for syllabograms, logograms (if applicable), transliteration rules, and regularization patterns. Below are the steps for adding a new script, along with examples.

Steps to Add a New Script
----------------------------

1. **Create a Single YAML Mapping and Rules File**: Define the mappings for syllabograms, logograms (if applicable), and the rules for transliteration and regularization. Here's an example for Linear B:

   .. code-block:: yaml

      mappings:
        a: 𐀀
        e: 𐀁
        i: 𐀂
        # logograms
        VIR: 𐂀  # man
        MUL: 𐂁  # woman
      transliteration:
        - ['ro2', '𐁊']
      regularization:
        - ['\\[•~\\]', '']  # Remove uncertain readings
        - ['\\bqs\\b', '%']  # Handle missing elements

2. **Add the New Script Class**: Create a `Script` class that points to the new YAML file (usually in the `scripts` directory). For example:

   .. code-block:: python

      from dataclasses import dataclass
      from ..script import Script

      @dataclass
      class NewScript(Script):
          config: str = "new_script"  # Refers to the YAML file name

      new_script = NewScript()

3. **Add to __init__.py**: Add the new script to the ``__init__.py`` file. For example:

   .. code-block:: python

      from .scripts.new_script import new_script, NewScript

4. **Write Test Cases**: Add test cases to ensure that the new script's transliteration and Unicode mapping work as expected. Example:

   .. code-block:: yaml

      test_newscript_unicode.yaml:
      "a-e-i": "𐀀𐀁𐀂"
      "VIR MUL": "𐂀𐂁"
    
    Then, write a test function to check the output of the new script:

    .. code-block:: python

    @pytest.mark.parametrize("test_input,expected", expected("test_newscript_unicode"))
    def test_test_newscript_unicode(test_input, expected):
        result = new_script(test_input)
        assert result == expected, f"Expected: new_script('{test_input}') to produce '{expected}' but got '{result}'"


5. **Usage Example**: Once the new script is added, it can be used as follows:

   .. code-block:: python

      from potnia import new_script

      # Convert transliterated text to Unicode
      new_script("a-e-i")

      # Regularize text
      new_script("a-[•~]", regularize=True)

This approach centralizes all configuration for a given script into a single YAML file, simplifying the process of adding new scripts while maintaining Potnia's flexible and modular design.
