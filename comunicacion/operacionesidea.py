#se le da como input dos strings de binarios, ejemplo abajo
#a = "11011111101100110110011001011101000"
#b = "11001011101100111000011100001100001"

import random
from math import sqrt
   
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
    
#    x = inversomodulo(b) mod n, (x * b) % n == 1
def inversomodulo(a, n = 2**16):
    b = int(a,2)
    g, x, _ = egcd(b, n+1)
    if g == 1:
        return '{0:0{1}b}'.format(x % (n+1),len(a))
    else:
        return "no se puede calcular"

def xor(a,b): 
    y = int(a,2) ^ int(b,2)
    return '{0:0{1}b}'.format(y,len(a))
    

def numerogrande(n):
    a = random.getrandbits(n)
    #print a
    b = str(a)
    #print b
    c = len(b)
    d = int(b)
    e = bin(d) 
    print e
    f = int(e,2)
    return '{0:0{1}b}'.format(f,128)

#http://stackoverflow.com/questions/17298130/working-with-large-primes-in-python

# for large numbers, xrange will throw an error.
# OverflowError: Python int too large to convert to C long
# to get over this:

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

# benchmark is_prime(100**10-1) using mrange
# 10000 calls, 53191 per second.
# 60006 function calls in 0.190 seconds.

def encontrarprimo(n): #n es el numero de bits
    booleano = False
    while booleano == False:
        m = numerogrande(n)
        booleano = is_prime(int(m,2))
    return m

#'1101100011001101110011010110011001011100000010010001101001110111'
#es primo, 64 bits, el programa lo ha sacado en unos 5-6 minutos
