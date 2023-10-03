#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    # Initialize an empty list to hold the results
    result = []

    # Iterate through the list of integers
    for num in my_list:
        # Append True to the result list if the number is divisible by 2,
        # otherwise append False
        result.append(num % 2 == 0)

    return result
