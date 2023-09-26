#!/usr/bin/python3

def islower(c):
    # Get ASCII value of character using ord()
    ascii_value = ord(c)

    # Check if ASCII value is within the range of lowercase alphabets
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False
