#!/usr/bin/python3

def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is out of range
    if idx >= len(my_list):
        return None

    return my_list[idx]
