# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:09:03 2017

"""

import random
import string

def encriptar_mensaje(mensaje,clave):
    separar = []
    separarbits = []
    bitsencr = ''
    encrseparado = []
    while len(mensaje) % 4 != 0:
        mensaje += ' '
    j = 0
    while j < len(mensaje):
        separar.append(mensaje[j:j+4])
        j += 4
        
    #IDEA
    #clave = numerogrande(128)
    separaridea = []
    for item in separar:
        #separarbits.append(text_to_bit(item))
        separaridea.append(ideaalg(clave,text_to_bit(item)))
    
    for item in separaridea:
        bitsencr += item
        #encrseparado.append(bit_to_text(item))   #esto no se puede hacer
        #UnicodeEncodeError: 'ascii' codec can't encode characters in
        #position 0-1: ordinal not in range(128)
    return bitsencr

def desencriptar_mensaje(mensaje,clave):
    separar = []
    juntarbits = ''
    textodesenc = ''
    #while len(mensaje) % 4 != 0:
    #    mensaje += ' '
    j = 0
    while j < len(mensaje):
        separar.append(mensaje[j:j+64])
        j += 64
        
    print separar
    #IDEA
    separaridea = []
    for item in separar:
        separaridea.append(ideaalg(clave,item,0))
    
    for item in separaridea:
        juntarbits += item
    textodesenc = bit_to_text(juntarbits)
    return textodesenc

#http://stackoverflow.com/questions/2257441/
#random-string-generation-with-upper-case-letters-and-digits-in-python/
#23728630#23728630
def id_generator(size=6, chars=string.punctuation + string.letters +
                 string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

mensaje = id_generator(int(random.random()*100))
claveidea = numerogrande(128)
encr = encriptar_mensaje(mensaje,claveidea)
desenc = desencriptar_mensaje(encr,claveidea)