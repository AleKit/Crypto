# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:55:31 2017

@author: ajand
"""

#creo que estoy haciendo la suma de strings de forma inversa
# a como viene en la pagina, pero no me queda claro
#solucion: transposed = plaintext[j] + transposed

def des_transpose(plaintext): #64 bits
    j = 57
    transposed = ''
    while True:
        transposed += plaintext[j]
        if j == 6:
            break
        elif j < 7:
            j += 58
        elif j == 7:
            j += 49
        else:
            j -= 8
    return transposed
        
def des_ffunction(plaintext):
    righthalf = plaintext[32:]
    expandedright = ''
    j = 0
    k = 0
    while j < 48:
        if j == 0:
            expandedright += righthalf[31]
        elif j < 47:
            expandedright += righthalf[j-1-k]
        elif j == 47:
            expandedright += righthalf[0]
        j += 1
        if j % 6 == 0: #estaria bien revisar si esto se hace cuando debe
            k += 2
            print j
    return expandedright

def des_subkeys(clave): #clave de 64 bits pero hay 8 de paridad??
    j = 56
    lefthalf = ''
    righthalf = ''    
    subkeys = []
    subkeystransp = []
    while True:
        #print j
        lefthalf += clave[j]
        if j == 35:
            break
        elif j < 7:
            j += 57
        else:
            j -= 8
    j = 62
    while True:
        #print j
        righthalf += clave[j]
        if j == 3:
            break
        elif j < 7:
            j += 55
        else:
            j -= 8
    #return lefthalf + righthalf
    for i in xrange(16):
        if i < 2 or i == 8 or i == 15:
            lefthalf = lefthalf[1:] + lefthalf[:1]
            righthalf = righthalf[1:] + righthalf[:1]
        else:
            lefthalf = lefthalf[2:] + lefthalf[:2]
            righthalf = righthalf[2:] + righthalf[:2]
        subkeys.append(lefthalf+righthalf)
        subkeystransp.append(subkeys[i][13]+subkeys[i][16]+subkeys[i][10]+
                             subkeys[i][23]+subkeys[i][0]+subkeys[i][4]+
                             subkeys[i][2]+subkeys[i][27]+subkeys[i][14]+
                             subkeys[i][5]+subkeys[i][20]+subkeys[i][9]+ 
                             subkeys[i][22]+subkeys[i][18]+subkeys[i][11]+
                             subkeys[i][3]+subkeys[i][25]+subkeys[i][7]+
                             subkeys[i][15]+subkeys[i][6]+subkeys[i][26]+
                             subkeys[i][19]+subkeys[i][12]+subkeys[i][1]+
                             subkeys[i][40]+subkeys[i][51]+subkeys[i][30]+
                             subkeys[i][36]+subkeys[i][46]+subkeys[i][54]+
                             subkeys[i][29]+subkeys[i][39]+subkeys[i][50]+
                             subkeys[i][44]+subkeys[i][32]+subkeys[i][47]+
                             subkeys[i][43]+subkeys[i][48]+subkeys[i][38]+
                             subkeys[i][55]+subkeys[i][33]+subkeys[i][52]+
                             subkeys[i][45]+subkeys[i][41]+subkeys[i][49]+
                             subkeys[i][35]+subkeys[i][28]+subkeys[i][31])
        
    return subkeystransp  #probablemente invertir