from tableflow.core.filtering import apply_filters
from tableflow.core.sorting import apply_sort
from tableflow.core.pagination import apply_pagination


def apply_table(data, filters: dict = None, sort: str = "", page: int = 1, limit: int = 10):
    """
    Apply filtering, sorting, and pagination to a list of dicts.

    Args:
        data:    List of row dicts.
        filters: Dict of {column: value} to filter by (substring, case-insensitive).
        sort:    Column name to sort by. Prefix with '-' for descending (e.g. '-name').
        page:    1-based page number.
        limit:   Number of rows per page.

    Returns:
        dict with keys: rows, total, page, limit, pages
    """
    if filters is None:
        filters = {}

    # 1. Filter
    result = apply_filters(data, filters)
    total = len(result)

    # 2. Sort
    result = apply_sort(result, sort)

    # 3. Paginate
    result = apply_pagination(result, page, limit)

    return {
        "rows": result,
        "total": total,
        "page": page,
        "limit": limit,
        "pages": max(1, -(-total // limit)),  # ceiling division
    }