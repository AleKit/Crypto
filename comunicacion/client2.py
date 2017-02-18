# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:45:10 2017

@author: adrian
"""

from multiprocessing.connection import Client
import cripto1

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')

p = 23
g = 5
b = 15
B = g**b % p

message = 'B' + str(B)

conn.send(message)

msg = conn.recv()
if msg[0] == 'A':
    message2 = msg[1:]

A = float(message2)
s = A**b % p
print s

cifrador = 'prueba'
conn.send('cif' + cifrador)

text = cripto1.vigenere('holaaliceestoyprobando', cifrador)
conn.send('vig' + text)

conn.send('close') #supongo que si comento esta línea puedo seguir mandando
#los mensajes que quiera usando la consola

# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])

conn.close()