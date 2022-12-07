# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input('Введите число: '))

right = [0, 1]
for i in range(number - 1):
    right.append(right[i] + right[i + 1])

left = []
for i in range(number):
    if i % 2 == 0:
        left.insert(0, right[i + 1])
    else:
        left.insert(0, right[i + 1]*(-1))

result = left + right
print(result)
