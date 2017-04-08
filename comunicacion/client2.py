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

msg1 = conn.recv()

if msg1[:3] == 'RSA':
    m_rsa = 123
    comma = msg1.index(',')
    encr_rsa = modular_pow(m_rsa,int(msg1[3:comma]),int(msg1[comma+1:]))
    conn.send('RSAe' + str(encr_rsa))
    
if msg1[:2] == 'EG':
    comma = msg1.index(',')
    semicolon = msg1.index(';')
    m_gamal = 128688
    b_gamal = 480
    y1_gamal = modular_pow(int(msg1[2:comma]),b_gamal,
                           int(msg1[comma+1:semicolon]))
    y2_gamal = (modular_pow(int(msg1[semicolon+1:]),b_gamal,
                           int(msg1[comma+1:semicolon])) * m_gamal
                           ) % int(msg1[comma+1:semicolon])
    conn.send('EGe' + str(y1_gamal) + ',' + str(y2_gamal))
    

p = 2**128-159
g = 127696581778553318510832226979062695964
b = p
while b > p-1:
    bstr = numerogrande(int(round(random.random()*10)+10))
    b = int(bstr,2)
#B = g**b % p
B = modular_pow(g,b,p)

message = 'B' + str(B)

conn.send(message)

msg = conn.recv()
if msg[0] == 'A':
    message2 = msg[1:]

A = int(message2)
print A
#s = A**b % p
s = modular_pow(A,b,p)
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
