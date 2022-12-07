# Напишите программу, 
# которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

number = int(input('Введите колличество элементов списка: '))
my_list = []
for i in range(number):
    my_list.append(int(input(f'Введите число: ')))

new_list = []
for i in range(len(my_list) // 2):
    new_list.append(my_list[i] * my_list[(len(my_list) - i - 1)])
if number % 2 != 0:
    new_list.append(my_list[len(my_list) // 2] * my_list[len(my_list) // 2])
print(f'{my_list} -> {new_list}')