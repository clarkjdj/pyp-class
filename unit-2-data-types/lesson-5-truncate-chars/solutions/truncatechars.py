def truncatechars(a_string, num_of_chars):
    if not isinstance(a_string, str):
        raise ValueError
    if num_of_chars >= len(a_string):
        return a_string
    return '{}...'.format(a_string[:num_of_chars])
