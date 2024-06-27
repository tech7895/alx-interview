#!/usr/bin/python3
"""
This script determines if given data
represents valid utf8.
"""


def validUTF8(data):
    """
    Return true if data is valid utf with chars 1-4 bytes long, data set can
    contain multiple chars data will be represented by a list of ints, each
    int reps 1 byteof data, only need to handle the 8 least
    significant bits of each integer
    """

    num_bytes = 0

    for number in data:
        bin_reslt = format(number, '#010b')[-8:]

        if num_bytes == 0:
            for bit in bin_reslt:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bin_reslt[0] == '1' and bin_reslt[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
