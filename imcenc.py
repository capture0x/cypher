
def imcenc_func():
    from Crypto.Cipher import AES

    def encrypt_image():
        try:
            key=input("ex:key 16 or 32 byte\nEnter Your Key :")
            iv=input("Enter Your IV :")
            file_name=input("Enter Your Image Path :")
            cfb_cipher = AES.new(key.encode(), AES.MODE_CFB, iv.encode())
            input_file = open(file_name, "rb")
            input_data = input_file.read()
            input_file.close()
            enc_data = cfb_cipher.encrypt(input_data)
            enc_file = open(file_name + ".wrr", "wb")
            enc_file.write(enc_data)
            enc_file.close()
            print("Encrypted :", file_name + ".wrr")
        except:
            print("Key and iv value must be 16 bytes...")

    encrypt_image()

