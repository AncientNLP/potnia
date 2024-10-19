import pytest

from typer.testing import CliRunner
from potnia.main import app
from .data import expected

runner = CliRunner()


@pytest.mark.parametrize("test_input,expected", expected("linear_a_unicode"))
def test_linear_a_main(test_input, expected):
    result = runner.invoke(app, ["linear-a", test_input])
    assert expected in result.stdout


@pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode"))
def test_linear_b_main(test_input, expected):
    result = runner.invoke(app, ["linear-b", test_input])
    assert expected in result.stdout


@pytest.mark.parametrize("test_input,expected", expected("linear_b_unicode_regularized"))
def test_linear_b_main_regularized(test_input, expected):
    result = runner.invoke(app, ["linear-b", test_input, "--regularize"])
    assert expected in result.stdout


@pytest.mark.parametrize("test_input,expected", expected("hittite_unicode"))
def test_hittite_main(test_input, expected):
    result = runner.invoke(app, ["hittite", test_input])
    assert expected in result.stdout


