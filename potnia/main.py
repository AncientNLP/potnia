import typer

from potnia import linear_a_mapper, linear_b_mapper, hittite_mapper, luwian_mapper
from guigaga import gui

app = typer.Typer()


@app.command()
def linear_a(text: list[str], regularize:bool=False):
    """ Converts a Linear A text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(linear_a_mapper(text, regularize=regularize))


@app.command()
def linear_b(text: list[str], regularize:bool=False):
    """ Converts a Linear B text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(linear_b_mapper(text, regularize=regularize))


@app.command()
def hittite(text: list[str], regularize:bool=False):
    """ Converts a Hittite text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(hittite_mapper(text, regularize=regularize))


@app.command()
def luwian(text: list[str], regularize:bool=False):
    """ Converts a Luwian text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(luwian_mapper(text, regularize=regularize))


click_command = typer.main.get_command(app)
cli = gui()(click_command)