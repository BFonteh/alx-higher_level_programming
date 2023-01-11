#!/usr/bin/python3
"""Module 0-lookup"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return list(dir(obj))
