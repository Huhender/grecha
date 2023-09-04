a = 1
z = 0

while a == 1:
    x = int(input('Введите операнд Х \n'))
    y = int(input('Введите операнд У \n'))
    string = input('Введите знак операции\n')
    if y != 0:
        if string == '+':
            z = x + y
            print(z)
        elif string == '-':
            z = x - y
            print(z)
        elif string == '*':
            z = x * y
            print(z)
        elif string == '/':
            z = x / y
            print(z)
    elif y == 0:
        print('На ноль делить нельзя')
        
    
    a = int(input("Введите число \n"))



