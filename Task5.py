# Вввод символов, приведение их к нижнему регистру, конвертация в номер
symbola = ord((input('Ввведите первый символ: ')).lower()) - 96
symbolb = ord((input('Введите второй символ: ')).lower()) - 96
# Своп при необходимости
if symbola > symbolb:
    symbola, symbolb = symbolb, symbola
# Вывод результата
print(
    f'Введенные символы занимают в алфавите места {symbola} и {symbolb} и между ними символов: {symbolb - symbola -1}')
