import random
A = []
n = 20

for i in range(n):
    A.append(random.randint(1, 20))
print(A)

x = int(input('Введите целое число х\n'))

B = []

for j in range(len(A)):
    if A[j] == x:
        B.append(j)
print('Массив имеет значения x', B)
        
if not B:
    print('В массиве отсутствуют значения x' , B)
 