import typer

from potnia import linear_a_mapper, linear_b_mapper

app = typer.Typer()


@app.command()
def linear_a(text: str, regularize:bool=False):
    print(linear_a_mapper(text, regularize=regularize))


@app.command()
def linear_b(text: str, regularize:bool=False):
    print(linear_b_mapper(text, regularize=regularize))


if __name__ == "__main__":
    app()
