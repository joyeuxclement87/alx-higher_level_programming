#!/usr/bin/python3
"""Defination for square"""


class Square:
    """represents to the sqr"""

    def __init__(self, size=0):
        """new sqr for initialize
        Args:
            size (int): Thenew sqr size
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
