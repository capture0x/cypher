from Crypto.Cipher import ARC2

try:
    hello = input("Secret message :")
    key = input("Please Enter Key 16 Byte :")
    cipher = ARC2.new(key.encode(), ARC2.MODE_CFB)
    a = cipher.iv
    msg = a + cipher.encrypt(hello.encode())
    print("Encrypted :",str(msg)[2:-1])

    ciphertext = msg
    iv = ciphertext[:ARC2.block_size]
    ciphertext = ciphertext[ARC2.block_size:]
    cipher = ARC2.new(key.encode(), ARC2.MODE_CFB, iv)
    text = cipher.decrypt(ciphertext)
    print("Decrypted :",str(text)[2:-1])
except:
    print("Wrong Value..!")
