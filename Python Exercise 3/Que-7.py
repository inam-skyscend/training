# 7. Using the above mentioned files 'test.py' and 'mod.py'. In 'test.py' create an object of the class defined in the 'mod.py'. Call the methods using the object. Make sure only that class is accessible and not the individual method to execute.

from mod import Student
s=Student(20,56)
print("x:",s.x,"y:",s.y)
print(s.z)
print(s.add())
print(s.sub())
