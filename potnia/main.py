import typer

from potnia import linear_a_mapper, linear_b_mapper

app = typer.Typer()


@app.command()
def linear_a(text: str, regularize:bool=False):
    """ Converts a Linear A text to Unicode. """
    print(linear_a_mapper(text, regularize=regularize))


@app.command()
def linear_b(text: str, regularize:bool=False):
    """ Converts a Linear B text to Unicode. """
    print(linear_b_mapper(text, regularize=regularize))

