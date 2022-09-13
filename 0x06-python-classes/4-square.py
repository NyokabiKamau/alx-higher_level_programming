#!/usr/bin/python3
"""class Square that defines a square by:
Private instance attribute: size:
- property def size(self)
- property setter def size(self, value)
Instantiation with optional size.
Public instance method: def area(self).
"""


class Square:
    """Initializes the data."""
    def __init__(self, size=0):
        self.__size = size

    @property
    """Retrieves the size."""
    def size(self):
        return self.__size

    @size.setter
    """Sets the size to a value."""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Returns the current square area."""
    def area(self):
        return self.__size ** 2
