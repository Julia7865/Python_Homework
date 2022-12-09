# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

from decimal import Decimal

number = abs(Decimal(input('Введите число: ')))
original = number

def sum_digits(number: int):
    summ = 0
    while number != 0:
        summ += number % 10
        number //= 10 
    return summ

while(number != int(number)):
    number *= 10

summ = sum_digits(number)
print(f'Сумма цифр в числе {original} равна {int(summ)}')

# number = input('Введите число: ')
# summ = 0
# for i in number:
#   if i.isdigit():           # i != '.' and i != ',' and i != '-':    
#       summ += int(i)
# print(summ)