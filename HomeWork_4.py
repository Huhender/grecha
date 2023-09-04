import math
import random


# Задание 1
# a = []
# n = 10
# mass = []
# for i in range(n):
#     a.append(random.randint(1, 25))
# print('Обычный массив ', a)    
# for i in a:
#     i *= -2
#     mass.append(i)
# print('Умноженный на -2 массив', mass)
# Конец задания


a = []
n = 10

for i in range(n):
    a.append(random.randint(1, 25))

chet = 0



for i in a:

    if i % 2 == 0: chet += 1

print(a)
print(chet)