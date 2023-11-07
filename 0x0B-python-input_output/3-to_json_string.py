#!/usr/bin/python3
"""
3-to_json_string module
"""
import json


def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation of an object (string):
    Args:
        my_obj: string
    Return: json representation of an object
    """
    return json.dumps(my_obj)
