def generadorclave(clave):
    z = []
    while len(z) <= 52:
        z.append(clave[:16])
        z.append(clave[16:32])
        z.append(clave[32:48])
        z.append(clave[48:64])
        z.append(clave[64:80])
        z.append(clave[80:96])
        z.append(clave[96:112])
        z.append(clave[112:128])
        
        clave = clave[24:] + clave[:24]
    return z


def ideaalg(texto):
    z = generadorclave(clave)
    #print z
    x1 = texto[:16]
    x2 = texto[16:32]
    x3 = texto[32:48]
    x4 = texto[48:64]
    j = 0
    for i in xrange(8):          
        g1 = multimodulo(x1,z[j])
        j += 1
        g2 = sumamodulo(x2,z[j])
        j += 1
        g3 = sumamodulo(x3,z[j])
        j += 1
        g4 = multimodulo(x4,z[j])
        j += 1
        g5 = xor(g1,g3) #paso 5
        g6 = xor(g2,g4) #paso 6
        
        g7 = multimodulo(g5,z[j])
        j += 1 
        g8 = sumamodulo(g6,g7) #paso 8
        g9 = multimodulo(g8,z[j])
        j += 1 #paso 9
        g10 = sumamodulo(g7,g9) #paso 10
        g11 = xor(g1,g9)
        g12 = xor(g3,g9)
        g13 = xor(g2,g10)
        g14 = xor(g4,g10)
        
        x1 = g11
        x2 = g13
        x3 = g12
        x4 = g14
        
    g1 = multimodulo(x1,z[j])
    j += 1
    g2 = sumamodulo(x2,z[j])
    j += 1
    g3 = sumamodulo(x3,z[j])
    j += 1
    g4 = multimodulo(x4,z[j])
    #print j
    return g1 + g2 + g3 + g4
