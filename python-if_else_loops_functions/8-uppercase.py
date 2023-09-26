#!/usr/bin/python3

def uppercase(str):
    result = ""
    # Iterate through each character in the string
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from ASCII value
            result += chr(ord(char) - 32)
        else:
            # If not lowercase, keep the character as is
            result += char

    # Print the converted string followed by a newline
    print("{}".format(result))
