# 15.Create a script/program to open a file 'test_file.txt' to append a string at the end of the existing string in a file.
f=open("test_file.txt","a")
string="""line 4
line 5
line 6
line 7
"""
f.write(string)
f.close()