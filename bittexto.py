# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:58:01 2017

@author: ajand
"""

#funcion para transformar una cadena de caracteres en una cadena de numeros binarios
#a cada caracter le corresponden 16 bits siguiendo el formato Unicode
def text_to_bit(texto):
    textobits = ''
    for letra in texto:
        aux = bin(ord(letra))
        bit = aux[2:]
        while len(bit) < 16:
            bit = '0' + bit
        textobits += bit
    return textobits

#funcion para transformar una cadena de bits en una cadena de texto
#cada 16 bits corresponden a un caracter siguiendo el formato Unicode
def bit_to_text(bits):
    bittexto = ''
    j = 0
    while j < len(bits):
        aux = bits[j:j+16]
        integ = int(aux,2)
        bittexto += unichr(integ)
        j += 16
    bittexto = str(bittexto)
    return bittexto
