# Task 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
ind_min = 0
for i in range(1, len(array)):
    if array[i] < array[ind_min]:
        ind_min = i

ind_max = 0
for f in range(1, len(array)):
    if array[f] > array[ind_max]:
        ind_max = f

array[ind_min], array[ind_max] = array[ind_max], array[ind_min]
print(array)
