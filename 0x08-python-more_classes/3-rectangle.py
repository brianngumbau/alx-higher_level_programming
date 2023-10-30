#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines a rectangle by: (based on 2-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle, defaults at 0.
            height (int, optional): height of rectangle, defaults at 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieves width

        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """retrieves height

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns area of a rectangle.

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns perimeter of a rectangle

        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with #

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for n in range(self.__height):
            for k in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)
