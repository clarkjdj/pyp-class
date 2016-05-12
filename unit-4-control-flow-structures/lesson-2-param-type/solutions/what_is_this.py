def what_is_this(param):
    if param in (False, True):
        return "This is a Boolean."
    elif isinstance(param, int):
        return "This is an Integer."
    elif isinstance(param, str):
        return "This is a String."
    elif isinstance(param, float):
        return "This is a Float."
    else:
        return "I have no idea what this is"
