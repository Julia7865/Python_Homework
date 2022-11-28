# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

number = abs(int(input('Введите число: ')))
sum = 0
while number != 0:
    sum += number % 10
    number //= 10 
print(sum)


# number = input('Введите число: ')
# sum = 0
# for i in number:
#     sum += int(i)
# print(sum)