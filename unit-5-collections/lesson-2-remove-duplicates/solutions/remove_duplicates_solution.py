def remove_duplicates_in_order(a_list):
    new_list = []
    for element in a_list:
        if element not in new_list:
            new_list.append(element)

    return new_list
