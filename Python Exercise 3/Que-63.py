# 63. Generate 15 random numbers from 1 to 100 and get the total of all these numbers.

import random
l1=random.sample(range(1,100),15)
print(l1)

print("total:",sum(l1))