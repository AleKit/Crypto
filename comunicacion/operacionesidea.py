#se le da como input dos strings de binarios, ejemplo abajo
#a = "11011111101100110110011001011101000"
#b = "11001011101100111000011100001100001"

import random
   
def sumamodulo(a,b, n= 2**16):
    abin = int(a,2)
    bbin = int(b,2)
    x = (abin+bbin)
    #print '{0:0{1}b}'.format(x,len(a))
    y = x % n
    return '{0:0{1}b}'.format(y,len(a))

def opuestomodulo(a, n = 2**16):
    abin = int(a,2)
    x = abin % n
    y = n - x
    return '{0:0{1}b}'.format(y,len(a))

def multimodulo(a,b, n = 2**16):
    abin = int(a,2)
    bbin = int(b,2)
    y = (abin*bbin) % (n+1)
    return '{0:0{1}b}'.format(y,len(a))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
    
    # x = mulinv(b) mod n, (x * b) % n == 1
def inversomodulo(b, n = 2**16):
    g, x, _ = egcd(b, n+1)
    if g == 1:
        return x % (n+1)
    else:
        return "no se puede calcular"

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
    e = bin(d) 
    print e
    f = int(e,2)
    return '{0:0{1}b}'.format(f,128)
