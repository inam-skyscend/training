class Parent:

    def add(self):
        return self.x+self.y

    def print_result(self):
        print(self.add())
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("constructor")
    def __del__(self):
        print("destructor")


p=Parent(10,5)
p.add()
p.print_result()





