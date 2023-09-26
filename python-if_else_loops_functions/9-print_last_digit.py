#!/usr/bin/python3

def print_last_digit(number):
    # Use the modulo operator to get the last digit
    last_digit = abs(number) % 10

    # Print the last digit
    print("{}".format(last_digit), end="")

    # Return the last digit
    return last_digit
