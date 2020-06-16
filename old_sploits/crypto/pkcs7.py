def encode(bytestring, k=16):
    l = len(bytestring)
    val = k - (l % k)
    return bytestring + bytearray([val] * val)


def decode(bytestring, k=16):
    val = bytestring[-1]
    if val > k:
        raise ValueError('Input is not padded or padding is corrupt')
    l = len(bytestring) - val
    return bytestring[:l]