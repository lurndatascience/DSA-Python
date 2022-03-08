# Program to demonstrate Merge Sort

def merge_sort(ls):
    if len(ls) > 1:
        left_list = ls[:len(ls) // 2]
        right_list = ls[len(ls) // 2:]

        # Recursion
        merge_sort(left_list)
        merge_sort(right_list)

        # Merge Lists
        i = 0  # Left most Index to track :param left_list
        j = 0  # Left most Index to track :param right_list
        k = 0  # Left most Index to track :param merged_list

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                ls[k] = left_list[i]
                i += 1
                k += 1
            else:
                ls[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            ls[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            ls[k] = right_list[j]
            j += 1
            k += 1


list_to_sort = [2, 1, 7, 8, 4, 6, 5, 9, 3]
merge_sort(list_to_sort)
print(list_to_sort)
