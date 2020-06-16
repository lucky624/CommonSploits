import hashlib
import rsa
import base64

#base64
a = base64.b64encode(bytes('complex string: Привет всем', "utf-8"))
b = base64.b64decode(a).decode("utf-8", "ignore")
print(bytes(a).decode())
print(b)

#md5_encrypt
m = hashlib.md5()
m.update("123qwe".encode())
print(m.hexdigest())

#byte xor
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
print(byte_xor(b'kek', b'fuck'))

#string xor
def string_xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
print(string_xor('kek','fuck').encode())

#sha256_encrypt
def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()
print(hash_string('123qwe'))

#rsa_encrypt
pubkey, prikey = rsa.newkeys(256)
message = b'Hello World'
enMessage = rsa.encrypt(message, pubkey)

#rsa_decrypt
message = rsa.decrypt(enMessage, prikey)
print(message)

