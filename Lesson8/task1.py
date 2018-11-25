# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок
# в этой строке. Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или
# встроенную функцию hash()

import collections, cProfile, random, string

# Генератор строки
def str_gen(size):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))

# Используем обычный массив
def count_substrings(s):
    hashesarray = []
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if hash(s[i:j + 1]) not in hashesarray:
                hashesarray.append(hash(s[i:j + 1]))
    return (len(hashesarray) - 2)

# Используем словарь с хешем в качестве индекса
def mod_count_substrings(s):
    d = collections.OrderedDict()
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            d.update({s[i:j + 1]:hash(s[i:j + 1])})
    return (len(d) - 2)

# Генерируем строку
s = str_gen(100)
print(s)

# Проверяем работу функции
print(count_substrings('mama'))
print(count_substrings('mama'))
print(count_substrings(s))
print(mod_count_substrings(s))

# Сравниваем скорость:
#cProfile.run('count_substrings(s)')             1    0.660    0.660    0.669    0.669 task1.py:16(count_substrings)
#cProfile.run('mod_count_substrings(s)')         1    0.018    0.018    0.030    0.030 task1.py:25(mod_count_substrings)

# Вывод: использование хешей в качестве индекса словаря - прекрасная идея
