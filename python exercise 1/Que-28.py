class Parent():
    
    def add(self):
        print("Parent add method")
    
    def sub(self,x,y):
        print(x-y)
    
    
class Child(Parent):

    def add(self):
        print("child add method")


p = Parent()
c = Child()

p.add()
p.sub(20,5)
c.add()


    