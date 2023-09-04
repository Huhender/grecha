# def Hi(name):
#     return name

# ls = ['Бэбэй', 'Вождь', 'Бабай', 'Бэбс', 'Лысая башка']

# for i in ls:
#     print(f'Hello, {Hi(i)}')



# def ar(*args):
    
#     return args
# print(sum(ar(1, 2, 3, 4, 5)))



def par(list):
    chislo = 0
    list2 = []
    for i in list:
        if -i not in list2:
                  list2.append(i)
            
        
            
    return list2


ls = [ 1, -1, 2, -2, 4, -4, 3]


print(par(ls))

