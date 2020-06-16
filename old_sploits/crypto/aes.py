from old_sploits.crypto import rotate
from old_sploits.crypto import get_bits_array, get_byte_from_bits
from old_sploits.lib.sblib import SB, invSB
from old_sploits.lib.srlib import SR, invSR
from old_sploits.lib.mclib import MC, invMC
from old_sploits.lib.vlib import V
import numpy as np

R_CON = (0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
         0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39,
         0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
         0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
         0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
         0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
         0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b,
         0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
         0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
         0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
         0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
         0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
         0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
         0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63,
         0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd,
         0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d)


def add_round_key(n, round_key, state):
    for i in range(0, 128):
        state[i] ^= round_key[n * 128 + i]
    return state


def get_s_box_item(index):
    row = int(index / 16)
    col = index % 16
    arr = SB[row][col:col + 8]
    return get_byte_from_bits(arr)


def key_expand(key, nr, nk):
    expanded = [k for k in key]
    tmp = [0] * 4
    r_con_iter = 1

    size = nk * 4

    expanded_key_size = (nr + 1) * 16
    current_size = size

    while current_size < expanded_key_size:

        for i in range(4):
            tmp[i] = expanded[(current_size - 4) + i]

        if current_size % size == 0:
            tmp = rotate(tmp)
            for i in range(4):
                tmp[i] = get_s_box_item(tmp[i])

            tmp[0] = tmp[0] ^ R_CON[r_con_iter]
            r_con_iter += 1

        if current_size % size == 16 and size == 32:
            for i in range(4):
                tmp[i] = get_s_box_item(tmp[i])

        for i in range(4):
            expanded.append(expanded[current_size - size] ^ tmp[i])
            current_size += 1

    expanded_bits = []

    for i in range(0, 240):
        expanded_bits += get_bits_array(expanded[i])

    return expanded_bits


def valid_key(key_size):
    return key_size == 256


def init(block, key):
    key = [ord(k) for k in key]
    key_size = len(key) * 8

    state = [ord(b) for b in block]
    bits = []

    for s in state:
        bits += get_bits_array(s)

    state = bits

    nk = key_size // 32
    nr = nk + 6

    round_key = key_expand(key, nr, nk)

    return state, round_key, nr


def get_string_from_bytes(state):
    return ''.join(chr(e) for e in state)


def sub_bytes(state):
    state = SB.dot(state) % 2
    state = np.add(state, V) % 2
    return state


def shift_rows(state):
    state = SR.dot(state) % 2
    return state


def mix_columns(state):
    state = MC.dot(state) % 2
    return state


def encrypt_block(block, key):
    state, round_key, nr = init(block, key)
    state = add_round_key(0, round_key, state)

    for i in range(1, nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(i, round_key, state)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(nr, round_key, state)

    blocks = [state[i:i + 8] for i in range(0, len(state), 8)]

    cipher_bytes = []

    for block in blocks:
        byte = get_byte_from_bits(block)
        cipher_bytes.append(byte)

    return get_string_from_bytes(cipher_bytes)


def inv_mix_columns(state):
    state = (invMC.dot(state) % 2).tolist()
    return state


def inv_shift_rows(state):
    state = (invSR.dot(state) % 2).tolist()
    return state


def inv_sub_bytes(state):
    state = (np.add(state, V) % 2).tolist()
    state = (invSB.dot(state) % 2).tolist()
    return state


def decrypt_block(block, key):
    state, round_key, nr = init(block, key)
    state = add_round_key(nr, round_key, state)

    for i in range(nr - 1, 0, -1):
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(i, round_key, state)

    state = inv_mix_columns(state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(0, round_key, state)

    blocks = [state[i:i + 8] for i in range(0, len(state), 8)]

    plain_bytes = []

    for block in blocks:
        byte = get_byte_from_bits(block)
        plain_bytes.append(byte)

    return get_string_from_bytes(plain_bytes)

