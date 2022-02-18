# 32.Get me a random combination of 4 different numbers between 1 to 100.

import random
res=list(range(1,101))
print(random.sample(res,4))