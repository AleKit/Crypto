#Test del algoritmo DES. Input: número de intentos
def test_des(number):
    k = 1
    for i in xrange(number):
        key = numerogrande(56)
        plaintext = numerogrande(64)
        if des_alg(des_alg(plaintext,key),key) != plaintext:
            print ("Test fallido")
            print ("clave:")
            print key
            print ("texto:")
            print plaintext
            print("xor:")
            print xor(des_alg(des_alg(plaintext,key),key), plaintext)
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
        if ideaalg(key,ideaalg(key,plaintext),0) != plaintext:
            print ("Test fallido")
            print ("clave:")
            print key
            print ("texto:")
            print plaintext
            print("xor:")
            print xor(ideaalg(key,ideaalg(key,plaintext),0),plaintext)
            k = 0
            break
    if k == 1:
        print ("Test exitoso")
