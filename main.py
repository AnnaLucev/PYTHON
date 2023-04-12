# print('Hello world')
# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 1234
# print(value)              # Hello world
                            # 123
                            # 1.23
                            # 1234

"""
n = 'ab'
N = "ab"
g = 'ab\'ab'
G = 'ab"abcd"ab'
print (n,N, g,G)            # ab ab ab\'ab ab"abcd"ab
"""                         

# print(a,b,c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))     # 

# print("Введите первое число:  ")
# a = input()
# b = input("Введите второе число:  ")
# print(a, '+', b, '=', a+b)                # 3 + 4 = 34

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))                            # 5.89

# a = 5.89
# b = 6.12458
# print(a * b)
# print(round(a * b,3))                     # 36.0737762
                                            # 36.074   

# a = 1 > 4
# print(a)                                  # False

# a = 1 < 4 and 5 > 2
# print(a)                                  # True

# a = 1 != 2
# print(a)                                  # True

# a = 1 == 2
# print(a)                                  # False

# a = 'qwe'
# b = 'qwe'
# print(a == b)                             # True

# a = 1 < 3 < 5 < 10
# print(a)                                  # True


# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)                                # 9

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else :
#     print ('Пожалуй ')
#     print ('Хватит ')
# print (i)                                   # 3

# n = int(input())
# i = 2
# flag = True
# while flag:
#     if n % i == 0:
#         flag = False
#         print (i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1                                  # 25  --- 5

# for i in 1, 5, 14, -5:
#     print(i)                                  #

# r = range(5)                                    # 0 1 2 3 4
# r = range(2,5)                                  #  2 3 4
# r = range(-5,0)                                 # -----
# r = range(1,10,2)                               # 1 3 5 7 9
# r = range(100,0,-20)                            # 100 80 60 40 20

# r = range(100,0,-20)
# for i in r:
#     print(i)                                      # 100 80 60 40 20

# for i in 'qwerty':
#     print(i) 

# q
# w
# e
# r
# t
# y

# a = 'qwerty'
# print(a[2])                                 # e

# line = ''
# for i in range (5):
#     line = ''
#     for j in range(5):
#         line += '*'
#     print(line)
# *****
# *****
# *****
# *****
# *****

# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(len(text))                              # 39
# print('еще' in text)                          # True
# print(text.lower())                           # съешь еще этих мягких французских булок
# print(text.upper())                           # СЪЕШЬ ЕЩЕ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# # print(text.replace('еще', 'ЕЩЕ'))             # СъЕШЬ ЕЩЕ этих МяГкИх французских булок
# text = 'съешь еще этих мягких французских булок'
# print(text[0])                                # с
# print(text[1])                              # ъ
# print(text[len(text)-1])                    # к
# print(text[-5])                             # б
# print(text[ : ])                            # съешь еще этих мягких французских булок
# print(text[ :2])                            # съ
# print(text[len(text)-2:])                   # ок
# print(text[2:9])                            # ешь еще
# print(text[6:-18])                          # еще этих мягких
# print(text[0:len(text):6])                  # сеикакл
# print(text[::6])                           # сеикакл



