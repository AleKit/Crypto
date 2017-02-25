#se le da como input dos strings de binarios, ejemplo abajo
#a = "11011111101100110110011001011101000"
#b = "11001011101100111000011100001100001"

def sumamodulo(a,b):
    abin = int(a,2)
    bbin = int(b,2)
    x = (abin+bbin)
    print '{0:0{1}b}'.format(x,len(a))
    y = x % (2**16)
    return '{0:0{1}b}'.format(y,len(a))

def opuestomodulo(a):
    abin = int(a,2)
    x = abin % (2**16)
    y = 2**16 - x
    return '{0:0{1}b}'.format(y,len(a))

def multimodulo(a,b):
    abin = int(a,2)
    bbin = int(b,2)
    y = (abin*bbin) % (2**16+1)
    return '{0:0{1}b}'.format(y,len(a))

def xor(a,b): 
    y = int(a,2) ^ int(b,2)
    return '{0:0{1}b}'.format(y,len(a))

def numerogrande(n):
    a = random.getrandbits(n)
    print a
    b = str(a)
    print b
    c = len(b)
    d = int(b)
    e = bin(d) #ahora hay que quitar el 0b del principio
    print e
    f = int(e,2)
    return '{0:0{1}b}'.format(f,128)
