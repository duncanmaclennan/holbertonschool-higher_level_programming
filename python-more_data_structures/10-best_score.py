#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is None or empty; if so, return None
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    # Initialize variables to store the best score and the corresponding key
    best_value = None
    best_key = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # If this is the first iteration or the value is greater than the best_value so far,
        # update best_value and best_key
        if best_value is None or value > best_value:
            best_value = value
            best_key = key

    # Return the key with the highest value
    return best_key
