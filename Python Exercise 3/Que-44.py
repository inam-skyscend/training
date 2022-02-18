# 44. Using range get me a list of 1 to 10 and from this list generate a list as [13,15,17,19,21,23,25,27,29,31]. Code needs to be done in one line only.
l1=list(range(1,11))
print(l1)
# l2=[]
# for i in range(0,len(l1),1):
#     l2.append(l1[i]*2+11)
#
# print(l2)


print([l1[i]*2+11 for i in range(0,len(l1))])