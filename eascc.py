import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

try:
    print('ENCRYPTION')
    data = input("Secret Message :")
    aad = input("authenticated but unencrypted data :")
    key = AESGCM.generate_key(bit_length=128)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data.encode(), aad.encode())
    ad=aesgcm.decrypt(nonce, ct, aad.encode())
    print("Encrypted :",str(ct)[2:-1],"\nKey:",str(key)[2:-1],"\nNonce :",str(nonce)[2:-1])

    print('\nDECRYPTION')
    print(str(ad)[2:-1])
except:
    print("Wrong Value..!")
