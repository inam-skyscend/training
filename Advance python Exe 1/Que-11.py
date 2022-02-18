# 11. The same above example should first print 5 random numbers from first thread
# then 5 random numbers from second thread and then it should print 5 random
# numbers from 3 rd thread using synchronization.

import random
import threading
import time

class mythred(threading.Thread):

    def __init__(self,a,b,delay):
        super().__init__()
        self.a=a
        self.b=b
        self.delay=delay

    def my_fun(self):
        threadLock.acquire()
        l1=random.sample(range(self.a,self.b),5)
        time.sleep(self.delay)
        print(l1[0:5])
        print(time.ctime(time.time()))
        threadLock.release()


threadLock = threading.Lock()

thread1=mythred(1,10,2)
thread2=mythred(11,20,1)
thread3=mythred(21,30,5)

thread1.my_fun()
thread2.my_fun()
thread3.my_fun()


thread1.start()
thread2.start()
thread3.start()