import random

SIZE = 10
array = []
for _ in range(SIZE):
    array.append(random.randint(0, SIZE * SIZE))

arrayb = []
for i in range(SIZE):
    if array[i] % 2 == 0:
        arrayb.append(i)

print(array)
print(arrayb)