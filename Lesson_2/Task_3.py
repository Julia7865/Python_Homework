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