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

#Если позиция максимального выше позиции минимального - поменять их местами
if maxpos < minpos:
    maxpos, minpos = minpos, maxpos

summ = 0

for i in range(minpos + 1, maxpos):
    summ += array[i]

print(summ)
