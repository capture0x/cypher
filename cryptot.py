import enter
import base64
import hashlib
import os
import sys
from time import sleep
import requests
from bs4 import BeautifulSoup


def base644():
    message = input("Enter String :")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("Encode String : ", end="")
    print(base64_message)


def base64d():
    base64_message = input("Enter Base64 :")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("Decoded Base64 : ", end="")
    print(message)


def encodemdh5():
    str2hash = input("Enter String :")
    result = hashlib.md5(str2hash.encode())
    print("Encode String : ", end="")
    print(result.hexdigest())


def decodemdh5():
    satr2hash = input("Enter hash :")
    url = f"https://md5.gromweb.com/?md5={satr2hash}"
    istek = requests.get(url)
    soup = BeautifulSoup(istek.text, "lxml")
    a = soup.findAll("em", {"class": "long-content string"})
    for i in a:
        print(i.text)


def shaa1():
    str2hash = input("Enter String :")
    result = hashlib.sha1(str2hash.encode())
    print("Encode String : ", end="")
    print(result.hexdigest())


def sha11():
    str2hash = input("Enter hash :")
    url = f"https://sha1.gromweb.com/?hash={str2hash}"
    istek = requests.get(url)
    soup = BeautifulSoup(istek.text, "lxml")
    a = soup.findAll("em", {"class": "long-content string"})
    for i in a:
        print(i.text)


def shaa3():
    str2hash = input("Enter String :")
    result = hashlib.sha384(str2hash.encode())
    print("Encode String : ", end="")
    print(result.hexdigest())


def sha33():
    str2hash = input("Enter hash :")
    with open("aaaa.txt", "w") as f:
        f.write(str2hash)
    os.system("john --format=Raw-SHA384 aaaa.txt")


def shaa22():
    str2hash = input("Enter String :")
    result = hashlib.sha256(str2hash.encode())
    print("Encode String : ", end="")
    print(result.hexdigest())


def sha2():
    str2hash = input("Enter hash :")
    with open("aaaa.txt", "w") as f:
        f.write(str2hash)
    os.system("john  --format=Raw-SHA256 aaaa.txt")


def shaa5():
    str2hash = input("Enter String :")
    result = hashlib.sha3_512(str2hash.encode())
    print("Encode String : ", end="")
    print(result.hexdigest())


def sha55():
    str2hash = input("Enter hash :")
    with open("aaaa.txt", "w") as f:
        f.write(str2hash)
    os.system("john --format=Raw-SHA512 aaaa.txt")


def hashh():
    x = """ 
    1) BASE64
    2) MD5
    3) SHA1
    4) SHA384
    5) SHA256
    6) SHA512
    7) GO BACK MAIN MENU 
    """
    print(x)
    choosee = input("--------------->PLEASE CHOOSE :")
    if choosee == "1":
        a = input("1.Encryption \n2.Decryption \nChoose(1,2): ")
        if a == "1":
            base644()
            sleep(3)
            hashh()
        elif a == "2":
            base64d()
            sleep(3)
            hashh()

    elif choosee == "2":
        a = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
        if a == "1":
            encodemdh5()
            sleep(3)
            hashh()
        elif a == "2":
            decodemdh5()
            sleep(3)
            hashh()
    elif choosee == "3":
        a = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
        if a == "1":
            shaa1()
            sleep(3)
            hashh()
        elif a == "2":
            sha11()
            sleep(3)
            hashh()
    elif choosee == "4":
        a = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
        if a == "1":
            shaa3()
            sleep(3)
            hashh()
        elif a == "2":
            sha33()
            sleep(3)
            hashh()

    elif choosee == "5":
        a = input("1.Encryption\n2. Decryption\nChoose(1,2): ")
        if a == "1":
            shaa22()
            sleep(3)
            hashh()
        elif a == "2":
            sha2()
            sleep(3)
            hashh()
    elif choosee == "6":
        a = input("1.Encryption\n2. Decryption\nChoose(1,2): ")
        if a == "1":
            shaa1()
            sleep(3)
            hashh()
        elif a == "2":
            sha11()
            sleep(3)
            hashh()
    elif choosee == "7":
        secim()
    else:
        print("Wrong Choose!!!!")


def rsaa():
    import rsaaa
    sleep(3)
    secim()

def xorr():
    import xorr
    sleep(3)
    secim()

def aess():
    import eascc
    sleep(3)
    secim()


def aessc():
    import eascb
    sleep(3)
    secim()


def dese():
    import descb
    sleep(3)
    secim()


def desc():
    import descc
    sleep(3)
    secim()


def rc22():
    import rc22
    sleep(3)
    secim()


def rc44():
    import rc44
    sleep(3)
    secim()


def efss():
    import chacha
    sleep(3)
    secim()

def tlss():
    import tlss
    sleep(3)
    secim()


def diffiee():
    import dff
    sleep(3)
    secim()

def imgenc():
    a = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
    if a =="1":
        import imcenc
        print("Img Encrypted...")
        sleep(2)
        secim()
    elif a == "2":
        import imcdec
        print("Img DEcrypted...")
        sleep(2)
        secim()

def fileenc():
    a = input("1. Encryption\n2. Decryption\nChoose(1,2): ")
    if a =="1":
        import fileenc
        print("Files Encrypted...")
        sleep(2)
        secim()
    elif a == "2":
        import filedecc
        print("Files DEcrypted...")
        sleep(2)
        secim()


def secim():
    while True:
        y = """
          >  1)  HASH               >  10)  CHACHA20POLY1305
          >  2)  RSA                >  11)  TRANSPOSITION
          >  3)  XOR                >  12)  DIFFIE HELMAN
          >  4)  AES (ECC)          >  13)  IMAGE ENCRYPT/DECRYPT
          >  5)  AES (CBC)          >  14)  FILE ENCRYPT/DECRYPT
          >  6)  DES (ECB)          >  15)  EXIT
          >  7)  FERNET            
          >  8)  RC2                
          >  9)  RC4               
             """
        print(y)
        choose = input("---->PLEASE CHOOSE ENCRYPTION METHOD :")
        if choose == '1':
            hashh()
        elif choose == '2':
            rsaa()
        elif choose == '3':
            xorr()
        elif choose == '4':
            aess()
        elif choose == '5':
            aessc()
        elif choose == '6':
            dese()
        elif choose == '7':
            desc()
        elif choose == '8':
            rc22()
        elif choose == '9':
            rc44()
        elif choose == '10':
            efss()
        elif choose == '11':
            tlss()
        elif choose == '12':
            diffiee()
        elif choose == '13':
            imgenc()
        elif choose == '14':
            fileenc()
        elif choose == '15':
            print("Exiting...")
            sys.exit()
        else:
            print("Wrong Choose!!!!")


secim()
