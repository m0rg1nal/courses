height = int(input('Height of the pyramid: '))

for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
