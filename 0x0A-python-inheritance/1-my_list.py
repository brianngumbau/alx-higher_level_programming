#!/usr/bin/python3

class MyList(list):
    """Class that inherits from list"""
    pass

    def print_sorted(self):
        """Method that prints sorted list"""

        print(sorted(list(self)))
