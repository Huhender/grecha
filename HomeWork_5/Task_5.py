import random
a = []
n = 19

for i in range(n):
    a.append(random.randint(1, 20))
print(a)

ls = []

for j in a:
    if j%2 == 0:
        ls.append(max(a))
    else: ls.append(j)


print(ls)
