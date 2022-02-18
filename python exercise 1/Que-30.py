# constructor overloading
class Sample:
    def __init__(self,*args):
        sum = 0
        for elem in args:
            sum += elem
        print(sum)
    # def demo(self):
    #     print("display demo method")

s=Sample(1,10,5,2,2,2,5)
s=Sample(50,88,66,4,5,5,5,8,1,5,5,5,5,5,5,5,5,5,5,5,5,8,8,8,54)
# s.demo()



#method overloading
class example:

    def area(self,x=None,y=None):
        if x != None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0

e=example()

print(e.area(10,20))
print(e.area(10))
print(e.area())

