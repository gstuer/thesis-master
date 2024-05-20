from Encryptor import RSA2048_SHA256_OAEP,RSA4096_SHA512_OAEP,AES128_CBC,AES256_CBC,AES128_GCM,AES256_GCM
import os

RANDOM_VALUE_AMOUNT = 100
RANDOM_BYTES_PER_VALUE = 128

randomValues = [os.urandom(RANDOM_BYTES_PER_VALUE) for x in range(RANDOM_VALUE_AMOUNT)]
results = []
encryptors = [RSA2048_SHA256_OAEP(), RSA4096_SHA512_OAEP(), AES128_CBC(), AES256_CBC(), AES128_GCM(), AES256_GCM()]
for encryptor in encryptors:
    # Dry run to avoid memory influence
    dryRunData = os.urandom(RANDOM_BYTES_PER_VALUE)
    encryptTime, encryptOutput = encryptor.encryptTimed(dryRunData)
    decryptTime, decryptOutput = encryptor.decryptTimed(encryptOutput)

    # Execute with random data
    encryptTimes = []
    decryptTimes = []
    for value in randomValues:
        encryptTime, encryptOutput = encryptor.encryptTimed(value)
        decryptTime, decryptOutput = encryptor.decryptTimed(encryptOutput)
        encryptTimes.append(encryptTime)
        decryptTimes.append(decryptTime)
    results.append({"algorithm": encryptor.identifier, "times_encrypt": encryptTimes, "times_decrypt": decryptTimes})
print(results)
