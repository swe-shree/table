def apply_filters(data, filters: dict):
    for key, value in filters.items():
        data = [d for d in data if str(value).lower() in str(d.get(key, "")).lower()]
    return data