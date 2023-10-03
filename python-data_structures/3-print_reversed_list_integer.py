#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order.

    Args:
        my_list (list): The list of integers.

    Returns:
        None
    """
    # Iterate through the list in reverse order
    for i in reversed(my_list):
        # Print each integer using str.format()
        print("{:d}".format(i))
