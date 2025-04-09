#!/usr/bin/env python

import threading, time

data = 0

lock = threading.Lock()

def generator(start, end):
    global data
    for _ in range(start, end + 1):
        lock.acquire()
        buf = data
        time.sleep(0.01)
        data = buf + 1
        lock.release()

t1 = threading.Thread(target=generator, args=(1, 10))
t2 = threading.Thread(target=generator, args=(1, 10))

t1.start()
t2.start()

t1.join()
t2.join()

print(data)