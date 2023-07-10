from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad


salt = b'\xb5\xba\xffn\x81\x01R\x86\xfaid0\xf4U\x8e\xfd\xaf))\xd9B\\.\x14\xdb\x06Z\x9a\x009\x19\xd3'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"bom dia"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print (ciphered_data)

with open ('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)


with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)



with open ('key.bin', 'wb') as f:
    f.write(key)





