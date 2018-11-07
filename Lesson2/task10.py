low = int(0)
high = int(101)
tries = 10
while tries > 0:
    mytry = low + (high - low) // 2
    print(f'Мое число {mytry}')
    answer = input('Введите знак >, < или =: ')
    if answer == '=':
        print('Ура!')
        exit(0)
    if answer == '>':
        high = mytry
    if answer == '<':
        low = mytry
    tries = tries - 1
