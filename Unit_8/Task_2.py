# Task_2
# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter


class SortedT:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def code_d(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    code_d(root.left, codes, code + '0')
    code_d(root.right, codes, code + '1')

    return codes


def tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        n = SortedT(None)

        if len(string_count) == 1:
            n.left = SortedT([key for key in string_count][0])
            n.right = SortedT(None)

        string_count = {n: 1}

    while len(string_count) != 1:
        n = SortedT(None)
        s = string_count.most_common()[:-3:-1]

        if isinstance(s[0][0], str):
            n.left = SortedT(s[0][0])

        else:
            n.left = s[0][0]

        if isinstance(s[1][0], str):
            n.right = SortedT(s[1][0])

        else:
            n.right = s[1][0]

        del string_count[s[0][0]]
        del string_count[s[1][0]]
        string_count[n] = s[0][1] + s[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


my_string = input('Введите строку для сжатия: ')
tree = tree(my_string)

codes = code_d(tree)
print(f'Ключи шифрования: {codes}')

coding_str = coding(my_string, codes)
print('Код строки: ', coding_str)
