#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 12:44:19 2017

@author: ale
"""

#def boxorarray(k): #sbox k = 256 ; parray k = 18
#    box = []
#    for i in xrange(k):
#        box.append(numerogrande(32))
#    return box

        
#def ffunction(numero): #input: 32 bits
#    sboxes = []
#    for i in xrange(4):
#        sboxes.append(boxorarray(256))
#    #sbox1 = sbox()
#    #sbox2 = sbox()
#    #sbox3 = sbox()
#    #sbox4 = sbox()
#    num1 = int(numero[:8],2)
#    num2 = int(numero[8:16],2)
#    num3 = int(numero[16:24],2)
#    num4 = int(numero[24:32],2)
##    s1 = sbox1[num1]
##    s2 = sbox2[num2]
##    s3 = sbox3[num3]
##    s4 = sbox4[num4]
#    s1 = sboxes[0][num1]
#    s2 = sboxes[1][num1]
#    s3 = sboxes[2][num1]
#    s4 = sboxes[3][num1]
#    value = xor(sumamodulo(s1,s2,2**32),sumamodulo(s3,s4,2**32))
#    return value

def subkeygeneration(clave,parray):
    lenclave = len(clave)
    listaclave = []
    parraynueva = []
    if lenclave % 32 != 0:
        print 'elige otra clave'
    else: 
        while len(listaclave) < 18:
            j = 0
            while j < lenclave:
                listaclave.append(clave[j:j+32])
                j += 32
    for i in xrange(18):
        parraynueva.append(xor(bin(parray[i])[2:],listaclave[i]))
    return parraynueva
        

def ffunction(numero,sboxes): #input: 32 bits

    num1 = int(numero[:8],2)
    num2 = int(numero[8:16],2)
    num3 = int(numero[16:24],2)
    num4 = int(numero[24:32],2)

    s1 = bin(sboxes[0][num1])[2:]
    s2 = bin(sboxes[1][num1])[2:]
    #s3 = sboxes[2][num1]
    s3 = bin(sboxes[2][num1])[2:]
    s4 = bin(sboxes[3][num1])[2:]
    value = xor(sumamodulo(s1,s2,2**32),sumamodulo(s3,s4,2**32))
    return value

#uso: ffunction(numerogrande(32))

def blowdecryption(subkeys):
    j = 17
    decrsubkey = []
    while j > -1:
        decrsubkey.append(subkeys[j])
        j-= 1
    return decrsubkey
        
#==============================================================================
# def blowfishalg(plaintext, sboxes = [], parray = None, encriptar = 1):
#     if encriptar == 1:
#         parray = boxorarray(18) #pi fractional??
#         for i in xrange(4):
#             sboxes.append(boxorarray(256))
#     elif encriptar == 0:
#         parray = blowdecryption(parray)
#     for i in xrange(16):
#         textleft = plaintext[:32]
#         textright = plaintext[32:]
#         a1 = xor(textleft,parray[i])
#         a2 = ffunction(a1,sboxes)
#         a3 = xor(a2,textright)
#         if i < 15:
#             textleft = a3
#             textright = a1
#         if i == 15:
#             textleft = a1
#             textright = a3
#     print i
#     b17 = xor(textright,parray[i+1])
#     b18 = xor(textleft,parray[i+2])
#     return (parray,sboxes,b18+b17)
#==============================================================================

def blowfishalg(plaintext, sboxes = [], parray = None, encriptar = 1):
#    if encriptar == 1:
#        parray = boxorarray(18) #pi fractional??
#        for i in xrange(4):
#            sboxes.append(boxorarray(256))
    if encriptar == 0:
        parray = blowdecryption(parray)
    for i in xrange(16):
        textleft = plaintext[:32]
        textright = plaintext[32:]
        a1 = xor(textleft,parray[i])
        a2 = ffunction(a1,sboxes)
        a3 = xor(a2,textright)
        if i < 15:
            textleft = a3
            textright = a1
        if i == 15:
            textleft = a1
            textright = a3
    #print i
    b17 = xor(textright,parray[i+1])
    b18 = xor(textleft,parray[i+2])
    return (b18,b17)

def changingsubkeys(clave, sbox0,sbox1,sbox2,sbox3, parray): #[sbox0,sbox1,sbox2,sbox3]
    plaintext = '0000000000000000000000000000000000000000000000000000000000000000'
    sboxes = [sbox0,sbox1,sbox2,sbox3]
    parraynew = subkeygeneration(clave,parray)
    print parraynew
    for i in mrange(0, 1042, 2): #256*4+18)/2 = 521
        #print i
        keys = blowfishalg(plaintext,sboxes,parraynew)
        if i < 18:
            parraynew[i] = keys[0]
            parraynew[i+1] = keys[1]
        elif i < 274:
            sboxes[0][i-18] = int(keys[0],2)
            sboxes[0][i-17] = int(keys[1],2)
        elif i < 530:
            sboxes[1][i-274] = int(keys[0],2)
            sboxes[1][i-273] = int(keys[1],2)
        elif i < 786:
            sboxes[2][i-530] = int(keys[0],2)
            sboxes[2][i-529] = int(keys[1],2)
        else:
            sboxes[3][i-786] = int(keys[0],2)
            sboxes[3][i-785] = int(keys[1],2)
        #print plaintext
        plaintext = keys[0] + keys[1]
    return(parraynew,sboxes)
    
    #por que se modifica sbox0 ??


#p = numerogrande(64)        
#a = blowfishalg(p)
#b = blowfishalg(a[2],a[1], a[0], 0)

#'0000000000000000000000000000000000000000000000000000000000000000'
#64 zeroes
#blowfishalg('0000000000000000000000000000000000000000000000000000000000000000',[sbox0,sbox1,sbox2,sbox3],subkeygeneration(clave,parray))
    