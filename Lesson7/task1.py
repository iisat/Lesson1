# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random

# Генерация массива размера SIZE с числами в диапазоне от MIN до MAX
def ar_gen(SIZE, MIN, MAX):
    array = []
    for _ in range(SIZE):
        array.append(random.randint(MIN, MAX))
    return array

# Функция сортировки массива
def bubble_sort(array):
    n = 0
    while n < len(array):
        subcount = 0
        if n % 2 == 0:
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    subcount += 1
        else:                       # Добавляем обратный проход для ускорения "всплытия" :)
             i = len(array) - 1
             while i > 0:
                 if array[i] < array[i - 1]:
                     array[i], array[i - 1] = array[i - 1], array[i]
                     subcount += 1
                 i -= 1
        if subcount == 0:           # Добавляем проверку на число перестановок за проход
            print(f'Cycles: {n}')   # Выводим число итоговое число проходов
            break
        n += 1

array = ar_gen(1000, -100, 100)
print(array)
bubble_sort(array)
print(array)
