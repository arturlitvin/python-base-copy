# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12
alphabet = {1: "AEIOULNSTRАВЕИНОРСТ",
            2: "DGДКЛМПУ",
            3: "BCMPБГЁЬЯ",
            4: "FHVWYЙЫ",
            5: "KЖЗХЦЧ",
            8: "JXШЭЮ",
            10: "QZФЩЪ"
            }
word = input('Введите слово: ').upper()
points = 0
for letter in word:
    for key, value in alphabet.items():
        if letter in value:
            points += key
print("Кол-во ваших очков: ", points)
exit()

list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T',
          'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
list_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

user_str = input("Введите слово: ")
user_str = user_str.upper()

user_list = list(user_str)

# print(user_list)

points = 0

for i in user_list:
    if i in list_1:
        points = points + 1
    elif i in list_2:
        points = points + 2
    elif i in list_3:
        points = points + 3
    elif i in list_4:
        points = points + 4
    elif i in list_5:
        points = points + 5
    elif i in list_8:
        points = points + 8
    elif i in list_10:
        points = points + 10

print("Кол-во ваших очков: ", points)
