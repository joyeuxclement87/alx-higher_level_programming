#!/usr/bin/python3
"""Defination for square"""


class Square:
    """represents to the sqr"""

    def __init__(self, size=0):
        """new sqr for initialize
        Args:
            size (int): Thenew sqr size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
