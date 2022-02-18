x={'a':1,'b':2,'c':3}
y={'a':4,'d':5,'e':6}


# x.update(y)       #first method
# print(x)
z=x.copy()
z.update(y)
print(z)