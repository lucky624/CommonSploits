from itertools import cycle

a = [16, 32, 48]

ciphertext = [0x5b,0x13,0x49,0x77,0x13,0x5e,0x7d,0x13]

for i, j in zip(ciphertext, cycle(a)):
    print(chr(j ^ i), end="")