from Crypto.Cipher import AES


def decrypt_image():
    try:
        key = input("Enter Your Key :")
        iv = input("Enter Your IV :")
        file_name = input("Enter Encrypt Image Path :")
        cfb_cipher = AES.new(key.encode(), AES.MODE_CFB,iv.encode())
        input_file = open(file_name, "rb")
        input_data = input_file.read()
        input_file.close()
        enc_data = cfb_cipher.decrypt(input_data)
        enc_file = open(file_name.replace(".wrr", ""), "wb")
        enc_file.write(enc_data)
        enc_file.close()
        print("Decrypted :", file_name)

    except Exception as f:
        print(f)

decrypt_image()
