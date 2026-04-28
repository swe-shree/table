import typer
from tableflow.core.engine import apply_table

app = typer.Typer()

DATA = [
    {"id": 1, "name": "ram", "department": "IT"},
    {"id": 2, "name": "john", "department": "HR"},
]

@app.command()
def run(department: str = ""):
    result = apply_table(
        DATA,
        filters={"department": department} if department else {}
    )
    print(result)