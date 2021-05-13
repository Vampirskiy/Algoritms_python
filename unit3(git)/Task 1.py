# Task 1
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

d_min = 2
d_max = 99
k_min = 2
k_max = 9

for p in range(k_min, k_max + 1):
    count = 0
    for i in range(d_min, d_max + 1):
        if i % p == 0:
            count += 1
    print(f'Чесел кратных {p} {count} штук')


