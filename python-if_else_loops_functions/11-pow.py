#!/usr/bin/python3

def pow(a, b):
    # Special case: b is zero
    if b == 0:
        return 1

    # Special case: b is negative
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    for _ in range(b):
        result *= a

    return result
