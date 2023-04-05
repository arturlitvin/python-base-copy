# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел
# a0 , a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def f(n):
#     if n < 2:
#         return n
#     else:
#         return f(n-1)+f(n-2)

# n = int(input('Введите число: '))
# print(f(n))

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# arr = [1, 3, 3, 3, 4]
# print(arr)
#

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


n = int(input('Введите число для проверки на простоту: '))
x = 0
for i in range(2, n):
    if n % i == 0:
        x += 1
print(x == 0)


def prime_num(n):
    n = abs(n)
    if n < 2:
        return 'не простое'
    for i in range(2, n):
        if n % i == 0:
            return 'Не Простое'
    return 'Простое'


print(prime_num(int(input('Введите число для проверки на простоту: '))))


# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# a = input('Введите число: ')
# print(a[::-1])
# print(type(a))

# def rev(n):
#     if n == 0:
#         return ' '
#     k = int(input('Введите элемент: '))
#     return rev(n-1) + f'{", " if n > 1 else ""} {k}'



# print(rev(int(input('Введите число: '))))


