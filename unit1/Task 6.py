# Task 6
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Ссылка на блоксхемму: https://drive.google.com/file/d/1033GR7-5qWp4K3oSrsq-eWiqQMDA1GmS/view?usp=sharing

n = int(input('Введите порядковый номер буквы алфавита: '))
print(f'Порядковый номер соответствует букве: {chr(n + 96)}')