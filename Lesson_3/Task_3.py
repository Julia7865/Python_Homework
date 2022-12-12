# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов. 
# (подробности в конце записи семинара).

# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# number = int(input('Введите колличество элементов списка: '))
# my_list = []
# for i in range(number):
#     my_list.append(float(input(f'Введите число: ')))
# print(my_list)

# new_list = []
# for i in range(len(my_list)):
#     new_list.append(round((my_list[i] % 1), 2))
# print(new_list)

# max = new_list[0]
# min = new_list[0]
# for j in range(len(new_list)):
#     if new_list[j] > max:
#         max = new_list[j]
#     if new_list[j] < min and min != 0.0:
#         min = new_list[j]
# print(f'{max}, {min}')
# print(f'{max - min}')

import random
size = int(input('Введите размер списка: '))

my_list = [round(random.uniform(0, 10), 2) for _ in range(size)]

def devine(number: float) -> float:
    return round(number%1, 2)

print(my_list)
my_list = list(map(devine, my_list))
print(my_list)
print(max(my_list) - min(my_list))