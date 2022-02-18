import random
l1=random.sample(range(1,11),2)
a=l1[0]
b=l1[1]
print("value of a:",a,"value of b:",b)
def dec_fun(func):
    def inner():
        fn=func(a,b)
        return fn
    return inner



@dec_fun
def add(a,b):
    return a+b

@dec_fun
def sub(a,b):
    return a-b

@dec_fun
def mul(a,b):
    return a*b

@dec_fun
def div(a,b):
    return a/b


s=add()
print(s)

s=sub()
print(s)

s=mul()
print(s)

s=div()
print(s)
