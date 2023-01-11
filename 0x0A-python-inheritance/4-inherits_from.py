#!/usr/bin/python3
"""
Checks if obj is instance of a class that
inherited from another specified class
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class else False """
    return isinstance(obj, a_class) and type(obj) != a_class
