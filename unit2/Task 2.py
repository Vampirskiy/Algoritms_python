# Task 2
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# Ссылка на блоксхемму: https://drive.google.com/file/d/1vRvEn7jcFUj2X4zD2leAMOUK4dvP_107/view?usp=sharing

chi = input('Введите чисто: ')
ch = 0
nch = 0

for i in map(int, str(chi)):
    if i % 2 == 0:
        ch += 1
    else:
        nch += 1
print(f'Четных цифр: {ch}, Не четных цифр: {nch}')