from datetime import date


def count_days(d1, d2):
    if d2 < d1:
        raise ValueError('Second date must be greater than first one.')
    return (d2 - d1).days
