ls = [2, 1, 7, 8, 4, 6, 5, 9, 0, 3]
iterations = 0

for index in range(1, len(ls)):

    value = ls[index]
    i = index - 1
    while i >= 0:
        #   2    < 1
        iterations += 1
        if value < ls[i]:
            ls[i + 1] = ls[i]
            ls[i] = value
            i = i - 1
        else:
            break
print("Number of Iterations ", iterations)
print(ls)
