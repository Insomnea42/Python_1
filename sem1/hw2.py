# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('введите значение x: '))
y = bool(input('введите значение y: '))
z = bool(input('введите значение z: '))

if not (x or y or z) == ((not x) and (not y) and (not z)):
    print(1 == 1)
else:
    print(1 == 0)
