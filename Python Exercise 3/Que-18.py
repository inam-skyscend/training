# 18.Create another script/program and read the dumped variables in the file 'my_variables.data'.

import pickle

f=open("my_variable.data","rb")

var1=pickle.load(f)
print(var1)
var2=pickle.load(f)
print(var2)
var3=pickle.load(f)
print(var3)
var4=pickle.load(f)
print(var4)
# var5=pickle.load(f)
# print(var5)

f.close()
