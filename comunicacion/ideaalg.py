def generadorclave(clave):
    z = []
    while len(z) < 52:
        z.append(clave[:16])
        z.append(clave[16:32])
        z.append(clave[32:48])
        z.append(clave[48:64])
        z.append(clave[64:80])
        z.append(clave[80:96])
        z.append(clave[96:112])
        z.append(clave[112:128])
        
        clave = clave[25:] + clave[:25]
        
    while len(z) > 52:
        z.pop()
    return z

def generadordecr(z):
    w = []
    j = 48
    w.append(inversomodulo(z[j]))
    w.append(opuestomodulo(z[j+1]))
    w.append(opuestomodulo(z[j+2]))
    w.append(inversomodulo(z[j+3]))
    while len(w) < 52:
        w.append(z[j-2])
        w.append(z[j-1])
        #print(w)
        j -= 6
        w.append(inversomodulo(z[j]))
        #print j
        w.append(opuestomodulo(z[j+2]))
        w.append(opuestomodulo(z[j+1]))
        w.append(inversomodulo(z[j+3]))
        
    return w

def ideaalg(clave,texto,encriptar = 1):
    z = generadorclave(clave)
    if encriptar == 0:
        z = generadordecr(z)
    print z
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
        g5 = xor(g1,g3) 
        g6 = xor(g2,g4) 
        
        g7 = multimodulo(g5,z[j])
        j += 1 
        g8 = sumamodulo(g6,g7) 
        g9 = multimodulo(g8,z[j])
        j += 1 
        g10 = sumamodulo(g7,g9) 
        g11 = xor(g1,g9)
        g12 = xor(g3,g9)
        g13 = xor(g2,g10)
        g14 = xor(g4,g10)

        x1 = g11
        x4 = g14
        if i < 7:
            x2 = g12
            x3 = g13
        elif i == 7:
            x2 = g13
            x3 = g12        
        
    g1 = multimodulo(x1,z[j])
    j += 1
    g2 = sumamodulo(x2,z[j])
    j += 1
    g3 = sumamodulo(x3,z[j])
    j += 1
    g4 = multimodulo(x4,z[j])
    print j
    return g1 + g2 + g3 + g4
