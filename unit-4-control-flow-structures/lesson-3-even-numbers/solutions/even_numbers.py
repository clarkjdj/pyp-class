def even_numbers(list_of_numbers, limit):
    result = []
    counter = 0
    for num in list_of_numbers:
        if counter == limit:
            break
        if not num % 2 == 0:
            continue
        result.append(num)
        counter += 1
    return result
