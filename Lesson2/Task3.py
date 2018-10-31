number = input('Введите целое число: ')
nlen = len(number) - 1
while nlen >= 0:
    print(number[nlen], end='')
    nlen = nlen - 1
