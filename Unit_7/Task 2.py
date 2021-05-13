# Task 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left_A = A[:middle]
    right_A = A[middle:]
    left_A = merge_sort(left_A)
    right_A = merge_sort(right_A)
    return list(merge(left_A, right_A))

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result

print(merge_sort(array))