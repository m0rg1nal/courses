numbers = [1, 2, 3, 5, 7, 8, 354, 456, 234, 654, 758, 324, 573, 543, 9, 10]
divider = float(input('Enter any number as a divider: '))
divided = []

for i in numbers:
    if i % divider == 0:
        print(i)
