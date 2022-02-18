# def myfun(a,b,c=0,d=0,e=0):
#     if a and b and not c:
#         return a*b
#     elif not d and not e:
#         return a,b,c
#     elif not e:
#         return a+b+c+d
#     else:
#         return (a*b)+(c*d*e)
#
#
# res=myfun(5,8,10,5,6)
# print(res)


def myfun(a,b,c=0,d=0,e=0):
    if a and b and c and d and e:
        return (a*b)+(c*d*e)
    elif a and b and c and d:
        return a+b+c+d
    elif a and b and c:
        return a,b,c
    elif a and b:
        return a*b

res=myfun(5,4,5)
print(res)

