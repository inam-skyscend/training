# 64. Get a list of 10 random characters and then merge all the characters in a single string.

import random
res=random.sample([chr(ele) for ele in range(ord("a"),ord("z")+1)], 10)
print(res)

print("\nafter merge all character:",''.join(res))
