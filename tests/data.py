import yaml
from typing import Dict
from pathlib import Path

EXPECTED_DIR = Path(__file__).parent / "expected"

def read_expected(filename: str) -> Dict[str, str]:
    path = EXPECTED_DIR / filename
    if not path.suffix:
        path = path.with_suffix(".yaml")

    if not path.exists():
        return dict()
    
    with open(path) as f:
        result = yaml.safe_load(f)
    return result or dict()


def expected(filename: str) -> str:
    return read_expected(filename).items()