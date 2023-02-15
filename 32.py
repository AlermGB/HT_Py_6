# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def fill_array_rnd() -> list:
    quantity = int(input('Введите количество элементов: '))
    max_value = int(input('Введите максимально допустимое значение: '))
    min_value = int(input('Введите минимально допустимое значение: '))
    result_array = []
    for i in range(quantity):
        result_array.append(random.randint(min_value,max_value))
    return result_array

import random

# array = [1, 35, 32, -90, 7, 22, 2, 6, 17, -3]
array = fill_array_rnd()
print(array)
index_array = []
max_lim = int(input('Введите максимальное значение проверяемого диапазона: '))
min_lim = int(input('Введите минимальное значение проверяемого диапазона: '))
for i in range(len(array)):
    if array[i] in range(min_lim, max_lim + 1):
        index_array.append(i)
print('Индексы, удовлетворяющие запросу: ')
print(index_array)