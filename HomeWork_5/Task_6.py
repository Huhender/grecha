import random
a = []
n = 19

for i in range(n):
    a.append(random.randint(1, 20))
print(a)


kol = 0
list1 = []
list2 = []
for j in range(len(a)):
          
    if a[j] != a[18]:  
        if a[j] < a[j+1] and a[j+1] < a[j+2]:
        
            kol += 1
print(kol) 








