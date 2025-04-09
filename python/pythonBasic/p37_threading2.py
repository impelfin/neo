#!/usr/bin/env python

import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), 'chars')

t = threading.Thread(target=getHtml, args=('http://google.com',))
t.start()

print('### END ###')