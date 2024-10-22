import typer
from enum import Enum
from potnia import linear_a_mapper, linear_b_mapper, hittite_mapper, luwian_mapper
from guigaga import gui
from pybtex import PybtexEngine
from unittest.mock import patch
import pybtex.richtext


from .data import DATA_DIR

BIBTEX_PATH = DATA_DIR / "potnia.bib"

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
    print("% This BibTeX entry can be used to cite this software package.")
    print("% This will get updated when Potnia has a preprint and is published.")
    bibtex_str = BIBTEX_PATH.read_text()
    print(bibtex_str)


def from_latex(latex):
    """ 
    Temporary patch until this issue isresolved:
    https://bitbucket.org/pybtex-devs/pybtex/issues/443/decoding-issue-in-from_latex-method-in-the
    """
    import codecs
    import latexcodec  # noqa
    from pybtex.markup import LaTeXParser

    if not isinstance(latex, str):
        latex = codecs.decode(latex, 'ulatex')

    return LaTeXParser(latex).parse()


class BibliographyFormat(str, Enum):
    plaintext = "plaintext"
    html = "html"
    latex = "latex"
    markdown = "markdown"

    def __str__(self):
        return self.value


class BibliographyStyle(str, Enum):
    plain = "plain"
    unsrt = "unsrt"
    alpha = "alpha"
    unsrtalpha = "unsrtalpha"

    def __str__(self):
        return self.value


@app.command()
@patch.object(pybtex.richtext.Text, 'from_latex', from_latex)
def bibliography(
    style:BibliographyStyle="plain", 
    output:BibliographyFormat="plaintext",
):
    engine = PybtexEngine()
    bibliography_string = engine.format_from_files(
        bib_files_or_filenames=[BIBTEX_PATH], 
        style=str(style), 
        output_backend=str(output),
    )
    print(bibliography_string)


click_command = typer.main.get_command(app)
cli = gui()(click_command)