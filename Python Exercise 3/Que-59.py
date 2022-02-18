# 59. Get 10 random numbers in a list and get the minimum number from the list.

import random
l1=[random.randrange(100) for i in range(10)]
print(l1)
print("minimum number of list",min(l1))

