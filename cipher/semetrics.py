import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP
import binascii

class Cipher():
    def __init__(self, instance) -> None:
        self.instance = instance
        self.private_key = RSA.importKey(self.instance.payer.private_key)
        self.public_key = RSA.importKey(self.instance.payer.public_key)


    def decrypt(self, exText):
        decryptor = PKCS1_OAEP.new(self.private_key)
        decrypted = decryptor.decrypt(exText)
        return decrypted

    def encrypt(self):
        encryptor = PKCS1_OAEP.new(self.public_key)
        encrypted = encryptor.encrypt(bytes(self.instance.data, encoding='utf8'))
        return binascii.hexlify(encrypted).decode("utf-8") 
        
