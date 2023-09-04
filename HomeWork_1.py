import math


# """Задание 1

# a = 8
# b = 7
# print(a+b)
# Задание завершено"""

# """Задание 2
# x = int(input('Введите число x'))
# y = int(input('Введите число y'))
# result = (abs(x)-abs(y))/(1+abs(x*y))
# print(result)
# Задание завершено"""


# Задание 3
# Cube = int(input('Введите длину куба\n'))
# V = int(Cube**3)
# print('Объем куба составляет' , V)
# Задание завершено

# Задание 4
# a = int(input("Введите первое действительное число\n"))
# b = int(input("Введите второе действительное число\n"))

# Sr_arifm = (a+b)/2
# Sr_geometr = math.sqrt((a+b)**2)
# print("Среднее арифметическое двух чисел равно " , Sr_arifm)
# print("Среднее геометрическое двух чисел равно " , Sr_geometr)
# Задание завершено

a = int(input("Длина первого катета \n"))
b = int(input("Длина второго катета \n"))
sum_kv = (a**2 + b**2)
gippo = math.sqrt(sum_kv)
print('Гипотенуза равна ' , gippo)
x = int(input("Основание треугольника \n"))
y = int(input("Высота треугольника \n"))
sum_osnv = x*y
height = sum_kv/2
print('Площадь треугольника равна ' , height)


