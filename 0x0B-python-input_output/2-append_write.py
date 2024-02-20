#!/usr/bin/python3
"""ile-appending function."""


def append_write(filename="", text=""):
    """str to the end of a UTF8 text file to be appended.

    Args:
        filename (str): file name.
        text (str): str file.
    Returns:
        chars nums
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
