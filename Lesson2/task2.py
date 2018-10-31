number = input('Введите целое число: ')
oddcnt = nonoddcnt = 0
for i, c in enumerate(number):
    check = int(c)
    if check % 2 == 0:
        oddcnt = oddcnt + 1
    else:
        nonoddcnt = nonoddcnt + 1
print(f'Число четных цифр: {oddcnt}')
print(f'Число нечетных цифр: {nonoddcnt}')


