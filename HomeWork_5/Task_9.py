m = int(input('Введите натуральное число m\n'))
n = int(input('Введите натуральное число n\n'))



for i in range(m,n):
        for j in range(2, i+1):
            
                 if i % j == 0: print("Число ", i, "Делитель ", j)