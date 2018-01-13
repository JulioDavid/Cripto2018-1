from hashlib import sha256
import base64

sal = open("/dev/urandom" , 'rb')
passwcifrados = open('passwords-salt.txt','rb')

passdescifrados = open("passdescifrados.txt", "w")

def pwd_hash(salt, password):
    hash_val = sha256(password+salt)
    hash_dig = hash_val.digest()
    return "$" + str(salt) + "$" + str(base64.b64encode(hash_dig))

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
            passdescifrados.write(line)
    return line + str(contador)

decifrando()
