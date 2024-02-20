#!/usr/bin/python3
"""function to define text file reading"""


def read_file(filename=""):
    """contents of UTF8 text file to stdout. will be printed"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
