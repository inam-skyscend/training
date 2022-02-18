#Multilevel inheritance
# class Base:
#
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#
# class Child(Base):
#
#     def __init__(self, name, age):
#         Base.__init__(self, name)
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#
# class GrandChild(Child):
#
#     def __init__(self, name, age, address):
#         Child.__init__(self, name, age)
#         self.address = address
#
#     def getAddress(self):
#         return self.address
#
#
# c = Child("Inam", 21)
# print(c.getName(), c.getAge())



#multiple inheritance

class Person:

    def __init__(self, name,age):
        self.name = name
        self.age=age

    def showName(self):
        print(self.name)

    def getAge(self):
        print(self.age)


class Student:
    def __init__(self,id):
        self.id = id

    def getId(self):
        print(self.id)


class Resident(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)


res=Resident("inam",21,2018095900008554)
res.showName()
res.getAge()
res.getId()




