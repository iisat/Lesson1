import random

# Определяем параметры генерируемого массива SIZE - число элементов, RANGEMAX - максимальное значение каждого элемента RANGEMIN - минимальное значение каждого элемента
SIZE = 10
RANGEMIN = -10
RANGEMAX = 10

#Определяем массив и заполняем случайными числами
array = []
for _ in range(SIZE):
    array.append(random.randint(RANGEMIN, RANGEMAX))

#Выводим исходный массив
print(array)
minmax = RANGEMIN
minpos = 0

#Находим позицию максимального орицательного числа
for i in range(SIZE):
    if array[i] < 0:
        if array[i] > minmax:
            minpos = i
            minmax = array[i]

#Выводим максимальное отрицательное число и его позицию (с корректировкой)
print(array[minpos], minpos + 1)