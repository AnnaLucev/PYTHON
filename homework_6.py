
# Задача №30
# Заполните массив элементами арифметической прогрессии. Ее первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для 
# получения n-го члена прогрессии: an = a1 + (n-1)*d.
# Каждое число вводится с новой строки
#  7 2 5  --------- 7 9 11 13 15

print("Задача доп 30: арифметическая прогрессия")

def arithm_progress(a1, difference, len_list):    # функция арифметической прогрессии
    a = []
    for i in range(1,len_list+1):
        a.append(a1 + (i-1)*difference)
    return a

a1 = int(input("Введите первый элемент массива - "))
d= int(input("Введите разность элементов массива - "))
n = int(input("Введите количество элементов массива - "))
print(arithm_progress(a1, d, n))

# Задача №32
# Определите индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданнного минимума и не больше заданного максимума
#  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]  --------- [1, 9, 13, 14, 19]

print("Задача доп 32: индексы списка не меньше мин и не больше макс")

def index_range(array, minim, maks):     # функция вывода индексов массива значения элементов которого больше заданного мин и меньше заданного макс
    index_list = []
    for i in range(len(array)):
        if array[i] > minim and array[i] < maks:
            index_list.append(i)
    return index_list

list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minim = int(input("Введите минимум диапазона - "))
maks = int(input("Введите максимум диапазона - "))
print(index_range(list1, minim, maks))


# Задача дополнительная 2
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы 
# отыскать все зараженные холодильники. Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно 
# рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы.
#  Формат входных данных: в первой строке подаётся число  n,  n – количество холодильников. В последующих nn строках 
# вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100 100 символов.
#  Формат выходных данных: программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет,ничего выводить не нужно.
# Sample Input 1: 6    array1 = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
#  Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9    array2 = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

print("Задача доп 1: поиск антона в холодильниках")

def anton(array):
    word_search = 'anton'
    word_search_ = list(word_search)
    res_word = []   
    error_cold = []
    for j in range(len(array)):
        for i in word_search_:
            if i in array[j]:
                res_word.append(i)
                array[j] = array[j].replace(i, '', 1) 
        print(res_word)
        res_word_ = str(''.join(res_word))
        if res_word_ == word_search:
            error_cold.append(j+1)
        res_word = []
    return error_cold

# len_n = int(input("Введите количество холодильников - "))
# array = [input(f'Введите {i} элемент множества:  ') for i in range(len_n)]
# print(array)
array1 = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']
array2 = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']

print(f'Номера холодильников с ошибкой - {anton(array1)}')
print(f'Номера холодильников с ошибкой - {anton(array2)}')

# Задача №45
# Два различных натуральных числа n и m называются дружественными, если сумму делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 - дружественные числа.  По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число к, не превосходящее 10**5.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит к
# Пары необходимо выводит по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает)
#  300  --------- 220 284

print("Задача №45: дружественные числа")

def sum_del(n):      # функция вывода суммы делителей числа
    sum =0
    for i in range(1,n):
        if n%i==0:
            sum +=i
    return sum

def friends(n):   # функция вывода список дружественных чисел до числа n
    res=[]
    for i in range(1,n):
        if i not in res:
            tmp = sum_del(i)
            if i == sum_del(tmp) and i != tmp:
                res.append(i)
                res.append(tmp)
    return res

k = int(input("Введите исходное число 0 < k < 10**5  - "))
print(*friends(k))
