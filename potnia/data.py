import yaml
from pathlib import Path
from functools import cache

DATA_DIR = Path(__file__).parent / "data"

@cache
def read_data_yaml_cached(filename: str) -> dict[str, str]:
    path = DATA_DIR / filename
    if not path.suffix:
        path = path.with_suffix(".yaml")

    if not path.exists():
        return dict()
    
    with open(path, encoding='utf8') as f:
        result = yaml.safe_load(f)
    return result or dict()


def read_data(*filenames) -> dict[str, str]:
    result = dict()
    for filename in filenames:
        result.update(read_data_yaml_cached(filename))

    return result
