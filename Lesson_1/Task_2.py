# Напишите программу для проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.


x = int(input())
y = int(input())
z = int(input())
left = not (x or y or z)
rigth = not x and not y and not z
if left == rigth:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')

# Не получилось