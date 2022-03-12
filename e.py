import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP
import binascii


key = RSA.generate(2048)



<<<<<<< HEAD
private_key = key.export_key()
public_key = key.publickey()



=======
private_key = key.export_key().decode("utf-8") 
public_key1 = key.publickey().exportKey().decode("utf-8")



# print(private_key)
# print(public_key )


>>>>>>> dfee7a2... more code


class CryptoGraphy():
    def __init__(self, model) -> None:
        ...

    def decrypt(self, exText):
<<<<<<< HEAD
        decryptor = PKCS1_OAEP.new(key)
=======
        key1 = RSA.importKey(private_key)
        decryptor = PKCS1_OAEP.new(key1)
>>>>>>> dfee7a2... more code
        decrypted = decryptor.decrypt(exText)
        return decrypted

    def encrypt(self, data: str=''):
<<<<<<< HEAD
        encryptor = PKCS1_OAEP.new(public_key)
=======
        key = RSA.importKey(public_key1)

        encryptor = PKCS1_OAEP.new(key)
>>>>>>> dfee7a2... more code
        encrypted = encryptor.encrypt(bytes(data, encoding='utf8'))
        return encrypted


crypto = CryptoGraphy(model=None)
l = crypto.encrypt('salim suleiman')
<<<<<<< HEAD


print(binascii.hexlify(l))

print(crypto.decrypt(l))
=======
print(binascii.hexlify(l))

print(crypto.decrypt(l).decode("utf-8") )
>>>>>>> dfee7a2... more code
