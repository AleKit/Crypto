# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:42:21 2017

@author: adrian
"""

from multiprocessing.connection import Listener

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
while True:
    msg = conn.recv()
    print msg
    # do something with msg
    if msg == 'close':
        conn.close()
        break
listener.close()