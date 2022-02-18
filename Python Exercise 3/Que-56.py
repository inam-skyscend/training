# 56. Create a class with member variables. Now perform the following.
# 1. Check whether an attribute exists in the class or not.
# 2. Fetch the value of an attribute of a class.
# 3. Update the value of an attribute of a class.
# 4. Delete the attribute of a class.


class Student:
    x=10
    z=512

    def add(self):
        print(self.x+self.z)

s=Student()

# 1. Check whether an attribute exists in the class or not.
res1=hasattr(Student,"x")
print(res1)
res2=hasattr(s,"z")
print(res2)

# 2. Fetch the value of an attribute of a class.
res1=getattr(Student,"x")
print(res1)
res2=getattr(s,"z")
print(res2)


# 3. Update the value of an attribute of a class.
setattr(Student,'x', 15)
setattr(s,'y', 20)

print(s.x)
print(s.y)

# 4. Delete the attribute of a class.

delattr(Student, 'x')       #here x is delete from class
delattr(s, 'y')

print(s.x)      #student class has no attribute "x"