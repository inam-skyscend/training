# 8. Create a module which has 4 methods. Create another python file where this
# module’s methods will be used multiple times. Check the time utilized for these
# methods. Add different sleeping durations for all the methods. Display the
# profiling using the pstats library.

import module
import cProfile
a=15
b=20

import pstats
import time
# # # #
pr = cProfile.Profile()
# # # #
pr.enable()

a=module.add(a,b)
print(a)
time.sleep(1)

a=module.sub(a,b)
print(a)
time.sleep(2)

a=module.mul(a,b)
print(a)
time.sleep(3)

a=module.add(a,b)
print(a)
time.sleep(4)

pr.disable()

ps = pstats.Stats(pr)
ps.print_stats()