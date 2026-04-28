def apply_sort(data, sort: str):
    if not sort:
        return data

    reverse = sort.startswith("-")
    key = sort.lstrip("-")

    return sorted(data, key=lambda x: x.get(key), reverse=reverse)