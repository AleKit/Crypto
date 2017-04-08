# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:42:21 2017

@author: adrian
"""

from multiprocessing.connection import Listener
import cripto1
import random

#RSA
usersa = input("RSA yes or no? yes = 1, no = 0: ")
if usersa == 1:
    p_rsa = 61
    q_rsa = 53
    n_rsa = p_rsa*q_rsa
    e_rsa = 17
    d_rsa = int(inversomodulo(bin(e_rsa),(p_rsa-1)*(q_rsa-1)-1),2)
   
#ElGamal
useElGamal = input("ElGamal yes or no? yes = 1, no = 0: ")
if useElGamal == 1:
    p_gamal = 15485863
    g_gamal = 7
    a_gamal = 21702
    K_gamal = modular_pow(g_gamal, a_gamal, p_gamal)



address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
a = -1 #esto hay que cambiarlo quiza

if usersa == 1:
    rsamessage = 'RSA' + str(e_rsa) + ',' + str(n_rsa)
    print rsamessage
    conn.send(rsamessage)

if useElGamal == 1:
    gamalmessage = 'EG' + str(g_gamal) + ',' + str(p_gamal) + ';' + str(K_gamal)
    print gamalmessage
    conn.send(gamalmessage)
    
B = 0

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
        A = modular_pow(g,a,p)
        message = 'A' + str(A)
        conn.send(message)
        B = int(msg[1:])
        #s = B**a % p
        s = modular_pow(B,a,p)
        print s
    elif B > 0 and msg[:3] == 'cif':
        descifrador = msg[3:]
    elif B > 0 and msg[:3] == 'vig':
        text = cripto1.decr_vigenere(msg[3:],descifrador)
        print text
    elif B > 0 and msg[:4] == 'idea':
        e = bin(s) 
        f = int(e,2)
        claveidea = '{0:0{1}b}'.format(f,128)
        descifradoidea = ideaalg(clave,msg[4:],0)
    elif msg[:4] == 'RSAe':
        decrypt_rsa = modular_pow(int(msg[4:]),d_rsa,n_rsa)
        print decrypt_rsa
    elif msg[:3] == 'EGe':
        comma = msg.index(',')
        decrypt_gamal = (modular_pow(int(msg[3:comma]),p_gamal-1-a_gamal, 
                                        p_gamal) * int(msg[comma+1:])) % p_gamal
        print decrypt_gamal
        
listener.close()
