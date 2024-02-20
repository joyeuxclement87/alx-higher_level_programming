#!/usr/bin/python3
"""text file insertion function to be define."""


def append_after(filename="", search_string="", new_string=""):
    """to insert text after each line.

    Args:
        filename (str): file name
        search_string (str): str file to be search
        new_string (str): inserted str
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
