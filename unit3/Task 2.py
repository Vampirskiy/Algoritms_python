# Task 2
# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

A = [8, 3, 15, 6, 4, 2]
B = []
ind = 0
for i in A:   
    if i % 2 == 0:
        B.append(ind)
    ind += 1
print(f'Индексы четных чисел: {B}')