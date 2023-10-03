#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_set = set(my_list)

    # Calculate the sum of all unique integers
    sum_unique = sum(unique_set)

    return sum_unique
