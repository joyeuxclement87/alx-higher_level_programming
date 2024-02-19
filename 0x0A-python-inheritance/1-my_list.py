#!/usr/bin/python3
"""defining my class of inhertance"""


class MyList(list):
    """sorted built-in list class"""

    def print_sorted(self):
        """printing them in ordered lisy"""
        print(sorted(self))
