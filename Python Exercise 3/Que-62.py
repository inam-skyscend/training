# 62. Using map generate a list from two lists by multiplying the elements in the two lists on the identical indexes in both the lists.

x = [1, 3, 4, 6, 8]
y = [4, 5, 6, 2, 10]
res_list =list(map(lambda a,b:a*b,x,y))
print(res_list)
