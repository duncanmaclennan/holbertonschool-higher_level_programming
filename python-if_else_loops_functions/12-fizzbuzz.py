#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        # Check if i is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        # Check if i is a multiple of 3
        elif i % 3 == 0:
            print("Fizz", end=' ')
        # Check if i is a multiple of 5
        elif i % 5 == 0:
            print("Buzz", end=' ')
        # Otherwise, print the number itself
        else:
            print(i, end=' ')
