# 31. Iterate through all the data structures.

#list
# x=["inam",1,56,"husain"]
# for i in x:
#     print(i)

        #or

# length=len(x)
# for i in range(length):
#     print(x[i])

    #or

# x=["inam",1,56,"husain"]
# length=len(x)
# s=0
# while s<length:
#     print(x[s])
#     s+=1


# Tuple
# y=(10,20,"i am","is",588.2)
# for i in y:
#     print(i)

#set
# z={10,"not",(10,20,30),58.56,2+5j}
# for i in z:
#     print(i)
#

# dictionary
d={"brand":"Ford","model":"Mustang","year":2018}

for key,value in d.items():
    print(key,value)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

