#!/usr/bin/env python

import threading

def example():
    for _ in range(1, 20):
        print(_)

threading.Thread(target=example).start()
threading.Thread(target=example).start()