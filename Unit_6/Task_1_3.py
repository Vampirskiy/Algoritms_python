import sys

# вариант 3
x = 5623096547834578
even = odd = 0
for i in str(x):
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    else:
        odd += 1
print(f"четных - {even}, нечетных - {odd}")
print(sys.getsizeof(x))
print(sys.getsizeof(even))
print(sys.getsizeof(odd))
print(sys.getsizeof(i))