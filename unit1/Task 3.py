# Task 3
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# Ссылка на блоксхемму: https://drive.google.com/file/d/1sn_t04SMo0qa03aAW8hffjfbMBkpweF_/view?usp=sharing

a1 = int(input('Введите x1:  '))
b1 = int(input('Введите y1:  '))
a2 = int(input('Введите x2:  '))
b2 = int(input('Введите y2:  '))
c1 = b2 - b1
c2 = a2 - a1
c3 = (c2 * a1) - (c1 * b1)
print(f'y = {c1 / c2}x + {c3 / c2}')