ls = [2, 1, 7, 8, 4, 6, 5, 9, 0, 3]
iterations = 0

for i in range(0, len(ls)):
    pos_of_min_value = i
    for j in range(i):
        iterations += 1
        if ls[j] > ls[j + 1]:
            temp = ls[j]
            ls[j] = ls[j + 1]
            ls[j + 1] = temp
            pos_of_min_value = i

print(ls)
print("Number of Iterations are ", iterations)
