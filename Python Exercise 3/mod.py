# Que-6
class Student:
    z="i am member variable of class"
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        def summ():
            return self.x*self.y
        return self.x+self.y,summ()

    def sub(self):
        return self.x-self.y

def power(no,p=0):
    return no**p










