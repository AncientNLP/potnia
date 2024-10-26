import typer
from pybtex import PybtexEngine
from potnia import linear_a as linear_a_script
from potnia import linear_b as linear_b_script
from potnia import hittite as hittite_script
from potnia import arabic as arabic_script
# from potnia import luwian as luwian_script
# from potnia import akkadian as akkadian_script

from .enums import BibliographyStyle, BibliographyFormat
from .data import DATA_DIR

BIBTEX_PATH = DATA_DIR / "potnia.bib"

app = typer.Typer()

TEXT_ARGUMENT = typer.Argument(help="The transliterated text to be converted to Unicode.")
REGULARIZATION_DEFAULT = typer.Option(False, help="Whether or not to regularize the output.")


@app.command()
def linear_a(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
    """ Converts a Linear A text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(linear_a_script(text, regularize=regularize))


@app.command()
def linear_b(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
    """ Converts a Linear B text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(linear_b_script(text, regularize=regularize))


@app.command()
def hittite(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
    """ Converts a Hittite text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(hittite_script(text, regularize=regularize))


# @app.command()
# def luwian(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
#     """ Converts a Luwian text to Unicode. """
#     if isinstance(text, list):
#         text = " ".join(text)
#     print(luwian_script(text, regularize=regularize))


# @app.command()
# def akkadian(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
#     """ Converts a Akkadian text to Unicode. """
#     if isinstance(text, list):
#         text = " ".join(text)
#     print(akkadian_script(text, regularize=regularize))


@app.command()
def arabic(text: list[str]=TEXT_ARGUMENT, regularize:bool=REGULARIZATION_DEFAULT):
    """ Converts a Arabic text to Unicode. """
    if isinstance(text, list):
        text = " ".join(text)
    print(arabic_script(text, regularize=regularize))


@app.command()
def bibtex():
    """ Prints the BibTeX entry for this software package. """
    print("% This BibTeX entry can be used to cite this software package.")
    print("% This will get updated when Potnia has a preprint and is published.")
    bibtex_str = BIBTEX_PATH.read_text()
    print(bibtex_str)


@app.command()
def bibliography(
    style:BibliographyStyle="plain", 
    output:BibliographyFormat="plaintext",
):
    """ Displays the bibliography. """
    engine = PybtexEngine()
    bibliography_string = engine.format_from_files(
        bib_files_or_filenames=[BIBTEX_PATH], 
        style=str(style), 
        output_backend=str(output),
    )
    print(bibliography_string)


@app.callback()
def potnia():
    """
    <img src="https://raw.githubusercontent.com/AncientNLP/potnia/main/docs/_static/img/PotniaLogo.png" alt="Potnia Logo" width="500"/>

    Potnia is an open-source Python library designed to convert Romanized transliterations of ancient texts into Unicode representations of ther respective native scripts.
    """


@app.command()    
def gui(ctx: typer.Context):    
    """ Launches the Potnia GUI. """
    from guigaga.themes import Theme
    from guigaga.guigaga import GUIGAGA    
    gui = GUIGAGA(
        typer.main.get_group(app), 
        click_context=ctx,
        theme=Theme.monochrome,
        allow_file_download=False,
    )
    gui.launch()    

