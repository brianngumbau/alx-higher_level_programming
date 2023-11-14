#!/usr/bin/python3
"""Modele for class Square that inherits from rectangle"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Class square that inherits from rectangle

    Uses super-superclass `Base` __init__ to create valid instance id,
    and passes args to superclass `__init__` to set attributes. Does not
    create its own attributes. `size` acts as alias for `width`/`height`.

    Args:
        size : x and y dimensions of square
        x : width of square
        y : height of square
        id : identifer for each instance of super()

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string with numeric representation of square

        Returns:
            '[Square] (<id>) <x>/<y> - <size>'
        """
        return ('[Square] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}'.format(self.y, self.width))

    @property
    def size(self):
        """size getter

        Returns:
            __size : x and y dimensions of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter

        Args:
            value : x and y dimensions of square

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns attributes

        Args :
            id : identifer for each instance of super()
            size : x and y dimensions of square
            x : width of rectangle
            y : height of rectangle

        Keyword args:
            any of the above if key matches arg name

        Raises:
            TypeError: if amount of consecutive non-keyword or keyword
                arguments given not between 1 and 4
            KeyError: if keyword not among superclass and super-superclass
                getters

        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 4:
                raise TypeError('Square.update() takes 1 to 4 keyword,' +
                                ' or 1 to 4 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        if self.id != value:
                            temp = self.id
                            self.id = value
                            Base._Base__assigned_ids.remove(temp)
                            Base._Base__assigned_ids.add(value)
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 4:
            raise TypeError('Square.update() takes 1 to 4 keyword,' +
                            ' or 1 to 4 non-keyword arguments')
        else:
            for k, arg in enumerate(args):
                if k == 0:
                    if self.id != arg:
                        temp = self.id
                        self.id = arg
                        Base._Base__assigned_ids.remove(temp)
                        Base._Base__assigned_ids.add(arg)
                elif k == 1:
                    self.size = arg
                elif k == 2:
                    self.x = arg
                elif k == 3:
                    self.y = arg

    def to_dictionary(self):
        """returns dictionary representation of rectangle

        Returns:
            self_dict (dict): dictionary of private attribute values

        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['size'] = self.size
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
