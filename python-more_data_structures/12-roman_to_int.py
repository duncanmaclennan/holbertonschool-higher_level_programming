#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for char in reversed(roman_string):
        current_value = roman_dict[char]

        if current_value < prev_value:
            integer_value -= current_value
        else:
            integer_value += current_value

        prev_value = current_value

    return integer_value
