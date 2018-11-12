# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего
# задания первых трех уроков.
# Алгоритм: Определить, какое число в массиве встречается чаще всего.

import random
import cProfile


# Вариант #1
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
    return maxpos

# Вариант #2 (ваш вариант, слегка модернизированный - добавлен параметр RANGEMAX и обернутый в функцию
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
    return num, frequency

# Слабым местом моего алгоритма является то, что при большом RANGEMAX массив, использующийся для подсчетов слишком сильно растет в размере.
# Исходя из этого проведем замеры производительности двумя способами - меняя RANGEMAX при константном SIZE и наоборот
# Сначала меняем RANGEMAX
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(10, 10000)"
# 100 loops, best of 5: 929 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(10, 100000)"
# 100 loops, best of 5: 9.03 msec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(10, 1000000)"
# 100 loops, best of 5: 93.6 msec per loop
#
# Далее меняем SIZE при константном RANGEMIN
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(1000, 10)"
# 100 loops, best of 5: 2.03 msec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(10000, 10)"
# 100 loops, best of 5: 20.5 msec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.maxfreq(100000, 10)"
# 100 loops, best of 5: 205 msec per loop
#
#cProfile.run('maxfreq(10, 10000)')        1    0.001    0.001    0.001    0.001 task1_l3t4.py:6(maxfreq)
#cProfile.run('maxfreq(10, 100000)')       1    0.009    0.009    0.009    0.009 task1_l3t4.py:6(maxfreq)
#Profile.run('maxfreq(10, 1000000)')       1    0.093    0.093    0.093    0.093 task1_l3t4.py:6(maxfreq)
#cProfile.run('maxfreq(10000, 10)')        1    0.011    0.011    0.053    0.053 task1_l3t4.py:6(maxfreq)
#cProfile.run('maxfreq(100000, 10)')       1    0.077    0.077    0.358    0.358 task1_l3t4.py:6(maxfreq)
#cProfile.run('maxfreq(1000000, 10)')      1    0.734    0.734    3.473    3.473 task1_l3t4.py:6(maxfreq)
#
# Проведем тестирование второго варианта алгоритма с теми же параметрами
#
# Меняем RANGEMAX
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(10, 10000)"
# 100 loops, best of 5: 31.6 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(10, 100000)"
# 100 loops, best of 5: 40.5 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(10, 1000000)"
# 100 loops, best of 5: 34.2 usec per loop
#
# Меняем SIZE (TimeIT пришлось запускать с меньшими SIZE, т.к. при росте SIZE алгоритм быстро теряет эффективность)
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(10, 10)"
# 100 loops, best of 5: 31 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(100, 10)"
# 100 loops, best of 5: 1.2 msec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task1_l3t4" "task1_l3t4.teachersmaxfreq(1000, 10)"
# 100 loops, best of 5: 110 msec per loop
#
#cProfile.run('teachersmaxfreq(10, 10000)')        1    0.000    0.000    0.000    0.000 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('teachersmaxfreq(10, 100000)')       1    0.000    0.000    0.000    0.000 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('teachersmaxfreq(10, 1000000)')      1    0.000    0.000    0.000    0.000 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('teachersmaxfreq(100, 10)')          1    0.001    0.001    0.001    0.001 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('teachersmaxfreq(1000, 10)')         1    0.106    0.106    0.109    0.109 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('teachersmaxfreq(10000, 10)')        1    8.184    8.184    8.211    8.211 task1_l3t4.py:26(teachersmaxfreq)
#
# Проведем дополнительные замеры масштабируемости, увеличивая одновременно параметры SIZE и RANGEMAX
#
#cProfile.run('teachersmaxfreq(10, 10)')        1    0.000    0.000    0.002    0.002 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('maxfreq(10, 10)')                1    0.000    0.000    0.000    0.000 task1_l3t4.py:8(maxfreq)
#cProfile.run('teachersmaxfreq(100, 100)')      1    0.001    0.001    0.001    0.001 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('maxfreq(100, 100)')              1    0.000    0.000    0.001    0.001 task1_l3t4.py:8(maxfreq)
#cProfile.run('teachersmaxfreq(1000, 1000)')    1    0.277    0.277    0.288    0.288 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('maxfreq(1000, 1000)')            1    0.003    0.003    0.013    0.013 task1_l3t4.py:8(maxfreq)
#cProfile.run('teachersmaxfreq(10000, 10000)')  1   10.959   10.959   11.017   11.017 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('maxfreq(10000, 10000)')          1    0.020    0.020    0.089    0.089 task1_l3t4.py:8(maxfreq)
#cProfile.run('teachersmaxfreq(100000, 100000)')1  949.559  949.559  950.063  950.063 task1_l3t4.py:26(teachersmaxfreq)
#cProfile.run('maxfreq(100000, 100000)')        1    0.167    0.167    0.778    0.778 task1_l3t4.py:8(maxfreq)
#cProfile.run('maxfreq(1000000, 1000000)')      1    1.406    1.406    5.140    5.140 task1_l3t4.py:8(maxfreq)
#cProfile.run('maxfreq(10000000, 10000000)')    1   14.630   14.630   53.828   53.828 task1_l3t4.py:8(maxfreq)
#
#
# Вывод:
# Первый вариант чувствителен к диапазону чисел, но лучше справляется с массивами из большего числа элементов.
# Второй вариант нечувствителен к диапазону чисел, но быстро теряет эффективность при увеличении числа элекментов
# в массиве