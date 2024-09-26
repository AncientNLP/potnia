from potnia.data import read_data_yaml_cached

def test_read_data_yaml_cached():
    result = read_data_yaml_cached("does-not-exists.yaml")
    assert isinstance(result, dict)
    assert len(result) == 0