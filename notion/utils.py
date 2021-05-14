def pick(base, keys):
    if base is None:
        return None
    entries = [(key, base[key]) for key in keys]
    return dict(entries)
