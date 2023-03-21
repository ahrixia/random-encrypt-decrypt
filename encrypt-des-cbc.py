import base64
from Crypto.Cipher import DES

def encrypt_message(message, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_message = message + (8 - (len(message) % 8)) * chr(8 - len(message) % 8)
    encrypted_message = cipher.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(encrypted_message)

# Example usage:
message = "PLAINTEXT-STRING"
key = b'KEY-STRING'
iv = b'IV-STRING'
encrypted_message = encrypt_message(message, key, iv)
print(encrypted_message)
