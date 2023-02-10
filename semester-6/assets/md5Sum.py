import struct
import math

def leftrotate(i, n):
    return ((i << n) & 0xffffffff) | (i >> (32 - n))

def md5(message):
    message = bytearray(message, 'ascii')
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += struct.pack('<Q', orig_len_in_bits)
    hash_pieces = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
    for chunk_ofst in range(0, len(message), 64):
        a, b, c, d = hash_pieces
        chunk = message[chunk_ofst:chunk_ofst+64]
        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16
            to_rotate = a + f + 0x100000000 * chunk[4 * g] + \
                        0x100 * chunk[4 * g + 1] + \
                        0x1 * chunk[4 * g + 2] + \
                        chunk[4 * g + 3]
            new_b = (b + leftrotate(to_rotate, [7, 12, 17, 22, 7, 12, 17, 22,
                                                7, 12, 17, 22, 7, 12, 17, 22,
                                                5, 9, 14, 20, 5, 9, 14, 20,
                                                5, 9, 14, 20, 5, 9, 14, 20,
                                                4, 11, 16, 23, 4, 11, 16, 23,
                                                4, 11, 16, 23, 4, 11, 16, 23,
                                                6, 10, 15, 21, 6, 10, 15, 21,
                                                6, 10, 15, 21, 6, 10, 15, 21][i])) & 0xffffffff
            a, b, c, d = d, new_b, b, c
        for i, val in enumerate([a, b, c, d]):
            hash_pieces[i] += val
            hash_pieces[i] &= 0xffffffff
    return sum(x << (32 * i) for i, x in enumerate(hash_pieces[::-1]))

def md5_hex(message):
    return '{:x}'.format(md5(message))


print(md5_hex("A"))