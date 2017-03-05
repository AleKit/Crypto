# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:42:21 2017

@author: adrian
"""

from multiprocessing.connection import Listener
import cripto1
import random

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
a = -1 #esto hay que cambiarlo quiza
while True:
    msg = conn.recv()
    print msg
    # do something with msg
    if msg == 'close':
        conn.close()
        break
    elif msg[0] == 'B' and a == -1:
        p = 2**128-159
        g = 127696581778553318510832226979062695964
        a = p
        while a > p-1:
            astr = numerogrande(int(round(random.random()*10)+10))
            a = int(astr,2)
        #A = g**a % p
        A = modular_power(g,a,p)
        message = 'A' + str(A)
        conn.send(message)
        B = int(msg[1:])
        #s = B**a % p
        s = modular_power(B,a,p)
        print s
    elif B and msg[0:3] == 'cif':
        descifrador = msg[3:]
    elif B and msg[0:3] == 'vig':
        text = cripto1.decr_vigenere(msg[3:],descifrador)
        print text
    elif B and msg[0:4] == 'idea':
        e = bin(s) 
        f = int(e,2)
        claveidea = '{0:0{1}b}'.format(f,128)
        descifradoidea = ideaalg(clave,msg[4:],0)
        
listener.close()
