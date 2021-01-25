from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from secrets import token_bytes


class DiffieHellman:
    def __init__(self):
        self.diffieHellman = ec.generate_private_key(ec.SECP384R1(), default_backend())
        self.public_key = self.diffieHellman.public_key()
        self.IV = token_bytes(16)

    def encrypt(self, public_key, secret):
        shared_key = self.diffieHellman.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=default_backend()
        ).derive(shared_key)

        aes = Cipher(algorithms.AES(derived_key), modes.CBC(self.IV), backend=default_backend())
        encryptor = aes.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(secret.encode()) + padder.finalize()
        return encryptor.update(padded_data) + encryptor.finalize()

    def decrypt(self, public_key, secret, iv):
        shared_key = self.diffieHellman.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=default_backend()
        ).derive(shared_key)

        aes = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
        decryptor = aes.decryptor()
        decrypted_data = decryptor.update(secret) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(decrypted_data) + unpadder.finalize()


try:
    print('ENCRYPTION')
    text = input("Secret Message :")
    aaaa = DiffieHellman()
    bbbb = DiffieHellman()
    encrypted_message = bbbb.encrypt(aaaa.public_key, text)
    print(str(encrypted_message)[2:-1])

    print('\nDECRYPTION')
    decrypted_message = aaaa.decrypt(bbbb.public_key, encrypted_message, bbbb.IV)
    print(str(decrypted_message)[2:-1])
except:
    print("Wrong Value..!")
