#!/usr/bin/python3
for value in range(97, 123):
    if value != 101 and value != 113:
        print("{:s}".format(chr(value)), end="")
