#!/usr/bin/python3
"""file-appending function."""


def append_write(filename="", text=""):
    """str to be appended on the end of UTF8 text 
    Args:
        filename (str): file name.
        text (str): file str
    Returns:
        chars numbers
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
