import sys

# вариант 2
num = 5623096547834578
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")
print(sys.getsizeof(num))
print(sys.getsizeof(even))
print(sys.getsizeof(odd))



