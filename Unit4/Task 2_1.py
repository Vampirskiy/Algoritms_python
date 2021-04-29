import timeit
import cProfile


def bez(num):
    n = 1
    m = 2

    while n < num:
        m += 1
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                break
        else:
            n += 1
    return m

number = 1
while number < 4100:
    number *= 2
    TNT = timeit.timeit('bez(number)', number=1000, globals=globals())
    print(f"{number=}\t{TNT=}\t{TNT / number =}")

#number=2        TNT=0.0005092000000000013       TNT / number =0.00025460000000000066
#number=4        TNT=0.0023355000000000008       TNT / number =0.0005838750000000002
#number=8        TNT=0.0077221999999999985       TNT / number =0.0009652749999999998
#number=16       TNT=0.0254435                   TNT / number =0.00159021875
#number=32       TNT=0.0664418                   TNT / number =0.00207630625
#number=64       TNT=0.19451480000000004         TNT / number =0.0030392937500000007
#number=128      TNT=0.4240893                   TNT / number =0.00331319765625
#number=256      TNT=1.0777273                   TNT / number =0.004209872265625
#number=512      TNT=2.4916694                   TNT / number =0.004866541796875
#number=1024     TNT=6.407302                    TNT / number =0.006257130859375
#number=2048     TNT=17.8390573                  TNT / number =0.008710477197265625
#number=4096     TNT=42.7364512                  TNT / number =0.01043370390625


cProfile.run('bez(4100)')

#       4 function calls in 0.136 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
#        1    0.042    0.042    0.042    0.042 Task 2_1.py:5(bez)
#        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
