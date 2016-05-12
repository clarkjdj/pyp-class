def string2number(a_string):
    if not isinstance(a_string, str):
        raise ValueError
    try:
        return float(a_string)
    except ValueError:
        return int(a_string)
