# Задача №16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве А[1...N].
# Пользователь в первой строке вводит натуральное число N- количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число Х.
#  5
#  1 2 3 4 5
#  3        ------ 1

print("Задача 16: ")
import random
N = int(input("Введите число элементов в массиве  N - "))
list = []
for i in range(0, N):
    list.append(random.randint(1, 10)) 
print(list)

X = int(input("Введите число для поиска в массиве  Х - "))
count = 0
for i in range(len(list)):
    if list[i] == X:
        count +=1
print(f"Число встречается в массиве  {count} раз")

# Задача №18
# Требуется найти в массиве А[1...N] самый близкий по величине элемент к заданному числу Х.
# Пользователь в первой строке вводит натуральное число N - количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число Х.
#  5
#  1 2 3 4 5
#  6        ------ 5

print("Задача 18: ")
import random
N = int(input("Введите число элементов в массиве  N - "))
list = []
for i in range(0, N):
    list.append(random.randint(1, 30)) 
print(list)

X = int(input("Введите число для поиска  Х - "))
min = 1000000
number = 0
for i in range(len(list)):
    if abs(X - list[i]) < min:
        number = list[i]
        min = abs(X - list[i])
print(f"Самый близкий к числу {X} элемент массива - число {number}")


# Задача №20
# В настольной игре Скрабл каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так
# A, E, I, O, U, L, N, S, T, R  ---  1 очко.
# D, G  ---  2 очка.
# B, C, M, P  ---  3 очка.
# F, H, V, W, Y  ---  4 очка.
# K  ---  5 очков.
# J, X  ---  8 очков.
# Q, Z  ---  10 очков.
# А русские буквы оцениваются так
# A, В, Е, И, Н, О, Р, С, Т  ---  1 очко.
# Д, К, Л, М, П, У  ---  2 очка.
# Б, Г, Ё, Ь, Я  ---  3 очка.
# Й, Ы  ---  4 очка.
# Ж, З, Х, Ц, Ч  ---  5 очков.
# Ш, Э, Ю  ---  8 очков.
# Ф, Щ, Ъ  ---  10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#  ввод - ноутбук   ------  вывод  12

print("Задача 20: ")
N = str(input("Введите слово (Input word) - "))
list = list(N.upper())
print(list)
dict =  { 1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'A', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
          2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
          3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
          4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
          5: ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
          8: ['J, X', 'Ш, Э, Ю'],
          10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ'],   }

summa = 0
t = {}
for key, vals in dict.items():
    for val in vals:
        t[val] = key
res = [t[ele] for ele in list]
print(f"Очки по буквам: {res}")

for j in range(len(res)):
    summa += res[j]
print(f"Cлово  '{N}' составляет   {summa}  очков")