# Ввод года
year = int(input('Введите год: '))
# Проверяем год на високосность
if (year % 4) > 0:
    print ('Год не високосный')
    exit(0)
if (year %4 ) == 0:
    if (year % 100) > 0:
        print('Год високосный')
        exit(0)
    if (year % 400) > 0:
        print('Год не високосный')
        exit(0)
    print('Год високосный')


