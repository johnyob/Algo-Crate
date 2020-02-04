DEFAULT_CMP = lambda x, y: 1 if x > y else (-1 if x < y else 0)

def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)


def is_series(value):
    return isinstance(value, list) or isinstance(value, tuple)
