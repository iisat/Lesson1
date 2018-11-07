import random

SIZE = 10
array = []
for _ in range(SIZE):
    array.append(random.randint(0, SIZE * SIZE))

print(array)

maxpos = minpos = 0
for i in range(SIZE):
    if array[i] > array[maxpos]:
        maxpos = i
    if array[i] < array[minpos]:
        minpos = i

array[maxpos], array[minpos] = array[minpos], array[maxpos]

print(array)