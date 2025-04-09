#!/usr/bin/env python

import threading, queue, time

work = queue.Queue()

def generator(start, end):
    for _ in range(start, end + 1):
        work.put(_)

def display():
    while work.empty() is False:
        data = work.get()
        print('data is ', str(data))
        time.sleep(1)
        work.task_done()

threading.Thread(target=generator, args=(1, 10)).start()
threading.Thread(target=display()).start()
work.join()