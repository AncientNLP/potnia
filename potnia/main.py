import typer

from potnia import linear_a_mapper, linear_b_mapper, hittite_mapper, luwian_mapper
from guigaga import gui
from .data import DATA_DIR

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


@app.command()
def bibtex():
    """ Prints the BibTeX entry for this software package. """
    bibtex_path = DATA_DIR / "potnia.bib"
    print("% This BibTeX entry can be used to cite this software package.")
    print("% This will get updated when Potnia has a preprint and is published.")
    bibtex_str = bibtex_path.read_text()
    print(bibtex_str)


click_command = typer.main.get_command(app)
cli = gui()(click_command)