# Это просто материал урока, не дз
import random

# Генерация массива размера SIZE с числами в диапазоне от MIN до MAX
def ar_gen(SIZE, MIN, MAX):
    array = []
    for _ in range(SIZE):
        array.append(random.randint(MIN, MAX))
    return array

def sel_sort(array):
    for i in range(len(array)):
        min_pos = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_pos]:
                min_pos = j

        array[i], array[min_pos] = array[min_pos], array[i]

def ins_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam

def quick_sort(array, fst, lst):
    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort(array, fst, j)
    quick_sort(array, i, lst)

def quick_sort_2(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    small = []
    medium = []
    large = []

    for item in array:
        if item < pivot:
            small.append(item)
        elif item > pivot:
            large.append(item)
        else:
            medium.append(item)

    return quick_sort_2(small) + medium + quick_sort_2(large)

array = ar_gen(10, 0, 10)
new = quick_sort_2(array)
print(new)