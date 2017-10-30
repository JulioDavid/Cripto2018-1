from hashlib import sha256
import base64

sal = open("passwords-salt.txt" , 'rb')
passwcifrados = open('passwords-salt.txt','rb')



def pwd_hash(salt, password):
    hash_val = sha256(password+salt)
    return "$" + str(salt) + "$" + base64.b64encode(hash_val)

def decifrando():
    salacion = sal.read(10)
    contador = 0
    with open('common-passwords.txt','rb') as f:
        for line in f:
            hasheado = pwd_hash(salacion, line)
            for linea in passwcifrados:
                while hasheado != linea:
                    salacion = sal.read(10)
                contador += 1
    return line + str(contador)

decifrando()
