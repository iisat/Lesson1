# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок
# в этой строке. Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или
# встроенную функцию hash()

def count_substrings(s):
    hashesarray = []
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if hash(s[i:j + 1]) not in hashesarray:
                hashesarray.append(hash(s[i:j + 1]))
    return (len(hashesarray) - 2)

print(count_substrings('mama'))