# Convert all the data structures to other data structures.


# list
# x=[1,2,3,4,5,6]
#
# # print(int(x))       #list is not convert to int
# # print(float(x))     #list is not convert to float
#
# print(tuple(x))       #list is convert to tuple
# print(str(x))         #list is convert to string ,its give answer like list
# print(set(x))         #list is convert to set
# print(bool(x))        #list is convert to boolean but in list have some data,empty list generate false
#
# # print(dict(x))      #here we can not convert to direct dictionary
#
# x=[("name","inam"),("age",22),("from","badarpur")]
# print(dict(x))
#


# Tuple
# y=(10,20,30,40,50)
# 
# #we can not directly convert tuple to int or float
# # print(int(y))
# # print(float(y))
# 
# #tuple directly convert  to list,string,boolean and set
# print(list(y))
# print(str(y))
# print(bool(y))
# print(set(y))
# 
# #for tuple convert to dictionary we have multiple tuple in tuple
# y=((10,20),(30,40),(50,60))
# print(dict(y))




#set
# z={"inam","husain","abid","siraj"}
# 
# #we can not convert set to int and float
# 
# # set convert to list,tuple,boolean and string.
# print(list(z))
# print(tuple(z))
# print(bool(z))
# print(str(z))
# 
# #for set to dictionary we have to tuple in set
# z={(10,20),(40,50)}
# print(dict(z))

# string
name="inamhusain"

#string is not convert to int and float
# print(int(name))
# print(float(name))


#we convert string to list,tuple,set and boolean
# print(list(name))
# print(tuple(name))
# print(set(name))
# print(bool(name))

# we can not convert string to dictionary

# dictionary
dic={"name":"inam","age":22,"from":"badarpur"}

print(list(dic.values()))
print(tuple(dic))
print(set(dic))
print(bool(dic))
print(str(dic))



