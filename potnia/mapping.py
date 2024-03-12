# import yaml
# from pathlib import Path

# DATA_DIR = Path(__file__).parent / "data"

# def read_yaml(filename: str) -> dict:
#     with open(DATA_DIR / filename) as f:
#         return yaml.safe_load(f)

# AEGEAN_SYLLABOGRAMS_TO_SYLLABLE = read_yaml("aegean_syllabograms.yaml")
# # EXTRA_LINEAR_A_SYLLABOGRAMS_TO_SYLLABLE = read_yaml("unique_linear_a_syllabograms.yaml")
# EXTRA_LINEAR_B_SYLLABOGRAMS_TO_SYLLABLE = read_yaml("unique_linear_b_syllabograms.yaml")
# # LINEAR_A_SYLLABOGRAMS_TO_SYLLABLE = {**AEGEAN_SYLLABOGRAMS_TO_SYLLABLE, **EXTRA_LINEAR_A_SYLLABOGRAMS_TO_SYLLABLE}
# LINEAR_B_SYLLABOGRAMS_TO_SYLLABLE = {**AEGEAN_SYLLABOGRAMS_TO_SYLLABLE, **EXTRA_LINEAR_B_SYLLABOGRAMS_TO_SYLLABLE}

# breakpoint()