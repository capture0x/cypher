import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

plaintext = input("Secret Message :")
key = get_random_bytes(32)
print("Your Key :", str(key)[2:-1])
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext.encode())

nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ciphertext).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
print(result)
