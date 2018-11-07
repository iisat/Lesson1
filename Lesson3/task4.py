import random

# Определяем параметры генерируемого массива SIZE - число элементов, RANGEMAX - максимальное значение каждого элемента
SIZE = 10
RANGEMAX = 10

#Определяем массив и заполняем случайными числами
array = []
for _ in range(SIZE):
    array.append(random.randint(0, RANGEMAX))

# Определяем массив счетчиков
countarray = [0] * (RANGEMAX + 1)

# Считаем число вхождений каждого элемента исходного массива
for i in range(SIZE):
    num = array[i]
    countarray[num] +=1

# Ищем максимальное значение в массиве счетчиков
maxpos = 0
for i in range(RANGEMAX):
    if countarray[i] > maxpos:
        maxpos = i

# Выводим реузльтаты
print(array)
print(maxpos)


