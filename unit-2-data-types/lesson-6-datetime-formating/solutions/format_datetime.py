def format_datetime(dt):
    first_days = {1: 'st', 2: 'nd', 3: 'rd'}
    if dt.day in first_days:
        prefix = first_days[dt.day]
    else:
        prefix = 'th'
    return dt.strftime("%A %B %d{}, %Y at %H:%M hs".format(prefix))
