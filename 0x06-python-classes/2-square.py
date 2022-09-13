#!/usr/bin/python3
"""class Square that defines a square by:
Private instance attribute: size.
Instantiation with optional size.
"""


class Square:
    """Initializes the data."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
