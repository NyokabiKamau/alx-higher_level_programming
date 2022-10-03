#!/usr/bin/python3
"""Square class model and inherits from Rectangle"""

from model.base import Base
from model.rectangle import Rectangle


class Square:
    """class describing a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing a square
        Args:
            - size: size
            - x: x coordinates
            - y: y coordinates
            - id: square identifier
        """

        self.size = size
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """returns string representation of a square instance"""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.__x,
                                                     self.__y, self.__width)

        @property
        def size(self):
            """getter of size attribute"""
            return self.width

        @size.setter
        def size(self, value):
            """setter of size attribute"""
            if type(value) is not int:
                raise TypeError("Width must be an integer")
            if value <= 0:
                raise ValueError("Width must be > 0")
            self.size = width
            self.height = height

        def update(self, *args, **kwargs):
            """updates attributes of an instance
            Args:
                - 1st: id attribute
                - 2nd: size attribute
                - 3rd: x attribute
                - 4th: y attribute
            """
            if args is not None and len(args) != 0:
                if len(args) >= 1:
                    if type(args[0]) is not int and args[0] is not None:
                        raise TypeError("id must be an integer")
                    self.id = arg[0]
                if len(args) > 1:
                    self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                if len(args) > 3:
                    self.y = args[3]
                else:
                    for key, value in kwargs.items():
                        if key == "id":
                            if type(value) is not int and value is not None:
                                raise TypeError("id must be an integer")
                            self.id = value
                        if key == "size":
                            self.size = value
                        if key == "x":
                            self.size = value
                        if key == "y":
                            self.size = value

        def to_dictionary(self):
            """Returns the dictionary representation of a square"""
            return {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                    }
