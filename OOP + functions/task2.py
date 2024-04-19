def minimum(*args):
    list_to_sort = list(args)
    list_to_sort.sort()
    return f"The minimum is {list_to_sort[0]}"


def maximum(*args):
    list_to_sort = list(args)
    list_to_sort.sort(reverse=True)
    return f"The maximum is {list_to_sort[0]}"


if __name__ == '__main__':
    print(minimum(1, 3, 6, 2, 7, 52, 74, 24324))
    print(maximum(1, 3, 6, 2, 7, 52, 74, 24324))
