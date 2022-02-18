# 37. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].

x=[1,2,3,4,5]
y=[4,5,6,7]

a=set(x)
b=set(y)
c=a.symmetric_difference(b)
print(list(c))

