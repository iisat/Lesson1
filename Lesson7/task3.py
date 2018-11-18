# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.
import random

def ar_gen(SIZE, MIN, MAX):
    array = []
    for _ in range(SIZE):
        array.append(random.randint(MIN, MAX))
        #array.append(random.uniform(MIN, MAX))
    return array

def find_med(array):
    source = array.copy()
    result = []
    i = len(source) - 1
    while i > -1:
        pointer = i
        for j in range(0,len(source)):
            if source[j] < source[pointer]:
                 pointer = j
        result.append(source[pointer])
        source.remove(source[pointer])
        i -= 1
    answer = len(result) // 2
    return result[answer]

array = ar_gen(7, 0, 10)
print(array)
print(find_med(array))