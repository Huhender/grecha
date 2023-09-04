import random

a = []
n = 10

for i in range(n):
    a.append(random.randint(1, 20))

print(a)

l = []
for j in a[1:]:
    l.append(j)
l.append(a[0])
    
print(l)

    
        
    
    
    


print(l)