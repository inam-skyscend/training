# 12.Create a script/program to open a file to write a string. Write a string in a file 'test_file.txt'.

f=open("test_file.txt","w")
f.write("""hello everyone,
my name is inamhusain.
i am currently intern at Skyscend Business Solution Pvt.Ltd.""")
f.close()