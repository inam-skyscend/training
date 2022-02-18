def mul(w,x,y=0,z=0):
    if not y and not z:
        return w*x
    elif not z:
        return w+x+y
    elif not y:
        return w+x+z
    else:
        return (w+x)-(y+z)

#
# y=int(input("Enter value"))
# z=int(input("Enter value"))
# w=int(input("enter value:"))
# x=int(input("Enter value:"))
res1=mul(5,2,y=11)
print(res1)
