from old_sploits.crypto import aes
from old_sploits.crypto import pkcs7

HEADER = "0123456789abcdef"
UTF = 'utf-8'


def add_padding(plaintext):
    return pkcs7.encode(plaintext.encode(UTF), 16).decode(UTF)


def remove_padding(plaintext):
    return pkcs7.decode(plaintext.encode(UTF), 16)


def encrypt(plaintext, key):
    plaintext = HEADER + plaintext
    padding_data = add_padding(plaintext)
    blocks = [padding_data[i:i + 16] for i in range(0, len(padding_data), 16)]

    encrypted_blocks = ""

    for i in range(0, len(blocks)):
        block = aes.encrypt_block(blocks[i], key)
        encrypted_blocks += block

    return encrypted_blocks


def decrypt(encrypted, key):
    decrypt_text = ""
    encrypted_blocks = [encrypted[i:i + 16] for i in range(0, len(encrypted), 16)]
    for i in range(0, len(encrypted_blocks)):
        block = aes.decrypt_block(encrypted_blocks[i], key)
        decrypt_text = decrypt_text + block

    return remove_padding(decrypt_text)[len(HEADER):]
