# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:45:10 2017

@author: adrian
"""

from multiprocessing.connection import Client
import cripto1
import random

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')

p = 2**128-159
g = 127696581778553318510832226979062695964
b = p
while b > p-1:
    bstr = numerogrande(int(round(random.random()*10)+10))
    b = int(bstr,2)
#B = g**b % p
B = modular_power(g,b,p)

message = 'B' + str(B)

conn.send(message)

msg = conn.recv()
if msg[0] == 'A':
    message2 = msg[1:]

A = int(message2)
#s = A**b % p
s = modular_power(A,b,p)
print s

cifrador = 'prueba'
conn.send('cif' + cifrador)

text = cripto1.vigenere('holaaliceestoyprobando', cifrador)
conn.send('vig' + text)

textoidea = '0110111101110010011010010110011101101110011011010111001101100111'
e = bin(s) 
f = int(e,2)
claveidea = '{0:0{1}b}'.format(f,128)
cifradoidea = ideaalg(clave,textoidea)

conn.send('idea' + cifradoidea)

conn.send('close') #supongo que si comento esta línea puedo seguir mandando
#los mensajes que quiera usando la consola

# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])

conn.close()
