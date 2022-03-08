
ls = [2, 1, 7, 8, 4, 6, 5, 9, 0, 3]
iterations = 0

for i in range(0, len(ls) - 1):
    for j in range(i, len(ls) - 1):
        iterations += 1
        if ls[j + 1] < ls[j]:
            # Swapping Numbers
            temp = ls[j]
            ls[j] = ls[j + 1]
            ls[j + 1] = temp
print(ls)
print("Number of Iterations are ", iterations)
