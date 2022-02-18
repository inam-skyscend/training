# Create a function and a nested function inside this function. Assign variables
# outsie both the functions, define two variables inside the first function. Make on of
# the variables to be global. Define other two variable inside the nested function and
# make one of them global. Now call the locals() and globals() function from
# outside both the functions, inside first function and inside the nested function and
# check what is available as local and global variables which can be accessed.

x=10
y=20

def myfun():
    global a
    a=15.5
    b="inam"

    print("global at inside fun",globals())
    print("local at inside fun",locals())

    def nested():
        n1=85.5
        global n2
        n2="i"
        print("locat at nested",locals())
        print("global at nested",globals())

    nested()
myfun()
print("local of outside:",locals())
print("global of outside:",globals())


