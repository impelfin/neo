#!/usr/bin/env python

import threading, time
from random import sample

class Sample(threading.Thread):
    def __init__(self, time):
        super(Sample, self).__init__()
        self.time = time
        self.start()

    def run(self):
        print(self.time, "starts")
        for i in range(0, self.time):
            time.sleep(1)
        print(self.time, " has finished")

t3 = Sample(3)
t2 = Sample(2)
t1 = Sample(1)
t3.join()
print("t3.join() has finished.")
t2.join()
print("t2.join() has finished.")
t1.join()
print("t1.join() has finished.")
