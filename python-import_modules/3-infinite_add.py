#!/usr/bin/python3

import sys

# Define the 'main' function to perform the addition of all command-line arguments


def main():
    # Initialize a variable to hold the sum of all arguments
    total_sum = 0

    # Loop through each argument, starting from index 1 (ignoring the script name)
    for i in range(1, len(sys.argv)):
        # Cast each argument to integer and add it to the total_sum
        total_sum += int(sys.argv[i])

    # Print the final sum
    print(total_sum)


# Ensure the code is not executed when imported
if __name__ == "__main__":
    main()
