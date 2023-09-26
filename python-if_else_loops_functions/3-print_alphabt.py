#!/usr/bin/python3

# Loop through the ASCII values of the lowercase alphabet (97-122)
for i in range(97, 123):
    # Skip the ASCII value for 'q' (113) and 'e' (101)
    if i != 113 and i != 101:
        print("{:s}".format(chr(i)), end="")
