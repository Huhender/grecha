# from functools import reduce

# ls = [2,8,3,4,0,9,2,8,3,7,4]

# summa = reduce((lambda x, y: x + y), ls)
# print(summa)

# a = [1,1,2,3,5,8,13,21,34,55,89]

# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# result = filter(lambda x: x in a and x in b, a)
# # for i in a:
# #     if i in b:
# #         result.append(i)
# # print(result)

# print(list(result))


# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}

# from collections import ChainMap
# from functools import reduce

# result = (lambda x, y, z: x**y**z, dict_a, dict_b, dict_c)
# print((result))


set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

print(set_1.difference(set_2))


