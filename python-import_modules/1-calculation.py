#!/usr/bin/python3

# Import the necessary functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define the 'main' function to perform calculations and print the results


def main():
    # Assign the value 10 to the variable 'a'
    a = 10

    # Assign the value 5 to the variable 'b'
    b = 5

    # Perform the calculations using the imported functions and store the results
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    # Print the results
    print("{} + {} = {}".format(a, b, addition_result))
    print("{} - {} = {}".format(a, b, subtraction_result))
    print("{} * {} = {}".format(a, b, multiplication_result))
    print("{} / {} = {}".format(a, b, division_result))


# Ensure the code is not executed when imported
if __name__ == "__main__":
    main()
