import base64
from Crypto.Cipher import DES

def MD5DecryptDal(pToDecrypt):
    key = b'KEY-STRING'
    iv = b'IV-STRING'
    
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted_data = bytes.fromhex(pToDecrypt)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')

encrypted_string = 'ENCRYPTED-STRING'
decrypted_string = MD5DecryptDal(encrypted_string)
print(decrypted_string)
