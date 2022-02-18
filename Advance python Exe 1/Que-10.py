# 10. Create a Thread that will print random numbers between the given number at the
# time of Thread Creation. Create 3 objects with different numbers. Thread 1 (1-10),
# Thread2(11 - 20, Thread3(21 - 30).Add diffferent sleep time for each thread and
# print the random numbers between the given numbers by specific threads.
import random
import time
from threading import Thread

def my_fun(a,b,delay):
    time.sleep(delay)
    print(random.randint(a,b))

    print(time.ctime(time.time()))



thread1 = Thread(target=my_fun,args=(1,10,3))
thread1.start()

thread2 = Thread(target=my_fun,args=(11,20,2))
thread2.start()

thread3 = Thread(target=my_fun,args=(21,30,5))
thread3.start()

