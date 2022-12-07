# Напишите программу для проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.



def equality():
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                print(f'При {x} {y} {z} -> {(not (x or y or z))} -> {(not (x) and not (y) and not (z)):}')
                if (not (x or y or z)) != (not (x) and not (y) and not (z)):
                    return 'Условие не выполняется'
    return 'Выражение истинно'
print(equality())

def equality():
    count = 0
    for x in ['a', 'b', 'c']:
        for y in ['1', '2', '3']:
            for z in ['!', '-', '?']:
                print(f'При {x} {y} {z}')
                count += 1
    print(count)
print(equality())

# x y z
# t t t 
# t t f
# t f f
# f t t
# f f t
# f t f
# f f f