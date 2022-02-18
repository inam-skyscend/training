# 13.Create a script/program to open a file 'test_file.txt' to read a string. Read the whole string content from the file and print it.

f=open("test_file.txt","r")
res=f.read()
print(res)
f.close()