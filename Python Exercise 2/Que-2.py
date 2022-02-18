# Get a list of 1 to 20 then remove elements from list to get only even elements.

x=list(range(1,20))
for i in x:
    if i%2!=0:
        x.remove(i)
print(x)