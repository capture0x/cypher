def rsa_func():
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii

    keyPair = RSA.generate(3072, e=65537)

    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    print("Public Key :",str(pubKeyPEM)[2:-1])
    privKeyPEM = keyPair.exportKey()
    print("Private Key :",str(privKeyPEM)[2:-1])
    msg = input("Secret message :")

    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt((bytearray(msg, 'utf-8')))
    aaaa=binascii.hexlify(encrypted)
    print("Encrypted:", str(aaaa)[2:-1])

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('Decrypted:', str(decrypted)[2:-1])
