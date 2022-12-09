# Реализуйте алгоритм перемешивания списка. 
# Встроенный алгоритм SHUFFLE не использовать! 
# Реализовать свой метод

import random
my_list = []
for i in range(0, 10):
    my_list.append(i+1)
print(my_list)

for i in range(len(my_list)):
    number = random.randint(0, 10)
    temp = my_list[i]
    my_list[i] = my_list[number]
    my_list[number] = temp
print(my_list)

for i in range(len(my_list)):
    n = random.randint(0, (len(my_list) - 1))
    my_list.append(my_list.pop(n))
print(f'Перемешанный список {my_list}')

for i in range(len(my_list)):
    n = random.randint(0, (len(my_list) - 1))
    my_list[i], my_list[n] = my_list[n], my_list[i]
print(f'Перемешанный список {my_list}')

random.shuffle(my_list)
print(f'Перемешанный список {my_list}')

# import datetime
# import time

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# length = len(my_list)
# print(f'Original my_list', list)

# for i in range(len(my_list)):
# n = datetime.datetime.now().microsecond % len(my_list)
# time.sleep(0.1)
# shuffled = my_list.pop(n)
# my_list.append(shuffled)
# print('Shuffled my_list', list)