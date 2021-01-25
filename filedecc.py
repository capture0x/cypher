import os
from cryptography.fernet import Fernet

key= input("PLease enter your key :")
cipKey = Fernet(key)

def decryptt(files):
    with open(files, "rb") as readFile:
        radFile = readFile.read()
    with open(files, "wb") as writeFile:
            deccc = cipKey.decrypt(radFile)
            writeFile.write(deccc)


def filedec():
    a = input("Enter files path :")
    os.chdir(a)
    for path, bos, files in os.walk(a):
        for dosya in files:
            dosyaYolu = path + os.sep + dosya
            decryptt(dosyaYolu)
            os.renames(dosya,dosya.replace(".wrr",""))

filedec()