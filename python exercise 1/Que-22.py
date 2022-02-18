def calc(n):
    if n==1:
        def add(x,y,z):
            return x+y+z

    elif n==2:
        def sub(x,y,z):
            return x-y-z

    elif n==3:
        def mul(x,y,z):
            return x*y*z

    elif n==4:
        def div(x,y):
            return x/y

    elif n==5:
        def exp(x,y):
            return x**y

    elif n==6:
        def flr(x,y):
            return x//y
    else:
        return "Invalid Argument"

    if n<=3 and n>0:
        x,y,z=map(int,input("Enter the value:").split())
        if n==1:
            return add(x,y,z)
        elif n==2:
            return sub(x,y,z)
        elif n==3:
            return mul(x,y,z)

    elif n>3 and n<=6:
        x,y=map(int,input("enter the value:").split())
        if n==4:
            return div(x,y)
        elif n==5:
            return exp(x,y)
        elif n==6:
            return flr(x,y)

    
n=int(input("Enter the choice:"))
print(calc(n))



