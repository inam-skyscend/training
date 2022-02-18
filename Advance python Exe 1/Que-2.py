# 2. Create two different decorators. One will give the square of a number and the other one will increase the number by 10. Assign these two decorators to a
# function such that first the square of the no will be done and then 10 will be added and then the function operation will be done.
no=int(input("Enter number: "))

def dec_fun1(func):
    print("Decorator Function1")
    def inner_func():
        fn = func(no)
        return fn
    return inner_func

def dec_fun2(func):
    print("Decorator Function2")
    def inner_func():
        fn = func(s)
        return fn
    return inner_func



@dec_fun1
def sqr(no):
    return no**2

s=sqr()
print(s)


@dec_fun2
def inc(s):
    return s+10

i=inc()
print(i)
