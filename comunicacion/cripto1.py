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

    
# 28-oct

def vigenere(text,cifrador):
    tn = normalizar(text)
    cifrador = normalizar(cifrador)
    while len(cifrador) < len(tn):
        cifrador += cifrador
    tv=""
    for i in range(len(tn)):

        index = ord(tn[i]) + ord(cifrador[i])-65  
        while index > 90:
            index = index - 26
        tv += chr(index)
    return tv
    

def decr_vigenere(text,descifrador):
    tn = normalizar(text)
    descifrador = normalizar(descifrador)
    while len(descifrador) < len(tn):
        descifrador += descifrador
    tdv =""
    for i in range(len(tn)):
        for j in range(len(descifrador)):
            if i == j:
                index = ord(tn[i]) - ord(descifrador[j]) + 65
                while index < 65:
                    index = index + 26
                tdv += chr(index)
    return tdv

