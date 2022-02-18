# 12. Make your main thread to wait until all the child threads have completed their execution.


import random
import threading
import time

class mythred(threading.Thread):

    def __init__(self,a,b,delay):
        threading.Thread.__init__(self)
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
thread3=mythred(21,30,6)

thread1.my_fun()
thread2.my_fun()
thread3.my_fun()


thread1.start()
thread2.start()
thread3.start()

print("it's Main Thread")
