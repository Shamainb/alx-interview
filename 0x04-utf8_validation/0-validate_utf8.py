#!/usr/bin/python3


def validUTF8(data):
    def get_num_of_bytes(byte):
        if byte & 0b10000000 == 0:
            return 1
        elif byte & 0b11100000 == 0b11000000:
            return 2
        elif byte & 0b11110000 == 0b11100000:
            return 3
        elif byte & 0b11111000 == 0b11110000:
            return 4
        else:
            return -1

    i = 0
    while i < len(data):
        num_of_bytes = get_num_of_bytes(data[i])
        if num_of_bytes == -1 or i + num_of_bytes > len(data):
            return False
        for j in range(1, num_of_bytes):
            if data[i + j] & 0b11000000 != 0b10000000:
                return False
        i += num_of_bytes

    return True
