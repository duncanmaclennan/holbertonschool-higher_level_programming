#!/usr/bin/python3

# Initialize an empty string to store the alphabet
alphabet_str = ""

# Loop through the ASCII values of the lowercase alphabet (97-122)
for i in range(97, 123):
    # Append the character corresponding to the ASCII value to alphabet_str
    alphabet_str += chr(i)

# Print the complete alphabet string without a new line
print(alphabet_str, end="")
