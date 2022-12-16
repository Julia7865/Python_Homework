# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

n = int(input('Введите степень: '))

def polynominal(num, min, max):
    result = ''
    for k in range(num, 1, -1):
        koefficient = random.randint(min, max)
        if koefficient != 0:
            result += f'{koefficient}*x**{k} + '
    penultimate = random.randint(min, max)
    if penultimate != 0:
        result += f'{penultimate}*x + '
    last = random.randint(min, max)
    if last != 0:
        result += f'{last}'
    result += ' = 0'
    return result

first_polynominal = polynominal(n, 0, 100)
second_polynominal = polynominal(n, 0, 100)
print(first_polynominal)
print(second_polynominal)

data = open('first.txt', 'w')
data.write(first_polynominal)
data.close()

data2 = open('second.txt', 'w')
data2.write(second_polynominal)
data2.close()