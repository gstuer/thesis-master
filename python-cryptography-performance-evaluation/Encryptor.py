import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding

from Timeable import Timeable

class Encryptor(Timeable):
    def __init__(self, identifier):
        self.identifier = identifier

    def encrypt(self, data):
        raise NotImplementedError()

    def decrypt(self, data):
        raise NotImplementedError()

    def encryptTimed(self, data):
        time = self.executeTimedMilliseconds(lambda: self.encrypt(data))
        output = self.encrypt(data)
        return (time, output)

    def decryptTimed(self, data):
        time = self.executeTimedMilliseconds(lambda: self.decrypt(data))
        output = self.decrypt(data)
        return (time, output)

class RSA2048_SHA256_OAEP(Encryptor):
    def __init__(self):
        super().__init__("RSA2048_SHA256_OAEP")
        # Initialize keys
        self.privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.publicKey = self.privateKey.public_key()

        # Initialize hash algorithm & padding
        self.hash = hashes.SHA256()
        self.padding = padding.OAEP(mgf=padding.MGF1(algorithm=self.hash), algorithm=self.hash, label=None)
        

    def encrypt(self, data):
        return self.publicKey.encrypt(data, self.padding)

    def decrypt(self, data):
        return self.privateKey.decrypt(data, self.padding)

class RSA4096_SHA512_OAEP(Encryptor):
    def __init__(self):
        super().__init__("RSA4096_SHA512_OAEP")
        # Initialize keys
        self.privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )
        self.publicKey = self.privateKey.public_key()

        # Initialize hash algorithm & padding
        self.hash = hashes.SHA512()
        self.padding = padding.OAEP(mgf=padding.MGF1(algorithm=self.hash), algorithm=self.hash, label=None)

    def encrypt(self, data):
        return self.publicKey.encrypt(data, self.padding)

    def decrypt(self, data):
        return self.privateKey.decrypt(data, self.padding)
