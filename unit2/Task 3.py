# Task 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
# Ссылка на блоксхемму: https://drive.google.com/file/d/1bvann3ezuU5zTzZ8WPrnAFt90KuRUktF/view?usp=sharing

def reverse_s(s):
    return ''.join(reversed(s))
 
print(f'Обратное число: {reverse_s(input("Введите число: "))}')