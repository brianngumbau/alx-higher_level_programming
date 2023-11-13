#!/usr/bin/python3
""" Module for Base class """
from json import dumps, loads
import csv


class Base:
    """Base class for the whole project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes JSON representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as k:
            k.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as k:
            return [cls.create(**d) for d in cls.from_json_string(k.read())]

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializez in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[i.id, i.width, i.height, i.x, i.y]
                             for i in list_objs]
            else:
                list_objs = [[i.id, i.size, i.x, i.y]
                             for i in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as k:
            writer = csv.writer(k)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializez in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as k:
            reader = csv.reader(k)
            for row in reader:
                row = [int(o) for o in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the rectangles and squares"""
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for n in list_rectangles + list_squares:
            l = turtle.Turtle()
            l.color((randrange(255), randrange(255), randrange(255)))
            l.pensize(1)
            l.penup()
            l.pendown()
            l.setpos((n.x + l.pos()[0], n.y - l.pos()[1]))
            l.pensize(10)
            l.forward(n.width)
            l.left(90)
            l.forward(n.height)
            l.left(90)
            l.forward(n.width)
            l.left(90)
            l.forward(n.height)
            l.left(90)
            l.end_fill()

        time.sleep(5)
