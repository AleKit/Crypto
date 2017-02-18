# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:42:21 2017

@author: adrian
"""

from multiprocessing.connection import Listener
import cripto1

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
    elif msg[0] == 'B':
        p = 23
        g = 5
        a = 6
        A = g**a % p
        message = 'A' + str(A)
        conn.send(message)
        B = float(msg[1:])
        s = B**a % p
        print s
    elif B and msg[0:3] == 'cif':
        descifrador = msg[3:]
    elif B and msg[0:3] == 'vig':
        text = cripto1.decr_vigenere(msg[3:],descifrador)
        print text
        
listener.close()