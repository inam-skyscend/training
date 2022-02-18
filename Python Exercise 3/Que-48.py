# 48. Create a generator method which gives random numbers between 1 to 100 and the number not being repeated. Make sure it generates only 10 numbers.
import random
#
# def generator():
#     l2 = []
#     for i in range(10):
#         l2.append(random.randrange(1,30))
#
#     print(l2)
# generator()

print(random.sample(range(1,100),10))



