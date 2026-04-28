def apply_pagination(data, page: int, limit: int):
    start = (page - 1) * limit
    end = start + limit
    return data[start:end]