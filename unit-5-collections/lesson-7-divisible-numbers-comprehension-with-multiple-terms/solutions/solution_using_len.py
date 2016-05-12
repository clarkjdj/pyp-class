def divisible_numbers(a_list, terms):
    return [x for x in a_list if len([1 for term in terms if x % term == 0]) == len(terms)]
