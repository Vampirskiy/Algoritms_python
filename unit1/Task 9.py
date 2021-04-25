# Task 9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
# Ссылка на блоксхемму: https://drive.google.com/file/d/1CWZdBmnP5ZthIUBzcMC-MAJ7fkAlAwx-/view?usp=sharing

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if (a > b > c) or (a < b < c):
    print(f'Среднее число {b}')
else:
    if (b > c > a) or (b < c < a):
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')