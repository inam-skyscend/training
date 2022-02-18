# 16.Create a script/program to write and read binary data in a file 'test_file.data'.

f=open("test_file.data","wb")
a = [1, 2, 3]
array=bytearray(a)
f.write(array)
f.close()


f2 = open("test_file.data", "rb")
res=f2.read()
print(list(res))

f.close()