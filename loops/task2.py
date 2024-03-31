sequence = [1, 2, 3, 4, 5, 6, 8, 9]

for i in range(len(sequence)):
    if sequence[i+1] - sequence[i] != 1:
        print(f"List is not consistent starting from {sequence[i+1]}.")
        break
    else:
        continue

