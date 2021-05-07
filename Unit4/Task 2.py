# Task 2
#Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

#Первый — с помощью алгоритма «Решето Эратосфена».
#Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.


import timeit
import cProfile

Ziro = 0


def resh(num):
    size = num ** 2 + 3
    assert num <= 5761455, 'Большой аргумент'
    if num > 5761455:
        raise Exception('Большой аргумент')
    
    array = [i for i in range(size)]

    array[1] = Ziro
    for i in range(2, size):
        if array[i] != Ziro:
            p = i ** 2
            while p < size:
                array[p] = Ziro
                p += i

    res = [i for i in array if i != Ziro]
    return res[num - 1]

number = 1
while number < 4100:
    number *= 2
    TNT = timeit.timeit('resh(number)', number=1000, globals=globals())
    print(f"{number=}\t{TNT=}\t{TNT / number =}")

#number=4        TNT=0.0049149                   TNT / number =0.001228725
#number=8        TNT=0.015539399999999995        TNT / number =0.0019424249999999994
#number=16       TNT=0.0572377                   TNT / number =0.00357735625
#number=32       TNT=0.2396834                   TNT / number =0.00749010625
#number=64       TNT=0.9829990000000001          TNT / number =0.015359359375000001
#number=128      TNT=4.1653169                   TNT / number =0.03254153828125
#number=256      TNT=18.6053196                  TNT / number =0.0726770296875
#number=512      TNT=79.5329824                  TNT / number =0.15533785625
#number=1024     TNT=362.1264873                 TNT / number =0.35363914775390626
#number=2048     TNT=1574.1166474000001          TNT / number =0.7686116442382813
#number=4096     TNT=6624.188038000001           TNT / number =1.617233407714844



cProfile.run('resh(4100)')

#       6 function calls in 7.294 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.141    0.141    7.294    7.294 <string>:1(<module>)     
#        1    5.807    5.807    7.153    7.153 Task 2.py:15(resh)
#        1    0.820    0.820    0.820    0.820 Task 2.py:21(<listcomp>)
#        1    0.525    0.525    0.525    0.525 Task 2.py:31(<listcomp>)
#        1    0.000    0.000    7.294    7.294 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}











