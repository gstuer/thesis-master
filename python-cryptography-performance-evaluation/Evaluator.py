from Encryptor import RSA2048_SHA256_OAEP,RSA4096_SHA512_OAEP
import os
import time
import timeit
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,padding

# def executeTimed(function):
#     timer = timeit.Timer(function, timer=time.perf_counter_ns)
#     milliseconds = timer.timeit(number=1) / 1000000.0
#     print(milliseconds)

# # Initialize keys
# privateKey = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048
# )
# publicKey = privateKey.public_key()

# # Initialize data
# data = os.urandom(64)

# # Encrypt
# hashAlgorithm = hashes.SHA256()
# cryptPadding = padding.OAEP(mgf=padding.MGF1(algorithm=hashAlgorithm), algorithm=hashAlgorithm, label=None)
# executeTimed(lambda: publicKey.encrypt(data, cryptPadding))
# dataEncrypted = publicKey.encrypt(data, cryptPadding)

# # Decrypt
# hashAlgorithm = hashes.SHA256()
# cryptPadding = padding.OAEP(mgf=padding.MGF1(algorithm=hashAlgorithm), algorithm=hashAlgorithm, label=None)
# executeTimed(lambda: privateKey.decrypt(dataEncrypted, cryptPadding))
# dataDecrypted = privateKey.decrypt(dataEncrypted, cryptPadding)
# assert(data == dataDecrypted)

encryptors = [RSA2048_SHA256_OAEP(), RSA4096_SHA512_OAEP()]
values = [os.urandom(64), os.urandom(64), os.urandom(64)]
results = []
for encryptor in encryptors:
    # Dry run to avoid memory influence
    dryRunData = os.urandom(64)
    encryptTime, encryptOutput = encryptor.encryptTimed(dryRunData)
    decryptTime, decryptOutput = encryptor.decryptTimed(encryptOutput)

    # Execute with random data
    for value in values:
        encryptTime, encryptOutput = encryptor.encryptTimed(value)
        decryptTime, decryptOutput = encryptor.decryptTimed(encryptOutput)
        results.append({"algorithm": encryptor.identifier, "time_encrypt": encryptTime, "time_decrypt": decryptTime})

print(results)