# Напишите программу, 
# которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

a = int(input('Введите число: '))
if 1 <= a < 6:
    print('Рабочий')
elif a == 6 or a == 7:
    print('Выходной')
else:
    print('Введите правильное число')


day = int(input('Введите день недели: '))
if 0 < day < 8:
    if day == 6 or day == 7:
        print('Выходной')
    else:
        print('Выходной')
else:
    print('Введено некорректное значение')


match day:
    case 1:
        print('Понедельник')
    case 2:
        print('Вторник')
    case 3:
        print('Среда')
    case 4:
        print('Четверг')
    case 5:
        print('Пятница')
    case 6:
        print('Суббота')
    case 7:
        print('Воскресенье')
    case _:
        print('Введено некорректное значение')