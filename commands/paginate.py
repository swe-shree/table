import typer
from tableflow.core.engine import apply_table

app = typer.Typer()

DATA = [
    {"id": i, "name": f"user{i}", "department": "IT"}
    for i in range(1, 51)
]

@app.command()
def run(page: int = 1, limit: int = 10):
    result = apply_table(DATA, page=page, limit=limit)
    print(result)