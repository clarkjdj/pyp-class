def sum_multiple(*args):
    if not args:
        raise AttributeError("You must pass at least one number to sum")
    return sum(args)
