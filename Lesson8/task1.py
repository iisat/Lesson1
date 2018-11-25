# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок
# в этой строке. Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или
# встроенную функцию hash()
import collections

# Используем обычный массив
def count_substrings(s):
    hashesarray = []
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if hash(s[i:j + 1]) not in hashesarray:
                hashesarray.append(hash(s[i:j + 1]))
    return (len(hashesarray) - 2)

# Используем словарь
def mod_count_substrings(s):
    d = collections.OrderedDict()
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            d.update({s[i:j + 1]:hash(s[i:j + 1])})
    return (len(d) - 2)


print(mod_count_substrings('mama'))