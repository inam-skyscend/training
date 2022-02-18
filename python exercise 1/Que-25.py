class Sample:
    x=''
    y=''

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        a = self.x + self.y
        return self.display(a)

    def display(self,a):
        print(a)


c = Sample(10,8)
c.add()



