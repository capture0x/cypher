import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

try:
    print('ENCRYPTION')
    data = input("Secret Message :")
    aad = b"authenticated but unencrypted data"
    key = AESGCM.generate_key(bit_length=128)
    print("Your key :",str(key)[2:-1])
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data.encode(), aad)
    ad=aesgcm.decrypt(nonce, ct, aad)
    print(str(ct)[2:-1])

    print('\nDECRYPTION')
    print(str(ad)[2:-1])
except:
    print("Wrong Value..!")
