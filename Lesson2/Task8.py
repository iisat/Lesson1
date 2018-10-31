number = input('Введите целое число: ')
count = input('Введите цифру которую необходимо посчитать: ')
counter = 0
for i, c in enumerate(number):
    print(c)
    if c == count:
        counter = counter + 1
print(f'Число заданных цифр в числе: {counter}')
