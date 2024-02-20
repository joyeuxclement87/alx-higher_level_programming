#!/usr/bin/python3
"""file-writing function."""


def write_file(filename="", text=""):
    """str to write for a UTF8 text file.

    Args:
        filename (str): file name
        text (str): text for file
    Returns:
        chars writen
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
