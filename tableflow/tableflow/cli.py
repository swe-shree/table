import typer
from tableflow.commands import search, filter, paginate

app = typer.Typer()

app.add_typer(search.app, name="search")
app.add_typer(filter.app, name="filter")
app.add_typer(paginate.app, name="paginate")

if __name__ == "__main__":
    app()