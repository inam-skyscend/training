# x=(1,2,3,4,5), y=(4,5,6,7). Combine these two tuples in a single tuple ignoring the common elements.

x=(1,2,3,4,5)
y=(4,5,6,7)
z=x+y

print(tuple(set(z)))

a=set(x)
b=set(y)
c=a.symmetric_difference(b)
print(tuple(c))