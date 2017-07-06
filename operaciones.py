#se le da como input dos strings de binarios, ejemplo abajo
#a = "11011111101100110110011001011101000"
#b = "11001011101100111000011100001100001"

   
""" 
c = '101'
'{0:0{1}b}'.format(int(c),0)
Out[27]: '1100101'

'{0:0{1}b}'.format(int(c,2),0)
Out[28]: '101' """

import random
from math import sqrt

#funcion para sumar dos numeros binarios a+b (cadenas de caracteres) modulo el numero n que se elija
def sumamodulo(a,b, n= 2**16):
    abin = int(a,2)
    bbin = int(b,2)
    x = (abin+bbin)
    #print '{0:0{1}b}'.format(x,len(a))
    y = x % n
    return '{0:0{1}b}'.format(y,len(a))

#funcion para encontrar el opuesto b de unnumero binario a (cadena de caracteres) modulo el numero n que se elija: (a + b) mod n = 0 mod n
def opuestomodulo(a, n = 2**16):
    abin = int(a,2)
    x = abin % n
    y = n - x
    return '{0:0{1}b}'.format(y,len(a))

#funcion para multiplicar dos numeros binarios a*b (cadenas de caracteres) modulo el numero n que se elija
def multimodulo(a,b, n = 2**16):
    abin = int(a,2)
    bbin = int(b,2)
    #caso particular a = 0 o b = 0
    if n == 2**16 and abin == 0:
        abin = 2**16
    if n == 2**16 and bbin == 0:
        bbin = 2**16
    y = (abin*bbin) % (n+1)
    return '{0:0{1}b}'.format(y,len(a))

#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#funcion para encontrar el maximo comun divisor de dos numeros a, b
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
    
    # x = mulinv(b) mod n, (x * b) % n == 1
    #en el caso particular la longitud es 17 en vez de 16
 
#def inversomoduloold(a, n = 2**16): #con AES no funciona bien
#    b = int(a,2)
    #caso particular a = 0
#    if n == 2**16 and b == 0:
#        b = 2**16
#    g, x, _ = egcd(b, n+1)
#    if g == 1:
#        return '{0:0{1}b}'.format(x % (n+1),len(a))
#    else:
#        return "no se puede calcular"

#funcion para calcular el inverso de un numero binario a (cadena de caracteres) modulo el numero n que se elija cuando sea posible
def inversomodulo(a, n = 2**16): #AES
    b = int(a,2)
    #caso particular a = 0
    #if n == 2**16 and b == 0:
    if b == 0:
        return '{0:0{1}b}'.format(0 ,len(a))
    else:
        g, x, _ = egcd(b, n+1)
        #print g
        if g == 1:
            return '{0:0{1}b}'.format(x % (n+1),len(a))
        else:
            return "no se puede calcular"

#funcion para realizar or exclusivo de dos numeros binarios a xor b (cadenas de caracteres)          
def xor(a,b): 
    y = int(a,2) ^ int(b,2)
    return '{0:0{1}b}'.format(y,len(a))
    
#funcion para generar una cadena de caracteres de un numero binario con la longitud n que se elija
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
    return '{0:0{1}b}'.format(f,n)

#http://stackoverflow.com/questions/17298130/working-with-large-primes-in-python

# for large numbers, xrange will throw an error.
# OverflowError: Python int too large to convert to C long
# to get over this:

#funcion para iterar desde start hasta stop con el paso step
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.

#funcion para comprobar si un numero es primo
def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

# benchmark is_prime(100**10-1) using mrange
# 10000 calls, 53191 per second.
# 60006 function calls in 0.190 seconds.

#funcion para encontrar un primo con el numero de bits n que se elija
def encontrarprimo(n): #n es el numero de bits
    booleano = False
    while booleano == False:
        m = numerogrande(n)
        booleano = is_prime(int(m,2))
    return m

#'1101100011001101110011010110011001011100000010010001101001110111'
#es primo, 64 bits, el programa lo ha sacado en unos 5-6 minutos

#funcion para calcular base^exponent mod modulus
def modular_pow(base, exponent, modulus):
    if modulus == 1: 
        return 0 
    c = 1
    for e_prime in xrange(exponent):
        c = (c * base) % modulus
    return c
