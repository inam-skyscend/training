# Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list.


x=list(range(1,9))
print(x)
y=list(range(4,11))
print(y)
a=set(x)
b=set(y)
z=a.intersection(b)
print(list(z))
