#!/use_/bin/python3
"""Rectangle class model"""
from models.base import Base


class Retangle(Base):
    """Represents a rectangle
    Private instance attributes:
    - width
    - height
    - x
    - y
    inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle instance
        Args:
        - width: width of rectangle
        - height: heigt of rectangle
        - x: coordinates
        - y: coordinates
        - id: rectangle identifier
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """getter for width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for width of rectangle"""
            if type(value) is not int:
                raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be > than 0")
        self.__width = value

        @property
        def height(self):
            """getter for height of rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for height of rectangle"""
            if type(value) is not int:
                raise TypeError("Value must be an integer")
            if value is <= 0:
                raise ValueError("Value must be > than 0")
            self.__height = value

        @property
        def x(self):
            """getter for x coordinate of rectangle"""
            return: self.__x

        @x.setter
        def x(self, value):
            """setter for x coordinates of rectangle"""
            if type(value) is not int:
                raise TypeError("Value must be an integer")
            if value is < 0:
                raise ValueError("Value must be >= than 0")
            self.__x = value

        @property
        def y(self):
            """getter for y coordinate of rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("Value must be an integer")
            if value is < 0:
                raise ValueError("Value must be >= than 0")
            self.__y = value

        def area(self):
            """area function for a rectangle"""
            return self.width * self.height

        def display(self):
            """prints in stdout the rectangle instance
            with the character #
            """
            for y in range(0, self.__y):
                print()
            for height in range(0, self.__height):
                for x in range(0, self.__x):
                    print(" ", end="")
                for width in range(0, self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            """Returns the string representation of rectangular instance"""
            s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
            return s

        def update(self, *args):
            """assigns an argument to each attribute
            Args:
                - 1st - id attribute
                - 2nd - width attribute
                - 3rd - height attribute
                - 4th - x attribute
                - 5th - y attribute
            """

            if args is not None and len(args) is not 0:
                if len(args) >= 1:
                    if type(args[0]) is not int and args[0] is not None:
                        raise TypeError("id must be an integer")
                    self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]
                else:
                    for key, value in kwargs.items():
                        if key == "id":
                            if type(value) is not int and value is not None:
                                raise TypeError("Value must be an integer")
                            self.id = value
                        if key == "width":
                            self.width = value
                        if key == "height":
                            self.height = value
                        if key == "x":
                            self.x = value
                        if key == "y":
                            self.y = value

        def to_dictionary(self):
            """Returns the dictionary representation of a rectangle"""
            return {
                    'id': self.id,
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y
                   }
