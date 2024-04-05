first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
first_set = set(first)
second_set = set(second)
united = first_set.intersection(second_set)
print(f'{united} - list of intersecting numbers in two lists.')
