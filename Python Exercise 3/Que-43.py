# 43. Read a file 'python.txt' which is containing python code and execute the python code which is read from the file.
f1=open("python.txt","r")
x=f1.read()
exec(x)