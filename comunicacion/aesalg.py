
#de momento todo para 128 bits

#para 192: las filas no cambian, pero son 6 columnas

def block_matrix(block):
    matrixk = [[0 for x in xrange(4)] for x in xrange(4)]
    k = 0
    l = 0
    for j in mrange(0,len(block),8):
        matrixk[k][l] = block[j:j+8]
        k += 1
        if k > 3:
            k = 0
            l += 1
    return matrixk

def sub_bytes(byte):
    invbyte = inversomodulo(byte,2**8)
    bit4rot = invbyte[4:] + invbyte[:4]
    bit5rot = invbyte[3:] + invbyte[:3]
    bit6rot = invbyte[2:] + invbyte[:2]
    bit7rot = invbyte[1:] + invbyte[0]
    c = '0' + bin(0x63)[2:]
    byteout = xor(xor(xor(xor(xor(invbyte,bit4rot),bit5rot),bit6rot),bit7rot),c)
    return byteout
    
def shift_row(matrix):
    shiftmatrix = [[0 for x in xrange(4)] for x in xrange(4)]
    shiftmatrix[0] = matrix[0]
    shiftmatrix[1] = matrix[1][1:] + matrix[1][:1]
    shiftmatrix[2] = matrix[2][2:] + matrix[2][:2]
    shiftmatrix[3] = matrix[3][3:] + matrix[3][:3]
    return shiftmatrix
    
def mix_columns(matrix):
    one = '00000001'
    two = '00000010'
    three = '00000011'
    replacematrix = [[two, three, one, one],[one, two, three, one],
                     [one, one, two, three],[three,one,one,two]]
    mixmatrix = [[bin(sum(int(a,2)*int(b,2) for a,b in zip(replacematrix_row,matrix_col)) % 2**8) for
                  matrix_col in zip(*matrix)] for replacematrix_row in replacematrix]

    return mixmatrix

def g_function(word, r, rc): #r is the round
    gcirc = word[1:] + word[0]
    bytes4 = []
    for i in mrange(0,32,8):
        bytes4.append(sub_bytes(gcirc[i:i+8]))
    if r == 1: 
        rc = '00000001'
    else:
        rc = multimodulo('00000010',rc)
    bytes4[0] = xor(bytes4[0], rc)
    newword = ''
    for j in xrange(4):
        newword += bytes4[j]
    return newword, rc

def key_expansion(key, r, rc): #en realidad la ronda 0 sobra
    oldwords = []
    newwords = []
    newkey = ''
    j = 0
    for i in mrange(0, 128, 32):
        oldwords.append(key[i:i+32])
        if r == 0:
            newkey += oldwords[j]
            j += 1
    if r != 0:
        bytes4, rc = g_function(oldwords[3], r, rc)
        newwords.append(xor(oldwords[0],bytes4))
        for j in mrange(0,4,1):
            if j != 0:
                newwords.append(xor(newwords[j-1],oldwords[j]))
            newkey += newwords[j]
            
    return newkey, rc

def aes_keys(key):
    rc = 0
    allkeys = []
    for r in xrange(11):
        key, rc = key_expansion(key, r, rc)
        allkeys.append(key)
    return allkeys

def aes_encr(plaintext, key):
    xorplain = xor(plaintext,key)
    allkeys = aes_keys(key)
    for j in xrange(1,11):
        step1 = ''
        for i in mrange(0,len(plaintext),8):
            step1 += sub_bytes(plaintext[i:i+8])
        bmatrix = block_matrix(step1)
        step2 = shift_row(bmatrix)
        step3 = mix_columns(step2)
        k = 0
        l = 0
        aux = ''
        for m in mrange(0,len(plaintext),8):
            auxaux = step3[k][l][2:]
            while len(auxaux) < 8:
                auxaux = '0' + auxaux
            aux += auxaux
            k += 1
            if k > 3:
                k = 0
                l += 1
        step4 = xor(aux,allkeys[j])
        plaintext = step4
        print len(plaintext)
    return plaintext
