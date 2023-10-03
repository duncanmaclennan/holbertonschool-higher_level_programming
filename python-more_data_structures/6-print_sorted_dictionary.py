#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary and store them in a list
    sorted_keys = sorted(a_dictionary.keys())

    # Loop through the sorted list of keys
    for key in sorted_keys:
        # Print the key and its corresponding value
        print("{}: {}".format(key, a_dictionary[key]))
