#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines a rectangle by: (based on 0-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults at 0.
            height (int, optional): height of rectangle. Defaults at 0.
        """
        self_height = height
        self_width = width

    @property
    def width(self):
        """retrieves width

        Returns:
            int: width of the rectangle.
        """
        return self_width

    @property
    def height(self):
        """retrieves height

        Returns:
            int: height of the rectangle.
        """
        return self_height

    @width.setter
    def width(self, value):
        """Property setter for width

        Args:
            value (int): width

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self_width = value

    @height.setter
    def height(self, value):
        """Property setter for height

        Args:
            value (int): height

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self_height = value
