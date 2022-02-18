# 14.Create a script/program to open a file 'test_file.txt' to read the content line by line and print it.

f=open("test_file.txt","r")

res1=f.readline()
print(res1)
res2=f.readline()
print(res2)
res3=f.readline()
print(res3)
res4=f.readline()
print(res4)

f.close()
