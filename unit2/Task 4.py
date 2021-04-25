# Task 4
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
# Ссылка на блоксхемму: https://drive.google.com/file/d/1ADdb6XmleHL4v2jD4sIFKzJA8gHE9Mzq/view?usp=sharing

n = int(input('Введите количество элементов :'))
summa = 0
m = 0
a = 1
while m <= n:
    m += 1
    summa += a
    a = (-a /2)
print(summa)