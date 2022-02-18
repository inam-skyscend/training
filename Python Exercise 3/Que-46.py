# 46. Generate a list of exponents of first 25 integers. Code needs to be in one line only.

# l1=[]
# for i in list(range(1,26)):
#     l1.append(i**2)
# print(l1)

l2=[i**2 for i in list(range(1,26))]
print(l2)