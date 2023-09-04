a = int(input('Введите натуральное число\n'))

i = 1
S = 1
while i <= a:
    if i >= 2:
        S += (1/i)
    i += 1
print(S)