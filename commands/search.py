import typer
from tableflow.core.engine import apply_table

app = typer.Typer()

DATA = [
    {"id": 1, "name": "ram",   "department": "IT"},
    {"id": 2, "name": "john",  "department": "HR"},
    {"id": 3, "name": "priya", "department": "IT"},
    {"id": 4, "name": "sara",  "department": "Finance"},
    {"id": 5, "name": "ravi",  "department": "HR"},
]


@app.command()
def run(
    query: str = typer.Argument(..., help="Search term to match against any column"),
    page:  int  = typer.Option(1,  help="Page number"),
    limit: int  = typer.Option(10, help="Rows per page"),
):
    """Search rows where ANY column contains the query string."""
    matched = [
        row for row in DATA
        if any(query.lower() in str(v).lower() for v in row.values())
    ]
    result = apply_table(matched, page=page, limit=limit)
    _print_result(result)


def _print_result(result: dict):
    rows = result["rows"]
    if not rows:
        print("No results found.")
        return

    # Simple table print
    headers = list(rows[0].keys())
    col_w = {h: max(len(h), max(len(str(r[h])) for r in rows)) for h in headers}

    sep = "+-" + "-+-".join("-" * col_w[h] for h in headers) + "-+"
    header_row = "| " + " | ".join(h.ljust(col_w[h]) for h in headers) + " |"

    print(sep)
    print(header_row)
    print(sep)
    for row in rows:
        print("| " + " | ".join(str(row[h]).ljust(col_w[h]) for h in headers) + " |")
    print(sep)
    print(f"  Page {result['page']} of {result['pages']}  |  {result['total']} total row(s)")