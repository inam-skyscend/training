# 33. Use the in, not in, is and is not operators with data structures.


# in

# # list
# x=[1,2,3,4,5,6]
# y=3
# if y in x:
#     print("y is present")
#
# # Tuple
# x=(10,20,30,40,50)
# if 20 in x:
#     print("20 is present")
#
# #set
# x={25,26,47,85,99,"abc"}
# if "abc" in x:
#     print("true")
#
# # dictionary
# d={"name":"inam","age":22,"from":"badarpur"}
# y="inam"
# if y in d.values():
#     print("yes,its present")





# # not in
#
# # list
# x=[1,2,3,4,5,6]
# y="inam"
# if y not in x:
#     print("y is  not present")
#
# # Tuple
# x=(10,20,30,40,50)
# if 89 not in x:
#     print("Its True")
#
# #set
# x={25,26,47,85,99,"abc"}
# if "abc" not in x:
#     print("TRUE")
# else:
#     print("FALSE")
#
# # dictionary
# d={"name":"inam","age":22,"from":"badarpur"}
# y=8956212
# if y not in d.values():
#     print("True")





# is

# # list
# x=[1,2,3,4,5,6]
# y=x
# if x is y:
#     print("y is x")
#
# if x is not y:
#     print("yes")
#
#
# Tuple
# x=(10,20,30,40,50)
# y=(10,20,30,40,50)
# if y is x:
#     print("y is x")
#
# #set
# x={25,26,47,85,99,"abc"}
# y={25,26,47,85,99,"abc"}            #here answer is false bcoz both variable store different memory
# if x is y:
#     print("true")
# else:
#     print("false")
#
# # dictionary
# d={"name":"inam","age":22,"from":"badarpur"}
# d={"name":"inam","age":22,"from":"badarpur"}
#
# if d is d :
#     print("yes,its true")




# is not

# list
# x=[1,2,3,4,5,6]
# y=[10,20,30]
# if x is not y:
#     print("x is not y")
#
#
# # Tuple
# x=(10,20,30,40,50)
# y=(10,20,30)
# if y is not x:
#     print("----")
#
# #set
# x={25,26,47,85,99,"abc"}
# y={25,26,47,85,99,"abc"}
# if x is y:
#     print("true")
# else:
#     print("false")
#
# # dictionary
# d={"name":"inam","age":22,"from":"badarpur"}
# w={"name":"abid","age":48,"from":"badarpur"}
#
# if d is not w :
#     print("yes,its true")

