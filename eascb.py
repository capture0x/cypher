def eascb_func():
    from hashlib import md5
    from base64 import b64decode
    from base64 import b64encode

    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    from Crypto.Util.Padding import pad, unpad

    class AESCipher:
       def __init__(self, key):
           self.key = md5(key.encode('utf8')).digest()

       def encrypt(self, data):
           iv = get_random_bytes(AES.block_size)
           self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
           return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),AES.block_size)))

       def decrypt(self, data):
           raw = b64decode(data)
           self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
           return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

    try:
        print('ENCRYPTION')
        msg = input('Secret Message: ')
        pwd = input('Key : ')
        print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'))

        print('\nDECRYPTION')
        cte = input('Ciphertext: ')
        pwd = input('Key : ')
        print('Message :', AESCipher(pwd).decrypt(cte).decode('utf-8'))
    except:
        print("Wrong Value..!")
