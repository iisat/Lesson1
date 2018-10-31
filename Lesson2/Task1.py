while True:
    operator = input('Выберите операцию (+,-,/,*,) или введите 0 для завершения работы: ')
    if operator not in ['0', '+', '-', '/', '*']:
        print('Операция не распознана')
    if operator == '0':
        break
    numa = float(input('Введите число a: '))
    numb = float(input('Введите число b: '))
    if operator == '+':
        print(f'Сумма равна {numa+numb}')
    if operator == '-':
        print(f'Разность равна {numa-numb}')
    if operator == '*':
        print(f'Результат умножения: {numa*numb}')
    if operator == '/':
        if 0 != numb:
            print(f'Результат деления: {numa/numb}')
        else:
            print('Не дели на 0!')
