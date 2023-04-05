# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = input('Введите символы через пробел: ').split()
# print(text)
# result = {}
# for char in text:
#     if char in result:
#         print (f'{char}_{result[char]}', end=" ")
#     else:
#         print(char, end=" ")
#     result[char] = result.get(char, 0) + 1

# result = {}
# result['a'] = (result.get("a", 0))
# result['b'] = (result.get("b", 1))
# print(result)


# a = input("Enter the string paragraph:")
# count = 0
# symbol_list = [' ', '.', ',', ';']
# for i in a:
#   if  i in symbol_list:
#        count = count + 1
# print("Number of symbols in a string:",count)

# lst =  "Geeks,For. geeks"
# print(lst.split(sep=(',') or (' ') or ('.') or (';')))


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# user_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells" # input("Введите строку")
# user_str = user_str.upper()
# new_str = set(user_str.split())
# print(new_str)
# print(len(new_str))


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# n = int(input('Введите число: '))
# max_number = 0
# while n > 0:
#     n = int(input('Введите число: '))
#     if max_number < n:
#         max_number = n
# print(max_number)

# n = int(input())
# max_number = n
# while n > 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12


# list_1 = set(map(int, input("введите числа через пробел: ").split(" ")))
# print(list_1)

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов первого множества: '))
set_n = []
set_m = []
for i in range(n):
    x = int(input('Введите сторону монеты (0-Орел, 1 - Решка): '))
    set_n.append(x)
for i in range(m):
    x = int(input('Введите сторону монеты (0-Орел, 1 - Решка): '))
    set_m.append(x)
    
intersection = list(set(set_n) & set(set_m))
print(sorted(intersection))
