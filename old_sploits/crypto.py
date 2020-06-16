from Crypto.Cipher import DES
import base64

key = '14276231'.encode()


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)
text = '800JCW51X23F5B94S61DJVBLLTNE42D6='.encode()
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

base = 'J3ECI7aQjMN4x3tVTjd9RLxoDdeBrZZez9KsXFSRGWI='
b = base64.b64decode(base)
print(b)

data = des.decrypt(b)
print(data)



