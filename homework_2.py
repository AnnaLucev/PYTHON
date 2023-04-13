# Задача №10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые - гербом.
# Определите минимальное число монеток, которое нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которое нужно перевернуть
#  5 ------ 1 0 1 1 0      -------- 2

print("Задача 10: ")
n = int(input("Введите общее число монеток  n  - "))
ocount = 0
rcount = 0
for i in range(n):
    x = int(input())
    if x == 0:
        ocount += 1
    else:
        rcount += 1
if ocount < rcount:
    print(f"Минимальное количество монет, которое надо перевернуть, - {ocount}")
else:
    print(f"Минимальное количество монет, которое надо перевернуть, - {rcount}")

# Задача №12
# Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X, Y <=1000), а Катя должна.
# их отгадать. Для этого Петя делает 2 подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа. 
# 4 4  ------ 2 2              5 6 ---------- 2 3

print("Задача 12: ")
X = int(input("Введите задуманное натуральное число  X (<=1000)  - "))
Y = int(input("Введите задуманное натуральное число  Y (<=1000)  - "))
s = X + Y
p = X * Y
if s**2 - 4 <0:
    print("Задача не имеет решения")
else:
    Y1 = (s + (s**2 - 4*p)**0.5)/2
    X1 = s - Y1
print(f"Задуманные числа - {X1} и {Y1}")

print("Задача 12: ")
s = int(input("Введите сумму задуманных чисел s  - "))
p = int(input("Введите произведение задуманных чисел p  - "))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(f"Задуманные числа - {i} и {j}")


# Задача №14
# Требуется вывести все целые степени двойки (т.е. числа виде 2**k), не превосходящие числа N
#  10  ------ 1 2 4 8

print("Задача 14: ")
N = int(input("Введите число  N  - "))
i = 0
while 2**i < N+1:
    print(2**i)
    i += 1