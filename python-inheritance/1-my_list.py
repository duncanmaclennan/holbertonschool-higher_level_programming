#!/usr/bin/python3
""" MyList module"""


class MyList(list):
    """define MyList subclass """

    def print_sorted(self):
        print(sorted(self))
