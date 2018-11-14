# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.
# Версия python: Python 3.7.0
# Разрядность ОС - 64 бит

import random
import sys

# Немного модифицировал функцию, которую вы написали на уроке - вместо вывода на экран она считает размер переменной
def mod_size(x, size = 0):
    size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

# Данную функцию тоже немного переписал. Перед завершением работы она выводит суммарно сколько памяти использовали
# все переменные
def maxfreq(SIZE, RANGEMAX):
    array = []
    for _ in range(SIZE):
        array.append(random.randint(0, RANGEMAX))

    countarray = [0] * (RANGEMAX + 1)

    for i in range(SIZE):
        num = array[i]
        countarray[num] += 1

    maxpos = 0

    for i in range(RANGEMAX):
        if countarray[i] > maxpos:
            maxpos = i
    print(mod_size(maxpos))
    print(mod_size(array))
    print(mod_size(countarray))
    print(f'Summary: {mod_size(maxpos) + mod_size(array) + mod_size(countarray)}')
    return maxpos

# Вариант #2 Сделал тоже самое и для этой функции
def teachersmaxfreq(SIZE, RANGEMAX):
    array = [random.randint(0, RANGEMAX) for _ in range(SIZE)]
    num = array[0]
    frequency = 1
    for i in range(SIZE):
        spam = 1
        for k in range(i + 1, SIZE):
            if array[i] == array[k]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    print(mod_size(array))
    print(mod_size(num))
    print(mod_size(frequency))
    print(mod_size(spam))
    print(f'Summary: {mod_size(array) + mod_size(num) + mod_size(frequency) + mod_size(spam)}' )

    return num, frequency

# Вызываем функции с разными параметрами и смотрим расход памяти
#maxfreq(1000, 1000)
# 14
# 18512
# 17296
# Summary: 35822
#teachersmaxfreq(1000, 1000)
# 118516
# 14
# 14
# 14
# Summary: 18558
#maxfreq(10000, 10000)
#14
#183814
#172634
#Summary: 356462
#teachersmaxfreq(10000, 10000)
#183816
#14
#14
#14
#Summary: 183858

# Вывод - функция 1 - жертвуем памятью ради быстродействия, функция 2 - жертвуем быстродействием - экономим память

# Подсчитаем память для других двух функций (разные реализации поиска простого числа) В данном случае считал размер
# только тех переменных размер которых изменяется с изменением параметров функции
# Вариант 1 - используем решето Эратосфена. Модернизирована под подсчет памяти
def erathnum(f):
    n = f * 100
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    #del a
    print(mod_size(a))
    print(mod_size(b))
    print(f'Summary: {mod_size(a) + mod_size(b)}')
    return(b[f - 1])

# Вариант 2. Поиск простых чисел делением на все предыдущие найденные. Модернизирована под подсчет памяти
def findsimple(f):
    simplenums = [2]
    testednum = 2
    while len(simplenums) < f:
        counter = 0
        testednum += 1
        for i in range(0, (len(simplenums) - 1)):
            if (testednum % simplenums[i]) == 0:
                counter += 1
        if counter == 0:
            simplenums.append(testednum)
    print(f'Summary: {mod_size(simplenums)}')
    return(simplenums[f - 1])

# Измеряем

#erathnum(1000)
# #1631380
# #185376
# #Summary: 1816756
#
# #findsimple(1000)
# # Summary: 18076

#erathnum(100)
#162494
#22310
#Summary: 184804

#findsimple(100)
#Summary: 1868

# В данном случае можем сделать точно такой же вывод как и в первом случае - алгоритм, экономнее расходующий память
# требовательнее к производительности и наоборот.