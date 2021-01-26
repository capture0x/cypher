def descc_func():
    import base64
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    try:
        mes = input("Secret Message :")
        password = input("Key :")
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = kdf.derive(password.encode())
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        kdf.verify(password.encode(), key)

        key = base64.urlsafe_b64encode(key)
        fernet = Fernet(key)
        token = fernet.encrypt(mes.encode())
        print("Encrypted :",str(token)[2:-1])
        ccc=fernet.decrypt(token)
        print("Decrypted :",str(ccc)[2:-1])
    except:
        print("Wrong Value..!")
