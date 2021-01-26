def descb_func():
    from Crypto.Cipher import DES


    def pad(text):
        n = len(text) % 8
        return text + (b' ' * n)


    try:
        print('ENCRYPTION')
        text1 = input("NOTE:Secret message and key must be 8 or 16 bytes\nSecret Message :")
        key = input("Key :")
        des = DES.new(key.encode(), DES.MODE_ECB)
        padded_text = pad(text1.encode())
        encrypted_text = des.encrypt(padded_text)
        print(str(encrypted_text)[2:-1])

        print('\nDECRYPTION')
        aaa=des.decrypt(encrypted_text)
        print(str(aaa)[2:-1])
    except:
        print("Wrong Value..!")
