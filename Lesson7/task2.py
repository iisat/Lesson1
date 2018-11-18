# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

def ar_gen(SIZE, MIN, MAX):
    array = []
    for _ in range(SIZE):
        #array.append(random.randint(MIN, MAX))
        array.append(random.uniform(MIN, MAX))
    return array

def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = []
        right = []
        for i in range(0, len(array) // 2):
            left.append(array[i])
        for i in range(len(array) // 2, len(array)):
            right.append(array[i])
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

array = ar_gen(10, 0, 50)

print(array)
print(merge_sort(array))

