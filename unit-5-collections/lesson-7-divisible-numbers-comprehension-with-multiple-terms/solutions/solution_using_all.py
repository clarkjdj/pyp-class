def divisible_numbers(a_list, a_list_of_terms):
    return [e for e in a_list if all([e % t == 0 for t in a_list_of_terms])]
