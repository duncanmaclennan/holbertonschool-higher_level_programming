#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    # Validate that the index is not negative and within range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list without the element at index idx
    my_list = my_list[:idx] + my_list[idx + 1:]

    return my_list
