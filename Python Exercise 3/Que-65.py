# 65. Create a class with few methods and in one of the method get all the global
# attributes that can be used in that method and also the local attributes that can be
# used in that method.

class A():
    z=15
    def add(self,x,y):

        print(globals())
        print(locals())
        return x + y
    def display(self):
        print("its display method")

a=A()
a.add(10,5)
a.display()
