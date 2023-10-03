#!/usr/bin/python3

def multiple_returns(sentence):

    # Calculate the length of the sentence
    length = len(sentence)

    # Determine the first character or set to None if the sentence is empty
    first_char = sentence[0] if length > 0 else None

    # Return a tuple containing the length and first character
    return (length, first_char)
