# Task 1
# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
#● написать 3 варианта кода (один у вас уже есть),
#● проанализировать 3 варианта и выбрать оптимальный,
#● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#● написать общий вывод: какой из трёх вариантов лучше и почему.

# За исходник взята задача 7 из урока 2


import timeit
import cProfile

# рекурсия
def m(n):
    if n == 1:
        return 1
    return m(n - 1) + n

# Квадратная функция
def f(n):
    return int(n*(n+1)/2)

# Цыкл
def c(n):
    x = 0
    for i in range(n + 1):
        x += i
    return x


# рекурсия исследования
print(timeit.timeit('m(5)', number=1000, globals=globals()))  #0.0004708000000000004
print(timeit.timeit('m(10)', number=1000, globals=globals())) #0.0009131999999999994
print(timeit.timeit('m(20)', number=1000, globals=globals())) #0.0018156000000000005
print(timeit.timeit('m(40)', number=1000, globals=globals())) #0.004103699999999998
print(timeit.timeit('m(80)', number=1000, globals=globals())) #0.008779899999999997
cProfile.run('m(5)')
#                   8 function calls (4 primitive calls) in 0.000 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      5/1    0.000    0.000    0.000    0.000 Task 1.py:15(m)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# рекурсия исследования
print(timeit.timeit('f(5)', number=1000, globals=globals()))  #0.0003263000000000016
print(timeit.timeit('f(10)', number=1000, globals=globals())) #0.0001729000000000036
print(timeit.timeit('f(20)', number=1000, globals=globals())) #0.00018270000000000092
print(timeit.timeit('f(40)', number=1000, globals=globals())) #0.00019129999999999842
print(timeit.timeit('f(80)', number=1000, globals=globals())) #0.00019099999999999673
cProfile.run('f(5)')
#                    4 function calls in 0.000 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task 1.py:21(f)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# цикл исследования
print(timeit.timeit('c(5)', number=1000, globals=globals()))  #0.00040279999999999483
print(timeit.timeit('c(10)', number=1000, globals=globals())) #0.0005346999999999991
print(timeit.timeit('c(20)', number=1000, globals=globals())) #0.0013385999999999953
print(timeit.timeit('c(40)', number=1000, globals=globals())) #0.002659499999999995
print(timeit.timeit('c(80)', number=1000, globals=globals())) #0.0027125999999999956
cProfile.run('c(5)')
#                    4 function calls in 0.000 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task 1.py:26(c)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}