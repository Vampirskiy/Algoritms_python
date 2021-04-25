# Task 7
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
# Ссылка на блоксхемму: https://drive.google.com/file/d/14vZjr7HoUfCmdr0BNCNs41PCJdkclAL2/view?usp=sharing


def m(n):
    if n == 1:
        return 1
    return m(n - 1) + n

def f(n):
    return int(n*(n+1)/2)

b = '(1+2+...+n = n(n+1)/2)'
s = int(input('Введите придел вычисления: ' ))
if m(s) == f(s):
    print(f'Равенство {b} выполняется ( {m(s)} = {f(s)} )')
else:
    print(f'Равенство {b} не выполняется ( {m(s)} = {f(s)} )')