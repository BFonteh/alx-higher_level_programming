#!/usr/bin/python3
"""Module 1-my_list inherits the list class"""


class MyList(list):
    """extends class list"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
