def cipherEn():
    msg = input("Secret Message :")
    key = input("Key :")

    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Encrypted Text :{}".format(encrypt_hex))


def cipherDe():
    msg = input("Encrypted Text :")
    key = input("Key :")

    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i+2]).decode('utf-8')

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Decrypted Text: {}".format(decryp_text))



choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
if choice == 1:
        print("Encrypted:")
        cipherEn()
elif choice == 2:
        print("Decrypted:")
        cipherDe()
else:
        print("Invalid Choice")

