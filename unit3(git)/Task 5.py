# Task 5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

B = []
for i in array:
    if i < 0:
        B.append(i)

array_max = B[0]
for p in B[1:]:
    if p > array_max:
        array_max = p

print(f'Наибольшее отрицательное чистл: {array_max}')



