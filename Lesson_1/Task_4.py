# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


a = int(input('Введите номер четверти: '))
if a == 1:
    print('Диапазон возможных координат точек: х > 0, y > 0')
elif a == 2:
    print('Диапазон возможных координат точек: х < 0, y > 0')
elif a == 3:
    print('Диапазон возможных координат точек: х < 0, y < 0')
elif a == 4:
    print('Диапазон возможных координат точек: х > 0, y < 0')
else:
    print('Введите правильное число')
