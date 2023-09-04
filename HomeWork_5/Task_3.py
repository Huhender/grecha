x = 200
y = 300

lst = []
dict = {}

for index in range(x, y):
    sum = 0
    for i in range (1, index):
        if index % i == 0:
            sum += i
        dict[index] = sum
print(dict.items())


