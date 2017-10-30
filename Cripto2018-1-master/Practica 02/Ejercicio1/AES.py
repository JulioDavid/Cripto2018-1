from Crypto import Random
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=32

def encrypt(mensaje, fraseDeContrasenia):
    # fraseDeContrasenia debe ser de longitud 16, 24 o 32 bytespass
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(fraseDeContrasenia, AES.MODE_CFB, IV)
    return base64.b64encode(aes.encrypt(mensaje))

def decrypt(cifrado, fraseDeContrasenia):
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(fraseDeContrasenia, AES.MODE_CFB, IV)
    return aes.decrypt(base64.b64decode(cifrado))