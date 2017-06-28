# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:59:43 2016
"""

def normalizar(texto):
    tn = ""
    for letra in texto:
        indx = ord(letra)
        if 97 <= indx <= 122:
            indx = indx - 32
            tn = tn + chr(indx)
        elif 65 <= indx <= 90:
            tn = tn + letra
    return tn
            

def cesar(texto,desplazamiento):
    tn = normalizar(texto)
    tc = ""
    for letra in tn:
        indx = ord(letra) + desplazamiento
        if indx >= 91:
            indx -= 26
        tc = tc + chr(indx)
    return tc

#27-jun
#def fac(n):
#  f = 1
#  if n == 0 or n == 1:
#    return f
#  else:
#    f = fac(n-1) * n
#    return f
    
# 28-oct

def vigenere(text):
    tn = normalizar(text)
    word = input("Introduce la palabra para cifrar:")
    word = normalizar(word)
    while len(word) < len(tn):
        word += word
    tv=""
    for i in range(len(tn)):
      #  for j in range(len(word)):  
      #      if i == j:
        index = ord(tn[i]) + ord(word[i])-65   #word[j], indexar
        while index > 90:
            index = index - 26
        tv += chr(index)
    return tv
    

def afin(text):
    print("Cifrado tipo ax+b")
    #Cesar: a = 1
    #usa ord("a") = 0
    tn = normalizar(text)
    taf = ""
    a = input("Introduce el multiplicador a:")
    b = input ("Introduce la constante b:")
    for letra in tn:
        index = (ord(letra)-65)*a + b + 65
        while index > 90:
            index = index - 26
        taf += chr(index)
    return taf
            
    
def railfence(text):
    t1 = ""
    t2 = ""
    t3 = ""
    #t4 = ""
    #t5 = ""
    trf = ""
    #n = input("Elige un numero de railes entre 2 y 5:)
    for i in range(len(text)):
        if i % 3 == 0:
            t1 += text[i]
        elif i % 3 == 1:
            t2 += text[i]
        elif i % 3 == 2:
            t3 += text[i]
    trf += t1 + t2 + t3 #podria cambiar el orden de la suma
    return trf

def decr_vigenere(text):
    tn = normalizar(text)
    word = input("Introduce la palabra para descifrar:")
    word = normalizar(word)
    while len(word) < len(tn):
        word += word
    tdv =""
    for i in range(len(tn)):
        for j in range(len(word)):
            if i == j:
                index = ord(tn[i]) - ord(word[j]) + 65
                while index < 65:
                    index = index + 26
                tdv += chr(index)
    return tdv

#

def beaufort(text):
    tn = normalizar(text)
    word = input("Introduce la palabra para cifrar:")
    word = normalizar(word)
    while len(word) < len(tn):
        word += word
    tb=""
    for i in range(len(tn)):   
        index = - ord(tn[i]) + ord(word[i]) + 65
        while index < 65:
            index = index + 26
        tb += chr(index)
    return tb
