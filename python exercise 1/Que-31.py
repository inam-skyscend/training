class my_parent_class:
    x=19
    y=20

    def __init__(self,a=0,b=0):
        if not a and not b:
            a=self.x
            b=self.y

        else:
            self.x=a
            self.y=b


    def add(self,a=0,b=0):
        res1=self.x+self.y
        return res1
    def sub(self, a=0, b=0):
        res2=self.x-self.y
        return res2

    def print_result(self):
        print("Addition is:",self.add())
        print("subtraction is:",self.sub())



class my_child_class(my_parent_class):
    z=20

    def __init__(self,a=0):
        super().__init__()
        if not a:
            a=self.z
        else:
            self.z=a

    def add(self,z=0):
        return my_parent_class.add(self)+self.z

    def sub(self,z=0):
        return self.x * self.y * self.z

    def print_result(self):
        print("child addition:",self.add())
        print("child sub method called",self.sub())



# create parents objects
parent_object_1=my_parent_class()
parent_object_2=my_parent_class(5)
parent_object_3=my_parent_class(10,15)

#call the print_result function
parent_object_1.print_result()
parent_object_2.print_result()
parent_object_3.print_result()

#create child object
child_object1=my_child_class()
child_object2=my_child_class(25)

# called child method print_result
child_object1.print_result()
child_object2.print_result()

