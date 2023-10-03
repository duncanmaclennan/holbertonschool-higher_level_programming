#!/usr/bin/python3

def no_c(my_string):

    # Initialize an empty string to store the result
    new_string = ''

    # Iterate through each character in the original string
    for char in my_string:
        # Add the character to the new string if it's not 'c' or 'C'
        if char not in ['c', 'C']:
            new_string += char

    return new_string
