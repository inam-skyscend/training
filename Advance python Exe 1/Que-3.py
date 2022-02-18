# 3. Create a decorator with 2 parameters. Assign these decorator to a function which
# also has 2 parameters. Multiply the parameters passed in the decorator and pass it
# to the function which is decorated by this decorator as an argument when calling
# the function from decorator.

# def dec_mkr(p, q):
#     print("MKR",p,q)
#     def dec_func(func):
#         print("DEC",func)
#         def inner_func(p, q):
#             print("INR",p,q)
#             return func()
#         return inner_func
#     return dec_func
#
#
# @dec_mkr(10,15)
# def mul(x,y):
#     return x*y
#
# m=mul()
# print(m)


def dec_mkr(p, q):
    print("MKR",p,q)
    def dec_func(func):
        print("DEC",func)
        def inner_func_with_args(b):
            a=p*q
            return func(a, b)
        return inner_func_with_args
    return dec_func


@dec_mkr(10, 15)
def add(i, j):
    return i * j


rs = add(4)
print(rs)
