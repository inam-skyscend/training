# 45. Using range get me a list of even numbers between 1 to 100. Code needs to be done in one line only.

# l1=list(range(1,100))
# l2=[]
# for i in l1:
#     if i%2==0:
#         l2.append(i)
#
# print(l2)

l2=[i for i in list(range(1,100)) if i%2==0]
print(l2)
