# Create a function for string that will check whether a string is having the first letter as Capital and not anyother letter is capital.

# def myfun(string):
#     for i in string.split():
#         for j in i:
#             k=0
#             if j[k].isupper():
#                 print("Yes ,First letter is Capital")
#                 
# 
# string=input("Enter the string:")
# myfun(string)

def myfun(string):
    if string.istitle():
        print("yes first latter is capital")
    else:
        print("first latter is not capital")
        for i in string:
            k = 0
            if i[k].isupper():
                print(i[k], ",This letter is capital in string")
            k += 1

string=input("Enter string:")
myfun(string)