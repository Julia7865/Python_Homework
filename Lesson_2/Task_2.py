# Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.


number = int(input('Введите число: '))
my_list = []
for i in range(1, number + 1):
    my_list.append(round(((1 + 1/i)**i), 2))
print(my_list)
summ = 0
for i in range(len(my_list)):
    summ += my_list[i]
print(summ)