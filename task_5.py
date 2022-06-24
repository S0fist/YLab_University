from math import prod


def count_find_num(primesL, limit):
    min_number = prod(primesL)
    result = set()
    result.add(min_number)
    if min_number > limit:
        return []
    old_values = {min_number}
    while min_number <= limit:
        new_values = set()
        for i in old_values:
            for n in primesL:
                mul = i * n
                new_values.add(mul)
                if mul <= limit:
                    result.add(mul)
        min_number = min(new_values)
        old_values = {i for i in new_values if i < limit}
    return [len(result), max(result)]
