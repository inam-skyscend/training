# 68. Sort a list of random 25 numbers between 1 to 100 without using the sort method.

import random
l1=random.sample(range(1,100),25)
print(l1)

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):

        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print(l1)

# print(set(l1))

