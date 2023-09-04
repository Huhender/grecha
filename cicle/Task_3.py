
a  = {'test':'test_value', 'europe':'eur', 'dollar':'usd','ruble':'rub'}
d = {}
# for i in a.copy():
#     d = i + str(len(i))
#     a[d] = a.pop(i)

# print('Измененный словарь через цикл For\n', a)
i = 0
l = a.copy()
p = ''
while i < len(a.keys()):

    i += 1
    p = len(l.keys())
    
    print(p)
    # a[d] = a.pop(p)
    
    # d = i + str(len(i))
    # a[d] = a.pop(i)

    


print('Измененный словарь через цикл While\n', a)
