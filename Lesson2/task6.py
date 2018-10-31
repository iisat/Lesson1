import random

number = random.randint(0, 100)
i = 10
print('Загадано число от 0 до 100. У вас есть 10 попыток чтобы отгадать число')
while i > 0:
    answer = int(input('Введите вариант ответа: '))
    if answer == number:
        print('Вы угадали!')
        exit(0)
    if answer > number:
        print('Ваше число больше загаданного')
    if answer < number:
        print('Ваше число меньше загаданного')
    i = i - 1
    print(f'Попыток осталось: {i}')
print(f'Вы не угадали! Было загадано число {number}')
