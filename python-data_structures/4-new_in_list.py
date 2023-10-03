#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of the original list using slicing
    new_list = my_list[:]

    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Replace the element at the given index in the new list
        new_list[idx] = element

    return new_list
