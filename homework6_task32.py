# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Введите колличество элементов N: '))
min_number = int(input('Введите минимум диапазона: '))
max_number = int(input('Введите максимум диапазона: '))

my_list = []

for i in range(n):
    my_list.append(random.randrange(1, 100, 1))
print(my_list)

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i, end=' ')
