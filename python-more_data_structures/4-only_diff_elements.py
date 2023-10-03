#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Find the elements that are unique to each set
    unique_elements = set_1 ^ set_2

    return unique_elements
