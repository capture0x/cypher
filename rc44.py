from Crypto.Cipher import ARC4

try:
    hh = input("Secret message :")
    aaa = input("Key :")
    cipher = ARC4.new(aaa.encode())
    encrypted_data = cipher.encrypt(hh.encode())
    print("Encrypted :",str(encrypted_data)[2:-1])

    key = ARC4.new(aaa.encode())
    msg = key.decrypt(encrypted_data)
    print("Decrypted :",str(msg)[2:-1])
except:
    print("Please enter key 16 bytes:")
