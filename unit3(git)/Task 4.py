# Task 4
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
chislo = array[0]
c = 1
for i in array:
    count = 0
    for p in array:
        if i == p:
            count += 1
    if count > c:
        c = count
        chislo = array[i]

print(f'В данном массиве чаще других встречается число: {chislo}. Оно встречается {c} раз.')



