# 67. Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.

x=['a','b','c','d','e']
y=[1,2,3,4,5]

res=dict(zip(x,y))
print(res)

