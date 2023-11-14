#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits from base

    superclass '__init__' 

    Args:
        width : x dimension of rectangle
        height : y dimension of rectangle
        x : width of rectangle
        y : height of rectangle
        id : identifier for each instance of super
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, att, value):
        """Method to validate all setter methods and instantiation

        Args:
            att : name of attribute
            value : input expected

        Raises:
            TypeError: if value is not int
            ValueError: if `width` or `height` is <= 0, or if
                `x` or `y` is < 0

        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(att))
        if att == 'width' or att == 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(att))
        elif att == 'x' or att == 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(att))

    @property
    def width(self):
        """width getter

        Returns:
            __width : x dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value : x dimension of rectangle

        Attributes:
            __width : x dimension of rectangle

        """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            __height : y dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value : y dimension of rectangle

        Attributes:
            __height : y dimension of rectangle

        """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """__x getter

        Returns:
            __x : width of rectangle

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Args:
            value : width of rectangle

        Attributes:
            __x : width of rectangle
        """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """__y getter

        Returns:
            __y : height of rectangle

        """
        return self.__y

    @y.setter
    def y(self, value):
        """Args:
            value : height of rectangle

        Attributes:
            __y : height of rectangle

        """
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """Returns area of rectangle

        Returns:
            `__width` * `__height`
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout rectangle instance with character #

        Attributes:
            display : ACSII art for rectangle
            __display (str): final value of `display` saved to instance 
            for unit testing
        """
        display = ''
        for row in range(self.y):
            display += '\n'
        for row in range(self.height):
            for column in range(self.x):
                display += ' '
            for column in range(self.width):
                display += '#'
            if row < self.height - 1:
                display += '\n'
        self.__display = display
        print(display)

    def __str__(self):
        """Returns string with numeric representation of rectangle

        Returns:
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'

        """
        return ('[Rectangle] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}/{:d}'.format(self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute

        Args :
            id : identifer for instances of `super()`
            width : x dimension of rectangle
            height : y dimension of rectangle
            x : width of rectangle
            y : height of rectangle

        Keyword args:
            any of the above if key matches arg name

        Raises:
            TypeError: if amount of arguments given is not between 1 and 5
            KeyError: if keyword not among class and superclass getters

        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 5:
                raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                                ' or 1 to 5 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                        Base._Base__assigned_ids.add(value)
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 5:
            raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                            ' or 1 to 5 non-keyword arguments')
        else:
            for k, arg in enumerate(args):
                if k == 0:
                    if self.id != arg:
                        self.id = arg
                        Base._Base__assigned_ids.add(arg)
                elif k == 1:
                    self.width = arg
                elif k == 2:
                    self.height = arg
                elif k == 3:
                    self.x = arg
                elif k == 4:
                    self.y = arg

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle
        Returns:
            self_dict : dictionary of private attribute values
        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['width'] = self.width
        self_dict['height'] = self.height
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
