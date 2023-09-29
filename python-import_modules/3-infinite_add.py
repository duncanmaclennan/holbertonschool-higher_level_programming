#!/usr/bin/python3

import sys


def main():

    total_sum = 0

    for i in range(1, len(sys.argv)):

        total_sum += int(sys.argv[i])

    print(total_sum)


if __name__ == "__main__":
    main()
