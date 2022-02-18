import random
l=random.sample(range(1,100),10)
print(l)


even=list(filter(lambda x:x%2==0,l))
print("even number list:",even)

odd=list(filter(lambda x:x%2!=0,l))
print("odd number list:",odd)