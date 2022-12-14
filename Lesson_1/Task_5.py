# Напишите программу, 
# которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве 
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)

# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x1, y1 = int(input('Введите X1: ')), int(input('Введите Y1: '))
x2, y2 = int(input('Введите X2: ')), int(input('Введите Y2: '))
distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
print(f'Расстояние мужду точками {x1, y1}, {x2, y2} равно {distance}')


# В 3D пространстве
x1, y1, z1 = int(input('Введите X1: ')), int(input('Введите Y1: ')), int(input('Введите Z1: '))
x2, y2, z2 = int(input('Введите X2: ')), int(input('Введите Y2: ')), int(input('Введите Z2: '))
distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z1 - z2) ** 2) ** 0.5, 2)
print(f'Расстояние мужду точками {x1, y1, z1}, {x2, y2, z2} равно {distance}')


coords = input('Введите координаты через пробел: ').split(' ')
print(coords)
result = math.sqrt((int(coords[0]) - int(coords[2])) ** 2 + (int(coords[1]) - int(coords[3])) ** 2)
print(round(result, 2))

coords = []
for i in range(6):
    coords.append(float(input(f'Введите координаты')))