def to_fahrenheit(a_list):
    return [(lambda x: x * 9 / 5.0 + 32)(x) for x in a_list]
