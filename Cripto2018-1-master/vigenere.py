archivo_a_cifrar = "cancion.mp3"
archllave = "cancion_clave_vigenere"

def encrypt(plaintext, key):

    listachars = []
    listacharllave = []
    with open(plaintext, encoding="utf8") as infile:
        for line in infile:
            for symbol in line:
                listachars += str(symbol)
                lista1 = ''.join(listachars)
    with open(key, encoding="utf8") as keyfile:
        for line in keyfile:
            for symbol in line:
                listacharllave += str(symbol)
                lista2 = ''.join(listacharllave)
    llave_length = len(lista2)
    llave_as_int = [ord(i) for i in lista2]
    textoclaro_int = [ord(i) for i in lista1]
    ciphertext = ''
    for i in range(len(textoclaro_int)):
        value = (textoclaro_int[i] + llave_as_int[i % llave_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    textoclaro = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        textoclaro += chr(value + 65)
    return textoclaro

encrypt(archivo_a_cifrar, archllave)
