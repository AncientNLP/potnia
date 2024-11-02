from potnia.script import Script



def test_tokenize_unicode():
    script = Script(config=dict(dummy="dummy"))

    result = script.tokenize_unicode("text")
    assert result == ["t", "e", "x", "t"]
