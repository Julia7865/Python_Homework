# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = []
# for i in range(5):
#     my_list.append(int(input(f'Введите число: ')))

# summ = 0
# for i in range(1, len(my_list), 2):
#     summ += my_list[i]
# print(f'Сумма нечетных элементов списка {my_list} равна {summ}')

import random

size = int(input('Введите размер списка: '))
my_list = [random.randint(-10, 10) for _ in range(size)]
print(my_list)

summ = 0
for i, item in enumerate(my_list):
    if i%2 != 0:
        summ += item
print(summ)