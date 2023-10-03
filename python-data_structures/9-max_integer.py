#!/usr/bin/python3

def max_integer(my_list=[]):

    # Initialize a variable to hold the maximum value. Set it to None initially.
    max_val = None

    # Iterate through the list
    for num in my_list:
        # If max_val is None (which means it's the first iteration),
        # or if the current number is greater than max_val,
        # update max_val
        if max_val is None or num > max_val:
            max_val = num

    return max_val
