# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 12:55:31 2017

"""

#Algoritmo Data Encryption Standard

###sboxes

sbox1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
         [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
         [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
         [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

sbox2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

sbox3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
         [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
         [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
         [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

sbox4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
         [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
         [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
         [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

sbox5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
         [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
         [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
         [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

sbox6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
         [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
         [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
         [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

sbox7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
         [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
         [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
         [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

sbox8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
         [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
         [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
         [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

sboxes = [sbox1, sbox2, sbox3, sbox4, sbox5, sbox6, sbox7, sbox8]

###/sboxes

#funcion para asignar un numero de una s-box a un conjunto de 6 bits
def des_assignment(bits):
    j = 0
    result = ''
    for i in xrange(8):
        bit1 = bits[j]
        bit6 = bits[j+5]
        selector = int(bits[j+1:j+5],2)
        aux = sboxes[i][int(bit1+bit6,2)][selector]
        result += '{0:0{1}b}'.format(aux,4) 
        j += 6
    return result

#funcion para permutar los bits
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
        
#f-function aplicada a la mitad derecha del texto
def des_ffunction(righthalf):
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
        if j % 6 == 0:
            k += 2
    return expandedright

#funcion para añadir los bits de paridad a la clave original
def des_parity(originalclave): #clave de 56 bits
    parities = ''
    for j in mrange(0,len(originalclave),7):
        if originalclave[j:j+8].count('1') % 2 == 0:
            parities += '1'
        else:
            parities += '0'            
    return ''.join(originalclave[:7] + parities[0] + originalclave[7:14] + 
            parities[1] + originalclave[14:21] + parities[2] + 
            originalclave[21:28] + parities[3] + originalclave[28:35] +
            parities[4] + originalclave[35:42] + parities[5] +
            originalclave[42:49] + parities[6] + 
            originalclave[49:56] + parities[7])

#funcion para generar las subclaves a partir de la clave original; para descifrar cambiar el valor de encriptar
def des_subkeys(clave,encriptar=1): #clave de 64 bits
    j = 56
    lefthalf = ''
    righthalf = ''    
    subkeys = []
    subkeystransp = []
    while True:
        lefthalf += clave[j]
        if j == 35:
            break
        elif j < 7:
            j += 57
        else:
            j -= 8
    j = 62
    while True:
        righthalf += clave[j]
        if j == 3:
            break
        elif j < 7:
            j += 55
        else:
            j -= 8
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
    if encriptar != 1:
        subkeystransp = subkeystransp[::-1]
    return subkeystransp  
    
#funcion que aplica el algoritmo completo, para descifrar cambiar el valor de encriptar
def des_alg(plaintext,key,encriptar=1):
    subkeys = des_subkeys(des_parity(key),encriptar)
    step1 = des_transpose(plaintext)
    lefthalf = step1[:32]
    righthalf = step1[32:]
    for i in xrange(16):
        step2 = des_ffunction(righthalf)
        step25 = xor(step2,subkeys[i])
        step3 = des_assignment(step25)
         #permutacion
        step4 = (step3[15] + step3[6] + step3[19] + step3[20] + 
                step3[28] + step3[11] + step3[27] + step3[16] + 
                step3[0] + step3[14] + step3[22] + step3[25] + 
                step3[4] + step3[17] + step3[30] + step3[9] + 
                step3[1] + step3[7] + step3[23] + step3[13] + 
                step3[31] + step3[26] + step3[2] + step3[8] + 
                step3[18] + step3[12] + step3[29] + step3[5] +
                step3[21] + step3[10] + step3[3] + step3[24])
        step5 = xor(lefthalf,step4)
        if i < 15:
            lefthalf = righthalf
            righthalf = step5
        if i == 15:
            lefthalf = step5
            #righthalf = step4
    finalstep = lefthalf + righthalf
     #permutacion
    encrypt = (finalstep[39] + finalstep[7] + finalstep[47] + finalstep[15] + 
             finalstep[55] + finalstep[23] + finalstep[63] + finalstep[31] + 
            finalstep[38] + finalstep[6] + finalstep[46] + finalstep[14] + 
            finalstep[54] + finalstep[22] + finalstep[62] + finalstep[30] + 
            finalstep[37] + finalstep[5] + finalstep[45] + finalstep[13] + 
            finalstep[53] + finalstep[21] + finalstep[61] + finalstep[29] + 
            finalstep[36] + finalstep[4] + finalstep[44] + finalstep[12] + 
            finalstep[52] + finalstep[20] + finalstep[60] + finalstep[28] + 
            finalstep[35] + finalstep[3] + finalstep[43] + finalstep[11] +
            finalstep[51] + finalstep[19] + finalstep[59] + finalstep[27] + 
            finalstep[34] + finalstep[2] + finalstep[42] + finalstep[10] + 
            finalstep[50] + finalstep[18] + finalstep[58] + finalstep[26] + 
            finalstep[33] + finalstep[1] + finalstep[41] + finalstep[9] +
            finalstep[49] + finalstep[17] + finalstep[57] + finalstep[25] + 
            finalstep[32] + finalstep[0] + finalstep[40] + finalstep[8] + 
            finalstep[48] + finalstep[16] + finalstep[56] + finalstep[24])
    return encrypt
