#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    Prevent the user for creating new instance
    for anything but attribute caled 'first_name'.
    """

    __slots__ = ["first_name"]
