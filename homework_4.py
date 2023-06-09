# Дополнительная задача
# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: 
# +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это 
# коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, 
# что и во входной строке) с соответствующими кодами. Полученный словарь вывести 
# командой:
# print(*sorted(d.items()))
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

print("Дополнительная задача семинара 4: ")
numbers = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890".split()
d = dict()
for i in numbers:
    if i[:2] in d:
        d[i[:2]].append(i[2:])
    else:
        d[i[:2]] = [i[2:]]
print(*sorted(d.items()))
print(d)


# Задача №22
# Даны два неупорядоченных набора целых чисел (может быть с повторениями)
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах
# Пользователь вводит 2 числа, n - кол-во элементов первого множества,
# m - кол-во элементов второго множества. Затем пользователь вводит сами
# элементы множеств
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18  ---------   6 12
#
print("Задача №22: ")
import random
N = int(input("Введите кол-во элементов в 1м множестве n - "))
M = int(input("Введите кол-во элементов во 2м множестве m - "))
listN = []
listM = []
for i in range(0, N):
    listN.append(random.randint(1, 30)) 
for i in range(0, M):
    listM.append(random.randint(1, 30)) 
resJoin = listN + listM
print(f"Первое множество -  {listN}")
print(f"Второе множество -  {listM}")
resJoin = list(set(sorted(resJoin)))
print(f"Результат объединения и сортировки -  {resJoin}")


# Задача №24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого
# куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод - на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального количества ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки 
# 4 ----------- 1 2 3 4      ---- 9
#

print("Задача №24: ")
n = int(input("Введите номер куста  n - "))
print("Введите кол-во ягод на кустах через пробел")
berries = [ int(x) for x in input( '-> ' ).split() ]
# n = len(berries)
berries = berries + berries[:2]
maxBerry = 0
for i in range(n):
    maxBerry = max(maxBerry, berries[i] + berries[i+1] + berries[i+2] )
print(maxBerry)
