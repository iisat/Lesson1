import random

# Выбираем тип операции
optype = input('Выберите тип операции (s - символ, i - целое, f - вещественное: ')
# Если выбран символ
if optype == 's':
    symbola = ord(input('Ввведите первый символ: '))
    symbolb = ord(input('Введите второй символ: '))
    if symbola > symbolb:
        symbola, symbolb = symbolb, symbola
    print(chr(random.randint(symbola, symbolb)))
    exit(0)
# Если выбрано число - запоминаем числа
numa = input('Ввведите первое число: ')
numb = input('Введите второе число: ')
# Вычисление для вещественных чисел
if optype == 'f':
    numa = float(numa)
    numb = float(numb)
    print(random.uniform(numa, numb))
    exit(0)
# Вычисление для целых чисел
if optype == 'i':
    numa = int(numa)
    numb = int(numb)
    if numa > numb:
        numa, numb = numb, numa
    print(random.randint(numa, numb))
