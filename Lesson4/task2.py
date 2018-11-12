# Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile

# Вариант 1 - используем решето Эратосфена
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
    del a
    return(b[f - 1])

# Вариант 2. Поиск простых чисел делением на все предыдущие найденные
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
    return(simplenums[f - 1])

#
# Тестируем производительность для первого варианта:
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.erathnum(1)"
# 100 loops, best of 5: 92.9 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.erathnum(10)"
# 100 loops, best of 5: 1.39 msec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.erathnum(100)"
# 100 loops, best of 5: 12.7 msec per loop
#
# cProfile.run('erathnum(100)')       1    0.013    0.013    0.013    0.013 task2.py:9(erathnum)
# cProfile.run('erathnum(1000)')      1    0.164    0.164    0.166    0.166 task2.py:9(erathnum)
# cProfile.run('erathnum(10000)')     1    2.043    2.043    2.058    2.058 task2.py:9(erathnum)
#
# Тестируем для второго алгоритма
#
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.findsimple(1)"
# 100 loops, best of 5: 640 nsec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.findsimple(10)"
# 100 loops, best of 5: 59.7 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import task2" "task2.findsimple(100)"
# 100 loops, best of 5: 4.98 msec per loop
#
#cProfile.run('findsimple(100)')         1    0.008    0.008    0.008    0.008 task2.py:31(findsimple)
#cProfile.run('findsimple(1000)')        1    1.270    1.270    1.276    1.276 task2.py:31(findsimple)
#cProfile.run('findsimple(2000)')         1    4.554    4.554    4.567    4.567 task2.py:31(findsimple)
#
# Вывод - второй алгоритм показывает большую скорость при нахождении небольшого количества простых чисел,
# но с ростом количества чисел, которые необходимо найти теряет эффективность,
# т.к. количество операций растет экспоненциально