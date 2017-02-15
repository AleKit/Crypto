# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:45:10 2017

@author: adrian
"""

from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
conn.send('close')
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])

conn.close()