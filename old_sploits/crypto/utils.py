

def get_bits_array(num):
    bits = bin(num).lstrip('0b')
    while len(bits) < 8:
        bits = '0' + bits
    bits_array = []
    for i in range(0, 8):
        bits_array.append(int(bits[i]))
    return bits_array


def get_byte_from_bits(bits):
    b = ""
    for i in range(0, 8):
        b += str(bits[i])
    byte = int(b, 2)
    return byte


def rotate(vector):
    tmp = vector[0]

    for i in range(len(vector) - 1):
        vector[i] = vector[i + 1]

    vector[len(vector) - 1] = tmp
    return vector
