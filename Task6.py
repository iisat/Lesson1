# Ввод длин отрезков
la = (input('Введите длинну первого отрезка: '))
lb = (input('Введите длинну вторго отрезка: '))
lc = (input('Введите длинну третьего отрезка: '))
# Проверка существует ли треугольник
if (la + lb >= lc) or (lb + lc >= la) or (la + lc >= lb):
    print('Треугольник существует')
    if (la == lb == lc):
        print('Треугольник равносторонний')
        exit(0)
    if (la == lb) or (lb == lc) or (la == lc):
        print('Треугольник равнобедренный')
        exit(0)
    print('Треугольник разносторонний')
    exit(0)
print('Такого треугольника не существует!')
