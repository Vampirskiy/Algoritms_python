#Task
#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
#Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple
Otchet = []
Corp = namedtuple('corp', 'name, I, II, III, IV, ИТОГО')
col = int(input('Введите количество компаний: '))
M = 0
for i in range(col):
    name = input('Введите имя компании: ')
    balans = []
    balans_sum = 0
    for x in range(1, 5):
        x = (float(input(f'{x} = ')))
        balans.append(x)
        balans_sum += x
    Otchet.append(Corp(name, *balans, balans_sum))
    M += balans_sum
good = []
bed = []
for v in range(col):
    w = Otchet[v]
    if w[5] >= M / col:
        good.append(w[0])
    if w[5] < M / col:
        bed.append(w[0])

print(f'Общая прибыль: {M}')
print(f'Прибыль выше среднего у компаний: {good}')
print(f'Прибыль ниже среднего у компаний: {bed}')
for o in Otchet:
    print(o)
