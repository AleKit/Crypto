#Test del algoritmo DES. Input: número de intentos
def test_des(number):
    k = 1
    for i in xrange(number):
        key = numerogrande(56)
        plaintext = numerogrande(64)
        cifcif = des_alg(des_alg(plaintext,key),key)
        if cifcif != plaintext:
            print ("Test fallido")
            print ("clave:")
            print key
            print ("texto:")
            print plaintext
            print("xor:")
            print xor(cifcif, plaintext)
            k = 0
            break
    if k == 1:
        print ("Test exitoso")
        
#Test del algoritmo AES. Input: número de intentos
def test_aes(number):
    k = 1
    for i in xrange(number):
        key = numerogrande(128)
        plaintext = numerogrande(128)
        cifcif = aes_decr(aes_encr(plaintext,key),key)
        if cifcif != plaintext:
            print ("Test fallido")
            print ("clave:")
            print key
            print ("texto:")
            print plaintext
            print("xor:")
            print xor(cifcif, plaintext)
            k = 0
            break
    if k == 1:
        print ("Test exitoso") 
        
#Test del algoritmo IDEA. Input: número de intentos
def test_idea(number):
    k = 1
    for i in xrange(number):
        key = numerogrande(128)
        plaintext = numerogrande(64)
        cifcif = ideaalg(key,ideaalg(key,plaintext),0)
        if cifcif != plaintext:
            print ("Test fallido")
            print ("clave:")
            print key
            print ("texto:")
            print plaintext
            print("xor:")
            print xor(cifcif, plaintext)
            k = 0
            break
    if k == 1:
        print ("Test exitoso")
