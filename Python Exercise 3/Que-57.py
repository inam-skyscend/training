# 57. Generate a list of having 10 elements using random but the numbers shoudl be either 1 or 0. Check if all the elements are 1 print “ALL” and if any of the single element is 1 print “ANY” and if all the elements are 0 print “NONE”.

import random
l1=[random.randrange(0,2) for i in range(10)]
print(l1)
if all(l1):
    print("ALL")
elif any(l1):
    print("ANY")
else:
    print("NONE")