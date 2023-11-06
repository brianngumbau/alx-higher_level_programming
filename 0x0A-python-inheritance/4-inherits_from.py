#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Method that returns True if the object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
