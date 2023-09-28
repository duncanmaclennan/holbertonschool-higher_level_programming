#!/usr/bin/python3

import sys

# Define the 'main' function to handle arguments and print the output


def main():
    argv = sys.argv
    arg_count = len(argv) - 1  # Exclude the script name itself

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg_count))
        for i in range(1, arg_count + 1):
            print("{}: {}".format(i, argv[i]))


# Ensure the code is not executed when imported
if __name__ == "__main__":
    main()
