# 8. Using the files 'test.py' and 'mod.py' call the individual method which is defined outside the class in 'mod.py' and call in it test.py. Make sure only that method from the file 'mod.py' is accessible in 'test.py'.

from mod import power

p=power(2,8)
print(p)